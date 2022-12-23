---
title: WorkbookSetting.StreamProvider kullanarak Harici Kaynakları Kontrol Edin
type: docs
weight: 10
url: /tr/net/control-external-resources-using-workbooksetting-streamprovider/
---
## **Olası Kullanım Senaryoları**

Bazen, Excel dosyanız bağlantılı resimler vb. gibi harici kaynaklar içerir. Aspose.Cells, bu harici kaynakları kullanarak kontrol etmenize olanak tanır.[**Workbook.Settings.StreamProvider**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/streamprovider)uygulanmasını gerektiren[**IStream Sağlayıcı**](https://reference.aspose.com/cells/net/aspose.cells/istreamprovider)arayüz. Bağlantılı resimler gibi harici kaynaklar içeren çalışma sayfanızı ne zaman oluşturmaya çalışsanız,[**IStream Sağlayıcı**](https://reference.aspose.com/cells/net/aspose.cells/istreamprovider)dış kaynaklarınız için uygun eylemleri gerçekleştirmenizi sağlayacak arayüz çağrılacaktır.

## **WorkbookSetting.StreamProvider kullanarak Harici Kaynakları Kontrol Edin**

Aşağıdaki örnek kod,[**Workbook.Settings.StreamProvider**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/streamprovider) . o yükler[örnek excel dosyası](61767863.xlsx) bağlantılı bir resim içerir. Kod, bağlantılı resmi şu şekilde değiştirir:[Aspose logosu](61767862.png) kullanarak tüm sayfayı tek bir görüntüye dönüştürür.[**SheetRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender) sınıf. Aşağıdaki ekran görüntüsü, örnek Excel dosyasını ve[işlenmiş çıktı görüntüsü](61767865.png) referans için Gördüğünüz gibi kopuk bağlantılı resim Aspose Logosu ile değiştirilmiştir.

![yapılacaklar:resim_alternatif_metin](control-external-resources-using-workbooksetting-streamprovider_1.png)

## **Basit kod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-WorkbookSettings-ControlExternalResourcesUsingWorkbookSetting_StreamProvider-1.cs" >}}
