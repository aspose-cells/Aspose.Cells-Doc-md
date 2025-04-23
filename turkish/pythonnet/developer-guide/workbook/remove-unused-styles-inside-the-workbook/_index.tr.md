---
title: Çalışma Kitabı İçinde Kullanılmayan Stilleri Kaldırma
type: docs
weight: 340
url: /tr/python-net/remove-unused-styles-inside-the-workbook/
---

{{% alert color="primary" %}}

Excel dosyasında kullanılmayan stiller sadece alan kaplamaz, aynı zamanda PDF, HTML gibi farklı biçimlere dönüştürürken performans sorunlarına da neden olur. Aspose.Cells for Python via .NET, çalışma kitabı içindeki kullanılmayan tüm stilleri kaldırmak için [**Workbook.remove_unused_styles()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/remove_unused_styles) sağlar.

{{% /alert %}}

Aşağıdaki kod, [**Workbook.remove_unused_styles()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/remove_unused_styles) kullanımını açıklar. Kod, [şablon excel dosyasını](5115520.xlsx) yükler, bu dosyayı sağlanan bağlantıdan indirebilirsiniz. İsminde **AsposeStyle** adında kullanılmayan bir stil içerir, bu stil ve tüm diğer kullanılmayan stiller, kodun çalıştırılmasından sonra kaldırılacaktır.

![todo:image_alt_text](remove-unused-styles-inside-the-workbook_1.png)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Workbook-RemoveUnusedStyles-1.py" >}}

