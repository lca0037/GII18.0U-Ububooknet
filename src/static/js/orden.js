
function ordenar(tipo){
	$.ajax({
      type: "POST",
      contentType: "application/json;charset=utf-8",
      url: "/Ordenar/",
      traditional: "true",
      data: JSON.stringify(tipo),
      dataType: "json",
      success: function(response){
      	$("#content #Personajes").replaceWith(response);
      }
    });
}