---
title: Exportar comentarios mientras se guarda el archivo de Excel en HTML
type: docs
weight: 60
url: /es/python-java/export-comments-while-saving-excel-file-to/
---
## **Exportar comentarios mientras se guarda el archivo de Excel en HTML**
Cuando Excel se convierte a HTML, los comentarios no se exportan. Aspose.Cells for Python via Java proporciona la función para exportar comentarios durante la conversión de Excel a HTML. Para lograr esto, el API proporciona la[HtmlSaveOptions.IsExportComments](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#IsExportComments)propiedad. Establecer el valor de[HtmlSaveOptions.IsExportComments](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#IsExportComments) propiedad a**Verdadero** exportará comentarios en la salida HTML.

La siguiente captura de pantalla muestra el archivo de salida HTML generado por el fragmento de código de muestra.

![todo:imagen_alternativa_texto](Export-Comments-while-Saving-Excel-file-to-Html.png)

El siguiente código de ejemplo muestra cómo exportar comentarios durante la conversión de Excel a HTML.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "HTML-ExportCommentsWhileSavingExcelFileToHtml.py" >}}
