---
title: Hücre Biçimleri
type: docs
weight: 100
url: /tr/java/cells-formatting/
---

## **Hücrelere Kenarlık Eklemek**
Microsoft Excel, kullanıcılara hücreleri sınırlar ekleyerek biçimlendirme olanağı sağlar.

**Microsoft Excel'de Sınırlar Ayarları** 

![todo:image_alt_text](cells-formatting_1.png)

Sınırın türü, eklenen konuma bağlıdır. Örneğin, bir üst sınır, bir hücrenin üst konumuna eklenendir. Kullanıcılar ayrıca sınırların çizgi stilini ve rengini değiştirebilir.

Aspose.Cells ile geliştiriciler, Microsoft Excel'de olduğu gibi sınırlar ekleyebilir ve bunları esnek bir şekilde özelleştirebilirler.
### **Hücrelere Kenarlık Eklemek**
Aspose.Cells, bir Microsoft Excel dosyasını temsil eden [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) sınıfını sağlar. [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) sınıfı, Excel dosyasındaki her çalışma sayfasına erişim sağlayan bir [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) içerir. Bir çalışma sayfası, [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) sınıfı ile temsil edilir. [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) sınıfı, [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) koleksiyonunu sağlar. [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) koleksiyonundaki her öğe, [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/Cell) sınıfının bir nesnesini temsil eder.

Aspose.Cells, hücrenin biçimlendirme stilini ayarlamak için [setStyle](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setStyle-com.aspose.cells.Style-) yöntemini içeren [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) sınıfını sağlar. Ayrıca, [Style](https://reference.aspose.com/cells/java/com.aspose.cells/Style) sınıfının nesnesi kullanılır ve yazı tipi ayarlarını yapılandırmak için özellikler sağlar.
#### **Bir Hücreye Sınır Ekleme**
Bir hücreye kenarlık eklemek için [Style](https://reference.aspose.com/cells/java/com.aspose.cells/Style) nesnesinin [setBorder](https://reference.aspose.com/cells/java/com.aspose.cells/style#setBorder-int-int-com.aspose.cells.Color-) metodunu kullanın. Kenarlık tipi parametre olarak geçirilir. Tüm kenarlık türleri, [BorderType](https://reference.aspose.com/cells/java/com.aspose.cells/BorderType) enum'ında önceden tanımlıdır.

|**Sınır Türleri**|**Açıklama**|
| :- | :- |
|[BOTTOM_BORDER](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#BOTTOM-BORDER)|En alt sınır çizgisi|
|[DIAGONAL_DOWN](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#DIAGONAL-DOWN)|Sol üstten sağ alta çapraz çizgi|
|[DIAGONAL_UP](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#DIAGONAL-UP)|Sol alttan sağ üste çapraz çizgi|
|[LEFT_BORDER](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#LEFT-BORDER)|Sol sınır çizgisi|
|[RIGHT_BORDER](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#RIGHT-BORDER)|Sağ sınır çizgisi|
|[TOP_BORDER](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#TOP-BORDER)|Üst sınır çizgisi|
|[HORIZONTAL](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#HORIZONTAL)| Yalnızca dinamik stile, koşullu biçimlendirmeye benzer bir özellik. |
|[VERTICAL](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#VERTICAL)| Yalnızca dinamik stile, koşullu biçimlendirmeye benzer bir özellik. |
Çizgi rengini ayarlamak için, [Color](https://reference.aspose.com/cells/java/com.aspose.cells/Color) enum'undan renk seçin ve bunu [Style](https://reference.aspose.com/cells/java/com.aspose.cells/Style) nesnesinin [setBorder](https://reference.aspose.com/cells/java/com.aspose.cells/style#setBorder-int-int-com.aspose.cells.Color-) metodunun Color parametresine iletin. Çizgi stilleri, [CellBorderType](https://reference.aspose.com/cells/java/com.aspose.cells/CellBorderType) enum'unda önceden tanımlıdır.

|**Çizgi Stilleri**|**Açıklama**|
| :- | :- |
|[DASH_DOT](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#DASH-DOT)|İnce çizgi- Noktalı çizgiyi temsil eder|
|[DASH_DOT_DOT](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#DASH-DOT_DOT)|İnce çizgi- Nokta- noktalı çizgi temsil eder|
|[DASHED](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#DASHED)|Kesikli çizgiyi temsil eder
|[DOTTED](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#DOTTED)|Noktalı çizgiyi temsil eder
|[DOUBLE](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#DOUBLE)|Çift çizgiyi temsil eder
|[HAIR](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#HAIR)|Saç çizgiyi temsil eder
|[MEDIUM_DASH_DOT](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#MEDIUM-DASH-DOT)|Orta kalınlıkta noktalı çizgi temsil eder|
|[ORTA_CIZGİ_DOT_DOT](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#MEDIUM-DASH-DOT_DOT)|Orta çizgi noktaları çizgisi temsil eder|
|[ORTA_CIZGI](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#MEDIUM-DASHED)|Orta çizgili çizgi temsil eder|
|[NONE](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#NONE)|Herhangi bir çizgiyi temsil etmez
|[MEDIUM](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#MEDIUM)|Orta çizgiyi temsil eder|
|[EĞİK_CIZGI_NOKTASI](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#SLANTED-DASH-DOT)|Eğik orta çizgi noktaları çizgisi temsil eder|
|[THICK](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#THICK)|Kalın çizgiyi temsil eder|
|[THIN](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#THIN)|İnce çizgiyi temsil eder|
Yukarıdaki çizgi stillerinden birini seçin ve ardından onu [Style](https://reference.aspose.com/cells/java/com.aspose.cells/Style) nesnesinin [setBorder](https://reference.aspose.com/cells/java/com.aspose.cells/style#setBorder-int-int-com.aspose.cells.Color-) yöntemine atayın.

Aşağıdaki çıktı, aşağıdaki kodu çalıştırırken üretilir.

**Bir hücrenin tüm kenarlarına uygulanan sınırlar** 

![todo:image_alt_text](cells-formatting_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AddingBordersToCells-AddingBordersToCells.java" >}}
#### **Hücre Aralığına Sınırlar Ekleme**
Bir hücre yerine sadece bir hücre aralığına sınır eklemek mümkündür. Öncelikle, [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) topluluğunu [createRange](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange-int-int-boolean-) metodunu çağırarak bir hücre aralığı oluşturun, bu metod aşağıdaki parametreleri alır:

- **İlk Satır**, aralığın ilk satırı.
- **İlk Sütun**, aralığın ilk sütunu.
- **Satır Sayısı**, aralıktaki satır sayısı.
- **Sütun Sayısı**, aralıktaki sütun sayısı.

[createRange](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange-int-int-boolean-) metodu belirtilen aralığı içeren bir [Range](https://reference.aspose.com/cells/java/com.aspose.cells/Range) nesnesi döndürür. [Range](https://reference.aspose.com/cells/java/com.aspose.cells/Range) nesnesi, aşağıdaki parametreleri alan bir [setOutlineBorders](https://reference.aspose.com/cells/java/com.aspose.cells/range#setOutlineBorders-int-com.aspose.cells.Color-) yöntemi sağlar:

- **CellBorderType**, seçilen kenar çizgisi stili, [CellBorderType](https://reference.aspose.com/cells/java/com.aspose.cells/CellBorderType) numaralandırmasından seçilmiştir.
- **Color**, seçilen kenar çizgisi rengi, [Color](https://reference.aspose.com/cells/java/com.aspose.cells/Color) numaralandırmasından seçilmiştir.

Aşağıdaki çıktı, aşağıdaki kodu çalıştırırken üretilir.

**Hücre aralığına uygulanan sınırlar** 

![todo:image_alt_text](cells-formatting_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AddingBorderstoRange-AddingBorderstoRange.java" >}}
## **Renkler ve Palet**
Bir palet, bir görüntü oluşturmak için kullanılabilen renk sayısıdır. Bir sunumda standart bir palet kullanımı, kullanıcının tutarlı bir görünüm oluşturmasına olanak tanır. Her Microsoft Excel (97-2003) dosyasının bir hücrelere, fontlara, ızgaralara, grafik nesnelerine, doldurmalara ve çizgilere uygulanabilen 56 renklik bir paleti vardır.

**Microsoft Excel'de Palet Ayarları** 

![todo:image_alt_text](cells-formatting_4.png)

Aspose.Cells ile sadece mevcut renkleri değil, özel renkleri de kullanmak mümkündür. Özel bir rengi kullanmadan önce, onu paletinize ekleyin. Bu konu, paletinize özel renkler eklemenin nasıl yapıldığını açıklar.
### **Paletine Özel Renkler Eklemek**
Aspose.Cells ayrıca 56 renklik bir paleti destekler. Standart renk paleti yukarıda gösterilmiştir. Paletinizde tanımlanmamış bir özel rengi kullanmak istiyorsanız, o rengi kullanmadan önce paletinize eklemeniz gerekir.

{{% alert color="primary" %}} 

Palet sadece 56 rengi saklar. Özel bir rengi paletinize eklediğinizde, palet değişir ve dosyadaki önceki renk ile biçimlendirilmiş her öğe değişir. Bu nedenle, paleti değiştirirken çok dikkatli olun. Ayrıca, bu yalnızca XLS (Excel 97 - 2003) dosya biçiminde bir sınırlamadır, XLSX veya diğer gelişmiş MS Excel (2007/2010) dosya biçimleri için böyle bir sınırlama yoktur.

{{% /alert %}} 

Aspose.Cells, Bir Microsoft Excel dosyasını temsil eden [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) sınıfını sağlar. Bu sınıf, aşağıdaki parametreleri alan ve paleti değiştirmek için kullanılan [changePalette](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#changePalette-com.aspose.cells.Color-int-) yöntemini sağlar:

- **Özel renk**, paletle değiştirilecek özel renk.
- **İndeks**, özel renkle değiştirilecek olan rengin indeksi. 0-55 arasında olmalıdır.

Aşağıdaki örnek, fonta uygulamadan önce özel bir rengi paletine ekler.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ColorsAndPalette-ColorsAndPalette.java" >}}
## **Renkler ve Arka Plan Desenleri**
Microsoft Excel hücrelerin ön plan (kontur) ve arka plan (dolgu) renklerini ve aşağıda gösterildiği gibi arka plan desenlerini ayarlayabilir.

**Microsoft Excel'de Renkler ve Arka Plan Desenlerinin Ayarlanması** 

![todo:image_alt_text](cells-formatting_5.png)

Aspose.Cells, bu özellikleri esnek bir şekilde destekler. Bu konuda, Aspose.Cells kullanarak bu özellikleri nasıl kullanacağımızı öğreneceğiz.
### **Renklerin ve Arka Plan Desenlerinin Ayarlanması**
Aspose.Cells, bir Microsoft Excel dosyasını temsil eden bir sınıf olan [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) sağlar. [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) sınıfı, Excel dosyasındaki her çalışma sayfasına erişim sağlayan [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) içerir. Bir çalışma sayfası, [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) sınıfı tarafından temsil edilir. [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) sınıfı bir [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) koleksiyonu sağlar. [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) koleksiyonundaki her öğe, [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) sınıfının bir öğesini temsil eder.

Aspose.Cells, hücrenin biçimlendirmesini ayarlamak için kullanılan [setStyle](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setStyle-com.aspose.cells.Style-) yöntemini sağlayan [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) sınıfında mevcuttur. Ayrıca, [Style](https://reference.aspose.com/cells/java/com.aspose.cells/Style) sınıfının nesnesi, yazı tipi ayarlarını yapılandırmak için kullanılabilir.

{{% alert color="primary" %}} 

Bir hücrenin ön veya arka plan rengini ayarlamak için, [Style](https://reference.aspose.com/cells/java/com.aspose.cells/Style) nesnesinin [setBackgroundColor](https://reference.aspose.com/cells/java/com.aspose.cells/style#BackgroundColor) veya [setForegroundColor](https://reference.aspose.com/cells/java/com.aspose.cells/style#ForegroundColor) özelliklerini kullanın. Bu özellikler, [Style](https://reference.aspose.com/cells/java/com.aspose.cells/Style) nesnesinin [setPattern](https://reference.aspose.com/cells/java/com.aspose.cells/style#Pattern) özelliği yapılandırılmışsa yalnızca etki yapar.

{{% /alert %}} 

[setForegroundColor](https://reference.aspose.com/cells/java/com.aspose.cells/style#ForegroundColor) özelliği hücrenin gölge rengini ayarlar.

[setPattern](https://reference.aspose.com/cells/java/com.aspose.cells/style#Pattern) özelliği, ön veya arka plan rengi için kullanılan arka plan desenini belirtir. Aspose.Cells, bir dizi önceden tanımlanmış arka plan deseni türünü içeren [BackgroundType](https://reference.aspose.com/cells/java/com.aspose.cells/BackgroundType) numaralandırmasını sağlar.

|**Desen Türü**|**Açıklama**|
| :- | :- |
|[DİAGONAL_MAT_RASTGELE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#DIAGONAL-CROSSHATCH)|Diyagonal çapraz dokuma desenini temsil eder|
|[DİAGONAL_KIRISIM](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#DIAGONAL-STRIPE)|Diyagonal çizgi deseni temsil eder|
|[GRİ_6](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#GRAY-6)|%6,25 gri deseni temsil eder|
|[GRİ_12](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#GRAY-12)|%12,5 gri deseni temsil eder|
|[GRİ_25](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#GRAY-25)|%25 gri deseni temsil eder|
|[GRİ_50](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#GRAY-50)|%50 gri deseni temsil eder|
|[GRİ_75](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#GRAY-75)|%75 gri deseni temsil eder|
|[YATAY_ÇİZGİ](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#HORIZONTAL-STRIPE)|Yatay çizgi desenini temsil eder|
|[NONE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#NONE)| Arka plan yok demektir.
|[TERS_DİAGONAL_ÇİZGİ](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#REVERSE-DIAGONAL-STRIPE)|Ters diyagonal çizgi desenini temsil eder|
|[SOLID](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#SOLID)| Düz deseni temsil eder.
|[KALIN_DİAGONAL_CROSSHATCH](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THICK-DIAGONAL-CROSSHATCH)|Kalın diyagonal çapraz dokuma desenini temsil eder|
|[İNCE_DİAGONAL_CROSSHATCH](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THIN-DIAGONAL-CROSSHATCH)|İnce diyagonal çapraz dokuma desenini temsil eder|
|[İNCE_DİAGONAL_ÇİZGİ](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THIN-DIAGONAL-STRIPE)|İnce diyagonal çizgi desenini temsil eder|
|[İNCE_YATAY_CROSSHATCH](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THIN-HORIZONTAL-CROSSHATCH)|İnce yatay çapraz dokuma desenini temsil eder|
|[İNCE_YATAY_ÇİZGİ](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THIN-HORIZONTAL-STRIPE)|İnce yatay çizgi desenini temsil eder|
|[İNCE_TERS_DİAGONAL_ÇİZGİ](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THIN-REVERSE-DIAGONAL-STRIPE)|İnce ters diyagonal çizgi desenini temsil eder|
|[İNCE_DİVARTİKAL_ÇİZGİ](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THIN-VERTICAL-STRIPE)|İnce dik çizgi deseni|
|[DİVERTİKAL_ÇİZGİ](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#VERTICAL-STRIPE)|Dikey çizgi deseni|
Aşağıdaki örnekte, A1 hücresinin ön plan rengi ayarlanmış ancak A2, dikey çizgili bir arka plan deseni olan hem ön plan rengi hem de arka plan rengi olarak yapılandırılmıştır.

Kodu çalıştırdığınızda aşağıdaki çıktı oluşturulur.

**Arka plan desenleri olan hücrelerde uygulanan ön plan ve arka plan renkleri** 

![todo:image_alt_text](cells-formatting_6.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ColorsAndBackground-ColorsAndBackground.java" >}}
### **Bilinmesi Gerekenler**
{{% alert color="primary" %}} 

- Bir hücrenin ön plan veya arka plan rengini ayarlamak için [Style](https://reference.aspose.com/cells/java/com.aspose.cells/Style) nesnesinin [ForegroundColor](https://reference.aspose.com/cells/java/com.aspose.cells/style#ForegroundColor) veya [BackgroundColor](https://reference.aspose.com/cells/java/com.aspose.cells/style#BackgroundColor) özelliklerini kullanın. Her iki özellik de [Style](https://reference.aspose.com/cells/java/com.aspose.cells/Style) nesnesinin [Pattern](https://reference.aspose.com/cells/java/com.aspose.cells/style#Pattern) özelliği yapılandırılmışsa yalnızca etki eder.
- [ForegroundColor](https://reference.aspose.com/cells/java/com.aspose.cells/style#ForegroundColor) özelliği hücrenin gölge rengini ayarlar.
  [Pattern](https://reference.aspose.com/cells/java/com.aspose.cells/style#Pattern) özelliği, ön plan veya arka plan rengi için kullanılan arka plan deseni türünü belirtir. Aspose.Cells, [BackgroundType](https://reference.aspose.com/cells/java/com.aspose.cells/BackgroundType) adlı önceden tanımlanmış arka plan deseni türlerini içeren bir numaralama sağlar.
- Eğer [BackgroundType](https://reference.aspose.com/cells/java/com.aspose.cells/BackgroundType) numaralamasından [BackgroundType.NONE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#NONE) değerini seçerseniz, ön plan rengi uygulanmaz.
  Benzer şekilde, [BackgroundType.NONE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#NONE) veya [BackgroundType.SOLID](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#SOLID) değerlerini seçerseniz arka plan rengi uygulanmaz.
- Hücrenin gölge/dolgu rengini alırken, eğer [Style.Pattern](https://reference.aspose.com/cells/java/com.aspose.cells/style#Pattern) değeri [BackgroundType.NONE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#NONE) ise, [Style.ForegroundColor](https://reference.aspose.com/cells/java/com.aspose.cells/style#ForegroundColor) *Color.Empty* değerini döndürecektir.

{{% /alert %}} 
## **Hücredeki Seçili Karakterleri Biçimlendirme**
[Yazı Tipi Ayarları İle İlgilenme](/cells/tr/java/dealing-with-font-settings/), hücreleri nasıl biçimlendireceğinizi ancak hücre içeriğini nasıl biçimlendireceğinizi açıklar. Peki ya sadece belirli karakterleri biçimlendirmek isterseniz?

Aspose.Cells bu özelliği destekler. Bu konu bu özelliği nasıl kullanacağınızı açıklar.
### **Seçili Karakterleri Biçimlendirme**
Aspose.Cells, bir Microsoft Excel dosyasını temsil eden bir sınıf olan [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) sağlar. [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) sınıfı, Excel dosyasındaki her çalışma sayfasına erişim sağlayan [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) içerir. Bir çalışma sayfası, [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) sınıfı tarafından temsil edilir. [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) sınıfı bir [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) koleksiyonu sağlar. [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) koleksiyonundaki her öğe, [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) sınıfının bir öğesini temsil eder.

[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) sınıfı, hücrede karakterleri seçmek için aşağıdaki parametreleri alan [characters](https://reference.aspose.com/cells/java/com.aspose.cells/cell#characters-int-int-) yöntemini sağlar:

- **Başlangıç Dizini**, seçimin başlayacağı karakterin dizini.
- **Karakter Sayısı**, seçilecek karakterlerin sayısı.

Çıktı dosyasında, A1 hücresindeki 'Visit' kelimesi varsayılan yazı tipi ile biçimlendirilir ancak 'Aspose!' kalın ve mavi renklidir.

**Seçili karakterleri biçimlendirme** 

![todo:image_alt_text](cells-formatting_7.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FormattingSelectedCharacters-FormattingSelectedCharacters.java" >}}

{{% alert color="primary" %}} 

Eğer hücredeki zengin metnin bir bölümünü biçimlendirmekle ilgileniyorsanız, [Cell.getCharacters](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getCharacters--) ve Cell.setCharacters yöntemlerini kullanmayı düşünün. [Cell.getCharacters](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getCharacters--) yöntemi, metnin bölümlerine erişmek için kullanılır ve ardından düzenlemeler Cell.setCharacters yöntemiyle yapılabilir. Ayrıca, **get** yöntemi, çeşitli özellikleri ayarlayabilecek [FontSetting](https://reference.aspose.com/cells/java/com.aspose.cells/FontSetting) nesneleri dizisi döndürür ve **set** yöntemi, değişiklikleri uygulamak için kullanılabilir.

{{% /alert %}}

## **Gelişmiş Konular**
- [Hizalama Ayarları](/cells/tr/java/cells-alignment-settings/)
- [Koşullu Biçimlendirme](/cells/tr/java/conditional-formatting/)
- [Veri Biçimlendirme](/cells/tr/java/data-formatting/)
- [Excel Temaları ve Renkleri](/cells/tr/java/excel-2007-themes-and-colors/)
- [Yazı Tipi Ayarları İle İlgilenme](/cells/tr/java/dealing-with-font-settings/)
- [Bir İşkitapta Hücreleri Biçimlendirme](/cells/tr/java/format-worksheet-cells-in-a-workbook/)
- [1904 Tarih Sistemi Uygulama](/cells/tr/java/implement-1904-date-system/)
- [Hücreleri Birleştirme ve Ayırma](/cells/tr/java/merging-and-unmerging-cells/)
- [Sayı Ayarları](/cells/tr/java/cells-number-settings/)
- [Hücre Değerinin veya Aralığın Ön Eklemesini Koruma](/cells/tr/java/preserve-single-quote-prefix-of-cell-value-or-range/)
- [Stil ve Veri Biçimlendirme](/cells/tr/java/styling-and-data-formatting/)
{{< app/cells/assistant language="java" >}}
