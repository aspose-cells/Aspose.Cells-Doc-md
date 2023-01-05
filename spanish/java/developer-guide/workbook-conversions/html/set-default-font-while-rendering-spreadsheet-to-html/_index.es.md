---
title: Establezca la fuente predeterminada al renderizar la hoja de cálculo en HTML
type: docs
weight: 830
url: /es/java/set-default-font-while-rendering-spreadsheet-to/
---
{{% alert color="primary" %}} 

 Aspose.Cells le permite configurar la fuente predeterminada al representar la hoja de cálculo en HTML. Utilice el[HtmlSaveOptions.DefaultFontName](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#DefaultFontName)para este propósito. Esta propiedad es útil cuando hay algunas celdas en una hoja de cálculo que tienen fuentes no válidas o inexistentes. Luego, esas celdas se representarán en una fuente especificada con[HtmlSaveOptions.DefaultFontName](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#DefaultFontName) propiedad.

{{% /alert %}} 
## **Establezca la fuente predeterminada al renderizar la hoja de cálculo en HTML**
El siguiente código de ejemplo crea un libro de trabajo y agrega texto en la celda B4 de la primera hoja de trabajo y establece su fuente en una fuente desconocida o inexistente. Luego guarda el libro de trabajo en HTML configurando diferentes nombres de fuente predeterminados como Courier New, Arial, Times New Roman, etc.

 La captura de pantalla muestra el efecto de configurar diferentes nombres de fuente predeterminados a través de[HtmlSaveOptions.DefaultFontName](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#DefaultFontName)propiedad.

![todo:imagen_alternativa_texto](set-default-font-while-rendering-spreadsheet-to-html_1.png)

 El código genera el[archivo de salida HTML con Courier New](5472568) , el[salida HTML con Arial](5472567) y el[archivo de salida HTML con Times New Roman](5472565).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-files-utility-SetDefaultFontWhileRenderingSpreadsheetToHTML-.java" >}}
