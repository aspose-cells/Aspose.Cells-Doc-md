---
title: Veriler Çok Büyükse Akıllı İşaretleyici Verilerini Diğer Çalışma Sayfalarına Otomatik Olarak Doldur
type: docs
weight: 10
url: /tr/java/auto-populate-smart-marker-data-to-other-worksheets-if-data-is-too-large/
---
## **Olası Kullanım Senaryoları**

Bazen, akıllı işaretçi verilerini çok büyükse diğer çalışma sayfalarına otomatik olarak doldurmak istersiniz. Veri kaynağınızın 1500000 kaydı olduğunu varsayalım. Bunlar, tek bir çalışma sayfası için çok fazla kayıt, ardından kalan kayıtları bir sonraki çalışma sayfasına taşıyabilirsiniz.

## **Veriler Çok Büyükse Akıllı İşaretleyici Verilerini Diğer Çalışma Sayfalarına Otomatik Olarak Doldur**

Aşağıdaki örnek kod, 21 kaydı olan bir veri kaynağına sahiptir. Bir çalışma sayfasında yalnızca 15 kayıt göstermek istiyoruz, ardından kalan kayıtlar otomatik olarak ikinci çalışma sayfasına taşınacaktır. Lütfen ikinci çalışma sayfasının da aynı akıllı işaretleyici etiketine sahip olması gerektiğini ve aramanız gerektiğini unutmayın.[**WorkbookDesigner.process(sheetIndex, isPreserved)**](https://reference.aspose.com/cells/java/com.aspose.cells/workbookdesigner#process(int,%20boolean) ) her iki sayfa için yöntem. lütfen kontrol ediniz[Microsoft Erişim Veritabanı dosyası](60489777.accdb) Bu kodun yanı sıra kullanılan[çıktı excel dosyası](60489786.xlsx)referans için kod tarafından oluşturulur.

## **Basit kod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "SmartMarkers-AutoPopulateSmartMarkerDataToOtherWorksheets.java" >}}
