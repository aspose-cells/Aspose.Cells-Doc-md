---
title: 使用C++应用高级条件格式
linktitle: 应用高级条件格式
description: 如何在C++中使用Aspose.Cells库应用高级条件格式。通过调整这些条件，您可以更好地控制单元格的外观和显示。
keywords: Aspose.Cells，高级条件格式，C++，条件，格式化
type: docs
weight: 70
url: /zh/cpp/apply-advanced-conditional-formatting/
---

{{% alert color="primary" %}}

Microsoft Excel 2007 年及以后的版本（2010/2013/2016）提供了一些高级的条件格式功能。例如，它允许您应用单元格底纹、边框、彩色图标、箭头、旗帜以及字体格式等。这些功能已经变得非常复杂。

{{% /alert %}}

## **将高级条件格式应用于 Microsoft Excel 文件**
条件格式可以：

- 使用数据条以图形化方式增强单元格中的基础数字，通过在单元格中嵌入简单的条形图。
- 根据它们与范围内其他单元格中的值的关系自动通过颜色比例给单元格着色。默认设置将最低值以红色着色，向上转为最高值以绿色着色。
- 以与颜色比例类似的方式使用图标集，但与给单元格着色不同，它向单元格中添加小图标，如箭头和交通灯。

Aspose.Cells 在运行时完全支持 Microsoft Excel 2007 年及以后版本在 XLSX 格式中提供的条件格式。此示例演示了包括图标集、数据条、颜色比例、时间周期、前/后和其他规则在内的高级条件格式类型的实参练习。

### **计算 Microsoft Excel 为 ColorScale 条件格式选择的颜色**
Aspose.Cells允许您在模板文件中使用ColorScale条件格式化时计算Microsoft Excel选择的颜色。请参阅下面的示例代码，了解如何计算Microsoft Excel选择的颜色。

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Instantiate a workbook object and open the template file
    Workbook workbook(srcDir + u"Book1.xlsx");

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Get the A1 cell
    Cell a1 = worksheet.GetCells().Get(u"A1");

    // Get the conditional formatting resultant object
    ConditionalFormattingResult cfr1 = a1.GetConditionalFormattingResult();

    // Get the ColorScale resultant color object
    Aspose::Cells::Color c = cfr1.GetColorScaleResult();

    Aspose::Cells::Cleanup();
}
```
