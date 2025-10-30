---
title: Exportar Comentarios al Guardar Archivo Excel en HTML
type: docs
weight: 40
url: /es/python-net/export-comments-while-saving-excel-file-to/
---

## **Escenarios de uso posibles**

Al guardar tu archivo Excel en HTML, los comentarios no se exportan. Sin embargo, Aspose.Cells para Python via .NET ofrece esta función usando la propiedad [**HtmlSaveOptions.is_export_comments**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/is_export_comments). Si la configuras en **true**, HTML también mostrará los comentarios presentes en tu archivo Excel.

## **Exportar comentarios al guardar archivo de Excel como HTML**

El siguiente código de muestra explica el uso de la propiedad [**HtmlSaveOptions.is_export_comments**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/is_export_comments). La captura de pantalla muestra el efecto del código en el HTML cuando está establecido en **verdadero**. Descargue el [archivo de Excel de muestra](50528260.xlsx) y el [HTML generado](5052826.txt) para referencia.

![todo:image_alt_text](export-comments-while-saving-excel-file-to-html_1.png)

## **Código de muestra**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-ExportCommentsWhileSavingExcelFileToHtml.py" >}}
{{< app/cells/assistant language="python-net" >}}
