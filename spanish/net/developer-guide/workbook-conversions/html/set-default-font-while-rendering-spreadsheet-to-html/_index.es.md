---
title: Establecer la fuente predeterminada al renderizar la hoja de cálculo en HTML
type: docs
weight: 370
url: /es/net/set-default-font-while-rendering-spreadsheet-to/
---

{{% alert color="primary" %}}

Aspose.Cells te permite establecer la fuente predeterminada al renderizar la hoja de cálculo en HTML. Utiliza [**HtmlSaveOptions.DefaultFontName**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/defaultfontname) para este propósito. Esta propiedad es útil cuando hay celdas en una hoja de cálculo que tienen fuentes inválidas o que no existen. Entonces esas celdas se renderizarán en una fuente especificada con la propiedad [**HtmlSaveOptions.DefaultFontName**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/defaultfontname).

{{% /alert %}}

## Establecer la fuente predeterminada al renderizar la hoja de cálculo en HTML

El siguiente código de ejemplo crea un libro de trabajo, agrega algo de texto en la celda B4 de la primera hoja de cálculo y establece su fuente en una fuente desconocida o inexistente. Luego guarda el libro en HTML estableciendo diferentes nombres de fuente predeterminada como Courier New, Arial, Times New Roman, etc.

La captura de pantalla muestra el efecto de establecer diferentes nombres de fuente predeterminada a través de la propiedad [**HtmlSaveOptions.DefaultFontName**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/defaultfontname).

![todo:image_alt_text](set-default-font-while-rendering-spreadsheet-to-html_1.png)

El código genera el [archivo HTML de salida con Courier New](5115516), el [archivo HTML de salida con Arial](5115518), y el [archivo HTML de salida con Times New Roman](5115517).

## Código de Muestra

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-SetDefaultFontWhileRendering-1.cs" >}}
