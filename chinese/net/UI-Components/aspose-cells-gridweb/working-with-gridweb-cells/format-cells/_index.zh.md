---
title: 格式单元格
type: docs
weight: 40
url: /zh/net/aspose-cells-gridweb/format-grid-cell/
keywords: GridWeb，格式，样式
description: 本文介绍了如何在GridWeb中为单元格（GridCell）设置或应用样式格式。
---

{{% alert color="primary" %}} 

本主题详细讨论了如何格式化单元格。

它涵盖了使用Aspose.Cells.GridWeb控件的样式对话框在GUI模式下格式化单元格。还展示了如何以编程方式格式化单元格。讨论了不同的格式设置，如字体，边框和数字格式，并通过例子进行了说明。

{{% /alert %}} 
## **使用样式对话框格式化单元格**
单元格可以通过[编程方式](/cells/zh/net/aspose-cells-gridweb/format-cells/)进行格式化，但在Aspose.Cells.GridWeb控件中以所见即所得的方式格式化单元格的最简单方法是使用样式对话框。

要使用样式对话框：
选择一系列单元格，然后右键单击并选择**格式单元格**。 

**选择格式单元格** 

![todo:image_alt_text](format-cells_1.png)



显示样式对话框。 

**使用样式对话框格式化单元格** 

![todo:image_alt_text](format-cells_2.png)

样式对话框允许用户通过自定义字体和边框设置来格式化单元格。
### **自定义字体设置**
您可以使用样式对话框自定义以下字体设置：

- 字体名称，从列表中选择所需的字体。
- 字体样式，应用粗体，斜体等字体样式。
- 字体大小，以点为单位选择字体大小。
- 下划线，给文字加下划线。
- 删除线，对文本应用删除线效果。
- 水平对齐，选择水平对齐方式。
- 垂直对齐，选择垂直对齐方式。
- 字体颜色，选择字体颜色。
- 背景，选择背景颜色。

您可以在一个小预览区域中检查所选的字体设置。

**自定义字体设置** 

![todo:image_alt_text](format-cells_3.png)
### **自定义边框设置**
该控件还允许用户通过在样式对话框中自定义边框设置来在单元格周围绘制边框。

要查看与边框相关的选项：
在样式对话框中点击**边框**。
显示与边框相关的选项。 

**在样式对话框中的边框选项** 

![todo:image_alt_text](format-cells_4.png)

可以从样式对话框中选择以下边框选项：

- 边框线样式，选择实线、虚线等边框样式。
- 边框线宽度，以像素为单位选择边框宽度。
- 边框线颜色，选择线条颜色。
- 边框线，选择边框线的编号和定位。

**自定义边框设置** 

![todo:image_alt_text](format-cells_5.png)
### **应用设置**
在样式对话框中单击**确定**以应用更改。

**应用字体和边框设置** 

![todo:image_alt_text](format-cells_6.png)


## **使用 API 格式化单元格**
可以使用 Aspose.Cells.GridWeb API 对单元格进行程序格式化。每个单元格都有一个代表 GridTableItemStyle 对象的 Style 属性。使用该 Style 属性自定义字体和边框设置。
### **设置字体**
要以编程方式自定义字体设置：

1. 将Aspose.Cells.GridWeb控件添加到Web表单中。
1. 访问工作表。
1. 访问要格式化的单元格。
1. 访问单元格的样式。
1. 设置点数为单位的字体大小。
1. 设置字体样式。
1. 设置前景色和背景色。
1. 设置水平和垂直对齐。
1. 将样式设置回单元格。

**输出：在 A1 中显示的自定义字体设置** 

![todo:image_alt_text](format-cells_7.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-FormatCells.aspx-ApplyFontStyles.cs" >}}
### **设置边框**
可以应用边框到单个单元格或范围。
#### **单个单元格**
要设置单个单元格的边框：

1. 将Aspose.Cells.GridWeb控件添加到Web表单中。
1. 访问工作表。
1. 访问要格式化的单元格。
1. 访问单元格的样式对象。
1. 设置边框样式。
1. 将边框宽度设置为像素。
1. 设置边框颜色。
1. 将样式设置为单元格。

**针对单个单元格的自定义边框设置** 

![todo:image_alt_text](format-cells_8.png)

{{% alert color="primary" %}} 

可以使用单元格的 Style.TopBorderStyle、Style.BottomBorderStyle、Style.LeftBorderStyle 和 Style.RightBorderStyle 属性为每条边框线设置不同的样式。

{{% /alert %}} 

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-FormatCells.aspx-ApplyBorderStyles.cs" >}}
#### **单元格范围**
设置一系列单元格的边框:

1. 将 Aspose.Cells.GridWeb 控件添加到您的 Web 表单中
1. 访问所需的工作表
1. 实例化 WebBorderStyle 类的对象
1. 将边框的样式设置为实线或虚线等
1. 将边框的宽度设置为像素
1. 将边框的颜色设置为指定颜色
1. 将 WebBorderStyle 对象中保存的边框设置应用于指定单元格范围

**带有自定义边框设置的单元格范围** 

![todo:image_alt_text](format-cells_9.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-FormatCells.aspx-ApplyRangeBorderStyles.cs" >}}
### **设置数字格式**
Aspose.Cells.GridWeb 支持设置数字格式。有 59 种内置的数字格式。要查看它们，请参阅此[支持的数字格式列表](/cells/zh/net/aspose-cells-gridweb/list-of-supported-number-formats/)。

所有内置的数字格式都位于 NumberType 枚举中。要使用内置的数字格式，可以使用单元格对象的 SetNumberType 方法将 NumberType 设置为 NumberType 枚举中的数字格式。

要设置自定义的数字格式，可以使用单元格的 SetCustom 方法。

**应用于 B1 和 B2 的数字格式设置** 

![todo:image_alt_text](format-cells_10.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-FormatCells.aspx-ApplyNumberFormats.cs" >}}
