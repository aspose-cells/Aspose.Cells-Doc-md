---
title: 在单元格上应用样式
type: docs
weight: 50
url: /zh/net/aspose-cells-griddesktop/apply-style-on-cell/
keywords: GridDesktop,format,style,number formats,number format,NumberFormat
description: 该文章介绍了如何在GridDesktop的工作表中的单元格中设置或获取样式格式。
---

{{% alert color="primary" %}} 

本主题涉及在单元格上应用样式格式，我们将涵盖几乎可以用于在单元格上应用样式的所有相关属性。除了一些基本的格式设置，我们还将详细讨论如何绘制边框和设置单元格上的数字格式。

{{% /alert %}} 
## **在单元格上应用自定义样式-一个例子**
要使用Aspose.Cells.GridDesktop更改单元格的字体和颜色，请按照以下步骤操作：

- 访问任何所需的**工作表**
- 访问要应用**样式**的**单元格**
- 获取**单元格**的**样式**
- 根据您的自定义需求设置**样式**属性
- 最后，使用更新后的**样式**设置单元格的**样式**

 **样式**对象提供了许多有用的属性和方法，开发人员可以根据自己的需求自定义样式。 下面的代码演示了如何在单元格上应用自定义样式。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-ApplyStyleOnCells-ApplyStyle.cs" >}}
## **绘制单元格的边框**
使用**样式**对象，我们可以非常容易地绘制单元格的边框。 边框可以使用任何颜色绘制。 此外，开发人员还可以灵活选择要用于绘制单元格周围边框的特定线条类型。 开发人员可以使用**样式**对象的**SetBorderLine**和**SetBorderColor**方法绘制任何类型和颜色的边框。 同样，要获取任何单元格的边框信息，开发人员还可以使用**样式**对象的**GetBorderLine**和**GetBorderColor**方法。
### **边框类型**
Aspose.Cells.GridDesktop支持以下六种边框类型：

- **左侧**，代表左边框
- **右侧**，代表右边框
- **顶部**，代表顶部边框
- **底部**，代表底部边框
- **向下对角线**，代表对角线下边框
- **向上对角线**，代表对角线上边框
### **边框线类型**
一个边框由一条线组成。 更改线的类型会改变边框的外观。 Aspose.Cells.GridDesktop支持许多类型的边框线，以下是列出的：

- **无**，代表无边框
- **细线**，代表实线边框
- **中等**，代表宽度为2f的实线边框
- **虚线**，代表虚线边框
- **点线**，代表点线边框
- **粗线**，代表宽度为3f的实线边框
- **中等虚线**，代表宽度为2f的虚线边框
- **细虚线点线**，代表虚线点线边框
- **中等虚线点线**，代表宽度为2f的虚线点线边框
- **细虚线点点线**，代表虚线点点边框
- **中等虚线点点线**，代表宽度为2f的虚线点点边框
## **总结在一起 - 示例**


{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-ApplyStyleOnCells-SummingUp.cs" >}}
## **设置数字格式**
Aspose.Cells.GridDesktop还提供了各种数字格式设置。Aspose.Cells.GridDesktop提供了58种内置数字格式。要查看所有支持的数字格式的完整列表，请参阅[支持的数字格式列表](/cells/zh/net/list-of-supported-number-formats/)

所有的内置数字格式都被分配了**索引**号。 例如，**0.00E+00**数字格式的**索引**号是**11**。 要在任何单元格中使用内置数字格式，开发人员可以将**Style**对象的NumberFormat属性设置为该特定数字格式的**索引**号。 但是，如果开发人员需要自定义数字格式，则也可以使用**Style**对象的Custom属性。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-ApplyStyleOnCells-SetNumberFormat.cs" >}}
