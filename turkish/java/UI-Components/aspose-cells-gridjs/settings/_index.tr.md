---
title: GridJs için Ayarlar
type: docs
weight: 250
url: /tr/java/aspose-cells-gridjs/settings/
description: Bu makale GridJs için ayarları açıklar.
keywords: GridJs, ayarlar, GridWorkbookSettings
aliases:
  - /java/aspose-cells-gridjs/how-to-use-setting/
  - /java/aspose-cells-gridjs/work-with-setting/
---


GridWorkbookSettings'ı belirterek ayarlayabileceğimiz bazı ayarlarımız vardır:


- [**GridWorkbookSettings**](https://reference.aspose.com/cells/java/aspose.cells.gridjs/GridWorkbookSettings)


Örneğin, aşağıdaki kod, Dosya'nın açılması sırasında hesaplamanın durdurulması için ReCalculateOnOpen özelliğini false olarak ayarlar:
```JAVA
   GridJsWorkbook gw = new GridJsWorkbook();
   GridWorkbookSettings gws = new GridWorkbookSettings();
   //do not re-calculate all formulas on opening the file.
    gws.setReCalculateOnOpen(false);
    gw.setSettings(gws);
    gw.importExcelFile(@"c:\test.xlsx");
```
 aşağıdaki kod, dosyanın yazarını ayarlar:
```JAVA
   GridJsWorkbook gw = new GridJsWorkbook();
   GridWorkbookSettings gws = new GridWorkbookSettings();
   //set author.
    gws.setAuthor("peter");
    gw.setSettings(gws);
    gw.importExcelFile(@"c:\test.xlsx");
```
Bu sınıfta daha fazla ayarı kontrol edebilirsiniz.

