---
title: Excel i PDF olarak dönüştürürken Hataları Yoksay
type: docs
weight: 80
url: /tr/python-net/ignore-errors-while-rendering-excel-to-pdf/
description: Aspose.Cells for Python via .NET API ile Excel den PDF ye Dönüştürme Sırasında Hataları Yoksaymayı Nasıl Öğrenirim
keywords: Python ile Excel den PDF ye Dönüştürme Sırasında Hataları Yoksay, Python kullanarak Excel den PDF ye Hataları Yoksayarak Kaydetme, Python ile Excel den PDF ye Dönüştürme Sırasında Hataları Yoksayma, Python da Excel den PDF ye Dönüştürme Sırasında Hataları Yoksayma
---

## **Olası Kullanım Senaryoları**

Excel dosyanızı PDF'e dönüştürdüğünüzde bazen hatalar veya istisnalar oluşur ve dönüşüm süreci sona erer. Bu tür tüm hataları dönüşüm süreci sırasında[**PdfSaveOptions.ignore_error**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/ignore_error/) özelliğini kullanarak yok sayabilirsiniz. Bu şekilde, dönüşüm süreci herhangi bir hata veya istisna fırlatmadan düzgün bir şekilde tamamlanır, ancak veri kaybı olabilir. Bu nedenle, veri kaybı sizin için kritik değilse lütfen bu özelliği kullanın.

## **Excel'den PDF'e Dönüştürme Sırasında Hataları Yoksay**

Aşağıdaki kod, [örnek Excel dosyasını](55541778.xlsx) yükler ancak örnek Excel dosyası hatalıdır ve 17.11'de [PDF'ye dönüşüm sırasında](55541779.pdf) bir hata fırlatır, ancak biz[**PdfSaveOptions.ignore_error**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/ignore_error/) özelliğini kullandığımızdan dolayı bir hata fırlatmaz. Bununla birlikte, bu ekran görüntüsünde gösterildiği gibi bir *yuvarlanmış kırmızı ok benzeri şekil* kaybolur.

![todo:image_alt_text](ignore-errors-while-rendering-excel-to-pdf_1.png)

## **Örnek Kod**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-IgnoreErrorsWhileRenderingExcelToPdf.py" >}}
{{< app/cells/assistant language="python-net" >}}
