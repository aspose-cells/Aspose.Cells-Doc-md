---
title: 在单元格上应用样式
type: docs
weight: 50
url: /zh/net/aspose-cells-griddesktop/apply-style-on-cell/
keywords: GridDesktop, 格式, 样式, 数字格式, 数字格式化, NumberFormat
description: 本文介绍如何在GridDesktop的工作表中的单元格中获取或设置样式格式。
---

{{% alert color="primary" %}} 

本主题涉及在单元格上应用样式格式，我们将覆盖几乎所有可以用于在单元格上应用样式的相关属性。除了一些基本的格式设置，我们还将详细讨论如何绘制边框，并在单元格上设置数字格式。

{{% /alert %}} 
## **在单元格上应用自定义样式-示例**
要使用 Aspose.Cells.GridDesktop 更改单元格的字体和颜色，请按照以下步骤操作:

- 访问任何所需的**工作表**
- 访问要应用 **样式** 的 **单元格**
- 获取 **单元格** 的 **样式**
- 根据自定义需求设置 **样式** 属性
- 最后，使用更新后的 **样式** 设置 **单元格** 的 **样式**

 **样式** 对象提供了许多有用的属性和方法，开发人员可以根据自己的需求自定义样式。在下面的代码中，演示了如何在单元格上应用自定义样式。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-ApplyStyleOnCells-ApplyStyle.cs" >}}
## **绘制单元格的边框**
使用 **样式** 对象，可以非常容易地绘制单元格的边框。边框可以用任何颜色绘制。此外，开发人员还可以灵活选择要用于在单元格周围绘制边框的特定类型的线。开发人员可以使用 **Style** 对象的 **SetBorderLine** 和 **SetBorderColor** 方法绘制任何类型和颜色的边框。类似地，要获取任何单元格的边框信息，开发人员还可以利用 **Style** 对象的 **GetBorderLine** 和 **GetBorderColor** 方法。
### **边框的类型**
Aspose.Cells.GridDesktop支持以下六种边框类型：

- **左** ，表示左边框
- **右** ，表示右边框
- **上** ，表示上边框
- **底部** ，表示底部边框
- **DiagonalDown** ，表示对角线向下的边框
- **DiagonalUp** ，表示对角线向上的边框
### **边框线的类型**
边框由一条线组成。更改线的类型会改变边框的外观。Aspose.Cells.GridDesktop支持许多种边框线类型，下面也列出了这些类型:

- **None** , 代表无边框
- **Thin** , 代表实线边框
- **Medium** , 代表宽度为2f的实线边框
- **Dashed** , 代表虚线边框
- **Dotted** , 代表点线边框
- **Thick** , 代表宽度为3f的实线边框
- **MediumDashed** , 代表宽度为2f的虚线边框
- **ThinDashDotted** , 代表虚线点线边框
- **MediumDashDotted** , 代表宽度为2f的虚线点线边框
- **ThinDashDotDotted** , 代表虚线点点线边框
- **MediumDashDotDotted** , 代表宽度为2f的虚线点点线边框
## **总结 - 示例**


{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-ApplyStyleOnCells-SummingUp.cs" >}}
## **设置数字格式**
Aspose.Cells.GridDesktop还提供了各种数字格式设置。Aspose.Cells.GridDesktop提供了58种内置数字格式。要查看所有支持的数字格式的完整列表，请参阅[支持的数字格式。](/cells/zh/net/list-of-supported-number-formats/)

所有内置数字格式都被分配了一个**索引**号。 例如，**0.00E+00**数字格式的**索引**号是**11**。要在任何单元格中使用内置数字格式，开发人员可以将**Style**对象的**NumberFormat**属性设置为该特定数字格式的**索引**号。但是，如果开发人员需要自定义数字格式，他们也可以使用**Style**对象的**Custom**属性。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-ApplyStyleOnCells-SetNumberFormat.cs" >}}
