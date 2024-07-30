---
title: GridJs için Ayarlar
type: docs
weight: 250
url: /tr/net/aspose-cells-gridjs/settings/
description: Bu makale GridJs için ayarları açıklar.
keywords: GridJs, ayarlar, GridWorkbookSettings
aliases:
  - /net/aspose-cells-gridjs/how-to-use-setting/
  - /net/aspose-cells-gridjs/work-with-setting/
---


GridWorkbookSettings'ı belirterek ayarlayabileceğimiz bazı ayarlarımız vardır:


- [**GridWorkbookSettings**](https://reference.aspose.com/cells/net/aspose.cells.gridjs/GridWorkbookSettings)


Örneğin, aşağıdaki kod, Dosya'nın açılması sırasında hesaplamanın durdurulması için ReCalculateOnOpen özelliğini false olarak ayarlar:
```C#
   GridJsWorkbook gw = new GridJsWorkbook();
   GridWorkbookSettings gws = new GridWorkbookSettings();
   //do not re-calculate all formulas on opening the file.
    gws.ReCalculateOnOpen = false;
    gw.Settings = gws;
    gw.ImportExcelFile(@"c:\test.xlsx");
```
 aşağıdaki kod, dosyanın yazarını ayarlar:
```C#
   GridJsWorkbook gw = new GridJsWorkbook();
   GridWorkbookSettings gws = new GridWorkbookSettings();
   //set author.
    gws.Author = "peter";
    gw.Settings = gws;
    gw.ImportExcelFile(@"c:\test.xlsx");
```
Bu sınıfta daha fazla ayarı kontrol edebilirsiniz.

