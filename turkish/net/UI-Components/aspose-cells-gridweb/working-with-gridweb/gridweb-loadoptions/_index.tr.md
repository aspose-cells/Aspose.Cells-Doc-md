---
title: GridWeb için Yükleme Seçenekleri
type: docs
weight: 90
url: /tr/net/aspose-cells-gridweb/aspose-cells-gridweb/loadoptions/
keywords: yükleme seçeneği, yükleme seçenekleri, ayar, yükle, seçenekler, seçenek
description: Bu makale, GridWeb de yükleme seçenekleriyle nasıl çalışılacağını tanıtır.
---

{{% alert color="primary" %}} 

Dosyayı içe aktarmadan önce ayarlayabileceğimiz bazı yükleme seçenekleri bulunmaktadır.

[GridLoadOptions](https://reference.aspose.com/cells/net/aspose-cells-gridweb/aspose.cells.gridweb.data/gridloadoptions/) (genel dosya için) ve [GridTxtLoadOptions](https://reference.aspose.com/cells/net/aspose-cells-gridweb/aspose.cells.gridweb.data/gridtxtloadoptions/) (csv dosyası için) kullanabiliriz	

{{% /alert %}} 
## **Diğer kodla yükle**
CSV dosyası için, aslında xlsx format dosyasında tanımlanan belirli kodlamaya sahip olmayan bir metin tabanlı dosyadır.

Bu nedenle, kullanıcılar dosyayı yüklemeden önce belirli karakter kodlamasını ayarlayabilirler.

İşte çince ile yüklemek için örnek kod:

```csharp
    GridTxtLoadOptions topt = new GridTxtLoadOptions();
    topt.Encoding = (Encoding.GetEncoding("GB2312"));
    GridWeb1.LoadOptions = topt;
    String filePath = Server.MapPath("~/workbook/chinesefile.csv");
    GridWeb1.ImportExcelFile(filePath);
```
