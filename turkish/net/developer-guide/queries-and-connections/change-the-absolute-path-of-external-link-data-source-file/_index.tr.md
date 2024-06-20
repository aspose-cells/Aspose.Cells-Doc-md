---
title: Harici Bağlantı Veri Kaynağı Dosya nın Mutlak Yolunu Değiştirme
type: docs
weight: 290
url: /tr/net/change-the-absolute-path-of-external-link-data-source-file/
---

## Olası Kullanım Senaryoları

Eğer harici bağlantı veri kaynağı dosyasının mutlak yolunu değiştirmek istiyorsanız, lütfen [**Workbook.AbsolutePath**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/absolutepath) özelliğini kullanın. Başlangıçta bu özellik, excel dosyasının yüklendiği yerden gelen yola ayarlanacaktır. Ancak bunu boş bir dize olarak ayarlayabilir veya bazı yerel klasör yolu veya uzak ağ yoluna ayarlayabilirsiniz. Bu özelliği değiştirdiğinizde, harici bağlantı veri kaynağı dosyasının yolu da değişecektir.

## Harici Bağlantı Veri Kaynağı Dosyasının Mutlak Yolunu Değiştir

Aşağıdaki örnek kod, harici bir bağlantı içeren [örnek excel dosyasını](5115146.xlsx) yükler. İlk önce uzak yolunu yazdırır. Ardından uzak yolu kaldırır ve tekrar yazdırır, bu sefer yerel yol harici bağlantı veri kaynağı yazdırılır. Daha sonra [**Workbook.AbsolutePath**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/absolutepath) özelliğini yerel ve uzak bir yol olarak değiştirir ve harici bağlantı veri kaynağını tekrar yazdırır ve değişiklikler konsol çıktısına yansıtılır.

Yukarıdaki örnek kodun çalıştırılmasından sonra konsol veya hata ayıklama çıktısı, verilen [örnek excel dosyasının](5115146.xlsx) çalıştırılmasından sonra aşağıdadır.

{{< highlight java >}}

External Link Data Source: http:\\ws874dmErit\WebFiles\Files\300\ExternalAccounts.xlsx

External Link Data Source After Removing Remote Path: D:\Downloads\ExternalAccounts.xlsx

External Link Data Source After Changing Workbook.AbsolutePath to Local Path: C:\Files\Extra\ExternalAccounts.xlsx

External Link Data Source After Changing Workbook.AbsolutePath to Remote Path: http://www.aspose.com/WebFiles/ExcelFiles/ExternalAccounts.xlsx

{{< /highlight >}}
