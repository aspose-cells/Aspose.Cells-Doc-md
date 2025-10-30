---
title: C++ ile Golang kullanarak Microsoft Excel’in Gelişmiş Filtreleme özelliğiyle Karmaşık Kriterlere Uyan Kayıtları Göster
linktitle: Microsoft Excel İleri Filtresini Kullanarak Karmaşık Kriterleri Karşılayan Kayıtları Göstermek
type: docs
weight: 280
url: /tr/go-cpp/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/
description: Gelişmiş filtre uygulama yollarını ve karmaşık kriterlere uyan kayıtları görüntüleme konusunda öğrenin, Aspose.Cells for C++ API kullanarak.
keywords: Gelişmiş Filtre Uygula, Gelişmiş Filtre Ayarla, Gelişmiş Filtre Ekle, Gelişmiş Filtre Oluştur, Bir aralığa Gelişmiş Filtre ekleme hakkında bilgi
---

## **Olası Kullanım Senaryoları**

Microsoft Excel, karmaşık kriterleri karşılayan kayıtları göstermek için çalışma sayfası verilerinde *Gelişmiş Filtre* uygulamanıza olanak tanır. Gelişmiş Filtre'yi *Veri > Gelişmiş* komutu ile uygulayabilirsiniz, ekran görüntüsünde gösterildiği gibi.

![todo:image_alt_text](apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria_1.png)

Aspose.Cells ayrıca [**GetAdvancedFilter()**](https://reference.aspose.com/cells/go-cpp/worksheet/getadvancedfilter/) yöntemi kullanılarak Gelişmiş Filtre'yi uygular. Tıpkı Microsoft Excel gibi, aşağıdaki parametreleri kabul eder.

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

Aşağıdaki örnek kod, [Örnek Excel Dosyası](48496692.xlsx) üzerinde gelişmiş filtreyi uygular ve [Çıktı Excel Dosyası](48496691.xlsx) oluşturur. Ekran görüntüsü her iki dosyayı karşılaştırmak için gösterir. Ekran görüntüsü içindekileri incelediğinizde, verilerin karmaşık kriterlere göre çıktı Excel dosyası içinde filtrelendiğini görebilirsiniz.

![todo:image_alt_text](apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria_2.png)

## **Örnek Kod**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ApplyAdvancedFilterOfMicrosoftExcelToDisplayRecordsMeetingComplexCriteria.go" >}}
