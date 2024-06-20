---
title: Font Ayarları
description: Aspose.Cells, elektronik tablo dosyalarıyla çalışmak için bir .NET kitaplığıdır. Kullanıcılara hücrelerin font ayarlarını ayarlama olanağı sağlar. Bu makale, hücre font ayarlarını ayarlamak için Aspose.Cells kitaplığını nasıl kullanacağınızı tanıtacaktır.
keywords: Aspose.Cells, Hücreler, Font Ayarları, Stilleri, Özellikleri
type: docs
weight: 30
url: /tr/net/cells-font-settings/
---

{{% alert color="primary" %}}

Bir metnin görünümü, font ayarlarını değiştirerek kontrol edilebilir. Font ayarları, yazı tiplerinin adı, stili, boyutu, rengi ve diğer efektlerini içerebilir. Microsoft Excel gibi, Aspose.Cells de hücrelerin font ayarlarını yapılandırmayı destekler.

{{% /alert %}}

## **Font Ayarlarını Yapılandırma**

Aspose.Cells, bir Microsoft Excel dosyasını temsil eden [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) adlı bir sınıf sağlar. [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sınıfı, bir Microsoft Excel dosyasındaki her bir çalışma sayfasına erişim sağlayan bir [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) koleksiyonunu içerir. Bir çalışma sayfası, [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıfı tarafından temsil edilir. [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıfı bir [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) koleksiyonu sağlar. [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) koleksiyonundaki her öğe, [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) sınıfının bir nesnesini temsil eder.

Aspose.Cells, [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) sınıfının [**GetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle) ve [**SetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle) yöntemlerini sağlar; bu yöntemler bir hücrenin biçimlendirme stiline getirilip alınmasında kullanılır. [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) sınıfı, font ayarlarını yapılandırmak için özellikler sağlar.

### **Yazı Tipi Adını Ayarlama**

Geliştiriciler, [**Style.Font**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font) nesnesinin [Adı](https://reference.aspose.com/cells/net/aspose.cells/font/properties/name) özelliğini kullanarak bir hücre içindeki metne herhangi bir font uygulayabilirler.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontName-1.cs" >}}

### **Yazı Tipi Stilini Kalın Yapma**

Geliştiriciler, metni kalın yapmak için [**Style.Font**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font) nesnesinin [**IsBold**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/isbold) özelliğini **true** olarak ayarlayarak yapabilirler.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontStyle-SetFontStyle.cs" >}}

### **Yazı Tipi Boyutunu Ayarlama**

[**Style.Font**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font) nesnesinin [**Size**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/size) özelliği ile yazı tipi boyutunu ayarlayın.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontSize-SetFontSize.cs" >}}

### **Yazı Tipi Rengini Ayarlama**

[**Style.Font**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font) nesnesinin [**Color**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/color) özelliğini kullanarak yazı tipi rengini ayarlayın. Renk numaralandırmasından ( .NET framework'ün bir parçası) herhangi bir rengi seçin ve [**Color**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/color) özelliğine atayın.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontColor-SetFontColor.cs" >}}

### **Yazı Tipi Altı Çizgi Türünü Ayarlama**

[**Style.Font**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font) nesnesinin [**Underline**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/underline) özelliğini kullanarak metni altı çizili yapın. Aspose.Cells, [**FontUnderlineType**](https://reference.aspose.com/cells/net/aspose.cells/fontunderlinetype) numaralandırmasında çeşitli önceden tanımlanmış yazı tipi altı çizgi tipleri sunar.

|**Yazı Tipi Altı Çizgi Tipleri**|**Açıklama**|
| :- | :- |
|Accounting|Tek hesap çizgisi|
|Double|Çift çizgi|
|DoubleAccounting|Çift hesap çizgisi|
|None|Çizgi yok|
|Single|Tek çizgi|

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontUnderlineType-1.cs" >}}

### **Üstü Çizili Etkiyi Ayarlama**

Üstü çizili uygulamak için [**Style.Font**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font) nesnesinin [**IsStrikeout**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/isstrikeout) özelliğini **true** olarak ayarlayın.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingStrikeOutEffect-SetStrikeout.cs" >}}

### **Üst Simge Etkisini Ayarlama**

Abone simgesini ayarlayarak [**Style.Font**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font) nesnesinin [**IsSubScript**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/issubscript) özelliğini **true** olarak ayarlayın.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingSubScriptEffect-SetSubscript.cs" >}}

### **Yazı Tipi Üzerine Üst Simge Efekti Ayarlama**

Geliştiriciler, yazı tipi üzerine üst simge efektini [**IsSuperscript**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/issuperscript) öğesinin [**Style.Font**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font) özelliğini **true** olarak ayarlayarak uygulayabilirler.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingSuperScriptEffect-SetSuperscript.cs" >}}

## **Gelişmiş Konular**
- [Yazı Tipi Üzerine Üst Simge ve Abone Etkileri Uygulama](/cells/tr/net/apply-superscript-and-subscript-effects-on-fonts/)
- [Bir Elektronik Tablo veya Çalışma Kitabında Kullanılan Yazı Tiplerinin Listesini Alın](/cells/tr/net/get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook/)

