---
title: Aspose.Cells.GridJs Temelleri
type: docs
weight: 250
url: /tr/net/aspose-cells-gridjs/basics/
keywords: GridJs
description: Bu makale, GridJs için bir web uygulaması kurmanın temel adımlarını tanıtır.
---

## GridJs'in Temelleri

Aspose.Cells.GridJs, kullanıcıların elektronik tablo göstermelerini/düzenlemelerini hızlı ve kolay bir şekilde geliştirmelerine olanak tanıyan bir .NET standart kütüphanesidir. 

Aspose.Cells.GridJs popüler elektronik tablo (XLS, XLSX, XLSM, XLSB,  CSV, SpreadsheetML, ODS) dosya formatlarını içe aktarmayı destekler.

Ayrıca Excel dosyalarını PDF, HTML vb. formatlara dışa aktarmayı da sağlar. Aşağıda GridJs web uygulamasını geliştirmek için temel adım adımları bulunmaktadır.

- Kendi önbellek depolama iş mantığı yazmak için GridCacheForStream'i uygulayın.
- Elektronik tablo dosyasından json almak için bir denetleyici işlemi kurun. GridJsWorkbook.ImportExcelFile ve GridJsWorkbook.ExportToJson API'lerini kullanabilirsiniz, GridJs otomatik olarak önbelleğe eşit dosyayı saklayacaktır.
- Güncelleme işlemi için json almak için bir denetleyici işlemi kurun. GridJsWorkbook.UpdateCell API'sini kullanabilirsiniz, GridJs önbellekte güncelleme işlemini gerçekleştirecek ve güncellenmiş json'ı dönecektir.
- Elektronik tablodaki resim/şekil dosyalarının URL'sini almak için bir denetleyici işlemi kurun, GridJs otomatik olarak önbellekteki tüm resim/şekilleri zipleyecektir. Bunun için GridCacheForStream.GetFileUrl API'sini kullanacaktır.
- Dosyayı önbellekten almak için bir denetleyici işlemi kurun, böylece önbellekteki resim/şekiller zip dosyasını ya da elektronik tablo dosyasını alabiliriz. Bunun için GridCacheForStream.LoadStream API'sini kullanacaktır.
- Elektronik tabloyu indirmek için bir denetleyici işlemi kurun. GridJsWorkbook.SaveToCacheWithFileName API'sini kullanabilirsiniz.

Aşağıda Aspose.Cells.GridJs'in kullanımını gösteren temel bir demo bulunmaktadır: https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Examples_GridJs 

Herhangi bir sorunuz, gereksiniminiz veya yardıma ihtiyacınız varsa lütfen aşağıdaki web sitesine geri bildirimde bulunun: https://forum.aspose.com/c/cells/9
