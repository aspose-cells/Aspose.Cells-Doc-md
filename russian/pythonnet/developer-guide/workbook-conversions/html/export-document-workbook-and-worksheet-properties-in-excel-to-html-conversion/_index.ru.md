---
title: Экспорт свойств документа, книги и листа Excel в HTML
type: docs
weight: 50
url: /ru/python-net/export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion/
---

## **Возможные сценарии использования**

Когда файл Microsoft Excel экспортируется в HTML с использованием Microsoft Excel или Aspose.Cells, он также экспортирует различные типы свойств документа, книги и листа, как показано на скриншоте ниже. Вы можете избежать экспорта этих свойств, установив [**HtmlSaveOptions.export_document_properties**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/export_document_properties), [**HtmlSaveOptions.export_workbook_properties**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/export_workbook_properties) и [**HtmlSaveOptions.export_worksheet_properties**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/export_worksheet_properties) как **false**. Значение по умолчанию для этих свойств **true**. Следующий скриншот показывает, как выглядят эти свойства в экспортированном HTML.

![todo:image_alt_text](export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion_1.png)

## **Экспорт свойств документа, книги и листа Excel в HTML**

Следующий образец кода загружает [образец Excel файла](61767776.xlsx) и преобразует его в HTML, не экспортируя свойства документа, книги и листа в [выходной HTML](61767779.zip).

## **Образец кода**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-ExportDocumentWorkbookAndWorksheetPropertiesInHTML.py" >}}
{{< app/cells/assistant language="python-net" >}}
