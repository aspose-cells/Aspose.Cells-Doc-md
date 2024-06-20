---
title: Ejecutar función del lado del cliente en cambio de página de GridWeb
type: docs
weight: 70
url: /es/java/execute-client-side-function-on-gridweb-page-change/
---

## **Escenarios de uso posibles**
A veces necesitas ejecutar tu función del lado del cliente cuando la página de GridWeb cambia. Aspose.Cells.GridWeb proporciona la propiedad OnPageChangeClientFunction para este propósito. Por favor configura esta propiedad con la función del lado del cliente que deseas ejecutar.
## **Ejecutar función del lado del cliente en cambio de página de GridWeb**
El siguiente código en Java explica cómo hacer uso de la propiedad GridWebBean.setOnPageChangeClientFunction(). Configura la propiedad con la función del lado del cliente llamada MyOnPageChange. Tenga en cuenta que esta propiedad es válida solo si ha habilitado el paginado, es decir, GridWebBean.setEnablePaging(true). Ahora, cada vez que cambie la página de GridWeb, llamará a la función del lado del cliente MyOnPageChange que imprimirá el **índice de página actual** en la **consola** como se muestra en esta captura de pantalla.

![todo:image_alt_text](execute-client-side-function-on-gridweb-page-change_1.png)
## **Código de muestra**
Este es el código de la función del lado del cliente MyOnPageChange que se ejecutará debido a esta línea, es decir, Gridweb.setOnPageChangeClientFunction("MyOnPageChange");

{{< highlight java >}}

 function MyOnPageChange(index) {

	console.log("current page is:" + (index+1));

}

{{< /highlight >}}

El siguiente código explica cómo habilitar el paginado y configurar la propiedad OnPageChangeClientFunction.

{{< highlight java >}}

 GridWebBean gridweb=BeanManager.getBean(request);

gridweb.setEnablePaging(true);

gridweb.setOnPageChangeClientFunction("MyOnPageChange");

{{< /highlight >}}
