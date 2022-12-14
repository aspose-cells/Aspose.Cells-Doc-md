---
title: Pivot Tablo için Genelleştirme Ayarlarını Özelleştirme
type: docs
weight: 50
url: /tr/net/customize-globalization-settings-for-pivot-table/
---
## **Olası Kullanım Senaryoları**

 Bazen özelleştirmek istersiniz*Özet Toplam, Alt Toplam, Genel Toplam, Tüm Öğeler, Birden Çok Öğe, Sütun Etiketleri, Satır Etiketleri, Boş Değerler*gereksinimlerinize göre metin. Aspose.Cells, bu tür senaryolarla başa çıkmak için pivot tablonun genelleştirme ayarlarını özelleştirmenize olanak tanır. Etiketleri Arapça, Hintçe, Lehçe vb. diğer dillere değiştirmek için de bu özelliği kullanabilirsiniz.

## **Pivot Tablo için Genelleştirme Ayarlarını Özelleştirme**

 Aşağıdaki örnek kod, pivot tablo için genelleştirme ayarlarının nasıl özelleştirileceğini açıklar. Bir sınıf oluşturur*ÖzelPivotTableGlobalizationSettings* bir temel sınıftan türetilen[**KüreselleşmeAyarları**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings) ve gerekli tüm yöntemlerini geçersiz kılar. Bu yöntemler için özelleştirilmiş metni döndürür.*Özet Toplam, Alt Toplam, Genel Toplam, Tüm Öğeler, Birden Çok Öğe, Sütun Etiketleri, Satır Etiketleri, Boş Değerler*. Sonra bu sınıfın nesnesini şuna atar:[**WorkbookSettings.GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/globalizationsettings) Emlak. Kod şunu yükler:[kaynak excel dosyası](40468488.xlsx) pivot tabloyu içeren, verilerini yeniler, hesaplar ve şu şekilde kaydeder:[çıktı PDF](40468487.pdf)dosya. Aşağıdaki ekran görüntüsü, örnek kodun çıktı PDF üzerindeki etkisini gösterir. Ekran görüntüsünde görebileceğiniz gibi, pivot tablonun farklı bölümleri artık geçersiz kılınan yöntemlerle döndürülen özelleştirilmiş bir metne sahiptir.[**KüreselleşmeAyarları**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings)sınıf.

![yapılacaklar:resim_alternatif_Metin](customize-globalization-settings-for-pivot-table_1.png)

## **Basit kod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-CustomizePivotTableGlobalSettings-CustomizePivotTableGlobalSettings.cs" >}}
