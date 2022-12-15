---
title: Çalışma Kitabını Farklı Biçimlere Dönüştürme
type: docs
weight: 20
url: /tr/java/converting-workbook-to-different-formats/
---
{{% alert color="primary" %}}

Aspose.Cells, birçok biçim arasında dönüştürmeyi destekler. Teknik olarak dönüştürme, bir çalışma kitabını bir dosya biçiminde yüklemek ve onu başka bir dosya biçiminde kaydetmek anlamına gelir.

{{% /alert %}}

## **Excel'i XPS'ye Dönüştürme**

XPS belge formatı, bir belgenin düzenini ve her sayfanın görsel görünümünü tanımlayan yapılandırılmış XML işaretlemesinin yanı sıra belgeleri dağıtmak, arşivlemek, işlemek, işlemek ve yazdırmak için işleme kurallarından oluşur.

XPS için biçimlendirme dili, XAML'nin, Windows Presentation Foundation (WPF) ilkel öğelerini işaretlemek için XAML kullanarak belgelerdeki vektör grafik öğelerini birleştirmesine izin veren bir alt kümesidir. Kullanılan öğeler, yollar ve diğer geometrik ilkel öğeler açısından açıklanmıştır.

Bir XPS dosyası aslında, belgeyi oluşturan dosyaları içeren Açık Paketleme Kurallarını kullanan Unicoded ZIP arşividir. Bunlar, her sayfa için bir XML biçimlendirme dosyası, metin, gömülü yazı tipleri, raster görüntüler, 2B vektör grafikleri ve ayrıca dijital haklar yönetimi bilgilerini içerir. Bir XPS dosyasının içeriği, dosyayı ZIP dosyalarını destekleyen bir uygulamada açarak incelenebilir.

Aspose.Cells 6.0.0, Microsoft Excel tp XPS dönüştürmesi desteklenmektedir.

### **Tek Çalışma Sayfasını XPS'ye Dönüştürme**

Aşağıdaki örnek, bir Excel dosyasındaki tek bir çalışma sayfasının XPS'ye nasıl dönüştürüleceğini gösterir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-ConvertingsingleWorksheetToXPS-ConvertingsingleWorksheetToXPS.java" >}}

### **Tüm Çalışma Kitabını XPS'e Aktar**

Aşağıdaki örnek, tüm çalışma kitabının XPS biçimine nasıl dönüştürüleceğini gösterir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-ExportWholeWorkbookToXPS-ExportWholeWorkbookToXPS.java" >}}

### **Hızlı Excel'den XPS'ye Dönüştürme**

Aşağıdaki örnek, Excel dosyasını doğrudan XPS biçimine dönüştürmenin basit bir yolunu gösterir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-QuickExcelToXPSConversion-QuickExcelToXPSConversion.java" >}}

## **Excel'i MHTML Dosyalarına Dönüştürme**

[MHTML](https://en.wikipedia.org/wiki/MHTML) normal HTML'yi harici kaynaklarla birleştirir; yani, genellikle benzer resimler, animasyonlar, ses vb. ile tek bir dosyada bağlantılı içerik. .mht dosya uzantılı e-postalar için kullanılırlar.

{{% alert color="primary" %}}

Aspose.Cells, MHTML dosyalarını okumayı ve yazmayı destekler.

{{% /alert %}}

Bir elektronik tabloyu MHTML'ye dönüştürmek, aşağıda gösterildiği gibi hızlı bir işlemdir.

Aşağıdaki kod örneği, bir çalışma kitabının MHTML dosyası olarak nasıl kaydedileceğini gösterir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-ConvertingToMHTMLFiles-ConvertingToMHTMLFiles.java" >}}

## **Excel Dosyalarını HTML'ye Dönüştürme**

 Aspose.Cells API'leri, elektronik tabloların HTML biçiminde dışa aktarılması için destek sağlar. Aspose.Cells bu amaçla**[HtmlSaveOptions](https://reference.aspose.com/cells/java/com.aspose.cells/HtmlSaveOptions)**geliştiricilerin çıktı HTML'sinin çeşitli yönlerini kontrol etmesine izin veren sınıf.

Aşağıdaki kod, nasıl kullanılacağını gösterir**[HtmlSaveOptions](https://reference.aspose.com/cells/java/com.aspose.cells/HtmlSaveOptions)**ek parametreler belirtmeden Microsoft Excel dosyalarını HTML biçimine dışa aktarmak için sınıf.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-ConvertingToHTMLFiles-ConvertingToHTMLFiles.java" >}}

{{% alert color="primary" %}}

 Geçerek aynı sonuçları elde edebilirsiniz.**[SaveFormat.HTML](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#HTML)** için**[Workbook.save](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions))** yöntem.

{{% /alert %}}

### **HTML için Görüntü Tercihlerini Ayarlama**

 8.0.2'den başlayarak, Aspose.Cells ortaya çıktı**[ImageOptions](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ImageOptions)**için**[HtmlSaveOptions](https://reference.aspose.com/cells/java/com.aspose.cells/HtmlSaveOptions)**geliştiricilerin elektronik tabloları HTML biçiminde kaydederken görüntü tercihlerini belirtmelerine olanak tanıyan sınıf.

Uygulanabilecek görüntü ayarları şunlardır:

- **[ImageType](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#ImageType)**: Görüntü türünü alır veya ayarlar. Grafikler de dahil olmak üzere tüm şekillerin çıktı HTML'sinde görüntü olarak oluşturulduğunu lütfen unutmayın.
- **[Kalite](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#Quality)**: ImageFormat Jpeg olarak belirtildiğinde, görüntülerin kalitesini 0 ile 100 arasında alır veya ayarlar.
- **[Dikey Çözünürlük](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#VerticalResolution)**: Görüntünün dikey çözünürlüğünü inç başına nokta cinsinden alır veya ayarlar.
- **[Yatay Çözünürlük](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#HorizontalResolution)**: Görüntünün yatay çözünürlüğünü inç başına nokta cinsinden alır veya ayarlar.
- **[TiffCompression](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#TiffCompression)**: ImageFormat Tiff olarak belirtildiğinde görüntülerin sıkıştırma türünü alır veya ayarlar.
- **[Şeffaf](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#Transparent)**ImageFormat Png olarak belirtildiğinde görüntünün arka planının saydam olup olmayacağını belirtir.

 Aşağıdaki kod nasıl kullanılacağını gösterir**[HtmlSaveOptions.ImageOptions](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ImageOptions)** farklı tercihler belirlemek için.

|**Dışa aktarmadan önce e-tablo görünümü**|**Dışa aktarmadan sonra HTML görünümü**|
|:- |:- |
|![Dışa aktarmadan önce e-tablo görünümü](converting-workbook-to-different-formats_1.png)|![Dışa aktarmadan sonra HTML görünümü](converting-workbook-to-different-formats_2.png)|

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SettingImagePrefrencesforHTML-SettingImagePrefrencesforHTML.java" >}}

## **Excel'i PDF Dosyalarına Dönüştürme**

PDF belgeleri, kuruluşlar, devlet sektörleri ve bireyler arasında belge alışverişinde standart bir format olarak yaygın şekilde kullanılmaktadır. Yazılım geliştiricilerinden genellikle Microsoft Excel dosyalarını kolayca PDF belgelerine dönüştürmenin bir yolunu bulmaları istenir. Aspose.Cells bu özellikleri destekler. Bu makale nasıl olduğunu gösterir.

### **Excel'i PDF'ye Dönüştürme**

 Microsoft Excel'den PDF'e dönüştürme, Aspose.Cells for Java 2.3.0 ile tanıtıldı. Bu sürümden, Aspose.Cells şunları yapabilir:[elektronik tabloları doğrudan PDF'ye dönüştürün](#direct-conversion) (içermek[PDF/A](#saving-excel-spreadsheets-to-pdfa-complied-files)), başka bir ürün olmadan. Aspose.Cells'in eski sürümlerine sahip elektronik tabloları dönüştürmek için,[dönüştürme için Aspose.PDF'i kullanın](#conversion-with-asposepdf-asposecells-prior-to-230).

 Aspose.Cell, elektronik tabloları yüksek derecede doğruluk ve aslına uygun olarak PDF'ye dönüştürür. Ancak, birkaç tane var[sınırlamalar](/cells/tr/java/converting-workbook-to-different-formats/#conversion-attributes), bu makalenin sonunda listelenmiştir.

{{% alert color="primary" %}}

 Aspose.Cells for Java, API ve Sürüm Numarası ile ilgili bilgileri doğrudan çıktı belgelerine yazar. Örneğin, Belgeyi PDF'ye dönüştürürken, Aspose.Cells for Java doldurulur**Başvuru** 'Aspose.Cells' değerine sahip alan ve**PDF Yapımcısı** değeri olan alan, örneğin 'Aspose.Cells for Java v17.9'.

Lütfen Aspose.Cells for Java'e bu bilgileri çıktı Belgelerinden değiştirme veya kaldırma talimatı veremeyeceğinizi unutmayın.

{{% /alert %}}

#### **Doğrudan Dönüşüm**

kullanarak bir Excel dosyasını doğrudan PDF'e kaydedin.**[Workbook.save](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions))** yöntemi sağlamak ve**[SaveFormat.PDF](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#PDF)**arayüz üyesi Bunun gibi doğrudan dönüştürme, en verimli dönüştürme yöntemidir. Verileri veya biçimlendirmeyi kaybetmez, ancak çıktı PDF'sinin giriş Excel dosyası gibi görünmesini sağlar.

 PDF'ye kaydederken güvenlik seçeneklerini belirtmek için şunu kullanın:**[PdfSaveOptions](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveOptions)**.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-Excel2PDFConversion-Excel2PDFConversion.java" >}}

#### **Gelişmiş Dönüşüm**

kullanmayı da tercih edebilirsiniz.**[PdfSaveOptions](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveOptions)** dönüşüm için farklı öznitelikler ayarlamak için sınıf. Farklı özelliklerin ayarlanması**[PdfSaveOptions](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveOptions)**class size elde edilen PDF dosyası için Yazdırma, Yazı Tipi, Güvenlik ve Sıkıştırma ayarları üzerinde kontrol sağlayacaktır. En dikkate değer özellik,**[Uygunluk](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#Compliance)**Excel dosyalarını PDF/A uyumlu PDF dosyalarına kaydetmenizi sağlar.

##### **Excel Elektronik Tablolarını PDF/A Uyumlu Dosyalara Kaydetme**

Aşağıda sağlanan kod parçacığı,**[PdfSaveOptions](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveOptions)** Excel dosyalarını PDF/A uyumlu PDF biçiminde kaydetmek için sınıf.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-AdvancedConversiontoPdf-AdvancedConversiontoPdf.java" >}}

#### **Aspose.Pdf ile dönüştürme: Aspose.Cells 2.3.0 öncesi**

 2.3.0 sürümünden önceki Aspose.Cells sürümleri için aşağıdaki gibi bir bileşen kullanmanız gerekir[Aspose.PDF for Java](/pdf/java/) elektronik tabloları PDF dosyalarına dönüştürmek için. Aspose.Cells ve Aspose.PDF, bir elektronik tabloyu bir ara adım aracılığıyla PDF'ye dönüştürmek için birlikte çalışır.

Aspose.Cells ve Aspose.PDF ile elektronik tabloları PDF'ye dönüştürmek için:

1.  nesnesinin örneğini oluşturun**[Çalışma Kitabı](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)**boş kurucusunu çağırarak sınıf.
1. Aspose.Cells API'i kullanarak elektronik tablo üzerinde istediğiniz işi yapın.
1. Ara**[Workbook.save](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions))**elektronik tabloyu kaydetme yöntemi:
1. Dosya biçimini XML olarak ayarlayın.
 1. FileFormatType arabiriminden Aspose_Pdf'yi (önceden tanımlanmış bir değer) seçin. Bu, kaydetme yöntemini, Aspose.PDF for Java'in bir PDF belgesi oluşturabilmesi için Aspose.PDF Şeması ile uyumlu XML biçiminde bir elektronik tablo oluşturmaya yönlendirir.
1. XML dosyası oluşturulduğunda, aspose.pdf paketinde Pdf sınıfından bir nesne oluşturun.
1. Pdf sınıfının bindXML yöntemini çağırın ve çıktı XML dosyasının adını iletin.
1. PDF belgesini oluşturmak için Pdf sınıfının kaydetme yöntemini çağırın.

Yukarıdaki adımlar aşağıda bir örnekte uygulanmıştır.

{{% alert color="primary" %}}

 E-tablonuz formüller içeriyorsa, aramak en iyisidir**[Workbook.calculateFormula](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula())** yöntemi, elektronik tabloyu PDF biçimine dönüştürmeden hemen önce. Bunu yapmak, formüle bağlı değerlerin yeniden hesaplanmasını ve doğru değerlerin PDF'de oluşturulmasını sağlar.

{{% /alert %}}

#### **Dönüşüm Nitelikleri**

Her sürümde Aspose.Cells'in dönüşümünü ve diğer özelliklerini iyileştirmek için çok çalışıyoruz. Excel'den PDF'e dönüştürmenin birkaç sınırlaması vardır. Elektronik tabloda belirtilen bazı biçim ayarları kaybolabilir ve tüm çizim nesneleri desteklenmez.

Aşağıdaki tablo, Aspose.Cells kullanılarak PDF'ye dışa aktarılırken tamamen veya kısmen desteklenen tüm özellikleri listeler. Bu tablo nihai değildir ve tüm elektronik tablo niteliklerini kapsamaz. Ayrıca, dönüştürme için desteklenmeyen veya kısmen desteklenen özellikleri de tanımlayabilir.

{{% alert color="primary" %}}

|**Belge Öğesi**|**Bağlanmak**|**ağ destekli**|**notlar**|
|:- |:- |:- |:- |
|Hizalama||Evet||
|Döndürme||Kısmen|Yalnızca 90 ve -90'ı destekler.|
|Arka plan ayarları||Evet||
|Sınır|Renk|Evet||
|Sınır|Çizgi stili|Evet||
|Sınır|Hat genişliği|Evet||
|Cell veri||Evet||
|Yorumlar||Numara||
|Koşullu biçimlendirme||Evet||
|Döküman özellikleri||Evet||
|Çizim Nesneleri||Evet||
|Yazı tipi|Boyut|Evet||
|Yazı tipi|Renk|Evet||
|Yazı tipi|stil|Evet||
|Yazı tipi|Altını çizmek|Evet||
|Yazı tipi|Etkileri|Kısmen|Yalnızca üstü çizili efekti desteklenir|
|Görüntüler||Evet||
|köprü||Evet||
|Grafikler||Evet||
|Birleştirilmiş Cells||Evet||
|Sayfa sonu||Evet||
|Sayfa ayarı|Üstbilgi Altbilgi|Evet||
|Sayfa ayarı|kenar boşlukları|Evet||
|Sayfa ayarı|Sayfa yönlendirmesi|Evet||
|Sayfa ayarı|Sayfa boyutu|Evet||
|Sayfa ayarı|Alanı yazdır|Evet||
|Sayfa ayarı|Başlıkları Yazdır|Evet||
|Sayfa ayarı|ölçekleme|Evet||
|Satır Yüksekliği/Sütun Genişliği||Evet||
{{% /alert %}}
