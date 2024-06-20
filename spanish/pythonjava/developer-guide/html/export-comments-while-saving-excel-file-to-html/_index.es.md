---
title: Exportar Comentarios al Guardar Archivo Excel en HTML
type: docs
weight: 60
url: /es/python-java/export-comments-while-saving-excel-file-to/
---

## **Exportar comentarios al guardar archivo de Excel como HTML**
Cuando Excel se convierte a HTML, los comentarios no se exportan. Aspose.Cells para Python via Java proporciona la función de exportar comentarios durante la conversión de Excel a HTML. Para lograr esto, la API proporciona la propiedad [HtmlSaveOptions.IsExportComments](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#IsExportComments). Establecer el valor de la propiedad [HtmlSaveOptions.IsExportComments](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#IsExportComments) en **True** exportará los comentarios en el HTML de salida.

La siguiente captura de pantalla muestra el archivo HTML de salida generado por el fragmento de código de ejemplo.

![todo:image_alt_text](Export-Comments-while-Saving-Excel-file-to-Html.png)

El siguiente código de ejemplo demuestra la exportación de comentarios durante la conversión de Excel a HTML.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "HTML-ExportCommentsWhileSavingExcelFileToHtml.py" >}}
