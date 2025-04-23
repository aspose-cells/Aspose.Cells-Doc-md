---
title: Çizim için Satırları Otomatik Sığdır
type: docs
weight: 130
url: /tr/net/autofit-rows-for-rendering/
---

Genellikle, bir hücredeki tüm metni görüntülemek istediğinizde, Microsoft Excel'de Normal görünümde %100 büyütmeyle satırı otomatik olarak sığdırabilirsiniz. Bu, metnin Normal görünümde tamamen görünmesine olanak tanır ve hatta dosyayı yazdırıp veya PDF olarak kaydettiğinizde metin doğru şekilde görüntülenir.

Ancak bazı durumlarda, satır otomatik sığdırma Normal görünümde iyi çalışır, ancak yazdırılan görünüme geçtiğinizde veya dosyayı PDF olarak kaydettiğinizde metin kesilir. Lütfen kaynak dosyayı kontrol edin [Book1.xlsx](Book1.xlsx) ve ekran görüntülerini inceleyin.

![metin yazdırma görünümünde kesilmiş](metin_yazdırma_görünümünde_kesilmiş.png)

Eğer kaydedilmiş PDF dosyasında metin kesilmemesini istiyorsanız, satır otomatik sığdırma seçeneği olan [AutoFitterOptions.ForRendering](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions/forrendering/) seçeneğini kullanabilirsiniz.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Docs-Autofit-AutofitRowsForRendering.cs" >}}

Şimdi, metin çıktı PDF dosyasında kesilmemiş durumda.

![kaydedilmiş pdf'de metin kesilmemiş](kaydedilmiş_pdfde_metin_kesilmemiş.png)
{{< app/cells/assistant language="csharp" >}}
