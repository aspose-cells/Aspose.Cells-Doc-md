---
title: 使用C++加载或导入带有公式的CSV文件。
linktitle: 加载或导入具有公式的CSV文件
type: docs
weight: 350
url: /zh/cpp/load-or-import-csv-file-with-formulas/
description: 使用Aspose.Cells与C++加载或导入包含公式的CSV文件。
---

{{% alert color="primary" %}} 

CSV文件大多包含文本数据，通常不包括任何公式。然而，也存在CSV文件可能包含公式的情况。这类CSV文件应通过设置 [TxtLoadOptions.GetHasFormula()](https://reference.aspose.com/cells/cpp/aspose.cells/txtloadoptions/gethasformula/) 为 **true** 来加载。一旦设置为 **true**，Aspose.Cells 不会将公式当作简单文本，而会作为公式处理，且Aspose.Cells的公式计算引擎会正常处理它们。

{{% /alert %}} 

以下代码演示如何加载和导入带有公式的CSV文件。你可以使用任何CSV文件。为了示例，我们使用包含此数据的 [简单CSV文件](5115034.csv)，如你所见，它包含一个公式。

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

代码首先加载CSV文件，然后在单元格D4处重新导入，并最终将工作簿保存为XLSX格式。输出的 XLSX 文件（[链接](5115052.xlsx)）如下所示。你可以看到，单元格C3和F4包含公式，其结果为800。

|![todo:image_alt_text](load-or-import-csv-file-with-formulas_1.png)|
| :- |
