---
title: 使用C++生成条件格式化数据条图片
linktitle: 生成条件格式数据条形图像
description: Aspose.Cells是一个用于操作电子表格文件的C++库。它支持生成条件格式化的数据条和图像，允许用户根据单元格的值自定义电子表格的显示。这篇文章将介绍如何使用Aspose.Cells库生成条件格式化的数据条和图像。
keywords: Aspose.Cells，条件格式，数据条，图像，电子表格
type: docs
weight: 40
url: /zh/cpp/generate-conditional-formatting-databars-images/
---

{{% alert color="primary" %}}

有时，您需要生成条件格式数据条的图像。您可以使用Aspose.Cells的[**DataBar.ToImage()**](https://reference.aspose.com/cells/cpp/aspose.cells/databar/toimage/)方法生成这些图像。本文展示了如何使用Aspose.Cells生成DataBar图像。

{{% /alert %}}

 以下示例代码生成单元格C1的DataBar图片。首先，它访问单元格的格式条件对象，然后从该对象访问 [**DataBar**](https://reference.aspose.com/cells/cpp/aspose.cells/databar/) ，并使用其 [**ToImage()**](https://reference.aspose.com/cells/cpp/aspose.cells/databar/toimage/) 方法生成单元格的图片。最后，它将图片保存到磁盘上。

```cpp
#include <iostream>
#include <fstream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook(srcDir + u"sampleGenerateDatabarImage.xlsx");
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Cell cell = worksheet.GetCells().Get(u"C1");

    int idx = worksheet.GetConditionalFormattings().Add();
    FormatConditionCollection fcc = worksheet.GetConditionalFormattings().Get(idx);
    fcc.AddCondition(FormatConditionType::DataBar);
    fcc.AddArea(CellArea::CreateCellArea(u"C1", u"C4"));

    DataBar dbar = fcc.Get(0).GetDataBar();

    ImageOrPrintOptions opts;
    opts.SetImageType(ImageType::Png);

    Vector<uint8_t> imgBytes = dbar.ToImage(cell, opts);

    std::ofstream outFile((outDir + u"outputGenerateDatabarImage.png").ToUtf8(), std::ios::binary);
    outFile.write(reinterpret_cast<const char*>(imgBytes.GetData()), imgBytes.GetLength());
    outFile.close();

    Aspose::Cells::Cleanup();
}
```
