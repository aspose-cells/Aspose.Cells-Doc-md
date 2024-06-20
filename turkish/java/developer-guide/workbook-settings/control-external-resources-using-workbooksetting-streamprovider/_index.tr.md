---
title: WorkbookSetting.StreamProvider Kullanarak Harici Kaynakları Kontrol Etme
type: docs
weight: 10
url: /tr/java/control-external-resources-using-workbooksetting-streamprovider/
---

## **Olası Kullanım Senaryoları**
Bazen, Excel dosyanız harici kaynaklar içerir, ör. bağlantılı resimler. Aspose.Cells, [Workbook.Settings.StreamProvider](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#StreamProvider) kullanarak bu harici kaynakları kontrol etmenize olanak tanır, [IStreamProvider](https://reference.aspose.com/cells/java/com.aspose.cells/IStreamProvider) arabiriminin uygulamasını alır. Harici kaynak içeren çalışsayınızı oluşturmaya çalıştığınızda, ör. bağlantılı resimler, [IStreamProvider](https://reference.aspose.com/cells/java/com.aspose.cells/IStreamProvider) arabirimine ait yöntemler çağrılacak ve harici kaynaklarınız için uygun adımları atmanıza olanak tanıyacaktır.
## **WorkbookSetting.StreamProvider Kullanarak Harici Kaynakları Kontrol Etme**
Aşağıdaki örnek kod, [Workbook.Settings.StreamProvider](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#StreamProvider) kullanımını açıklar. Bağlantılı bir resim içeren [örnek Excel dosyasını](61767877.xlsx) yükler. Kod, bağlantılı resmi [Aspose Logosu ile](61767874.png) değiştirir ve tüm sayfayı tek bir resim olarak [SheetRender](https://reference.aspose.com/cells/java/com.aspose.cells/SheetRender) sınıfını kullanarak render eder. Aşağıdaki ekran görüntüsü, örnek Excel dosyasını ve bir referans için [render edilmiş çıktı resmini](61767874.png) gösterir. Görebileceğiniz gibi, bozuk bağlantılı resim, Aspose Logosu ile değiştirilmiştir.

![todo:image_alt_text](control-external-resources-using-workbooksetting-streamprovider_1.png)
## **Örnek Kod**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-WorkbookSettings-ControlExternalResourcesUsingWorkbookSetting_StreamProvider-1.java" >}}
