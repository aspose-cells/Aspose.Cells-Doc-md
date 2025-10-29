---
title: 用C++计算数据表的数组公式
linktitle: 数据表的数组公式计算
description: 如何使用Aspose.Cells库在Microsoft Excel中用C++计算数据表的数组公式。通过加载现有Excel文件或创建新Excel文件，利用Aspose.Cells提供的方法计算数组公式并获取结果。最后保存修改后的Excel文件。
keywords: Aspose.Cells、Excel、数据表、数组公式、计算、C++
type: docs
weight: 70
url: /zh/cpp/calculation-of-array-formula-of-data-tables/
---

{{% alert color="primary" %}}

您可以在Microsoft Excel中使用数据>数据表...来创建数据表。 Aspose.Cells现在允许您计算数据表的数组公式。请在计算任何类型的公式时使用[**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/calculateformula/)。

{{% /alert %}}

在以下示例代码中，我们使用了[source excel file](5115535.xlsx)。如果您将单元格B1的值更改为100，则填充为黄色的数据表的值将变为120，如下图所示。 示例代码生成了[output PDF](5115538.pdf)。

![todo:image_alt_text](calculation-of-array-formula-of-data-tables_1.png)

![todo:image_alt_text](calculation-of-array-formula-of-data-tables_2.png)

以下是用于从[source excel file](5115535.xlsx)生成[output PDF](5115538.pdf)的示例代码。 请阅读注释以获取更多信息。

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"DataTable.xlsx";

    // Create workbook from source excel file
    Workbook workbook(inputFilePath);

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // When you will put 100 in B1, then all Data Table values formatted as Yellow will become 120
    worksheet.GetCells().Get(u"B1").PutValue(100);

    // Calculate formula, now it also calculates Data Table array formula
    workbook.CalculateFormula();

    // Save the workbook in pdf format
    workbook.Save(outDir + u"output_out.pdf");

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
