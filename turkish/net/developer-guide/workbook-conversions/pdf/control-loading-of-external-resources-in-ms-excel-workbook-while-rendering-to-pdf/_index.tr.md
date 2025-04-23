---
title: MS Excel Çalışma Kitabının PDF ye dönüştürülürken Harici Kaynakların Yüklenmesini Kontrol Etme
type: docs
weight: 40
url: /tr/net/control-loading-of-external-resources-in-ms-excel-workbook-while-rendering-to-pdf/
---

## **Olası Kullanım Senaryoları**

Excel dosyanız bağlantılı resimler veya nesneler içerebilir. Excel dosyanızı PDF'ye dönüştürdüğünüzde, Aspose.Cells bu harici kaynakları alır ve bunları PDF'ye döker. Ancak bazen bu harici kaynakları yüklemek istemezsiniz ve daha da fazlası, onları manipüle etmek istersiniz. Bu, [**WorkbookSettings.StreamProvider**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/streamprovider) kullanarak yapılabilir. [**IStreamProvider**](https://reference.aspose.com/cells/net/aspose.cells/istreamprovider) arayüzünü uygular.

## **MS Excel Çalışma Kitabında Harici Kaynakların Yüklenmesine Kontrol Etmek**

Aşağıdaki örnek kod, harici kaynakların yüklenmesini kontrol etmek ve bunları manipüle etmek için [**WorkbookSettings.StreamProvider**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/streamprovider) kullanımını açıklar. Lütfen kod içinde kullanılan [örnek Excel dosyasına](50528322.xlsx) ve kod tarafından oluşturulan [çıktı PDF'sine](50528325.pdf) bakın. [Ekran görüntüsü](50528326.png), [örnekteki eski harici görüntünün](50528324.png) çıktı PDF'de bir [yeni görüntü](50528323.png) ile nasıl değiştirildiğini göstermektedir.

![todo:image_alt_text](control-loading-of-external-resources-in-ms-excel-workbook-while-rendering-to-pdf_1.png)

## **Örnek Kod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Rendering-ControlLoadingOfExternalResourcesInExcelToPDF-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
