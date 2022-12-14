---
title: Veri Biçimlendirme
type: docs
weight: 80
url: /tr/java/data-formatting/
---
## **Cells'de Verileri Biçimlendirme Yaklaşımları**
Çalışma sayfası hücreleri düzgün biçimlendirilirse, kullanıcıların hücrenin içeriğini (verilerini) okumasının daha kolay hale geldiği yaygın bir gerçektir. Hücreleri ve içeriklerini biçimlendirmenin birçok yolu vardır. En basit yol, Tasarımcı Elektronik Tablosu oluştururken WYSIWYG ortamında Microsoft Excel kullanarak hücreleri biçimlendirmektir. Tasarımcı e-tablosu oluşturulduktan sonra, e-tablo ile kaydedilen tüm biçim ayarlarını koruyarak Aspose.Cells'i kullanarak elektronik tabloyu açabilirsiniz. Hücreleri ve içeriklerini biçimlendirmenin başka bir yolu da Aspose.Cells API'i kullanmaktır. Bu konuda, Aspose.Cells API kullanarak hücreleri ve içeriklerini biçimlendirmek için iki yaklaşım açıklayacağız.
### **biçimlendirme Cells**
 Geliştiriciler, Aspose.Cells'in esnek API'ini kullanarak hücreleri ve içeriklerini biçimlendirebilir. Aspose.Cells, bir sınıf sağlar,[Çalışma kitabı](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) , bu bir Microsoft Excel dosyasını temsil eder. bu[Çalışma kitabı](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) sınıf bir içerir[Çalışma Sayfası Koleksiyonu](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection) Bu, bir Excel dosyasındaki her çalışma sayfasına erişim sağlar. Bir çalışma sayfası şununla temsil edilir:[Çalışma kağıdı](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) sınıf. bu[Çalışma kağıdı](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) class bir Cells koleksiyonu sağlar. İçindeki her öğe[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/cells)koleksiyon bir nesneyi temsil eder**Cell** sınıf.

 Aspose.Cells şunları sağlar:[stil](https://reference.aspose.com/cells/java/com.aspose.cells/style) mülkiyet[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) sınıf, bir hücrenin biçimlendirme stilini ayarlamak için kullanılır. Ayrıca, Aspose.Cells ayrıca bir[stil](https://reference.aspose.com/cells/java/com.aspose.cells/style) Aynı amaca hizmet etmek için kullanılan sınıf. Arka plan veya ön plan renklerini, kenarlıkları, yazı tiplerini, yatay ve dikey hizalamaları, girinti düzeyini, metin yönünü, döndürme açısını ve çok daha fazlasını ayarlamak için hücrelere farklı biçimlendirme stilleri uygulayın.
#### **setStyle Yöntemini Kullanma**
 Farklı hücrelere farklı biçimlendirme stilleri uygularken setStyle yöntemini kullanmak daha iyidir.[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) sınıf. Bir hücrede çeşitli biçimlendirme ayarlarını uygulamak için setStyle yönteminin kullanımını gösteren bir örnek aşağıda verilmiştir.





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formatting-FormattingCellsUsingsetStyleMethod-1.java" >}}




#### **Stil Nesnesini Kullanma**
 Aynı biçimlendirme stilini farklı hücrelere uygularken,[stil](https://reference.aspose.com/cells/java/com.aspose.cells/style) nesne.

1.  Ekle[stil](https://reference.aspose.com/cells/java/com.aspose.cells/style) Styles koleksiyonuna nesne[Çalışma kitabı](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) Workbook sınıfının createStyle yöntemini çağırarak sınıfı.
1. Yeni eklenen Style nesnesine Styles koleksiyonundan erişin.
1. İstenen biçimlendirme ayarlarını uygulamak için Style nesnesinin istenen özelliklerini ayarlayın.
1. Yapılandırılan Style nesnesini istenen herhangi bir hücrenin Style özelliğine atayın.

Bu yaklaşım, uygulamalarınızın verimliliğini büyük ölçüde artırabilir ve bellek tasarrufu da sağlayabilir.





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FormattingCellsUsingStyleObject-FormattingCellsUsingStyleObject.java" >}}




#### **Degrade Dolgu Efektlerini Uygulama**
İstediğiniz Degrade Dolgu Efektlerini hücreye uygulamak için, buna göre Style nesnesinin setTwoColorGradient yöntemini kullanın.
#### **Kod Örneği**
 Aşağıdaki çıktı aşağıdaki kod çalıştırılarak elde edilir.

**Degrade Dolgu Efektlerini Uygulama** 

![yapılacaklar:resim_alternatif_Metin](data-formatting_1.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ApplyGradientFillEffects-ApplyGradientFillEffects.java" >}}




## **Hizalama Ayarlarını Yapılandırma**
Hücreleri biçimlendirmek için Microsoft Excel'i kullanan herkes, Microsoft Excel'deki hizalama ayarlarına aşina olacaktır.

**Microsoft Excel'deki hizalama ayarları** 

![yapılacaklar:resim_alternatif_Metin](data-formatting_2.png)

Yukarıdaki şekilde görebileceğiniz gibi, farklı hizalama seçenekleri vardır:

- [Metin hizalama](/cells/tr/java/data-formatting/) (yatay dikey)
- [Girinti](/cells/tr/java/data-formatting/).
- [Oryantasyon](/cells/tr/java/data-formatting/).
- [Metin kontrolü](/cells/tr/java/data-formatting/).
- [Metin yönü](/cells/tr/java/data-formatting/).

Bu hizalama ayarlarının tümü Aspose.Cells tarafından tam olarak desteklenmektedir ve aşağıda daha ayrıntılı olarak ele alınmıştır.
### **Hizalama Ayarlarını Yapılandırma**
 Aspose.Cells bir sınıf sağlar,[Çalışma kitabı](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) , bu bir Excel dosyasını temsil eder. Workbook sınıfı, Excel dosyasındaki her çalışma sayfasına erişim sağlayan bir WorksheetCollection içerir. Bir çalışma sayfası şununla temsil edilir:[Çalışma kağıdı](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) sınıf.

 Worksheet sınıfı bir Cells koleksiyonu sağlar. Cells koleksiyonundaki her öğe, bir nesneyi temsil eder.[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) sınıf.

Aspose.Cells, setStyle yöntemini sağlar.[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) bir hücrenin biçimlendirmesi için kullanılan sınıf. bu[stil](https://reference.aspose.com/cells/java/com.aspose.cells/style) class, yazı tipi ayarlarını yapılandırmak için yararlı özellikler sağlar.

TextAlignmentType numaralandırmasını kullanarak herhangi bir metin hizalama türünü seçin. TextAlignmentType numaralandırmasındaki önceden tanımlanmış metin hizalama türleri şunlardır:

|**Metin Hizalama Türleri**|**Tanım**|
|:- |:- |
|Alt|Alt metin hizalamasını temsil eder|
|Merkez|Merkez metin hizalamasını temsil eder|
|Merkez Boyunca|Metin hizalaması boyunca merkezi temsil eder|
|dağıtılmış|Dağıtılmış metin hizalamasını temsil eder|
|Doldurmak|Dolgu metni hizalamasını temsil eder|
|Genel|Genel metin hizalamasını temsil eder|
|Savunmak|Yaslanmış metin hizalamasını temsil eder|
|Ayrıldı|Sola metin hizalamasını temsil eder|
|Doğru|Doğru metin hizalamasını temsil eder|
|Tepe|Üst metin hizalamasını temsil eder|
{{% alert color="primary" %}} 

Justify dağıtılmış ayarını Style.setJustifyDistributed() yöntemini kullanarak da uygulayabilirsiniz.

{{% /alert %}} 
#### **Yatay hizalama**
 Kullan[stil](https://reference.aspose.com/cells/java/com.aspose.cells/style) Metni yatay olarak hizalamak için nesnenin setHorizontalAlignment yöntemi.

Aşağıdaki çıktı, aşağıdaki örnek kodu çalıştırarak elde edilir:

**Metni yatay olarak hizalama** 

![yapılacaklar:resim_alternatif_Metin](data-formatting_3.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-TextAlignmentHorizontal-TextAlignmentHorizontal.java" >}}




#### **Dikey hizalama**
 Kullan[stil](https://reference.aspose.com/cells/java/com.aspose.cells/style) Metni dikey olarak hizalamak için nesnenin setVerticalAlignment yöntemi.

VerticalAlignment merkeze ayarlandığında aşağıdaki çıktı elde edilir.

**Metni dikey olarak hizalama** 

![yapılacaklar:resim_alternatif_Metin](data-formatting_4.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-TextAlignmentVertical-TextAlignmentVertical.java" >}}




### **Girinti**
 Kullanarak bir hücredeki metnin girinti düzeyini ayarlamak mümkündür.[stil](https://reference.aspose.com/cells/java/com.aspose.cells/style) nesnenin setIndentLevel yöntemi.

IndentLevel 2 olarak ayarlandığında aşağıdaki çıktı elde edilir.

**Girinti seviyesi 2'ye ayarlandı** 

![yapılacaklar:resim_alternatif_Metin](data-formatting_5.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-Indentation-ImportingfromResultSet.java" >}}




### **Oryantasyon**
 ile bir hücredeki metnin yönünü (döndürme) ayarlayın.[stil](https://reference.aspose.com/cells/java/com.aspose.cells/style) nesnenin setRotationAngle yöntemi.

Dönme açısı 25 olarak ayarlandığında aşağıdaki çıkış elde edilir.

**Dönüş açısı 25 olarak ayarlandı** 

![yapılacaklar:resim_alternatif_Metin](data-formatting_6.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-Orientation-Orientation.java" >}}




### **Metin Kontrolü**
Aşağıdaki bölümde, metin kaydırma, sığdırmak için küçültme ve diğer biçimlendirme seçeneklerini ayarlayarak metnin nasıl kontrol edileceği anlatılmaktadır.
#### **Metni Kaydırma**
Metni bir hücreye kaydırmak okumayı kolaylaştırır: Hücrenin yüksekliği, onu kesmek veya bitişik hücrelere dökmek yerine tüm metne sığacak şekilde ayarlanır.

 ile metin kaydırmayı açık veya kapalı olarak ayarlayın.[stil](https://reference.aspose.com/cells/java/com.aspose.cells/style) nesnenin setTextWrapped yöntemi.

Metin kaydırma etkinleştirildiğinde aşağıdaki çıktı elde edilir.

**Hücrenin içine sarılmış metin** 

![yapılacaklar:resim_alternatif_Metin](data-formatting_7.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-WrapText-WrapText.java" >}}




#### **Sığdırmak İçin Küçültmek**
 Metni bir alana kaydırma seçeneği, metin boyutunu bir hücrenin boyutlarına sığacak şekilde küçültmektir. Bu ayarlanarak yapılır.[stil](https://reference.aspose.com/cells/java/com.aspose.cells/style) nesnenin IsTextWrapped özelliği**doğru**.

Metin hücreye sığacak şekilde küçültüldüğünde aşağıdaki çıktı elde edilir.

**Metin, hücrenin sınırları içine sığacak şekilde küçültüldü** 

![yapılacaklar:resim_alternatif_Metin](data-formatting_8.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ShrinkingToFit-ShrinkingToFit.java" >}}




#### **Birleştirme Cells**
Microsoft Excel gibi, Aspose.Cells de birkaç hücrenin tek hücrede birleştirilmesini destekler.

İlk satırdaki üç hücre birleştirilerek büyük bir tek hücre oluşturulursa aşağıdaki çıktı elde edilir.

**Büyük bir hücre oluşturmak için üç hücre birleştirildi** 

![yapılacaklar:resim_alternatif_Metin](data-formatting_9.png)

 Kullan[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/cells) koleksiyonun Hücreleri birleştirmek için Merge yöntemi. Merge yöntemi aşağıdaki parametreleri alır:

- İlk sıra, birleştirmeye nereden başlayacağınız ilk sıra.
- İlk sütun, birleştirmeye nereden başlayacağınız ilk sütun.
- Satır sayısı, birleştirilecek satır sayısı.
- Sütun sayısı, birleştirilecek sütun sayısı.





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-MergingCellsInWorksheet-MergingCellsInWorksheet.java" >}}




### **Metin yönü**
Hücrelerdeki metnin okuma sırasını ayarlamak mümkündür. Okuma sırası, karakterlerin, kelimelerin vb. görüntülendiği görsel sıradır. Örneğin, İngilizce soldan sağa bir dilken, Arapça sağdan sola bir dildir.

 Okuma sırası ile ayarlanır[stil](https://reference.aspose.com/cells/java/com.aspose.cells/style) nesnenin TextDirection özelliği. Aspose.Cells, TextDirectionType numaralandırmasında önceden tanımlanmış metin yönü türleri sağlar.

|**Metin Yönü Türleri**|**Tanım**|
|:- |:- |
|Bağlam|İlk girilen karakterin diliyle tutarlı okuma sırası|
|Soldan sağa|Soldan sağa okuma sırası|
|Sağdan sola|Sağdan sola okuma sırası|






{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ChangeTextDirection-ChangeTextDirection.java" >}}





Metnin okuma sırası sağdan sola doğru ayarlanırsa aşağıdaki çıktı elde edilir.

**Metin okuma sırasını sağdan sola ayarlama** 

![yapılacaklar:resim_alternatif_Metin](data-formatting_10.png)
## **Cell'de Seçili Karakterleri Biçimlendirme**
[Yazı Tipi Ayarlarıyla Başa Çıkma](/cells/tr/java/dealing-with-font-settings/)hücrelerin nasıl biçimlendirileceğini, ancak yalnızca tüm hücrelerin içeriğinin nasıl biçimlendirileceğini açıkladı. Yalnızca seçili karakterleri biçimlendirmek isterseniz ne olur?

Aspose.Cells bu özelliği destekler. Bu konuda, bu özelliğin nasıl kullanılacağı açıklanmaktadır.
### **Seçilen Karakterleri Biçimlendirme**
 Aspose.Cells bir sınıf sağlar,[Çalışma kitabı](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) , bu bir Microsoft Excel dosyasını temsil eder. Workbook sınıfı, Excel dosyasındaki her çalışma sayfasına erişim sağlayan bir Worksheets koleksiyonu içerir. Bir çalışma sayfası şununla temsil edilir:[Çalışma kağıdı](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) sınıf. Worksheet sınıfı bir Cells koleksiyonu sağlar. Cells koleksiyonundaki her öğe, bir nesneyi temsil eder.[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) sınıf.

Cell sınıfı, bir hücrede bir dizi karakter seçmek için aşağıdaki parametreleri alan karakter yöntemini sağlar:

- **Dizini başlat**, seçimin başlatılacağı karakterin dizini.
- **Karakter sayısı**, seçilecek karakter sayısı.

Çıktı dosyasında, A1" hücresinde, 'Ziyaret' sözcüğü varsayılan yazı tipiyle biçimlendirilmiştir ancak 'Aspose!' kalın ve mavidir.

**Seçilen karakterleri biçimlendirme** 

![yapılacaklar:resim_alternatif_Metin](data-formatting_11.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FormattingSelectedCharacters-FormattingSelectedCharacters.java" >}}







{{% alert color="primary" %}} 

 Eğer ilgileniyorsanız[[hücre] içindeki Zengin Metnin bir bölümünü biçimlendirme](/cells/tr/java/access-and-update-the-portions-of-rich-text-of-cell/) , Cell.getCharacters & Cell.setCharacters yöntemlerini kullanmayı düşünün. Cell.getCharacters metodu ile metnin bölümlerine ulaşılır ve sonrasında Cell.setCharacters metodu ile değişiklikler yapılabilir.**almak** yöntemi, yazı tipi adı, yazı tipi rengi, kalınlık vb. çeşitli özellikleri ayarlamak için kullanılabilecek bir FontSetting nesneleri dizisi döndürür ve**Ayarlamak** Yöntem, değişiklikleri uygulamak için kullanılabilir.

{{% /alert %}} 
## **Sayfaları Etkinleştirme ve Cell Etkinleştirme veya Çalışma Sayfasında Cells Aralık Seçme**
Bazen, birisi dosyayı Microsoft Excel'de açtığında ilk görüntülenen sayfa olması için belirli bir çalışma sayfasını etkinleştirmeniz gerekebilir. Belirli bir hücreyi, kaydırma çubukları etkin hücreye kaydırılarak açıkça görülebilecek şekilde etkinleştirmeniz de gerekebilir. Aspose.Cells yukarıda sayılan tüm görevleri yapabilecek kapasitededir.

Etkin sayfa, çalışma kitabında üzerinde çalıştığınız sayfadır. Etkin sayfanın sekmesindeki ad varsayılan olarak kalındır. Bu arada etkin hücre, siz yazmaya başladığınızda seçilen ve içine verilerin girildiği hücredir. Aynı anda yalnızca bir hücre etkindir. Aktif hücre, diğer hücrelere karşı görünmesini sağlamak için kalın bir sınırla çevrilidir. Aspose.Cells, çalışma sayfasında bir hücre aralığı seçmenize de olanak tanır.
### **Bir Sayfayı Etkinleştirme ve Cell'i Etkinleştirme**
Aspose.Cells, bu görevler için belirli bir API sağlar. Örneğin, WorksheetCollection.setActiveSheetIndex yöntemi, etkin bir sayfa ayarlamak için kullanışlıdır. Benzer şekilde, Worksheet.setActiveCell yöntemi, bir çalışma sayfasında etkin bir hücreyi ayarlamak ve almak için kullanılır.

Dosya Microsoft Excel'de açıldığında seçilen verilerin iyi bir görünümünü vermek için yatay ve dikey kaydırma çubuklarının satır ve sütun dizini konumuna kaydırılmasını istiyorsanız, Worksheet.setFirstVisibleRow ve Worksheet.setFirstVisibleColumn özelliklerini kullanın.

Aşağıdaki örnek, bir çalışma sayfasının nasıl etkinleştirileceğini ve içindeki bir hücrenin nasıl etkinleştirileceğini gösterir. Kaydırma çubukları, 2. satırı ve 2. sütunu ilk görünür satır ve sütunları yapmak için kaydırılır.

**B2 hücresini aktif hücre olarak ayarlama** 

![yapılacaklar:resim_alternatif_Metin](data-formatting_12.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-MakeCellActive-MakeCellActive.java" >}}




#### **Çalışma Sayfasında Cells Aralığı Seçme**
Aspose.Cells, Worksheet.selectRange(int startRow, int startColumn, int totalRows, int totalColumns, bool removeOthers) yöntemini sağlar. Son parametre - removeOthers - true olarak kullanıldığında, sayfadaki diğer hücre veya hücre aralığı seçimleri kaldırılır.

Aşağıdaki örnek, etkin çalışma sayfasında bir hücre aralığının nasıl seçileceğini gösterir.





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SelectRangeofCellsinWorksheet-SelectRangeofCellsinWorksheet.java" >}}







{{% alert color="primary" %}} 

Yukarıdaki tüm sınıflar ve yöntemler, Aspose.Cells lisanslı sürümünde mevcuttur.

{{% /alert %}} 
## **Satırları ve Sütunları Biçimlendirme**
Rapora bir görünüm vermek için bir elektronik tablodaki satırları ve sütunları biçimlendirmek, muhtemelen Excel uygulamasının en yaygın kullanılan özelliğidir. Aspose.Cells API'ler ayrıca, yazı tipi ve öznitelikleri, metnin hizalanması, arka plan/ön plan renkleri, kenarlıklar, sayılar ve tarih değişmezleri için görüntüleme formatı vb. . Aspose.Cells API'lerinin sağladığı diğer bir yararlı sınıf, Style nesnesinin yeniden kullanılabilirliğini sağlayan StyleFlag'dır.

Bu yazımızda satır ve sütunlara biçimlendirme uygulamak için Aspose.Cells for Java API nasıl kullanılacağını açıklamaya çalışacağız.
### **Satırları ve Sütunları Biçimlendirme**
 Aspose.Cells bir sınıf sağlar,[Çalışma kitabı](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) bu bir Microsoft Excel dosyasını temsil eder. bu[Çalışma kitabı](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) sınıfı, Excel dosyasındaki her çalışma sayfasına erişim sağlayan bir WorksheetCollection içerir. Bir çalışma sayfası, Worksheet sınıfı tarafından temsil edilir. bu[Çalışma kağıdı](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) class Cells koleksiyonunu sağlar. Cells koleksiyonu bir Rows koleksiyonu sağlar.
#### **Satır Biçimlendirme**
Rows koleksiyonundaki her öğe bir Row nesnesini temsil eder. Row nesnesi, bir satıra biçimlendirme uygulamak için kullanılan ApplyStyle yöntemini sunar.

Aynı biçimlendirmeyi bir satıra uygulamak için Style nesnesini kullanın:

1. CreateStyle yöntemini çağırarak Workbook sınıfına bir Style nesnesi ekleyin.
1. Biçimlendirme ayarlarını uygulamak için Stil nesnesi özelliklerini ayarlayın.
1. Yapılandırılan Style nesnesini bir Row nesnesinin ApplyStyle yöntemine atayın.





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FormattingARow-FormattingARow.java" >}}




#### **Bir Sütunu Biçimlendirme**
Cells koleksiyonu, bir Sütun koleksiyonu sağlar. Columns koleksiyonundaki her öğe bir Column nesnesini temsil eder. Row nesnesine benzer şekilde Column nesnesi, sütun biçimlendirmesini ayarlamak için kullanılan ApplyStyle yöntemini sunar. Bir sütunu satırla aynı şekilde biçimlendirmek için Column nesnesinin ApplyStyle yöntemini kullanın.





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FormattingAColumn-FormattingAColumn.java" >}}




#### **Satırlar ve Sütunlar İçin Sayıların ve Tarihlerin Görüntüleme Biçimini Ayarlama**
Gereksinim, tam bir satır veya sütun için sayıların ve tarihlerin görüntülenme biçimini ayarlamaksa, süreç aşağı yukarı yukarıda tartışılanla aynıdır, ancak metin içerikleri için parametreler ayarlamak yerine, sayılar için biçimlendirmeyi ayarlıyor olacaksınız. ve Style.Number veya Style.Custom kullanarak tarihler. Lütfen, Style.Number özelliğinin tamsayı türünde olduğunu ve yerleşik sayı ve tarih biçimlerine atıfta bulunduğunu, oysa Style.Custom özelliğinin dize türünde olduğunu ve geçerli kalıpları kabul ettiğini unutmayın.





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SettingDisplayFormat-SettingDisplayFormat.java" >}}







{{% alert color="primary" %}} 

 Lütfen adresindeki ayrıntılı makaleyi kontrol edin.[Sayıların ve [Tarihlerin] Görüntü Biçimlerini Ayarlama](/cells/tr/java/data-formatting/).

{{% /alert %}}
