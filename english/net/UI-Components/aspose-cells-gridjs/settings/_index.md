---
title: Settings for GridJs
type: docs
weight: 250
url: /net/aspose-cells-gridjs/settings/
description: This article describes the setting for GridJs.
keywords: GridJs,settings,GridWorkbookSettings
aliases:
  - /net/aspose-cells-gridjs/how-to-use-setting/
  - /net/aspose-cells-gridjs/work-with-setting/
---


There are some settings we can specified by set GridWorkbookSettings :

 
- [**GridWorkbookSettings**](https://reference.aspose.com/cells/net/aspose.cells.gridjs/GridWorkbookSettings)


For example, the following code set the ReCalculateOnOpen to false to stop the caculate on opening the file :
```C#
   GridJsWorkbook gw = new GridJsWorkbook();
   GridWorkbookSettings gws = new GridWorkbookSettings();
   //do not re-calculate all formulas on opening the file.
    gws.ReCalculateOnOpen = false;
    gw.Settings = gws;
    gw.ImportExcelFile(@"c:\test.xlsx");
```
 the following code set the author for the file :
```C#
   GridJsWorkbook gw = new GridJsWorkbook();
   GridWorkbookSettings gws = new GridWorkbookSettings();
   //set author.
    gws.Author = "peter";
    gw.Settings = gws;
    gw.ImportExcelFile(@"c:\test.xlsx");
```
You can check more settings in this class.
 