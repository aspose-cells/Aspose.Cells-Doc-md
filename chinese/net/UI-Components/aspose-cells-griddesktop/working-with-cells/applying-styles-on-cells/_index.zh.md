---
title: 在 Cells 上应用样式
type: docs
weight: 50
url: /zh/net/applying-styles-on-cells/
---
{{% alert color="primary" %}} 

本主题涉及在单元格上应用样式，因此我们将尝试涵盖几乎所有可用于在单元格上应用样式的内容。除了一些基本的格式设置外，我们还将详细讨论绘制边框和设置单元格的数字格式。

{{% /alert %}} 
## **在 Cell 上应用自定义样式 - 示例**
要使用 Aspose.Cells.GridDesktop 更改单元格的字体和颜色，请按照以下步骤操作：

- 访问任何想要的**工作表**
- 访问一个**Cell**我们要在其上应用**风格**
- 得到**风格**的**Cell**
- 放**风格**根据您的自定义需求属性
- 最后，设置**风格**的**Cell**与更新的

提供了许多有用的属性和方法**风格**开发人员可以使用该对象根据他们的要求自定义样式。在下面的代码中，演示了如何在单元格上应用自定义样式。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-ApplyStyleOnCells-ApplyStyle.cs" >}}
## **Cells 的绘图边框**
使用**风格**对象，我们可以很容易地绘制单元格的边框。边框可以用任何颜色绘制。此外，开发人员还可以灵活地选择用于在单元格周围绘制边框的特定类型的线条。开发者可以使用**设置边框线**和**设置边框颜色**的方法**风格**对象绘制任何类型和颜色的边框。同样，要获取任意单元格的边框信息，开发者也可以利用**获取边界线**和**获取边框颜色**的方法**风格**目的。
### **边框类型**
Aspose.Cells.GridDesktop支持的边框类型有以下六种：

- **剩下** , 代表左边框
- **正确的** 代表右边框
- **最佳** 代表上边框
- **底部** 代表底边框
- **对角向下** 代表对角线下边界
- **对角向上** 代表对角向上边框
### **边界线的类型**
边框由一条线组成。更改线条类型会更改边框的外观。 Aspose.Cells.GridDesktop支持的边框线种类很多，下面也一一列举：

- **没有任何** , 代表没有边框
- **薄的** 代表实线边框
- **中等的** 表示线宽等于2f的实线边框
- **虚线** 代表虚线边框
- **点缀的** 代表虚线边框
- **厚的** 表示线宽等于3f的实线边框
- **中虚线** 表示线宽等于 2f 的虚线边框
- **细线虚线** 代表点划线边框
- **MediumDashDotted** , 表示虚线边框，线宽等于 2f
- **ThinDashDotDotted** , 代表点划线虚线边框
- **MediumDashDotDotted** , 表示线宽等于2f的虚点虚线边框
## **总结在一起 - 示例**


{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-ApplyStyleOnCells-SummingUp.cs" >}}
## **设置数字格式**
Aspose.Cells.GridDesktop 还提供了为输入到单元格中的值设置数字格式的强大功能。 Aspose.Cells.GridDesktop 提供了 58 种内置数字格式。要查看所有支持的数字格式的完整列表，请参阅[支持的数字格式。](/cells/zh/net/list-of-supported-number-formats/)

所有内置数字格式都分配了一个**指数**数字。**例如**这**指数**数量**0.00E+00**数字格式是**11**.要在任何单元格中使用内置数字格式，开发人员可以设置 NumberFormat 属性**风格**反对**指数**该特定数字格式的数字。但是，如果开发人员需要有自己的自定义数字格式，那么他们也可以使用 Custom 属性**风格**目的。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-ApplyStyleOnCells-SetNumberFormat.cs" >}}
