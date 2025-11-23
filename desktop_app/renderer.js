const generateBtn = document.getElementById('generate-btn');
const audioDrop = document.getElementById('audio-drop');

// Drag and Drop Logic
audioDrop.addEventListener('dragover', (e) => {
    e.preventDefault();
    audioDrop.style.borderColor = '#6366f1';
    audioDrop.style.backgroundColor = 'rgba(99, 102, 241, 0.1)';
});

audioDrop.addEventListener('dragleave', (e) => {
    e.preventDefault();
    audioDrop.style.borderColor = '#334155';
    audioDrop.style.backgroundColor = 'transparent';
});

audioDrop.addEventListener('drop', (e) => {
    e.preventDefault();
    audioDrop.style.borderColor = '#334155';
    audioDrop.style.backgroundColor = 'transparent';

    const files = e.dataTransfer.files;
    if (files.length > 0) {
        const file = files[0];
        console.log('File dropped:', file.path);
        audioDrop.innerHTML = `<p>✅ ${file.name}</p>`;
    }
});

// Generate Button Logic
generateBtn.addEventListener('click', async () => {
    generateBtn.disabled = true;
    generateBtn.innerText = 'PROCESANDO...';
    generateBtn.style.opacity = '0.7';

    try {
        const result = await window.electronAPI.generateVideo({
            audio: 'selected_audio.wav',
            text: 'Sample text',
            avatar: 'avatar_1.png'
        });

        if (result.success) {
            alert('Video generado con éxito en: ' + result.path);
        }
    } catch (error) {
        console.error('Error generating video:', error);
        alert('Error al generar video');
    } finally {
        generateBtn.disabled = false;
        generateBtn.innerText = 'GENERAR VIDEO (Render Local)';
        generateBtn.style.opacity = '1';
    }
});

// Settings Modal Logic
const settingsBtn = document.querySelector('.nav-item:last-child');
const modal = document.getElementById('settings-modal');
const closeBtn = document.querySelector('.close-btn');
const engineSelect = document.getElementById('engine-mode');
const remoteConfig = document.getElementById('remote-config');

settingsBtn.addEventListener('click', () => {
    modal.style.display = 'flex';
});

closeBtn.addEventListener('click', () => {
    modal.style.display = 'none';
});

engineSelect.addEventListener('change', (e) => {
    if (e.target.value === 'remote') {
        remoteConfig.style.display = 'block';
    } else {
        remoteConfig.style.display = 'none';
    }
});

// Close modal on click outside
window.addEventListener('click', (e) => {
    if (e.target === modal) {
        modal.style.display = 'none';
    }
});
