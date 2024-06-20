---
title: Çizim için Satırları Otomatik Sığdır
type: docs
weight: 130
url: /tr/java/autofit-rows-for-rendering/
---

Genellikle, bir hücredeki tüm metni görüntülemek istediğinizde, Microsoft Excel'de Normal görünümde %100 büyütmeyle satırı otomatik olarak sığdırabilirsiniz. Bu, metnin Normal görünümde tamamen görünmesine olanak tanır ve hatta dosyayı yazdırıp veya PDF olarak kaydettiğinizde metin doğru şekilde görüntülenir.

Ancak bazı durumlarda, satır otomatik sığdırma Normal görünümde iyi çalışır, ancak yazdırılan görünüme geçtiğinizde veya dosyayı PDF olarak kaydettiğinizde metin kesilir. Lütfen kaynak dosyayı kontrol edin [Book1.xlsx](Book1.xlsx) ve ekran görüntülerini inceleyin.

![metin yazdırma görünümünde kesilmiş](metin_yazdırma_görünümünde_kesilmiş.png)

Eğer kaydedilen PDF dosyasında metnin kesilmesini engellemek istiyorsanız, satırı [AutoFitterOptions.ForRendering](https://reference.aspose.com/cells/java/com.aspose.cells/autofitteroptions/#setForRendering-boolean-) seçeneği ile otomatik olarak ayarlayabilirsiniz.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Docs-Autofit-AutofitRowsForRendering.java" >}}

Şimdi, metin çıktı PDF dosyasında kesilmemiş durumda.

![kaydedilmiş pdf'de metin kesilmemiş](kaydedilmiş_pdfde_metin_kesilmemiş.png)
