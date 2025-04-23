---
title: Çalışma Kitabı İçinde Kullanılmayan Stilleri Kaldırma
type: docs
weight: 470
url: /tr/java/remove-unused-styles-inside-the-workbook/
---

{{% alert color="primary" %}} 

Excel dosyasındaki kullanılmayan stiller sadece alan kazanmakla kalmaz, aynı zamanda PDF, HTML vb. farklı biçimlere dönüştürürken performans sorunlarına da yol açar. Aspose.Cells, çalışma kitabındaki kullanılmayan tüm stilleri kaldırmak için [Workbook.removeUnusedStyles()](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#removeUnusedStyles--) sağlar.

{{% /alert %}} 
## **Çalışma Kitabı İçinde Kullanılmayan Stilleri Kaldırma**
Aşağıdaki kod, [Workbook.removeUnusedStyles()](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#removeUnusedStyles--) kullanımını açıklar. Kod, sağlanan bağlantıdan indirebileceğiniz [şablon Excel dosyasını](5473451.xlsx) yükler. Bu dosyada, **AsposeStyle** adında kullanılmayan bir stil içerir. Bu stil ve diğer kullanılmayan tüm stiller, kodun yürütülmesinin ardından kaldırılır. Daha fazla açıklama için aşağıdaki ekran görüntüsüne bakabilirsiniz.

![todo:image_alt_text](remove-unused-styles-inside-the-workbook_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-RemoveUnusedStyles-RemoveUnusedStyles.java" >}}
{{< app/cells/assistant language="java" >}}
