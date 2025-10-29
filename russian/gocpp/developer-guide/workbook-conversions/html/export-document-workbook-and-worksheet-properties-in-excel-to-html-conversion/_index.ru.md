---
title: Экспорт свойств рабочей книги и листа документа при конвертации Excel в HTML с помощью Golang через C++
linktitle: Экспорт свойств документа, книги и листа Excel в преобразование в HTML
type: docs
weight: 50
url: /ru/go-cpp/export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion/
description: Узнайте, как экспортировать или избегать экспорта свойств документов, книги и листа при преобразовании файлов Excel в HTML с использованием Aspose.Cells for C++.
---

## **Возможные сценарии использования**

Когда файл Microsoft Excel экспортируется в HTML с помощью Microsoft Excel или Aspose.Cells, он также экспортирует различные типы свойств документа, книги и листа, как показано на следующем скриншоте. Вы можете избегать экспорта этих свойств, установив значения [**HtmlSaveOptions.GetExportDocumentProperties()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getexportdocumentproperties/), [**HtmlSaveOptions.GetExportWorkbookProperties()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getexportworkbookproperties/) и [**HtmlSaveOptions.GetExportWorksheetProperties()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getexportworksheetproperties/) в **false**. Значение по умолчанию этих свойств — **true**. Следующий скриншот показывает, как эти свойства выглядят в экспортированном HTML.

![todo:image_alt_text](export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion_1.png)

## **Экспорт свойств документа, книги и листа Excel в преобразование в HTML**

Следующий пример кода загружает [пример файла Excel](61767776.xlsx) и преобразует его в HTML без экспорта свойств документа, рабочей книги и листа в [выходной HTML](61767779.zip).

## **Образец кода**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ExportDocumentWorkbookAndWorksheetPropertiesInExcelToHtmlConversion.go" >}}
