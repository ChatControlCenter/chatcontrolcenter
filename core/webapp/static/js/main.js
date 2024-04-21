// inizializza il pulsante per copiare ID della chat
function setupCopyChatIdButton() {
    const button = document.querySelector('button#copy-chat-id');
    const span = document.querySelector('span#chat-id');

    button.addEventListener(
        'click',
        async () => await navigator.clipboard.writeText(span.textContent)
    );
}

// inizializza il pulsante salva
function setupMainButton() {
    const form = document.querySelector('form');

    Telegram.WebApp.MainButton.text = 'Salva';
    Telegram.WebApp.MainButton.onClick(async () => {
        Telegram.WebApp.MainButton.disable();
        Telegram.WebApp.MainButton.showProgress();

        const fd = new FormData(form);
        const url = new URL(window.location.href);

        const response = await fetch(url, { cache: 'no-cache', mode: 'same-origin', method: 'POST', body: fd })
            .then(response => response.json());

        Telegram.WebApp.showAlert(response.message);

        Telegram.WebApp.MainButton.enable();
        Telegram.WebApp.MainButton.hideProgress();
    });

    Telegram.WebApp.MainButton.show();
}

document.addEventListener('DOMContentLoaded', function() {
    let overlay = document.getElementById('loadingOverlay');
    overlay.style.display = 'none';

    Telegram.WebApp.expand();

    setupMainButton();
    setupCopyChatIdButton();
});
