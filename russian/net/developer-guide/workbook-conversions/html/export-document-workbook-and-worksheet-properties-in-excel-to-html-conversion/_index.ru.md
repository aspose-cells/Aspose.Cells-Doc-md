---
title: Экспорт рабочей книги документа и свойств рабочего листа в Excel для преобразования HTML
type: docs
weight: 50
url: /ru/net/export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion/
---
## **Возможные сценарии использования**

Когда файл Excel Microsoft экспортируется в HTML с помощью Microsoft Excel или Aspose.Cells, он также экспортирует различные типы свойств документа, рабочей книги и рабочего листа, как показано на следующем снимке экрана. Вы можете избежать экспорта этих свойств, установив[**HtmlSaveOptions.ExportDocumentProperties**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exportdocumentproperties), [**HtmlSaveOptions.ExportWorkbookProperties**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exportworkbookproperties)а также[**HtmlSaveOptions.ExportWorksheetProperties**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exportworksheetproperties) в качестве**ЛОЖЬ** . Значение этих свойств по умолчанию равно**истинный**. На следующем снимке экрана показано, как эти свойства выглядят в экспортированном HTML.

![дело:изображение_альтернативный_текст](export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion_1.png)

## **Экспорт свойств документа, рабочей книги и рабочего листа в Excel для преобразования HTML**

 Следующий пример кода загружает[образец файла Excel](61767776.xlsx) и преобразует его в HTML и не экспортирует свойства документа, рабочей книги и рабочего листа в[вывод HTML](61767779.zip).

## **Образец кода**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "HTML-ExportDocumentWorkbookAndWorksheetPropertiesInHTML.cs" >}}
