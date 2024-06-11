---
title: 忽略样式以获取更好的GridWeb性能
type: docs
weight: 1060
url: /zh/net/aspose-cells-gridweb/ignorestylewithnodata
description: 本文描述了如何使用IgnoreStyleWithNoData以获得更好的GridWeb性能。
keywords: GridWeb,performance
---

## **可能的使用场景**
请使用 [GridWeb.IgnoreStyleWithNoData](https://reference.aspose.com/cells/net/aspose.cells.gridweb/mainweb/ignorestylewithnodata) 属性从工作簿中加载所需的行/列较少。

## **在加载工作簿时获得更好的性能**
请查看 [样本Excel文件](largerowswithstyle.xlsx) 

当设置 IgnoreStyleWithNoData = true 时；

正如您所见，它显示了行（至15）和列（至L），不会显示最后连续的没有数据的行和列，因此加载时间会更短。

![拥有忽略样式的工作簿](ignorestyletrue.png)


当设置 IgnoreStyleWithNoData = false 时；（默认值为false）

正如您所见，它显示了更多的行（至500）和列（至CZ）

从第16行到第500行，某些单元格已设置边框样式，但是单元格内没有数据。

从M列到CZ列，某些单元格已设置边框样式，但是单元格内没有数据。

![没有忽略样式的工作簿](ignorestylefalse.png)



