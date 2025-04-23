---
title: Font Ayarları
description: Aspose.Cells, tablo dosyalarıyla çalışmak için Python kitaplığıdır. Hücrelerin yazı tipi ayarlarını belirlemeyi destekler ve kullanıcıların hücrelerin yazı tipi stil ve özelliklerini özelleştirmesine olanak tanır. Bu makale, Aspose.Cells for Python via .NET kitaplığını kullanarak hücre yazı tipi ayarlarını nasıl yapacağınızı tanıtacaktır.
keywords: Aspose.Cells for Python via .NET, Hücreler, Yazı Tipi Ayarları, Stiller, Özellikler
type: docs
weight: 30
url: /tr/python-net/cells-font-settings/
---

{{% alert color="primary" %}}

Bir metnin görünüm ve hissiyatı, yazı tipi ayarlarını değiştirerek kontrol edilebilir. Yazı tipi ayarları, isim, stil, boyut, renk ve diğer efektleri içerebilir. Microsoft Excel gibi, Aspose.Cells for Python via .NET de hücrelerin yazı tipi ayarlarını yapılandırmayı destekler.

{{% /alert %}}

## **Font Ayarlarını Yapılandırma**

Aspose.Cells for Python via .NET, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) sınıfı ile bir Microsoft Excel dosyasını temsil eder. [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) sınıfı, bir Excel dosyasındaki her çalışma sayfasına erişim sağlayan bir [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets) koleksiyonunu içerir. Bir çalışma sayfası, [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) sınıfı ile temsil edilir. [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) sınıfı, bir [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells) koleksiyonu sağlar. [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/) koleksiyonundaki her öğe, bir [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell) sınıfı nesnesini temsil eder.

Aspose.Cells, [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell) sınıfının [**get_style**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_style) ve [**set_style**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/set_style) yöntemlerini sağlar; bu yöntemler bir hücrenin biçimlendirme stiline getirilip alınmasında kullanılır. [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) sınıfı, font ayarlarını yapılandırmak için özellikler sağlar.

### **Yazı Tipi Adını Ayarlama**

Geliştiriciler herhangi bir fontu, [**Style.font**](https://reference.aspose.com/cells/python-net/aspose.cells/style/font) nesnesinin [**name**](https://reference.aspose.com/cells/python-net/aspose.cells/font/name/) özelliğini kullanarak hücre içeriğine uygulayabilir.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-SettingFontName-1.py" >}}

### **Yazı Tipi Stilini Kalın Yapma**

Geliştiriciler, metni kalın yapmak için [**Style.font**](https://reference.aspose.com/cells/python-net/aspose.cells/style/font) nesnesinin [**is_bold**](https://reference.aspose.com/cells/python-net/aspose.cells/font/is_bold) özelliğini **true** olarak ayarlayarak yapabilirler.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-SetFontStyle.py" >}}

### **Yazı Tipi Boyutunu Ayarlama**

[**Style.font**](https://reference.aspose.com/cells/python-net/aspose.cells/style/font) nesnesinin [**size**](https://reference.aspose.com/cells/python-net/aspose.cells/font/size) özelliği ile yazı tipi boyutunu ayarlayın.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-SetFontSize.py" >}}

### **Yazı Tipi Rengini Ayarlama**

[**Style.font**](https://reference.aspose.com/cells/python-net/aspose.cells/style/font) nesnesinin [**color**](https://reference.aspose.com/cells/python-net/aspose.cells/font/color) özelliğini kullanarak yazı tipi rengini ayarlayın. Renk numaralandırmasından ( .NET framework'ün bir parçası) herhangi bir rengi seçin ve [**color**](https://reference.aspose.com/cells/python-net/aspose.cells/font/color) özelliğine atayın.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-SetFontColor.py" >}}

### **Yazı Tipi Altı Çizgi Türünü Ayarlama**

Metni altı çizili yapmak için [**Style.font**](https://reference.aspose.com/cells/python-net/aspose.cells/style/font) nesnesinin [**underline**](https://reference.aspose.com/cells/python-net/aspose.cells/font/underline) özelliğini kullanın. Aspose.Cells for Python via .NET çeşitli ön tanımlı altı çizili türleri [**FontUnderlineType**](https://reference.aspose.com/cells/python-net/aspose.cells/fontunderlinetype) enumunda sunar.

|**Yazı Tipi Altı Çizgi Tipleri**|**Açıklama**|
| :- | :- |
|DİKEY HESAPLAMA|Tek altı çizgi|
|ÇİFT|Çift altı çizgi|
|İKİ DİZİ|İki hesaplama alt çizgisi|
|YOK|Alt çizgi yok|
|TEK|Tek alt çizgi|

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-SettingFontUnderlineType-1.py" >}}

### **Üstü Çizili Etkiyi Ayarlama**

Üstü çizili uygulamak için [**Style.font**](https://reference.aspose.com/cells/python-net/aspose.cells/style/font) nesnesinin [**is_strikeout**](https://reference.aspose.com/cells/python-net/aspose.cells/font/is_strikeout) özelliğini **true** olarak ayarlayın.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-SetStrikeout.py" >}}

### **Üst Simge Etkisini Ayarlama**

Abone simgesini ayarlayarak [**Style.font**](https://reference.aspose.com/cells/python-net/aspose.cells/style/font) nesnesinin [**is_subscript**](https://reference.aspose.com/cells/python-net/aspose.cells/font/is_subscript/) özelliğini **true** olarak ayarlayın.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-SetSubscript.py" >}}

### **Yazı Tipi Üzerine Üst Simge Efekti Ayarlama**

Geliştiriciler, yazı tipi üzerine üst simge efektini [**is_superscript**](https://reference.aspose.com/cells/python-net/aspose.cells/font/is_superscript) öğesinin [**Style.font**](https://reference.aspose.com/cells/python-net/aspose.cells/style/font) özelliğini **true** olarak ayarlayarak uygulayabilirler.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-SetSuperscript.py" >}}

## **Gelişmiş Konular**
- [Yazı Tipi Üzerine Üst Simge ve Abone Etkileri Uygulama](/cells/tr/python-net/apply-superscript-and-subscript-effects-on-fonts/)
- [Bir Elektronik Tablo veya Çalışma Kitabında Kullanılan Yazı Tiplerinin Listesini Alın](/cells/tr/python-net/get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook/)


