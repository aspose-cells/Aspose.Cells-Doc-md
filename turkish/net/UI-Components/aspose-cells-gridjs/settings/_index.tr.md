---
title: GridJ'ler için ayarlar
type: docs
weight: 250
url: /tr/net/aspose-cells-gridjs/settings/
description: Bu makalede, GridJ'ler için ayar açıklanmaktadır.
keywords: settings
---
set GridWorkbookSettings ile belirtebileceğimiz bazı ayarlar var:

 
- **[GridWorkbookSettings](https://reference.aspose.com/cells/net/aspose.cells.gridjs/GridWorkbookSettings)**


Örneğin, aşağıdaki kod, dosyayı açarken caculate'i durdurmak için ReCalculateOnOpen'ı false olarak ayarlar:
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
 