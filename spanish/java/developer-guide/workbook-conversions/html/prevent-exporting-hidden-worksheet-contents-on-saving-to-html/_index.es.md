---
title: Evitar la exportación de contenidos ocultos de la hoja de cálculo al guardar en HTML
type: docs
weight: 90
url: /es/java/prevent-exporting-hidden-worksheet-contents-on-saving-to/
---

{{% alert color="primary" %}}

Puede guardar libros de Excel en HTML. Sin embargo, si el libro contiene hojas de cálculo ocultas, por defecto Aspose.Cells exporta los contenidos ocultos de la hoja de cálculo al directorio de salida HTML (_files) que contiene archivos como hojas de cálculo, imágenes, tabstrip.htm, stylesheet.css, etc. A veces, exportar el contenido de las hojas de cálculo ocultas de esta manera no es apropiado. Por ejemplo, si la hoja de cálculo oculta contiene imágenes que no deben ser exportadas al directorio _files.

{{% /alert %}}

Aspose.Cells proporciona la propiedad [**HtmlSaveOptions.ExportHiddenWorksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportHiddenWorksheet). De forma predeterminada, la propiedad [**ExportHiddenWorksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportHiddenWorksheet) está configurada en **true**. Si la configura en **false**, entonces Aspose.Cells no exportará los contenidos de la hoja de cálculo oculta.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-PreventExportingHiddenWorksheetContent-PreventExportingHiddenWorksheetContent.java" >}}

Además de controlar si exportar hojas de cálculo ocultas o no, también puede configurar ajustes adicionales para exportar el libro de trabajo a HTML. Los siguientes artículos muestran otras características admitidas por Aspose.Cells para exportar libros de trabajo a HTML.

- [Convertir Excel a HTML con encabezados](/cells/es/java/convert-excel-to-html-with-headings/)
- [Excluir estilos no utilizados durante la conversión de Excel a HTML](/cells/es/java/exclude-unused-styles-during-excel-to-html-conversion/)
- [Exportar comentarios al guardar archivo de Excel como HTML](/cells/es/java/export-comments-while-saving-excel-file-to-html/)
- [Ocultar Contenido Superpuesto con CrossHideRight al guardar en HTML](/cells/es/java/hiding-overlaid-content-with-crosshideright-while-saving-to-html/)
- [Exportar un estilo de borde similar cuando el estilo de borde no es soportado por los navegadores web](/cells/es/java/export-similar-border-style-when-border-style-is-not-supported-by-web-browsers/)
{{< app/cells/assistant language="java" >}}
