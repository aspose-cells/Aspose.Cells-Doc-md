---
title: Excluir estilos no utilizados durante la conversión de Excel a HTML con Golang a través de C++
linktitle: Excluir estilos no utilizados
type: docs
weight: 30
url: /es/go-cpp/exclude-unused-styles-during-excel-to-html-conversion/
description: Aprende cómo excluir estilos no utilizados durante la conversión de Excel a HTML usando Aspose.Cells for C++.
---

## **Escenarios de uso posibles**

Los archivos de Microsoft Excel pueden contener muchos estilos no utilizados. Cuando exportas el archivo Excel a formato HTML, estos estilos no utilizados también se exportan, lo que puede aumentar el tamaño del HTML. Puedes excluir los estilos no utilizados durante la conversión de un archivo Excel a HTML usando la propiedad [**HtmlSaveOptions.GetExcludeUnusedStyles()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getexcludeunusedstyles/). Cuando la configuras a **true**, todos los estilos no utilizados son excluidos del HTML de salida. La siguiente captura muestra un ejemplo de estilo no utilizado dentro del HTML de salida.

![todo:image_alt_text](exclude-unused-styles-during-excel-to-html-conversion_1.png)

## **Excluir estilos no utilizados durante la conversión de Excel a HTML**

El siguiente código de ejemplo crea un libro de trabajo y también crea un estilo no utilizado. Dado que [**HtmlSaveOptions.GetExcludeUnusedStyles()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getexcludeunusedstyles/) está configurado a **true**, este estilo no utilizado no será exportado al [HTML de salida](61767778.zip). Sin embargo, si lo configuras a **false**, este estilo no utilizado estará presente en el HTML de salida, como se muestra en la captura arriba.

## **Código de muestra**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ExcludeUnusedStylesDuringExcelToHtmlConversion.go" >}}
