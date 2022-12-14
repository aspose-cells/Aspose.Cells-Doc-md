---
title: 格式 Cells
type: docs
weight: 40
url: /zh/net/format-grid-cells/
---
{{% alert color="primary" %}} 

本主题详细讨论如何设置单元格格式。

它涵盖了使用 Aspose.Cells.GridWeb 控件的样式对话框在 GUI 模式下格式化单元格。它还展示了如何以编程方式格式化单元格。讨论了不同的格式设置，如字体、边框和数字格式，并举例说明。

{{% /alert %}} 
## **使用样式对话框格式化 Cells**
 Cells 可以格式化[以编程方式](/cells/zh/net/format-cells/)但以所见即所得方式格式化 Aspose.Cells.GridWeb 控件中的单元格的最简单方法是使用“样式”对话框。

要使用样式对话框：
选择一系列单元格，然后右键单击并选择**格式 Cell**. 

**选择格式 Cell** 

![待办事项：图片_替代_文本](format-cells_1.png)



显示样式对话框。

**样式对话框用于格式化单元格** 

![待办事项：图片_替代_文本](format-cells_2.png)

“样式”对话框允许用户通过自定义字体和边框设置来格式化单元格。
### **自定义字体设置**
您可以使用“样式”对话框自定义以下字体设置：

- 字体名称，从列表中选择所需的字体。
- 字体样式，应用粗体、斜体等字体样式。
- 字体大小，以点为单位选择字体大小。
- 下划线，下划线文本。
- 删除线，对文本应用删除线效果。
- 水平对齐方式，选择水平对齐方式。
- 垂直对齐，选择垂直对齐。
- 字体颜色，选择一种字体颜色。
- 背景，选择背景颜色。

您可以在一个小的预览区域中检查选定的字体设置。

**自定义字体设置** 

![待办事项：图片_替代_文本](format-cells_3.png)
### **自定义边框设置**
该控件还允许用户通过在“样式”对话框中自定义边框设置来在单元格周围绘制边框。

查看边框相关选项：
点击**边框**在样式对话框中。
显示边框相关选项。

**样式对话框中的边框选项** 

![待办事项：图片_替代_文本](format-cells_4.png)

可以从“样式”对话框中选择以下边框选项：

- 边框线条样式，选择边框样式，如实线、虚线等。
- 边框线条宽度，以像素为单位选择边框宽度。
- 边框线条颜色，选择线条颜色。
- 边框线，选择边框线的编号和定位。

**自定义边框设置** 

![待办事项：图片_替代_文本](format-cells_5.png)
### **应用设置**
点击**好的**在“样式”对话框中应用更改。

**已应用字体和边框设置** 

![待办事项：图片_替代_文本](format-cells_6.png)


## **格式化 Cells 使用 API**
Cells 也可以使用 Aspose.Cells.GridWeb API 以编程方式进行格式化。每个单元格都有一个 Style 属性，代表一个 GridTableItemStyle 对象。使用 Style 属性自定义字体和边框设置。
### **设置字体**
要以编程方式自定义字体设置：

1. 将 Aspose.Cells.GridWeb 控件添加到 Web 窗体。
1. 访问工作表。
1. 访问您正在格式化的单元格。
1. 访问单元格的样式。
1. 以磅为单位设置字体大小。
1. 设置字体样式。
1. 设置前景色和背景色。
1. 设置水平和垂直对齐方式。
1. 将样式设置回单元格。

**输出：A1 中显示的自定义字体设置** 

![待办事项：图片_替代_文本](format-cells_7.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-FormatCells.aspx-ApplyFontStyles.cs" >}}
### **设置边框**
边框可以应用于单个单元格或范围。
#### **单 Cell**
设置单个单元格的边框：

1. 将 Aspose.Cells.GridWeb 控件添加到 Web 窗体。
1. 访问工作表。
1. 访问您要格式化的单元格。
1. 访问单元格的 Style 对象。
1. 设置边框样式。
1. 以像素为单位设置边框宽度。
1. 设置边框颜色。
1. 将样式设置为单元格。

**单个单元格上的自定义边框设置** 

![待办事项：图片_替代_文本](format-cells_8.png)

{{% alert color="primary" %}} 

可以使用单元格的 Style.TopBorderStyle、Style.BottomBorderStyle、Style.LeftBorderStyle、Style.RightBorderStyle 属性为每条边框线设置不同的样式。

{{% /alert %}} 

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-FormatCells.aspx-ApplyBorderStyles.cs" >}}
#### **范围Cells**
要在一系列单元格上设置边框：

1. 将 Aspose.Cells.GridWeb 控件添加到您的 Web 窗体
1. 访问所需的工作表
1. 实例化 WebBorderStyle 类的对象
1. 将边框的样式设置为实线或虚线等。
1. 以像素为单位设置边框宽度
1. 设置边框颜色
1. 将存储在 WebBorderStyle 对象中的边框设置应用于指定范围的单元格

**具有自定义边框设置的一系列单元格** 

![待办事项：图片_替代_文本](format-cells_9.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-FormatCells.aspx-ApplyRangeBorderStyles.cs" >}}
### **设置数字格式**
Aspose.Cells.GridWeb支持设置数字格式。有 59 种内置数字格式。要查看它们，请参阅此[支持的数字格式列表](/cells/zh/net/list-of-supported-number-formats/).

所有内置数字格式都在 NumberType 枚举中。要使用内置数字格式，请使用单元格对象的 SetNumberType 方法将 NumberType 设置为 NumberType 枚举中的数字格式。

要设置自定义数字格式，请使用单元格的 SetCustom 方法。

**应用于 B1 和 B2 的数字格式设置** 

![待办事项：图片_替代_文本](format-cells_10.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-FormatCells.aspx-ApplyNumberFormats.cs" >}}
