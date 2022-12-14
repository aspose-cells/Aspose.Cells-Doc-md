---
title: Java 18.12 Sürüm Notları aracılığıyla Android için Aspose.Cells
type: docs
weight: 10
url: /tr/java/aspose-cells-for-android-via-java-18-12-release-notes/
---
{{% alert color="primary" %}}

Bu sayfa, Java 18.12 aracılığıyla Android için Aspose.Cells için sürüm notları içerir.

{{% /alert %}}

|**Anahtar**|**Özet**|**Kategori**|
|:- |:- |:- |
|CELLSJAVA-42745|Bağlantı noktalarını almak için döndürülen değeri değiştirin|Yeni özellik|
|CELLSJAVA-42662|Aralığı HTML olarak dışa aktarma yeteneği sağlayın|Yeni özellik|
|CELLSJAVA-42746|XLSX, HTML'ye dönüştürüldüğünde veri çubukları eksik|Yeni özellik|
|CELLSJAVA-42747|Değer, XLSX HTML'ye dönüştürüldüğünde hala mevcuttur|Yeni özellik|
|CELLSJAVA-42634|Sol sağ şerit şeklini resme dönüştürün|Artırma|
|CELLSJAVA-42713|Aspose.Cells for Java JavaDocs - eksik paket listesi dosyası|Artırma|
|CELLSJAVA-42528|Yazı tipi geçerli bir HTML5 değil ve kendi kendine kapanan etiket ve web tarayıcıları içeriğini yanlış tanıtıyor|Artırma|
|CELLSJAVA-42738|Doğrulama değerlerinin yanlış sayısı XLSX'ten okunuyor|Artırma|
|CELLSJAVA-42734|Ardışık sınırlayıcıları farklı olarak ele alırken sorun|Artırma|
|CELLSJAVA-42731|Japonca yerel ayar için tarih biçimi yanlış|Artırma|
|CELLSJAVA-42748|LightCells API, büyük dosyayı yükleyemiyor|Artırma|
|CELLSJAVA-42728|PDF çıktısına kaydederken bir istisna (StackOverFlow) ortaya çıkıyor|Böcek|
|CELLSJAVA-42729|ROUNDUP() tarafından hesaplanan yanlış değer|Böcek|
|CELLSJAVA-42724|Satır yüksekliklerini düzgün şekilde kopyalamayan PasteType.ALL (Yapıştırma seçenekleri) ile bir aralığı kopyalayın|Böcek|
|CELLSJAVA-42722|Yeni metin ayarlandığında köprü metni biçimlendirmesi kayboluyor|Böcek|
|CELLSJAVA-42688|Geçersiz Rusça tarih biçimi çıktısı|Böcek|
|CELLSJAVA-42721|SheetRender yazı tipleriyle ilgili sorun|Böcek|
|CELLSJAVA-42723|MS Excel dosyasını PDF'ye dönüştürürken "java.lang.OutOfMemoryError: Java yığın alanı" istisnası|Böcek|
|CELLSJAVA-42725|Aspose.Cells aracılığıyla hücre formülü alınırken formülde alıntılar görünüyor|Böcek|
|CELLSJAVA-42720|Koşullu biçimlendirme kullanılırken performans düşüşü|Böcek|
|CELLSJAVA-42737|XLSX->PNG dönüşümünde grafik satırı eksik|Böcek|
|CELLSJAVA-42735|getActualChartSize yöntemiyle ilgili sorun|Böcek|
|CELLSJAVA-40861|Çalışma kitabı kopyalandığında SmartArt kopyalanmıyor|Böcek|
|CELLSJAVA-42727|Excel aralığının HTML çıktısında metin biçimlendirmesi eksik|Böcek|
|CELLSJAVA-42744|XLSX HTML'ye dönüştürüldüğünde Simge Kümeleri yanlış hizalanır|Böcek|
|CELLSJAVA-42772|Adlandırılmış aralık verilerini dışa aktarma, HTML'ye doğru şekilde işlenmedi (Java)|Böcek|
|CELLSJAVA-42753|Adlandırılmış Aralık Sorunu|Böcek|
|CELLSJAVA-42764|Doğrulama, 'getInCellDropDown()' yöntemi için her zaman true değerini döndürür|Böcek|
|CELLSJAVA-42768|Farklı yerel ayarlar (Almanya, Fransa, İtalya ve İspanya) için yanlış kültür özel biçimi döndürülüyor|Böcek|
|CELLSJAVA-42758|Excel'den PDF'e dönüştürme - Gösterge grafiği oluşturma sorunu|Böcek|
|CELLSJAVA-42761|PDF yorumlama, OutOfMemoryError istisnasını atar|Böcek|
|CELLSJAVA-42759|Dosyaları dönüştürürken CellsException|İstisna|
|CELLSJAVA-42755|XLSX dosyalarının örneğini oluştururken "NullPointerException" istisnası|İstisna|
|CELLSJAVA-42762|Dosyaları işlerken NumberFormatException|İstisna|
|CELLSJAVA-42774|CSV yüklerken NullPointerException|İstisna|
|CELLSJAVA-42765|Bir Excel dosyasını PDF dosya biçimine dönüştürürken "com.aspose.cells.CellsException" istisnası|İstisna|
|CELLSJAVA-42754|Bir XLS dosya formatını başlatırken "IllegalStateException: Geçersiz kodlama: null" istisnası|İstisna|

## **Herkese Açık API ve Geriye Dönük Uyumsuz Değişiklikler**

Aşağıda, eklenen, yeniden adlandırılan, kaldırılan veya kullanımdan kaldırılan üyeler gibi genel API'de yapılan tüm değişikliklerin ve Java aracılığıyla Android için Aspose.Cells'de yapılan geriye dönük uyumlu olmayan değişikliklerin bir listesi bulunmaktadır. Listelenen herhangi bir değişiklikle ilgili endişeleriniz varsa, lütfen Aspose.Cells destek forumunda yükseltin.

**HtmlSaveOptions.WidthScalable özelliğini ekler**

Dosyayı HTML'ye dışa aktarırken sütun genişliğini açıklamak için ölçeklenebilir birim kullanılıp kullanılmadığını gösterir. Varsayılan değer yanlıştır.

**WorkbookDesigner.UpdateEmptyStringAsNull özelliğini ekler**

Boş dize değerinin null olarak işlenip işlenmediğini gösterir.

**DocumentProperty.ToDateTime() yönteminin, BuiltInDocumentPropertyCollection.CreatedTime, BuiltInDocumentPropertyCollection.LastPrinted ve BuiltInDocumentPropertyCollection.LastSavedTime özelliklerinin döndürülen değerini günceller**

Yerel saat dilimindeki saati döndürür.

**FormatCondition.Formula1/Formula2 için kullanıcının girişi için daha güçlü kısıtlama gerektirir**

Düz girdi dizisi, bir Ad referansına mı atıfta bulunacağı yoksa yalnızca sabit bir dize değeri mi olduğu belirlenemez. Yani, şimdi formülün '=' işareti ile başlamasını istiyoruz. Düz dize değeri "sss" için lütfen "=\"sss\"" gibi bir biçim kullanın.

**PivotTable.RefreshedByWho özelliğini ekler**

PivotTable'ı en son yenileyen kullanıcının adını alır.

**PivotTable.RefreshDate özelliğini ekler**

PivotTable'ın en son yenilendiği tarihi alır.

**CalculationData.CellRow/CellColumn özelliklerini ekler**

Kullanıcının Cell nesnesini getirmek yerine hücrenin satır ve sütun indekslerini alması için etkili bir yol sağlar.

**CalculationCell sınıfını ekler**

Hesaplanan bir hücreyle ilgili hesaplama verilerini temsil eder.

**AbstractCalculationMonitor.OnCircular(IEnumerator circleCellsData) yöntemini ekler**

Kullanıcının döngüsel referansları toplaması ve işlemesi için yöntem sağlar.

**TxtLoadOptions.TreatConsecutiveDelimitersAsOne özelliğini ekler**

Kullanıcının, CSV dosyasını içe aktarırken ardışık sınırlayıcıların tek olarak alınması gerekip gerekmediğini seçmesine izin verir.

**FormatCondition.SetFormulas(dize formülü1, dize formülü2, bool isR1C1, bool isLocal) yöntemini ekler**

Kullanıcının FormatCondition için formüller ayarlaması için verimli ve uygun bir yol sağlar.

**Validation.GetListValue(int satır, int sütun) yöntemini ekler**

Kullanıcının, belirli bir hücrenin Doğrulanması için listeyi oluşturacak değeri almasına izin verir.

**Eski ValidationCollection.Add(Doğrulama doğrulama) yöntemi**

Bunun yerine ValidationCollection.Add(CellArea) yöntemini kullanın.

**Validation.Copy(Aspose.Cells.Validation,Aspose.Cells.CopyOptions) yöntemini ekler**

Doğrulamayı kopyalar.

**BuiltInDocumentPropertyCollection'ın CreatedUniversalTime,LastPrintedUniversalTime ve LastSavedUniversalTime özelliklerini ekler**

Yerleşik özelliklerle ilgili UTC saatini döndürür.

**OoxmlSaveOptions.UpdateSmartArt özelliğini ekler**

Smart art'ın güncellenip güncellenmediğini gösterir.

**SmartArtShape sınıfını ekler** 

Akıllı sanat şeklini temsil eder.

**HtmlSaveOptions.ExportSingleTab özelliğini ekler**

Dosyada yalnızca bir çalışma sayfası olduğunda tek sekmenin dışa aktarılıp aktarılmadığını gösterir. Varsayılan değer yanlıştır.

**HtmlSaveOptions.ExportPrintAreaOnly özelliğini ekler**

Yalnızca yazdırma alanının html dosyasına aktarılıp aktarılmadığını gösterir. Varsayılan değer yanlıştır.

**Eski Workbook.Initialize() yöntemini siler**

Bunun yerine Çalışma Kitabı yapıcısını kullanın.

**Eski Workbook.Styles özelliğini siler**

StyleCollection.Add() yerine çalışma kitabı stili oluşturmak ve işlemek için Workbook.CreateStyle()'ı kullanın;
StyleCollection yerine adlandırılmış stil almak için Workbook.GetNamedStyle(string) kullanın

**Eski Workbook.CheckWriteProtectedPassword() yöntemini siler**

Bunun yerine WorkbookSettings.WriteProtection.ValidatePassword yöntemini kullanın.

**LoadDataFilterOptions.VBA numaralandırmasını ekler**

Şablon dosyası yüklenirken VBA projelerini yok sayma seçeneği.

**Style.InvariantCustom özelliği ekler**

Sayı biçimi için kültürden bağımsız desen dizesini alır (yerleşik sayı için desen dizesi dahil).

**FindOptions.ValueTypeSensitive özelliği ekler**

Aranan hücre değeri türünün aranan anahtarla aynı olup olmayacağını belirtir.

**Eski FindOptions.SearchNext özelliği**

Bunun yerine FindOptions.SearchBackward özelliğini kullanın, bu yeni özellik için SearchNext'in false değerine karşılık gelen true değeri.

**Eski Cells.FindString, FindStringStartsWith, FindStringEndsWith, FindStringContains ve FindNumber yöntemlerini siler**

Bunun yerine Cells.Find(object,Cell,FindOptions) yöntemini kullanın. FindNumber, FindString yöntemleriyle aynı sonucu elde etmek için lütfen FindOptions.ValueTypeSensitive öğesini doğru olarak ayarlayın.

Eski Cells.Start özelliğini siler

Bunun yerine Cells.FirstCell özelliğini kullanın.

**Eskimiş Cells.End özelliğini siler**

Bunun yerine Cells.LastCell özelliğini kullanın.

**Cells[int] özelliğini siler**

Bunun yerine bu çalışma sayfasındaki tüm hücreleri yinelemek için Cells.GetEnumerator() yöntemini kullanın.

**Eski Shape.Rotation özelliğini siler**

Bunun yerine Shape.RotationAngle özelliğini kullanın.

**Eski Validation.AreaList özelliğini siler**

Bunun yerine Validation.Areas özelliğini kullanın.

**Eski Stil yapıcısını siler**

Bunun yerine CellsFactory.CreateStyle() veya Workbook.CreateStyle() yöntemini kullanın.

**Eski Shape.IsPrinted özelliğini siler**

Bunun yerine Shape.IsPrintable özelliğini kullanın.

**Eskimiş PivotItem.Move(int) yöntemini siler**

Bunun yerine PivotItem.Move(int , bool ) yöntemini kullanın.

**Eski siler Cells.ExportDataTable(int, int, int, int,bool, bool),Cells.ExportDataTable(int, int, int, int,object[]), Cells.ExportDataTable(int, int, int, int,bool) , Cells.ExportDataTable(DataTable, int, int[],int, bool) ve Cells.ExportDataTable(DataTable,int, int, int, bool, bool)yöntemleri**

Bunun yerine ExportDataTable(firstRow,firstColumn, totalRows, totalColumns,ExportTableOptions) yöntemini kullanın.

{{% alert color="primary" %}}

Java üzerinden Android için Aspose.Cells kod tabanı, ilgili .NET ve 07613481 sürüm (ler) koduyla eşleştiğinden, Aspose.Cells for .NET v18.10, for .NET v18.10, 0763101. 12, Aspose.Cells for Java v18.10, Aspose.Cells for Java v18.11 ve Aspose.Cells for Java v18.12 de Java v18.12 aracılığıyla Android için bu Aspose.Cells'e dahildir.

{{% /alert %}}
