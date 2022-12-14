---
title: Cells Biçimler
type: docs
weight: 100
url: /tr/java/cells-formatting/
---
## **Cells'e Kenarlık Ekleme**
Microsoft Excel, kullanıcıların kenarlık ekleyerek hücreleri biçimlendirmesine olanak tanır.

**Microsoft Excel'deki kenarlıklar ayarları** 

![yapılacaklar:resim_alternatif_Metin](cells-formatting_1.png)

Kenarlığın türü, nereye eklendiğine bağlıdır. Örneğin, bir üst kenarlık bir hücrenin en üst konumuna eklenir. Kullanıcılar ayrıca kenarlıkların çizgi stilini ve rengini değiştirebilir.

Aspose.Cells ile geliştiriciler, Microsoft Excel'de yapabildikleri aynı esnek yöntemle kenarlıklar ekleyebilir ve görünüşlerini özelleştirebilir.
### **Cells'e Kenarlık Ekleme**
 Aspose.Cells bir sınıf sağlar,[Çalışma kitabı](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) bu bir Microsoft Excel dosyasını temsil eder. bu[Çalışma kitabı](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) sınıf bir içerir[Çalışma Sayfası Koleksiyonu](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)Excel dosyasındaki her çalışma sayfasına erişim sağlar. Bir çalışma sayfası şununla temsil edilir:[Çalışma kağıdı](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) sınıf. bu[Çalışma kağıdı](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) sınıf bir sağlar[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) Toplamak. İçindeki her öğe[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) koleksiyon bir nesneyi temsil eder[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell)sınıf.

 Aspose.Cells şunları sağlar:[setStyle](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setStyle\(com.aspose.cells.Style\) ) yönteminde[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) hücrenin biçimlendirme stilini ayarlamak için kullanılan sınıf. Ayrıca, nesnenin[stil](https://reference.aspose.com/cells/java/com.aspose.cells/Style)class kullanılır ve yazı tipi ayarlarını yapılandırmak için özellikler sağlar.
#### **Cell'e Kenarlık Ekleme**
 ile bir hücreye kenarlıklar ekleyin[stil](https://reference.aspose.com/cells/java/com.aspose.cells/Style) nesnenin[sınır ayarla](https://reference.aspose.com/cells/java/com.aspose.cells/style#setBorder\(int,%20int,%20com.aspose.cells.Color\) ) yöntem. Kenarlık türü parametre olarak iletilir. Tüm kenarlık türleri,[Kenarlık Türü](https://reference.aspose.com/cells/java/com.aspose.cells/BorderType)numaralandırma.

|**Kenarlık Türleri**|**Tanım**|
|:- |:- |
|[ALT SINIR](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#BOTTOM_BORDER)|Alt sınır çizgisi|
|[DIAGONAL_DOWN](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#DIAGONAL_DOWN)|Sol üstten sağ alta çapraz bir çizgi|
|[DIAGONAL_UP](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#DIAGONAL_UP)|Sol alttan sağ üste çapraz bir çizgi|
|[LEFT_BORDER](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#LEFT_BORDER)|Sol sınır çizgisi|
|[SAĞ_KENAR](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#RIGHT_BORDER)|Sağ sınır çizgisi|
|[TOP_BORDER](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#TOP_BORDER)|Üst sınır çizgisi|
|[YATAY](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#HORIZONTAL)|Yalnızca koşullu biçimlendirme gibi dinamik stil için.|
|[DİKEY](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#VERTICAL)|Yalnızca koşullu biçimlendirme gibi dinamik stil için.|
 Çizgi rengini ayarlamak için, kullanarak bir renk seçin.[Renk](https://reference.aspose.com/cells/java/com.aspose.cells/Color) numaralandırmak ve ona iletmek[stil](https://reference.aspose.com/cells/java/com.aspose.cells/Style) nesnenin[sınır ayarla](https://reference.aspose.com/cells/java/com.aspose.cells/style#setBorder\(int,%20int,%20com.aspose.cells.Color\) ) yöntemin Color parametresi. Çizgi stilleri önceden tanımlanmıştır.[Hücre Sınır Türü](https://reference.aspose.com/cells/java/com.aspose.cells/CellBorderType)numaralandırma.

|**Çizgi Stilleri**|**Tanım**|
|:- |:- |
|[ÇİZGİ NOKTA](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#DASH_DOT)|İnce çizgi noktalı çizgiyi temsil eder|
|[DASH_NOKTA_NOKTA](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#DASH_DOT_DOT)|İnce çizgi noktalı çizgiyi temsil eder|
|[KESİKLİ](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#DASHED)|Kesikli çizgiyi temsil eder|
|[NOKTALI](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#DOTTED)|Noktalı çizgiyi temsil eder|
|[ÇİFT](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#DOUBLE)|Çift çizgiyi temsil eder|
|[SAÇ](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#HAIR)|Saç çizgisini temsil eder|
|[ORTA_DASH_NOKTA](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#MEDIUM_DASH_DOT)|Orta çizgi noktalı çizgiyi temsil eder|
|[ORTA_DASH_NOKTA NOKTA](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#MEDIUM_DASH_DOT_DOT)|Orta çizgi noktalı çizgiyi temsil eder|
|[ORTA_DASHED](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#MEDIUM_DASHED)|Orta kesikli çizgiyi temsil eder|
|[YOK](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#NONE)|Hiçbir çizgiyi temsil etmez|
|[ORTA](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#MEDIUM)|Orta çizgiyi temsil eder|
|[EĞİMLİ_DASH_NOKTA](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#SLANTED_DASH_DOT)|Eğimli orta noktalı çizgiyi temsil eder|
|[KALIN](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#THICK)|Kalın çizgiyi temsil eder|
|[İNCE](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#THIN)|İnce çizgiyi temsil eder|
 Yukarıdaki çizgi stillerinden birini seçin ve ardından bunu[stil](https://reference.aspose.com/cells/java/com.aspose.cells/Style)nesnenin[sınır ayarla](https://reference.aspose.com/cells/java/com.aspose.cells/style#setBorder\(int,%20int,%20com.aspose.cells.Color\)) yöntem.

Aşağıdaki kod yürütülürken aşağıdaki çıktı üretilir.

**Bir hücrenin her tarafına uygulanan kenarlıklar** 

![yapılacaklar:resim_alternatif_Metin](cells-formatting_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AddingBordersToCells-AddingBordersToCells.java" >}}
#### **Cells Aralığına Kenarlık Ekleme**
 Tek bir hücre yerine bir dizi hücreye kenarlık eklemek mümkündür. İlk olarak, çağırarak bir hücre aralığı oluşturun.[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) koleksiyonun[aralık oluştur](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange\(int,%20int,%20boolean\)) yöntemi, aşağıdaki parametreleri alır:

- **İlk sıra**, aralığın ilk satırı.
- **İlk sütun**, aralığın ilk sütunu.
- **Satır sayısı**, aralıktaki satır sayısı.
- **Sütun sayısı**, aralıktaki sütun sayısı.

 bu[aralık oluştur](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange\(int,%20int,%20boolean\) ) yöntemi bir döndürür[Menzil](https://reference.aspose.com/cells/java/com.aspose.cells/Range) belirtilen aralığı içeren nesne. bu[Menzil](https://reference.aspose.com/cells/java/com.aspose.cells/Range) nesne sağlar[setOutlineBorders](https://reference.aspose.com/cells/java/com.aspose.cells/range#setOutlineBorders\(int,%20com.aspose.cells.Color\)) aşağıdaki parametreleri alan yöntem:

- **Hücre Sınır Türü**, sınır çizgisi stili,[Hücre Sınır Türü](https://reference.aspose.com/cells/java/com.aspose.cells/CellBorderType)numaralandırma.
- **Renk**, sınır çizgisi rengi,[Renk](https://reference.aspose.com/cells/java/com.aspose.cells/Color)numaralandırma.

Aşağıdaki kod yürütülürken aşağıdaki çıktı üretilir.

**Bir hücre aralığına uygulanan kenarlıklar** 

![yapılacaklar:resim_alternatif_Metin](cells-formatting_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AddingBorderstoRange-AddingBorderstoRange.java" >}}
## **Renkler ve Palet**
Palet, bir görüntü oluştururken kullanılabilecek renk sayısıdır. Bir sunumda standartlaştırılmış bir paletin kullanılması, kullanıcının tutarlı bir görünüm oluşturmasına olanak tanır. Her Microsoft Excel (97-2003) dosyası, bir grafikteki hücrelere, yazı tiplerine, kılavuz çizgilerine, grafik nesnelerine, dolgulara ve çizgilere uygulanabilen 56 renk paletine sahiptir.

**Microsoft Excel'deki palet ayarları** 

![yapılacaklar:resim_alternatif_Metin](cells-formatting_4.png)

Aspose.Cells ile sadece mevcut renkleri değil, özel renkleri de kullanmak mümkündür. Özel bir renk kullanmadan önce palete ekleyin. Bu konu, özel renklerin palete nasıl ekleneceğini açıklar.
### **Palete Özel Renkler Ekleme**
Aspose.Cells ayrıca 56 renk paletini destekler. Yukarıda standart bir renk paleti gösterilmektedir. Palette tanımlı olmayan özel bir renk kullanmak istiyorsanız, kullanmadan önce o rengi palete eklemeniz gerekecektir.

{{% alert color="primary" %}} 

Palet sadece 56 renk içerir. Palete özel bir renk eklediğinizde, palet değiştirilir ve önceki renkle biçimlendirilmiş dosyadaki herhangi bir öğe değiştirilir. Bu yüzden paleti değiştirirken lütfen çok dikkatli olun. Ayrıca, XLSX veya diğer gelişmiş MS Excel (2007/2010) dosya biçimleri için böyle bir sınırlama olmadığından, bu yalnızca XLS (Excel 97 - 2003) dosya biçimindeki sınırlamadır.

{{% /alert %}} 

Aspose.Cells bir sınıf sağlar,[Çalışma kitabı](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook), bu bir Microsoft Excel dosyasını temsil eder. sınıf sağlar[paleti değiştir](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#changePalette\(com.aspose.cells.Color,%20int\)) paleti değiştirmek üzere özel bir renk eklemek için aşağıdaki parametreleri alan yöntem:

- **Özel renk**, palete eklenecek özel renk.
- **dizin**, özel renkle değiştirilecek rengin dizini. 0-55 arasında olmalıdır.

Aşağıdaki örnek, bir yazı tipine uygulamadan önce palete özel bir renk ekler.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ColorsAndPalette-ColorsAndPalette.java" >}}
## **Renkler ve Arka Plan Desenleri**
Microsoft Excel, hücrelerin ön plan (anahat) ve arka plan (dolgu) renklerini ve arka plan desenlerini aşağıda gösterildiği gibi ayarlayabilir.

**Microsoft Excel'de renkleri ve arka plan Desenlerini ayarlama** 

![yapılacaklar:resim_alternatif_Metin](cells-formatting_5.png)

Aspose.Cells de bu özellikleri esnek bir şekilde destekler. Bu konuda Aspose.Cells kullanarak bu özellikleri kullanmayı öğreniyoruz.
### **Renkleri ve Arka Plan Desenlerini Ayarlama**
Aspose.Cells bir sınıf sağlar,[Çalışma kitabı](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook), bu bir Microsoft Excel dosyasını temsil eder. bu[Çalışma kitabı](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)sınıf bir içerir[Çalışma Sayfası Koleksiyonu](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)Excel dosyasındaki her çalışma sayfasına erişim sağlar. Bir çalışma sayfası şununla temsil edilir:[Çalışma kağıdı](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)sınıf. bu[Çalışma kağıdı](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)sınıf bir sağlar[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)Toplamak. İçindeki her öğe[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)koleksiyon bir nesneyi temsil eder[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell)sınıf.

Aspose.Cells şunları sağlar:[setStyle](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setStyle\(com.aspose.cells.Style\)) yönteminde[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell)hücre biçimlendirmesini ayarlamak için kullanılan sınıf. Ayrıca, nesnenin[stil](https://reference.aspose.com/cells/java/com.aspose.cells/Style)class yazı tipi ayarlarını yapılandırmak için kullanılabilir.

{{% alert color="primary" %}} 

 Bir hücrenin ön plan veya arka plan rengini ayarlamak için[stil](https://reference.aspose.com/cells/java/com.aspose.cells/Style) nesnenin[setBackgroundColor](https://reference.aspose.com/cells/java/com.aspose.cells/style#BackgroundColor) veya[setÖn PlanRengi](https://reference.aspose.com/cells/java/com.aspose.cells/style#ForegroundColor) özellikleri. Bu özellikler yalnızca şu durumlarda yürürlüğe girer:[stil](https://reference.aspose.com/cells/java/com.aspose.cells/Style) nesnenin[setPattern](https://reference.aspose.com/cells/java/com.aspose.cells/style#Pattern) özellik yapılandırılır.

{{% /alert %}} 

bu[setÖn PlanRengi](https://reference.aspose.com/cells/java/com.aspose.cells/style#ForegroundColor)özelliği hücrenin gölgeleme rengini ayarlar.

bu[setPattern](https://reference.aspose.com/cells/java/com.aspose.cells/style#Pattern) özelliği, ön plan veya arka plan rengi için kullanılan arka plan desenini belirtir. Aspose.Cells şunları sağlar:[ArkaplanTürü](https://reference.aspose.com/cells/java/com.aspose.cells/BackgroundType)önceden tanımlanmış bir dizi arka plan deseni içeren numaralandırma.

|**Desen Tipi**|**Tanım**|
|:- |:- |
|[DIAGONAL_CROSSHATCH](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#DIAGONAL_CROSSHATCH)|Çapraz çapraz tarama modelini temsil eder|
|[DIAGONAL_STRIPE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#DIAGONAL_STRIPE)|Çapraz şerit desenini temsil eder|
|[GRAY_6](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#GRAY_6)|%6,25 gri deseni temsil eder|
|[GRAY_12](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#GRAY_12)|%12,5 gri deseni temsil eder|
|[GRAY_25](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#GRAY_25)|%25 gri deseni temsil eder|
|[GRAY_50](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#GRAY_50)|%50 gri modeli temsil eder|
|[GRAY_75](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#GRAY_75)|%75 gri deseni temsil eder|
|[YATAY_STRIPE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#HORIZONTAL_STRIPE)|Yatay şerit desenini temsil eder|
|[YOK](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#NONE)|arka planı temsil etmez|
|[TERSİ_DİYAGONAL_ŞERİT](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#REVERSE_DIAGONAL_STRIPE)|Ters diyagonal şerit desenini temsil eder|
|[SAĞLAM](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#SOLID)|Katı modeli temsil eder|
|[KALIN_DİYAGONAL_ÇAPRAZ HAT](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THICK_DIAGONAL_CROSSHATCH)|Kalın çapraz tarama desenini temsil eder|
|[İNCE_DİYAGONAL_ÇAPRAZ HAT](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THIN_DIAGONAL_CROSSHATCH)|İnce çapraz tarama modelini temsil eder|
|[İNCE_DİYAGONAL_ŞERİT](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THIN_DIAGONAL_STRIPE)|İnce çapraz şerit desenini temsil eder|
|[İNCE_YATAY_ÇAPRAZ HAT](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THIN_HORIZONTAL_CROSSHATCH)|İnce yatay çapraz tarama modelini temsil eder|
|[İNCE_YATAY_ŞERİT](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THIN_HORIZONTAL_STRIPE)|İnce yatay şerit desenini temsil eder|
|[İNCE_TERSİ_DIAGONAL_STRIPE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THIN_REVERSE_DIAGONAL_STRIPE)|İnce ters köşegen şerit desenini temsil eder|
|[İNCE_DİKEY_ŞERİT](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THIN_VERTICAL_STRIPE)|İnce dikey şerit desenini temsil eder|
|[VERTICAL_STRIPE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#VERTICAL_STRIPE)|Dikey şerit desenini temsil eder|
Aşağıdaki örnekte, A1 hücresinin ön plan rengi ayarlanmıştır ancak A2, dikey şerit arka plan deseniyle hem ön plan hem de arka plan renklerine sahip olacak şekilde yapılandırılmıştır.

Kod yürütülürken aşağıdaki çıktı oluşturulur.

**Arka plan desenlerine sahip hücrelere uygulanan ön plan ve arka plan renkleri** 

![yapılacaklar:resim_alternatif_Metin](cells-formatting_6.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ColorsAndBackground-ColorsAndBackground.java" >}}
### **Bilmeniz Önemli**
{{% alert color="primary" %}} 

-  Bir hücrenin ön plan veya arka plan rengini ayarlamak için[stil](https://reference.aspose.com/cells/java/com.aspose.cells/Style) nesnenin[Ön plan rengi](https://reference.aspose.com/cells/java/com.aspose.cells/style#ForegroundColor) veya[Arka plan rengi](https://reference.aspose.com/cells/java/com.aspose.cells/style#BackgroundColor) özellikleri. Her iki özellik de yalnızca şu durumlarda geçerli olacaktır:[stil](https://reference.aspose.com/cells/java/com.aspose.cells/Style) nesnenin[Model](https://reference.aspose.com/cells/java/com.aspose.cells/style#Pattern) özellik yapılandırılır.
-  bu[Ön plan rengi](https://reference.aspose.com/cells/java/com.aspose.cells/style#ForegroundColor) özelliği hücrenin gölge rengini ayarlar.
 bu[Model](https://reference.aspose.com/cells/java/com.aspose.cells/style#Pattern) özelliği, ön plan veya arka plan rengi için kullanılan arka plan deseninin türünü belirtir. Aspose.Cells bir numaralandırma sağlar,[ArkaplanTürü](https://reference.aspose.com/cells/java/com.aspose.cells/BackgroundType)önceden tanımlanmış bir dizi arka plan deseni içerir.
-  eğer seçersen[ArkaplanTürü.YOK](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#NONE) gelen değer[ArkaplanTürü](https://reference.aspose.com/cells/java/com.aspose.cells/BackgroundType) numaralandırma, ön plan rengi uygulanmaz.
 Aynı şekilde, arka plan rengini seçerseniz arka plan rengi uygulanmaz.[ArkaplanTürü.YOK](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#NONE) veya[BackgroundType.SOLID](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#SOLID) değerler.
-  Hücrenin gölgeleme/dolgu rengini alırken, eğer[Stil.Desen](https://reference.aspose.com/cells/java/com.aspose.cells/style#Pattern) dır-dir[ArkaplanTürü.YOK](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#NONE), [Stil.Ön PlanRenk](https://reference.aspose.com/cells/java/com.aspose.cells/style#ForegroundColor) geri dönücek*Renk.Boş*.

{{% /alert %}} 
## **Cell'de Seçili Karakterleri Biçimlendirme**
[Yazı Tipi Ayarlarıyla Başa Çıkma](/cells/tr/java/dealing-with-font-settings/) hücrelerin nasıl biçimlendirileceğini, ancak yalnızca tüm hücrelerin içeriğinin nasıl biçimlendirileceğini açıkladı. Yalnızca seçili karakterleri biçimlendirmek isterseniz ne olur?

Aspose.Cells bu özelliği destekler. Bu konuda, bu özelliğin nasıl kullanılacağı açıklanmaktadır.
### **Seçilen Karakterleri Biçimlendirme**
Aspose.Cells bir sınıf sağlar,[Çalışma kitabı](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook), bu bir Microsoft Excel dosyasını temsil eder. bu[Çalışma kitabı](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)sınıf bir içerir[Çalışma Sayfası Koleksiyonu](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)Excel dosyasındaki her çalışma sayfasına erişim sağlar. Bir çalışma sayfası şununla temsil edilir:[Çalışma kağıdı](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)sınıf. bu[Çalışma kağıdı](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)sınıf bir sağlar[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)Toplamak. İçindeki her öğe[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)koleksiyon bir nesneyi temsil eder[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell)sınıf.

bu[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) sınıf sağlar[karakterler](https://reference.aspose.com/cells/java/com.aspose.cells/cell#characters\(int,%20int\)) bir hücrede bir dizi karakter seçmek için aşağıdaki parametreleri alan yöntem:

- **Dizini başlat**, seçimin başlatılacağı karakterin dizini.
- **Karakter sayısı**, seçilecek karakter sayısı.

Çıktı dosyasında, A1" hücresinde, 'Ziyaret' sözcüğü varsayılan yazı tipiyle biçimlendirilmiştir ancak 'Aspose!' kalın ve mavidir.

**Seçilen karakterleri biçimlendirme** 

![yapılacaklar:resim_alternatif_Metin](cells-formatting_7.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FormattingSelectedCharacters-FormattingSelectedCharacters.java" >}}

{{% alert color="primary" %}} 

 Eğer ilgileniyorsanız[bir hücrede Zengin Metnin bir bölümünü biçimlendirme](/cells/tr/java/access-and-update-the-portions-of-rich-text-of-cell/) kullanmayı düşünün[Cell.getCharacters](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getCharacters\(\) ) & Cell.setCharacters yöntemleri. bu[Cell.getCharacters](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getCharacters\(\) ) yöntemi kullanılarak metnin bölümlerine erişilir ve daha sonra Cell.setCharacters yöntemi kullanılarak değişiklikler yapılabilir.**almak**yöntem bir dizi döndürür[Yazı Tipi Ayarı](https://reference.aspose.com/cells/java/com.aspose.cells/FontSetting) yazı tipi adı, yazı tipi rengi, kalınlık vb. gibi çeşitli özellikleri ayarlamak için değiştirilebilen nesneler ve**Ayarlamak** Yöntem, değişiklikleri uygulamak için kullanılabilir.

{{% /alert %}}

## **ileri konular**
- [Hizalama Ayarları](/cells/tr/java/cells-alignment-settings/)
- [Koşullu biçimlendirme](/cells/tr/java/conditional-formatting/)
- [Veri Biçimlendirme](/cells/tr/java/data-formatting/)
- [Excel Temaları ve Renkleri](/cells/tr/java/excel-2007-themes-and-colors/)
- [Yazı Tipi Ayarlarıyla Başa Çıkma](/cells/tr/java/dealing-with-font-settings/)
- [Bir Çalışma Kitabında Çalışma Sayfasını Biçimlendir Cells](/cells/tr/java/format-worksheet-cells-in-a-workbook/)
- [1904 Tarih Sistemini Uygulayın](/cells/tr/java/implement-1904-date-system/)
- [Birleşme ve Ayrılma Cells](/cells/tr/java/merging-and-unmerging-cells/)
- [Sayı Ayarları](/cells/tr/java/cells-number-settings/)
- [Cell Değerinin veya Aralığının Tek Alıntı Ön Ekini Koru](/cells/tr/java/preserve-single-quote-prefix-of-cell-value-or-range/)
- [Şekillendirme ve Veri Biçimlendirme](/cells/tr/java/styling-and-data-formatting/)
