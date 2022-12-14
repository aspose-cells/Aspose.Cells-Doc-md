---
title: 添加和引用命名范围
type: docs
weight: 120
url: /zh/net/add-and-reference-named-ranges/
---
{{% alert color="primary" %}} 

通常，列和行标签用于唯一引用单元格。但是您可以创建描述性名称来表示单元格、单元格区域、公式或常量值。这个单词**姓名**可以指表示单元格、单元格范围、公式或常量值的字符串。例如，使用易于理解的名称（例如 Products）来指代难以理解的范围（例如 Sales!C20:C30）。标签可用于引用同一工作表上数据的公式中；如果你想在另一个工作表上表示一个范围，你可以使用一个名称。**命名范围**是 Microsoft Excel 最强大的功能之一。用户可以为范围指定一个名称并在公式中使用该名称。 Aspose.Cells.GridWeb 支持此功能。

{{% /alert %}} 
## **在公式中添加/引用命名范围**
GridWeb 控件提供了两个类（GridName 和 GridNameCollection）用于处理命名范围。以下代码片段将帮助您了解如何创建命名范围并在公式中访问它。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-AccessNamedRanges.aspx-AddNamedRange.cs" >}}
