const { contextBridge, ipcRenderer } = require('electron');

contextBridge.exposeInMainWorld('electronAPI', {
    generateVideo: (data) => ipcRenderer.invoke('generate-video', data),
    onProgress: (callback) => ipcRenderer.on('progress-update', (_event, value) => callback(value))
});
