---
title: Aspose.Cells for .NET 9.0.0 Sürüm Notları
type: docs
weight: 40
url: /tr/net/aspose-cells-for-net-9-0-0-release-notes/
---
### **1) Aspose.Cells**

|**Anahtar** |**Özet** |**Kategori** |
|:- |:- |:- |
|CELLSNET-40617 | ActiveX ComboBox denetiminden/denetimine değer okuma/yazma| Yeni özellik|
|CELLSNET-41264 | Aspose.Cells.GridDesktop'u WPF uygulamasında kullanma| Yeni özellik|
|CELLSNET-44681 | Komut dosyası etiketi CDATA kullandığında HTML içe aktarma başarısız oluyor| Artırma|
|CELLSNET-44693 | HTML'yi XLSX'e dönüştürürken içerikler eksik| Böcek|
|CELLSNET-44650 | HTML'den arka plan veya ön plan renkleri dönüştürülemiyor| Böcek|
|CELLSNET-44645 | Çıktı dosyasında PivotTable'ın herhangi bir değerine çift tıklandığında hata mesajı gösteriliyor| Böcek|
|CELLSNET-44644 | Ortaya çıkan dosya, XLS dosyasını açıp kaydettiğinizde bozulur| Böcek|
|CELLSNET-44622 | Nihai XLSX dosyası, giriş XLSX'inde ve ara HTML'de mevcutken altyazı stillerinden yoksundur.| Böcek|
|CELLSNET-44581 | Elektronik Tablodan HTML'ye dönüştürmeyle ilgili sorun: BODY ve HTML etiketleri arasındaki STYLE etiketi| Böcek|
|CELLSNET-44718 |ICustomFunction, [@columnName] ile çalışmıyor| Böcek|
|CELLSNET-44705 | Formülleri hesaplarken yanlış TOPLAM görüntüleniyor| Böcek|
|CELLSNET-44692 |API, MS Excel'e kıyasla formül değerini yanlış hesaplıyor| Böcek|
|CELLSNET-44688 | Hücre değerinin yanlış hesaplanması| Böcek|
|CELLSNET-44684 | Formülleri hesaplarken hücreden yanlış değer| Böcek|
|CELLSNET-44716 | PDF sonucu, başlık satırlarını yazdırmak için Excel ile eşleşmiyor| Böcek|
|CELLSNET-44713 | Veriler, PDF'nin dönüştürme sonucunda gizlidir| Böcek|
|CELLSNET-44675 | Bir çalışma sayfası için görüntü dosyası oluşturma işlemi başarısız oluyor| Böcek|
|CELLSNET-44717 | Elektronik tablodan XPS'ye: İşlem hiçbir zaman tamamlanmaz ve çok fazla bellek alır| Böcek|
|CELLSNET-44678 | Elektronik tabloyu PDF/resme dönüştürürken mini grafikler doğru oluşturulmuyor| Böcek|
|CELLSNET-44654 | Chart.Calculate() yöntemi grafik görüntüsünü bozar| Böcek|
|CELLSNET-44714 | Bellek akışına (SpreadsheetML) kaydediliyor, işlem askıda kalıyor ve çok zaman alıyor| Böcek|
|CELLSNET-44711 | Aspose.Cells tarafından gizlenen satırın gösterilmesi, Microsoft Excel'de düzgün çalışmıyor| Böcek|
|CELLSNET-44709 | Resmi kaldırıp yeniden taktıktan sonra resim formülü gitti| Böcek|
|CELLSNET-44708 |Sunum slaydının XLS'ye yeniden gömülmesi, çift tıklandığında sunum görünümüyle sonuçlanır| Böcek|
|CELLSNET-44696 | Ok başlı çizgi, XLSX ve PDF formatlarında tam olarak oluşturulmaz| Böcek|
|CELLSNET-44689 | Kaynak XLS dosyası açılıp yeniden kaydedildiğinde yazıcı ayarları değiştirilir| Böcek|
|CELLSNET-44683 |"customSheetView" xml içindeki "pane" xml, tasarımcı elektronik tablosundan çoğaltılmıyor| Böcek|
|CELLSNET-44660 | Bir XLS dosyasını yükleyip kaydettikten sonra grafiğin Y ve X Ekseni kalınlaşır| Böcek|
|CELLSNET-44658 | XLS dosyası yüklenip kaydedildikten sonra grafiğin dikey eksen etiketlerinin metin boyutu değişiyor| Böcek|
|CELLSNET-44691 | Kaynak HTML'de display:none nedeniyle Workbook ctor'da NullReferenceException| İstisna|
|CELLSNET-44685 | Workbook.CalculateFormula() yöntemi, kaynak Excel dosyasında istisna oluşturuyor| İstisna|
|CELLSNET-44712 | İstisna: "Tanımlanan adın geçersiz metni." Excel dosyasını açarken| İstisna|
### **2) Aspose.Cells Izgara Süit**

|**Anahtar** |**Özet** |**Kategori** |
|:- |:- |:- |
|CELLSNET-44667 | Cell koşullu biçimlendirme nedeniyle gölgeleme, GridWeb arayüzünde görüntülenmiyor| Böcek|
### **Herkese Açık API ve Geriye Dönük Uyumsuz Değişiklikler**
Aşağıda, API numaralı telefon numarasına eklenen, yeniden adlandırılan, kaldırılan veya kullanımdan kaldırılan üyeler gibi genele açık olarak yapılan tüm değişikliklerin ve Aspose.Cells for .NET numaralı telefona yapılan geriye dönük uyumlu olmayan değişikliklerin bir listesi bulunmaktadır. Listelenen herhangi bir değişiklikle ilgili endişeleriniz varsa lütfen şu adrese bildirin: Aspose.Cells destek forumu.
#### **Shape.TextOptions özelliğini ekler**
Şeklin metin seçeneklerini temsil eder.
#### **Eski Worksheet.SetBackground yöntemi**
Lütfen bunun yerine Worksheet.BackgroundImage özelliğini kullanın.
#### **Eskimiş LineShape.BeginArrowheadStyle ve ArcShape.BeginArrowheadStyle**
Lütfen bunun yerine Shape.Line.BeginArrowheadStyle özelliğini kullanın.
#### **Eski LineShape.BeginArrowheadWidth ve ArcShape.BeginArrowheadWidth**
Lütfen bunun yerine Shape.Line.BeginArrowheadWidth özelliğini kullanın.
#### **Eski LineShape.BeginArrowheadLength ve ArcShape.BeginArrowheadLength**
Lütfen bunun yerine Shape.Line.BeginArrowheadLength özelliğini kullanın.
#### **Eski LineShape.EndArrowheadStyle ve ArcShape.EndArrowheadStyle**
Lütfen bunun yerine Shape.Line.EndArrowheadStyle özelliğini kullanın.
#### **Eskimiş LineShape.EndArrowheadWidth ve ArcShape.EndArrowheadWidth**
Lütfen bunun yerine Shape.Line.EndArrowheadWidth özelliğini kullanın.
#### **Eski LineShape.EndArrowheadLength ve ArcShape.EndArrowheadLength**
Lütfen bunun yerine Shape.Line.EndArrowheadLength özelliğini kullanın.
#### **Eski Worksheet.CopyConditionalFormatting() yöntemini siler**
#### **Eski Workbook.CheckWriteProtectedPassword() yöntemini siler**
Lütfen bunun yerine WorkbookSettings.WriteProtection.ValidatePassword yöntemini kullanın.
#### **Workbook.RemoveDigitalSign'ı Workbook.RemoveDigitalSignature yöntemi olarak yeniden adlandırır**
Workbook.RemoveDigitalSign yöntemi, Workbook.RemoveDigitalSignature olarak yeniden adlandırıldı.
#### **ChartSplitType.Auto özelliğini ekler**
Veri noktalarının bu grafik türü için varsayılan mekanizma kullanılarak bölüneceğini temsil eder.
#### **ChartPoint.IsInSecondaryPlot özelliği ekler**
Bir değer alır veya ayarlar, bu veri noktalarının bir pasta pastasında veya pasta çubuğu grafiğinde ikinci pastada mı yoksa çubukta mı olduğunu gösterir.
#### **OleObject.ClassIdentifier özelliğini ekler**
Katıştırılmış nesnenin sınıf tanımlayıcısını alır veya ayarlar.
#### **LoadOptions.CultureInfo özelliğini ekler**
Dosyanın yüklendiği andaki sistem kültürü bilgisini alır veya ayarlar.
