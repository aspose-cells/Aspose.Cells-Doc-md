---
title: 使用格式刷
type: docs
weight: 80
url: /zh/net/using-format-painter/
---
{{% alert color="primary" %}} 

格式刷是Aspose.Cells.GridDesktop中适配的MS Excel的特性。这是一个非常好的功能。对于那些还没有使用过此功能的人，格式刷允许用户将任何焦点单元格的格式设置应用到另一个单元格。这个特性的实现非常简单。在本主题中，我们也将介绍这一点。

{{% /alert %}} 
## **使用格式刷**
的特点**格式刷**要求用户选择一个单元格，您希望将其格式设置应用于其他单元格，然后调用**启动格式刷**方法**网格桌面**.格式刷有以下两种模式：

- **使用一次格式刷**
- **始终使用格式刷**
### **使用一次格式刷**
如果开发人员只想使用一次格式刷功能，将焦点单元格的格式设置应用到单个单元格，那么他们可以通过调用**启动格式刷**方法并传递一个**错误的**对它的价值。这个**错误的**值将永远禁止格式刷绘制。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-UsingFormatPainter-UseOnce.cs" >}}
### **始终使用格式刷**
当我们需要在多个单元格上应用格式设置时，始终使用格式刷是一项有用的功能。开发者只需调用即可实现此功能**启动格式刷**方法并传递一个**真的**对它的价值。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-UsingFormatPainter-UseAlways.cs" >}}


这种格式画家会一直画下去，除非我们停止它。所以，要阻止格式刷一直绘画，我们可以简单地调用**EndFormatPainter**的方法**网格桌面**.

{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-UsingFormatPainter-EndUse.cs" >}}
