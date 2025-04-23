---
title: Çalışma Kitabını Farklı Biçimlere Dönüştürme
type: docs
weight: 20
url: /tr/java/converting-workbook-to-different-formats/
---

{{% alert color="primary" %}}

Aspose.Cells, birçok biçim arasında dönüşümü destekler. Teknik olarak, dönüştürme, bir elektronik tabloyu bir dosya biçiminde yüklemek ve başka bir biçimde kaydetmek anlamına gelir.

{{% /alert %}}

## **Excel'i XPS'e Dönüştürme**

XPS belge biçimi, her bir sayfanın düzenini ve görsel görünümünü tanımlayan yapılandırılmış XML işaretleme ve dağıtma, arşivleme, işleme ve belgelerin yazdırılması için görüntüleme kurallarını içerir.

XPS için işaretleme dili, XAML'nin bir alt kümesidir ve bunun sayesinde belgelerde vektör grafik öğeleri kullanmasına izin verir. XAML'i kullanarak Windows Sunum Vakfı (WPF) primitiflerini işaretlemek için kullanılır. Kullanılan öğeler, yollar ve diğer geometrik primitifler açısından tanımlanmıştır.

Bir XPS dosyası aslında, belgeyi oluşturan dosyaları içeren Open Packaging Konvansiyonlarını kullanan Unicoded bir ZIP arşividir. Bunlar, her sayfa için bir XML işaretleme dosyası, metin, gömülü yazı tipleri, radye görüntüler, 2B vektör grafikleri ve dijital hak yönetimi bilgilerini içerir. Bir XPS dosyasının içeriği, ZIP dosyalarını destekleyen bir uygulamada açılarak kolayca incelenebilir.

Aspose.Cells 6.0.0'dan itibaren Microsoft Excel tp XPS dönüştürme desteklenmektedir.

### **Tek bir Çalışma Sayfasını XPS'e Dönüştürme**

Aşağıdaki örnek, bir Excel dosyasındaki tek bir çalışma sayfasını XPS'e dönüştürmenin nasıl yapıldığını göstermektedir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-ConvertingsingleWorksheetToXPS-ConvertingsingleWorksheetToXPS.java" >}}

### **Bütün Çalışma Kitabını XPS'e Dışa Aktarma**

Aşağıdaki örnek, bütün çalışma kitabını XPS formatına nasıl dönüştüreceğinizi göstermektedir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-ExportWholeWorkbookToXPS-ExportWholeWorkbookToXPS.java" >}}

### **Hızlı Excel'den XPS'e Dönüşüm**

Aşağıdaki örnek, Excel dosyasını doğrudan XPS formatına nasıl dönüştüreceğinizi göstermektedir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-QuickExcelToXPSConversion-QuickExcelToXPSConversion.java" >}}

## **Excel'den MHTML Dosyalarına Dönüştürme**

[**MHTML**](https://en.wikipedia.org/wiki/MHTML), genellikle resimler, animasyonlar, sesler vb. gibi içeriğin normal HTML'yi dış kaynaklarla birleştirdiği, yani genellikle bağlantılı olan bir dosyadır. Bunlar .mht dosya uzantısına sahip e-postalar için kullanılır.

{{% alert color="primary" %}}

Aspose.Cells, MHTML dosyalarını okuma ve yazma desteği sağlamaktadır.

{{% /alert %}}

Bir elektronik tabloyu MHTML'e dönüştürmek hızlı bir işlem olup aşağıda gösterilmiştir.

Aşağıdaki kod örneği, bir çalışma kitabını MHTML dosyası olarak kaydetmenin nasıl yapıldığını göstermektedir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-ConvertingToMHTMLFiles-ConvertingToMHTMLFiles.java" >}}

## **Excel Dosyalarını HTML'e Dönüştürme**

Aspose.Cells API'leri, elektronik tabloları HTML formatına dışa aktarma desteği sağlar. Bu amaçla Aspose.Cells, geliştiricilere çıktı HTML'sinin several yönlerini kontrol etmelerine izin veren [**HtmlSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/HtmlSaveOptions) sınıfını kullanır.

Aşağıdaki kod, ek parametre belirtmeden Microsoft Excel dosyalarını HTML formatına dışa aktarmak için [**HtmlSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/HtmlSaveOptions) sınıfını nasıl kullandığını göstermektedir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-ConvertingToHTMLFiles-ConvertingToHTMLFiles.java" >}}

{{% alert color="primary" %}}

Aynı sonuçları elde edebilirsiniz, [**SaveFormat.HTML**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#HTML) ve [**Workbook.save**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save-java.io.OutputStream-com.aspose.cells.SaveOptions-) yöntemine geçirerek.

{{% /alert %}}

### **HTML için Görüntü Tercihlerini Ayarlama**

8.0.2'den itibaren, Aspose.Cells, elektronik tabloları HTML formatına kaydederken görüntü tercihlerini belirlemek için [**HtmlSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/HtmlSaveOptions) sınıfı için [**ImageOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ImageOptions) sunmuştur. 

Uygulanabilecek görüntü ayarları şunlardır:

- [**ImageType**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#ImageType): Görüntü türünü alır veya ayarlar. Lütfen unutmayın, tüm şekiller, grafikler de dahil olmak üzere, çıktı HTML'de resim olarak render olur.
- [**Quality**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#Quality): Jpeg olarak ImageFormat belirtildiğinde, resimlerin kalitesini 0 ila 100 arasında alır veya ayarlar.
- [**VerticalResolution**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#VerticalResolution): Görüntünün inç başına noktada dikey çözünürlüğünü alır veya ayarlar.
- [**HorizontalResolution**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#HorizontalResolution): Görüntünün inç başına noktada yatay çözünürlüğünü alır veya ayarlar.
- [**TiffCompression**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#TiffCompression): ImageFormat olarak Tiff belirtildiğinde, görüntülerin sıkıştırma türünü alır veya ayarlar.
- [**Transparent**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#Transparent): ImageFormat olarak Png belirtildiğinde bir görüntünün arka planının şeffaf olup olmadığını gösterir.

Aşağıdaki kod, farklı tercihleri belirtmek için [**HtmlSaveOptions.ImageOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ImageOptions) kullanımını gösterir.

|**Dışa aktarma öncesi elektronik tablo görünümü**|**Dışa aktarma sonrası HTML görünümü**|
| :- | :- |
|![Dışa aktarma öncesi elektronik tablo görünümü](converting-workbook-to-different-formats_1.png)|![Dışa aktarma sonrası HTML görünümü](converting-workbook-to-different-formats_2.png)|

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SettingImagePrefrencesforHTML-SettingImagePrefrencesforHTML.java" >}}

## **Excel Dosyalarını PDF'ye Dönüştürme**

PDF belgeleri, kuruluşlar, devlet sektörleri ve bireyler arasında belgelerin değiş tokuşunun standart biçimi olarak geniş çapta kullanılmaktadır. Yazılım geliştiricileri genellikle Microsoft Excel dosyalarını PDF belgelerine kolayca dönüştürmek için bir yol bulmaları istenir. Aspose.Cells bu özellikleri destekler. Bu makale, bunun nasıl yapıldığını göstermektedir.

### **Excel'i PDF'ye Dönüştürme**

Microsoft Excel'den PDF dönüşümü Aspose.Cells for Java 2.3.0 ile tanıtıldı. Bu sürümden itibaren Aspose.Cells, başka bir ürün olmadan elektronik tabloları doğrudan PDF'e dönüştürebilir (PDF/A dahil). Daha eski Aspose.Cells sürümleriyle elektronik tabloları dönüştürmek için [Aspose.PDF'yi kullanabilirsiniz](#conversion-with-asposepdf-asposecells-prior-to-230).

Aspose.Cell, elektronik tabloları PDF'ye yüksek bir doğruluk ve sadakat derecesiyle dönüştürür. Bununla birlikte, bu makalenin sonunda listelenen birkaç [kısıtlama](/cells/tr/java/converting-workbook-to-different-formats/#conversion-attributes) vardır.

{{% alert color="primary" %}}

Aspose.Cells for Java, API ve Sürüm Numarası hakkında bilgiyi çıkış belgelerine doğrudan yazar. Örneğin, PDF'ye belgeyi renderlarken, Aspose.Cells for Java **Uygulama** alanını 'Aspose.Cells' değeriyle doldurur ve **PDF Üretici** alanını, örneğin 'Aspose.Cells for Java v17.9' değeriyle doldurur.

Lütfen unutmayın ki Aspose.Cells for Java'ye çıkış Belgerinden bu bilgileri değiştirmesini veya kaldırmasını talimat veremezsiniz.

{{% /alert %}}

#### **Doğrudan Dönüşüm**

Bir Excel dosyasını en verimli dönüşüm yöntemi olarak doğrudan PDF'ye [**Workbook.save**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save-java.io.OutputStream-com.aspose.cells.SaveOptions-) yoluyla kaydedin ve [**SaveFormat.PDF**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#PDF) arayüz üyesini sağlayın. Doğrudan dönüşüm, veri veya biçimlendirmeyi kaybetmez, ancak çıktı PDF'sinin girdi Excel dosyasına benzer bir görünüme sahip olmasını sağlar.

PDF'ye kaydederken güvenlik seçeneklerini belirtmek için [**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveOptions) kullanın.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-Excel2PDFConversion-Excel2PDFConversion.java" >}}

#### **Gelişmiş Dönüşüm**

Dönüşüm için farklı özellikler belirlemek için [**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveOptions) sınıfını kullanmayı tercih edebilirsiniz. [**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveOptions) sınıfının farklı özelliklerini ayarlamak, sonuç PDF dosyası için Baskı, Yazı tipi, Güvenlik ve Sıkıştırma ayarları üzerinde kontrol sağlar. En dikkat çekici özellik Excel dosyalarını PDF/A uyumlu PDF dosyalarına kaydetmenizi sağlayan [**Compliance**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#Compliance) özelliğidir.

##### **Excel Elektronik Tablolarını PDF/A Uyumlu Dosyalara Kaydetme**

Aşağıdaki kod örneği, Excel dosyalarını PDF/A uyumlu PDF formatına kaydetmek için [**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveOptions) sınıfının kullanımını göstermektedir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-AdvancedConversiontoPdf-AdvancedConversiontoPdf.java" >}}

#### **Aspose.Pdf ile Dönüşüm: Aspose.Cells 2.3.0 Öncesi**

2.3.0 sürümünden önceki Aspose.Cells sürümleri için elektronik tabloları PDF dosyalarına dönüştürmek için [Aspose.PDF için Java](/pdf/java/) gibi bir bileşen kullanmanız gerekir. Aspose.Cells ve Aspose.PDF, bir elektronik tabloyu PDF'ye dönüştürmek için ara bir adım üzerinden birlikte çalışır.

Aspose.Cells ve Aspose.PDF ile elektronik tabloları PDF'ye dönüştürmek için:

1. Boş kurucuyu çağırarak [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) sınıfının nesnesini örnekleyin.
1. Aspose.Cells API'sini kullanarak elektronik tabloda istediğiniz çalışmayı yapın.
1. Elektronik tabloyu kaydetmek için [**Workbook.save**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save-java.io.OutputStream-com.aspose.cells.SaveOptions-) yöntemini çağırın:
   1. Dosya biçimini XML olarak ayarlayın.
   1. FileFormatType arayüzünden önceden tanımlanmış bir değer olan Aspose_Pdf'yi seçin. Bu, kaydetme yöntemini Aspose.PDF Şeması ile uyumlu XML formunda bir elektronik tablo üretmeye yönlendirir, böylece Aspose.PDF for Java sonrasında bir PDF belgesi oluşturabilir.
1. XML dosyası oluşturulduğunda, aspose.pdf paketindeki Pdf sınıfının bir örneğini oluşturun.
1. Pdf sınıfının bindXML yöntemini çağırın ve çıkış XML dosyasının adını geçirin.
1. Pdf sınıfının save yöntemini çağırarak PDF belgesi oluşturun.

Yukarıdaki adımlar, aşağıda bir örnekte uygulanmıştır.

{{% alert color="primary" %}}

Elektronik tablonuzda formüller bulunuyorsa, en iyi şekilde [**Workbook.calculateFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula--) yöntemini elektronik tabloyu PDF biçimine dönüştürmeden hemen önce çağırmanız önerilir. Böylece formül bağımlı değerler yeniden hesaplanır ve doğru değerler PDF'de render edilir.

{{% /alert %}}

#### **Dönüşüm Özellikleri**

Her sürümle dönüşüm ve Aspose.Cells'ın diğer yönlerini iyileştirmek için çaba gösteriyoruz. Excel'den PDF'ye dönüşümün bazı kısıtlamaları vardır. Elektronik tabloda belirtilen bazı biçim ayarları kaybolabilir ve tüm çizim nesneleri desteklenmez.

Aşağıdaki tablo, Aspose.Cells kullanılarak PDF'ye dönüşüm yapılırken tamamen veya kısmen desteklenen tüm özellikleri listeler. Bu tablo nihai değildir ve tüm elektronik tablo özelliklerini kapsamaz. Ayrıca, dönüşüm için desteklenmeyen veya kısmen desteklenen özellikleri de belirleyebilir.

{{% alert color="primary" %}}

|**Döküman Elemanı**|**Özellik**|**Desteklenir**|**Notlar**|
| :- | :- | :- | :- |
|Hizalama| |Evet| |
|Döndürme| |Kısmen|Sadece 90 ve -90 desteklenir.|
|Arka plan Ayarları| |Evet| |
|Kenarlık|Renk|Evet| |
|Kenarlık|Çizgi stili|Evet| |
|Kenarlık|Çizgi genişliği|Evet| |
|Hücre Verisi| |Evet| |
|Yorumlar| |Hayır| |
|Koşullu Biçimlendirme| |Evet| |
|Döküman Özellikleri| |Evet| |
|Çizim Nesneleri| |Evet| |
|Yazı Tipi|Boyut|Evet| |
|Yazı Tipi|Rengi|Evet| |
|Yazı Tipi|Stili|Evet| |
|Yazı Tipi|Altı çizili|Evet| |
|Yazı Tipi|Efektleri|Kısmen|Sadece üstü çizili efekti desteklenir|
|Resimler| |Evet| |
|Hyperlink| |Evet| |
|Grafikler| |Evet| |
|Birleştirilmiş Hücreler| |Evet| |
|Sayfa Sonu| |Evet| |
|Sayfa Ayarı|Üstbilgi/Altbilgi|Evet| |
|Sayfa Ayarı|Kenar Boşlukları|Evet| |
|Sayfa Ayarı|Sayfa Yönü|Evet| |
|Sayfa Ayarı|Sayfa Boyutu|Evet| |
|Sayfa Ayarı|Yazdırma Alanı|Evet| |
|Sayfa Ayarı|Yazdırma Başlıkları|Evet| |
|Sayfa Ayarı|Ölçekleme|Evet| |
|Satır Yüksekliği/Sütun Genişliği| |Evet| |
{{% /alert %}}
{{< app/cells/assistant language="java" >}}
