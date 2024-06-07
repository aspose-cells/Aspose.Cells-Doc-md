---
title: 忽略样式以获得更好的性能在GridWeb中
type: docs
weight: 1060
url: /zh/net/aspose-cells-gridweb/ignorestylewithnodata
description: 本文介绍了如何使用IgnoreStyleWithNoData来获得GridWeb中更好的性能。
keywords: GridWeb，性能
---

## **可能的使用场景**
请使用[GridWeb.IgnoreStyleWithNoData](https://reference.aspose.com/cells/net/aspose.cells.gridweb/mainweb/ignorestylewithnodata)属性从工作簿中加载所需的行/列较少。

## **加载工作簿时获得更好的性能**
请检查[示例Excel文件](largerowswithstyle.xlsx) 

当设置IgnoreStyleWithNoData = true时；

正如您所看到的，它显示行（到15）和列（到L），它不会显示最后连续的没有单元格数据的行和列，因此加载时间会更短。

![带有忽略样式的工作簿](ignorestyletrue.png)


当设置IgnoreStyleWithNoData = false时；（默认值为false）

如您所见，它显示更多的行（到500）和列（到CZ）

从第16行到第500行，一些单元格设置了边框样式，然而这些单元格中并无数据。

从M列到CZ列，一些单元格设置了边框样式，然而这些单元格中并无数据。

![没有忽略样式的工作簿](ignorestylefalse.png)



