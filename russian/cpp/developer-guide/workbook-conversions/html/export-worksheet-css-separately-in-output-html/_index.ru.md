---
title: Экспорт CSS листа отдельно в итоговом HTML с C++
linktitle: Экспорт CSS таблицы рабочего листа отдельно в выходном HTML
type: docs
weight: 80
url: /ru/cpp/export-worksheet-css-separately-in-output/
description: Узнайте, как экспортировать CSS листа отдельно при преобразовании Excel в HTML с помощью Aspose.Cells for C++.
---

## **Возможные сценарии использования**

Aspose.Cells позволяет экспортировать CSS листа отдельно при преобразовании файла Excel в HTML. Используйте свойство [**HtmlSaveOptions.GetExportWorksheetCSSSeparately()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getexportworksheetcssseparately/) для этой цели и установите его в **true** при сохранении файла в формат HTML.

## **Экспорт CSS таблицы рабочего листа отдельно в выходном HTML**

Следующий образец кода создает Excel файл, добавляет некоторый текст в ячейку **B5** красного цвета, а затем сохраняет его в формате HTML, используя свойство [**HtmlSaveOptions.GetExportWorksheetCSSSeparately()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getexportworksheetcssseparately/). Пожалуйста, ознакомьтесь с [выходным HTML](60489766.zip), сгенерированным кодом для справки. Вы найдете **stylesheet.css** как результат работы образца кода.

## **Образец кода**

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create workbook object
    Workbook wb;

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access cell B5 and put value inside it
    Cell cell = ws.GetCells().Get(u"B5");
    cell.PutValue(u"This is some text.");

    // Set the style of the cell - font color is Red
    Style st = cell.GetStyle();
    st.GetFont().SetColor(Color::Red());
    cell.SetStyle(st);

    // Specify html save options - export worksheet css separately
    HtmlSaveOptions opts;
    opts.SetExportWorksheetCSSSeparately(true);

    // Save the workbook in html
    wb.Save(u"outputExportWorksheetCSSSeparately.html", opts);

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Экспортировать книгу с одним листом в HTML**

Когда книга с несколькими листами конвертируется в HTML с помощью Aspose.Cells, создается HTML-файл вместе с папкой, содержащей CSS и несколько HTML-файлов. При открытии этого HTML-файла в браузере отображаются вкладки. Тоже поведение требуется для книги с одним листом при конвертации в HTML. Ранее не создавалась отдельная папка для книг с одним листом, создавался только HTML-файл, который не показывал вкладки. Microsoft Excel создает соответствующую папку и HTML-файл для одного листа, поэтому это поведение реализовано с помощью API Aspose.Cells. Скачать пример файла для использования в приведенном ниже коде можно по следующей ссылке:

[sampleSingleSheet.xlsx](79527937.xlsx)

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
    U16String inputFilePath = srcDir + u"sampleSingleSheet.xlsx";

    // Path of output HTML file
    U16String outputFilePath = outDir + u"outputSampleSingleSheet.htm";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Specify HTML save options
    HtmlSaveOptions options;

    // Set optional settings
    options.SetEncoding(EncodingType::UTF8);
    options.SetExportImagesAsBase64(true);
    options.SetExportGridLines(true);
    options.SetExportSimilarBorderStyle(true);
    options.SetExportBogusRowData(true);
    options.SetExcludeUnusedStyles(true);
    options.SetExportHiddenWorksheet(true);

    // Save the workbook in HTML format with specified HTML save options
    workbook.Save(outputFilePath, options);

    std::cout << "Workbook saved successfully in HTML format!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
