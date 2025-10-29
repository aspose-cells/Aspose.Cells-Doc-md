---
title: 如何用C++旋转单元格文本
linktitle: 如何旋转单元格文本
type: docs
weight: 80
url: /zh/cpp/how-to-rotate-text-of-cell/
description: 使用Aspose.Cells for C++ API用C++代码旋转单元格文本
keywords: 用C++旋转单元格中的文本，在工作簿中以编程方式旋转单元格文本，设置单元格旋转角度，如何在Excel中用C++旋转单元格文本
---

## **在 Aspose.Cells 中旋转单元格文本**

Aspose.Cells是一个强大的C++组件，让开发者可以以编程方式操作Excel电子表格。Aspose.Cells提供的一个功能是旋转单元格，允许你定制文本的方向，改善数据的视觉展示。在本文中，我们将探讨如何使用Aspose.Cells旋转单元格。

## **如何在Excel中旋转单元格中的文本**
要在Excel中旋转单元格，您可以按照以下步骤操作：
1. 打开Excel并选择您要旋转的单元格或单元格范围。
1. 右键单击所选单元格，并从上下文菜单中选择“格式单元格”。或者，您还可以在Excel功能区中的“主页”选项卡中，单击“单元格”组中的“格式”下拉菜单，然后选择“格式单元格”。
1. 在“格式单元格”对话框中，转到“对齐”选项卡。
1. 在“方向”部分下，您将看到旋转文本的选项。您可以直接在“度数”框中输入所需的旋转角度。正值逆时针旋转文本，负值顺时针旋转文本。
<br>
![todo:image_alt_text](alignment.png)
1. 选择所需的旋转后，单击“确定”以应用更改。所选单元格现在将根据您选择的旋转角度或方向进行旋转。

## **如何使用Aspose.Cells API旋转单元格文本**

[**Style.GetRotationAngle()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getrotationangle/)属性使旋转单元格更加方便。要在Aspose.Cells中旋转单元格，您需要按照以下步骤操作：
1. 加载Excel工作簿
<br>
首先，您需要使用Aspose.Cells加载Excel工作簿。您可以使用Workbook类打开现有的Excel文件或创建新文件。 

1. 访问工作表
<br>
加载工作簿后，您需要访问要旋转单元格的工作表。您可以通过索引或名称访问工作表。 

1. 旋转单元格文本
<br>
现在您已经可以访问工作表，就可以通过修改所需单元格的样式对象来旋转单元格。样式对象允许您设置各种格式选项，包括旋转。 

1. 保存工作簿
<br>
旋转单元格后，您可以使用Save方法将修改后的工作簿保存回文件或流。

## ** C++ 示例代码**

请参阅以下代码，它创建一个工作簿对象，并为几个单元格设置不同的旋转角度。屏幕截图显示了执行示例代码后的结果。
<br>
<img src="rotation.png" width=80% />

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a new workbook
    Workbook workbook;

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Row index of the cell
    int row = 0;
    // Column index of the cell
    int column = 0;

    // Get cell A1 and set its value
    Cell a1 = worksheet.GetCells().Get(row, column);
    a1.PutValue(u"a1 rotate text");
    Style a1Style = a1.GetStyle();

    // Set the rotation angle in degrees
    a1Style.SetRotationAngle(45);
    a1.SetStyle(a1Style);

    // Set column index to 1 for cell B1
    column = 1;
    Cell b1 = worksheet.GetCells().Get(row, column);
    b1.PutValue(u"b1 rotate text");
    Style b1Style = b1.GetStyle();

    // Set the rotation angle in degrees
    b1Style.SetRotationAngle(255);
    b1.SetStyle(b1Style);

    // Set column index to 2 for cell C1
    column = 2;
    Cell c1 = worksheet.GetCells().Get(row, column);
    c1.PutValue(u"c1 rotate text");
    Style c1Style = c1.GetStyle();

    // Set the rotation angle in degrees
    c1Style.SetRotationAngle(-90);
    c1.SetStyle(c1Style);

    // Set column index to 3 for cell D1
    column = 3;
    Cell d1 = worksheet.GetCells().Get(row, column);
    d1.PutValue(u"d1 rotate text");
    Style d1Style = d1.GetStyle();

    // Set the rotation angle in degrees
    d1Style.SetRotationAngle(-90);
    d1.SetStyle(d1Style);

    // Save the workbook
    workbook.Save(u"out.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
