---
title: Her Çalışma Sayfasını Farklı Bir PDF Dosyasına Kaydet
type: docs
weight: 50
url: /tr/java/save-each-worksheet-to-a-different-pdf-file/
---
{{% alert color="primary" %}}

Aspose.Cells, elektronik tablo dosyalarının (resimler, grafikler vb. içeren) PDF belgelerine dönüştürülmesini destekler. Aspose.Cells for Java, bir elektronik tabloyu PDF belgesine dönüştürmek için bağımsız olarak çalışabilir ve artık dönüştürme için Aspose.PDF for Java kullanmanıza gerek yoktur. Tüm işlem bellekte yapılabildiğinden, dönüştürme herhangi bir geçici dosya (lar) oluşturmayı / kullanmayı gerektirmez.

{{% /alert %}}

Farklı PDF dosyaları oluşturmak için şablon Excel dosyanızdaki her çalışma sayfasını kaydetmeniz gerekiyorsa. Bu kolayca elde edilebilir. Bir sayfa dizini olarak ayarlamayı deneyebilirsiniz.**[`PdfSaveOptions.SheetSet`](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions/#setSheetSet-com.aspose.cells.SheetSet-)** PDF'e işlenecek bir seferde seçenek.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SaveEachWorksheettoDifferentPDF-SaveEachWorksheettoDifferentPDF.java" >}}

{{% alert color="primary" %}}

 Elektronik tablo formüller içeriyorsa, en iyisi[**Workbook.calculateFormula()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula()) yöntemi, elektronik tabloyu PDF'e dönüştürmeden hemen önce. Bu, formüle bağlı değerlerin yeniden hesaplanmasını ve doğru değerlerin PDF'de oluşturulmasını sağlar.

{{% /alert %}}
