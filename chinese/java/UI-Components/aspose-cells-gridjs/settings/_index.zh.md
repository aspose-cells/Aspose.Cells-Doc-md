---
title: GridJs的设置
type: docs
weight: 250
url: /zh/java/aspose-cells-gridjs/settings/
description: 本文描述了GridJs的设置。
keywords: GridJs, 设置, GridWorkbookSettings
aliases:
  - /java/aspose-cells-gridjs/how-to-use-setting/
  - /java/aspose-cells-gridjs/work-with-setting/
---


我们可以通过设置GridWorkbookSettings来指定一些设置：


- [**GridWorkbookSettings**](https://reference.aspose.com/cells/java/aspose.cells.gridjs/GridWorkbookSettings)


例如，以下代码将ReCalculateOnOpen设置为false，在打开文件时停止计算：
```JAVA
   GridJsWorkbook gw = new GridJsWorkbook();
   GridWorkbookSettings gws = new GridWorkbookSettings();
   //do not re-calculate all formulas on opening the file.
    gws.setReCalculateOnOpen(false);
    gw.setSettings(gws);
    gw.importExcelFile(@"c:\test.xlsx");
```
 以下代码为文件设置作者：
```JAVA
   GridJsWorkbook gw = new GridJsWorkbook();
   GridWorkbookSettings gws = new GridWorkbookSettings();
   //set author.
    gws.setAuthor("peter");
    gw.setSettings(gws);
    gw.importExcelFile(@"c:\test.xlsx");
```
您可以在此类中查看更多设置。

