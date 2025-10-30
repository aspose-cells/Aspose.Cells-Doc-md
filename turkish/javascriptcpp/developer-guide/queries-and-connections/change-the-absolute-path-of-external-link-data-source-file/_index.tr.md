---
title: C++ kullanarak JavaScript ile Harici Bağlantı Veri Kaynağı Dosyasının Mutlak Yolunu değiştirin
linktitle: Harici Bağlantı Veri Kaynağı Dosya nın Mutlak Yolunu Değiştirme
type: docs
weight: 290
url: /tr/javascript-cpp/change-the-absolute-path-of-external-link-data-source-file/
description: C++ kullanarak Aspose.Cells for JavaScript ile harici bağlantı veri kaynağı dosyasının mutlak yolunu nasıl değiştireceğinizi öğrenin. 
---

## Olası Kullanım Senaryoları

Dış bağlantı veri kaynağı dosyasının mutlak yolunu değiştirmek istiyorsanız, lütfen [**Workbook.absolutePath**](https://reference.aspose.com/cells/javascript-cpp/workbook/#absolutePath--) özelliğini kullanın. Başlangıçta, bu özellik yükleme sırasında Excel dosyasını aldığınız yoldadır. Ancak, boş bir dizeye ayarlayabilir veya yerel bir klasör yolu veya uzak ağ yolu olarak ayarlayabilirsiniz. Bu özelliği değiştirdiğinizde, dış bağlantı veri kaynağı dosyasının yolu da değişecektir.

## Harici Bağlantı Veri Kaynağı Dosyasının Mutlak Yolunu Değiştir

Aşağıdaki örnek kod, içeren dış bağlantının olduğu örnek Excel dosyasını yükler (5115146.xlsx). İlk olarak, uzak yolu yazdırır. Sonra uzak yolu kaldırır ve yeniden yazar; bu sefer içeren dış bağlantı veri kaynağını yerel yol ile yazdırır. Ardından, [**Workbook.absolutePath**](https://reference.aspose.com/cells/javascript-cpp/workbook/#absolutePath--) özelliğini yerel ve uzak yola değiştirir ve dış bağlantı veri kaynağını tekrar yazdırır, ve değişiklikler konsol çıktısında yansıtılır.



{{< highlight javascript >}}

External Link Data Source: http:\\ws874dmErit\WebFiles\Files\300\ExternalAccounts.xlsx

External Link Data Source After Removing Remote Path: D:\Downloads\ExternalAccounts.xlsx

External Link Data Source After Changing Workbook.AbsolutePath to Local Path: C:\Files\Extra\ExternalAccounts.xlsx

External Link Data Source After Changing Workbook.AbsolutePath to Remote Path: http://www.aspose.com/WebFiles/ExcelFiles/ExternalAccounts.xlsx

{{< /highlight >}}
