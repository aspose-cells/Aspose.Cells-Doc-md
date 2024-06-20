---
title: # GridJsの設定
type: docs
weight: 250
url: /ja/net/aspose-cells-gridjs/settings/
description: この記事では、GridJsの設定について説明しています。
keywords: GridJs,settings,GridWorkbookSettings
---


GridWorkbookSettingsで指定できるいくつかの設定があります :


- [**GridWorkbookSettings**](https://reference.aspose.com/cells/net/aspose.cells.gridjs/GridWorkbookSettings)


たとえば、次のコードはReCalculateOnOpenをfalseに設定して、ファイルを開くときの計算を停止します :
```C#
   GridJsWorkbook gw = new GridJsWorkbook();
   GridWorkbookSettings gws = new GridWorkbookSettings();
   //do not re-calculate all formulas on opening the file.
    gws.ReCalculateOnOpen = false;
    gw.Settings = gws;
    gw.ImportExcelFile(@"c:\test.xlsx");
```
 次のコードは、ファイルの作成者を設定します :
```C#
   GridJsWorkbook gw = new GridJsWorkbook();
   GridWorkbookSettings gws = new GridWorkbookSettings();
   //set author.
    gws.Author = "peter";
    gw.Settings = gws;
    gw.ImportExcelFile(@"c:\test.xlsx");
```
このクラスでさらなる設定を確認できます。

