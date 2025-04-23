---
title: Harici Bağlantı Veri Kaynağı Dosya nın Mutlak Yolunu Değiştirme
type: docs
weight: 1020
url: /tr/java/change-the-absolute-path-of-external-link-data-source-file/
---

## **Olası Kullanım Senaryoları**
Mutlak yolunu değiştirmek istiyorsanız Harici Bağlantı Veri Kaynağı Dosya'nın [Workbook.AbsolutePath](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#AbsolutePath) özelliğini kullanın. Bu özellik başlangıçta excel dosyasının yüklenmiş olduğu yolda ayarlanacaktır. Ancak bunu boş bir dizeye ayarlayabilir veya yerel bir klasör yoluna veya uzak ağ yoluna ayarlayabilirsiniz. Bu özelliği değiştirdiğinizde, harici bağlantı veri kaynağı dosyasının yolu da değişir.
## **Harici Bağlantı Veri Kaynağı Dosya'nın Mutlak Yolunu Değiştirme**
Aşağıdaki örnek kod, dış bağlantı içeren [örnek excel dosyasını](5472589.xlsx) yükler. İlk olarak harici bağlantı veri kaynağını yazdırır, uzak yolunu yazdırır. Ardından uzak yolu kaldırır ve bu sefer harici bağlantı veri kaynağını yerel yolla yazdırır. Daha sonra [Workbook.AbsolutePath](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#AbsolutePath) özelliğini bir yerel ve uzak yola değiştirir ve harici bağlantı veri kaynağını tekrar yazdırır ve değişiklikler konsol çıktısına yansır.
## **Örnek Kod**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ChangeAbsolutePathofExternalLink-ChangeAbsolutePathofExternalLink.java" >}}
## **Konsol Çıktısı**
Yukarıdaki örnek kodun yürütülmesinden sonra konsol veya hata ayıklama çıktısı aşağıdaki gibidir [örnek excel dosyası](5472589.xlsx) ile birlikte.

{{< highlight java >}}

 External Link Data Source: http:\\ws874dmErit\WebFiles\Files\300\ExternalAccounts.xlsx

External Link Data Source After Removing Remote Path: D:\Downloads\ExternalAccounts.xlsx

External Link Data Source After Changing Workbook.AbsolutePath to Local Path: C:\Files\Extra\ExternalAccounts.xlsx

External Link Data Source After Changing Workbook.AbsolutePath to Remote Path: http://www.aspose.com/WebFiles/ExcelFiles/ExternalAccounts.xlsx

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
