---
title: Aspose.Cells for .NET 17.5 Sürüm Notları
type: docs
weight: 80
url: /tr/net/aspose-cells-for-net-17-5-release-notes/
---
{{% alert color="primary" %}} 

 Bu sayfa için sürüm notları içerir[Aspose.Cells for .NET 17.5](https://downloads.aspose.com/cells/net/new-releases/aspose.cells-for-.net-17.5/).

{{% /alert %}} 

|**Anahtar**|**Özet**|**Kategori**|
|:- |:- |:- |
|CELLSNET-41365|PdfSaveOptions'ta PDF/A-1a uyumluluğunu destekleyin|Yeni özellik|
|CELLSNET-45347|Excel dosyasındaki mevcut PrinterSettings'i kaldırın|Yeni özellik|
|CELLSNET-45340|Çalışma sayfası için Özel Sayfa Boyutu seçeneklerini uygulama|Yeni özellik|
|CELLSNET-45327|HTML hücrelerinin verilerini DataTable'a aktarma desteği|Yeni özellik|
|CELLSNET-45316|ASP.NET Oturum durumu modu SQL Server olduğunda GridWeb'in çalışmasını destekleyin|Yeni özellik|
|CELLSNET-45350|Görüntü işleme sırasında OutOfMemory hatası|Verim|
|CELLSNET-45341|Filtrelere sahip XLS'yi SpreadsheetML'ye dönüştürmek çıktı dosyasını bozar|Verim|
|CELLSNET-45217|Excel'i PDF'ye kaydetmek görüntüyü döndürür|Böcek|
|CELLSNET-45306|CSS önekiyle HTML'ye kaydederken yanlış stiller|Böcek|
|CELLSNET-45304|Çıktı HTML'sinde dikey olarak döndürülen metnin metin hizalaması yanlış|Böcek|
|CELLSNET-45299|HTML olarak kaydederken metin hücreye sığmıyor|Böcek|
|CELLSNET-45288|Bir HTML dosyası yüklenirken istisna oluştu|Böcek|
|CELLSNET-45274|Pivot tablo verileri doğru şekilde yenilenmiyor|Böcek|
|CELLSNET-45336|Çalışma kitabı hesaplama yöntemi XIRR formülünü hesaplayamıyor - II|Böcek|
|CELLSNET-45333|Çalışma Kitabı formülü hesaplamasından sonra M114 ve N114 hücresindeki değerler doğru değil|Böcek|
|CELLSNET-45318|Çalışma kitabı hesaplama yöntemi, XIRR formülünü hesaplayamıyor|Böcek|
|CELLSNET-45310|Oturum durumu işlem dışı olduğunda birden çok kullanıcı GridWeb'de sorunla karşı karşıya|Böcek|
|CELLSNET-45324|Bir Excel dosyasını PDF'ye dönüştürürken karakterlerin konumu ortaya hizalı değil|Böcek|
|CELLSNET-45339|ODS'den XML'e dönüştürülen (SpreadsheetML) dosyası MS Excel tarafından açılmıyor|Böcek|
|CELLSNET-45326|Cell.HtmlString, iç içe geçmiş yazı tipi rengini düzgün şekilde vurgulamıyor|Böcek|
|CELLSNET-45325|Yeni satırlar eklendikten sonra veri doğrulamaları garipleşiyor|Böcek|
|CELLSNET-45322|Cells.ImportDataTable yöntemi değişti|Böcek|
|CELLSNET-45314|CopyOptions.ExtendToAdjacentRange özelliği çalışmıyor|Böcek|
|CELLSNET-45312|Nihai Excel dosyası, orijinal Excel dosyasından farklı|Böcek|
|CELLSNET-45303|XLSX'ten XLS dosya biçimine yeniden kaydedilirken şekiller (dikdörtgenler, çizgiler vb.) artık birleştirilmez.|Böcek|
|CELLSNET-45301|Excel dosyasını açıp kaydetmek hizalamayı yanlış yapıyor|Böcek|
|CELLSNET-45297|XLSM dosyasını daha yeni bir sürümle açıp kaydetmek onu bozuyor|Böcek|
|CELLSNET-45296|Bir çalışma kitabından tüm açıklamaların kaldırılması, Excel'de açıldığında hatalara neden oluyor|Böcek|
|CELLSNET-45308|Pasta grafiğin "Diğer" ifadesini çevir|Böcek|
|CELLSNET-45298|Açıklama girişleri, birleştirilmiş grafikte doğru şekilde gizlenmiyor|Böcek|
|CELLSNET-45313|PivotTable'a hesaplanan alan eklenirken istisna|İstisna|
|CELLSNET-45307|Çalışma Sayfasını Resme dönüştürürken şekil-resim hatası|İstisna|
### **Herkese Açık API ve Geriye Dönük Uyumsuz Değişiklikler**
Aşağıda, API numaralı telefon numarasına eklenen, yeniden adlandırılan, kaldırılan veya kullanımdan kaldırılan üyeler gibi genele açık olarak yapılan tüm değişikliklerin ve Aspose.Cells for .NET numaralı telefona yapılan geriye dönük uyumlu olmayan değişikliklerin bir listesi bulunmaktadır. Listelenen herhangi bir değişiklikle ilgili endişeleriniz varsa lütfen şu adrese bildirin: Aspose.Cells destek forumu.
#### **ExportTableOptions.ExportAsHtmlString özelliğini ekler**
Hücrelerin HTML dize değerini DataTable'a verir.
#### **PageSetup.Copy(PageSetup kaynağı,CopyOptions copyOptions) yöntemini ekler**
Sayfa Yapısı ayarlarını kopyalar.
#### **ImportTableOptions.ShiftFirstRowDown özelliğini ekler**
Tablo eklenirken ilk satırın aşağı kaydırılıp kaydırılmadığını gösterir.
#### **PageSetup.CustomPaperSize() yöntemini ekler**
İnç biriminde özel kağıt boyutunu ayarlar.
#### **PageSetup.PrinterSettings özelliğini ekler**
Varsayılan yazıcının ayarlarını alır ve ayarlar.
#### **Enum PaperSizeType.Custom ekler**
Özel kağıt boyutunu temsil eder.
#### **Enum PdfCompliance.PdfA1a ekler**
PDFA-1a ile uyumlu PDF biçimini temsil eder.


#### **Kullanım Örnekleri**
Lütfen Aspose.Cells Wiki belgelerine eklenen yardım konularının listesini kontrol edin:

- [Excel dosyasını PDFA-1a ile uyumlu PDF formatına dönüştürün](/cells/tr/net/convert-excel-file-to-pdf-format-compatible-with-pdfa-1a/)
- [Sayfa Yapısı Ayarlarını Kaynak Çalışma Sayfasından Hedef Çalışma Sayfasına Kopyalayın](/cells/tr/net/copy-page-setup-settings-from-source-worksheet-into-destination-worksheet/)
- [İşleme için Çalışma Sayfasının Özel Kağıt Boyutunu Uygulayın](/cells/tr/net/implement-custom-paper-size-of-worksheet-for-rendering/)
- [Excel dosyasındaki Çalışma Sayfalarının Mevcut Yazıcı Ayarlarını Kaldır](/cells/tr/net/remove-existing-printersettings-of-worksheets-in-excel-file/)
- [Cells Veri Tablosu Satırlarını eklerken İlk Satırı aşağı kaydır](/cells/tr/net/shift-first-row-down-when-inserting-cells-data-table-rows/)
- [Cells'in HTML Dizesi Değerini DataTable'a Aktarın](/cells/tr/net/export-html-string-value-of-the-cells-to-the-datatable/)
- [ASP.NET Oturum durumu modu SQL Server olduğunda GridWeb'in çalışması](/cells/tr/net/working-of-gridweb-when-asp-net-session-state-mode-is-sql-server/)
- [Farklı GridWeb Modlarını Etkinleştirin](/cells/tr/net/enable-different-gridweb-modes/)


