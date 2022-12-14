---
title: Pivot Tablo için Genelleştirme Ayarlarını Özelleştirme
type: docs
weight: 20
url: /tr/java/customize-globalization-settings-for-pivot-table/
---
## **Olası Kullanım Senaryoları**

 Bazen özelleştirmek istersiniz*Özet Toplam, Alt Toplam, Genel Toplam, Tüm Öğeler, Birden Çok Öğe, Sütun Etiketleri, Satır Etiketleri, Boş Değerler*gereksinimlerinize göre metin. Aspose.Cells, bu tür senaryolarla başa çıkmak için pivot tablonun genelleştirme ayarlarını özelleştirmenize olanak tanır. Etiketleri Arapça, Hintçe, Lehçe vb. diğer dillere değiştirmek için de bu özelliği kullanabilirsiniz.

## **Pivot Tablo için Genelleştirme Ayarlarını Özelleştirme**

 Aşağıdaki örnek kod, pivot tablo için genelleştirme ayarlarının nasıl özelleştirileceğini açıklar. Bir sınıf oluşturur*ÖzelPivotTableGlobalizationSettings* bir temel sınıftan türetilen[**KüreselleşmeAyarları**](https://reference.aspose.com/cells/java/com.aspose.cells/GlobalizationSettings) ve gerekli tüm yöntemlerini geçersiz kılar. Bu yöntemler için özelleştirilmiş metni döndürür.*Özet Toplam, Alt Toplam, Genel Toplam, Tüm Öğeler, Birden Çok Öğe, Sütun Etiketleri, Satır Etiketleri, Boş Değerler* . Sonra bu sınıfın nesnesini şuna atar:[**WorkbookSettings.GlobalizationSettings**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#GlobalizationSettings) Emlak. Kod şunu yükler:[kaynak excel dosyası](40468491.xlsx) pivot tabloyu içeren, verilerini yeniler, hesaplar ve şu şekilde kaydeder:[çıktı PDF dosyası](40468490.pdf) . Aşağıdaki ekran görüntüsü, örnek kodun çıktı PDF üzerindeki etkisini gösterir. Ekran görüntüsünde görebileceğiniz gibi, pivot tablonun farklı bölümleri artık geçersiz kılınan yöntemlerle döndürülen özelleştirilmiş bir metne sahiptir.[**KüreselleşmeAyarları**](https://reference.aspose.com/cells/java/com.aspose.cells/GlobalizationSettings)sınıf.

![yapılacaklar:resim_alternatif_Metin](customize-globalization-settings-for-pivot-table_1.png)

## **Basit kod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-PivotTables-CustomizeGlobalizationSettingsforPivotTable-1.java" >}}
