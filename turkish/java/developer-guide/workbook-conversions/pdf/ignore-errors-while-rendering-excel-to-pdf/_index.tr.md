---
title: Excel i PDF olarak dönüştürürken Hataları Yoksay
type: docs
weight: 70
url: /tr/java/ignore-errors-while-rendering-excel-to-pdf/
---

## **Olası Kullanım Senaryoları**

Excel dosyanızı PDF'ye dönüştürdüğünüzde bazen hatalar veya istisnalar meydana gelir ve dönüşüm işlemi sona erer. Bu tür hataları dönüşüm süreci sırasında göz ardı edebilir ve [**PdfSaveOptions.IgnoreError**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#IgnoreError) özelliğini kullanabilirsiniz. Böylelikle, dönüşüm işlemi herhangi bir hata veya istisna fırlatmadan düzgün bir şekilde tamamlanır, ancak veri kaybı meydana gelebilir. Bu nedenle, veri kaybı sizin için kritik değilse lütfen yalnızca bu özelliği kullanın.

## **Excel'den PDF'e Dönüştürme Sırasında Hataları Yoksay**

Aşağıdaki kod, [örnek Excel dosyasını](55541813.xlsx) yükler, ancak örnek Excel dosyası hatalıdır ve 17.11 sürümünde [PDF'ye dönüştürme işleminde](55541814.pdf) bir hata fırlatır, ancak [**PdfSaveOptions.IgnoreError**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#IgnoreError) özelliğini kullandığımız için bir hata fırlatmaz. Ancak, bu ekran görüntüsünde gösterildiği gibi 17.11'de bir yuvarlak kırmızı ok benzeri şekil kaybolur.

![todo:image_alt_text](ignore-errors-while-rendering-excel-to-pdf_1.png)

## **Örnek Kod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Rendering-IgnoreErrorsWhileRenderingExcelToPdf.java" >}}
