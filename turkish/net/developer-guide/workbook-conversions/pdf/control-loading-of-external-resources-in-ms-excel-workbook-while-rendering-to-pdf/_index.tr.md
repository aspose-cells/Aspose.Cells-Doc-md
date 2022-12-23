---
title: PDF'e işlenirken MS Excel Çalışma Kitabında Dış Kaynakların yüklenmesini kontrol edin
type: docs
weight: 40
url: /tr/net/control-loading-of-external-resources-in-ms-excel-workbook-while-rendering-to-pdf/
---
## **Olası Kullanım Senaryoları**

Excel dosyanız, bağlantılı resimler veya nesneler gibi harici kaynaklar içerebilir. Excel dosyanızı PDF'e dönüştürdüğünüzde, Aspose.Cells bu harici kaynakları alır ve PDF'e dönüştürür. Ancak bazen bu harici kaynakları yüklemek istemezsiniz ve bundan daha fazlası, onları manipüle etmek istersiniz. Bunu kullanarak yapabilirsiniz[**WorkbookSettings.StreamProvider**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/streamprovider)hangi uygular[**IStream Sağlayıcı**](https://reference.aspose.com/cells/net/aspose.cells/istreamprovider)arayüz.

## **PDF'e işlenirken MS Excel Çalışma Kitabında Dış Kaynakların yüklenmesini kontrol edin**

 Aşağıdaki örnek kod, nasıl kullanılacağını açıklar[**WorkbookSettings.StreamProvider**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/streamprovider) dış kaynakların yüklenmesini kontrol etmek ve bunları manipüle etmek. lütfen kontrol ediniz[örnek excel dosyası](50528322.xlsx) kodun içinde kullanılır ve[çıkış PDF](50528325.pdf) kod tarafından oluşturulur. bu[ekran görüntüsü](50528326.png) nasıl olduğunu gösterir[eski dış görüntü](50528324.png) örnek Excel dosyasında bir ile değiştirildi[yeni görüntü](50528323.png) PDF çıktısında.

![yapılacaklar:resim_alternatif_metin](control-loading-of-external-resources-in-ms-excel-workbook-while-rendering-to-pdf_1.png)

## **Basit kod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Rendering-ControlLoadingOfExternalResourcesInExcelToPDF-1.cs" >}}
