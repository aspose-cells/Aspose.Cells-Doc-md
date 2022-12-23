---
title: Экспорт рабочей книги документа и свойств рабочего листа в Excel в преобразование HTML
type: docs
weight: 50
url: /ru/java/export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion/
---
## **Возможные сценарии использования**

Когда файл Excel Microsoft экспортируется в HTML с использованием Microsoft Excel или Aspose.Cells, он также экспортирует различные типы свойств документа, рабочей книги и рабочего листа, как показано на следующем снимке экрана. Вы можете избежать экспорта этих свойств, установив[**HtmlSaveOptions.ExportDocumentProperties**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportDocumentProperties), [**HtmlSaveOptions.ExportWorkbookProperties**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportWorkbookProperties)и[**HtmlSaveOptions.ExportWorksheetProperties**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportWorksheetProperties)как**ЛОЖЬ**. Значение этих свойств по умолчанию равно**истинный**. На следующем снимке экрана показано, как эти свойства выглядят в экспортированном HTML.

![дело:изображение_альтернативный_текст](export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion_1.png)

## **Экспорт свойств документа, книги и листа в Excel в преобразование HTML**

Следующий пример кода загружает[образец файла Excel](61767784.xlsx)и преобразует его в HTML и не экспортирует свойства документа, рабочей книги и рабочего листа в[вывод HTML](61767783.zip).

## **Образец кода**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "HTML-ExportDocumentWorkbookAndWorksheetPropertiesInHTML.java" >}}
