---
title: Doldurma Ayarları
description: Aspose.Cells, çalışma sayfası dosyalarıyla çalışmak için kullanılan bir Python kütüphanesidir. Hücrelerin dolgu ayarlarını belirlemenize olanak tanır, böylece kullanıcılar hücrelerin arka planını ve stilini özelleştirebilir. Bu makale, Aspose.Cells for Python via .NET kütüphanesini kullanarak hücre dolgu ayarlarının nasıl ayarlanacağını tanıtacaktır.
keywords: Aspose.Cells for Python via .NET, Hücreler, Dolgu Ayarları, Arka Plan, Stil
type: docs
weight: 50
url: /tr/python-net/cells-fill-settings/
---

## **Renkler ve Arka Plan Desenleri**

Microsoft Excel, hücrelerin ön plan (çerçeve) ve arka plan (doldurma) renklerini ve arka plan desenlerini ayarlayabilir.

Aspose.Cells for Python via .NET, bu özellikleri esnek bir biçimde destekler. Bu konuda, bu özellikleri Aspose.Cells kullanarak nasıl kullanacağınızı öğreneceğiz.

### **Renkler ve Arka Plan Desenlerini Ayarlama**

Aspose.Cells for Python via .NET, Microsoft Excel dosyasını temsil eden [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) adlı bir sınıf sağlar. [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) sınıfı, Excel dosyasındaki her çalışma sayfasına erişim sağlayan bir [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets) koleksiyonu içerir. Bir çalışma sayfası, [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) sınıfı ile temsil edilir. [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) sınıfı, bir [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) koleksiyonu sağlar. [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) koleksiyonundaki her öğe, bir [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell) sınıfı nesnesini temsil eder.

[**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell) sınıfı, [**get_style**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_style) ve [**set_style**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/set_style) yöntemlerine sahiptir; bunlar, bir hücrenin biçimlendirmesini almak ve ayarlamak için kullanılır. [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) sınıfı, hücrelerin ön plan ve arka plan renklerini ayarlamak için özellikler sağlar. Aspose.Cells for Python via .NET, aşağıda listelenen önceden tanımlı arka plan desenleri seti içeren [**BackgroundType**](https://reference.aspose.com/cells/python-net/aspose.cells/backgroundtype) adında bir enumerasyon sağlar.

|**Arka Plan Desenleri**|**Açıklama**|
| :- | :- |
|DIAGONAL_CROSSHATCH|Diagonal çapraz çizgili deseni temsil eder|
|DIAGONAL_STRIPE|Diagonal çizgi deseni temsil eder|
|GRAY6|%6,25 gri deseni temsil eder|
|GRAY12|%12,5 gri deseni temsil eder|
|GRAY25|%25 gri deseni temsil eder|
|GRAY50|%50 gri deseni temsil eder|
|GRAY75|%75 gri deseni temsil eder|
|YATAY ÇİZGİ|Yatay şerit desenini temsil eder|
|YOK|Arka plan yok|
|TERS DİKİŞLİ ÇİZGİ|Ters çapraz çizgi desenini temsil eder|
|DÜZ|Katı desenleri temsil eder|
|KOYUŞA DİKİŞLİ ÇİZGİ|Kalın çapraz dikiş deseni|
|İnce DİKİŞLİ ÇİZGİ|İnce çapraz dikiş deseni|
|İNCE DİKİŞLİ ÇİZGİ|İnce çapraz şerit deseni|
|İnce YATAY ÇAPRAZ|İnce yatay çapraz desen|
|İnce YATAY ÇİZGİ|İnce yatay şerit deseni|
|İnce TERS DİKİŞLİ ÇİZGİ|İnce ters çapraz şerit deseni|
|İnce DİKEN|İnce dikey çizgi deseni|
|DÜZ DİZİ|Dikey şerit deseni|

Aşağıdaki örnekte, A1 hücresinin ön plan rengi ayarlanmış ancak A2, dikey çizgili bir arka plan deseni olan hem ön plan rengi hem de arka plan rengi olarak yapılandırılmıştır.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ColorsAndBackground-1.py" >}}

### **Bilinmesi Gerekenler**

{{% alert color="primary" %}}

- Bir hücrenin ön plan veya arka plan rengini ayarlamak için, [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) nesnesinin [**foreground_color**](https://reference.aspose.com/cells/python-net/aspose.cells/style/foreground_color) veya [**background_color**](https://reference.aspose.com/cells/python-net/aspose.cells/style/background_color) özelliklerini kullanın. Her iki özellik de, [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) nesnesinin [**pattern**](https://reference.aspose.com/cells/python-net/aspose.cells/style/pattern) özelliği yapılandırılmışsa yalnızca etki eder.
- [**foreground_color**](https://reference.aspose.com/cells/python-net/aspose.cells/style/foreground_color) özelliği hücrenin gölge rengini belirler.
   [**pattern**](https://reference.aspose.com/cells/python-net/aspose.cells/style/pattern) özelliği, ön veya arkaba renginde kullanılan arka plan deseni türünü belirtir. Aspose.Cells for Python via .NET önceden tanımlanmış arka plan desenleri kümesini içeren [**BackgroundType**](https://reference.aspose.com/cells/python-net/aspose.cells/backgroundtype) adlı bir enum sağlar.
- Eğer [**BackgroundType**](https://reference.aspose.com/cells/python-net/aspose.cells/backgroundtype) numaralandırmasından *BackgroundType.None* değerini seçerseniz, ön plan rengi uygulanmaz.
  Benzer şekilde, *BackgroundType.None* veya *BackgroundType.Solid* değerlerini seçerseniz arka plan rengi uygulanmaz.
- Hücrenin gölgelendirme/dolgu rengini alırken, [**Style.pattern**](https://reference.aspose.com/cells/python-net/aspose.cells/style/pattern) *BackgroundType.None* ise, [**Style.foreground_color**](https://reference.aspose.com/cells/python-net/aspose.cells/style/foreground_color) *Color.Empty* değerini döndürecektir.

{{% /alert %}}

### **Gradyan Dolgu Efektleri Uygulama**

Hücreye istenilen Gradyan Dolgu Efektlerini uygulamak için, [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) nesnesinin [**set_two_color_gradient**](https://reference.aspose.com/cells/python-net/aspose.cells/style/set_two_color_gradient) metodunu kullanın.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ApplyingGradientFillEffects-1.py" >}}

## **Renkler ve Palet**

Bir palet, bir görüntü oluşturmak için kullanılabilen renk sayısıdır. Bir sunumda standart bir palet kullanımı, kullanıcının tutarlı bir görünüm oluşturmasına olanak tanır. Her Microsoft Excel (97-2003) dosyasının bir hücrelere, fontlara, ızgaralara, grafik nesnelerine, doldurmalara ve çizgilere uygulanabilen 56 renklik bir paleti vardır.

Aspose.Cells for Python via .NET ile mevcut paletin renkleri kullanılabildiği gibi, özel renkler de kullanılabilir. Bir özel renk kullanmadan önce onu palete ekleyin.

Bu konu, paletine özel renkler eklemenin nasıl yapıldığını tartışmaktadır.

### **Paletine Özel Renkler Eklemek**

Aspose.Cells for Python via .NET, Microsoft Excel'in 56 renk paletini destekler. Paletede tanımlı olmayan bir özel renk kullanmak için, renk paletine ekleyin.

Aspose.Cells for Python via .NET, bir Microsoft Excel dosyasını temsil eden {0} adında bir sınıf sağlar. {1} sınıfı, bir Excel dosyasındaki her çalışma sayfasına erişim sağlayan {2} koleksiyonunu içerir. Bir çalışma sayfası, {3} sınıfı ile temsil edilir. {4} sınıfı ise bir {5} koleksiyonu sağlar. {6} koleksiyondaki her öğe, bir {7} sınıfı nesnesini temsil eder.

- Özel Renk, paletine eklenecek özel renk.
- İndeks, özel rengin paletindeki rengin yerini belirtir. 0-55 arasında olmalıdır.

Aşağıdaki örnek, (Orkide) özel bir rengi paletine ekleyip bunu bir font üzerine uygulamadan önce paletine ekler.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ColorsAndPalette-1.py" >}}

{{% alert color="primary" %}}

Palet sadece 56 renk tutar. Bir özel rengi paletine eklediğinizde, palet değişir ve önceki rengiyle biçimlendirilen dosyadaki her eleman değişir. Bu nedenle, paleti değiştirirken lütfen çok dikkatli olun. Dahası, bu sadece XLS (Excel 97 - 2003) dosya biçiminde bir kısıtlama olarak mevcuttur, XLSX veya diğer gelişmiş MS Excel (2007/2010 veya 2013) dosya biçimleri için böyle bir kısıtlama yoktur.

{{% /alert %}}

