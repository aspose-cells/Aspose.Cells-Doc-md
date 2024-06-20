---
title: Pivot Tablo için Küreselleştirme Ayarlarını Özelleştir
type: docs
weight: 20
url: /tr/java/customize-globalization-settings-for-pivot-table/
---

## **Olası Kullanım Senaryoları**

Bazen *Pivot Toplamı, Ara Toplam, Genel Toplam, Tüm Öğeler, Çoklu Öğeler, Sütun Etiketleri, Satır Etiketleri, Boş Değerler* metinlerini gereksinimlerinize göre özelleştirmek isteyebilirsiniz. Aspose.Cells, pivot tablosunun küreselleştirme ayarlarını özelleştirmenize olanak tanır. Bu özelliği, etiketleri Arapça, Hintçe, Lehçe vb. gibi diğer dillere değiştirmek için kullanabilirsiniz.

## **Pivot Tablo için Küreselleştirme Ayarlarını Özelleştir**

Aşağıdaki örnek kod, pivot tablosu için küreselleştirme ayarlarını nasıl özelleştireceğinizi açıklar. Bu, gerekli tüm yöntemlerini geçersiz kılan bir temel sınıf [**GlobalizationSettings**](https://reference.aspose.com/cells/java/com.aspose.cells/GlobalizationSettings) türetilmiş olan *CustomPivotTableGlobalizationSettings* adlı bir sınıf oluşturur. Bu yöntemler, *Pivot Toplamı, Ara Toplam, Genel Toplam, Tüm Öğeler, Çoklu Öğeler, Sütun Etiketleri, Satır Etiketleri, Boş Değerler* için özelleştirilmiş metni döndürür. Daha sonra bu sınıfın nesnesini [**WorkbookSettings.GlobalizationSettings**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#GlobalizationSettings) özelliğine atar. Kod, pivot tablosunu içeren [kaynak excel dosyasını](40468491.xlsx) yükler, verilerini tazeleyip hesaplar ve [çıktı PDF dosyası olarak](40468490.pdf) kaydeder. Aşağıdaki ekran görüntüsü, çıktı PDF üzerinde örnek kodun etkisini gösterir. Ekran görüntüsünde, pivot tablosunun farklı bölümlerinin [**GlobalizationSettings**](https://reference.aspose.com/cells/java/com.aspose.cells/GlobalizationSettings) sınıfının geçersiz kılan yöntemleri tarafından döndürülen özelleştirilmiş metni olduğunu görebilirsiniz.

![todo:image_alt_text](customize-globalization-settings-for-pivot-table_1.png)

## **Örnek Kod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-PivotTables-CustomizeGlobalizationSettingsforPivotTable-1.java" >}}
