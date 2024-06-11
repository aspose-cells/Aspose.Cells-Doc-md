---
title: 使用格式刷功能。
type: docs
weight: 80
url: /zh/net/aspose-cells-griddesktop/use-format-painter/
keywords: GridDesktop,format painter
description: 介绍GridDesktop中的格式刷功能。
---

{{% alert color="primary" %}} 

格式刷是MS Excel的一项功能，已经适用于Aspose.Cells.GridDesktop。这是一个非常好的功能。对于尚未使用此功能的用户，格式刷允许用户将任何焦点单元格的格式设置应用到另一个单元格。此功能的实现非常简单。本主题将涵盖此内容。

{{% /alert %}} 
## **使用格式刷功能**
格式刷功能需要用户选择一个希望将其格式设置应用于其他单元格的单元格，然后调用GridDesktop的StartFormatPainter方法。格式刷有两种模式如下：

- 仅使用一次格式刷
- 始终使用格式刷
### **仅使用一次格式刷**
如果开发人员只想一次性使用格式刷功能，将焦点单元格的格式设置应用到单个单元格，则可以调用StartFormatPainter方法，并传递一个false值。此false值将永远禁止格式刷功能。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-UsingFormatPainter-UseOnce.cs" >}}
### **始终使用格式刷**
始终使用格式刷是一个有用的功能，当需要对多个单元格应用格式设置时。开发人员只需调用StartFormatPainter方法，并传递true值即可实现此功能。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-UsingFormatPainter-UseAlways.cs" >}}


这种格式刷将永久继续应用，除非我们停止它。因此，要停止始终使用格式刷功能，只需简单地调用GridDesktop的EndFormatPainter方法。

{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-UsingFormatPainter-EndUse.cs" >}}
