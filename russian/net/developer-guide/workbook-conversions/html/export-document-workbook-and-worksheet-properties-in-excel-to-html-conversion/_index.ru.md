---
title: Экспорт свойств документа, книги и листа Excel в HTML
type: docs
weight: 50
url: /ru/net/export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion/
---

## **Возможные сценарии использования**

Когда файл Microsoft Excel экспортируется в HTML с использованием Microsoft Excel или Aspose.Cells, он также экспортирует различные типы свойств документа, книги и листа, как показано на скриншоте ниже. Вы можете избежать экспорта этих свойств, установив [**HtmlSaveOptions.ExportDocumentProperties**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exportdocumentproperties), [**HtmlSaveOptions.ExportWorkbookProperties**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exportworkbookproperties) и [**HtmlSaveOptions.ExportWorksheetProperties**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exportworksheetproperties) как **false**. Значение по умолчанию для этих свойств **true**. Следующий скриншот показывает, как выглядят эти свойства в экспортированном HTML.

![todo:image_alt_text](export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion_1.png)

## **Экспорт свойств документа, книги и листа Excel в HTML**

Следующий образец кода загружает [образец Excel файла](61767776.xlsx) и преобразует его в HTML, не экспортируя свойства документа, книги и листа в [выходной HTML](61767779.zip).

## **Образец кода**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "HTML-ExportDocumentWorkbookAndWorksheetPropertiesInHTML.cs" >}}
