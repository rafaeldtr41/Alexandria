let nombre = document.getElementById('name');
let password = document.getElementById('password');
let error = [];




function Confirmar() {
    if (nombre.value !== "maikol") {
        error.push("Usuario incorrecto");
    }
    if (password.value !== "N@tsu.1118") {
        error.push("Contraseña incorrecta");
    }
    if (error.length === 0) {
        alert("Formulario valido");
        window.location.href = "http://127.0.0.1:5500/Home.html";
    } else { alert(error); }

}
document.getElementById('Enviar').addEventListener("click", Confirmar);