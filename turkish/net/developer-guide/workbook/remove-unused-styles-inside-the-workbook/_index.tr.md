---
title: Çalışma Kitabı İçinde Kullanılmayan Stilleri Kaldırma
type: docs
weight: 340
url: /tr/net/remove-unused-styles-inside-the-workbook/
---

{{% alert color="primary" %}}

Excel dosyasındaki kullanılmayan stiller sadece alan kaplamakla kalmaz, aynı zamanda PDF, HTML vb. farklı biçimlere dönüştürürken performans sorunlarına neden olur. Aspose.Cells, çalışma kitabı içindeki tüm kullanılmayan stilleri kaldırmak için [**Workbook.RemoveUnusedStyles()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/removeunusedstyles) sağlar.

{{% /alert %}}

Aşağıdaki kod, [**Workbook.RemoveUnusedStyles()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/removeunusedstyles) kullanımını açıklar. Kod, [şablon excel dosyasını](5115520.xlsx) yükler, bu dosyayı sağlanan bağlantıdan indirebilirsiniz. İsminde **AsposeStyle** adında kullanılmayan bir stil içerir, bu stil ve tüm diğer kullanılmayan stiller, kodun çalıştırılmasından sonra kaldırılacaktır.

![todo:image_alt_text](remove-unused-styles-inside-the-workbook_1.png)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RemoveUnusedStyles-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
