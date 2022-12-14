---
title: Dış Bağlantı Veri Kaynağı Dosyasının Mutlak Yolunu Değiştirme
type: docs
weight: 290
url: /tr/net/change-the-absolute-path-of-external-link-data-source-file/
---
## Olası Kullanım Senaryoları

 Harici bağlantı veri kaynağı dosyasının mutlak yolunu değiştirmek istiyorsanız, lütfen[**Workbook.AbsolutePath**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/absolutepath)Emlak. Başlangıçta, bu özellik, excel dosyasının yüklendiği yerden yola ayarlanacaktır. Ancak onu boş bir dizeye veya bazı yerel klasör yollarına veya uzak ağ yollarına ayarlayabilirsiniz. Bu özelliği her değiştirdiğinizde, dış bağlantı veri kaynak dosyasının yolu da değiştirilecektir.

## Dış Bağlantı Veri Kaynağı Dosyasının Mutlak Yolunu Değiştirme

 Aşağıdaki örnek kod,[örnek excel dosyası](5115146.xlsx) harici bir bağlantı içerir. Önce uzak yolu yazdıran harici bağlantı veri kaynağını yazdırır. Daha sonra uzak yolu kaldırır ve tekrar yazdırır, bu sefer yerel yol ile harici bağlantı veri kaynağını yazdırır. Sonra değiştirir[**Workbook.AbsolutePath**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/absolutepath)özelliğini yerel ve uzak bir yola aktarır ve dış bağlantı veri kaynağını yeniden yazdırır ve değişiklikler konsol çıktısına yansıtılır.

Yukarıdaki örnek kodun aşağıdaki kodla yürütülmesinden sonraki konsol veya hata ayıklama çıktısı:[örnek excel dosyası](5115146.xlsx).

{{< highlight "java" >}}

External Link Data Source: http:\\ws874dmErit\WebFiles\Files\300\ExternalAccounts.xlsx

External Link Data Source After Removing Remote Path: D:\Downloads\ExternalAccounts.xlsx

External Link Data Source After Changing Workbook.AbsolutePath to Local Path: C:\Files\Extra\ExternalAccounts.xlsx

External Link Data Source After Changing Workbook.AbsolutePath to Remote Path: http://www.aspose.com/WebFiles/ExcelFiles/ExternalAccounts.xlsx

{{< /highlight >}}
