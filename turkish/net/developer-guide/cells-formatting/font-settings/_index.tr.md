---
title: Yazı Tipi Ayarları
type: docs
weight: 30
url: /tr/net/cells-font-settings/
---
{{% alert color="primary" %}}

Bir metnin görünümü ve verdiği his, yazı tipi ayarları değiştirilerek kontrol edilebilir. Yazı tipi ayarları, yazı tiplerinin adını, stilini, boyutunu, rengini ve diğer efektlerini içerebilir. Tıpkı Microsoft Excel gibi, Aspose.Cells de hücrelerin yazı tipi ayarlarını yapılandırmayı destekler.

{{% /alert %}}

## **Yazı Tipi Ayarlarını Yapılandırma**

 Aspose.Cells bir sınıf sağlar,[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook) bu bir Microsoft Excel dosyasını temsil eder. bu[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sınıf bir içerir[**çalışma sayfaları**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) bir Excel dosyasındaki her çalışma sayfasına erişim sağlayan koleksiyon. Bir çalışma sayfası şununla temsil edilir:[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıf. bu[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıf bir sağlar[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) Toplamak. İçindeki her öğe[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) koleksiyon bir nesneyi temsil eder[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)sınıf.

 Aspose.Cells şunları sağlar:[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) sınıf'[**Stil Al**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle) ve[**SetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle) bir hücrenin biçimlendirme stilini almak ve ayarlamak için kullanılan yöntemler. bu[**stil**](https://reference.aspose.com/cells/net/aspose.cells/style)class, yazı tipi ayarlarını yapılandırmak için özellikler sağlar.

### **Yazı Tipi Adını Ayarlama**

 Geliştiriciler, kullanarak herhangi bir yazı tipini bir hücre içindeki metne uygulayabilir.[**Stil.Yazı Tipi**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font) nesnenin[İsim](https://reference.aspose.com/cells/net/aspose.cells/font/properties/name)Emlak.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontName-1.cs" >}}

### **Yazı Tipi Stilini Kalın Olarak Ayarlama**

 Geliştiriciler,[**Stil.Yazı Tipi**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font) nesnenin[**Kalın mı**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/isbold) mülkiyet**doğru**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontStyle-SetFontStyle.cs" >}}

### **Yazı Tipi Boyutunu Ayarlama**

ile yazı tipi boyutunu ayarlayın.[**Stil.Yazı Tipi**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font)nesnenin[**Boyut**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/size)Emlak.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontSize-SetFontSize.cs" >}}

### **Yazı Tipi Rengini Ayarlama**

Kullan[**Stil.Yazı Tipi**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font) nesnenin[**Renk**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/color)yazı tipi rengini ayarlama özelliği. Renk numaralandırmasından (.NET çerçevesinin bir parçası) herhangi bir rengi seçin ve onu[**Renk**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/color)Emlak.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontColor-SetFontColor.cs" >}}

### **Yazı Tipi Altı Çizili Tipini Ayarlama**

Kullan[**Stil.Yazı Tipi**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font)nesnenin[**Altını çizmek**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/underline)metnin altını çizme özelliği. Aspose.Cells, önceden tanımlanmış çeşitli alt çizgili yazı tipleri sunar.[**FontUnderlineType**](https://reference.aspose.com/cells/net/aspose.cells/fontunderlinetype) numaralandırma.

|**Alt Çizgi Tipleri**|**Tanım**|
|:- |:- |
|Muhasebe|Tek bir muhasebe alt çizgisi|
|Çift|Çift alt çizgi|
|Çift Muhasebe|Çift hesap altı çizili|
|Hiçbiri|Alt çizgi yok|
|Bekar|Tek bir alt çizgi|

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontUnderlineType-1.cs" >}}

### **Üstü Çizili Efekti Ayarlama**

Ayarlayarak üstü çizili uygula[**Stil.Yazı Tipi**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font) nesnenin[**Üstü çizili mi**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/isstrikeout)mülkiyet**doğru**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingStrikeOutEffect-SetStrikeout.cs" >}}

### **Abonelik Etkisini Ayarlama**

ayarlayarak alt simgeyi uygula[**Stil.Yazı Tipi**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font)nesnenin[**IsSubScript**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/issubscript) mülkiyet**doğru**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingSubScriptEffect-SetSubscript.cs" >}}

### **Yazı Tipinde Üst Simge Efekti Ayarlama**

 Geliştiriciler, üst simge efektini yazı tipine ayarlayarak uygulayabilir.[**üst simge**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/issuperscript) mülkiyeti[**Stil.Yazı Tipi**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font) itiraz etmek**doğru**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingSuperScriptEffect-SetSuperscript.cs" >}}

## **ileri konular**
- [Yazı Tiplerine Üst Simge ve Alt Simge Efektleri Uygulayın](/cells/tr/net/apply-superscript-and-subscript-effects-on-fonts/)
- [Elektronik Tablo veya Çalışma Kitabında kullanılan Yazı Tiplerinin Listesini Alın](/cells/tr/net/get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook/)

