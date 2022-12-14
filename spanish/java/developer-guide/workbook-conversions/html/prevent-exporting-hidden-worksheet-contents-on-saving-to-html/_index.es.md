---
title: Impedir la exportación de contenido oculto de la hoja de cálculo al guardar en HTML
type: docs
weight: 90
url: /es/java/prevent-exporting-hidden-worksheet-contents-on-saving-to/
---
{{% alert color="primary" %}}

Puede guardar libros de Excel en HTML. Sin embargo, si el libro de trabajo contiene hojas de trabajo ocultas, Aspose.Cells exporta de manera predeterminada el contenido de la hoja de trabajo oculta a la salida HTML (_ files) que contiene archivos como hojas de trabajo, imágenes, tabstrip.htm, stylesheet.css, etc. A veces, exportar el contenido de las hojas de trabajo ocultas de esta manera no es apropiado. Por ejemplo, si la hoja de cálculo oculta contiene imágenes que no deben exportarse a la_directorio de archivos.

{{% /alert %}}

Aspose.Cells proporciona el[**HtmlSaveOptions.ExportHiddenWorksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportHiddenWorksheet) propiedad. Por defecto, el[**Exportar hoja de cálculo oculta**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportHiddenWorksheet) la propiedad se establece en**verdadero**. Si lo configuras en**falso**, entonces Aspose.Cells no exportará el contenido oculto de la hoja de cálculo.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-PreventExportingHiddenWorksheetContent-PreventExportingHiddenWorksheetContent.java" >}}

Además de controlar si exportar hojas de trabajo ocultas o no, también puede configurar ajustes adicionales para exportar el libro de trabajo a HTML. Los siguientes artículos muestran otras funciones admitidas por Aspose.Cells para exportar libros de trabajo a HTML.

- [Convertir Excel a HTML con encabezados](/cells/es/java/convert-excel-to-html-with-headings/)
- [Excluir estilos no utilizados durante la conversión de Excel a HTML](/cells/es/java/exclude-unused-styles-during-excel-to-html-conversion/)
- [Exportar comentarios mientras se guarda un archivo de Excel en HTML](/cells/es/java/export-comments-while-saving-excel-file-to-html/)
- [Ocultar contenido superpuesto con CrossHideRight mientras se guarda en HTML](/cells/es/java/hiding-overlaid-content-with-crosshideright-while-saving-to-html/)
- [Exporte un estilo de borde similar cuando los navegadores web no admitan el estilo de borde](/cells/es/java/export-similar-border-style-when-border-style-is-not-supported-by-web-browsers/)
