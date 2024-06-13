---
title: GridJs的设置
type: docs
weight: 250
url: /zh/net/aspose-cells-gridjs/settings/
description: 本文描述了GridJs的设置。
keywords: GridJs, 设置, GridWorkbookSettings
---


我们可以通过设置GridWorkbookSettings来指定一些设置：


- [**GridWorkbookSettings**](https://reference.aspose.com/cells/net/aspose.cells.gridjs/GridWorkbookSettings)


例如，以下代码将ReCalculateOnOpen设置为false，在打开文件时停止计算：
```C#
   GridJsWorkbook gw = new GridJsWorkbook();
   GridWorkbookSettings gws = new GridWorkbookSettings();
   //do not re-calculate all formulas on opening the file.
    gws.ReCalculateOnOpen = false;
    gw.Settings = gws;
    gw.ImportExcelFile(@"c:\test.xlsx");
```
 以下代码为文件设置作者：
```C#
   GridJsWorkbook gw = new GridJsWorkbook();
   GridWorkbookSettings gws = new GridWorkbookSettings();
   //set author.
    gws.Author = "peter";
    gw.Settings = gws;
    gw.ImportExcelFile(@"c:\test.xlsx");
```
您可以在此类中查看更多设置。

