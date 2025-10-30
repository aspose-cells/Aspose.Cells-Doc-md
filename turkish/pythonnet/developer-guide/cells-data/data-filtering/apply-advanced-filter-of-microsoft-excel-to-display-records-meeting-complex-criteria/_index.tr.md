---
title: Microsoft Excel İleri Filtresini Kullanarak Karmaşık Kriterleri Karşılayan Kayıtları Göstermek
type: docs
weight: 280
url: /tr/python-net/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/
description: Aspose.Cells for Python via .NET API kullanarak karmaşık kriterlere uyan kayıtları göstermek için Microsoft Excel in Gelişmiş Filtresini nasıl uygulayacağınızı öğrenin.
keywords: Python Excel Kütüphanesi, Python Gelişmiş Filtre Uygula, Python Gelişmiş Filtre Ayarla, Python Gelişmiş Filtre Ekle, Python Gelişmiş Filtre Oluştur, Python da Bir Aralığa Gelişmiş Filtre Nasıl Eklenir.
---

## **Olası Kullanım Senaryoları**

Microsoft Excel, çalışma sayfası verilerinde karmaşık kriterlere uygun kayıtları göstermek için *İleri Filtre* uygulamanıza izin verir. Microsoft Excel ile *Veri > İleri* komutunu kullanarak İleri Filtre uygulayabilirsiniz. Bu ekran görüntüsünde gösterildiği gibi.

![todo:image_alt_text](1.png)

Aspose.Cells for Python via .NET ayrıca aşağıdaki parametreleri kabul eden [**Worksheet.advancedFilter()**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/advanced_filter/#bool-str-str-str-bool) yöntemini kullanarak Gelişmiş Filtreyi uygulamanıza olanak tanır, bu da Microsoft Excel gibi.

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

![todo:image_alt_text](2.png)

## **Örnek Kod**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-ApplyAdvancedFilterOfMicrosoftExcel.py" >}}
{{< app/cells/assistant language="python-net" >}}
