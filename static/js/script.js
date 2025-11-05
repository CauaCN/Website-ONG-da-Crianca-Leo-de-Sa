const mobile = document.getElementById('mobile');
const navLista = document.querySelector('#nav .nav_lista');

mobile.addEventListener('click', () => {
    const isOpen = navLista.classList.toggle('active');
    mobile.classList.toggle('open', isOpen);
    mobile.setAttribute('aria-expanded', String(isOpen));
});

const copiar = 
document.getElementById('copiar');
const chave =
document.getElementById('chave').innerText;
const msg = 
document.getElementById('Msg_copiado');

copiar.addEventListener('click', () => {
    navigator.clipboard.writeText(chave);
    msg.textContent = "Chave PIX copiada!";
    setTimeout(() => (msg.textContent = ""),3000);
});