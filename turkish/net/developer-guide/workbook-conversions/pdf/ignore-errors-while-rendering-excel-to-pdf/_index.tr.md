---
title: Excel'i PDF'e Dönüştürürken Hataları Yoksay
type: docs
weight: 80
url: /tr/net/ignore-errors-while-rendering-excel-to-pdf/
---
## **Olası Kullanım Senaryoları**

 Bazen Excel dosyanızı PDF'ye dönüştürdüğünüzde hatalar veya istisnalar oluşur ve dönüştürme işlemi sona erer. Dönüştürme işlemi sırasında bu tür tüm hataları,[**PdfSaveOptions.IgnoreError**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/ignoreerror)Emlak. Bu sayede dönüştürme işlemi herhangi bir hata veya istisna atmadan sorunsuz bir şekilde tamamlanır ancak veri kaybı meydana gelebilir. Bu nedenle, lütfen bu özelliği yalnızca veri kaybı sizin için kritik değilse kullanın.

## **Excel'i PDF'e Dönüştürürken Hataları Yoksay**

 Aşağıdaki kod,[örnek excel dosyası](55541778.xlsx) ancak örnek Excel dosyası hatalı ve işlem sırasında bir hata veriyor.[PDF'ye dönüştürme](55541779.pdf) 17.11'de ama kullandığımızdan beri[**PdfSaveOptions.IgnoreError**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/ignoreerror)özellik, bir hata atmaz. Ancak, bir*şekli gibi yuvarlak kırmızı ok*bu ekran görüntüsünde gösterildiği gibi kaybolur.

![yapılacaklar:resim_alternatif_Metin](ignore-errors-while-rendering-excel-to-pdf_1.png)

## **Basit kod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Rendering-IgnoreErrorsWhileRenderingExcelToPdf.cs" >}}
