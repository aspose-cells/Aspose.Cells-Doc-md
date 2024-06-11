---
title: 使用命名范围
type: docs
weight: 110
url: /zh/net/aspose-cells-griddesktop/use-named-ranges/
keywords: GridDesktop，命名范围，名称
description: 本文介绍了GridDesktop中的命名范围。
---

{{% alert color="primary" %}} 

通常，您可以使用工作表上列和行的标签来引用这些列和行内的单元格。但是您可以创建描述性名称来代表单元格、单元格范围、公式或固定值。名称可能指代表示单元格、单元格范围、公式或固定值的一串字符。例如，使用易于理解的名称，比如“Products”，来引用难以理解的范围，比如“Sales!C20:C30”。标签可以用于引用同一工作表上的数据的公式；如果要表示另一工作表上的范围，则可以使用名称。命名范围是Microsoft中功能最强大的特性之一。用户可以为命名范围分配一个名称，这样就可以在公式中使用该名称来引用这一范围的单元格。Aspose.Cells.GridDesktop确实支持此功能。

{{% /alert %}} 
## **在公式中添加/引用命名范围**
GridDesktop控件支持在Excel文件中导入/导出命名范围，它提供了两个类（名称和名称集合）来处理命名范围。

以下代码片段将帮助您了解如何使用它们。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-UsingNamedRanges-1.cs" >}}
