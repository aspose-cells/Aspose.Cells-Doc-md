---
title: Загрузить или импортировать CSV файл с формулами с помощью C++
linktitle: Загрузка или импорт файла CSV с формулами
type: docs
weight: 350
url: /ru/cpp/load-or-import-csv-file-with-formulas/
description: Загрузить или импортировать CSV файл с формулами, используя Aspose.Cells с C++.
---

{{% alert color="primary" %}} 

CSV-файлы в основном содержат текстовые данные и обычно не включают формулы. Однако бывают случаи, когда CSV может содержать формулы. Такие файлы должны загружаться с установкой свойства [TxtLoadOptions.GetHasFormula()](https://reference.aspose.com/cells/cpp/aspose.cells/txtloadoptions/gethasformula/) в значение **true**. После установки этого свойства Aspose.Cells не будет интерпретировать формулы как простой текст. Они будут обрабатываться как формулы, а движок вычислений Aspose.Cells выполнит их как обычно.

{{% /alert %}} 

Следующий пример показывает, как можно загрузить и импортировать CSV-файл с формулами. Можно использовать любой CSV. В примере используется [простой CSV-файл](5115034.csv), содержащий эти данные. Как видно, он содержит формулу.

{{< highlight cpp >}}
 300,500,=Sum(A1:B1)
{{< /highlight >}}

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    //For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    //Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    //Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    //Create TxtLoadOptions with specified settings
    TxtLoadOptions opts;
    opts.SetSeparator(u','); // Set the separator to a comma
    opts.SetHasFormula(true); // Indicate that the CSV may have formulas

    // Load the CSV file into a Workbook object
    Workbook workbook(srcDir + u"sample.csv", opts);

    // You can also import the CSV file starting from cell D4 (indices 3,3)
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    worksheet.GetCells().ImportCSV(srcDir + u"sample.csv", opts, 3, 3);

    // Save the workbook in Xlsx format
    workbook.Save(outDir + u"output_out.xlsx");

    std::cout << "CSV file loaded and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

Сначала код загружает CSV-файл, затем импортирует его заново в ячейку D4. В конце он сохраняет рабочую книгу в формате XLSX. [Выходной XLSX-файл](5115052.xlsx) выглядит так. Как видно, ячейки C3 и F4 содержат формулы, а их результат — 800.

|![todo:image_alt_text](load-or-import-csv-file-with-formulas_1.png)|
| :- |
