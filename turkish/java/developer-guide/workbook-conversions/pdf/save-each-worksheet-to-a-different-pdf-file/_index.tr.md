---
title: Her bir Çalışsayfayı Farklı Bir PDF Dosyasına Kaydet
type: docs
weight: 50
url: /tr/java/save-each-worksheet-to-a-different-pdf-file/
---

{{% alert color="primary" %}}

Aspose.Cells, (görüntüler, grafikler vb. içeren) elektronik tablo dosyalarını PDF belgelerine dönüştürmeyi destekler. Aspose.Cells for Java bağımsız bir şekilde bir elektronik tabloyu PDF belgesine dönüştürebilir ve dönüşüm için artık Aspose.PDF for Java'yı kullanmanıza gerek yoktur. Dönüşüm, herhangi bir geçici dosya oluşturmayı / kullanmayı gerektirmez çünkü tüm işlem bellekte yapılabilir.

{{% /alert %}}

Eğer şablon Excel dosyanızdaki her çalışma sayfasını farklı PDF dosyaları oluşturmak istiyorsanız, bu kolayca gerçekleştirilebilir. PDF'ye dönüştürmek için [**PdfSaveOptions.SheetSet**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions/#setSheetSet-com.aspose.cells.SheetSet-) seçeneğini bir seferde bir sayfa indeksine ayarlamayı deneyebilirsiniz.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SaveEachWorksheettoDifferentPDF-SaveEachWorksheettoDifferentPDF.java" >}}

{{% alert color="primary" %}}

Eğer elektronik tablo formüller içeriyorsa, elektronik tabloyu PDF'ye dönüştürmeden önce [**Workbook.calculateFormula()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula--) yöntemini çağırmak en iyisidir. Bu, formül bağımlı değerlerin yeniden hesaplanmasını sağlar ve doğru değerler PDF'de gösterilir.

{{% /alert %}}
