---
title: Aspose.Cells for .NET 19.7 Sürüm Notları
type: docs
weight: 60
url: /tr/net/aspose-cells-for-net-19-7-release-notes/
---
{{% alert color="primary" %}} 

 Bu sayfa için sürüm notları içerir[Aspose.Cells for .NET 19.7](https://www.nuget.org/packages/Aspose.Cells/19.7.0).

{{% /alert %}} 

|**Anahtar**|**Özet**|**Kategori**|
|:- |:- |:- |
|CELLSNET-42029|Dönüşümün ilerleyişini size bildiren bir tür Geri Arama olayı/mekanizması ekleme desteği|Yeni özellik|
|CELLSNET-46791|Daha fazla görünümü destekler, ancak özel görünümü desteklemez|Yeni özellik|
|CELLSNET-46808|XLS dosyasının tablo tek hücrelerini okuma desteği.|Yeni özellik|
|CELLSNET-46775|Gruplanmış şeklin genişliği ayarlanamaz|Artırma|
|CELLSNET-46785|Aynı kelimeler için kısaltma durumu farklıdır: HtmlSaveOptions ve HTMLLoadOptions, JsonLayoutOptions ve JSONUtility, ODSLoadOptions ve OdsSaveOptions.|Artırma|
|CELLSNET-46811|XLS dosyasının HeadingPairs ve TitlesOfParts etiketlerini destekler.|Artırma|
|CELLSNET-46783|CalculateFormula çok yavaş|Verim|
|CELLSNET-46746|CalculateFormula - formüller çizelgeleri etkilemez|Böcek|
|CELLSNET-46772|Grafiklerin eksik olması nedeniyle oluşturulan hatalı PDF|Böcek|
|CELLSNET-46802|Grafik, XLS'de PDF'den farklı şekilde işlendi|Böcek|
|CELLSNET-46806|Birleşik Grafik, PDF'ye yanlış işleniyor|Böcek|
|CELLSNET-41449|Karmaşık PivotTable dosyalarıyla XLSB|Böcek|
|CELLSNET-43921|XLSX'i XLSB'ye dönüştürmek bozuk dosya üretiyor|Böcek|
|CELLSNET-44593|Çıktı Excel dosyası, HTML'yi Excel'e dönüştürürken iyi değil|Böcek|
|CELLSNET-46794|Cells HTML, XLSX'e dönüştürüldüğünde kayma|Böcek|
|CELLSNET-46809|Koşullu biçimler, sütundaki (B, C ve D sütunları) tüm hücreleri boşalttı|Böcek|
|CELLSNET-46778|CalculateFormula(), UNICHAR() tasvirini bozar|Böcek|
|CELLSNET-46781|System.Globalization.CultureInfo.CurrentCulture değiştirildi|Böcek|
|CELLSNET-46244|GridDesktop Kopyala ve Yorum hatalarıyla yapıştır|Böcek|
|CELLSNET-46774|Büyük bir dosyayı PDF'ye dönüştürürken satırlardaki metin bozuk|Böcek|
|CELLSNET-46798|Excel'i PDF'ye dönüştürme sorunu|Böcek|
|CELLSNET-46797|Excel sayfasını BMP/Tiff'e dönüştürürken altı çizili yazı tipi stili yoksayılır|Böcek|
|CELLSNET-46664|HeadingPairs ve TitlesOfParts etiketleri, temizlenmiş XLS'yi tekrar XLSM dosya formatına dönüştürdükten sonra tekrar geri yüklenir|Böcek|
|CELLSNET-46782|Smart Marker, çapraz tablo formül referansını güncellemez|Böcek|
|CELLSNET-46784|Akıllı İşaretçiler - JSON liste nesnelerini özelliklere sahip olarak görüntüleme sorunu|Böcek|
|CELLSNET-46800|Aç/Kaydet, CheckBox.AlternativeText'i kaldırır|Böcek|
|CELLSNET-46807|XLS'yi PDF'ye dönüştürürken metnin bir kısmı eksik|Böcek|
|CELLSNET-42168|IndexOutOfRangeException: Workbook.SaveToStream'de|İstisna|
|CELLSNET-46248|HTML dosyası okunurken istisna atılıyor.|İstisna|
|CELLSNET-46792|Belirli çalışma kitabındaki boş sütunları silmeye çalışırken istisna|İstisna|
|CELLSNET-46799|XLSX dosyası PDF'ye dönüştürülürken ortaya çıkan istisna|İstisna|
|CELLSNET-46803|Bir XLSX dosyası yüklenirken "Nesne referansı bir nesnenin örneğine ayarlanmadı" istisnası|İstisna|
### **Herkese Açık API ve Geriye Dönük Uyumsuz Değişiklikler**
Aşağıda, API numaralı telefon numarasına eklenen, yeniden adlandırılan, kaldırılan veya kullanımdan kaldırılan üyeler gibi genele açık olarak yapılan tüm değişikliklerin ve Aspose.Cells for .NET numaralı telefona yapılan geriye dönük uyumlu olmayan değişikliklerin bir listesi bulunmaktadır. Listelenen herhangi bir değişiklikle ilgili endişeleriniz varsa lütfen şu adrese bildirin: Aspose.Cells destek forumu.
#### **HTMLLoadOptions sınıfını geçersiz kılar ve HtmlLoadOptions sınıfını ekler**
Bunun yerine HtmlLoadOptions sınıfını kullanın.
#### **ODSLoadOptions sınıfını geçersiz kılar ve OdsLoadOptions sınıfını ekler**
Bunun yerine OdsLoadOptions sınıfını kullanın.
#### **JSONUtility sınıfını geçersiz kılar ve JsonUtility sınıfını ekler**
Bunun yerine JsonUtility sınıfını kullanın.
#### **Aspose.Cells.ODS ad alanını Aspose.Cells.Ods olarak güncelleyin ve ODS* sınıflarını/enums/özellikleri Ods olarak güncelleyin**
Bunun yerine güncellenmiş sınıfları/enums/özellikleri kullanın.
#### **IPageSavingCallback arabirimini ekler**
Sayfa kaydetme işleminin ilerleyişini kontrol edin/gösterin.
#### **PageSavingArgs sınıfını ekler**
Sayfa kaydetme işlemi için bilgi.
#### **PageStartSavingArgs sınıfını ekler**
Bir sayfa için bilgi kaydetme işlemi başlar.
#### **PageEndSavingArgs sınıfını ekler**
Bir sayfa için bilgi kaydetme işlemi sona erer.
#### **PdfSaveOptions.PageSavingCallback özelliğini ekler**
Sayfa kaydetme işleminin ilerleyişini kontrol edin/gösterin.
