window.onload = function(){
    var ancho=document.getElementById("contenido").offsetWidth;
    var element=document.getElementById("contenido")
    var element2 = document.getElementById("menu");
    var element3 = document.getElementById("estad");

    if(ancho<548){
        element.classList.add("menu2");
        element2.classList.add("contenido2");
    }

    //alert (element)
}

var cont = 0;
function contador(){
	var contador = document.getElementById("contador");
	contador.value = cont;
    cont++;
}

var show=0;
function elmenu(){
    var element = document.getElementById("menu");

    if(show==0){
        element.style.left="0";
        //document.getElementById("contenido").style.width="69%";
        show=1;
    }else{
        element.removeAttribute("style");
        //document.getElementById("contenido").removeAttribute("style");
        show=0;
    }
}

function elestad(){
    var element = document.getElementById("estad");

    if(show==0){
        //element.style.left="0";
        element.style.transform="translateY(0)";
        show=1;
    }else{
        element.removeAttribute("style");
        show=0;
    }
}

function totalprod() {
    var cant = document.getElementById("id_amoutn").value;
    var prec = document.getElementById("id_unitv").value;

    if(cant==""||prec==""){
        document.getElementById("id_total").value = 0;
    }
    else{
        document.getElementById("id_total").value = parseInt(cant)*parseInt(prec);
    }
 }