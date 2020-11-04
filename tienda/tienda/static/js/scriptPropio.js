       //Mis Funciones
       function validarEdad(){
        var edad = document.getElementById("edad").value;
            if(edad < 18){
                alert("No cumple con la edad minima para crear su cuenta")
                edad.focus();
                edad.value = "";
            }          
    }
    function min8(){
        var pass = document.getElementById("pass").value;
            if(pass.length < 8){
                alert("necesita al menos 8 caracteres en la contraseña")
                pass.focus();
            }          
    }

    function min3(){
        var nombre = document.getElementById("nombre").value;
            if(nombre.length < 3){
                alert("no cumple los caracteres minimos")
                nombre.focus();
            }          
    }

    function min3v2(){
        var apellido = document.getElementById("apellido").value;
            if(apellido.length < 3){
                alert("no cumple los caracteres minimos")
                apellido.focus();
            }          
    }


    function vaciarN(){
        var nombre =document.getElementById("nombre");
        nombre.value="";
    }

    function vaciarA(){
        var apellido =document.getElementById("apellido");
        apellido.value="";
    }

    function ConMail(){
        if (mail.value != c_mail.value) {
            document.getElementById(alert("Sus correos no son iguales")).value;
            mail.value = "";
            c_mail.value = "";
            mail.focus();
          }
    }
    function ConPass(){
        if (pass.value != c_pass.value) {
            document.getElementById(alert("Sus contraseñas no coinciden")).value;
            pass.value = "";
            c_pass.value = "";
            pass.focus();
          }
        }   



       //funciones de materialize
      document.addEventListener('DOMContentLoaded', function() {
      var elems = document.querySelectorAll('.slider');
      var instances = M.Slider.init(elems,{
      fullWidth: true,
      height:500  ,
        });
        });

         document.addEventListener('DOMContentLoaded', function() {
          M.AutoInit()});



            document.addEventListener('DOMContentLoaded', function() {
            var elems = document.querySelectorAll('.parallax');
            var instances = M.Parallax.init(elems);
            });

            //De aqui para abajo son funciones que encontre en un video que explica como filtrar productos
            //https://youtu.be/UH7Xtn4J5ZM Link del video

            $(document).ready(function(){

                // AGREGANDO CLASE ACTIVE AL PRIMER ENLACE ====================
                $('.category_list .category_item[category="all"]').addClass('ct_item-active');
            
                // FILTRANDO PRODUCTOS  ============================================
            
                $('.category_item').click(function(){
                    var catProduct = $(this).attr('category');
                    console.log(catProduct);
            
                    // AGREGANDO CLASE ACTIVE AL ENLACE SELECCIONADO
                    $('.category_item').removeClass('ct_item-active');
                    $(this).addClass('ct_item-active');
            
                    // OCULTANDO PRODUCTOS =========================
                    $('.product-item').css('transform', 'scale(0)');
                    function hideProduct(){
                        $('.product-item').hide();
                    } setTimeout(hideProduct,400);
            
                    // MOSTRANDO PRODUCTOS =========================
                    function showProduct(){
                        $('.product-item[category="'+catProduct+'"]').show();
                        $('.product-item[category="'+catProduct+'"]').css('transform', 'scale(1)');
                    } setTimeout(showProduct,400);
                });
            
                // MOSTRANDO TODOS LOS PRODUCTOS =======================
            
                $('.category_item[category="all"]').click(function(){
                    function showAll(){
                        $('.product-item').show();
                        $('.product-item').css('transform', 'scale(1)');
                    } setTimeout(showAll,400);
                });
            });