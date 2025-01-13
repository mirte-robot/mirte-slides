window.addEventListener("load", (event) => {
    window.document.querySelectorAll('.button1').forEach(button => {
        button.addEventListener('click', function () {
            this.classList.toggle('pressed');
        });
    });
    window.document.querySelectorAll('.button2').forEach(button => {
        button.addEventListener('click', function () {
            this.classList.toggle('pressed');
        });
    });
    window.document.querySelectorAll('.button3').forEach(button => {
        button.addEventListener('click', function () {
            this.classList.toggle('pressed');
        });
    });
    window.document.querySelectorAll('.button4').forEach(button => {
        button.addEventListener('click', function () {
            this.classList.toggle('pressed');
        });
    });
}); 