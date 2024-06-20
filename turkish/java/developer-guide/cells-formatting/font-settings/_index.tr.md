---
title: Yazı Tipi Ayarları İle İlgilenme
linktitle: Font Ayarları
type: docs
weight: 20
url: /tr/java/dealing-with-font-settings/
---

{{% alert color="primary" %}} 

Metnin görünümü, yazı tipi ayarlarını değiştirerek kontrol edilebilir. Bu yazı tipi ayarları, aşağıdaki şekilde gösterildiği gibi yazı tipinin adını, stilini, boyutunu, rengini ve diğer etkilerini içerebilir.

**Microsoft Excel'de Yazı Tipi Ayarları** 

![todo:image_alt_text](dealing-with-font-settings_1.png)

Microsoft Excel gibi, Aspose.Cells de hücrelerin yazı tipi ayarlarını yapılandırmayı destekler.

{{% /alert %}} 
## **Font Ayarlarını Yapılandırma**
Aspose.Cells, bir Microsoft Excel dosyasını temsil eden [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) sınıfını sağlar. [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) sınıfı, bir Excel dosyasındaki her çalışma sayfasına erişime izin veren [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) içerir. Bir çalışma sayfası, [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) sınıfı tarafından temsil edilir. [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) sınıfı, bir [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) koleksiyonu sağlar. [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) koleksiyonundaki her öğe, [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) sınıfının bir nesnesini temsil eder.

Aspose.Cells, [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) sınıfının [setStyle](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setStyle\(com.aspose.cells.Style\)) metodunu sağlar. Bu metod, bir hücrenin biçimlendirmesini ayarlamak için kullanılır. Ayrıca [Style](https://reference.aspose.com/cells/java/com.aspose.cells/Style) sınıfının nesnesi, yazı tipi ayarlarını yapılandırmak için özellikler sağlar.

Bu makalede, şunları gösterecektir:

- [Metne belirli bir yazı tipi uygulayın.](/cells/tr/java/dealing-with-font-settings/)
- [Metni kalın yap](/cells/tr/java/dealing-with-font-settings/).
- [Yazı tipi boyutunu ayarlayın](/cells/tr/java/dealing-with-font-settings/).
- [Yazı tipi rengini ayarlayın](/cells/tr/java/dealing-with-font-settings/).
- [Metni altını çiz](/cells/tr/java/dealing-with-font-settings/).
- [Metni üstü çizili yap](/cells/tr/java/dealing-with-font-settings/).
- [Metni alt simge yap](/cells/tr/java/dealing-with-font-settings/).
- [Metni üst simge yap](/cells/tr/java/dealing-with-font-settings/).
### **Yazı Tipi Adını Ayarlama**
Hücrelerdeki metne belirli bir yazı tipi uygulamak için [Font](https://reference.aspose.com/cells/java/com.aspose.cells/Font) nesnesinin [setName](https://reference.aspose.com/cells/java/com.aspose.cells/font#Name) özelliğini kullanın.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SettingFontName-SettingFontName.java" >}}
### **Yazı Tipi Stilini Kalın Yapma**
[Font](https://reference.aspose.com/cells/java/com.aspose.cells/Font) nesnesinin [setBold](https://reference.aspose.com/cells/java/com.aspose.cells/font#IsBold) özelliğini **true** olarak ayarlayarak metni kalın yapın.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-SettingFontStyle-1.java" >}}
### **Yazı Tipi Boyutunu Ayarlama**
[Font](https://reference.aspose.com/cells/java/com.aspose.cells/Font) nesnesinin [setSize](https://reference.aspose.com/cells/java/com.aspose.cells/font#Size) özelliğini kullanarak yazı tipi boyutunu ayarlayın.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SetFontSize-SetFontSize.java" >}}
### **Yazı Tipi Altı Çizgi Türünü Ayarlama**
[Font](https://reference.aspose.com/cells/java/com.aspose.cells/Font) nesnesinin [setUnderline](https://reference.aspose.com/cells/java/com.aspose.cells/font#Underline) özelliği ile metni altı çizili yapın. Aspose.Cells, [FontUnderlineType](https://reference.aspose.com/cells/java/com.aspose.cells/FontUnderlineType) numaralandırmasında çeşitli önceden tanımlanmış yazı tipi alt çizgi türleri sunar.

|**Yazı Tipi Altı Çizgi Tipleri**|**Açıklama**|
| :- | :- |
|[NONE](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#NONE)|Alt çizgi yok|
|[SINGLE](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#SINGLE)|Tek bir alt çizgi|
|[DOUBLE](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DOUBLE)|Çift alt çizgi|
|[ACCOUNTING](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#ACCOUNTING)|Tek bir muhasebe alt çizgisi|
|[DOUBLE_ACCOUNTING](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DOUBLE_ACCOUNTING)|Çift muhasebe alt çizgisi|
|[DASH](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DASH)|Kesikli Alt Çizgi|
|[DASH_DOT_DOT_HEAVY](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DASH_DOT_DOT_HEAVY)|Kalın Kesikli Nokta-Nokta Alt Çizgi|
|[DASH_DOT_HEAVY](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DASH_DOT_HEAVY)|Kesikli Nokta-Nokta Alt Çizgi|
|[DASHED_HEAVY](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DASHED_HEAVY)|Kalın Kesikli Alt Çizgi|
|[DASH_LONG](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DASH_LONG)|Uzun Kesik Alt Çizgi|
|[DASH_LONG_HEAVY](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DASH_LONG_HEAVY)|Kalın Uzun Kesik Alt Çizgi|
|[DOT_DASH](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DOT_DASH)|Çizgi-Nokta Alt Çizgi|
|[DOT_DOT_DASH](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DOT_DOT_DASH)|Çizgi-Nokta-Nokta Alt Çizgi|
|[DOTTED](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DOTTED)|Noktalı Alt Çizgi|
|[DOTTED_HEAVY](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DOTTED_HEAVY)|Kalın Noktalı Alt Çizgi|
|[HEAVY](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#HEAVY)|Kalın Alt Çizgi|
|[WAVE](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#WAVE)|Dalgalı Alt Çizgi|
|[WAVY_DOUBLE](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#WAVY_DOUBLE)|Çift Dalgalı Alt Çizgi|
|[WAVY_HEAVY](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#WAVY_HEAVY)|Kalın Dalgalı Alt Çizgi|
|[WORDS](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#WORDS)|Sadece Boşluk Olmayan Karakterlere Alt Çizgi Uygula|
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SettingFontUnderlineType-SettingFontUnderlineType.java" >}}



### **Yazı Tipi Rengini Ayarlama**
[Font](https://reference.aspose.com/cells/java/com.aspose.cells/Font) nesnesinin [setColor](https://reference.aspose.com/cells/java/com.aspose.cells/font#Color) özelliği ile yazı tipi rengini ayarlayın. [Color](https://reference.aspose.com/cells/java/com.aspose.cells/Color) enum'den herhangi bir rengi seçin ve seçilen rengi [Font](https://reference.aspose.com/cells/java/com.aspose.cells/Font) nesnesinin [setColor](https://reference.aspose.com/cells/java/com.aspose.cells/font#Color) özelliğine atayın.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SetFontColor-SetFontColor.java" >}}



### **Metin Üzerine Çizgi Çekme Efektini Ayarlama**
[Font](https://reference.aspose.com/cells/java/com.aspose.cells/Font) nesnesinin [setStrikeout](https://reference.aspose.com/cells/java/com.aspose.cells/font#IsStrikeout) özelliği ile metin üzerine çizgi çekme efektini ayarlayın.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SettingStrikeOutEffect-SettingStrikeOutEffect.java" >}}



### **Alt Skript Ayarlama**
[Font](https://reference.aspose.com/cells/java/com.aspose.cells/Font) nesnesinin [setSubscript](https://reference.aspose.com/cells/java/com.aspose.cells/font#IsSubscript) özelliği ile metni alt skript yapın.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SetSubscript-SetSubscript.java" >}}



### **Üst Skript Ayarlama**
[Font](https://reference.aspose.com/cells/java/com.aspose.cells/Font) nesnesinin [setSuperscript](https://reference.aspose.com/cells/java/com.aspose.cells/font#IsSuperscript) özelliği ile metni üst skript yapın.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SetSuperscript-SetSuperscript.java" >}}

## **Gelişmiş Konular**
- [Yazı Tipi Üzerine Üst Simge ve Abone Etkileri Uygulama](/cells/tr/java/apply-superscript-and-subscript-effects-on-fonts/)
- [Bir Elektronik Tablo veya Çalışma Kitabında Kullanılan Yazı Tiplerinin Listesini Alın](/cells/tr/java/get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook/)
