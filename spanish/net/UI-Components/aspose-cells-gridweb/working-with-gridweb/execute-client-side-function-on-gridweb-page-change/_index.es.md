---
title: Ejecutar la función del lado del cliente en el cambio de página de GridWeb
type: docs
weight: 140
url: /es/net/execute-client-side-function-on-gridweb-page-change/
---
## **Posibles escenarios de uso**
A veces necesita ejecutar su función del lado del cliente cuando cambia la página de GridWeb. Aspose.Cells.GridWeb proporciona la propiedad OnPageChangeClientFunction para este fin. Establezca esta propiedad con la función del lado del cliente que desea ejecutar.
## **Ejecutar la función del lado del cliente en el cambio de página de GridWeb**
El siguiente marcado aspx explica cómo hacer uso de la propiedad OnPageChangeClientFunction. Establece la propiedad con la función del lado del cliente denominada MyOnPageChange. Tenga en cuenta que esta propiedad solo es válida si ha habilitado la paginación, es decir, EnablePaging="true". Ahora, cada vez que cambie la página GridWeb, llamará a la función del lado del cliente MyOnPageChange que imprime el**índice de la página actual** sobre el**consola** como se muestra en esta captura de pantalla.

![todo:imagen_alternativa_texto](execute-client-side-function-on-gridweb-page-change_1.png)
## **Código de muestra**
Este es el código de la función del lado del cliente MyOnPageChange que se ejecutará debido a la configuración de la propiedad OnPageChangeClientFunction ="MyOnPageChange" en GridWeb. Este es el marcado completo de la página aspx.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples.GridWeb-CSharp-GridWebBasics-CallClientsideScriptforGridWeb.aspx-CallClientsideScriptforGridWeb.cs" >}}
