window.onload = function(){
    var fecha = new Date(); //Fecha actual
    var mes = fecha.getMonth()+1; //obteniendo mes
    var dia = fecha.getDate(); //obteniendo dia
    var ano = fecha.getFullYear(); //obteniendo año
    if(dia<10)
      dia='0'+dia; //agrega cero si el menor de 10
    if(mes<10)
      mes='0'+mes //agrega cero si el menor de 10
    document.getElementById('date').value=ano+"-"+mes+"-"+dia;
}

var show=0;
function elmenu(){
    var element = document.getElementById("menu");
    var element2=document.getElementById("contenido");

    if(show==0){
        element.classList.add("menu2");
        element2.classList.add("contenido2");
        
        show=1;
    }else{
        element.classList.remove("menu2");
        element2.classList.remove("contenido2");
        show=0;
    }
}

function totalprod() {
    var cant = document.getElementById("cantidad").value;
    var prec = document.getElementById("precio").value;

    if(cant==""||prec==""){
        document.getElementById("total").value = 0;
    }
    else{
        document.getElementById("total").value = parseInt(cant)*parseInt(prec);
    }
 }