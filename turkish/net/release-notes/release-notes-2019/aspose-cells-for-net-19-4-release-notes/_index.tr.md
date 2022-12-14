---
title: Aspose.Cells for .NET 19.4 Sürüm Notları
type: docs
weight: 90
url: /tr/net/aspose-cells-for-net-19-4-release-notes/
---
{{% alert color="primary" %}} 

 Bu sayfa için sürüm notları içerir[Aspose.Cells for .NET 19.4](https://www.nuget.org/packages/Aspose.Cells/19.4.0).

{{% /alert %}} 

|**Anahtar**|**Özet**|**Kategori**|
|:- |:- |:- |
|CELLSNET-46619|Markdown formatındaki belgeyi kaydetme desteği|Yeni özellik|
|CELLSNET-46124|WebExtension şekli ekleme desteği|Yeni özellik|
|CELLSNET-46553|JSON dosyalarını içe aktarma desteği|Yeni özellik|
|CELLSNET-46653|WebExtension görev bölmesi ekleme desteği|Yeni özellik|
|CELLSNET-46656|Zincirleme yorumları destekleyin|Yeni özellik|
|CELLSNET-46657|Hücreleri kesme ve yapıştırma desteği|Yeni özellik|
|CELLSNET-46686|Fransızca dili için sayı grubu ayırıcısı olarak beyaz boşluğun (karakter kodu 20) alınmasını destekler|Artırma|
|CELLSNET-46649|Çevrimiçi araç iLovePDF ile karşılaştırıldığında oluşturulan büyük PDF|Artırma|
|CELLSNET-46093|Grafikler, Siyah Beyaz Sayfa Düzenini dikkate almaz|Artırma|
|CELLSNET-46677|Excel'i PDF'ye dışa aktarmak, Arapça metinleri grafiklerde tam olarak göstermiyor|Artırma|
|CELLSNET-46639|ODS dosyası için dikey sayfa sonu desteği.|Artırma|
|CELLSNET-46631|İşleme sırasında OutOfMemoryException istisnası|Verim|
|CELLSNET-46596|Şekillerde eksik etiketler|Böcek|
|CELLSNET-46615|Shape.ToImage(), farklı boyutlardaki görüntüleri dışa aktarır|Böcek|
|CELLSNET-46637|Oluşturulan HTML'deki biçimlendirme hataları|Böcek|
|CELLSNET-46650|PivotTable.ShowValuesRow programlı olarak yanlış olarak ayarlanmadı|Böcek|
|CELLSNET-46652|Pivot tablo dilimleyicileri yüklendikten ve kaydedildikten sonra kaldırılır|Böcek|
|CELLSNET-46678|PivotField.IsRepeatItemLabels, XLSB çıktısında korunmaz|Böcek|
|CELLSNET-46671|Range.CopyData çalışma kitabını bozduktan sonra Range.Copy|Böcek|
|CELLSNET-42423|PDF'ye kaydetme, satır verilerini kırpar|Böcek|
|CELLSNET-45698|Worksheet.AutoFitColumns yöntemi, PDF'ye dönüştürülürken uzun metni keser|Böcek|
|CELLSNET-46661|Excel 365 ile karşılaştırıldığında PDF'de işlenen daha az sayıda sayfa|Böcek|
|CELLSNET-46673|Excel'i PDF'ye dönüştürürken Dosya Boyutu sorunu|Böcek|
|CELLSNET-46632|ChartPoint.Datalabels.ShowValue beklendiği gibi çalışmıyor|Böcek|
|CELLSNET-46655|RefreshChartCache = true ile kaydederken kaybolan Çok Düzeyli Kategori Eksen Etiketleri|Böcek|
|CELLSNET-46665|Yüzey grafiklerinde NSeries.Clear() çağrıldıktan sonra Excel dosyası bozuk|Böcek|
|CELLSNET-46672|Grafiği bir resme aktarırken seri verileri eksik|Böcek|
|CELLSNET-46627|Pivot grafiğin işaretlenmesiyle ilgili bir sorun|Böcek|
|CELLSNET-46640|ODS dosyasını kaydederken satır boşsa Yatay Sayfa Sonu kayboluyor|Böcek|
|CELLSNET-46643|Sütun kopyalanırken adlandırılmış aralıklar kopyalanmıyor|Böcek|
|CELLSNET-46644|HeadingPairs ve TitlesOfParts etiketleri kayboluyor|Böcek|
|CELLSNET-46651|Excel dosyası açılırken ve kaydedilirken bozuk|Böcek|
|CELLSNET-46654|WebExtension ekleme desteği|Böcek|
|CELLSNET-46662|BuiltInDocumentProperties'i alma sorunu|Böcek|
|CELLSNET-46663|XLS'yi PDF'ye dönüştürürken görüntü boyutu değişti|Böcek|
|CELLSNET-46667|Gizli satırlar alınırken PlotVisibleRows = true|Böcek|
|CELLSNET-46668|XLSX, ODS olarak kaydedildiğinde noktalı çizgi düz hale gelir|Böcek|
|CELLSNET-46669|Şekilden görüntüye Excel dosyası PDF'ye dönüştürülürken hata oluştu|İstisna|
|CELLSNET-46645|PivotTable.GetChildrens() çağrılırken özel durum oluştu|İstisna|
|CELLSNET-46675|Bir XLSX dosyasını açarken istisna|İstisna|
|CELLSNET-46646|Grafiği güncelledikten sonra Excel dosyasını açarak ortaya çıkan istisna|İstisna|
|CELLSNET-46660|Style.ForegroundColor özelliği, belirli senaryolar için bir istisna atar|İstisna|
|CELLSNET-46688|Stilleri dinamik olarak uygularken ortaya çıkan istisnalar|İstisna|
### **Herkese Açık API ve Geriye Dönük Uyumsuz Değişiklikler**
Aşağıda, API numaralı telefon numarasına eklenen, yeniden adlandırılan, kaldırılan veya kullanımdan kaldırılan üyeler gibi genele açık olarak yapılan tüm değişikliklerin ve Aspose.Cells for .NET numaralı telefona yapılan geriye dönük uyumlu olmayan değişikliklerin bir listesi bulunmaktadır. Listelenen herhangi bir değişiklikle ilgili endişeleriniz varsa lütfen şu adrese bildirin: Aspose.Cells destek forumu.
#### **Markdown belgesini kaydetmek için API'ler ekler: SaveFormat.Markdown, FileFormatType.Markdown, MarkdownSaveOptions**
Hücre içeriğini işaretleme tablosu olarak kaydetmeyi destekler. Workbook.Save() yöntemiyle, etkin sayfadaki tüm hücre içerikleri, işaretleme belgesinde bir tablo olarak dışa aktarılacaktır.
#### **TxtLoadOptions'ın eski özelliklerini kaldırır**
Lütfen KeepExactFormat yerine LoadStyleStrategy özelliğini kullanın.
#### **Eski sınıf LoadDataOption'ı kaldırır**
Lütfen bunun yerine LoadFilter sınıfını ve LoadOptions.LoadFilter özelliğini kullanın.
#### **LoadOptions'ın eski özelliklerini kaldırır**
LoadOptions.ConvertNumericData: Lütfen bu özelliği, TxtLoadOptions gibi ilgili LoadOptions alt sınıfıyla birlikte kullanın.
LoadOptions.LoadDataOptions: Lütfen özel LoadFilter uygulamasıyla LoadOptions.LoadFilter özelliğini kullanın.
LoadOptions.LoadDataFilterOptions: lütfen bunun yerine LoadOptions.LoadFilter.LoadDataFilterOptions kullanın.
LoadOptions.OnlyLoadDocumentProperties: lütfen LoadOptions.LoadFilter.LoadDataFilterOptions=LoadDataFilterOptions.DocumentProperties'i kullanın.
LoadOptions.LoadDataAndFormatting/LoadDataOnly: lütfen LoadOptions.LoadFilter.LoadDataFilterOptions=LoadDataFilterOptions.CellData'yı kullanın | LoadDataFilterOptions.DefinedNames.
#### **PdfSaveOptions.ExportDocumentStructure özelliğini ekler**
Belge yapısının dışa aktarılıp aktarılmayacağını belirleyen bir değer alır veya ayarlar.
#### **Aspose.Cells.WebExtensions ad alanının sınıflarını ekler**
WebExtensions ve WebExtensionTasks'ı temsil eder.
#### **WorksheetCollection.WebExtensions ve WorksheetCollection.WebExtensionTaskPanes özelliklerini ekler.**
Tüm WebExtensions ve WebExtensionTasks'ı temsil eder.
#### **WebExtensionShape sınıfını ekler.**
WebExtension şeklini temsil eder.
#### **Cells.InsertCutCells() yöntemini ekler.**
Kesilmiş hücreleri ekler.
#### **Cells.SetViewColumnWidthPixel yöntemini ekler.**
Sütunun görünüm genişliğini ayarlar.
#### **ThreadedCommentCollection ve ThreadedComment sınıflarını ekler.**
Zincirleme açıklamayı temsil eder.
#### **WorksheetCollection.ThreadedCommentAuthors özelliğini ekler.**
Zincirleme yorumların yazarlarını alır ve ayarlar.
#### **Comment.ThreadedComments özelliğini ekler.**
Yorumdaki zincirleme açıklamaları temsil eder.
#### **CommentCollection.AddThreadedComment() ve CommentCollection.GetThreadedComments() yöntemlerini ekleyin.**
Zincirleme yorumları ekler ve alır.
#### **Chart.SubTitle özelliğini ekleyin.**
Grafiğin alt başlığını alır. Yalnızca ODS biçimli dosya için.
