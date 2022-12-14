---
title: Aspose.Cells for .NET 19.8 Sürüm Notları
type: docs
weight: 50
url: /tr/net/aspose-cells-for-net-19-8-release-notes/
---
{{% alert color="primary" %}} 

 Bu sayfa için sürüm notları içerir[Aspose.Cells for .NET 19.8](https://www.nuget.org/packages/Aspose.Cells/19.8.0).

{{% /alert %}} 

|**Anahtar**|**Özet**|**Kategori**|
|:- |:- |:- |
|CELLSNET-46823|P-384 ve P-521 için Eliptik Eğri Dijital İmza Algoritmasını (ECDSA) Destekleyin|Yeni özellik|
|CELLSNET-46813|OLE Gömülü .MOL dosyasını ayıklamak için destek|Yeni özellik|
|CELLSNET-46822|Dahili ve harici köprüler arasındaki farkı algılama|Yeni özellik|
|CELLSNET-42334|MVC ile Aspose.Cells.GridWeb uyumluluğu|Artırma|
|CELLSNET-46804|Büyük matrisi çift değerli hesaplamak için performansı iyileştirin|Verim|
|CELLSNET-46856|Belge, 10 defadan fazla kaydedildiğinde kaydedilemiyor|Verim|
|CELLSNET-46827|XLSX'ten ODS'ye dönüştürmede eksik içerik|Böcek|
|CELLSNET-46833|Excel'den PDF'e dönüştürmede şekiller bozuk|Böcek|
|CELLSNET-46835|Çizim şekilleri, Excel'den PDF'e dönüştürmede düzgün şekilde oluşturulmuyor|Böcek|
|CELLSNET-46848|Excel'den PDF'e dönüştürmede Arapça metinle ilgili sorun|Böcek|
|CELLSNET-44973|Pivot Tablo hücrelerinin dolgu rengi ayarlanamıyor|Böcek|
|CELLSNET-46818|HTML'ye kaydederken tüm stiller dışa aktarılmaz|Böcek|
|CELLSNET-46824|Pivot kaynak verileri güncellendikten sonra özet tablo bozuldu|Böcek|
|CELLSNET-46820|Akıllı işaretçi gruplama veri sorunları|Böcek|
|CELLSNET-46840|Workbook.RemoveUnusedStyles yöntemiyle ilgili sorun|Böcek|
|CELLSNET-46853|Excel'den PDF'e dönüştürmede bazı sütunlar kırmızı renkte işlenir|Böcek|
|CELLSNET-46829|DBConnection nesnesi, DBConnection.ConnectionInfo için değer sağlamıyor|Böcek|
|CELLSNET-46830|Sorguları okuma ve yazma|Böcek|
|CELLSNET-46841|Aspose hatalarıyla belirli XLS dosyasını açma|Böcek|
|CELLSNET-46845|ImportTableOptions.InsertRows davranışındaki sorunlar|Böcek|
|CELLSNET-46846|Excel dosyası yeniden kaydedildikten sonra bozuldu|Böcek|
|CELLSNET-46849|Harici veri bağlantılarında sorun|Böcek|
|CELLSNET-46850|Cells.DeleteRange() kullanılırken veri gruplaması korunmadı|Böcek|
|CELLSNET-46855|InsertRows, gruplandırılmış satırları yanlış bir şekilde böler|Böcek|
|CELLSNET-46858|XLSX'ten ODS'ye dönüştürme, ders kitabındaki metin yazı tipini değiştirir|Böcek|
|CELLSNET-46859|Baskı önizleme, XLSX'ten dönüştürülen ODS dosyasındaki metin kutusunu göstermiyor|Böcek|
|CELLSNET-46723|Şifreli ODS dosyası için SheetRender'dan Görüntü alınırken bir istisna atılıyor|İstisna|
|CELLSNET-46842|Sayı> int.MaxValue olan bir Excel'de grafikleri hesaplamak hata veriyor|İstisna|
|CELLSNET-46828|Pivot tabloyla akıllı işaretçi kullanırken ve çalışma kitabını kaydederken "IndexOutOfRangeException"|İstisna|
|CELLSNET-46814|XLSX'i PDF'ye dönüştürürken "Dizin dizinin sınırlarının dışındaydı" istisnası|İstisna|
|CELLSNET-46831|Bir Excel dosyasını PDF'ye dönüştürürken istisna|İstisna|
|CELLSNET-46844|Workbook.CalculateFormula(), NullReferenceException'a neden olur|İstisna|
|CELLSNET-46832|Bir XLSX dosya formatı yüklenirken "Geçersiz MsoLineDashStyle dize değeri" istisnası|İstisna|
### **Herkese Açık API ve Geriye Dönük Uyumsuz Değişiklikler**
Aşağıda, API numaralı telefon numarasına eklenen, yeniden adlandırılan, kaldırılan veya kullanımdan kaldırılan üyeler gibi genele açık olarak yapılan tüm değişikliklerin ve Aspose.Cells for .NET numaralı telefona yapılan geriye dönük uyumlu olmayan değişikliklerin bir listesi bulunmaktadır. Listelenen herhangi bir değişiklikle ilgili endişeleriniz varsa lütfen şu adrese bildirin: Aspose.Cells destek forumu.
#### **SheetPrintingPreview sınıfını ekler**
Çalışma sayfası yazdırma önizlemesi.
#### **WorkbookPrintingPreview sınıfını ekler**
Çalışma kitabı yazdırma önizlemesi.
#### **QueryTable.ExternalConnection özelliğini ekler.**
Sorgu tablosunun bağlantısını alır.
#### **Hyperlink.LinkType özelliğini ve enum TargetModeType özelliğini ekler.**
Köprünün bağlantı türünü temsil eder.
