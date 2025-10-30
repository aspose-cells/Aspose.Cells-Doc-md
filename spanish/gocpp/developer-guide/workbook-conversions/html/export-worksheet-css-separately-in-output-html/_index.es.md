---
title: Exportar CSS de hoja de trabajo por separado en HTML de salida con Golang a través de C++
linktitle: Exportar la hoja de estilos CSS por separado en el HTML de salida
type: docs
weight: 80
url: /es/go-cpp/export-worksheet-css-separately-in-output/
description: Aprende cómo exportar el CSS de la hoja de trabajo por separado al convertir archivos de Excel a HTML usando Aspose.Cells for C++.
---

## **Escenarios de uso posibles**

Aspose.Cells ofrece la función para exportar el CSS de la hoja de trabajo por separado cuando conviertes tu archivo de Excel a HTML. Por favor, usa la propiedad [**HtmlSaveOptions.GetExportWorksheetCSSSeparately()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getexportworksheetcssseparately/) para este propósito y configúralo en **true** al guardar el archivo de Excel en formato HTML.

## **Exportar la hoja de estilos CSS por separado en el HTML de salida**

El siguiente código de ejemplo crea un archivo de Excel, agrega algo de texto en la celda **B5** en color **Rojo** y luego lo guarda en formato HTML usando la propiedad [**HtmlSaveOptions.GetExportWorksheetCSSSeparately()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getexportworksheetcssseparately/). Por favor, consulta el [HTML de salida](60489766.zip) generado por el código para referencia. Encontrarás el archivo **stylesheet.css** dentro como resultado del código de ejemplo.

## **Código de muestra**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ExportWorksheetCssSeparatelyInOutputHtml.go" >}}
## **Exportar libro de una sola hoja a HTML**

Cuando un libro con múltiples hojas se convierte a HTML usando Aspose.Cells, crea un archivo HTML junto con una carpeta que contiene CSS y múltiples archivos HTML. Cuando se abre este archivo HTML en el navegador, las pestañas son visibles. El mismo comportamiento es necesario para un libro con una sola hoja de trabajo cuando se convierte a HTML. Antes, no se creaba una carpeta separada para libros de una sola hoja, solo se creaba un archivo HTML. Dicho archivo HTML no muestra una pestaña al abrirlo en el navegador. MS Excel crea una carpeta y un HTML adecuados para una sola hoja también, por lo que se implementa el mismo comportamiento usando las API de Aspose.Cells. El archivo de ejemplo se puede descargar desde el siguiente enlace para usar en el código de ejemplo a continuación:

[sampleSingleSheet.xlsx](79527937.xlsx)

## **Código de muestra**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ExportWorksheetCssSeparatelyInOutputHtml-1.go" >}}
