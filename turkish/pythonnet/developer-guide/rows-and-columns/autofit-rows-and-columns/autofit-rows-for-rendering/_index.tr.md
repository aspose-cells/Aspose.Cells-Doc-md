---
title: Çizim için Satırları Otomatik Sığdır
type: docs
weight: 130
url: /tr/python-net/autofit-rows-for-rendering/
description: Aspose.Cells for Python via .NET API si aracılığıyla Çizim için Satırları Otomatik Olarak Ayarlama yöntemini öğrenin.
keywords: Python Excel Kütüphanesi, Python Çizim için Satırları Otomatik Olarak Ayarlama, Excel dosyasını açarken satır yüksekliğini otomatik olarak ayarlama. 
---

Genellikle, bir hücredeki tüm metni görüntülemek istediğinizde, Microsoft Excel'de Normal görünümde %100 büyütmeyle satırı otomatik olarak sığdırabilirsiniz. Bu, metnin Normal görünümde tamamen görünmesine olanak tanır ve hatta dosyayı yazdırıp veya PDF olarak kaydettiğinizde metin doğru şekilde görüntülenir.

Ancak bazı durumlarda, satır otomatik sığdırma Normal görünümde iyi çalışır, ancak yazdırılan görünüme geçtiğinizde veya dosyayı PDF olarak kaydettiğinizde metin kesilir. Lütfen kaynak dosyayı kontrol edin [Book1.xlsx](Book1.xlsx) ve ekran görüntülerini inceleyin.

![metin yazdırma görünümünde kesilmiş](metin_yazdırma_görünümünde_kesilmiş.png)

Kaydedilen PDF dosyasındaki metnin kesilmesini önlemek istiyorsanız, [AutoFitterOptions.for_rendering](https://reference.aspose.com/cells/python-net/aspose.cells/autofitteroptions/for_rendering/) seçeneği ile sütunu otomatik boyutlandırabilirsiniz.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-AutofitRowsForRendering.py" >}}

Şimdi, metin çıktı PDF dosyasında kesilmemiş durumda.

![kaydedilmiş pdf'de metin kesilmemiş](kaydedilmiş_pdfde_metin_kesilmemiş.png)
