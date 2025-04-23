---
title: Doldurma Ayarları
description: Aspose.Cells, elektronik tablo dosyaları ile çalışmak için bir .NET kitaplığıdır. Hücrelerin doldurma ayarlarını ayarlama özelliğini destekler, böylece kullanıcılar hücrelerin arka planını ve stilini özelleştirebilir. Bu makalede, Aspose.Cells kitaplığını kullanarak hücre doldurma ayarlarını nasıl ayarlayacağımızı öğreneceğiz.
keywords: Aspose.Cells, Hücreler, Doldurma Ayarları, Arka Plan, Stil
type: docs
weight: 50
url: /tr/net/cells-fill-settings/
---

## **Renkler ve Arka Plan Desenleri**

Microsoft Excel, hücrelerin ön plan (çerçeve) ve arka plan (doldurma) renklerini ve arka plan desenlerini ayarlayabilir.

Aspose.Cells, bu özellikleri esnek bir şekilde destekler. Bu konuda, Aspose.Cells kullanarak bu özellikleri nasıl kullanacağımızı öğreneceğiz.

### **Renkler ve Arka Plan Desenlerini Ayarlama**

Aspose.Cells, Microsoft Excel dosyasını temsil eden bir sınıf olan [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sunar. [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sınıfı, Excel dosyasındaki her bir çalışma sayfasına erişim sağlayan bir koleksiyon içerir. Bir çalışma sayfası [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) sınıfı tarafından temsil edilir. [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıfı, bir koleksiyon sağlar. [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıfı, bir koleksiyon sağlar. [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) koleksiyonundaki her öğe, [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) sınıfının bir nesnesini temsil eder.

[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell), hücre biçimlendirme işlemlerini almak ve ayarlamak için kullanılan [**GetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle/index) ve [**SetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle/index) metodlarına sahiptir. [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) sınıfı, hücrelerin ön plan ve arka plan renklerini ayarlamak için özellikler sağlar. Aspose.Cells, aşağıda verilen önceden tanımlanmış arka plan desenlerini içeren bir [**BackgroundType**](https://reference.aspose.com/cells/net/aspose.cells/backgroundtype) numaralı sıralı koleksiyon sağlar.

|**Arka Plan Desenleri**|**Açıklama**|
| :- | :- |
|DiagonalCrosshatch|Çapraz çizgili deseni temsil eder|
|DiagonalStripe|Çapraz şerit deseni temsil eder|
|Gray6|%6,25 gri deseni temsil eder|
|Gray12|%12,5 gri deseni temsil eder|
|Gray25|%25 gri deseni temsil eder|
|Gray50|%50 gri deseni temsil eder|
|Gray75|%75 gri deseni temsil eder|
|HorizontalStripe|Dikey şerit deseni temsil eder|
|None|Arka plan yok|
|ReverseDiagonalStripe|Çapraz ters şerit deseni temsil eder|
|Solid|Düz deseni temsil eder|
|ThickDiagonalCrosshatch|Kalın çapraz çizgili deseni temsil eder|
|ThinDiagonalCrosshatch|İnce çapraz çizgili deseni temsil eder|
|ThinDiagonalStripe|İnce çapraz şerit deseni temsil eder|
|ThinHorizontalCrosshatch|İnce yatay çapraz çizgili deseni temsil eder|
|ThinHorizontalStripe|İnce yatay şerit deseni temsil eder|
|ThinReverseDiagonalStripe|İnce ters çapraz şerit deseni temsil eder|
|ThinVerticalStripe|İnce dikey şerit deseni temsil eder|
|VerticalStripe|Dikey şerit deseni temsil eder|

Aşağıdaki örnekte, A1 hücresinin ön plan rengi ayarlanmış ancak A2, dikey çizgili bir arka plan deseni olan hem ön plan rengi hem de arka plan rengi olarak yapılandırılmıştır.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ColorsAndBackground-1.cs" >}}

### **Bilinmesi Gerekenler**

{{% alert color="primary" %}}

- Bir hücrenin ön plan veya arka plan rengini ayarlamak için, [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) nesnesinin [**ForegroundColor**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/foregroundcolor) veya [**BackgroundColor**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/backgroundcolor) özelliklerini kullanın. Her iki özellik de, [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) nesnesinin [**Pattern**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/pattern) özelliği yapılandırılmışsa yalnızca etki eder.
- [**ForegroundColor**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/foregroundcolor) özelliği hücrenin gölge rengini belirler.
  [**Pattern**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/pattern) özelliği, önyüz veya arka plan rengi için kullanılan arka plan deseninin türünü belirtir. Aspose.Cells, bir dizi önceden tanımlanmış arka plan desenlerini içeren [**BackgroundType**](https://reference.aspose.com/cells/net/aspose.cells/backgroundtype) adlı bir numaralandırmayı sağlar.
- Eğer [**BackgroundType**](https://reference.aspose.com/cells/net/aspose.cells/backgroundtype) numaralandırmasından *BackgroundType.None* değerini seçerseniz, ön plan rengi uygulanmaz.
  Benzer şekilde, *BackgroundType.None* veya *BackgroundType.Solid* değerlerini seçerseniz arka plan rengi uygulanmaz.
- Hücrenin gölgelendirme/dolgu rengini alırken, [**Style.Pattern**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/pattern) *BackgroundType.None* ise, [**Style.ForegroundColor**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/foregroundcolor) *Color.Empty* değerini döndürecektir.

{{% /alert %}}

### **Gradyan Dolgu Efektleri Uygulama**

Hücreye istenilen Gradyan Dolgu Efektlerini uygulamak için, [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) nesnesinin [**SetTwoColorGradient**](https://reference.aspose.com/cells/net/aspose.cells/style/methods/settwocolorgradient) metodunu kullanın.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ApproachesToFormatData-ApplyingGradientFillEffects-1.cs" >}}

## **Renkler ve Palet**

Bir palet, bir görüntü oluşturmak için kullanılabilen renk sayısıdır. Bir sunumda standart bir palet kullanımı, kullanıcının tutarlı bir görünüm oluşturmasına olanak tanır. Her Microsoft Excel (97-2003) dosyasının bir hücrelere, fontlara, ızgaralara, grafik nesnelerine, doldurmalara ve çizgilere uygulanabilen 56 renklik bir paleti vardır.

Aspose.Cells ile sadece paletin mevcut renklerini değil aynı zamanda özel renkleri de kullanmak mümkündür. Özel bir rengi kullanmadan önce, önce paletine ekleyin.

Bu konu, paletine özel renkler eklemenin nasıl yapıldığını tartışmaktadır.

### **Paletine Özel Renkler Eklemek**

Aspose.Cells, Microsoft Excel'in 56 renkli paletini destekler. Paletine tanımlanmamış özel bir renk kullanmak için, rengi paletine ekleyin.

Aspose.Cells, bir Microsoft Excel dosyasını temsil eden [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sınıfını sağlar. [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sınıfı, paleti değiştirmek için özel bir renk eklemek için aşağıdaki parametreleri alan bir [**ChangePalette**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/changepalette) yöntemi sağlar:

- Özel Renk, paletine eklenecek özel renk.
- İndeks, özel rengin paletindeki rengin yerini belirtir. 0-55 arasında olmalıdır.

Aşağıdaki örnek, (Orkide) özel bir rengi paletine ekleyip bunu bir font üzerine uygulamadan önce paletine ekler.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ColorsAndPalette-1.cs" >}}

{{% alert color="primary" %}}

Palet sadece 56 renk tutar. Bir özel rengi paletine eklediğinizde, palet değişir ve önceki rengiyle biçimlendirilen dosyadaki her eleman değişir. Bu nedenle, paleti değiştirirken lütfen çok dikkatli olun. Dahası, bu sadece XLS (Excel 97 - 2003) dosya biçiminde bir kısıtlama olarak mevcuttur, XLSX veya diğer gelişmiş MS Excel (2007/2010 veya 2013) dosya biçimleri için böyle bir kısıtlama yoktur.

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
