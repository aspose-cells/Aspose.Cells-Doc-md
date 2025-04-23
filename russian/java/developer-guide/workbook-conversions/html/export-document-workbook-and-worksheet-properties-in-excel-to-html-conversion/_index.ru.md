---
title: Экспорт свойств документа, книги и листа Excel в HTML
type: docs
weight: 50
url: /ru/java/export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion/
---

## **Возможные сценарии использования**

Когда файл Microsoft Excel экспортируется в HTML с использованием Microsoft Excel или Aspose.Cells, также экспортируются различные типы свойств документа, книги и листа, как показано на следующем снимке экрана. Вы можете избежать экспорта этих свойств, установив [**HtmlSaveOptions.ExportDocumentProperties**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportDocumentProperties), [**HtmlSaveOptions.ExportWorkbookProperties**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportWorkbookProperties) и [**HtmlSaveOptions.ExportWorksheetProperties**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportWorksheetProperties) в значение **false**. Значение по умолчанию для этих свойств **true**. На следующем скриншоте показано, как выглядят эти свойства в экспортированном HTML.

![todo:image_alt_text](export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion_1.png)

## **Экспорт свойств документа, книги и листа Excel в HTML**

Следующий образец кода загружает [пример файла Excel](61767784.xlsx) и преобразует его в HTML, и не экспортирует свойства документа, книги и листа в [выходной HTML](61767783.zip).

## **Образец кода**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "HTML-ExportDocumentWorkbookAndWorksheetPropertiesInHTML.java" >}}
{{< app/cells/assistant language="java" >}}
