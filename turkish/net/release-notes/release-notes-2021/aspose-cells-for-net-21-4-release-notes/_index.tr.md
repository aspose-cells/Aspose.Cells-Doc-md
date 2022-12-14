---
title: Aspose.Cells for .NET 21.4 Sürüm Notları
type: docs
weight: 9
url: /tr/net/aspose-cells-for-net-21-4-release-notes/
---
{{% alert color="primary" %}}

 Bu sayfa için sürüm notları içerir[Aspose.Cells for .NET 21.4](https://www.nuget.org/packages/Aspose.Cells/21.4.0).

{{% /alert %}}

|**Anahtar**|**Özet**|**Kategori**|
|:- |:- |:- |
|CELLSNET-47891|Önbellek etkinken görüntü stili alma desteği|Yeni özellik|
|CELLSNET-47922|Excel'de hücre koordinatlarıyla verileri HTML'ye dönüştürme|Artırma|
|CELLSNET-47924|BouncyCastle'ın API ile Kriptoyu Uygulayın|Artırma|
|CELLSNET-47951|XSD tarafından desteklenen XML haritaları|Artırma|
|CELLSNET-47206|Yatay Akıllı İşaretleyiciler ve iç içe geçmiş veri kaynağı ile verileri gruplama|Artırma|
|CELLSNET-47888|İstenen çıktıyı elde etmek için gereken uygun SmartMarker'lar|Artırma|
|CELLSNET-47918|Akıllı işaretçilerle birlikte daraltılabilir satırlar|Artırma|
|CELLSNET-47953|.xlsx dosyalarına .webp görüntüsü ekleme desteği.|Artırma|
|CELLSNET-47916|HTML stil etiketi, 4 Gb bellek tüketir ve çalışma kitabına yüklenirken çöküyor|Verim|
|CELLSNET-46869|WordArts ve şekiller PDF'de düzgün şekilde oluşturulmuyor|Böcek|
|CELLSNET-47890|Pdf dönüştürme sırasında çizgiler kayacak|Böcek|
|CELLSNET-47858|Şekiller HTML ve PDF'de düzgün şekilde oluşturulmuyor|Böcek|
|CELLSNET-47907|Excel'i HTML'ye dönüştürürken grafiğin yerleşimi değiştirildi|Böcek|
|CELLSNET-47856|Pivot tablolarla XLSX'ten PDF'e dönüştürme sorunu|Böcek|
|CELLSNET-47846|GridWeb uygulaması, son DevExpress bileşenleriyle uyumsuz|Böcek|
|CELLSNET-47923|Calibri dışında varsayılan yazı tipine sahip çalışma kitabı için uygun olmayan sayfa düzeni görünümü|Böcek|
|CELLSNET-47965| Excel'den PDF'e Dönüştürme - Belge sayfaları karışık|Böcek|
|CELLSNET-46161|Çıktı PDF'sinde eğik metin doğru şekilde gösterilmiyor|Böcek|
|CELLSNET-47917|Excel Çalışma Sayfasından Oluşturulan PDF'de Dağınık Pasta Grafik Etiketleri|Böcek|
|CELLSNET-47919|Grafiklerden çıkarılan yanlış maksimum değer|Böcek|
|CELLSNET-46363|Yuvalanmış yapı, XLSX'e düzgün şekilde aktarılmaz|Böcek|
|CELLSNET-47838|Yerel grafik renk paleti korunmaz|Böcek|
|CELLSNET-47910|Range.Copy, koşullu biçimlendirmeyi hatalı bir şekilde günceller|Böcek|
|CELLSNET-47931|Birden fazla seçenek aynı anda ayarlandığında Style.SetBorder() çöküyor|Böcek|
|CELLSNET-47937|Yazar meta verisi özelliği güncellenmedi|Böcek|
|CELLSNET-47958|Yüklenen çalışma kitabında eksik sayfa|Böcek|
|CELLSNET-47976|FontSettings kullanılırken biçim uygulanmadı|Böcek|
|CELLSNET-47935|PivotTable.CalculateData() çağrılırken istisna atılıyor|İstisna|
|CELLSNET-47940|Özel bir mht dosyası açılırken bir İstisna atılır.|İstisna|
|CELLSNET-47944|Dilimleyici şeklini görüntüye dönüştürürken Boş İstisna|İstisna|
|CELLSNET-47932|Garip formüle sahip özel bir xlsx dosyası yüklenirken Boş İstisna.|İstisna|
|CELLSNET-47963|Aralık PNG'ye dönüştürülürken parametre geçerli bir istisna değil|İstisna|
|CELLSNET-47967|Bir XLS dosyasını kaydederken taşma hatası|İstisna|
|CELLSNET-47921|Özel bir xlsx dosyası yüklenirken Boş İstisna|İstisna|
|CELLSNET-47945|Özel bir html dosyası yüklenirken Boş İstisna|İstisna|
|CELLSNET-47949|Yeni çalışma kitabı açıldığında geçersiz küçük birim istisnası atılıyor|İstisna|
|CELLSNET-47950|Kopyalanan bir çalışma kitabını kaydederken NullReferenceException|İstisna|
|CELLSNET-47961|pivotCacheRecords1.xml olmadığında boş istisna.|İstisna|
|


## **Herkese Açık API ve Geriye Dönük Uyumsuz Değişiklikler**

Aşağıda, API numaralı telefon numarasına eklenen, yeniden adlandırılan, kaldırılan veya kullanımdan kaldırılan üyeler gibi genele açık olarak yapılan tüm değişikliklerin ve Aspose.Cells for .NET numaralı telefona yapılan geriye dönük uyumlu olmayan değişikliklerin bir listesi bulunmaktadır. Listelenen herhangi bir değişiklikle ilgili endişeleriniz varsa lütfen şu adrese bildirin: Aspose.Cells destek forumu.

### **Çalışma Kitabı ve Çalışma Sayfası için StartAccessCache()/CloseAccessCache() yöntemlerini ekler.**

Kullanıcılara daha iyi performansla toplu modda verilere erişme yeteneği sağlayın.

### **TxtSaveOptions.ExportQuotePrefix ve TxtLoadOptions.TreatQuotePrefixAsValue özelliklerini ekler.**

Kullanıcılara, CSV/TSV dosyalarını dışa/içe aktarırken hücrenin değerinin baştaki tek tırnak işaretiyle nasıl yapılacağına karar verme yeteneği sağlayın.

### **GlobalizationSettings.GetCollationKey(string,bool) ve Compare(string,string,bool) yöntemlerini ekler.**

Kullanıcılara varsayılan dize karşılaştırma kurallarını geçersiz kılma olanağı sağlayın. Bazı yerel ayarlar veya dize değerleri için, dize karşılaştırmasının varsayılan kuralı beklenen kural olmayabilir (formül hesaplama, sıralama vb. gibi bazı özelliklerin sonucu ms excel'de olması gerekenden farklıdır). Böyleyse, kullanıcı bu yöntemleri beklenen kuralla geçersiz kılabilir (örneğin, kullanıcı yoğun bakım kitaplığının uygulamasını kullanabilir).

### **Enum ImageType.WebP'yi ekler.**

Weppy görüntüsünü temsil eder.

### **OleObject.SetEmbeddedObject() yöntemini ekler.**

Simgenin otomatik olarak güncellenip güncellenmediğini kontrol etmek için.

### **WorkbookDesigner.LineByLine özelliğini ekler.**

Akıllı işaretleyicilerin satır satır işlenip işlenmediğini gösterir.

### **HtmlSaveOptions.ExportCellCoordinate? özelliğini ekler.**

Dosyayı html'ye kaydederken boş olmayan hücrelerin excel koordinatlarının dışa aktarılıp aktarılmadığını gösterir. Varsayılan değer false'tur. Çıktı html'sini excel'e aktarmak istiyorsanız, lütfen varsayılan değeri koruyun.

### **AutoFitterOptions.DefaultEditLanguage özelliğini ekler.**

 Varsayılan düzenleme dilini alır veya ayarlar.

