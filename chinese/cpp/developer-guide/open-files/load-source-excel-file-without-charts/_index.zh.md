---
title: 使用 C++ 不加载图表的源Excel文件
linktitle: 不带图表加载源Excel文件
type: docs
weight: 420
url: /zh/cpp/load-source-excel-file-without-charts/
description: 学习如何使用 Aspose.Cells 和 C++ 加载不含图表的Excel文件。
---

{{% alert color="primary" %}}

Aspose.Cells 允许您不加载图表，使用 [**LoadOptions.GetLoadFilter()**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/getloadfilter/) 属性实现。

{{% /alert %}}

## **加载不带图表的电子表格**

以下示例代码加载不含图表的Excel文件，并以输出PDF格式保存。

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

    // Specify the load options and filter the data
    LoadOptions options;

    // Include everything except charts
    options.SetLoadFilter(new LoadFilter(LoadDataFilterOptions::All & ~LoadDataFilterOptions::Chart));

    // Path of input excel file
    U16String inputFilePath = srcDir + u"chart.xlsx";

    // Load the workbook with specified load options
    Workbook workbook(inputFilePath, options);

    // Path of output PDF file
    U16String outputFilePath = outDir + u"ResultWithoutChart.pdf";

    // Save the workbook in PDF format
    workbook.Save(outputFilePath, SaveFormat::Pdf);

    std::cout << "Workbook saved successfully without charts!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
