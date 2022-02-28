---
title: Settings for GridJs
type: docs
weight: 250
url: /net/aspose-cells-gridjs/settings/
description: This article describes the setting for GridJs.
keywords: settings
---


There are some settings we can specified by set GridWorkbookSettings :

 
- **[GridWorkbookSettings](https://apireference.aspose.com/cells/net/aspose.cells.gridjs/GridWorkbookSettings)**


For example, the following code set the ReCalculateOnOpen to false to stop the caculate on opening the file :
```C#
   GridJsWorkbook gw = new GridJsWorkbook();
   GridWorkbookSettings gws = new GridWorkbookSettings();
   //do not re-calculate all formulas on opening the file.
    gws.ReCalculateOnOpen = false;
    gw.Settings = gws;
    gw.ImportExcelFile(ms, GridLoadFormat.Xlsx);
```
 the following code set the author for the file :
```C#
   GridJsWorkbook gw = new GridJsWorkbook();
   GridWorkbookSettings gws = new GridWorkbookSettings();
   //set author.
    gws.Author = "peter";
    gw.Settings = gws;
    gw.ImportExcelFile(ms, GridLoadFormat.Xlsx);
```
You can check more settings in this class.
 