---
title: Pivot Tablo için Genelleştirme Ayarlarını Özelleştirme
type: docs
weight: 50
url: /tr/net/customize-globalization-settings-for-pivot-table/
---
##  **Olası Kullanım Senaryoları**

 Bazen özelleştirmek istersiniz*Pivot Toplam, Alt Toplam, Genel Toplam, Tüm Öğeler, Çoklu Öğeler, Sütun Etiketleri, Satır Etiketleri, Boş Değerler*Gereksinimlerinize göre metin. Aspose.Cells, bu tür senaryolarla başa çıkmak için pivot tablonun genelleştirme ayarlarını özelleştirmenize olanak tanır. Etiketleri Arapça, Hintçe, Lehçe vb. diğer dillere değiştirmek için de bu özelliği kullanabilirsiniz.

##  **Pivot Tablo için Genelleştirme Ayarlarını Özelleştirme**

Aşağıdaki örnek kod, pivot tablo için genelleştirme ayarlarının nasıl özelleştirileceğini açıklamaktadır. Bir sınıf oluşturur*Özel PivotTableGlobalizasyonAyarları* bir temel sınıftan türetilmiştir[**PivotGlobalizasyonAyarları**](https://reference.aspose.com/cells/net/aspose.cells.settings/pivotglobalizationsettings/)ve gerekli tüm yöntemleri geçersiz kılar. Bu yöntemler *Özet Toplam, Alt Toplam, Genel Toplam, Tüm Öğeler, Çoklu Öğeler, Sütun Etiketleri, Satır Etiketleri, Boş Değerler* için özelleştirilmiş metni döndürür. Daha sonra bu sınıfın nesnesini şuraya atar:[**WorkbookSettings.GlobalizationSettings.PivotSettings**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/pivotsettings/) mülk. Kod şunları yükler:[kaynak excel dosyası](40468488.xlsx) pivot tabloyu içeren, verilerini yenileyip hesaplayan ve farklı olarak kaydeden[çıkış PDF](40468487.pdf) dosya. Aşağıdaki ekran görüntüsü, örnek kodun PDF çıktısı üzerindeki etkisini göstermektedir. Ekran görüntüsünde görebileceğiniz gibi, pivot tablonun farklı bölümleri artık geçersiz kılınan yöntemler tarafından döndürülen özelleştirilmiş bir metne sahiptir.[**PivotGlobalizasyonAyarları**](https://reference.aspose.com/cells/net/aspose.cells.settings/pivotglobalizationsettings/)sınıf.

![yapılacak şey:image_alt_text](customize-globalization-settings-for-pivot-table_1.png)

##  **Basit kod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-CustomizePivotTableGlobalSettings-CustomizePivotTableGlobalSettings.cs" >}}
