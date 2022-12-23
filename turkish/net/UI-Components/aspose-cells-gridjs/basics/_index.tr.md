---
title: Aspose.Cells.GridJs Temelleri
type: docs
weight: 250
url: /tr/net/aspose-cells-gridjs/basics/
---
## GridJ'lerin Temelleri

 Aspose.Cells.GridJs, kullanıcıların elektronik tabloları hızlı ve kolay bir şekilde göstermek/düzenlemek için web uygulaması geliştirmelerine olanak tanıyan bir .NET standart kitaplığıdır.

Aspose.Cells.GridJs, popüler e-tablo (XLS, XLSX, XLSM, XLSB, CSV, SpreadsheetML, ODS) dosya biçimlerini içe aktarmayı destekler.

Ayrıca Excel dosyalarının PDF, HTML .etc'ye aktarılmasına da izin verir. GridJ'lerin bir web uygulamasını geliştirmek için temel işlem adımları aşağıdadır.

- Önbellek depolaması için kendi iş mantığınızı yazmak üzere GridCacheForStream'i uygulayın.
- Elektronik tablo dosyasından json almak için bir denetleyici eylemi ayarlayın. GridJsWorkbook.ImportExcelFile ve GridJsWorkbook.ExportToJson API'lerini kullanabilirsiniz, GridJ'ler forma dosyasını otomatik olarak önbellekte depolar.
- Güncelleme işlemi için json'u almak üzere bir denetleyici eylemi ayarlayın. GridJsWorkbook'u kullanabilirsiniz.
- Elektronik tablodaki resim/şekil dosyalarının url'sini almak için bir denetleyici eylemi ayarlayın, GridJs önbellekteki tüm resimleri/şekilleri otomatik olarak sıkıştırır. GridCacheForStream.GetFileUrl API'i kullanır.
- Dosyayı önbelleğe almak için bir denetleyici eylemi ayarlayın, böylece görüntüleri/şekilleri zip dosyasını veya elektronik tablo dosyasını önbelleğe alabiliriz. GridCacheForStream.LoadStream API'i kullanacaktır.
- Elektronik tabloyu indirmek için bir denetleyici eylemi ayarlayın. GridJsWorkbook.SaveToCacheWithFileName API'i kullanabilirsiniz.

 Aşağıda Aspose.Cells.GridJs kullanımını gösteren temel bir demo bulunmaktadır: https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Examples_GridJs

Herhangi bir sorunuz, gereksiniminiz veya yardıma ihtiyacınız varsa, lütfen https://forum.aspose.com/c/cells/9 web sitesine geri bildirimde bulunun.