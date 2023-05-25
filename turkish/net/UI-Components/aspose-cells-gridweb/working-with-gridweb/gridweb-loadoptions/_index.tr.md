---
title: GridWeb için LoadOptions
type: docs
weight: 90
url: /tr/net/aspose-cells-gridweb/loadoptions/
keywords: loadoption,loadoptions,setting,
---
{{% alert color="primary" %}} 

Dosyayı içe aktarmadan önce ayarlayabileceğimiz bazı yükleme seçenekleri vardır.

 kullanabiliriz[GridLoadOptions](https://reference.aspose.com/cells/net/aspose.cells.gridweb.data/gridloadoptions/)(genel dosya için) ve[GridTxtLoadOptions](https://reference.aspose.com/cells/net/aspose.cells.gridweb.data/gridtxtloadoptions/) (csv dosyası için)
 
{{% /alert %}} 
##  ** diğer kodlama ile yükle**
CSV dosyası için, xlsx biçim dosyasında açıklanan özel kodlama olmadan, aslında metin tabanlı bir dosyadır.

Bu nedenle, kullanıcılar dosyayı yüklemeden önce belirli karakter kodlaması ayarlayabilir.

Çince ile yüklemek için örnek bir kod:

```csharp
    GridTxtLoadOptions topt = new GridTxtLoadOptions();
    topt.Encoding = (Encoding.GetEncoding("GB2312"));
    GridWeb1.LoadOptions = topt;
    String filePath = Server.MapPath("~/workbook/chinesefile.csv");
    GridWeb1.ImportExcelFile(filePath);
```