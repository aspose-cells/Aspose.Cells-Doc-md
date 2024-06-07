---
title: 使用格式刷
type: docs
weight: 80
url: /zh/net/aspose-cells-griddesktop/use-format-painter/
keywords: GridDesktop，格式刷
description: 本文介绍了GridDesktop中的格式刷。
---

{{% alert color="primary" %}} 

格式刷是MS Excel的一项功能，已经在Aspose.Cells.GridDesktop中适用。它是一个非常好的功能。 对于尚未使用过此功能的人来说，格式刷允许用户将任何焦点单元格的格式设置应用到另一个单元格上。 此功能的实现非常简单。 在本主题中，我们也将涵盖这一点。

{{% /alert %}} 
## **使用格式刷**
**格式刷**功能要求用户选择要应用在其他单元格上的格式设置的单元格，然后调用**GridDesktop**的**StartFormatPainter**方法。格式刷有两种模式，如下：

- **使用一次格式刷**
- **始终使用格式刷**
### **一次使用格式刷**
如果开发人员只想使用一次格式刷功能，将焦点单元格的格式设置应用于单个单元格，那么他们可以通过调用**StartFormatPainter**方法并向其传递**false**值来实现。 这个**false**值将永远禁止格式刷功能。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-UsingFormatPainter-UseOnce.cs" >}}
### **始终使用格式刷**
当我们需要在多个单元格上应用格式设置时，始终使用格式刷是一个有用的功能。 开发人员可以通过简单地调用**StartFormatPainter**方法并向其传递**true**值来实现此功能。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-UsingFormatPainter-UseAlways.cs" >}}


这种格式刷会一直持续涂画，除非我们停止它。 因此，要停止格式刷一直涂画，我们可以简单地调用**GridDesktop**的**EndFormatPainter**方法。

{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-UsingFormatPainter-EndUse.cs" >}}
