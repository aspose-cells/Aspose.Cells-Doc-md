---
title: Akıllı İşaretleri Otomatik Doldurun, Veri Çok Büyükse Diğer Çalışma Sayfalarına
type: docs
weight: 50
url: /tr/net/auto-populate-smart-marker-data-to-other-worksheets-if-data-is-too-large/
---

## **Olası Kullanım Senaryoları**
Bazı durumlarda, veri kaynağınızın çok büyük olması durumunda Akıllı İşaretlerini diğer çalışma sayfalarına otomatik olarak doldurmak isteyebilirsiniz. Varsayalım ki, veri kaynağınızın 1500000 kaydı var. Bu, tek bir çalışma sayfası için çok fazla kayıttır, o zaman geri kalan kayıtları bir sonraki çalışma sayfasına taşıyabilirsiniz. 
## **Akıllı İşaretleri Otomatik Doldurun, Veri Çok Büyükse Diğer Çalışma Sayfalarına**
Aşağıdaki örnek kodun veri kaynağında 21 kayıt bulunmaktadır. Bir çalışma sayfasında yalnızca 15 kaydı göstermek istiyoruz, o zaman geri kalan kayıtlar otomatik olarak ikinci çalışma sayfasına taşınır. Lütfen dikkat edin, ikinci çalışma sayfasının aynı akıllı işaret etiketlerine sahip olması gerekmekte ve her iki sayfa için de [WorkbookDesigner.Process(sheetIndex, isPreserved)](https://reference.aspose.com/cells/net/aspose.cells.workbookdesigner/process/methods/2) yöntemini çağırmalısınız. Referans için kod tarafından üretilen [çıktı Excel dosyasını](60489775.xlsx) inceleyin.
## **Örnek Kod**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-AutoPopulateSmartMarkerDataToOtherWorksheets.cs" >}}
{{< app/cells/assistant language="csharp" >}}
