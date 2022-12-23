---
title: Excel'i PDF Olarak İşlerken Hataları Yoksay
type: docs
weight: 70
url: /tr/java/ignore-errors-while-rendering-excel-to-pdf/
---
## **Olası Kullanım Senaryoları**

Bazen Excel dosyanızı PDF'e dönüştürdüğünüzde hatalar veya istisnalar oluşur ve dönüştürme işlemi sona erer. kullanarak dönüştürme işlemi sırasında tüm bu tür hataları yok sayabilirsiniz.[**PdfSaveOptions.IgnoreError**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#IgnoreError)Emlak. Bu sayede dönüştürme işlemi herhangi bir hata veya istisna atmadan sorunsuz bir şekilde tamamlanır ancak veri kaybı meydana gelebilir. Bu nedenle, lütfen bu özelliği yalnızca veri kaybı sizin için kritik değilse kullanın.

## **Excel'i PDF Olarak İşlerken Hataları Yoksay**

Aşağıdaki kod,[örnek excel dosyası](55541813.xlsx)ancak örnek Excel dosyası hatalı ve işlem sırasında bir hata veriyor.[PDF'e dönüştürme](55541814.pdf)17.11'de ama kullandığımızdan beri[**PdfSaveOptions.IgnoreError**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#IgnoreError)özellik, bir hata atmaz. Ancak, bu ekran görüntüsünde gösterilen yuvarlak kırmızı ok benzeri bir şekil kaybolmuştur.

![yapılacaklar:resim_alternatif_metin](ignore-errors-while-rendering-excel-to-pdf_1.png)

## **Basit kod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Rendering-IgnoreErrorsWhileRenderingExcelToPdf.java" >}}
