---
title: 使用指定名称
type: docs
weight: 110
url: /zh/net/aspose-cells-griddesktop/use-named-ranges/
keywords: GridDesktop，命名范围，名称
description: 本文介绍了GridDesktop中的命名范围。
---

{{% alert color="primary" %}} 

通常，您可以使用工作表上列和行的标签来引用这些列和行内的单元格。 但是，您可以创建描述性名称来表示单元格、单元格范围、公式或常量值。 名称一词可能指代代表单元格、单元格范围、公式或常量值的一系列字符。 例如，使用易于理解的名称，如“产品”，来引用很难理解的范围，如Sales!C20:C30，以表示单元格、单元格范围、公式或常量值。 标签可用于引用同一工作表上的数据的公式； 如果要表示另一工作表上的范围，您可能会使用名称。 **命名范围**是Microsoft中最强大的功能之一。 用户可以为命名范围分配一个名称，以便可以在公式中使用其名称引用这些单元格范围。 **Aspose.Cells.GridDesktop**支持此功能。

{{% /alert %}} 
## **在公式中添加/引用命名区域**
GridDesktop控件确实支持在Excel文件中导入/导出命名范围，它提供了两个类（**Name**和**NameCollection**）来处理命名范围。

以下代码片段将帮助您如何使用它们。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-UsingNamedRanges-1.cs" >}}
