---
title: Ejecutar la función del lado del cliente en el cambio de página de GridWeb
type: docs
weight: 70
url: /es/java/execute-client-side-function-on-gridweb-page-change/
---
##  **Posibles escenarios de uso**
A veces es necesario ejecutar la función del lado del cliente cuando cambia la página GridWeb. Aspose.Cells.GridWeb proporciona la propiedad OnPageChangeClientFunction para este propósito. Configure esta propiedad con la función del lado del cliente que desea ejecutar.
##  **Ejecutar la función del lado del cliente en el cambio de página de GridWeb**
 El siguiente código Java explica cómo utilizar la propiedad GridWebBean.setOnPageChangeClientFunction(). Establece la propiedad con la función del lado del cliente denominada MyOnPageChange. Tenga en cuenta que esta propiedad sólo es válida si ha habilitado la paginación, es decir, GridWebBean.setEnablePaging(true). Ahora, cada vez que cambie la página GridWeb, llamará a la función del lado del cliente MyOnPageChange que imprime el**índice de la página actual** sobre el**consola** como se muestra en esta captura de pantalla.

![todo:image_alt_text](execute-client-side-function-on-gridweb-page-change_1.png)
##  **Código de muestra**
Este es el código de la función del lado del cliente MyOnPageChange que se ejecutará debido a esta línea, es decir, Gridweb.setOnPageChangeClientFunction("MyOnPageChange");

{{< highlight "java" >}}

 function MyOnPageChange(index) {

	console.log("current page is:" + (index+1));

}

{{< /highlight >}}

El siguiente código explica cómo habilitar la paginación y establecer la propiedad OnPageChangeClientFunction.

{{< highlight "java" >}}

 GridWebBean gridweb=BeanManager.getBean(request);

gridweb.setEnablePaging(true);

gridweb.setOnPageChangeClientFunction("MyOnPageChange");

{{< /highlight >}}
