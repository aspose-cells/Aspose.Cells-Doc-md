---
title: Ejecutar función del lado del cliente en cambio de página de GridWeb
type: docs
weight: 140
url: /es/net/aspose-cells-gridweb/execute-client-side-function-on-gridweb-page-change/
keywords: GridWeb,client,js,javascript,function
description: Este artículo introduce cómo trabajar con funciones js del lado del cliente en GridWeb.
---

## **Escenarios de uso posibles**
A veces necesitas ejecutar tu función del lado del cliente cuando la página de GridWeb cambia. Aspose.Cells.GridWeb proporciona la propiedad OnPageChangeClientFunction para este propósito. Por favor configura esta propiedad con la función del lado del cliente que deseas ejecutar.
## **Ejecutar función del lado del cliente en cambio de página de GridWeb**
El marcado aspx siguiente explica cómo hacer uso de la propiedad OnPageChangeClientFunction. Establece la propiedad con la función del lado del cliente llamada MyOnPageChange. Por favor nota, esta propiedad es válida solo si has habilitado el paginado es decir EnablePaging="true". Ahora, cada vez que cambies la página de GridWeb, llamará a la función del lado del cliente MyOnPageChange que imprimirá el **índice de página actual** en la **consola** como se muestra en esta captura de pantalla.

![todo:image_alt_text](execute-client-side-function-on-gridweb-page-change_1.png)
## **Código de muestra**
Este es el código de la función del lado del cliente MyOnPageChange que se ejecutará debido a la configuración de la propiedad OnPageChangeClientFunction ="MyOnPageChange" en GridWeb. Esta es la marca completa de la página aspx.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples.GridWeb-CSharp-GridWebBasics-CallClientsideScriptforGridWeb.aspx-CallClientsideScriptforGridWeb.cs" >}}
