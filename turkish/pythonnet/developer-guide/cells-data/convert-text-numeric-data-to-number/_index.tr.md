---
title: Metin Sayısal Verileri Sayıya Dönüştür
type: docs
weight: 900
url: /tr/python-net/convert-text-numeric-data-to-number/
description: Aspose.Cells for Python via .NET API sını kullanarak Excel de metin olarak depolanan sayıları sayılara dönüştürmeyi öğrenin.
keywords: python excel metni sayıya dönüştür, python excel metni sayıya dönüştür, python excel metinsel sayısal veriyi sayıya dönüştür, python excel metinsel sayısal veriyi sayıya dönüştür, python excel sayısal metini sayıya dönüştür, python excel sayısal metini sayıya dönüştür, excel sayısal metni sayıya dönüştürme python ile, excel de sayısal metni sayıya dönüştürme python ile, excel de sayısal metni sayıya dönüştürme python ile, excel de sayısal dizeden sayıya dönüştürme python excel kütüphanesi, python excel metinsel sayısal veriyi sayıya dönüştür, python excel sayısal dizeden sayıya dönüştürme.
---

## **Olası Kullanım Senaryoları**
Bazı durumlarda, metin olarak girilen sayısal verileri sayıya dönüştürmek isteyebilirsiniz. Bir sayıyı metin olarak Microsoft Excel'e girerek, örneğin **'12345**. Excel daha sonra sayıyı bir dize olarak işler. Aspose.Cells for Python via .NET, metinleri sayılara dönüştürmenizi sağlar.


## **Excel'de metin olarak depolanan sayıları sayılara dönüştürme**
Birkaç basit adımı izleyerek metin olarak depolanan sayıları sayılara dönüştürebilirsiniz.
1. Sol üst köşede bir hata göstergesi bulunan herhangi bir tek hücre veya hücre aralığını seçin.
1. Seçili hücre veya hücre aralığının yanına, ortaya çıkan hata düğmesine tıklayın. Menüde, Sayıya Dönüştür üzerine tıklayın. 
<br>
<img src="4.png" width=70% />
1. Uyarı düğmesi kullanılabilir değilse, Bu sorunu yaşayan bir sütun seçin. Tüm sütunu dönüştürmek istemiyorsanız, bunun yerine bir veya daha fazla hücre seçebilirsiniz. Seçtiğiniz hücrelerin aynı sütunda olduğundan emin olun, aksi halde bu işlem çalışmaz. Bir sütunu bölme için genellikle Metin Bölme düğmesi kullanılır, ancak aynı zamanda bir sütun metnini sayılara dönüştürmek için de kullanılabilir. Veri sekmesinde, Metin Bölme'ye tıklayın.
<br>
<img src="1.png" width=70% />
1. Açılır pencerede Tamam düğmesine tıklayın.
<br>
<img src="2.png" width=70% />
1. Metin olarak depolanan sayılar sayılara dönüştürülür.
<br>
<img src="3.png" width=70% />

## **Python Excel Kütüphanesi Aspose.Cells ile Metin Olarak Depolanan Sayıları Sayılara Nasıl Dönüştürülür**
Aspose.Cells for Python via .NET, tüm dize veya metin sayısal verilerini sayılara dönüştürmek için kullanılabilecek olan [**Cells.convert_string_to_numeric_value()**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/convert_string_to_numeric_value/) yöntemini sağlar.

Aşağıdaki ekran görüntüsü, hücrelerdeki string sayıları **A1:A17** göstermektedir. Dize sayıları sola hizalanmıştır.
<br>
<img src="5.png" width=70% />

Bu string sayılar aşağıdaki ekran görüntüsünde [**Cells.convert_string_to_numeric_value()**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/convert_string_to_numeric_value/) kullanılarak sayılara dönüştürülmüştür. Görebileceğiniz gibi, şimdi sağa hizalanmış durumdadırlar.
<br>
<img src="6.png" width=70% />

## **Dize sayısal verileri gerçek sayılara dönüştürmek için Python kodu**

Aşağıdaki örnek kod, tüm çalışma sayfalarındaki dize sayısal verileri gerçek sayılara dönüştürmenin nasıl yapıldığını göstermektedir.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-ConvertStringToNumericValue-ConvertTextNumericDatatoNumber.py" >}}
{{< app/cells/assistant language="python-net" >}}
