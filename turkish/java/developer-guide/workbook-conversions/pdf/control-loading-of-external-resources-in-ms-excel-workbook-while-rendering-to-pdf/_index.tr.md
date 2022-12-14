---
title: PDF'ye dönüştürürken MS Excel Çalışma Kitabında Dış Kaynakların yüklenmesini kontrol edin
type: docs
weight: 40
url: /tr/java/control-loading-of-external-resources-in-ms-excel-workbook-while-rendering-to-pdf/
---
## **Olası Kullanım Senaryoları**

Excel dosyanız, bağlantılı resimler veya nesneler gibi harici kaynaklar içerebilir. Excel dosyanızı PDF'ye dönüştürdüğünüzde, Aspose.Cells bu harici kaynakları alır ve PDF'e dönüştürür. Ancak bazen bu dış kaynakları yüklemek istemezsiniz ve bundan daha fazlası onları manipüle etmek istersiniz. Bunu kullanarak yapabilirsiniz[**PdfSaveOptions.StreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#StreamProvider)hangi uygular[**IStream Sağlayıcı**](https://reference.aspose.com/cells/java/com.aspose.cells/IStreamProvider)arayüz.

## **PDF'ye dönüştürürken MS Excel Çalışma Kitabında Dış Kaynakların yüklenmesini kontrol edin**

Aşağıdaki örnek kod, nasıl kullanılacağını açıklar[**PdfSaveOptions.StreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#StreamProvider)dış kaynakların yüklenmesini kontrol etmek ve bunları manipüle etmek. lütfen kontrol ediniz[örnek excel dosyası](50528353.xlsx)kodun içinde kullanılır ve[çıktı PDF](50528354.pdf)kod tarafından oluşturulur. bu[ekran görüntüsü](50528357.png)nasıl olduğunu gösterir[eski dış görüntü](50528356.png)örnek Excel dosyasında bir ile değiştirildi[yeni görüntü](50528355.png)çıktı PDF'sinde.

![yapılacaklar:resim_alternatif_Metin](control-loading-of-external-resources-in-ms-excel-workbook-while-rendering-to-pdf_1.png)

## **Basit kod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Rendering-ControlLoadingOfExternalResourcesInExcelToPDF.java" >}}
