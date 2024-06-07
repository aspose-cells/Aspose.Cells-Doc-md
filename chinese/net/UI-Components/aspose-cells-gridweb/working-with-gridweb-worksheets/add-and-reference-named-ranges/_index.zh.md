---
title: 添加和引用命名区域
type: docs
weight: 120
url: /zh/net/aspose-cells-gridweb/add-and-reference-named-ranges/
keywords: GridWeb，GridName，Names
description: 本文介绍了如何在GridWeb中使用命名区域。 
---

{{% alert color="primary" %}} 

通常，列和行标签用于唯一地引用单元格。但是，您可以创建描述性名称来表示单元格、单元格范围、公式或常量值。**名称**可能是表示单元格、单元格范围、公式或常量值的一系列字符。例如，使用易于理解的名称（如Products）来引用难以理解的范围（如Sales!C20:C30）。标签可用于引用同一工作表上的数据的公式；如果您想要表示另一工作表上的范围，可能会使用名称。**命名区域**是Microsoft Excel中最强大的功能之一。用户可以为范围指定名称，并在公式中使用该名称。Aspose.Cells.GridWeb支持此功能。

{{% /alert %}} 
## **在公式中添加/引用命名区域**
GridWeb控件提供了两个用于处理命名区域的类（GridName和GridNameCollection）。以下代码片段将帮助您了解如何创建命名区域并在公式中使用它。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-AccessNamedRanges.aspx-AddNamedRange.cs" >}}
