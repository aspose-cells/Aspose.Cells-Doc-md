---
title: 用 C++ 将 Excel 转换为 JSON
linktitle: 转换 Excel 为 JSON
type: docs
weight: 300
url: /zh/cpp/convert-excel-to-json/
description: 学习如何使用 Aspose.Cells 和 C++ 将 Excel 文件转换为 JSON。
keywords: 在没有office 2013、office 2016、office 2019和office 365的情况下将工作簿导出为JSON
---

{{% alert color="primary" %}}

Aspose.Cells支持将工作簿转换为Json(JavaScript对象表示)文件。

{{% /alert %}}

## **将Excel工作簿转换为JSON**

 不必担心如何将 Excel 工作簿转换为 JSON，因为 Aspose.Cells for C++ 库提供了最佳方案。Aspose.Cells API 支持将电子表格转换为 JSON 格式。要将工作簿导出为 JSON，请将 [**SaveFormat.Json**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) 作为 [**Workbook.Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) 方法的第二个参数传入。您还可以使用 [**JsonSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/jsonsaveoptions/) 类来为导出工作表到 JSON 指定额外的设置。

 以下代码示例演示了导出 Excel 工作簿到 JSON。请查看代码以将 [源文件](sample.xlsx) 转换成由代码生成的 JSON 文件作为参考。

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Load your source workbook
    U16String inputFilePath(u"sample.xlsx");
    Workbook workbook(inputFilePath);

    // Convert the workbook to JSON file.
    U16String outputFilePath(u"sample_out.json");
    workbook.Save(outputFilePath, SaveFormat::Json);

    std::cout << "Workbook converted to JSON successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

 使用 JsonSaveOptions 类指定额外设置的代码示例演示了导出 Excel 工作簿到 JSON。请查看代码以将 [源文件](sample.xlsx) 转换成由代码生成的 JSON 文件作为参考。

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Create an options of saving the file.
    JsonSaveOptions options;

    // Set the exporting range.
    options.SetExportArea(CellArea::CreateCellArea(u"B1", u"C4"));

    // Load your source workbook
    Workbook workbook(u"sample.xlsx");

    // Convert the workbook to json file.
    workbook.Save(u"sample_out.json", options);

    std::cout << "Workbook successfully converted to JSON!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{< app/cells/assistant language="cpp" >}}
