---
title: Metin Sayısal Verileri Sayıya Dönüştür
type: docs
weight: 900
url: /tr/net/convert-text-numeric-data-to-number/
description: Excel de metin olarak depolanan sayıları Aspose.Cells for .NET API sini kullanarak sayılara dönüştürmeyi öğrenin.
keywords: excel metinden sayıya dönüştürme, excel metinden sayıya dönüştürme c#, excel metin sayısal verileri sayıya dönüştürme, excel metin sayısal verileri sayıya dönüştürme c#, excel sayısal metni sayıya dönüştürme, excel sayısal metni sayıya dönüştürme c#, excel sayısal metni sayıya dönüştürme c# ile, excelde sayısal metni sayıya dönüştürme, excelde sayısal metni sayıya dönüştürme c#, excelde sayısal dizesi sayıya dönüştürme c#, excel metin sayısal verileri sayıya dönüştürme c#, excel sayısal dizesi sayıya dönüştürme c#
---

## **Olası Kullanım Senaryoları**
Ara sıra, metin olarak girilmiş sayısal verileri sayılara dönüştürmek isteyebilirsiniz. Microsoft Excel'de sayıları metin olarak girebilirsiniz, örneğin **'12345**. Excel, ardından sayıyı bir dize olarak işler. Aspose.Cells, dizeleri sayılara dönüştürmenize olanak sağlar.


## Excel'de metin olarak depolanan sayıları sayılara dönüştürme
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

## Aspose.Cells for .NET Kullanarak Metin olarak depolanan sayıları sayılara dönüştürme
Aspose.Cells, tüm dize veya metin sayısal verilerini sayılara dönüştürmek için kullanılabilecek [**Cells.ConvertStringToNumericValue()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/convertstringtonumericvalue) yöntemini sağlar.

Aşağıdaki ekran görüntüsü, hücrelerdeki string sayıları **A1:A17** göstermektedir. Dize sayıları sola hizalanmıştır.
<br>
<img src="5.png" width=70% />

Bu string sayılar aşağıdaki ekran görüntüsünde [**Cells.ConvertStringToNumericValue()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/convertstringtonumericvalue) kullanılarak sayılara dönüştürülmüştür. Görebileceğiniz gibi, şimdi sağa hizalanmış durumdadırlar.
<br>
<img src="6.png" width=70% />

## Gerçek Sayılara Dönüştürmek İçin C# Kodu

Aşağıdaki örnek kod, tüm çalışma sayfalarındaki dize sayısal verileri gerçek sayılara dönüştürmenin nasıl yapıldığını göstermektedir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-StylingAndDataFormatting-ConvertStringToNumericValue-ConvertTextNumericDatatoNumber.cs" >}}
{{< app/cells/assistant language="csharp" >}}
