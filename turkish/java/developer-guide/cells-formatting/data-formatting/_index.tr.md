---
title: Veri Biçimlendirme
type: docs
weight: 80
url: /tr/java/data-formatting/
---

## **Hücre Verilerini Biçimlendirme Yaklaşımları**
Çalışma sayfası hücreleri uygun şekilde biçimlendirildiğinde, hücre içeriğini okuyan kullanıcılar için işlerin daha kolay hale geldiği yaygın bir gerçektir. Hücreleri ve içeriklerini biçimlendirmenin birçok yolu vardır. En basit yol, bir Tasarımcı Elektronik Tablo oluştururken Microsoft Excel'i kullanarak hücreleri biçimlendirmektir. Tasarımcı elektronik tablo oluşturulduktan sonra Aspose.Cells kullanarak bu elektronik tabloyu açabilir ve tüm biçim ayarlarını kaydedebilirsiniz. Hücreleri ve içeriklerini biçimlendirmenin diğer bir yolu ise Aspose.Cells API'sini kullanmaktır. Bu konuda, Aspose.Cells API'nin kullanımıyla hücreleri ve içeriklerini biçimlendirmenin iki yaklaşımını açıklayacağız.
### **Hücreleri Biçimlendirme**
Geliştiriciler, Aspose.Cells'in esnek API'sini kullanarak hücreleri ve içeriklerini biçimlendirebilir. Aspose.Cells, bir Microsoft Excel dosyasını temsil eden [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) sınıfını sağlar. [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) sınıfı, bir Excel dosyasındaki her çalışma sayfasına erişim sağlayan [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection)'ı içerir. Bir çalışma sayfası, [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) sınıfı tarafından temsil edilir. [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) sınıfı bir Hücreler koleksiyonu sağlar. [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/cells) koleksiyonundaki her öğe, **Cell** sınıfının bir nesnesini temsil eder.

Aspose.Cells, [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) sınıfında, bir hücrenin biçimlendirme stili ayarlamak için kullanılan [Style](https://reference.aspose.com/cells/java/com.aspose.cells/style) özelliğini sağlar. Ayrıca, aynı amaca hizmet eden bir [Style](https://reference.aspose.com/cells/java/com.aspose.cells/style) sınıfı da sağlar. Hücrelere farklı türde biçimlendirme stilleri uygulayarak arka plan veya ön plan renklerini, kenarlıkları, yazı tiplerini, yatay ve dikey hizalamaları, girinti seviyesini, metin yönünü, döndürme açısını ve çok daha fazlasını ayarlayabilirsiniz.
#### **setStyle Yöntemi Kullanma**
Farklı hücrelere farklı biçimlendirme stilleri uygularken, [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) sınıfının setStyle yöntemini kullanmak daha iyidir. Aşağıda, bir hücreye çeşitli biçimlendirme ayarları uygulamak için setStyle yönteminin nasıl kullanılacağını gösteren bir örnek verilmiştir.





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formatting-FormattingCellsUsingsetStyleMethod-1.java" >}}




#### **Stil Nesnesi Kullanma**
Aynı biçimlendirme stiline farklı hücrelere uygularken, [Style](https://reference.aspose.com/cells/java/com.aspose.cells/style) nesnesini kullanın.

1. [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) sınıfının Styles koleksiyonuna, Workbook sınıfının createStyle metodunu çağırarak [Style](https://reference.aspose.com/cells/java/com.aspose.cells/style) nesnesi ekleyin.
1. Styles koleksiyonundan yeni eklenen Style nesnesine erişin.
1. Style nesnesinin istenen özelliklerini ayarlayarak istenen biçimlendirme ayarlarını uygulayın.
1. Konfigure edilmiş Style nesnesini istenen hücrenin Style özelliğine atayın.

Bu yaklaşım uygulamalarınızın verimliliğini büyük ölçüde artırabilir ve aynı zamanda bellek tasarrufu sağlayabilir.





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FormattingCellsUsingStyleObject-FormattingCellsUsingStyleObject.java" >}}




#### **Gradyan Dolgu Efektleri Uygulama**
Hücreye istenen Gradyan Dolgu Efektlerini uygulamak için, Style nesnesinin setTwoColorGradient metodu uygun şekilde kullanılır.
#### **Kod Örneği**
Aşağıdaki çıktı, aşağıdaki kodu çalıştırarak elde edilir. 

**Gradyan Dolgu Efektlerinin Uygulanması** 

![todo:image_alt_text](data-formatting_1.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ApplyGradientFillEffects-ApplyGradientFillEffects.java" >}}




## **Hizalama Ayarlarının Yapılandırılması**
Hücreleri biçimlendirmek için Microsoft Excel kullanan herkes, Microsoft Excel'deki hizalama ayarlarına aşinadır.

**Microsoft Excel'deki Hizalama Ayarları** 

![todo:image_alt_text](data-formatting_2.png)

Yukarıdaki şekilden görebileceğiniz gibi, farklı türde hizalama seçenekleri bulunmaktadır:

- [Metin hizalama](/cells/tr/java/data-formatting/) (yatay & dikey)
- [Girinti](/cells/tr/java/data-formatting/)
- [Yönlendirme](/cells/tr/java/data-formatting/)
- [Metin kontrolü](/cells/tr/java/data-formatting/)
- [Metin yönü](/cells/tr/java/data-formatting/)

Bu tüm hizalama ayarları, Aspose.Cells tarafından tamamen desteklenir ve aşağıda daha detaylı olarak tartışılmaktadır.
### **Hizalama Ayarlarının Yapılandırılması**
Aspose.Cells, bir Excel dosyasını temsil eden [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) adında bir sınıf sağlar. Workbook sınıfı, Excel dosyasındaki her bir çalışma sayfasına erişime izin veren bir WorksheetCollection'a sahiptir. Bir çalışma sayfası, [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) sınıfı tarafından temsil edilir.

Worksheet sınıfı bir Cells koleksiyonu sağlar. Cells koleksiyonundaki her öğe, [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) sınıfının bir nesnesini temsil eder.

Aspose.Cells, [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) sınıfındaki setStyle metodu sağlar. Bu metot, bir hücrenin biçimlendirilmesi için kullanılır. [Style](https://reference.aspose.com/cells/java/com.aspose.cells/style) sınıfı, yazı tiplerini yapılandırmak için kullanışlı özellikler sağlar.

MetinAlignmentType numaralandırmasını kullanarak herhangi bir metin hizalama türünü seçin. MetinAlignmentType numaralandırmasındaki önceden tanımlanmış metin hizalama tipleri şunlardır:

|**Metin Hizalama Türleri**|**Açıklama**|
| :- | :- |
|Bottom|, alt metin hizalamasını temsil eder
|Center|, merkez metin hizalamasını temsil eder
|CenterAcross|, metin hizalamasını çapraz merkezlemeyi temsil eder
|Distributed|, dağıtılmış metin hizalamasını temsil eder
|Fill|, doldurma metin hizalamasını temsil eder
|General|, genel metin hizalamasını temsil eder
|Justify|, düzgün metin hizalamasını temsil eder
|Left|, sol metin hizalamasını temsil eder
|Right|, sağ metin hizalamasını temsil eder
|Top|, üst metin hizalamasını temsil eder
{{% alert color="primary" %}} 

Style.setJustifyDistributed() yöntemini kullanarak dağıtılmış hizalamayı da uygulayabilirsiniz.

{{% /alert %}} 
#### **Yatay Hizalama**
Metni yatay olarak hizalamak için [Style](https://reference.aspose.com/cells/java/com.aspose.cells/style) nesnesinin setHorizontalAlignment yöntemini kullanın.

Aşağıdaki çıktı, aşağıdaki örnek kodu çalıştırarak elde edilir:

**Metni yatay olarak hizalamak** 

![todo:image_alt_text](data-formatting_3.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-TextAlignmentHorizontal-TextAlignmentHorizontal.java" >}}




#### **Dikey Hizalama**
Metni dikey olarak hizalamak için [Style](https://reference.aspose.com/cells/java/com.aspose.cells/style) nesnesinin setVerticalAlignment yöntemini kullanın.

Dikey Hizalama merkeze ayarlandığında aşağıdaki çıktı elde edilir.

**Metni dikey olarak hizalamak** 

![todo:image_alt_text](data-formatting_4.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-TextAlignmentVertical-TextAlignmentVertical.java" >}}




### **Girinti**
Hücredeki metnin girinti düzeyini ayarlamak için [Style](https://reference.aspose.com/cells/java/com.aspose.cells/style) nesnesinin setIndentLevel yöntemini kullanabilirsiniz.

Girinti Düzeyi 2 olarak ayarlandığında aşağıdaki çıktı elde edilir.

**Girinti düzeyi 2'ye ayarlandı** 

![todo:image_alt_text](data-formatting_5.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-Indentation-ImportingfromResultSet.java" >}}




### **Yönlendirme**
Hücredeki metnin yönlendirmesini (dönüş) [Style](https://reference.aspose.com/cells/java/com.aspose.cells/style) nesnesinin setRotationAngle yöntemiyle ayarlayın.

Yönlendirme açısı 25'e ayarlandığında aşağıdaki çıktı elde edilir.

**Yönlendirme açısı 25'e ayarlandı** 

![todo:image_alt_text](data-formatting_6.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-Orientation-Orientation.java" >}}




### **Metin Kontrolü**
Aşağıdaki bölüm metin kaydırma, sığdırmayı daraltma ve diğer biçimlendirme seçeneklerini ayarlayarak metni nasıl kontrol edeceğinizi tartışmaktadır.
#### **Metni Kaydırma**
Bir hücrede metni sarmak, metni okumayı kolaylaştırır: hücrenin yüksekliği, metnin tümünü sığdırmak için ayarlanır, onu kesmez veya bitişik hücrelere taşmaz.

[Style](https://reference.aspose.com/cells/java/com.aspose.cells/style) nesnesinin setTextWrapped yöntemiyle metni sarmayı açın veya kapatın.

Metni sarma etkinleştirildiğinde aşağıdaki çıktı elde edilir.

**Hücre içindeki metin** 

![todo:image_alt_text](data-formatting_7.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-WrapText-WrapText.java" >}}




#### **Sığdırmayı Daraltma**
Bir alanı sarmak için bir seçenek, hücre boyutlarına sığdırmak için metin boyutunu küçültmektir. Bunun için [Stil](https://reference.aspose.com/cells/java/com.aspose.cells/style) nesnesinin IsTextWrapped özelliği **true** olarak ayarlanır.

Metin hücreye sığdırılmak için aşağıdaki çıktıya ulaşılır.

**Hücre sınırları içine sığdırılmış metin** 

![todo:image_alt_text](data-formatting_8.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ShrinkingToFit-ShrinkingToFit.java" >}}




#### **Hücreleri Birleştirme**
Microsoft Excel gibi, Aspose.Cells birçok hücreyi bir araya getirerek tek bir hücre oluşturmayı destekler.

İlk satırdaki üç hücrenin birleştirilmesiyle büyük tek bir hücre oluşturulursa aşağıdaki çıktı elde edilir.

**Büyük bir hücre oluşturmak için üç hücre birleştirildi** 

![todo:image_alt_text](data-formatting_9.png)

Hücreleri birleştirmek için [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/cells) koleksiyonunun Merge yöntemini kullanın. Birleştirme yöntemi aşağıdaki parametreleri alır:

- İlk satır, birleştirmeye başlamak için ilk satır.
- İlk sütun, birleştirmeye başlamak için ilk sütun.
- Satır sayısı, birleştirilecek satır sayısı.
- Sütun sayısı, birleştirilecek sütun sayısı.





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-MergingCellsInWorksheet-MergingCellsInWorksheet.java" >}}




### **Metin Yönü**
Hücrelerde metnin okuma sırasını ayarlamak mümkündür. Okuma sırası, karakterlerin, kelimelerin vb. gösterildiği görsel sıradır. Örneğin, İngilizce soldan sağa bir dil iken Arapça sağdan sola bir dildir.

Okuma sırası [Style](https://reference.aspose.com/cells/java/com.aspose.cells/style) nesnesinin TextDirection özelliği ile ayarlanır. Aspose.Cells, TextDirectionType numaralandırmasında önceden tanımlanmış metin yönü tiplerini sağlar.

|**Metin Yönü Türleri**|**Açıklama**|
| :- | :- |
|Context|Girilen ilk karakterin diline uygun okuma sırası|
|LeftToRight|Soldan sağa okuma sırası|
|RightToLeft|Sağdan sola okuma sırası|






{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ChangeTextDirection-ChangeTextDirection.java" >}}





Metnin okuma sırası sağdan sola olarak ayarlandığında aşağıdaki çıktı elde edilir.

**Metin okuma sırası sağdan sola ayarlanıyor** 

![todo:image_alt_text](data-formatting_10.png)
## **Hücredeki Seçili Karakterleri Biçimlendirme**
[Yazı Tipi Ayarlarıyla İlgilenme](/cells/tr/java/dealing-with-font-settings/) sadece hücreleri nasıl biçimlendireceğini açıklar, ancak yalnızca seçili karakterleri biçimlendirmek istersen ne yapacaksın?

Aspose.Cells bu özelliği destekler. Bu konu bu özelliği nasıl kullanacağınızı açıklar.
### **Seçili Karakterleri Biçimlendirme**
Aspose.Cells, bir Microsoft Excel dosyasını temsil eden [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) adlı bir sınıf sağlar. Workbook sınıfı, Excel dosyasındaki her çalışma sayfasına erişim sağlayan Worksheets koleksiyonunu içerir. Bir çalışma sayfası [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) sınıfı tarafından temsil edilir. Worksheet sınıfı bir Cells koleksiyonu sağlar. Hücreler koleksiyonundaki her bir öğe, [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) sınıfının bir nesnesini temsil eder.

Cell sınıfı, bir hücredeki karakterleri seçmek için aşağıdaki parametreleri alan characters yöntemi sağlar:

- **Başlangıç Dizini**, seçimin başlayacağı karakterin dizini.
- **Karakter Sayısı**, seçilecek karakterlerin sayısı.

Çıktı dosyasında, A1 hücresindeki 'Visit' kelimesi varsayılan yazı tipi ile biçimlendirilir ancak 'Aspose!' kalın ve mavi renklidir.

**Seçili karakterleri biçimlendirme** 

![todo:image_alt_text](data-formatting_11.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FormattingSelectedCharacters-FormattingSelectedCharacters.java" >}}







{{% alert color="primary" %}} 

Eğer [hücre](/hücreler/tr/java/hücrenin-bölümlerini-erişme-ve-güncelleme/) içerisindeki Zengin Metin'in bir kısmını biçimlendirmek istiyorsanız, Cell.getCharacters & Cell.setCharacters yöntemlerini kullanmayı düşünebilirsiniz. Cell.getCharacters yöntemi, metnin parçalarını erişmek için kullanılır ve ardından değişiklikler, Cell.setCharacters yöntemi kullanılarak yapılabilirken **get** yöntemi, yazı tipi adı, yazı tipi rengi, kalınlık vb. gibi çeşitli özellikleri ayarlamak için manipüle edilebilen FontSetting nesnelerinin bir dizisini döndürür ve **set** yöntemi, değişiklikleri uygulamak için kullanılabilir.

{{% /alert %}} 
## **Çalışma Kitabını Etkinleştirme ve Çalışma Sayfasındaki Etkin Bir Hücreyi veya Hücre Aralığını Seçme**
Bazen, bir dosyayı Microsoft Excel'de birisi açtığında ilk olarak görünen sayfanın belirli bir çalışma sayfası olmasını isteyebilirsiniz. Ayrıca, belirli bir hücreyi etkinleştirmeniz ve bu hücreye girilmeye başlandığında kaydırma çubuklarının etkin hücreye kaydırılmasını isteyebilirsiniz. Aspose.Cells, yukarıda bahsedilen tüm görevleri yapabilir.

Etkin bir sayfa, bir çalışma kitabı içinde çalıştığınız sayfadır. Etkin sayfanın sekmesindeki adı varsayılan olarak kalındır. Etkin hücre ise seçili olan ve veri girilmeye başlandığında içine veri girilen hücredir. Aynı anda yalnızca bir hücre etkindir. Etkin hücre, diğer hücrelere karşı açıkça görünmesi için kalın bir kenarlıkla çevrilmiştir. Aspose.Cells ayrıca çalışma sayfasındaki bir hücre aralığını seçmenize de olanak tanır.
### **Bir Sayfayı Etkinleştirme ve Bir Hücreyi Etkin Hale Getirme**
Aspose.Cells, bu görevler için belirli bir API sağlar. Örneğin, WorksheetCollection.setActiveSheetIndex yöntemi, etkin bir sayfa ayarlamak için kullanışlıdır. Benzer şekilde, Worksheet.setActiveCell yöntemi bir çalışma sayfasındaki etkin hücreyi ayarlamak ve almak için kullanılır.

Dosya Microsoft Excel'de açıldığında yatay ve dikey kaydırma çubuklarının seçilen veriyi güzel bir görüntü sağlamak için satır ve sütun dizin konumuna kaydırılmasını istiyorsanız, Worksheet.setFirstVisibleRow ve Worksheet.setFirstVisibleColumn özelliklerini kullanın.

Aşağıdaki örnek, bir çalışma sayfasını etkinleştirme ve içindeki bir hücreyi etkin hale getirme şeklini gösterir. Kaydırma çubukları, 2. satırı ve 2. sütunu ilk görünür satır ve sütun olarak kaydırılmıştır.

**B2 hücresini etkin hücre olarak ayarlama** 

![todo:image_alt_text](data-formatting_12.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-MakeCellActive-MakeCellActive.java" >}}




#### **Çalışma Sayfasında Bir Hücre Aralığı Seçme**
Aspose.Cells, int startRow, int startColumn, int totalRows, int totalColumns, bool removeOthers parametrelerini kullanan Worksheet.selectRange(int startRow, int startColumn, int totalRows, int totalColumns, bool removeOthers) yöntemini sağlar. removeOthers parametresini true olarak kullanarak, çalışma sayfasındaki diğer hücre ya da hücre aralığı seçimleri kaldırılır.

Aşağıdaki örnek, etkin çalışma sayfasında bir hücre aralığı seçme şeklini gösterir.





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SelectRangeofCellsinWorksheet-SelectRangeofCellsinWorksheet.java" >}}







{{% alert color="primary" %}} 

Yukarıdaki tüm sınıflar ve yöntemler, Aspose.Cells'in lisanslı sürümü ile kullanılabilir.

{{% /alert %}} 
## **Satır ve Sütunların Biçimlendirilmesi**
Raporun görünümünü sağlamak için elektronik tablo içindeki satır ve sütunları biçimlendirmek, Excel uygulamasının muhtemelen en yaygın kullanılan özelliklerindendir. Aspose.Cells API'leri de veri modeli aracılığıyla bu işlevselliği sunar ve özellikle yazı tipi ve özellikleri, metnin hizalaması, arka plan/önrenkleri, kenarlıkları, sayıların ve tarihsel dizelerin görüntü biçimlendirmesini ele alan Style sınıfını açığa çıkarır. Aspose.Cells API'lerinin sağladığı diğer faydalı bir sınıf ise StyleFlag'dir ve Style nesnesinin tekrar kullanılmasını sağlar. 

Bu makalede, satır ve sütunlara biçimlendirme uygulamak için Aspose.Cells for Java API'sını nasıl kullanacağımızı açıklamaya çalışacağız. 
### **Satırları ve Sütunları Biçimlendirme**
Aspose.Cells, bir Microsoft Excel dosyasını temsil eden [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) sınıfını sağlar. [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) sınıfı, Excel dosyasındaki her çalışma sayfasına erişim sağlayan bir WorksheetCollection içerir. Bir çalışma sayfası, Worksheet sınıfı tarafından temsil edilir. [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) sınıfı, Cells koleksiyonunu sağlar. Cells koleksiyonu, Row koleksiyonunu sağlar.
#### **Bir Satırı Biçimlendirme**
Row koleksiyonundaki her öğe, bir Satır nesnesini temsil eder. Satır nesnesi, bir satıra biçimlendirme uygulamak için kullanılan applyStyle yöntemini sunar.

Aynı biçimlendirmeyi bir satıra uygulamak için Style objesini kullanın:

1. createStyle yöntemini çağırarak Style objesini Workbook sınıfına ekleyin.
1. Biçimlendirme ayarlarını uygulamak için Style objesi özelliklerini ayarlayın.
1. Yapılandırılmış Style objesini Satır nesnesinin applyStyle yöntemine atayın.





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FormattingARow-FormattingARow.java" >}}




#### **Bir Sütunu Biçimlendirme**
Cells koleksiyonu, Columns koleksiyonunu sağlar. Columns koleksiyonundaki her öğe, bir Sütun nesnesini temsil eder. Satır nesnesi gibi, Sütun nesnesi de sütun biçimlendirmesi yapmak için applyStyle yöntemini sunar. Sütun nesnesinin applyStyle yöntemini kullanarak bir sütunu satır biçimleriyle aynı şekilde biçimlendirebilirsiniz.





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FormattingAColumn-FormattingAColumn.java" >}}




#### **Satırlar ve Sütunlar için Sayı ve Tarihlerin Görüntü Biçimini Ayarlama**
Eğer tam bir satır veya sütunun ekran biçimini sayı ve tarihler için ayarlamanız gerekiyorsa, süreç yukarıda tartışıldığı gibi daha veya daha az aynıdır, ancak metin içeriği için parametreleri ayarlamak yerine, Style.Number veya Style.Custom'ı kullanarak sayılar ve tarihler için biçimlendirme ayarlayacaksınız. Lütfen dikkat edin, Style.Number özelliği tamsayı türündedir ve yerleşik sayı ve tarih biçimlerine işaret ederken, Style.Custom özelliği dize türündedir ve geçerli desenleri kabul eder.





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SettingDisplayFormat-SettingDisplayFormat.java" >}}







{{% alert color="primary" %}} 

[Sayıların ve [Tarihlerin Gösterim Biçimlerinin Ayarlanması](/cells/tr/java/data-formatting/) hakkında detaylı makaleyi kontrol edin.

{{% /alert %}}
