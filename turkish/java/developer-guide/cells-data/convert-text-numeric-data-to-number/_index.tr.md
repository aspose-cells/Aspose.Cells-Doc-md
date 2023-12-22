---
title: Metin Sayısal Verilerini Sayıya Dönüştür
type: docs
weight: 150
url: /tr/java/convert-text-numeric-data-to-number/
description: Aspose.Cells for Java API'i kullanarak metin olarak saklanan sayıları sayılara nasıl dönüştüreceğinizi öğrenin.
keywords: excel convert text to number, excel convert text to number java, excel convert text numeric data to number, excel convert text numeric data to number java, excel convert numeric text to number, excel convert numeric text to number java, excel convert numeric text to number with java, convert numeric text to number in excel with java, convert numeric text to number in excel with java, convert numeric string to number in excel with java, excel convert text numeric data to number java, excel convert numeric string to number java
---
##  **Olası Kullanım Senaryoları**
Bazen metin olarak girilen sayısal verileri sayılara dönüştürmek istersiniz. Microsoft Excel'de sayıların önüne kesme işareti koyarak sayıları metin olarak girebilirsiniz, örneğin *'12345**. Excel daha sonra sayıyı bir dize olarak ele alır. Aspose.Cells, dizeleri sayılara dönüştürmenize olanak tanır.


## Metin olarak saklanan sayıları Excel'deki sayılara dönüştürün
Metin olarak saklanan sayıları birkaç basit adımı izleyerek sayılara dönüştürebilirsiniz.
1. Sol üst köşesinde hata göstergesi bulunan herhangi bir hücreyi veya hücre aralığını seçin.
1.  Seçilen hücrenin veya hücre aralığının yanında görünen hata düğmesini tıklayın. Menüde Numaraya Dönüştür'ü tıklayın.
<br>
<img src="4.png" width=70% />
1. Uyarı düğmesi kullanılamıyorsa bu sorunun olduğu bir sütunu seçin. Sütunun tamamını dönüştürmek istemiyorsanız bunun yerine bir veya daha fazla hücre seçebilirsiniz. Seçtiğiniz hücrelerin aynı sütunda olduğundan emin olun, aksi takdirde bu işlem çalışmayacaktır. Metni Sütunlara Dönüştür düğmesi genellikle bir sütunu bölmek için kullanılır, ancak tek bir metin sütununu sayılara dönüştürmek için de kullanılabilir. Veri sekmesinde Metni Sütunlara Dönüştür'e tıklayın.
<br>
<img src="1.png" width=70% />
1. Açılan kutudaki Son düğmesini tıklayın.
<br>
<img src="2.png" width=70% />
1. Metin olarak saklanan sayılar sayılara dönüştürülür.
<br>
<img src="3.png" width=70% />

##  JAVA için Aspose.Cells'i kullanarak metin olarak saklanan sayıları sayılara dönüştürün
Aspose.Cells for Java API şunları sağlar[**Cells.convertStringToNumericValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#convertStringToNumericValue()) tüm dize veya metin sayısal verilerini sayılara dönüştürmek için kullanılabilen yöntem.

Aşağıdaki ekran görüntüsü *A1:A17** hücrelerindeki dize numaralarını göstermektedir. Dize numaraları sola hizalanır.
<br>
<img src="5.png" width=70% />

 Bu dize numaraları kullanılarak sayılara dönüştürüldü.[**Cells.convertStringToNumericValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#convertStringToNumericValue()) aşağıdaki ekran görüntüsünde. Gördüğünüz gibi artık sağa hizalanmışlar.
<br>
<img src="6.png" width=70% />

##  Dize sayısal verilerini gerçek sayılara dönüştürmek için Java kodu
Aşağıdaki örnek kod, tüm çalışma sayfalarındaki tüm dize sayısal verilerinin gerçek sayılara nasıl dönüştürüleceğini gösterir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ConvertTextNumericDatatoNumber-ConvertTextNumericDatatoNumber.java" >}}
