---
title: 忽略样式以获得更好的 GridWeb 性能
type: docs
weight: 1060
url: /zh/net/aspose-cells-gridweb/ignorestylewithnodata
description: 本文介绍如何使用 IgnoreStyleWithNoData 为 Aspose.Cells.GridWeb 库获得更好的性能。
keywords: performance
---
## **可能的使用场景**
请用[GridWeb.IgnoreStyleWithNoData](https://reference.aspose.com/cells/net/aspose.cells.gridweb/mainweb/ignorestylewithnodata)属性以从工作簿中加载较少需要的行/列。
 
## **在加载工作簿时获得更好的性能**
请检查[示例 excel 文件](largerowswithstyle.xlsx) 

当设置 IgnoreStyleWithNoData = true;

如您所见，它显示行（到 15）和列（到 L），它不会显示单元格中没有数据的最后连续行和列。因此加载时间会更少。

![忽略样式的工作簿](ignorestyletrue.png)


当设置IgnoreStyleWithNoData = false时；（默认值为false）

如您所见，它显示了更多的行（至 500）和列（至 CZ）

从第16行到第500行，部分单元格设置了边框样式，但单元格中没有任何数据。

从M列到CZ列，部分单元格设置了边框样式，但单元格中没有数据。

![没有忽略样式的工作簿](ignorestylefalse.png)
 
 
 