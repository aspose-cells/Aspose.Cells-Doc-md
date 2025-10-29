---
title: 将多个工作簿合并成一个单一工作簿，使用C++实现
linktitle: 工作簿合并器
type: docs
weight: 66
url: /zh/cpp/combine-multiple-workbooks-into-a-single-workbook/
description: 学习如何使用Aspose.Cells和C++将多个工作簿合并为一个单一工作簿。
---

{{% alert color="primary" %}}

有时，您需要将包含图像、图表和数据的多个工作簿合并到一个工作簿中。Aspose.Cells支持此功能。本文演示如何在Visual Studio中创建控制台应用程序，并使用几行简单的代码合并工作簿。

{{% /alert %}}

## **将具有图像和图表的工作簿合并**

示例代码使用Aspose.Cells将两个工作簿合并为单个工作簿。该代码加载源工作簿，使用[**Workbook::Combine()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/combine/)方法将它们合并，并保存输出工作簿。

### **源工作簿**

- [charts.xlsx](5473097.xlsx)
- [picture.xlsx](5473096.xlsx)

### **输出工作簿**

- [combined.xlsx](5473095.xlsx)

### **屏幕截图**

以下是源和输出工作簿的屏幕截图。

{{% alert color="primary" %}}

您可以使用任何源工作簿。这些图像仅用于说明目的。

{{% /alert %}}

**图表工作簿的第一个工作表 - 堆叠** 

![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_1.jpg)

**图表工作簿的第二个工作表 - 折线** 

![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_2.jpg)

**图片工作簿的第一个工作表 - 图片** 

![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_3.jpg)

**组合工作簿中的三个工作表 - 堆叠、线条、图片** 

![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_4.jpg)

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

    // Path of the first source excel file
    U16String sourceFile1 = srcDir + u"SampleChart.xlsx";

    // Path of the second source excel file
    U16String sourceFile2 = srcDir + u"SampleImage.xlsx";

    // Open the first excel file.
    Workbook sourceBook1(sourceFile1);

    // Open the second excel file.
    Workbook sourceBook2(sourceFile2);

    // Combining the two workbooks
    sourceBook1.Combine(sourceBook2);

    // Define the output file path
    U16String outputFilePath = srcDir + u"Combined.out.xlsx";

    // Save the target book file.
    sourceBook1.Save(outputFilePath);

    std::cout << "Workbooks combined and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **高级主题**
- [将多个工作表合并成一个工作表](/cells/zh/cpp/combine-multiple-worksheets-into-a-single-worksheet/)
- [合并文件](/cells/zh/cpp/merge-files/)
{{< app/cells/assistant language="cpp" >}}
