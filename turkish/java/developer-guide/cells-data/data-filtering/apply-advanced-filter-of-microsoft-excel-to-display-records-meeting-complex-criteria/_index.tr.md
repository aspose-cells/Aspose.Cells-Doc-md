---
title: Microsoft Excel İleri Filtresini Kullanarak Karmaşık Kriterleri Karşılayan Kayıtları Göstermek
type: docs
weight: 190
url: /tr/java/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/
---

## **Olası Kullanım Senaryoları**
Microsoft Excel, çalışma sayfası verilerinde karmaşık kriterlere uygun kayıtları göstermek için *İleri Filtre* uygulamanıza izin verir. Microsoft Excel ile *Veri > İleri* komutunu kullanarak İleri Filtre uygulayabilirsiniz. Bu ekran görüntüsünde gösterildiği gibi.

![todo:image_alt_text](apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria_1.png)

Aspose.Cells ayrıca [Worksheet.advancedFilter()](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#advancedFilter\(boolean,%20java.lang.String,%20java.lang.String,%20java.lang.String,%20boolean\)) yöntemini kullanarak İleri Filtre uygulamanıza izin verir. Microsoft Excel gibi aşağıdaki parametreleri kabul eder.

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
Aşağıdaki örnek kod, [Örnek Excel Dosyası](48496702.xlsx) üzerinde İleri Filtre uygular ve [Çıkış Excel Dosyası](48496705.xlsx) oluşturur. Ekran görüntüsü, karşılaştırma amaçlı her iki dosyayı gösterir. Ekran görüntüsünde de görebileceğiniz gibi, veriler çıkış Excel dosyasında karmaşık kriterlere göre filtrelenmiştir.

![todo:image_alt_text](apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria_2.png)
## **Örnek Kod**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-ApplyAdvancedFilterOfMicrosoftExcel.java" >}}
