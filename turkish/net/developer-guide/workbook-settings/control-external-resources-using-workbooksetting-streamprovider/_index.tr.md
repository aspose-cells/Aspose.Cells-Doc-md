---
title: WorkbookSetting.StreamProvider Kullanarak Harici Kaynakları Kontrol Etme
type: docs
weight: 10
url: /tr/net/control-external-resources-using-workbooksetting-streamprovider/
---

## **Olası Kullanım Senaryoları**

Bazen Excel dosyanız harici kaynaklar içerebilir, örneğin bağlantılı resimler vb. Aspose.Cells, [**Workbook.Settings.StreamProvider**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/streamprovider) kullanarak bu harici kaynakları kontrol etmenize izin verir ki bu, [**IStreamProvider**](https://reference.aspose.com/cells/net/aspose.cells/istreamprovider) arayüzünün uygulamasını alır. Eğer çalışma sayfasınız harici kaynaklar içeren bir resmi oluşturulduğunda, [**IStreamProvider**](https://reference.aspose.com/cells/net/aspose.cells/istreamprovider) arayüzünün yöntemleri tetiklenecek ve harici kaynaklarınıza uygun eylemleri gerçekleştirmenize olanak sağlayacaktır.

## **WorkbookSetting.StreamProvider Kullanarak Harici Kaynakları Kontrol Etme**

Aşağıdaki örnek kod, [**Workbook.Settings.StreamProvider**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/streamprovider) kullanımını açıklar. [Örnek Excel dosyasını](61767863.xlsx) içeren bağlantılı bir resim bulunmaktadır. Kod, bağlantılı resmi [Aspose Logosu](61767862.png) ile değiştirir ve [**SheetRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender) sınıfını kullanarak çalışma sayfasını tek bir resim haline getirir. Aşağıdaki ekran görüntüsü, örnek Excel dosyasını ve referans için [oluşturulmuş çıktı resmi](61767865.png)'ni göstermektedir. Bozuk bağlantılı resmi Aspose Logosu ile değiştirildiği gibi görünmektedir.

![todo:image_alt_text](control-external-resources-using-workbooksetting-streamprovider_1.png)

## **Örnek Kod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-WorkbookSettings-ControlExternalResourcesUsingWorkbookSetting_StreamProvider-1.cs" >}}
