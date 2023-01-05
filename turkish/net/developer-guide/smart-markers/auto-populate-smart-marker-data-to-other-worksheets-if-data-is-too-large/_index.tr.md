---
title: Veriler Çok Büyükse Akıllı İşaretleyici Verilerini Diğer Çalışma Sayfalarına Otomatik Olarak Doldur
type: docs
weight: 50
url: /tr/net/auto-populate-smart-marker-data-to-other-worksheets-if-data-is-too-large/
---
## **Olası Kullanım Senaryoları**
Bazen, akıllı işaretçi verilerini çok büyükse diğer çalışma sayfalarına otomatik olarak doldurmak istersiniz. Veri kaynağınızın 1500000 kaydı olduğunu varsayalım. Bunlar, tek bir çalışma sayfası için çok fazla kayıt, ardından kalan kayıtları bir sonraki çalışma sayfasına taşıyabilirsiniz.
## **Veriler Çok Büyükse Akıllı İşaretleyici Verilerini Diğer Çalışma Sayfalarına Otomatik Olarak Doldurun**
 Aşağıdaki örnek kod, 21 kaydı olan bir veri kaynağına sahiptir. Bir çalışma sayfasında yalnızca 15 kayıt göstermek istiyoruz, ardından kalan kayıtlar otomatik olarak ikinci çalışma sayfasına taşınacaktır. Lütfen ikinci çalışma sayfasının da aynı akıllı işaretleyici etiketine sahip olması gerektiğini ve aramanız gerektiğini unutmayın.[WorkbookDesigner.Process(sheetIndex, isPreserved)](https://reference.aspose.com/cells/net/aspose.cells.workbookdesigner/process/methods/2) Her iki sayfa için yöntem. Lütfen bkz[çıktı excel dosyası](60489775.xlsx) referans için kod tarafından oluşturulur.
## **Basit kod**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-AutoPopulateSmartMarkerDataToOtherWorksheets.cs" >}}
