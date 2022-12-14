---
title: 访问工作表 Cells
type: docs
weight: 10
url: /zh/net/access-worksheet-cells/
---
{{% alert color="primary" %}} 

本主题讨论单元格，看Aspose.Cells.GridWeb最基本的特性：访问单元格。

{{% /alert %}} 
## **在工作表中访问 Cells**
每个工作表都包含一个名为 Cells 的属性，它实际上是 GridCell 对象的集合，其中 GridCell 对象表示 Aspose.Cells.GridWeb 中的一个单元格。可以使用 Aspose.Cells.GridWeb 访问任何单元格。有两种优选的方法，每一种都在下面讨论。


### **使用 Cell 名称**
所有单元格都有一个唯一的名称。例如，A1、A2、B1、B2 等。 Aspose.Cells.GridWeb 允许开发人员使用单元格名称访问任何所需的单元格。只需将单元格名称（作为索引）传递给 GridWorksheet 的 Cells 集合。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AccessCells.aspx-AccessCellByName.cs" >}}


### **使用行和列索引**
单元格也可以通过其在行和列索引方面的位置来识别。只需将单元格的行和列索引传递给 GridWorksheet 的 Cells 集合。这种方法比上面的方法更快。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AccessCells.aspx-AccessCellByRowColumnIndex.cs" >}}
