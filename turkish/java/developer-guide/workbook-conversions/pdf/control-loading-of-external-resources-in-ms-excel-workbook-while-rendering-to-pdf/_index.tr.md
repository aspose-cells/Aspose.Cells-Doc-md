---
title: MS Excel Çalışma Kitabının PDF ye dönüştürülürken Harici Kaynakların Yüklenmesini Kontrol Etme
type: docs
weight: 40
url: /tr/java/control-loading-of-external-resources-in-ms-excel-workbook-while-rendering-to-pdf/
---

## **Olası Kullanım Senaryoları**

Excel dosyanız harici kaynaklar içerebilir, örneğin bağlı resimler veya nesneler. Excel dosyanızı PDF'e dönüştürdüğünüzde, Aspose.Cells bu harici kaynakları alır ve bunları PDF'e dönüştürür. Ancak bazen bu harici kaynakları yüklemek istemeyebilirsiniz ve daha da önemlisi, bunları yönetmek isteyebilirsiniz. Bunun için [**PdfSaveOptions.StreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#StreamProvider) kullanabilirsiniz ve [**IStreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/IStreamProvider) arayüzünü uygular.

## **MS Excel Çalışma Kitabında Harici Kaynakların Yüklenmesine Kontrol Etmek**

Aşağıdaki örnek kod, harici kaynakların yüklenmesini kontrol etmek ve bunları manipüle etmek için [**PdfSaveOptions.StreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#StreamProvider) nasıl kullanılacağını açıklar. Kod içinde kullanılan [örnek Excel dosyasını](50528353.xlsx) ve kod tarafından üretilen [çıktı PDF'sini](50528354.pdf) kontrol edin. [Ekran görüntüsü](50528357.png) old external image(50528356.png) örnek Excel dosyasında nasıl yeni bir görüntü olan [new image](50528355.png) ile değiştirildiğini gösterir.

![todo:image_alt_text](control-loading-of-external-resources-in-ms-excel-workbook-while-rendering-to-pdf_1.png)

## **Örnek Kod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Rendering-ControlLoadingOfExternalResourcesInExcelToPDF.java" >}}
