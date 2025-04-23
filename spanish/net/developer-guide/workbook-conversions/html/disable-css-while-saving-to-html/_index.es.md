---
title: Desactivar CSS al guardar en HTML
type: docs
weight: 320
url: /es/net/disable-css-while-saving-to-html/
---

## **Escenarios de uso posibles**

Cuando guardas tu archivo Excel en un HTML de página única, normalmente los elementos CSS se integran dentro del archivo HTML y se ubican en la sección HEAD.Si adjuntas este archivo como contenido/cuerpo de un correo electrónico, los elementos CSS serán eliminados por la mayoría de los clientes de correo, resultando en una visualización incorrecta. La versión 24.12 de Aspose.Cells introduce una opción que permite desactivar opcionalmente CSS, permitiendo que los estilos se apliquen directamente en los elementos HTML mismos. Si deseas establecer el HTML como contenido/cuerpo del correo electrónico, usa la propiedad [**HtmlSaveOptions.DisableCss**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/disablecss) y configúrala en **true**.



## **Desactivar CSS al guardar en HTML**

El siguiente código de ejemplo muestra el uso de la propiedad [**HtmlSaveOptions.DisableCss**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/disablecss). 



## **Código de muestra**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-HTML-DisableCss-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
