---
title: Pivot Tablo için Küreselleştirme Ayarlarını Özelleştir
type: docs
weight: 50
url: /tr/net/customize-globalization-settings-for-pivot-table/
---

## **Olası Kullanım Senaryoları**

Bazen *Pivot Toplamı, Ara Toplam, Genel Toplam, Tüm Öğeler, Çoklu Öğeler, Sütun Etiketleri, Satır Etiketleri, Boş Değerler* metinlerini gereksinimlerinize göre özelleştirmek isteyebilirsiniz. Aspose.Cells, pivot tablosunun küreselleştirme ayarlarını özelleştirmenize olanak tanır. Bu özelliği, etiketleri Arapça, Hintçe, Lehçe vb. gibi diğer dillere değiştirmek için kullanabilirsiniz.

## **Pivot Tablo için Küreselleştirme Ayarlarını Özelleştir**

Aşağıdaki örnek kod, pivot tablosunun küreselleştirme ayarlarını nasıl özelleştireceğinizi açıklar. Bu, temel bir sınıftan türetilmiş *CustomPivotTableGlobalizationSettings* adlı bir sınıf oluşturur ve gerekli tüm yöntemleri geçersiz kılar. Bu yöntemler, *Pivot Toplamı, Alt Toplam, Genel Toplam, Tüm Öğeler, Birden Fazla Öğe, Sütun Etiketleri, Satır Etiketleri, Boş Değerler* için özelleştirilmiş metinleri döndürür. Ardından bu sınıfın nesnesini [**WorkbookSettings.GlobalizationSettings.PivotSettings**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/pivotsettings/) özelliğine atar. Kod, pivot tablosunu içeren [kaynak excel dosyası](40468488.xlsx) yükler, verilerini günceller ve hesaplar ve [çıktı PDF](40468487.pdf) olarak kaydeder. Aşağıdaki ekran görüntüsü, örnek kodun çıktı PDF üzerindeki etkisini gösterir. Ekran görüntüsünde pivot tablosunun farklı bölümlerinin, [**PivotGlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells.settings/pivotglobalizationsettings/) sınıfının geçersiz kılınmış yöntemleri tarafından döndürülen özelleştirilmiş metinleri bulunmaktadır.

![todo:image_alt_text](customize-globalization-settings-for-pivot-table_1.png)

## **Örnek Kod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-CustomizePivotTableGlobalSettings-CustomizePivotTableGlobalSettings.cs" >}}
{{< app/cells/assistant language="csharp" >}}
