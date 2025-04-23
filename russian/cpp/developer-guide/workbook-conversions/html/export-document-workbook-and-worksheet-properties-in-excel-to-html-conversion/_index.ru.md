---
title: Экспорт свойств документа книги и листа Excel в преобразование в HTML с C++
linktitle: Экспорт свойств документа, книги и листа Excel в преобразование в HTML
type: docs
weight: 50
url: /ru/cpp/export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion/
description: Узнайте, как экспортировать или избегать экспорта свойств документов, книги и листа при преобразовании файлов Excel в HTML с использованием Aspose.Cells for C++.
---

## **Возможные сценарии использования**

Когда файл Microsoft Excel экспортируется в HTML с помощью Microsoft Excel или Aspose.Cells, он также экспортирует различные типы свойств документа, книги и листа, как показано на следующем скриншоте. Вы можете избегать экспорта этих свойств, установив значения [**HtmlSaveOptions.GetExportDocumentProperties()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getexportdocumentproperties/), [**HtmlSaveOptions.GetExportWorkbookProperties()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getexportworkbookproperties/) и [**HtmlSaveOptions.GetExportWorksheetProperties()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getexportworksheetproperties/) в **false**. Значение по умолчанию этих свойств — **true**. Следующий скриншот показывает, как эти свойства выглядят в экспортированном HTML.

![todo:image_alt_text](export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion_1.png)

## **Экспорт свойств документа, книги и листа Excel в преобразование в HTML**

Следующий пример кода загружает [пример файла Excel](61767776.xlsx) и преобразует его в HTML без экспорта свойств документа, рабочей книги и листа в [выходной HTML](61767779.zip).

## **Образец кода**

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"sampleExportDocumentWorkbookAndWorksheetPropertiesInHTML.xlsx";

    // Path of output HTML file
    U16String outputFilePath = outDir + u"outputExportDocumentWorkbookAndWorksheetPropertiesInHTML.html";

    // Load the sample Excel file
    Workbook workbook(inputFilePath);

    // Specify Html Save Options
    HtmlSaveOptions options;

    // We do not want to export document, workbook and worksheet properties
    options.SetExportDocumentProperties(false);
    options.SetExportWorkbookProperties(false);
    options.SetExportWorksheetProperties(false);

    // Export the Excel file to Html with Html Save Options
    workbook.Save(outputFilePath, options);

    std::cout << "Excel file exported to HTML successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
