---
title: 格式单元格
type: docs
weight: 40
url: /zh/net/aspose-cells-gridweb/format-grid-cell/
keywords: GridWeb，格式，样式
description: 本文介绍如何设置或应用网格中单元格（GridCell）的样式格式。
---

{{% alert color="primary" %}} 

此主题详细讨论了如何格式化单元格。

它涵盖了使用 Aspose.Cells.GridWeb 控件的样式对话框在 GUI 模式下格式化单元格的内容。还展示了如何以编程方式格式化单元格。讨论了不同的格式设置，如字体、边框和数字格式，并通过示例进行说明。

{{% /alert %}} 
## **使用样式对话框格式化单元格**
单元格可以通过[以编程方式](/cells/zh/net/aspose-cells-gridweb/format-cells/)格式化，但使用 Aspose.Cells.GridWeb 控件以所见即所得的方式格式化单元格的最简便方法是使用样式对话框。

使用样式对话框：
选择一系列单元格，然后右键单击并选择**格式化单元格**。 

**选择格式化单元格** 

![todo:image_alt_text](format-cells_1.png)



显示样式对话框。 

**使用样式对话框格式化单元格** 

![todo:image_alt_text](format-cells_2.png)

样式对话框让用户通过自定义字体和边框设置来格式化单元格。
### **自定义字体设置**
您可以使用样式对话框自定义以下字体设置：

- 字体名称，从列表中选择所需的字体。
- 字体样式，应用粗体、斜体等字体样式。
- 字体大小，选择磅值的字体大小。
- 下划线，给文字加下划线。
- 删除线，给文字应用删除线效果。
- 水平对齐，选择水平对齐方式。
- 垂直对齐，选择垂直对齐方式。
- 字体颜色，选择字体颜色。
- 背景，选择背景颜色。

您可以在小预览区域检查所选字体设置。

**自定义字体设置** 

![todo:image_alt_text](format-cells_3.png)
### **自定义边框设置**
该控件还允许用户通过在样式对话框中自定义边框设置来绘制单元格周围的边框。

查看与边框相关的选项：
单击样式对话框中的**边框**。
边框相关选项将显示。 

**样式对话框中的边框选项** 

![todo:image_alt_text](format-cells_4.png)

可以从样式对话框中选择以下边框选项：

- 边框线样式，选择实线、虚线等边框样式。
- 边框线宽度，选择像素单位的边框宽度。
- 边框线颜色，选择线条颜色。
- 边框线，选择边框线的编号和位置。

**自定义边框设置** 

![todo:image_alt_text](format-cells_5.png)
### **应用设置**
单击样式对话框中的**确定**以应用更改。

**应用了字体和边框设置** 

![todo:image_alt_text](format-cells_6.png)


## **使用API格式化单元格**
单元格还可以使用 Aspose.Cells.GridWeb API 进行程序化格式化。每个单元格都有一个 Style 属性，该属性表示一个 GridTableItemStyle 对象。使用 Style 属性自定义字体和边框设置。
### **设置字体**
要进行程序化自定义字体设置：

1. 将 Aspose.Cells.GridWeb 控件添加到 Web 表单中。
1. 访问工作表。
1. 访问要进行格式化的单元格。
1. 访问单元格的样式。
1. 设置点数（points）中的字体大小。
1. 设置字体样式。
1. 设置前景色和背景色。
1. 设置水平和垂直对齐。
1. 将样式重新设置到单元格。

输出：在 A1 中显示自定义字体设置。 

![todo:image_alt_text](format-cells_7.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-FormatCells.aspx-ApplyFontStyles.cs" >}}
### **设置边框**
边框可以应用于单个单元格，或者应用到一个范围内。
#### **单个单元格**
要设置单个单元格的边框：

1. 将 Aspose.Cells.GridWeb 控件添加到 Web 表单中。
1. 访问工作表。
1. 访问要进行格式化的单元格。
1. 访问单元格的样式对象。
1. 设置边框样式。
1. 以像素设置边框宽度。
1. 设置边框颜色。
1. 将样式设置为单元格样式。

**单个单元格的自定义边框设置** 

![todo:image_alt_text](format-cells_8.png)

{{% alert color="primary" %}} 

可以使用单元格的 Style.TopBorderStyle、Style.BottomBorderStyle、Style.LeftBorderStyle、Style.RightBorderStyle 属性为每条边框线设置不同的样式。

{{% /alert %}} 

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-FormatCells.aspx-ApplyBorderStyles.cs" >}}
#### **单元格范围**
在一系列单元格上设置边框：

1. 将 Aspose.Cells.GridWeb 控件添加到 Web 表单。
1. 访问所需的工作表
1. 实例化 WebBorderStyle 类的对象
1. 将边框的样式设置为实线或虚线等
1. 以像素设置边框的宽度
1. 设置边框的颜色
1. 将存储在 WebBorderStyle 对象中的边框设置应用于指定范围的单元格

**具有自定义边框设置的单元格范围** 

![todo:image_alt_text](format-cells_9.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-FormatCells.aspx-ApplyRangeBorderStyles.cs" >}}
### **设置数字格式**
Aspose.Cells.GridWeb 支持设置数字格式。 有 59 种内置数字格式。 要查看它们，请参阅[支持的数字格式列表](/cells/zh/net/aspose-cells-gridweb/list-of-supported-number-formats/)

所有内置的数字格式都位于 NumberType 枚举中。 要使用内置数字格式，请使用单元格对象的 SetNumberType 方法将 NumberType 设置为 NumberType 枚举中的数字格式。

要设置自定义数字格式，请使用单元格的 SetCustom 方法。

**应用于 B1 和 B2 的数字格式设置** 

![todo:image_alt_text](format-cells_10.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-FormatCells.aspx-ApplyNumberFormats.cs" >}}
