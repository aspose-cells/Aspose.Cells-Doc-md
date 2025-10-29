---
title: 用C++将表格转换为ODS格式
linktitle: 将表格转换为ODS
type: docs
weight: 70
url: /zh/cpp/convert-table-to-ods/
description: 使用Aspose.Cells将含表格的Excel文件转换为ODS文件格式。
---

Aspose.Cells支持将含有表格的Excel文件转换为ODS文件。只需将文件保存为ODS格式，生成的ODS文件内将包含可用的表格。

## 示例代码

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C++

    // Source directory path
    U16String sourceDir = u"..\\Data\\01_SourceDirectory\\";

    // Output directory path
    U16String outputDir = u"..\\Data\\02_OutputDirectory\\";

    // Open an existing file that contains a table/list object in it
    U16String inputFilePath = sourceDir + u"SampleTable.xlsx";
    Workbook workbook(inputFilePath);

    // Save the file in ODS format
    workbook.Save(outputDir + u"ConvertTableToOds_out.ods");

    std::cout << "Conversion to ODS completed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

示例代码生成的输出ODS文件已附上供您参考。

[**Output ODS File**](ConvertTableToOds_out.ods)
{{< app/cells/assistant language="cpp" >}}
