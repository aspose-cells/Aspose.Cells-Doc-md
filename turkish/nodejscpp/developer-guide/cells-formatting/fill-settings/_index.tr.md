---  
title: Doldurma Ayarları
linktitle: Doldurma Ayarları  
description: Node.js kullanarak Aspose.Cells kütüphanesi ile hücreleri doldurma ayarları, arka plan ve stil nasıl özelleştirilir öğrenin.  
keywords: Aspose.Cells, Cells, Doldurma Ayarları, Arka Plan, Stil, Node.js C++ üzerinden  
type: docs  
weight: 50  
url: /tr/nodejs-cpp/cells-fill-settings/  
---  

## **Renkler ve Arka Plan Desenleri**  

Microsoft Excel, hücrelerin ön plan (çerçeve) ve arka plan (doldurma) renklerini ve arka plan desenlerini ayarlayabilir.  

Aspose.Cells, bu özellikleri esnek bir şekilde destekler. Bu konuda, Aspose.Cells kullanarak bu özellikleri nasıl kullanacağımızı öğreneceğiz.  

### **Renkler ve Arka Plan Desenlerini Ayarlama**  

Aspose.Cells, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) sınıfını sağlar; bu, bir Microsoft Excel dosyasını temsil eder. [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) sınıfı, Excel dosyasındaki her sayfaya erişimi sağlayan [**Worksheets**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) koleksiyonunu içerir. Bir çalışma sayfası, [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) sınıfı ile temsil edilir. [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) sınıfı, [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) koleksiyonunu sağlar. [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) koleksiyonundaki her öğe [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell) sınıfının bir nesnesini temsil eder.  

[**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell) sınıfının [**getStyle**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getStyle--) ve [**setStyle**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setStyle-style-) metodları, hücrenin biçimlendirmesini almak ve ayarlamak için kullanılır. [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) sınıfı, hücrelerin ön plan ve arka plan renklerini ayarlamak için özellikler sağlar. Aspose.Cells, aşağıda verilen önceden tanımlanmış arka plan desenleri kümesini içeren [**BackgroundType**](https://reference.aspose.com/cells/nodejs-cpp/backgroundtype) adlı bir enum sağlar.  

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

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-FillSettings-SetColorsAndBackgroundPatterns.js" >}}


### **Bilinmesi Gerekenler**  

{{% alert color="primary" %}}  

- Bir hücrenin ön plan veya arka plan rengini ayarlamak için [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) nesnesinin [**setForegroundColor**](https://reference.aspose.com/cells/nodejs-cpp/style/#setForegroundColor-color-) veya [**setBackgroundColor**](https://reference.aspose.com/cells/nodejs-cpp/style/#setBackgroundColor-color-) metodlarını kullanın. Her iki metod, [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) nesnesinin [**Pattern**](https://reference.aspose.com/cells/nodejs-cpp/style/#setPattern-backgroundtype-) özelliği yapılandırılmışsa etkili olur.  
- [**setForegroundColor**](https://reference.aspose.com/cells/nodejs-cpp/style/#setForegroundColor-color-) metodu, hücrenin gölge rengini belirler.  
  [**setPattern**](https://reference.aspose.com/cells/nodejs-cpp/style/#setPattern-backgroundtype-) metodu, ön plan veya arka plan rengi için kullanılan arka plan deseninin türünü belirtir. Aspose.Cells, önceden tanımlanmış arka plan desenleri kümesini içeren [**BackgroundType**](https://reference.aspose.com/cells/nodejs-cpp/backgroundtype) adlı bir enum sağlar.  
- Eğer [**BackgroundType**](https://reference.aspose.com/cells/nodejs-cpp/backgroundtype) enumundan *BackgroundType.None* değeri seçerseniz, ön plan rengi uygulanmaz.  
  Benzer şekilde, *BackgroundType.None* veya *BackgroundType.Solid* değerlerini seçerseniz arka plan rengi uygulanmaz.  
- Hücrenin gölgelendirme/dolgu rengini alırken, [**Style.setPattern**](https://reference.aspose.com/cells/nodejs-cpp/style/#setPattern-backgroundtype-) *BackgroundType.None* ise, [**Style.getForegroundColor**](https://reference.aspose.com/cells/nodejs-cpp/style/#getForegroundColor--) *Color.Empty* değerini döndürecektir.  

{{% /alert %}}  

### **Gradyan Dolgu Efektleri Uygulama**  

Hücreye istediğiniz Gradyan Dolgu Efektlerini uygulamak için, uygun şekilde [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) nesnesinin [**setTwoColorGradient**](https://reference.aspose.com/cells/nodejs-cpp/style/#setTwoColorGradient-color-color-gradientstyletype-number-) metodunu kullanın.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-FillSettings-ApplyGradientFillEffects.js" >}}


## **Renkler ve Palet**  

Bir palet, bir görüntü oluşturmak için kullanılabilen renk sayısıdır. Bir sunumda standart bir palet kullanımı, kullanıcının tutarlı bir görünüm oluşturmasına olanak tanır. Her Microsoft Excel (97-2003) dosyasının bir hücrelere, fontlara, ızgaralara, grafik nesnelerine, doldurmalara ve çizgilere uygulanabilen 56 renklik bir paleti vardır.  

Aspose.Cells ile sadece paletin mevcut renklerini değil aynı zamanda özel renkleri de kullanmak mümkündür. Özel bir rengi kullanmadan önce, önce paletine ekleyin.  

Bu konu, paletine özel renkler eklemenin nasıl yapıldığını tartışmaktadır.  

### **Paletine Özel Renkler Eklemek**  

Aspose.Cells, Microsoft Excel'in 56 renkli paletini destekler. Paletine tanımlanmamış özel bir renk kullanmak için, rengi paletine ekleyin.  

Aspose.Cells, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) adlı bir sınıf sağlar; bu, bir Microsoft Excel dosyasını temsil eder. [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) sınıfı, aşağıdaki parametreleri kullanarak paleti değiştirmek için özel bir renk eklemek amacıyla [**changePalette**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#changePalette-color-number-) metodunu sağlar:  

- Özel Renk, paletine eklenecek özel renk.  
- İndeks, özel rengin paletindeki rengin yerini belirtir. 0-55 arasında olmalıdır.  

Aşağıdaki örnek, (Orkide) özel bir rengi paletine ekleyip bunu bir font üzerine uygulamadan önce paletine ekler.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-FillSettings-AddCustomColorsToPalette.js" >}}


{{% alert color="primary" %}}  

Palet sadece 56 renk tutar. Bir özel rengi paletine eklediğinizde, palet değişir ve önceki rengiyle biçimlendirilen dosyadaki her eleman değişir. Bu nedenle, paleti değiştirirken lütfen çok dikkatli olun. Dahası, bu sadece XLS (Excel 97 - 2003) dosya biçiminde bir kısıtlama olarak mevcuttur, XLSX veya diğer gelişmiş MS Excel (2007/2010 veya 2013) dosya biçimleri için böyle bir kısıtlama yoktur.  

{{% /alert %}}  

