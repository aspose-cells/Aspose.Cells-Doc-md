---
title: Excel'i PDF'e Oluştururken Hataları Yoksay
type: docs
weight: 80
url: /tr/python-net/ignore-errors-while-rendering-excel-to-pdf/
description: Aspose.Cells for Python via .NET API ile Excel'i PDF'e İşlerken Hataları Nasıl Yoksayacağınızı öğrenin.
keywords: Python Ignore Errors while Rendering Excel to PDF, Ignore Errors while saving Excel to PDF using Python, Python Ignore Errors while converting Excel to PDF, Ignore Errors for Excel to PDF in python
---
##  **Olası Kullanım Senaryoları**

 Bazen Excel dosyanızı PDF'e dönüştürdüğünüzde hatalar veya istisnalar meydana gelir ve dönüştürme işlemi sona erer. Dönüştürme işlemi sırasında bu tür hataların tamamını göz ardı edebilirsiniz.[**PdfSaveOptions.ignore_error**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/ignore_error/)mülk. Bu sayede herhangi bir hata veya istisna atmadan dönüştürme işlemi sorunsuz bir şekilde tamamlanacaktır ancak veri kaybı yaşanabilir. Bu nedenle lütfen bu özelliği yalnızca veri kaybının sizin için kritik olmadığı durumlarda kullanın.

##  **Excel'i PDF'e Oluştururken Hataları Yoksay**

 Aşağıdaki kod şunu yükler:[örnek Excel dosyası](55541778.xlsx) ancak örnek Excel dosyası hatalı ve işlem sırasında hata veriyor[PDF'e dönüştürme](55541779.pdf) 17.11'de ancak kullandığımızdan beri[**PdfSaveOptions.ignore_error**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/ignore_error/)özelliği hata atmamaktadır. Ancak bir*yuvarlak kırmızı ok şekline benzer*bu ekran görüntüsünde gösterildiği gibi kaybolur.

![yapılacak şey:image_alt_text](ignore-errors-while-rendering-excel-to-pdf_1.png)

##  **Basit kod**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-IgnoreErrorsWhileRenderingExcelToPdf.py" >}}
