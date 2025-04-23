---
title: Dış Bağlantı Veri Kaynağı Dosyasının Mutlak Yolunu C++ ile Değiştir
linktitle: Harici Bağlantı Veri Kaynağı Dosya nın Mutlak Yolunu Değiştirme
type: docs
weight: 290
url: /tr/cpp/change-the-absolute-path-of-external-link-data-source-file/
description: Aspose.Cells kullanarak dış bağlantı veri kaynağı dosyasının mutlak yolunu değiştirin.
---

## Olası Kullanım Senaryoları

Dış bağlantı veri kaynağı dosyasının mutlak yolunu değiştirmek istiyorsanız, lütfen [**GetAbsolutePath()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/getabsolutepath/) yöntemini kullanın. Başlangıçta, bu özellik yüklenirken Excel dosyasının alındığı yoldur. Ancak, onu boş bir dize veya yerel bir klasör yolu veya uzak ağ yolu yapabilirsiniz. Bu özelliği değiştirdiğinizde, dış bağlantı veri kaynağı dosyasının yolu da değişecektir.

## Harici Bağlantı Veri Kaynağı Dosyasının Mutlak Yolunu Değiştir

Aşağıdaki örnek kod, uzak bağlantı içeren bir örnek excel dosyasını yükler ([sample excel dosyası](5115146.xlsx)). İlk olarak, uzak yolu yazdırır. Sonra uzak yolu kaldırır ve tekrar yazdırır, bu sefer yerel yol ile dış bağlantı veri kaynağını gösterir. Sonra [**GetAbsolutePath()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/getabsolutepath/) yöntemini hem yerel hem de uzak yola göre değiştirir ve dış bağlantı veri kaynağını tekrar yazdırır, ve değişiklikler konsola yansır.

Yukarıdaki örnek kodun çalıştırılmasından sonra konsol veya hata ayıklama çıktısı, verilen [örnek excel dosyasının](5115146.xlsx) çalıştırılmasından sonra aşağıdadır.

{{< highlight cpp >}}

External Link Data Source: http:\\ws874dmErit\WebFiles\Files\300\ExternalAccounts.xlsx

External Link Data Source After Removing Remote Path: D:\Downloads\ExternalAccounts.xlsx

External Link Data Source After Changing Workbook.AbsolutePath to Local Path: C:\Files\Extra\ExternalAccounts.xlsx

External Link Data Source After Changing Workbook.AbsolutePath to Remote Path: http://www.aspose.com/WebFiles/ExcelFiles/ExternalAccounts.xlsx

{{< /highlight >}}
