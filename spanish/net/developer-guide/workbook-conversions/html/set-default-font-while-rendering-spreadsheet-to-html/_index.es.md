---
title: Establezca la fuente predeterminada al renderizar la hoja de cálculo en HTML
type: docs
weight: 370
url: /es/net/set-default-font-while-rendering-spreadsheet-to/
---
{{% alert color="primary" %}}

 Aspose.Cells le permite configurar la fuente predeterminada al representar la hoja de cálculo en HTML. Utilice el[**HtmlSaveOptions.DefaultFontName**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/defaultfontname) para este propósito. Esta propiedad es útil cuando hay algunas celdas en una hoja de cálculo que tienen fuentes no válidas o inexistentes. Luego, esas celdas se representarán en una fuente especificada con el[**HtmlSaveOptions.DefaultFontName**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/defaultfontname) propiedad.

{{% /alert %}}

## Establezca la fuente predeterminada al renderizar la hoja de cálculo en HTML

El siguiente código de ejemplo crea un libro de trabajo y agrega texto en la celda B4 de la primera hoja de trabajo y establece su fuente en una fuente desconocida o inexistente. Luego guarda el libro de trabajo en HTML configurando diferentes nombres de fuente predeterminados como Courier New, Arial, Times New Roman, etc.

 La captura de pantalla muestra el efecto de configurar diferentes nombres de fuente predeterminados a través de[**HtmlSaveOptions.DefaultFontName**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/defaultfontname)propiedad.

![todo:imagen_alternativa_texto](set-default-font-while-rendering-spreadsheet-to-html_1.png)

 El código genera el[archivo de salida HTML con Courier New](5115516) , el[salida HTML con Arial](5115518) , y el[archivo de salida HTML con Times New Roman](5115517).

## Código de muestra

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-SetDefaultFontWhileRendering-1.cs" >}}
