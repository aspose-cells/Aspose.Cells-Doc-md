---
title: Metin Sayısal Verileri Sayıya Dönüştür
type: docs
weight: 150
url: /tr/java/convert-text-numeric-data-to-number/
description: Aspose.Cells for Java API yı kullanarak metin olarak depolanan sayıları sayılara dönüştürmeyi öğrenin.
keywords: excel metni sayıya çevir, excel metni sayıya çevir java, excel metin sayısal veriyi sayıya dönüştür, excel metin sayısal veriyi sayıya dönüştür java, excel sayısal metni sayıya dönüştür, excel sayısal metni sayıya dönüştür java, excel sayısal metni sayıya dönüştürme java ile, excelde sayısal metni sayıya dönüştürme java ile, excelde sayısal metni sayıya dönüştürme java ile, excelde sayısal dizesi sayıya dönüştür, excel metin sayısal veriyi sayıya dönüştür java, excelde sayısal dizesi sayıya dönüştürme java ile
---

## **Olası Kullanım Senaryoları**
Ara sıra, metin olarak girilmiş sayısal verileri sayılara dönüştürmek isteyebilirsiniz. Microsoft Excel'de sayıları metin olarak girebilirsiniz, örneğin **'12345**. Excel, ardından sayıyı bir dize olarak işler. Aspose.Cells, dizeleri sayılara dönüştürmenize olanak sağlar.


Excel'de metin olarak depolanan sayıları sayılara dönüştürme
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

## Aspose.Cells ile metin olarak depolanan sayıları sayılara dönüştürme
Aspose.Cells for Java API, tüm metin veya metin sayısal verilerini sayılara dönüştürmek için kullanılabilecek [**Cells.convertStringToNumericValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#convertStringToNumericValue--) yöntemini sağlar.

Aşağıdaki ekran görüntüsü, hücrelerdeki string sayıları **A1:A17** göstermektedir. Dize sayıları sola hizalanmıştır.
<br>
<img src="5.png" width=70% />

Bu string sayılar aşağıdaki ekran görüntüsünde [**Cells.convertStringToNumericValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#convertStringToNumericValue--) kullanılarak sayılara dönüştürülmüştür. Görebileceğiniz gibi, şimdi sağa hizalanmış durumdadırlar.
<br>
<img src="6.png" width=70% />

## Dize sayısal verileri gerçek sayılara dönüştürmek için Java kodu
Aşağıdaki örnek kod, tüm çalışma sayfalarındaki dize sayısal verileri gerçek sayılara dönüştürmenin nasıl yapıldığını göstermektedir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ConvertTextNumericDatatoNumber-ConvertTextNumericDatatoNumber.java" >}}
{{< app/cells/assistant language="java" >}}
