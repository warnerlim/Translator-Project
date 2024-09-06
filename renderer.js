const { ipcRenderer } = require('electron');
const EventEmitter = require('events');
const emitter = new EventEmitter();
emitter.setMaxListeners(20);

  document.getElementById('Download').addEventListener('click', () => {
      const userInput = document.getElementById('downloadInput').value;
      runPython('Download', userInput, 'downloadOutput');
    });

  document.getElementById('Transcribe').addEventListener('click', () => {
    runPython('Transcribe', null, 'transcribeOutput'); // Replace null for dynamic file naming in the future. E.g: input.mp4 would be here as it's name instead
  });

  document.getElementById('Translate').addEventListener('click', () => {
    runPython('Translate', null, 'translateOutput'); // Replace null for dynamic file naming in the future. E.g: raw_text.txt would be here as it's name instead
  });
  
  document.getElementById('Upload').addEventListener('click', () => {
    runPython('Upload', null, 'UploadOutput');
  });
  
  document.getElementById('Delete').addEventListener('click', () => {
    runPython('Delete', null, 'deleteOutput');
  });

  ipcRenderer.on('update-output', (event, message, target) => {
    document.getElementById(target).innerText += message + '\n';
  });

  // Function to run Python script
  function runPython(action, input, target) {
      ipcRenderer.send('run-python', { action, input, target });
}