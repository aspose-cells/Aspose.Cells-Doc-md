---
title: Excel Çalışsayfası Başına Bir PDF Sayfası Oluşturma  Excel den PDF ye Dönüştürme
type: docs
weight: 100
url: /tr/net/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/
---

{{% alert color="primary" %}} 

Büyük Microsoft Excel dosyaları ile çalışırken (örneğin, her biri 50 sütun ve 300 veya daha fazla satır veri içeren birçok çalışsayfaya sahip bir çalışma kitabı), PDF çıktısının, çalışsayfa boyutundan bağımsız olarak her bir çalışsayfa başına bir sayfa göstermesini isteyebilirsiniz. Bu, her sayfanın muhtemelen radikal farklı bir sayfa boyutuna sahip olacağı anlamına gelir. Bu, Aspose.Cells for .NET kullanılarak başarıyla gerçekleştirilebilir.

{{% /alert %}} 

Lütfen birden çok çalışsayfasına sahip bir Excel dosyasını PDF'ye dönüştüren aşağıdaki örnek kodu inceleyin.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderOnePdfPagePerExcelWorksheet-1.cs" >}}

{{% alert color="primary" %}} 

[AnasayfaSayfaBaşı](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/onepagepersheet) seçeneğine **true** ayarlandığında, tüm sayfa içeriği bir PDF sayfasına oluşturulur.

{{% /alert %}} {{% alert color="primary" %}} 

Eğer elektronik tablonuz formüller içeriyorsa, elektronik tablonun PDF'ye dönüştürülmeden önce [Workbook.CalculateFormula()](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula) çağrılması en iyisidir. Bu, formül bağımlı değerlerin yeniden hesaplandığından ve doğru değerlerin PDF'de oluşturulduğundan emin olur.

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
