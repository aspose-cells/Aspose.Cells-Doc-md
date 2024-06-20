---
title: Sayfa Ayarı Özellikleri
type: docs
weight: 40
url: /tr/java/page-setup-features/
---

Bazen, baskıyı kontrol etmek için çalışma sayfaları için sayfa düzeni ayarlarını yapılandırmak gereklidir. Bu sayfa düzeni ayarları çeşitli seçenekler sunar.

**Sayfa Seçenekleri** 

![todo:image_alt_text](page-setup-features_1.png)

Aspose.Cells, sayfa ayarları seçeneklerini tamamen destekler. Bu makale, Aspose.Cells ile sayfa seçeneklerinin nasıl ayarlanacağını açıklar.

## **Sayfa Seçeneklerini Ayarlama**

Aspose.Cells, bir Microsoft Excel dosyasını temsil eden [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) sınıfını sağlar. Workbook sınıfı, Excel dosyasındaki her çalışma sayfasına erişime izin veren bir Worksheets koleksiyonunu içerir. Bir çalışma sayfası, [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) sınıfı tarafından temsil edilir.

Worksheet sınıfı, sayfa düzeni seçeneklerini ayarlamak için kullanılan PageSetup özelliğini sağlar. Aslında, PageSetup özelliği, yazdırılan bir çalışma sayfası için sayfa düzeni seçeneklerini ayarlamayı mümkün kılan PageSetup sınıfının bir nesnesidir. PageSetup sınıfı, sayfa ayarlama seçeneklerini ayarlamak için kullanılan çeşitli özellikleri sağlar. Bu özelliklerden bazıları aşağıda tartışılmıştır.

### **Sayfa Yönlendirmesi**

Sayfa yönlendirmesi, [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) sınıfının [**setOrientation(PageOrientationType)**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#Orientation) yöntemi kullanılarak portre veya manzara olarak ayarlanabilir. [**setOrientation(PageOrientationType)**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#Orientation) yöntemi, [**PageOrientationType**](https://reference.aspose.com/cells/java/com.aspose.cells/PageOrientationType) numaralandırmasını parametre olarak alır. [**PageOrientationType**](https://reference.aspose.com/cells/java/com.aspose.cells/PageOrientationType) numaralandırmasının üyeleri aşağıda listelenmiştir.

|**Sayfa Yönlendirme Türleri**|**Açıklama**|
| :- | :- |
|[**MANZARA**](https://reference.aspose.com/cells/java/com.aspose.cells/pageorientationtype#LANDSCAPE)|Manzara yönlendirmesi|
|[**PORTRE**](https://reference.aspose.com/cells/java/com.aspose.cells/pageorientationtype#PORTRAIT)|Portre yönlendirmesi|

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-PageOrientation-PageOrientation.java" >}}

### **Ölçekleme Faktörü**

Bir çalışma sayfasının boyutunu küçültebilir veya büyültebilirsiniz. Bunun için [**setZoom**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#Zoom) sınıfının [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) yöntemini kullanarak ölçek faktörünü ayarlamak mümkündür.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ScalingFactor-ScalingFactor.java" >}}

### **FitToPages Seçenekleri**

Çalışma sayfasının içeriğini belirli sayıda sayfaya sığdırmak için [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) sınıfının [**setFitToPagesTall**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#FitToPagesTall) ve [**setFitToPagesWide**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#FitToPagesWide) yöntemlerini kullanın. Bu yöntemler aynı zamanda çalışma sayfalarını ölçeklendirmek için de kullanılır.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-FitToPagesOptions-FitToPagesOptions.java" >}}

### **Kağıt Boyutu**

Çalışma sayfalarının basılacağı kağıt boyutunu, [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) sınıfının [**PaperSize**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PaperSize) özelliğini kullanarak ayarlayın. PaperSize özelliği, aşağıda listelenen [**PaperSizeType**](https://reference.aspose.com/cells/java/com.aspose.cells/PaperSizeType) numaralandırmasındaki önceden tanımlanmış değerlerden birini kabul eder.

|**Kağıt Boyutu Türleri**|**Açıklama**|
| :- | :- |
|Paper10x14|10 in. x 14 in.|
|Paper11x17|11 in. x 17 in.|
|PaperA3|A3 (297 mm x 420 mm)|
|PaperA4|A4 (210 mm x 297 mm)|
|PaperA4Small|A4 Small (210 mm x 297 mm)|
|PaperA5|A5 (148 mm x 210 mm)|
|PaperB3|B3 (13.9 x 19.7 inches)|
|PaperB4|B4 (250 mm x 354 mm)|
|PaperB5|B5 (182 mm x 257 mm)|
|PaperBusinessCard|Business Card (90 mm x 55 mm)|
|PaperCSheet|C size sheet|
|PaperDSheet|D size sheet|
|PaperEnvelope10|Envelope #10 (4-1/8 in. x 9-1/2 in.)|
|PaperEnvelope11|Envelope #11 (4-1/2 in. x 10-3/8 in.)|
|PaperEnvelope12|Envelope #12 (4-1/2 in. x 11 in.)|
|PaperEnvelope14|Envelope #14 (5 in. x 11-1/2 in.)|
|PaperEnvelope9|Envelope #9 (3-7/8 in. x 8-7/8 in.)|
|PaperEnvelopeB4|Envelope B4 (250 mm x 353 mm)|
|PaperEnvelopeB5|Envelope B5 (176 mm x 250 mm)|
|PaperEnvelopeB6|Envelope B6 (176 mm x 125 mm)|
|PaperEnvelopeC3|Envelope C3 (324 mm x 458 mm)|
|PaperEnvelopeC4|Envelope C4 (229 mm x 324 mm)|
|PaperEnvelopeC5|Envelope C5 (162 mm x 229 mm)|
|PaperEnvelopeC6|Envelope C6 (114 mm x 162 mm)|
|PaperEnvelopeC65|Envelope C65 (114 mm x 229 mm)|
|PaperEnvelopeDL|Envelope DL (110 mm x 220 mm)|
|PaperEnvelopeItaly|Envelope Italy (110 mm x 230 mm)|
|PaperEnvelopeMonarch|Envelope Monarch (3-7/8 in. x 7-1/2 in.)|
|PaperEnvelopePersonal|Envelope (3-5/8 in. x 6-1/2 in.)|
|PaperESheet|E size sheet|
|PaperExecutive|Executive (7-1/2 in. x 10-1/2 in.)|
|PaperFanfoldLegalGerman|German Legal Fanfold (8-1/2 in. x 13 in.)|
|PaperFanfoldStdGerman|German Standard Fanfold (8-1/2 in. x 12 in.)|
|PaperFanfoldUS|U.S. Standard Fanfold (14-7/8 in. x 11 in.)|
|PaperFolio|Folio (8-1/2 in. x 13 in.)|
|PaperLedger|Ledger (17 in. x 11 in.)|
|PaperLegal|Legal (8-1/2 in. x 14 in.)|
|PaperLetter|Letter (8-1/2 in. x 11 in.)|
|PaperLetterSmall|Letter Small (8-1/2 in. x 11 in.)|
|PaperNote|Note (8-1/2 in. x 11 in.)|
|PaperQuarto|Quarto (215 mm x 275 mm)|
|PaperStatement|Statement (5-1/2 in. x 8-1/2 in.)|
|PaperTabloid|Tabloid (11 in. x 17 in.)|

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ManagePaperSize-ManagePaperSize.java" >}}

### **Baskı Kalitesi**

Çalışma sayfalarının baskı kalitesini [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) sınıfının [**setPrintQuality**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintQuality) yöntemiyle ayarlayın. Baskı kalitesi için ölçü birimi, inç başına pik (DPI) 'dir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SetPrintQuality-SetPrintQuality.java" >}}

### **İlk Sayfa Numarası**

Çalışma sayfasının numaralandırmasını [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) sınıfının [**setFirstPageNumber**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#FirstPageNumber) yöntemiyle başlatın. setFirstPageNumber yöntemi, ilk çalışma sayfasının sayfa numarasını ayarlar ve sonraki sayfalar artan düzende numaralandırılır.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SetFirstPageNumber-SetFirstPageNumber.java" >}}

## **Kenar Boşlukları Ayarlama**

Aspose.Cells, Microsoft Excel'in sayfa düzeni seçeneklerini tamamen destekler. Geliştiriciler, baskı işlemini kontrol etmek için çalışma sayfaları için sayfa düzeni ayarlarını yapılandırabilirler. Bu konu, Aspose.Cells'ı kullanarak sayfa kenar boşluklarını yapılandırmanın nasıl yapıldığını tartışmaktadır.

**Microsoft Excel'de Sayfa Kenar Boşlukları**

![todo:image_alt_text](page-setup-features_2.png)

Aspose.Cells, bir Microsoft Excel dosyasını temsil eden [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) sınıfını sağlar. Workbook sınıfı, Excel dosyasındaki her çalışma sayfasına erişime izin veren bir Worksheets koleksiyonunu içerir. Bir çalışma sayfası, [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) sınıfı tarafından temsil edilir.

Worksheet sınıfı, sayfa düzeni seçeneklerini ayarlamak için kullanılan PageSetup özelliğini sağlar. PageSetup özelliği, yazdırılan bir çalışma sayfası için farklı sayfa düzeni seçeneklerini ayarlamayı mümkün kılan [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) sınıfının bir nesnesidir. PageSetup sınıfı, sayfa ayarlama seçeneklerini ayarlamak için kullanılan çeşitli özellikler ve yöntemler sağlar.

### **Sayfa Kenar Boşlukları**

Bir sayfanın kenar boşluklarını (sol, sağ, üst, alt) [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) sınıfının üyeleri ile belirtmek mümkündür. Sayfa kenar boşluklarını belirtmek için kullanılan bazı yöntemler aşağıda listelenmiştir.

- [**setLeftMargin(int)**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#LeftMargin)
- [**setRightMargin(int)**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#RightMargin)
- [**setTopMargin(int)**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#TopMargin)
- [**setBottomMargin(int)**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#BottomMargin)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SetMargins-SetMargins.java" >}}

### **Sayfa Üzerinde Ortala**

Bir şeyin yatay ve dikey olarak sayfa ortasına yerleştirilmesi mümkündür. [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) sınıfı bunun için üyelere sahiptir: [**setCenterHorizontally**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#CenterHorizontally) ve [**setCenterVertically**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#CenterVertically).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-CenterOnPage-CenterOnPage.java" >}}

### **Üst Bilgi ve Alt Bilgi Kenar Boşlukları**

Başlık ve altbilgi kenar boşluklarını [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) gibi üyelerle ayarlayın: [**setHeaderMargin**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#HeaderMargin) ve [**setFooterMargin**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#FooterMargin).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-HeaderAndFooterMargins-HeaderAndFooterMargins.java" >}}

## **Başlık ve Altbilgileri Ayarlama**

Başlıklar ve altbilgiler, sayfa üst kenarı veya alt kenarı üzerindeki metin ve görüntü bölümleridir. Excel çalışma sayfalarına başlık ve altbilgi eklemek de mümkündür. Başlık ve altbilgiler, örneğin sayfa numarası, yazar adı, belge başlığı veya tarih ve saat gibi her türlü yararlı bilgiyi görüntülemek için kullanılabilir. Başlık ve altbilgiler, Sayfa Düzeni ile yönetilir.

**Sayfa Düzeni diyaloğu** 

![todo:image_alt_text](page-setup-features_3.png)

Aspose.Cells, çalışma zamanında çalışma sayfalarına başlık ve altbilgi eklemeyi sağlar, ancak yazdırma için başlık ve altbilgilerin önceden tasarlanmış bir dosyada manuel olarak ayarlanması önerilir. Geliştirme süresini azaltmak için başlık ve altbilgileri kolayca ayarlamak için Microsoft Excel'i bir GUI aracı olarak kullanabilirsiniz. Aspose.Cells, dosyayı içe aktarabilir ve bu ayarları korur.

Başlık ve altbilgileri çalışma zamanında eklemek için Aspose.Cells özel sınıflar ve bazı betik komutları sağlar.

### **Betik Komutları**

Betik komutları, başlık ve altbilgileri biçimlendirmek için Aspose.Cells tarafından sağlanan özel komutlardır.

|**Betik Komutları**|**Açıklama**|
| :- | :- |
|&P| Geçerli sayfa numarası.
|&G| Bir resim.
|&N| Toplam sayfa sayısı.
|&D| Geçerli tarih.
|&T| Geçerli saat.
|&A| Çalışma sayfasının adı.
|&F| Yol olmadan dosya adı.
|&"\<FontName>"| Bir font adı. Örneğin: &"Arial"|
|&"\<FontName>, \<FontStyle>"| Bir font adı ve stil. Örneğin: &"Arial,Kalın"|
|&\<FontSize>| Yazı tipi boyutunu temsil eder. Örneğin: “&14abc”. Ancak, bu komuttan sonra başlığa yazdırılacak düz bir sayı izlenecekse, bu, yazı tipi boyutundan bir boşluk karakteri ile ayrılmalıdır. Örneğin: “&14 123”.|

### **Başlık ve Altbilgileri Ayarlama**

 [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) sınıfı, bir başlık eklemek için [**setHeader**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#setHeader(int,%20java.lang.String)) ve bir altbilgi eklemek için [**setFooter**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#setFooter(int,%20java.lang.String)) yöntemini sağlar. Betik yukarıda bahsedilen tüm yöntemler için bir argüman olarak kullanılır. Bu betik, başlık veya altbilgi için kullanılacak betiği temsil eder. Bu betik, başlıkları veya altbilgileri biçimlendirmek için betik komutlarını içerir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SetHeadersAndFooters-SetHeadersAndFooters.java" >}}

### **Bir Başlık veya Altbilgiye Grafik Ekleyin**

 [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) sınıfı, çalışma sayfası başlığı ve altbilgisine resim eklemek için [**setHeadPicture**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#setHeaderPicture(int,%20byte[])) ve [**setFooterPicture**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#setFooterPicture(int,%20byte[])) yöntemlerine sahiptir. Bu yöntemler iki parametre alır:

- **Bölüm**, resmin yerleştirileceği başlık veya altbilgi bölümü. 0, 1 ve 2 numaralı değerlerle temsil edilen sol, orta ve sağ olmak üzere üç bölüm vardır.
- **Dosya InputStream**, grafik verisi. Bin veriler, bir byte dizisi bufferine yazılmalıdır.

Kodu çalıştırdıktan sonra dosyayı açın ve Microsoft Excel'de çalışma sayfasının başlığını kontrol edin:

1. **Dosya** menüsünde, **Sayfa Düzeni**'ni seçin.
1. Sayfa Düzeni iletişim kutusunda **Başlık/Altbilgi** sekmesini seçin.

**Başlık/Altbilgiye grafik ekleme** 

![todo:image_alt_text](page-setup-features_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-InsertImageInHeaderFooter-InsertImageInHeaderFooter.java" >}}

### **Sadece İlk Sayfa Başlığına Grafik Ekle**

[**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) sınıfı ayrıca örneğin [**setPicture**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#setPicture(boolean,%20boolean,%20boolean,%20int,%20byte[])), [**setFirstPageHeader**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#setFirstPageHeader(int,%20java.lang.String)), [**setFirstPageFooter**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#setFirstPageFooter(int,%20java.lang.String)) gibi diğer faydalı yöntemlere sahiptir, sayfa başlığı/altbilgisine resim eklemek için. İlk sayfa özel bir sayfadır: örneğin bir şirket logosunu göstermek istemek yaygındır.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-InsertGraphicinFirstPageHeaderOnly-InsertGraphicinFirstPageHeaderOnly.java" >}}

## **Baskı Seçeneklerini Ayarlama**

Microsoft Excel'in sayfa ayarı ayarları, kullanıcıların çalışma sayfalarının nasıl yazdırılacağını kontrol etmelerini sağlayan birkaç yazdırma seçeneği (ayrıca sayfa seçenekleri olarak da adlandırılır) sağlar. Bu yazdırma seçenekleri, kullanıcıların:

- Çalışma sayfasında belirli bir baskı alanı seçin.
- Başlıkları yazdırın.
- Izgaraları yazdırın.
- Satır ve sütun başlıklarını yazdırma.
- Taslak kalitesine ulaşın.
- Yorumları yazdırın.
- Hücre hatalarını yazdırın.
- Sayfa sıralamasını tanımlayın.

Tüm bu yazdırma seçenekleri aşağıda gösterilmiştir.

**Yazdırma (sayfa) seçenekleri** 

![todo:image_alt_text](page-setup-features_5.png)

### **Yazdırma ve Sayfa Seçeneklerini Ayarlama**

spose.Cells, Microsoft Excel tarafından sunulan tüm yazdırma seçeneklerini destekler ve geliştiriciler [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) sınıfının sunduğu özellikler kullanarak bu seçenekleri çalışma sayfaları için kolayca yapılandırabilir. Bu özelliklerin nasıl kullanılacağı aşağıda daha detaylı olarak tartışılmıştır.

### **Baskı Alanı Belirle**

Varsayılan olarak, sadece veri içeren çalışma sayfasının tüm alanlarını içeren baskı alanı oluşturulur. Geliştiriciler, çalışma sayfasının belirli bir baskı alanını belirleyebilirler.

Belirli bir baskı alanı seçmek için, [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) sınıfının [**setPrintArea**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintArea) özelliğini kullanın. Bu özelliğe baskı alanını tanımlayan bir hücre aralığı atayın.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SetPrintArea-SetPrintArea.java" >}}

### **Başlıkları Yazdırma**

Aspose.Cells, basılı bir çalışma sayfasının tüm sayfalarında tekrarlanacak satır ve sütun başlıklarını belirlemenize izin verir. Bunu yapmak için [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) sınıfının [**setPrintTitleColumns**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintTitleColumns) ve [**setPrintTitleRows**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintTitleRows) özelliklerini kullanın.

Tekrar edilecek satırlar veya sütunlar, satır veya sütun numaralarını geçirerek tanımlanır. Örneğin satırlar $1:$2 ve sütunlar $A:$B olarak tanımlanır.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SetPrintTitle-SetPrintTitle.java" >}}

### **Diğer Yazdırma Seçeneklerini Belirleme**

[**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) sınıfı ayrıca aşağıdaki genel yazdırma seçeneklerini ayarlamak için birkaç başka özellik sunar:

- [**setPrintGridlines**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintGridlines), ızgaraların yazdırılıp yazdırılmayacağını tanımlayan boolean bir özellik.
- [*setPrintHeadings*](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintHeadings), satır ve sütun başlıklarını yazdırıp yazdırmayacağını tanımlayan boolean bir özellik.
- [**setBlackAndWhite**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#BlackAndWhite), çalışma sayfasını siyah beyaz modda yazdırıp yazdırmayacağını tanımlayan boolean bir özellik.
- [**setPrintComments**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintComments), çalışma sayfasındaki yazdırma yorumlarını veya çalışma sayfasının sonunda görüntülemeyi tanımlar.
- [**setPrintDraft**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintDraft), bir çalışma sayfasının taslak kalitesinde mi yoksa kaliteli basılmasını isteyip istemediğini belirleyen bir boolean özelliği.
- [**setPrintErrors**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintErrors), hücre hatalarının görüntülendiği, boş, tire veya N/A olarak basılıp basılmayacağını belirler.

[**PrintComments**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintComments) ve [**PrintErrors**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintErrors) özelliklerini ayarlamak için Aspose.Cells ayrıca [**setPrintComments**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintComments) ve [**setPrintErrors**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintErrors) özelliklerine atanacak önceden tanımlanmış değerleri içeren iki numaralandırma, [**PrintCommentsType**](https://reference.aspose.com/cells/java/com.aspose.cells/PrintCommentsType) ve [**PrintErrorsType**](https://reference.aspose.com/cells/java/com.aspose.cells/PrintErrorsType) sağlar.

[**PrintCommentsType**](https://reference.aspose.com/cells/java/com.aspose.cells/PrintCommentsType) numaralandırmasındaki önceden tanımlanmış değerler aşağıda açıklanmıştır.

|**Yazdırma Yorumları Türleri**|**Açıklama**|
| :- | :- |
|[**PRINT_IN_PLACE**](https://reference.aspose.com/cells/java/com.aspose.cells/printcommentstype#PRINT_IN_PLACE)|Çalışma sayfasında görüntülendiği gibi yorumları yazdırmayı belirtir.|
|[**PRINT_NO_COMMENTS**](https://reference.aspose.com/cells/java/com.aspose.cells/printcommentstype#PRINT_NO_COMMENTS)|Yorumları yazdırmamayı belirtir.|
|[**PRINT_SHEET_END**](https://reference.aspose.com/cells/java/com.aspose.cells/printcommentstype#PRINT_SHEET_END)|Çalışma sayfasının sonunda yorumları yazdırmayı belirtir.|

[**PrintErrorsType**](https://reference.aspose.com/cells/java/com.aspose.cells/PrintErrorsType) numaralandırmasındaki önceden tanımlanmış değerler aşağıda açıklanmıştır.

|**Yazdırma Hataları Türleri**|**Açıklama**|
| :- | :- |
|[**PRINT_ERRORS_BLANK**](https://reference.aspose.com/cells/java/com.aspose.cells/printerrorstype#PRINT_ERRORS_BLANK)|Hataları yazdırmamayı belirtir.|
|[**PRINT_ERRORS_DASH**](https://reference.aspose.com/cells/java/com.aspose.cells/printerrorstype#PRINT_ERRORS_DASH)|Hataları "--" olarak yazdırmayı belirtir.|
|[**PRINT_ERRORS_DISPLAYED**](https://reference.aspose.com/cells/java/com.aspose.cells/printerrorstype#PRINT_ERRORS_DISPLAYED)|Hataları görüntülendiği gibi yazdırmayı belirtir.|
|[**PRINT_ERRORS_NA**](https://reference.aspose.com/cells/java/com.aspose.cells/printerrorstype#PRINT_ERRORS_NA)|Hataları "#N/A" olarak yazdırmayı belirtir.|

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-OtherPrintOptions-OtherPrintOptions.java" >}}

### **Sayfa Sırasını Belirleme**

[**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) sınıfı, çalışma sayfanızın birden fazla sayfasının yazdırılacak sırasını belirlemek için kullanılan [**setOrder**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#Order) özelliğini sağlar. Sayfaların sıralanması için iki olasılık aşağıdaki gibidir:

- **Aşağıdan sonra sağa** tüm sayfaları sağa yazdırmadan önce tüm sayfaları aşağı yazdırır.
- **Saat yönünün tersine** sayfaları alttan sağa yazdırır önce tüm sayfaları altta yazdırır.

Aspose.Cells, [**setOrder**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#Order) yöntemine atanacak tüm önceden tanımlanmış sıralama türlerini içeren bir numaralandırma olan [**PrintOrderType**](https://reference.aspose.com/cells/java/com.aspose.cells/PrintOrderType) sağlar.

[**PrintOrderType**](https://reference.aspose.com/cells/java/com.aspose.cells/PrintOrderType) numaralandırmasındaki önceden tanımlanmış değerler aşağıda açıklanmıştır.

|**Yazdırma Sıralama Türleri**|**Açıklama**|
| :- | :- |
|[**DOWN_THEN_OVER**](https://reference.aspose.com/cells/java/com.aspose.cells/printordertype#DOWN_THEN_OVER)|Aşağı, sonra sağa yazdırır.|
|[**OVER_THEN_DOWN**](https://reference.aspose.com/cells/java/com.aspose.cells/printordertype#OVER_THEN_DOWN)|Soldan sağa yazdırır önce tüm sayfaları altta yazdırır.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SetPageOrder-SetPageOrder.java" >}}

## **Excel dosyasındaki Mevcut Çalışma Sayfası Yazıcı Ayarlarını Kaldırma**

Bu konuyla ilgili bu makaleyi inceleyin.

## **Gelişmiş Konular**
- [Sayfa Ayarı Ölçekleme Faktörünü Hesaplayın](/cells/tr/java/calculate-page-setup-scaling-factor/)
- [Kaynak Çalışma Sayfasından Hedef Çalışma Sayfasına Sayfa Ayarı Ayarlarını Kopyala](/cells/tr/java/copy-page-setup-settings-from-source-worksheet-into-destination-worksheet/)
- [Çalışma Sayfasının Kağıt Boyutunu Otomatik Olup Olmadığını Belirleme](/cells/tr/java/determine-if-paper-size-of-worksheet-is-automatic/)
- [Çalışma Sayfasının PageSetup'tan Kağıt Genişliği ve Yüksekliğini Al](/cells/tr/java/get-paper-width-and-height-from-pagesetup-of-worksheet/)
- [Otomatik Olarak Çalışma Sayfası için Özel Kağıt Boyutunun Uygulanması](/cells/tr/java/implement-custom-paper-size-of-worksheet-for-rendering/)
- [Sayfa Ayarları ve Yazdırma Seçenekleri](/cells/tr/java/page-setup-and-printing-options/)
- [Excel dosyasındaki Mevcut Çalışma Sayfası Yazıcı Ayarlarını Kaldırma](/cells/tr/java/remove-existing-printersettings-of-worksheets-in-excel-file/)
