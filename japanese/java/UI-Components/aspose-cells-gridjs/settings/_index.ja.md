---
title: # GridJsの設定
type: docs
weight: 250
url: /ja/java/aspose-cells-gridjs/settings/
description: この記事では、GridJsの設定について説明しています。
keywords: GridJs,settings,GridWorkbookSettings
aliases:
  - /java/aspose-cells-gridjs/how-to-use-setting/
  - /java/aspose-cells-gridjs/work-with-setting/
---


GridWorkbookSettingsで指定できるいくつかの設定があります :


- [**GridWorkbookSettings**](https://reference.aspose.com/cells/java/aspose.cells.gridjs/GridWorkbookSettings)


たとえば、次のコードはReCalculateOnOpenをfalseに設定して、ファイルを開くときの計算を停止します :
```JAVA
   GridJsWorkbook gw = new GridJsWorkbook();
   GridWorkbookSettings gws = new GridWorkbookSettings();
   //do not re-calculate all formulas on opening the file.
    gws.setReCalculateOnOpen(false);
    gw.setSettings(gws);
    gw.importExcelFile(@"c:\test.xlsx");
```
 次のコードは、ファイルの作成者を設定します :
```JAVA
   GridJsWorkbook gw = new GridJsWorkbook();
   GridWorkbookSettings gws = new GridWorkbookSettings();
   //set author.
    gws.setAuthor("peter");
    gw.setSettings(gws);
    gw.importExcelFile(@"c:\test.xlsx");
```
このクラスでさらなる設定を確認できます。

