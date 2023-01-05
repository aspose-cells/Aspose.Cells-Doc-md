---
title: GridJsの設定
type: docs
weight: 250
url: /ja/net/aspose-cells-gridjs/settings/
description: この記事では、GridJs の設定について説明します。
keywords: settings
---
set GridWorkbookSettings で指定できる設定がいくつかあります。

 
- **[GridWorkbookSettings](https://reference.aspose.com/cells/net/aspose.cells.gridjs/GridWorkbookSettings)**


たとえば、次のコードは ReCalculateOnOpen を false に設定して、ファイルを開くときに caculate を停止します。
```C#
   GridJsWorkbook gw = new GridJsWorkbook();
   GridWorkbookSettings gws = new GridWorkbookSettings();
   //do not re-calculate all formulas on opening the file.
    gws.ReCalculateOnOpen = false;
    gw.Settings = gws;
    gw.ImportExcelFile(@"c:\test.xlsx");
```
次のコードは、ファイルの作成者を設定します。
```C#
   GridJsWorkbook gw = new GridJsWorkbook();
   GridWorkbookSettings gws = new GridWorkbookSettings();
   //set author.
    gws.Author = "peter";
    gw.Settings = gws;
    gw.ImportExcelFile(@"c:\test.xlsx");
```
このクラスでより多くの設定を確認できます。
 