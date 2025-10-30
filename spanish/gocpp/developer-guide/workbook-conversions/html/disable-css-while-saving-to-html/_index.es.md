---
title: Desactivar CSS al guardar en HTML con Golang vía C++
linktitle: Desactivar CSS al guardar en HTML
type: docs
weight: 320
url: /es/go-cpp/disable-css-while-saving-to-html/
description: Aprende cómo desactivar CSS al guardar archivos de Excel en HTML usando Aspose.Cells for C++.
---

## **Escenarios de uso posibles**

Cuando guardas tu archivo de Excel como HTML de una sola página, generalmente los elementos CSS se insertan dentro del archivo HTML y se ubican en la sección HEAD. Si adjuntas este archivo como contenido/cuerpo de un email, la mayoría de los clientes de correo eliminarán los elementos CSS, resultando en una presentación incorrecta. La versión 24.12 de Aspose.Cells introduce una opción que permite desactivar CSS opcionalmente, permitiendo que los estilos se apliquen directamente en los elementos HTML. Si deseas establecer el HTML como contenido/cuerpo del correo, usa la propiedad [**HtmlSaveOptions.GetDisableCss()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getdisablecss/) y configúrala en **true**.

## **Desactivar CSS al guardar en HTML**

El siguiente código muestra cómo usar la propiedad [**HtmlSaveOptions.GetDisableCss()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getdisablecss/).

## **Código de muestra**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DisableCssWhileSavingToHtml.go" >}}
