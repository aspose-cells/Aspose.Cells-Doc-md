---
title: Yazı Tipi Ayarlarıyla Başa Çıkma
linktitle: Yazı Tipi Ayarları
type: docs
weight: 20
url: /tr/java/dealing-with-font-settings/
---
{{% alert color="primary" %}} 

Metnin görünümü ve hissi, yazı tipi ayarları değiştirilerek kontrol edilebilir. Bu yazı tipi ayarları, aşağıda şekilde gösterildiği gibi yazı tiplerinin adını, stilini, boyutunu, rengini ve diğer efektlerini içerebilir:

**Microsoft Excel'deki yazı tipi ayarları** 

![yapılacaklar:resim_alternatif_Metin](dealing-with-font-settings_1.png)

Tıpkı Microsoft Excel gibi, Aspose.Cells de hücrelerin yazı tipi ayarlarını yapılandırmayı destekler.

{{% /alert %}} 
## **Yazı Tipi Ayarlarını Yapılandırma**
 Aspose.Cells bir sınıf sağlar,[Çalışma kitabı](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) bu bir Microsoft Excel dosyasını temsil eder. bu[Çalışma kitabı](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) sınıf bir içerir[Çalışma Sayfası Koleksiyonu](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) Bu, bir Excel dosyasındaki her çalışma sayfasına erişim sağlar. Bir çalışma sayfası şununla temsil edilir:[Çalışma kağıdı](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)sınıf. bu[Çalışma kağıdı](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) sınıf bir sağlar[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) Toplamak. İçindeki her öğe[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) koleksiyon bir nesneyi temsil eder[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell)sınıf.

 Aspose.Cells şunları sağlar:[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) sınıf'[setStyle](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setStyle\(com.aspose.cells.Style\) ) yöntemi, bir hücrenin biçimlendirmesini ayarlamak için kullanılır. Ayrıca, nesnenin[stil](https://reference.aspose.com/cells/java/com.aspose.cells/Style)class, yazı tipi ayarlarını yapılandırmak için özellikler sağlar.

Bu makale şunların nasıl yapılacağını gösterir:

- [Metne belirli bir yazı tipi uygulayın.](/cells/tr/java/dealing-with-font-settings/)
- [Metni kalın olarak ayarla](/cells/tr/java/dealing-with-font-settings/).
- [Yazı tipi boyutunu ayarla](/cells/tr/java/dealing-with-font-settings/).
- [Yazı tipi rengini ayarla](/cells/tr/java/dealing-with-font-settings/).
- [Metnin altını çiz](/cells/tr/java/dealing-with-font-settings/).
- [üstü çizili metin](/cells/tr/java/dealing-with-font-settings/).
- [Metni alt simgeye ayarla](/cells/tr/java/dealing-with-font-settings/).
- [Metni üst simge olarak ayarla](/cells/tr/java/dealing-with-font-settings/).
### **Yazı Tipi Adını Ayarlama**
 Kullanarak hücrelerdeki metne belirli bir yazı tipi uygulayın.[Yazı tipi](https://reference.aspose.com/cells/java/com.aspose.cells/Font) nesnenin[setName](https://reference.aspose.com/cells/java/com.aspose.cells/font#Name)Emlak.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SettingFontName-SettingFontName.java" >}}
### **Yazı Tipi Stilini Kalın Olarak Ayarlama**
 ayarlayarak metni kalın olarak ayarlayın.[Yazı tipi](https://reference.aspose.com/cells/java/com.aspose.cells/Font) nesnenin[kalın ayarla](https://reference.aspose.com/cells/java/com.aspose.cells/font#IsBold) mülkiyet**doğru**.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-SettingFontStyle-1.java" >}}
### **Yazı Tipi Boyutunu Ayarlama**
 kullanarak yazı tipi boyutunu ayarlayın.[Yazı tipi](https://reference.aspose.com/cells/java/com.aspose.cells/Font) nesnenin[setBoyutu](https://reference.aspose.com/cells/java/com.aspose.cells/font#Size)Emlak.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SetFontSize-SetFontSize.java" >}}
### **Yazı Tipi Altı Çizili Tipini Ayarlama**
 ile metnin altını çizin[Yazı tipi](https://reference.aspose.com/cells/java/com.aspose.cells/Font) nesnenin[setUnderline](https://reference.aspose.com/cells/java/com.aspose.cells/font#Underline) Emlak. Aspose.Cells, önceden tanımlanmış çeşitli alt çizgili yazı tipleri sunar.[FontUnderlineType](https://reference.aspose.com/cells/java/com.aspose.cells/FontUnderlineType)numaralandırma.

|**Alt Çizgi Tipleri**|**Tanım**|
|:- |:- |
|[YOK](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#NONE)|Alt çizgi yok|
|[BEKAR](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#SINGLE)|Tek bir alt çizgi|
|[ÇİFT](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DOUBLE)|Çift alt çizgi|
|[MUHASEBE](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#ACCOUNTING)|Tek bir muhasebe alt çizgisi|
|[DOUBLE_ACCOUNTING](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DOUBLE_ACCOUNTING)|Çift hesap altı çizili|
|[DASH](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DASH)|Kesikli Altı Çizili|
|[DASH_NOKTA_DOT_AĞIR](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DASH_DOT_DOT_HEAVY)|Kalın Çizgi-Nokta-Nokta Altı Çizili|
|[DASH_NOKTA_AĞIR](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DASH_DOT_HEAVY)|Kalın Çizgi-Nokta Altı Çizili|
|[DASHED_AĞIR](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DASHED_HEAVY)|Kalın Kesikli Alt Çizgi|
|[DASH_LONG](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DASH_LONG)|Uzun Kesikli Alt Çizgi|
|[DASH_UZUN_AĞIR](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DASH_LONG_HEAVY)|Kalın Uzun Kesikli Alt Çizgi|
|[DOT_DASH](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DOT_DASH)|Tire-Nokta Altı Çizili|
|[NOKTA_NOKTA_DASH](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DOT_DOT_DASH)|Tire-Nokta-Nokta Altı Çizili|
|[NOKTALI](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DOTTED)|Noktalı Altı Çizili|
|[DOTTED_AĞIR](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DOTTED_HEAVY)|Kalın Noktalı Alt Çizgi|
|[AĞIR](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#HEAVY)|Kalın Alt Çizgi|
|[DALGA](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#WAVE)|Dalga Alt Çizgisi|
|[WAVY_DOUBLE](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#WAVY_DOUBLE)|Çift Dalga Alt Çizgi|
|[dalgalı_ağır](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#WAVY_HEAVY)|Ağır Dalga Alt Çizgisi|
|` `[KELİMELER](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#WORDS)|Yalnızca Boşluk Olmayan Karakterlerin Altı Çizili|
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SettingFontUnderlineType-SettingFontUnderlineType.java" >}}



### **Yazı Tipi Rengini Ayarlama**
 ile yazı tipi rengini ayarlayın.[Yazı tipi](https://reference.aspose.com/cells/java/com.aspose.cells/Font) nesnenin[renk ayarla](https://reference.aspose.com/cells/java/com.aspose.cells/font#Color) Emlak. herhangi bir renk seçin[Renk](https://reference.aspose.com/cells/java/com.aspose.cells/Color) numaralandırın ve seçilen rengi[Yazı tipi](https://reference.aspose.com/cells/java/com.aspose.cells/Font) nesnenin[renk ayarla](https://reference.aspose.com/cells/java/com.aspose.cells/font#Color).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SetFontColor-SetFontColor.java" >}}



### **Metin Üzerinde Üstü Çizili Efekti Ayarlama**
 Üstü çizili metin ile[Yazı tipi](https://reference.aspose.com/cells/java/com.aspose.cells/Font) nesnenin[setStrikeout](https://reference.aspose.com/cells/java/com.aspose.cells/font#IsStrikeout)Emlak.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SettingStrikeOutEffect-SettingStrikeOutEffect.java" >}}



### **Aboneliği Ayarlama**
 Kullanarak metni üst simge yapın[Yazı tipi](https://reference.aspose.com/cells/java/com.aspose.cells/Font) nesnenin[setSubscript](https://reference.aspose.com/cells/java/com.aspose.cells/font#IsSubscript)Emlak.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SetSubscript-SetSubscript.java" >}}



### **Ayar Üst Simgesi**
 ile metne üst simge uygula[Yazı tipi](https://reference.aspose.com/cells/java/com.aspose.cells/Font) nesnenin[setSuperscript](https://reference.aspose.com/cells/java/com.aspose.cells/font#IsSuperscript)Emlak.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SetSuperscript-SetSuperscript.java" >}}

## **ileri konular**
- [Yazı Tiplerine Üst Simge ve Alt Simge Efektleri Uygulayın](/cells/tr/java/apply-superscript-and-subscript-effects-on-fonts/)
- [Elektronik Tablo veya Çalışma Kitabında kullanılan Yazı Tiplerinin Listesini Alın](/cells/tr/java/get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook/)
