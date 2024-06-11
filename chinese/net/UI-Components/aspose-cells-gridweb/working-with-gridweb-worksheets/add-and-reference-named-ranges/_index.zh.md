---
title: 添加和引用命名区域
type: docs
weight: 120
url: /zh/net/aspose-cells-gridweb/add-and-reference-named-ranges/
keywords: GridWeb,GridName,Names
description: 本文介绍了如何在GridWeb中处理命名区域。 
---

{{% alert color="primary" %}} 

通常，列和行标签用于唯一地引用单元格。但您可以创建描述性名称来表示单元格、单元格范围、公式或常量值。单词**名称**可能指代一个表示单元格、单元格范围、公式或常量值的一串字符。例如，使用易于理解的名称，如“产品”，来引用难以理解的范围，如“销售！C20:C30”。标签可以用于引用同一工作表上的数据的公式；如果要表示另一个工作表上的范围，可以使用名称。**命名区域**是Microsoft Excel的最强大的功能之一。用户可以为一个区域分配一个名称，并在公式中使用该名称。Aspose.Cells.GridWeb支持此功能。

{{% /alert %}} 
## **在公式中添加/引用命名范围**
GridWeb控件提供了两个类（GridName和GridNameCollection）用于处理命名区域。以下代码片段将帮助您了解如何创建命名区域并在公式中访问它。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-AccessNamedRanges.aspx-AddNamedRange.cs" >}}
