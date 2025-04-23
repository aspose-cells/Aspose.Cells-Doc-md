---
title: Metin Sayısal Verileri Sayıya Dönüştür
type: docs
weight: 900
url: /tr/nodejs-cpp/convert-text-numeric-data-to-number/
description: Excel de metin olarak saklanan sayıları sayılara nasıl dönüştüreceğinizi öğrenmek için Aspose.Cells for Node.js via C++ API sini kullanın.
keywords: excel metni sayıya dönüştür, excel metni sayıya dönüştür Node js kodu, excel metin sayısal veriyi sayıya dönüştür, excel metin sayısal veriyi sayıya dönüştür Node js kodu, excel sayısal metni sayıya dönüştür, excel sayısal metni sayıya dönüştür Node js kodu, excel sayısal metni sayıya dönüştür Node js kodu ile, excel de sayısal metni sayıya dönüştür, excel de sayısal metni sayıya dönüştür Node js kodu ile, excel de sayısal dizgiyi sayıya dönüştürün Node js kodu ile, excel de metin sayısal veriyi sayıya dönüştürmek Node js kodu ile
---

## **Olası Kullanım Senaryoları**
Bazen, metin olarak girilen sayısal verileri sayıya dönüştürmek isteyebilirsiniz. Microsoft Excel'de sayıları metin olarak girmek için, sayının önüne bir kesme işareti koyabilirsiniz, örneğin **'12345**. Excel, sayıyı bir dizi olarak işler. Aspose.Cells for Node.js via C++, dizeleri sayılara dönüştürmenize olanak sağlar.


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

## Aspose.Cells for Node.js via C++ kullanarak metin olarak saklanan sayıları sayıya dönüştürme
Aspose.Cells for Node.js via C++, tüm dizgi veya metin sayısal verileri sayıya dönüştürmek için kullanılabilecek [**Cells.convertStringToNumericValue()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#convertStringToNumericValue--) yöntemini sağlar.

Aşağıdaki ekran görüntüsü, hücrelerdeki string sayıları **A1:A17** göstermektedir. Dize sayıları sola hizalanmıştır.
<br>
<img src="5.png" width=70% />

Bu string sayılar aşağıdaki ekran görüntüsünde [**Cells.convertStringToNumericValue()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#convertStringToNumericValue--) kullanılarak sayılara dönüştürülmüştür. Görebileceğiniz gibi, şimdi sağa hizalanmış durumdadırlar.
<br>
<img src="6.png" width=70% />

## Dize sayılarını gerçek sayılara dönüştürmek için Node.js kodu

Aşağıdaki örnek kod, tüm çalışma sayfalarındaki dize sayısal verileri gerçek sayılara dönüştürmenin nasıl yapıldığını göstermektedir.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-ConvertTextNumericDatatoNumber.js" >}}
