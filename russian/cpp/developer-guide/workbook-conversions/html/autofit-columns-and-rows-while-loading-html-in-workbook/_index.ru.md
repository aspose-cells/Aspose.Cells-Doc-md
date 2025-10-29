---
title: Автоподгонка столбцов и строк при загрузке HTML в рабочую книгу с помощью C++
linktitle: Автоматическое подгонка столбцов и строк при загрузке HTML в Рабочей книге
type: docs
weight: 120
url: /ru/cpp/autofit-columns-and-rows-while-loading-html-in-workbook/
description: Узнайте, как автоматически подгонять столбцы и строки при загрузке HTML в рабочую книгу с помощью Aspose.Cells for C++.
---

## **Возможные сценарии использования**

Вы можете автоматически подобрать ширину столбцов и строк при загрузке вашего HTML-файла в объект рабочей книги. Установите свойство [**HtmlLoadOptions.GetAutoFitColsAndRows()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlloadoptions/getautofitcolsandrows/) в **true** для этой цели.

## **Автоматическая подгонка столбцов и строк при загрузке HTML в Рабочей книге**

Приведенный ниже образец кода сначала загружает образец HTML в рабочую книгу без каких-либо параметров загрузки и сохраняет его в формате XLSX. Затем снова загружает образец HTML в рабочую книгу, но на этот раз загружает HTML после установки свойства [**HtmlLoadOptions.GetAutoFitColsAndRows()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlloadoptions/getautofitcolsandrows/) в **true** и сохраняет его в формате XLSX. Пожалуйста, скачайте оба выходных файла Excel, т.е. [Выходной файл Excel без автоподгонки столбцов и строк](outputWithout_AutoFitColsAndRows.xlsx) и [Выходной файл Excel с автоподгонкой столбцов и строк](outputWith_AutoFitColsAndRows.xlsx). На следующем снимке экрана показан эффект свойства [**HtmlLoadOptions.GetAutoFitColsAndRows()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlloadoptions/getautofitcolsandrows/) на оба выходных файла Excel.

![todo:image_alt_text](autofit-columns-and-rows-while-loading-html-in-workbook_1.png)

## **Образец кода**

```cpp
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

    // Sample HTML string
    U16String sampleHtml(u"<html><body><table><tr><td>This is sample text.</td><td>Some text.</td></tr><tr><td>This is another sample text.</td><td>Some text.</td></tr></table></body></html>");

    // Convert HTML string to memory stream
    std::string utf8Data = sampleHtml.ToUtf8();
    Vector<uint8_t> ms(utf8Data.size());
    std::memcpy(ms.GetData(), utf8Data.data(), utf8Data.size());

    // Load memory stream into workbook
    Workbook wb(ms);

    // Save the workbook in xlsx format
    wb.Save(outDir + u"outputWithout_AutoFitColsAndRows.xlsx");

    // Specify the HTMLLoadOptions and set AutoFitColsAndRows = true
    HtmlLoadOptions opts;
    opts.SetAutoFitColsAndRows(true);

    // Load memory stream into workbook with the above HTMLLoadOptions
    Workbook wbWithOptions(ms, opts);

    // Save the workbook in xlsx format
    wbWithOptions.Save(outDir + u"outputWith_AutoFitColsAndRows.xlsx");

    std::cout << "HTML to Excel conversion completed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
