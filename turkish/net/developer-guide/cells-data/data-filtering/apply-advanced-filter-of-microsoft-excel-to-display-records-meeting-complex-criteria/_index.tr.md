---
title: Microsoft Excel İleri Filtresini Kullanarak Karmaşık Kriterleri Karşılayan Kayıtları Göstermek
type: docs
weight: 280
url: /tr/net/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/
description: Microsoft Excel in karmaşık kriterleri karşılayan kayıtları görüntülemek için Aspose.Cells for .NET API sını kullanarak Microsoft Excel in Veri > Gelişmiş komutunu kullanarak gelişmiş filtre uygulamanın nasıl yapılacağını öğrenin.
keywords: Gelişmiş Filtre Uygula, Gelişmiş Filtre Ayarla, Gelişmiş Filtre Ekle, Gelişmiş Filtre Oluştur, Bir aralığa Gelişmiş Filtre ekleme hakkında bilgi 
---

## **Olası Kullanım Senaryoları**

Microsoft Excel, çalışma sayfası verilerinde karmaşık kriterlere uygun kayıtları göstermek için *İleri Filtre* uygulamanıza izin verir. Microsoft Excel ile *Veri > İleri* komutunu kullanarak İleri Filtre uygulayabilirsiniz. Bu ekran görüntüsünde gösterildiği gibi.

![todo:image_alt_text](apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria_1.png)

Aspose.Cells de, [**Worksheet.AdvancedFilter()**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/advancedfilter) yöntemini kullanarak Gelişmiş Filtre uygulamanıza izin verir. Microsoft Excel gibi, aşağıdaki parametreleri kabul eder.

**isFilter**

Listeyi yerinde filtrelemenin belirtilip belirtilmediğini gösterir.

**listRange**

Liste aralığı.

**criteriaRange**

Kriter aralığı.

**copyTo**

Verilerin kopyalanacağı aralık.

**uniqueRecordOnly**

Yalnızca benzersiz satırların gösterimi veya kopyalanması.

## **Karmaşık Kriterleri Karşılayan Kayıtları Göstermek İçin Microsoft Excel'in İleri Filtresini Uygulayın**

Aşağıdaki örnek kod, [Örnek Excel Dosyası](48496692.xlsx)'da gelişmiş filtrelemeyi uygular ve [Çıktı Excel Dosyası](48496691.xlsx) oluşturur. Ekran görüntüsü, karşılaştırma yapmak için her iki dosyayı da göstermektedir. Ekran görüntüsü içinde görebileceğiniz gibi, çıktı Excel dosyası içinde veriler karmaşık kriterlere göre filtrelenmiştir.

![todo:image_alt_text](apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria_2.png)

## **Örnek Kod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-ApplyAdvancedFilterOfMicrosoftExcel.cs" >}}
