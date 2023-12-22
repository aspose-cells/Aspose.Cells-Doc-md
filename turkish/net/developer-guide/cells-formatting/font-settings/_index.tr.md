---
title: Yazı Tipi Ayarları
description: Aspose.Cells, elektronik tablo dosyalarıyla çalışmaya yönelik bir .NET kitaplığıdır. Hücrelerin yazı tipi ayarlarının belirlenmesini destekleyerek kullanıcıların yazı tipi stilini ve hücrelerin özelliklerini özelleştirmesine olanak tanır. Bu makale, hücre yazı tipi ayarlarını yapmak için Aspose.Cells kitaplığının nasıl kullanılacağını tanıtacaktır.
keywords: Aspose.Cells, Cells, Font Settings, Styles, Properties
type: docs
weight: 30
url: /tr/net/cells-font-settings/
---
{{% alert color="primary" %}}

Bir metnin görünümü ve hissi, yazı tipi ayarları değiştirilerek kontrol edilebilir. Yazı tipi ayarları yazı tiplerinin adını, stilini, boyutunu, rengini ve diğer efektlerini içerebilir. Tıpkı Microsoft Excel gibi Aspose.Cells de hücrelerin yazı tipi ayarlarının yapılandırılmasını destekler.

{{% /alert %}}

##  **Yazı Tipi Ayarlarını Yapılandırma**

 Aspose.Cells bir sınıf sağlar,[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook) bu bir Microsoft Excel dosyasını temsil eder.[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sınıf bir içerir[**Çalışma sayfaları**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)Bir Excel dosyasındaki her çalışma sayfasına erişime izin veren koleksiyon. Bir çalışma sayfası şu şekilde temsil edilir:[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıf.[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıf sağlar[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) Toplamak. İçindeki her öğe[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) koleksiyon bir nesneyi temsil eder[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)sınıf.

 Aspose.Cells şunları sağlar[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)sınıf'[**GetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle) Ve[**SetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle) Bir hücrenin biçimlendirme stilini almak ve ayarlamak için kullanılan yöntemler.[**Stil**](https://reference.aspose.com/cells/net/aspose.cells/style)sınıf yazı tipi ayarlarını yapılandırmak için özellikler sağlar.

###  **Yazı Tipi Adını Ayarlama**

 Geliştiriciler, herhangi bir yazı tipini kullanarak hücre içindeki metne uygulayabilir.[**Stil.Yazı Tipi**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font) nesnenin[İsim](https://reference.aspose.com/cells/net/aspose.cells/font/properties/name)mülk.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontName-1.cs" >}}

###  **Yazı Tipi Stilini Kalın Olarak Ayarlama**

 Geliştiriciler metni kalınlaştırabilir.[**Stil.Yazı Tipi**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font) nesnenin[**Kalın**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/isbold)özelliği *true** olarak değiştirin.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontStyle-SetFontStyle.cs" >}}

###  **Yazı Tipi Boyutunun Ayarlanması**

Yazı tipi boyutunu şununla ayarlayın:[**Stil.Yazı Tipi**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font)nesnenin[**Boyut**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/size)mülk.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontSize-SetFontSize.cs" >}}

###  **Yazı Tipi Rengini Ayarlama**

Kullan[**Stil.Yazı Tipi**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font) nesnenin[**Renk**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/color)Yazı tipi rengini ayarlama özelliği. Renk numaralandırmasından (.NET çerçevesinin bir parçası) herhangi bir rengi seçin ve bunu[**Renk**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/color)mülk.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontColor-SetFontColor.cs" >}}

###  **Yazı Tipi Altı Çizili Türünü Ayarlama**

Kullan[**Stil.Yazı Tipi**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font)nesnenin[**Altını çizmek**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/underline)Metnin altını çizme özelliği. Aspose.Cells, önceden tanımlanmış çeşitli yazı tipi alt çizgi türlerini sunar.[**FontUnderlineType**](https://reference.aspose.com/cells/net/aspose.cells/fontunderlinetype) numaralandırma.

|**Yazı Tipi Altı Çizili Türleri**|**Tanım**|
| :- | :- |
|Muhasebe|Tek bir muhasebenin altı çizili|
|Çift|Çift alt çizgi|
|Çift Muhasebe|Çift muhasebenin altı çizili|
|Hiçbiri|Alt çizgi yok|
|Bekar|Tek bir alt çizgi|

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontUnderlineType-1.cs" >}}

###  **Üstü Çizilme Efektini Ayarlama**

Ayarlayarak üstü çizili uygulayın[**Stil.Yazı Tipi**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font) nesnenin[**Üstü çizili**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/isstrikeout)özelliği *true** olarak değiştirin.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingStrikeOutEffect-SetStrikeout.cs" >}}

###  **Abonelik Efektini Ayarlama**

ayarlayarak alt simgeyi uygulayın[**Stil.Yazı Tipi**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font)nesnenin[**IsSubScript**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/issubscript)özelliği *true** olarak değiştirin.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingSubScriptEffect-SetSubscript.cs" >}}

###  **Yazı Tipi Üzerinde Üst Simge Efektini Ayarlama**

 Geliştiriciler, üst simge efektini yazı tipine uygulayabilir.[**Üst simge**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/issuperscript) mülkiyeti[**Stil.Yazı Tipi**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font)*doğruya** itiraz edin.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingSuperScriptEffect-SetSuperscript.cs" >}}

##  **İleri konular**
- [Yazı Tiplerine Üst Simge ve Alt Simge Efektleri Uygulama](/cells/tr/net/apply-superscript-and-subscript-effects-on-fonts/)
- [Bir Elektronik Tabloda veya Çalışma Kitabında kullanılan Yazı Tiplerinin Listesini Alma](/cells/tr/net/get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook/)

