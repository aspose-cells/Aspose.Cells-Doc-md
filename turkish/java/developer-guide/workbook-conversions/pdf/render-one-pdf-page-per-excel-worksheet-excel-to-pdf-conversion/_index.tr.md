---
title: Excel Çalışsayfası Başına Bir PDF Sayfası Oluşturma  Excel den PDF ye Dönüştürme
type: docs
weight: 40
url: /tr/java/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/
---

{{% alert color="primary" %}}

Büyük Microsoft Excel dosyaları ile çalışırken (örneğin her biri 50 sütun ve 300 veya daha fazla satırdan oluşan birçok çalışsayfaya sahip bir elektronik tablo) PDF çıktısının sayfa başına bir çalışsayfa göstermesini isteyebilirsiniz, çalışsayfanın boyutuna bakılmaksızın. Bu, her sayfanın büyük olasılıkla radikal bir şekilde farklı bir sayfa boyutuna sahip olacağı anlamına gelir. Bunun için Aspose.Cells for Java kullanılabilir.

{{% /alert %}}

Lütfen birden çok çalışsayfasına sahip bir Excel dosyasını PDF'ye dönüştüren aşağıdaki örnek kodu inceleyin.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ExceltoPDF-ExceltoPDF.java" >}}

{{% alert color="primary" %}}

Eğer [**PdfSaveOptions.OnePagePerSheet**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#OnePagePerSheet) seçeneği **true** olarak ayarlanmışsa, tüm çalışsayfa içeriği bir PDF sayfasına dönüştürülür. [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/PageSetup) tarafından belirlenen kağıt boyutu geçersizdir, ancak [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/PageSetup) ile ayarlanmış diğer ayarlar yine de etki gösterir.

{{% /alert %}} {{% alert color="primary" %}}

Eğer elektronik tablonuz formülleri içeriyorsa, elektronik tabloyu PDF'ye dönüştürmeden hemen önce [**Workbook.calculateFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula--) metodunu çağırmak en iyisidir. Bu, formül bağımlı değerlerin yeniden hesaplanmasını sağlar ve doğru değerler PDF'de görüntülenir.

{{% /alert %}}
