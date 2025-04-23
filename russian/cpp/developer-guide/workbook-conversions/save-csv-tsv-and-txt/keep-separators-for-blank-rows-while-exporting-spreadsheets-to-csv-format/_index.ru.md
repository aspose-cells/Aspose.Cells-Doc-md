---
title: Сохранять разделители для пустых строк при экспорте таблиц в CSV с C++
linktitle: Сохранять разделители для пустых строк при экспорте таблиц в формат CSV
type: docs
weight: 160
url: /ru/cpp/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/
description: Узнайте, как сохранять разделители для пустых строк при экспорте таблиц в CSV с помощью Aspose.Cells с C++.
---

## **Сохранять разделители для пустых строк при экспорте таблиц в формат CSV**

Aspose.Cells позволяет сохранять разделители строк при преобразовании таблиц в CSV. Для этого используйте свойство [**GetKeepSeparatorsForBlankRow()**](https://reference.aspose.com/cells/cpp/aspose.cells/txtsaveoptions/getkeepseparatorsforblankrow/) класса [**TxtSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/txtsaveoptions/). [**GetKeepSeparatorsForBlankRow()**](https://reference.aspose.com/cells/cpp/aspose.cells/txtsaveoptions/getkeepseparatorsforblankrow/) — булево свойство. Чтобы сохранять разделители для пустых строк при преобразовании файла Excel в CSV, установите свойство [**GetKeepSeparatorsForBlankRow()**](https://reference.aspose.com/cells/cpp/aspose.cells/txtsaveoptions/getkeepseparatorsforblankrow/) в **true**.

Следующий пример загружает [исходный файл Excel](84378743.xlsx). Он устанавливает свойство [**TxtSaveOptions.GetKeepSeparatorsForBlankRow()**](https://reference.aspose.com/cells/cpp/aspose.cells/txtsaveoptions/getkeepseparatorsforblankrow/) в **true** и сохраняет файл как [output.csv](84378744.csv). Скриншот показывает сравнение исходного файла Excel, стандартного вывода при преобразовании в CSV и итогового результата, созданного при установке [**GetKeepSeparatorsForBlankRow()**](https://reference.aspose.com/cells/cpp/aspose.cells/txtsaveoptions/getkeepseparatorsforblankrow/) в **true**.

![todo:image_alt_text](keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format_1.jpg)

## **Образец кода**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Create a Workbook object and opening the file from its path
    Workbook workbook(inputFilePath);

    // Instantiate Text File's Save Options
    TxtSaveOptions options;

    // Set KeepSeparatorsForBlankRow to true to show separators in blank rows
    options.SetKeepSeparatorsForBlankRow(true);

    // Save the file with the options
    workbook.Save(outDir + u"output.csv", options);

    std::cout << "File saved successfully as output.csv!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
