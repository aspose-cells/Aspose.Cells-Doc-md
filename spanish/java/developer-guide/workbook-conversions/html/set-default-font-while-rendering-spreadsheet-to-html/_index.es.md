---
title: Establecer la fuente predeterminada al renderizar la hoja de cálculo en HTML
type: docs
weight: 830
url: /es/java/set-default-font-while-rendering-spreadsheet-to/
---

{{% alert color="primary" %}} 

Aspose.Cells le permite configurar la fuente predeterminada al renderizar la hoja de cálculo a HTML. Utilice el [HtmlSaveOptions.DefaultFontName](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#DefaultFontName) para este propósito. Esta propiedad es útil cuando algunas celdas en una hoja de cálculo tienen fuentes inválidas o inexistentes. Entonces esas celdas se mostrarán con la fuente especificada en la propiedad [HtmlSaveOptions.DefaultFontName](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#DefaultFontName).

{{% /alert %}} 
## **Establecer fuente predeterminada al renderizar la hoja de cálculo a HTML**
El siguiente código de ejemplo crea un libro de trabajo, agrega algo de texto en la celda B4 de la primera hoja de cálculo y establece su fuente en una fuente desconocida o inexistente. Luego guarda el libro en HTML estableciendo diferentes nombres de fuente predeterminada como Courier New, Arial, Times New Roman, etc.

La captura de pantalla muestra el efecto de establecer diferentes nombres de fuente predeterminada a través de la propiedad [HtmlSaveOptions.DefaultFontName](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#DefaultFontName).

![todo:image_alt_text](set-default-font-while-rendering-spreadsheet-to-html_1.png)

El código genera el [archivo HTML de salida con Courier New](5472568), el [archivo HTML de salida con Arial](5472567) y el [archivo HTML de salida con Times New Roman](5472565).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-files-utility-SetDefaultFontWhileRenderingSpreadsheetToHTML-.java" >}}
{{< app/cells/assistant language="java" >}}
