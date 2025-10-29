---
title: 使用C++应用Subtotal和更改详细下方轮廓总结行方向
linktitle: 应用小计并更改大纲摘要行的方向，而不是详细信息下面的行
type: docs
weight: 100
url: /zh/cpp/applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail/
description: 了解如何使用Aspose.Cells for C++ API对数据应用Subtotal并更改详细下方轮廓总结行的方向。
keywords: 应用小计，添加小计，更改详细下面概要行的方向，更改详细右边概要列的方向，创建小计并更改详细下面概要行的方向
---

{{% alert color="primary" %}}

本文将解释如何对数据应用Subtotal并改变详细下方轮廓总结行的方向。

您可以使用[**Worksheet.Cells.Subtotal()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/subtotal/)方法对数据应用Subtotal。它接受以下参数：

- **单元格区域** - 应用小计的范围
- **按组** - 按零为基础的整数偏移量分组
- **功能** - 小计功能。
- **TotalList** - 一个从零开始的字段偏移量数组，指示要添加小计的字段。
- **替换** - 表示是否替换当前的小计
- **分页符** - 表示是否在组间添加分页符
- **数据下方总结** - 表示是否在数据下方添加总结。

此外，您还可以使用`Worksheet.Outline.SummaryRowBelow`属性控制“详细信息下的轮廓总结行”的方向。如图所示，您可以在Microsoft Excel中通过**数据 > 大纲 > 设置**打开此设置。

![todo:image_alt_text](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_1.png)

{{% /alert %}}

## 源文件和输出文件的图像

下图显示了示例代码中使用的源Excel文件，其中包含列A和B中的一些数据。

![todo:image_alt_text](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_2.png)

下图显示了示例代码生成的输出Excel文件。如您所见，对范围A2:B11应用了小计，并且大纲的方向是细节下方的摘要行。

![todo:image_alt_text](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_3.png)

## 在C++中应用Subtotal并更改轮廓总结行的方向的示例代码

以下是实现上述输出的示例代码。

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

    // Create workbook from source Excel file
    Workbook workbook(srcDir + u"Book1.xlsx");

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Get the Cells collection in the first worksheet
    Cells cells = worksheet.GetCells();

    // Create a cellarea i.e.., A2:B11
    CellArea ca = CellArea::CreateCellArea(u"A2", u"B11");

    // Apply subtotal, the consolidation function is Sum and it will applied to Second column (B) in the list
    cells.Subtotal(ca, 0, ConsolidationFunction::Sum, { 1 }, true, false, true);

    // Set the direction of outline summary
    worksheet.GetOutline().SetSummaryRowBelow(true);

    // Save the excel file
    workbook.Save(outDir + u"output_out.xlsx");

    std::cout << "Subtotal applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
