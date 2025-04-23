---
title: Excel i PDF olarak dönüştürürken Hataları Yoksay
type: docs
weight: 80
url: /tr/net/ignore-errors-while-rendering-excel-to-pdf/
---

## **Olası Kullanım Senaryoları**

Excel dosyanızı PDF'e dönüştürdüğünüzde bazen hatalar veya istisnalar oluşur ve dönüşüm süreci sona erer. Bu tür tüm hataları dönüşüm süreci sırasında[**PdfSaveOptions.IgnoreError**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/ignoreerror) özelliğini kullanarak yok sayabilirsiniz. Bu şekilde, dönüşüm süreci herhangi bir hata veya istisna fırlatmadan düzgün bir şekilde tamamlanır, ancak veri kaybı olabilir. Bu nedenle, veri kaybı sizin için kritik değilse lütfen bu özelliği kullanın.

## **Excel'den PDF'e Dönüştürme Sırasında Hataları Yoksay**

Aşağıdaki kod, [örnek Excel dosyasını](55541778.xlsx) yükler ancak örnek Excel dosyası hatalıdır ve 17.11'de [PDF'ye dönüşüm sırasında](55541779.pdf) bir hata fırlatır, ancak biz[**PdfSaveOptions.IgnoreError**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/ignoreerror) özelliğini kullandığımızdan dolayı bir hata fırlatmaz. Bununla birlikte, bu ekran görüntüsünde gösterildiği gibi bir *yuvarlanmış kırmızı ok benzeri şekil* kaybolur.

![todo:image_alt_text](ignore-errors-while-rendering-excel-to-pdf_1.png)

## **Örnek Kod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Rendering-IgnoreErrorsWhileRenderingExcelToPdf.cs" >}}
{{< app/cells/assistant language="csharp" >}}
