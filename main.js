const { app, BrowserWindow, ipcMain } = require('electron');
const path = require('path');
const { spawn } = require('child_process');

function createWindow() {
  const win = new BrowserWindow({
    width: 800,
    height: 600,
    webPreferences: {
      preload: path.join(__dirname, 'renderer.js'),
      contextIsolation: false,
      enableRemoteModule: true,
      nodeIntegration: true
    },
  });

  win.loadFile('index.html');
  win.webContents.openDevTools();
}

app.whenReady().then(() => {
  createWindow();

  app.on('activate', () => {
    if (BrowserWindow.getAllWindows().length === 0) createWindow();
  });
});

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') {
    app.quit();
  }
});

ipcMain.on('run-python', (event, arg) => {
  const { action, input } = arg;
  const pythonProcess = spawn('python', ['script.py', action, input]);
  
  pythonProcess.stdout.on('data', (data) => {
    event.reply('python-result', data.toString());

  pythonProcess.stderr.on('data', (data) => {
    event.reply('python-result', `Error: ${data.toString()}`);
  });
  });
});