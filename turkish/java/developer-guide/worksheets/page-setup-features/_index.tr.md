---
title: Sayfa Düzeni Özellikleri
type: docs
weight: 40
url: /tr/java/page-setup-features/
---
Bazen, çalışma sayfalarının yazdırmayı denetlemesi için sayfa yapısı ayarlarının yapılandırılması gerekir. Bu sayfa yapısı ayarları çeşitli seçenekler sunar.

**Sayfa Seçenekleri** 

![yapılacaklar:resim_alternatif_metin](page-setup-features_1.png)

Sayfa yapısı seçenekleri Aspose.Cells'de tam olarak desteklenmektedir. Bu makale, Aspose.Cells ile sayfa seçeneklerinin nasıl ayarlanacağını açıklamaktadır.

## **Ayar Sayfası Seçenekleri**

 Aspose.Cells bir sınıf sağlar,[**Çalışma kitabı**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) , bu bir Microsoft Excel dosyasını temsil eder. Workbook sınıfı, Excel dosyasındaki her çalışma sayfasına erişim sağlayan bir Worksheets koleksiyonu içerir. Bir çalışma sayfası şununla temsil edilir:[**Çalışma kağıdı**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) sınıf.

Worksheet sınıfı, sayfa yapısı seçeneklerini ayarlamak için kullanılan PageSetup özelliğini sağlar. Aslında, PageSetup özelliği, yazdırılan bir çalışma sayfası için sayfa düzeni seçeneklerini ayarlamayı mümkün kılan PageSetup sınıfının bir nesnesidir. PageSetup sınıfı, sayfa kurulum seçeneklerini ayarlamak için kullanılan çeşitli özellikler sağlar. Bu özelliklerden bazıları aşağıda tartışılmaktadır.

### **Sayfa yönlendirmesi**

Sayfa yönlendirmesi kullanılarak dikey veya yatay olarak ayarlanabilir.[**Sayfa ayarı**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) sınıf'[**setOrientation(PageOrientationType)**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#Orientation) yöntem. bu[**setOrientation(PageOrientationType)**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#Orientation) yöntemi alır[**Sayfa Yönlendirme Türü**](https://reference.aspose.com/cells/java/com.aspose.cells/PageOrientationType) parametre olarak numaralandırma. üyeleri[**Sayfa Yönlendirme Türü**](https://reference.aspose.com/cells/java/com.aspose.cells/PageOrientationType) numaralandırma aşağıda listelenmiştir.

|**Sayfa Yönlendirme Türleri**|**Açıklama**|
|:- |:- |
|[**MANZARA**](https://reference.aspose.com/cells/java/com.aspose.cells/pageorientationtype#LANDSCAPE)|Yatay yönlendirme|
|[**VESİKA**](https://reference.aspose.com/cells/java/com.aspose.cells/pageorientationtype#PORTRAIT)|Dikey yönlendirme|

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-PageOrientation-PageOrientation.java" >}}

### **Ölçekleme faktörü**

 Ölçeklendirme faktörünü ayarlayarak bir çalışma sayfasının boyutunu küçültmek veya büyütmek mümkündür.[**yakınlaştırmayı ayarla**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#Zoom) yöntemi[**Sayfa ayarı**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) sınıf.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ScalingFactor-ScalingFactor.java" >}}

### **Sayfalara Sığdır Seçenekleri**

 Çalışma sayfasının içeriğini belirli sayıda sayfaya sığdırmak için[**Sayfa ayarı**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) sınıf'[**setFitToPagesUzun**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#FitToPagesTall) ve[**setFitToPagesWide**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#FitToPagesWide) yöntemler. Bu yöntemler aynı zamanda çalışma sayfalarını ölçeklendirmek için de kullanılır.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-FitToPagesOptions-FitToPagesOptions.java" >}}

### **Kağıt boyutu**

 kullanarak çalışma sayfalarının yazdırılacağı kağıt boyutunu ayarlayın.[**Sayfa ayarı**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) sınıf'[**Kağıt boyutu**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PaperSize) Emlak. PaperSize özelliği, ön tanımlı değerlerden birini kabul eder.[**KağıtBoyutuTürü**](https://reference.aspose.com/cells/java/com.aspose.cells/PaperSizeType) numaralandırma, aşağıda listelenmiştir.

|**Kağıt Boyutu Türleri**|**Açıklama**|
|:- |:- |
|Kağıt10x14|10 inç x 14 inç|
|Kağıt11x17|11 inç x 17 inç|
|KağıtA3|A3 (297 mm x 420 mm)|
|KağıtA4|A4 (210 mm x 297 mm)|
|KağıtA4Küçük|A4 Küçük (210 mm x 297 mm)|
|KağıtA5|A5 (148 mm x 210 mm)|
|KağıtB3|B3 (13,9 x 19,7 inç)|
|KağıtB4|B4 (250 mm x 354 mm)|
|KağıtB5|B5 (182 mm x 257 mm)|
|KağıtKartvizit|Kartvizit (90 mm x 55 mm)|
|KağıtÇerçeve|C boyutlu levha|
|KağıtDSayfa|D boyutlu sayfa|
|KağıtZarf10|Zarf #10 (4-1/8 inç x 9-1/2 inç)|
|KağıtZarf11|Zarf #11 (4-1/2 inç x 10-3/8 inç)|
|KağıtZarf12|Zarf #12 (4-1/2 inç x 11 inç)|
|KağıtZarf14|Zarf #14 (5 inç x 11-1/2 inç)|
|KağıtZarf9|Zarf #9 (3-7/8 inç x 8-7/8 inç)|
|KağıtZarfB4|Zarf B4 (250 mm x 353 mm)|
|KağıtZarfB5|Zarf B5 (176 mm x 250 mm)|
|KağıtZarfB6|Zarf B6 (176 mm x 125 mm)|
|KağıtZarfC3|Zarf C3 (324 mm x 458 mm)|
|KağıtZarfC4|Zarf C4 (229 mm x 324 mm)|
|KağıtZarfC5|Zarf C5 (162 mm x 229 mm)|
|KağıtZarfC6|Zarf C6 (114 mm x 162 mm)|
|KağıtZarfC65|Zarf C65 (114 mm x 229 mm)|
|Kağıt ZarfıDL|Zarf DL (110 mm x 220 mm)|
|KağıtZarfİtalya|Zarf İtalya (110 mm x 230 mm)|
|KağıtZarfMonarch|Zarf Monarch (3-7/8 inç x 7-1/2 inç)|
|KağıtZarfKişisel|Zarf (3-5/8 inç x 6-1/2 inç)|
|KâğıtÇerçeve|E boyutu sayfası|
|Kağıt Yöneticisi|Yönetici (7-1/2 inç x 10-1/2 inç)|
|PaperFanfoldLegal Almanca|Alman Yasal Yelpaze Katlama (8-1/2 inç x 13 inç)|
|PaperFanfoldStd Almanca|Alman Standardı Yelpaze Katlama (8-1/2 inç x 12 inç)|
|PaperFanfoldABD|ABD Standardı Yelpaze Katlama (14-7/8 inç x 11 inç)|
|Kağıt Folyo|Folyo (8-1/2 inç x 13 inç)|
|Kağıt Defteri|Defter (17 inç x 11 inç)|
|KağıtYasal|Yasal (8-1/2 inç x 14 inç)|
|KağıtMektup|Harf (8-1/2 inç x 11 inç)|
|KağıtMektupKüçük|Küçük Harf (8-1/2 inç x 11 inç)|
|Kağıt Not|Not (8-1/2 inç x 11 inç)|
|Kağıt Çeyrek|Çeyrek (215 mm x 275 mm)|
|Kağıt Bildirimi|Açıklama (5-1/2 inç x 8-1/2 inç)|
|Kağıt Tabloid|Tabloid (11 inç x 17 inç)|

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ManagePaperSize-ManagePaperSize.java" >}}

### **Baskı kalitesi**

 ile yazdırılacak çalışma sayfalarının baskı kalitesini ayarlayın.[**Sayfa ayarı**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) sınıf'[**setPrintQuality**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintQuality) yöntem. Baskı kalitesi için ölçüm birimi inç başına nokta sayısıdır (DPI).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SetPrintQuality-SetPrintQuality.java" >}}

### **İlk Sayfa Numarası**

 kullanarak çalışma sayfası sayfalarının numaralandırılmasını başlatın.[**Sayfa ayarı**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) sınıf'[**setFirstPageNumber**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#FirstPageNumber) yöntem. setFirstPageNumber yöntemi, ilk çalışma sayfası sayfasının sayfa numarasını ayarlar ve sonraki sayfalar artan sırada numaralandırılır.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SetFirstPageNumber-SetFirstPageNumber.java" >}}

## **Kenar Boşluklarını Ayarlama**

Aspose.Cells, Microsoft Excel'in sayfa düzeni seçeneklerini tamamen destekler. Geliştiricilerin, yazdırma sürecini kontrol etmek için çalışma sayfaları için sayfa kurulum ayarlarını yapılandırması gerekebilir. Bu konuda, sayfa kenar boşluklarını yapılandırmak için Aspose.Cells'in nasıl kullanılacağı anlatılmaktadır.

**Microsoft Excel'de sayfa kenar boşlukları**

![yapılacaklar:resim_alternatif_metin](page-setup-features_2.png)

 Aspose.Cells bir sınıf sağlar,[**Çalışma kitabı**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) bu bir Microsoft Excel dosyasını temsil eder. Workbook sınıfı, bir Excel dosyasındaki her çalışma sayfasına erişim sağlayan Worksheets koleksiyonunu içerir. Bir çalışma sayfası şununla temsil edilir:[**Çalışma kağıdı**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) sınıf.

 Worksheet sınıfı, sayfa yapısı seçeneklerini ayarlamak için kullanılan PageSetup özelliğini sağlar. PageSetup özniteliği,[**Sayfa ayarı**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) yazdırılan bir çalışma sayfası için farklı sayfa düzeni seçenekleri ayarlamayı mümkün kılan sınıf. PageSetup sınıfı, sayfa yapısı seçeneklerini ayarlamak için kullanılan çeşitli özellikler ve yöntemler sağlar.

### **Sayfa Kenar Boşlukları**

 ile bir sayfanın kenar boşluklarını (sol, sağ, üst, alt) ayarlayın.[**Sayfa ayarı**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) sınıf üyeleri. Sayfa kenar boşluklarını belirtmek için kullanılan yöntemlerden birkaçı aşağıda listelenmiştir:

- [**setLeftMargin(int)**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#LeftMargin)
- [**setRightMargin(int)**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#RightMargin)
- [**setTopMargin(int)**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#TopMargin)
- [**setBottomMargin(int)**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#BottomMargin)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SetMargins-SetMargins.java" >}}

### **Sayfada Ortala**

 Bir sayfada bir şeyi yatay ve dikey olarak ortalamak mümkündür. bu[**Sayfa ayarı**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) sınıfın bu amaç için üyeleri vardır:[**setCenterYatay olarak**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#CenterHorizontally) ve[**setCenterDikey olarak**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#CenterVertically).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-CenterOnPage-CenterOnPage.java" >}}

### **Üstbilgi ve Altbilgi Kenar Boşlukları**

 ile üstbilgi ve altbilgi kenar boşluklarını ayarlayın[**Sayfa ayarı**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) gibi üyeler[**setHeaderMargin**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#HeaderMargin) ve[**setFooterMargin**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#FooterMargin).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-HeaderAndFooterMargins-HeaderAndFooterMargins.java" >}}

## **Üst Bilgileri ve Alt Bilgileri Ayarlama**

Üstbilgiler ve altbilgiler, bir sayfada üst kenar boşluğunun üstündeki veya alt kenar boşluğunun altındaki metin ve resim bölümleridir. Çalışma sayfalarına üstbilgi ve altbilgi eklemek de mümkündür. Üstbilgiler ve altbilgiler, sayfa numarası, yazar adı, belge başlığı veya tarih ve saat gibi her türlü yararlı bilgiyi görüntülemek için kullanılabilir. Üst bilgiler ve alt bilgiler de Sayfa Yapısı iletişim kutusu kullanılarak yönetilir.

**Sayfa Yapısı iletişim kutusu** 

![yapılacaklar:resim_alternatif_metin](page-setup-features_3.png)

Aspose.Cells, çalışma zamanında çalışma sayfalarına üstbilgi ve altbilgi eklenmesine izin verir, ancak üstbilgi ve altbilgilerin yazdırma için önceden tasarlanmış bir dosyada manuel olarak ayarlanması önerilir. Microsoft Excel'i, geliştirme süresini kısaltmak üzere üst bilgileri ve alt bilgileri kolayca ayarlamak için bir GUI aracı olarak kullanabilirsiniz. Aspose.Cells dosyayı içe aktarabilir ve bu ayarları rezerve edebilir.

Çalışma zamanında üst bilgiler ve alt bilgiler eklemek için Aspose.Cells, biçimlendirmeyi kontrol etmek için özel sınıflar ve bazı betik komutları sağlar.

### **Komut Dosyası Komutları**

Komut dosyası komutları, Aspose.Cells tarafından sağlanan ve geliştiricilerin üst bilgileri ve alt bilgileri biçimlendirmesine olanak tanıyan özel komutlardır.

|**Komut Dosyası Komutları**|**Açıklama**|
|:- |:- |
|&P|Geçerli sayfa numarası.|
|&G|Bir resim.|
|&N|Toplam sayfa sayısı.|
|&D|Geçerli tarih.|
|&T|şimdiki zaman|
|&A|Çalışma sayfasının adı.|
|&F|Yolsuz dosya adı.|
|&"\<FontName>"|Bir yazı tipi adı. Örneğin: &"Arial"|
|&"\<FontName>, \<FontStyle>"|Stili olan bir yazı tipi adı. Örneğin: &"Arial,Kalın"|
|&\<FontSize>|Yazı tipi boyutunu temsil eder. Örneğin: “&14abc”. Ancak bu komutun ardından başlıkta yazdırılacak düz bir sayı geliyorsa bu, yazı tipi boyutundan bir boşluk karakteri ile ayrılmalıdır. Örneğin: “&14 123”.|

### **Üstbilgileri ve Altbilgileri Ayarlama**

 bu[**Sayfa ayarı**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) sınıf yöntem sağlar[**setHeader**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#setHeader(int,%20java.lang.String) bir başlık eklemek için ve[**setFooter**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#setFooter(int,%20java.lang.String)) çalışma sayfasına altbilgi eklemek için. Komut dosyası, yukarıda belirtilen tüm yöntemler için bir argüman olarak kullanılır. Üstbilgi veya altbilgi için kullanılacak komut dosyasını temsil eder. Bu komut dosyası, üst bilgileri veya alt bilgileri biçimlendirmek için komut dosyası komutları içerir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SetHeadersAndFooters-SetHeadersAndFooters.java" >}}

### **Üst Bilgiye veya Alt Bilgiye Grafik Ekleme**

 bu[**Sayfa ayarı**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) sınıfın yöntemleri vardır[**setHeadPicture**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#setHeaderPicture(int,%20byte[]) ) ve[**setFooterPicture**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#setFooterPicture(int,%20byte[])) bir çalışma sayfasının üst bilgisine ve alt bilgisine resim eklemek için. Bu yöntemler iki parametre alır:

- **Bölüm**, üstbilginin veya altbilginin resmin yerleştirileceği bölümü. Üç bölüm vardır: sırasıyla 0, 1 ve 2 sayısal değerleri ile temsil edilen sol, orta ve sağ.
- **Dosya Giriş Akışı**, grafiksel veriler. İkili veriler, bir bayt dizisinin arabelleğine yazılmalıdır.

Kodu çalıştırdıktan ve dosyayı açtıktan sonra, çalışma sayfasının başlığını Microsoft Excel'de kontrol edin:

1.  Üzerinde**Dosya** menü, seç**Sayfa ayarı**.
1.  Sayfa Yapısı iletişim kutusunda,**Üstbilgi Altbilgi** sekme.

**Üst bilgiye/alt bilgiye grafik ekleme** 

![yapılacaklar:resim_alternatif_metin](page-setup-features_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-InsertImageInHeaderFooter-InsertImageInHeaderFooter.java" >}}

### **Yalnızca İlk Sayfa Başlığına Grafik Ekleme**

 bu[**Sayfa ayarı**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) sınıfın başka yararlı yöntemleri de vardır, örneğin[**resim ayarla**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#setPicture(boolean,%20boolean,%20boolean,%20int,%20byte[])), [**setFirstPageHeader**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#setFirstPageHeader(int,%20java.lang.String)), [**setFirstPageFooter**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#setFirstPageFooter(int,%20java.lang.String)), bir çalışma sayfasının ilk sayfa üstbilgisine/altbilgisine resim eklemek için. İlk sayfa özel bir sayfadır: şirket logosu gibi özel bilgilerin gösterilmesini istemek yaygındır.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-InsertGraphicinFirstPageHeaderOnly-InsertGraphicinFirstPageHeaderOnly.java" >}}

## **Yazdırma Seçeneklerini Ayarlama**

Microsoft Excel'in sayfa ayarı ayarları, kullanıcıların çalışma sayfası sayfalarının nasıl yazdırılacağını denetlemesine olanak tanıyan çeşitli yazdırma seçenekleri (sayfa seçenekleri olarak da anılır) sağlar. Bu yazdırma seçenekleri, kullanıcıların şunları yapmasına olanak tanır:

- Çalışma sayfasında belirli bir yazdırma alanı seçin.
- Başlıkları yazdırın.
- Kılavuz çizgilerini yazdırın.
- Satır ve sütun başlıklarını yazdır
- Taslak kalitesine ulaşın.
- Yorumları yazdırın.
- Yazdırma hücresi hataları.
- Sayfa sıralamasını tanımlayın.

Bu yazdırma seçeneklerinin tümü aşağıda gösterilmiştir.

**Yazdırma (sayfa) seçenekleri** 

![yapılacaklar:resim_alternatif_metin](page-setup-features_5.png)

### **Yazdırma ve Sayfa Seçeneklerini Ayarlama**

 spose.Cells, Microsoft Excel tarafından sunulan tüm yazdırma seçeneklerini destekler ve geliştiriciler, Excel tarafından sunulan özellikleri kullanarak bu seçenekleri çalışma sayfaları için kolayca yapılandırabilir.[**Sayfa ayarı**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup)sınıf. Bu özelliklerin nasıl kullanıldığı aşağıda daha ayrıntılı olarak tartışılmaktadır.

### **Yazdırma Alanını Ayarla**

Varsayılan olarak, yalnızca yazdırma alanı, çalışma sayfasının veri içeren tüm alanlarını içerir. Geliştiriciler, çalışma sayfasının belirli bir yazdırma alanını oluşturabilir.

 Belirli bir yazdırma alanı seçmek için[**Sayfa ayarı**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) sınıf'[**setPrintArea**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintArea) Emlak. Bu özelliğe yazdırma alanını tanımlayan bir hücre aralığı atayın.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SetPrintArea-SetPrintArea.java" >}}

### **Baskı Başlıklarını Ayarla**

 Aspose.Cells, yazdırılan bir çalışma sayfasının tüm sayfalarında yinelenecek satır ve sütun başlıkları belirlemenizi sağlar. Bunu yapmak için[**Sayfa ayarı**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) sınıf'[**setPrintTitleColumns**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintTitleColumns) ve[**setPrintTitleRows**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintTitleRows) özellikler.

Tekrarlanacak satır veya sütunlar, satır veya sütun numaraları geçirilerek tanımlanır. Örneğin, satırlar $1:$2 olarak tanımlanır ve sütunlar $A:$B olarak tanımlanır.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SetPrintTitle-SetPrintTitle.java" >}}

### **Diğer Yazdırma Seçeneklerini Ayarlayın**

 bu[**Sayfa ayarı**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) class ayrıca genel yazdırma seçeneklerini aşağıdaki gibi ayarlamak için birkaç başka özellik daha sağlar:

- [**setPrintGridlines**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintGridlines), kılavuz çizgilerinin yazdırılıp yazdırılmayacağını tanımlayan bir Boole özelliği.
- [*setPrintHeadings*](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintHeadings), satır ve sütun başlıklarının yazdırılıp yazdırılmayacağını tanımlayan bir Boole özelliği.
- [**setSiyahBeyaz**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#BlackAndWhite), çalışma sayfasının siyah beyaz modda yazdırılıp yazdırılmayacağını tanımlayan bir Boole özelliği.
- [**setPrintComments**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintComments), yazdırma yorumlarının çalışma sayfasında mı yoksa çalışma sayfasının sonunda mı görüntüleneceğini tanımlar.
- [**setPrintDraft**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintDraft), çalışma sayfasının taslak kalitesinde yazdırılıp yazdırılmayacağını tanımlayan bir boole özelliği.
- [**setPrintErrors**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintErrors), hücre hatalarının görüntülenen, boş, kısa çizgi veya N/A olarak yazdırılıp yazdırılmayacağını tanımlar.

 ayarlamak için[**Yorumları Yazdır**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintComments) ve[**Yazdırma Hataları**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintErrors) özellikler, Aspose.Cells ayrıca iki numaralandırma sağlar,[**YazdırYorum Türü**](https://reference.aspose.com/cells/java/com.aspose.cells/PrintCommentsType) ve[**Yazdırma HatalarıTürü**](https://reference.aspose.com/cells/java/com.aspose.cells/PrintErrorsType) atanacak önceden tanımlanmış değerleri içeren[**setPrintComments**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintComments) ve[**setPrintErrors**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintErrors) sırasıyla özellikler.

 Önceden tanımlanmış değerler,[**YazdırYorum Türü**](https://reference.aspose.com/cells/java/com.aspose.cells/PrintCommentsType) numaralandırma aşağıda açıklanmıştır.

|**Yorum Türlerini Yazdır**|**Açıklama**|
|:- |:- |
|[**PRINT_IN_PLACE**](https://reference.aspose.com/cells/java/com.aspose.cells/printcommentstype#PRINT_IN_PLACE)|Yorumların çalışma sayfasında görüntülendiği şekilde yazdırılacağını belirtir.|
|[**PRINT_NO_COMMENTS**](https://reference.aspose.com/cells/java/com.aspose.cells/printcommentstype#PRINT_NO_COMMENTS)|Yorumların yazdırılmayacağını belirtir.|
|[**PRINT_SHEET_END**](https://reference.aspose.com/cells/java/com.aspose.cells/printcommentstype#PRINT_SHEET_END)|Çalışma sayfasının sonunda yorumların yazdırılacağını belirtir.|

 Önceden tanımlanmış değerler[**Yazdırma HatalarıTürü**](https://reference.aspose.com/cells/java/com.aspose.cells/PrintErrorsType) numaralandırma aşağıda açıklanmıştır.

|**Yazdırma Hatası Türleri**|**Açıklama**|
|:- |:- |
|[*PRINT_ERRORS_BLANK*](https://reference.aspose.com/cells/java/com.aspose.cells/printerrorstype#PRINT_ERRORS_BLANK)|Hataların yazdırılmayacağını belirtir.|
|[**PRINT_ERRORS_DASH**](https://reference.aspose.com/cells/java/com.aspose.cells/printerrorstype#PRINT_ERRORS_DASH)|Hataların "--" olarak yazdırılacağını belirtir.|
|[**PRINT_ERRORS_DISPLAYED**](https://reference.aspose.com/cells/java/com.aspose.cells/printerrorstype#PRINT_ERRORS_DISPLAYED)|Hataların görüntülendiği şekilde yazdırılacağını belirtir.|
|[**PRINT_ERRORS_NA**](https://reference.aspose.com/cells/java/com.aspose.cells/printerrorstype#PRINT_ERRORS_NA)|Hataların "#N/A" olarak yazdırılacağını belirtir.|

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-OtherPrintOptions-OtherPrintOptions.java" >}}

### **Sayfa Sırasını Ayarla**

 bu[**Sayfa ayarı**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) sınıf sağlar[**siparişi ayarla**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#Order) çalışma sayfanızın birden çok sayfasının yazdırılmasını sıralamak için kullanılan özellik. Sayfaları aşağıdaki gibi sıralamak için iki olasılık vardır:

- **Aşağı sonra üzerinde** herhangi bir sayfayı sağa yazdırmadan önce tüm sayfaları aşağıya yazdırır.
- **Sonra aşağı** aşağıdaki sayfaları yazdırmadan önce sayfaları soldan sağa yazdırır.

 Aspose.Cells bir numaralandırma sağlar,[**BaskıSiparişTürü**](https://reference.aspose.com/cells/java/com.aspose.cells/PrintOrderType) , atanacak tüm önceden tanımlanmış sipariş türlerini içeren[**siparişi ayarla**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#Order) yöntem.

 Önceden tanımlanmış değerler[**BaskıSiparişTürü**](https://reference.aspose.com/cells/java/com.aspose.cells/PrintOrderType) numaralandırma aşağıda açıklanmıştır.

|**Yazdırma Sırası Türleri**|**Açıklama**|
|:- |:- |
|[**AŞAĞI_THEN_OVER**](https://reference.aspose.com/cells/java/com.aspose.cells/printordertype#DOWN_THEN_OVER)|Aşağıya doğru yazdırın, sonra üzerine.|
|[**OVER_THEN_DOWN**](https://reference.aspose.com/cells/java/com.aspose.cells/printordertype#OVER_THEN_DOWN)|Üstüne yazdırın, sonra aşağı.|

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SetPageOrder-SetPageOrder.java" >}}

## **Excel dosyasındaki Çalışma Sayfalarının Mevcut Yazıcı Ayarlarını Kaldır**

Lütfen bu konuyla ilgili bu makaleye bakın.

## **ileri konular**
- [Sayfa Yapısı Ölçeklendirme Faktörünü Hesapla](/cells/tr/java/calculate-page-setup-scaling-factor/)
- [Sayfa Yapısı Ayarlarını Kaynak Çalışma Sayfasından Hedef Çalışma Sayfasına Kopyalayın](/cells/tr/java/copy-page-setup-settings-from-source-worksheet-into-destination-worksheet/)
- [Çalışma Sayfasının Kağıt Boyutunun Otomatik olup olmadığını belirleme](/cells/tr/java/determine-if-paper-size-of-worksheet-is-automatic/)
- [Çalışma Sayfasının Sayfa Yapısından Kağıt Genişliğini ve Yüksekliğini Alın](/cells/tr/java/get-paper-width-and-height-from-pagesetup-of-worksheet/)
- [İşleme için Çalışma Sayfasının Özel Kağıt Boyutunu Uygulayın](/cells/tr/java/implement-custom-paper-size-of-worksheet-for-rendering/)
- [Sayfa Yapısı ve Yazdırma Seçenekleri](/cells/tr/java/page-setup-and-printing-options/)
- [Excel dosyasındaki Çalışma Sayfalarının Mevcut Yazıcı Ayarlarını Kaldır](/cells/tr/java/remove-existing-printersettings-of-worksheets-in-excel-file/)
