---
title: Establecer fuente predeterminada al renderizar hoja de cálculo a HTML con Golang mediante C++
linktitle: Establecer la fuente predeterminada al renderizar la hoja de cálculo en HTML
type: docs
weight: 370
url: /es/go-cpp/set-default-font-while-rendering-spreadsheet-to/
description: Aprende cómo establecer la fuente predeterminada al renderizar hojas de cálculo a HTML utilizando Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Aspose.Cells te permite establecer la fuente predeterminada al renderizar una hoja de cálculo a HTML. Por favor, usa [**HtmlSaveOptions.GetDefaultFontName()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getdefaultfontname/) para este propósito. Esta propiedad es útil cuando hay celdas en una hoja de cálculo que tienen fuentes inválidas o no existentes. Entonces, esas celdas se renderizarán con la fuente especificada con la propiedad [**HtmlSaveOptions.GetDefaultFontName()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getdefaultfontname/).

{{% /alert %}}

## Establecer la fuente predeterminada al renderizar la hoja de cálculo en HTML

El siguiente código de ejemplo crea un libro de trabajo, agrega algo de texto en la celda B4 de la primera hoja de cálculo y establece su fuente en una fuente desconocida o inexistente. Luego guarda el libro en HTML estableciendo diferentes nombres de fuente predeterminada como Courier New, Arial, Times New Roman, etc.

La captura de pantalla muestra el efecto de establecer diferentes nombres de fuentes predeterminadas mediante la propiedad [**HtmlSaveOptions.GetDefaultFontName()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getdefaultfontname/).

![todo:image_alt_text](set-default-font-while-rendering-spreadsheet-to-html_1.png)

El código genera el [archivo HTML de salida con Courier New](5115516), el [archivo HTML de salida con Arial](5115518), y el [archivo HTML de salida con Times New Roman](5115517).

## Código de Muestra

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SetDefaultFontWhileRenderingSpreadsheetToHtml.go" >}}
