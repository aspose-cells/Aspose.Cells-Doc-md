---
title: GridJs 的设置
type: docs
weight: 250
url: /zh/net/aspose-cells-gridjs/settings/
description: 本文介绍了 GridJs 的设置。
keywords: settings
---
我们可以通过 set GridWorkbookSettings 指定一些设置：

 
- **[GridWorkbookSettings](https://reference.aspose.com/cells/net/aspose.cells.gridjs/GridWorkbookSettings)**


例如，以下代码将 ReCalculateOnOpen 设置为 false 以在打开文件时停止计算：
```C#
   GridJsWorkbook gw = new GridJsWorkbook();
   GridWorkbookSettings gws = new GridWorkbookSettings();
   //do not re-calculate all formulas on opening the file.
    gws.ReCalculateOnOpen = false;
    gw.Settings = gws;
    gw.ImportExcelFile(@"c:\test.xlsx");
```
以下代码设置文件的作者：
```C#
   GridJsWorkbook gw = new GridJsWorkbook();
   GridWorkbookSettings gws = new GridWorkbookSettings();
   //set author.
    gws.Author = "peter";
    gw.Settings = gws;
    gw.ImportExcelFile(@"c:\test.xlsx");
```
您可以在此类中检查更多设置。
 