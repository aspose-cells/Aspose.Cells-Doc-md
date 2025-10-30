---
title: Golang ile C++ kullanarak Excel i PDF ye dönüştürürken Hataları Görmezden Gel
linktitle: Excel i PDF olarak dönüştürürken Hataları Yoksay
type: docs
weight: 80
url: /tr/go-cpp/ignore-errors-while-rendering-excel-to-pdf/
description: Aspose.Cells for C++ kullanarak Excel den PDF ye dönüştürürken hataları nasıl yoksayacağınızı öğrenin.
---

## **Olası Kullanım Senaryoları**

 Bazen, Excel dosyanızı PDF'ye dönüştürürken hatalar veya istisnalar meydana gelir ve dönüşüm işlemi durur. Bu hataları göz ardı etmek için [**PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)**](https://reference.aspose.com/cells/go-cpp/paginatedsaveoptions/~paginatedsaveoptions/) özelliğini kullanabilirsiniz. Bu şekilde, dönüşüm sorunsuz tamamlanır ve hata veya istisna atmaz, ancak veri kaybı olabilir. Bu nedenle, veri kaybı sizin için kritik değilse, sadece bu özelliği kullanın.

## **Excel'den PDF'e Dönüştürme Sırasında Hataları Yoksay**

 Aşağıdaki kod, [örnek Excel dosyasını](55541778.xlsx) yükler, ancak bu Excel dosyası hatalıdır ve [PDF'ye dönüştürme](55541779.pdf) sırasında 17.11'de bir hata verir. Ancak, [**PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)**](https://reference.aspose.com/cells/go-cpp/paginatedsaveoptions/~paginatedsaveoptions/) özelliği kullanıldığından hata vermez. Ancak, bu ekran görüntüsünde gösterilen *yuvarlanan kırmızı ok şeklinde* bir şekil kaybolur.

![todo:image_alt_text](ignore-errors-while-rendering-excel-to-pdf_1.png)

## **Örnek Kod**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-IgnoreErrorsWhileRenderingExcelToPdf.go" >}}
