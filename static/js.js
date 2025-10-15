// Example starter JavaScript for disabling form submissions if there are invalid fields
(() => {
  'use strict'

  // Fetch all the forms we want to apply custom Bootstrap validation styles to
  const forms = document.querySelectorAll('.needs-validation')

  // Loop over them and prevent submission
  Array.from(forms).forEach(form => {
    form.addEventListener('submit', event => {
      if (!form.checkValidity()) {
        event.preventDefault()
        event.stopPropagation()
      }

      form.classList.add('was-validated')
    }, false)
  })
})()



/*-------------------Funcion para poder mandar url del obejeto a eliminar ---------------------------------------------- */

document.addEventListener("DOMContentLoaded", function () {
    // Obtener todos los botones de eliminar
    const eliminarBtns = document.querySelectorAll('.eliminar-btn');

    eliminarBtns.forEach(btn => {
        // Agregar un listener de clic a cada boton
        btn.addEventListener('click', function () {
            // Obtener la URL de eliminar
            const actionUrl = btn.getAttribute('data-action-url');
            // Obtener el enlace de eliminacion
            const eliminarLink = document.querySelector('#eliminarLink');
            // Actualizar el atributo href del enlace de eliminar en el modal
            eliminarLink.setAttribute('href', actionUrl);
        });
    });
});

/*-------------------Funcion para poder mandar url del obejeto a eliminar ---------------------------------------------- */








/*--------------------Alerta flotante mensajes -------------------------------------------*/

// Cerrar alerta en 5 segundos
document.addEventListener('DOMContentLoaded', function(){
    setTimeout(function() {
        var alert = document.querySelector('.alert-sonner');
        if (alert) {
            alert.classList.remove('show');
        }
    }, 5000);
});

// Alerta flotante 
document.addEventListener('scroll', function () {
    const alert = document.querySelector('.alert-sonner');
    if (alert) {
        // Obtiene la posicion relativa del scroll
        const scrollTop = window.scrollY || document.documentElement.scrollTop;
        // Ajusta la posicion de la alerta segun el scroll
        alert.style.top = `${30 + scrollTop}px`;
    }
});

/*--------------------Fin Alerta flotante mensajes -------------------------------------------*/
