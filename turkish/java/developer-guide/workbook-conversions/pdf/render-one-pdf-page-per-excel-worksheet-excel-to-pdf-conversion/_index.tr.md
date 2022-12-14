---
title: Excel Çalışma Sayfası Başına Bir PDF Sayfası Oluşturun - Excel'den PDF'e Dönüştürme
type: docs
weight: 40
url: /tr/java/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/
---
{{% alert color="primary" %}}

Büyük Microsoft Excel dosyalarıyla çalışırken (örneğin, her biri 50 sütun ve 300 veya daha fazla veri satırı içeren birçok sayfası olan bir çalışma kitabı), çalışma sayfasının boyutundan bağımsız olarak PDF çıktısının çalışma sayfası başına bir sayfa göstermesini isteyebilirsiniz. . Bu, her sayfanın kökten farklı bir sayfa boyutuna sahip olabileceği anlamına gelir. Bu, Aspose.Cells for Java kullanılarak elde edilebilir.

{{% /alert %}}

Birden çok çalışma sayfası içeren bir Excel dosyasını PDF'ye dönüştüren aşağıdaki örnek koda bakın.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ExceltoPDF-ExceltoPDF.java" >}}

{{% alert color="primary" %}}

 Eğer[**PdfSaveOptions.OnePagePerSheet**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#OnePagePerSheet) seçeneği ayarlandı**doğru** , tüm sayfa içeriği tek bir PDF sayfasına dönüştürülür. tarafından ayarlanan kağıt boyutu[**Sayfa ayarı**](https://reference.aspose.com/cells/java/com.aspose.cells/PageSetup) geçersizdir, ancak ile ayarlanan diğer ayarlar[**Sayfa ayarı**](https://reference.aspose.com/cells/java/com.aspose.cells/PageSetup)hala geçerli.

{{% /alert %}} {{% alert color="primary" %}}

E-tablonuz formüller içeriyorsa, en iyisi[**Workbook.calculateFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula()) yöntemi, elektronik tabloyu PDF'ye dönüştürmeden hemen önce. Bu, formüle bağlı değerlerin yeniden hesaplanmasını ve doğru değerlerin PDF'de işlenmesini sağlar.

{{% /alert %}}
