---
title: WorkbookSetting.StreamProvider kullanarak Harici Kaynakları Kontrol Edin
type: docs
weight: 10
url: /tr/java/control-external-resources-using-workbooksetting-streamprovider/
---
## **Olası Kullanım Senaryoları**
Bazen, Excel dosyanız bağlantılı resimler vb. gibi harici kaynaklar içerir. Aspose.Cells, bu harici kaynakları kullanarak kontrol etmenize olanak tanır.[Workbook.Settings.StreamProvider](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#StreamProvider)uygulanmasını gerektiren[IStream Sağlayıcı](https://reference.aspose.com/cells/java/com.aspose.cells/IStreamProvider)arayüz. Bağlantılı resimler gibi harici kaynaklar içeren çalışma sayfanızı oluşturmaya çalıştığınızda,[IStream Sağlayıcı](https://reference.aspose.com/cells/java/com.aspose.cells/IStreamProvider)dış kaynaklarınız için uygun eylemleri gerçekleştirmenizi sağlayacak arayüz çağrılacaktır.
## **WorkbookSetting.StreamProvider kullanarak Harici Kaynakları Kontrol Edin**
Aşağıdaki örnek kod, kullanımını açıklar[Workbook.Settings.StreamProvider](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#StreamProvider). o yükler[örnek excel dosyası](61767877.xlsx)bağlantılı bir resim içerir. Kod, bağlantılı resmi şu şekilde değiştirir:[Aspose logosu](61767874.png)kullanarak tüm sayfayı tek bir görüntüye dönüştürür.[SheetRender](https://reference.aspose.com/cells/java/com.aspose.cells/SheetRender)sınıf. Aşağıdaki ekran görüntüsü, örnek Excel dosyasını ve[işlenmiş çıktı görüntüsü](61767874.png)referans için Gördüğünüz gibi kopuk bağlantılı resim Aspose Logosu ile değiştirilmiştir.

![yapılacaklar:resim_alternatif_Metin](control-external-resources-using-workbooksetting-streamprovider_1.png)
## **Basit kod**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-WorkbookSettings-ControlExternalResourcesUsingWorkbookSetting_StreamProvider-1.java" >}}
