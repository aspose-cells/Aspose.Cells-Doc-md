---
title: İşleme için Satırları Otomatik Sığdır
type: docs
weight: 130
url: /tr/net/autofit-rows-for-rendering/
---
Genel olarak, bir hücredeki metnin tamamını görüntülemek istediğinizde, Microsoft Excel'de normal görünümde %100 yakınlaştırmayla satırı otomatik olarak sığdırabilirsiniz. Bu, metnin Normal görünümde tamamen görünmesini sağlar ve dosyayı PDF olarak yazdırdığınızda veya kaydettiğinizde bile metin doğru şekilde görüntülenir.

 Ancak bazı durumlarda satırın otomatik sığdırılması Normal görünümde düzgün çalışır ancak yazdırma görünümüne geçtiğinizde veya dosyayı PDF olarak kaydettiğinizde metin kırpılır. Lütfen kaynak dosyayı kontrol edin[Kitap1.xlsx](Book1.xlsx) ve ekran görüntüleri.

![metin baskı görünümünde kırpılıyor](text_clipped_in_printview.png)

Kaydedilen PDF dosyasında metnin kırpılmasını önlemek istiyorsanız satırı otomatik olarak sığdırabilirsiniz.[AutoFitterOptions.ForRendering](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions/forrendering/) seçenek.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Docs-Autofit-AutofitRowsForRendering.cs" >}}

Artık metin PDF çıktı dosyasında kırpılmıyor.

![kayıtlı pdf'te metin kırpılmıyor](text_not_clipped_in_saved_pdf.png)