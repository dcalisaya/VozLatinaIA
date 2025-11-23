const { app, BrowserWindow, ipcMain } = require('electron');
const path = require('path');
const { spawn } = require('child_process');

let mainWindow;
let comfyProcess;

function createWindow() {
  mainWindow = new BrowserWindow({
    width: 1280,
    height: 800,
    minWidth: 1024,
    minHeight: 768,
    titleBarStyle: 'hidden',
    titleBarOverlay: {
      color: '#0f172a',
      symbolColor: '#e2e8f0',
      height: 40
    },
    webPreferences: {
      preload: path.join(__dirname, 'preload.js'),
      nodeIntegration: false,
      contextIsolation: true
    },
    backgroundColor: '#0f172a',
    show: false
  });

  mainWindow.loadFile('index.html');

  mainWindow.once('ready-to-show', () => {
    mainWindow.show();
  });

  // Open DevTools in dev mode
  // mainWindow.webContents.openDevTools();
}

function startComfyBackend() {
  // Placeholder: In production, this would spawn the portable python environment
  console.log('Starting ComfyUI Backend...');
  // comfyProcess = spawn('python', ['main.py'], { cwd: '../ComfyUI' });
}

app.whenReady().then(() => {
  createWindow();
  startComfyBackend();

  app.on('activate', function () {
    if (BrowserWindow.getAllWindows().length === 0) createWindow();
  });
});

app.on('window-all-closed', function () {
  if (process.platform !== 'darwin') app.quit();
});

app.on('will-quit', () => {
  if (comfyProcess) {
    comfyProcess.kill();
  }
});

// IPC Handlers
ipcMain.handle('generate-video', async (event, data) => {
  console.log('Received generation request:', data);
  // Simulate processing delay
  return new Promise(resolve => setTimeout(() => resolve({ success: true, path: '/path/to/video.mp4' }), 2000));
});
