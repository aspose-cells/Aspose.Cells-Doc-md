﻿---
title: Karmaşık Kriterleri Karşılayan Kayıtları Görüntülemek için Microsoft Excel'in Gelişmiş Filtresini Uygulayın
type: docs
weight: 190
url: /tr/java/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/
---
## **Olası Kullanım Senaryoları**
 Microsoft Excel başvuru yapmanızı sağlar*Gelişmiş Filtre* karmaşık ölçütleri karşılayan kayıtları görüntülemek için çalışma sayfası verilerinde. Gelişmiş Filtre'yi Microsoft Excel ile uygulayabilirsiniz.*Veri > Gelişmiş*Bu ekran görüntüsünde gösterildiği gibi komut.

![yapılacaklar:resim_alternatif_metin](apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria_1.png)

Aspose.Cells ayrıca Gelişmiş Filtreyi uygulamanıza olanak tanır.[Worksheet.advancedFilter()](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#advancedFilter\(boolean,%20java.lang.String,%20java.lang.String,%20java.lang.String,%20boolean\)) yöntem. Tıpkı Microsoft Excel gibi aşağıdaki parametreleri kabul eder.

**isFiltre**

Listeyi yerinde filtreleyip filtrelemediğini gösterir.

**liste aralığı**

Liste aralığı.

**Ölçüt aralığı**

Kriter aralığı.

**kopyala**

Verilerin kopyalandığı aralık.

**Yalnızca benzersiz Kayıt**

Yalnızca benzersiz satırları görüntüleme veya kopyalama.
## **Karmaşık Kriterleri Karşılayan Kayıtları Görüntülemek için Microsoft Excel'in Gelişmiş Filtresini Uygulayın**
Aşağıdaki örnek kod, üzerinde gelişmiş filtreyi uygular.[Örnek Excel Dosyası](48496702.xlsx) ve oluşturur[Çıktı Excel Dosyası](48496705.xlsx). Ekran görüntüsü, karşılaştırma için her iki dosyayı da gösterir. Ekran görüntüsünde görebileceğiniz gibi, çıktı Excel dosyasında veriler karmaşık kriterlere göre filtrelenmiştir.

![yapılacaklar:resim_alternatif_metin](apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria_2.png)
## **Basit kod**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-ApplyAdvancedFilterOfMicrosoftExcel.java" >}}