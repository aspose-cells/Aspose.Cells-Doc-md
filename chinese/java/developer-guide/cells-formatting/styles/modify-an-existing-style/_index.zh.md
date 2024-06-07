---
title: 修改现有样式
type: docs
weight: 50
url: /zh/java/modify-an-existing-style/
description: 学习如何使用Microsoft Excel和Aspose.Cells for Java API在Excel中更改样式。
keywords: 修改现有样式excel、在excel Java中修改现有样式、修改现有样式excel、在excel Java中修改现有样式、更改excel中的现有样式、更改excel中的现有样式Java、如何在excel中更改样式、如何在excel中使用Java更改样式、如何在Excel中更改样式、如何使用Java更改Excel中的样式、在Excel中更改现有样式Java、在Excel中更改现有样式
---

{{% alert color="primary" %}}

要将相同的格式设置应用于单元格，需创建一个新的格式样式对象。格式样式对象是格式特性的组合，例如字体、字体大小、缩进、数字、边框、图案等，被命名保存为一组。应用时，该样式中的所有格式都将被应用。

您也可以使用现有样式，将其保存到工作簿并使用它来格式化具有相同属性的信息。

当单元格没有明确定义格式时，默认应用“Normal”样式（工作簿的默认样式）。Microsoft Excel除“Normal”样式外，还预定义了几种样式，包括逗号、货币和百分比。

Aspose.Cells允许修改这些样式中的任何一个或您定义的任何其他样式，并具有所需的属性。

{{% /alert %}}

## **使用Microsoft Excel**

要在Microsoft Excel 97-2003中更新样式:

1.在**格式**菜单上，单击**样式**。
1.从**样式名称**列表中选择要修改的样式。
1.单击**修改**。
1.使用“格式单元格”对话框中的选项卡选择要使用的样式选项。
1. 单击**确定**。
1.在**样式包括**下，指定要使用的样式特征。
1.单击**确定**以保存样式并将其应用于所选范围。

## **使用Aspose.Cells**

Aspose.Cells为更新现有样式提供了[**Style.update**](https://reference.aspose.com/cells/java/com.aspose.cells/style#update()）方法。

要更改命名样式，无论是使用Aspose.Cells动态创建的样式还是预定义的，都可以调用[**Style.update**](https://reference.aspose.com/cells/java/com.aspose.cells/style#update()）方法来反映应用于单元格或范围的样式的任何更改。

[**Style.update**](https://reference.aspose.com/cells/java/com.aspose.cells/style#update()）方法的行为类似于样式对话框中的**确定**按钮：对现有样式进行更改后，调用以实现更改。如果已经将样式应用于一系列单元格，修改样式属性并调用该方法，那些单元格的格式将自动更新

### **创建和修改样式**

此示例创建一个样式对象，将其应用于一系列单元格，并修改样式对象。修改将自动应用于应用了样式的单元格和范围。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CreatingStyle-CreatingStyle.java" >}}

### **修改现有样式**

此示例使用一个简单的模板Excel文件，其中已经应用了一个名为“百分比”的样式到一个范围。示例：

1.获取样式，
1.创建一个样式对象，
1.修改样式格式。

修改将自动应用于应用样式的范围。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ModifyExistingStyle-ModifyExistingStyle.java" >}}
