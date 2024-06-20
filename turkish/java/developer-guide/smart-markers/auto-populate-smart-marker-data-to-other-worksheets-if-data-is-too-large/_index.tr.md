---
title: Akıllı İşaretleri Otomatik Doldurun, Veri Çok Büyükse Diğer Çalışma Sayfalarına
type: docs
weight: 10
url: /tr/java/auto-populate-smart-marker-data-to-other-worksheets-if-data-is-too-large/
---

## **Olası Kullanım Senaryoları**

Bazı durumlarda veri kaynağınızın 1500000 kaydı olduğunu varsayalım. Bu, bir çalışsayfa için çok fazla kayıttır; bu durumda geri kalan kayıtları bir sonraki çalışsayfaya taşıyabilirsiniz.

## **Veri Çok Büyükse Diğer Çalışsayfalara Akıllı İşaret Verileri Otomatik Doldur**

Aşağıdaki örnek kodun veri kaynağı 21 kayıt içeriyor. Bir çalışsayfada yalnızca 15 kaydı göstermek istiyoruz, geri kalan kayıtlar otomatik olarak ikinci çalışsayfaya taşınacaktır. Lütfen dikkat, ikinci çalışsayfada aynı akıllı işaret etiketi olmalıdır ve her iki sayfa için de [**WorkbookDesigner.process(sheetIndex, isPreserved)**](https://reference.aspose.com/cells/java/com.aspose.cells/workbookdesigner#process(int,%20boolean)) methodunu çağırmalısınız. Bu kodda kullanılan [Microsoft Access Database dosyasını](60489777.accdb) ve kod tarafından oluşturulan [çıkış Excel dosyasını](60489786.xlsx) referans için kontrol ediniz.

## **Örnek Kod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "SmartMarkers-AutoPopulateSmartMarkerDataToOtherWorksheets.java" >}}
