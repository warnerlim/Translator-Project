const { ipcRenderer } = require('electron');
const EventEmitter = require('events');
const emitter = new EventEmitter();

  document.getElementById('Download').addEventListener('click', () => {
      emitter.setMaxListeners(20);
      const userInput = document.getElementById('userInput').value;
      ipcRenderer.send('run-python', { action: 'Download', input: userInput });
    });

  document.getElementById('Transcribe').addEventListener('click', () => {
    ipcRenderer.send('run-python', { action: 'Transcribe' });
  });

  document.getElementById('Delete').addEventListener('click', () => {
    ipcRenderer.send('run-python', { action: 'Delete' });
  });

  document.getElementById('Translate').addEventListener('click', () => {
    ipcRenderer.send('run-python', { action: 'Translate' });
  });

  document.getElementById('Upload').addEventListener('click', () => {
    ipcRenderer.send('run-python', 'Upload');
  });
  
  ipcRenderer.on('python-result', (event, result) => {
    document.getElementById('output').innerText = result;
  });