---
title: Render Bir PDF Sayfa Başına Excel Çalışma Sayfası - Excel'den PDF'e Dönüştürme
type: docs
weight: 100
url: /tr/net/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/
---
{{% alert color="primary" %}} 

Büyük Microsoft Excel dosyalarıyla çalışırken (örneğin, her biri 50 sütun ve 300 veya daha fazla veri satırı içeren birçok sayfası olan bir çalışma kitabı), çalışma sayfasının boyutundan bağımsız olarak, PDF çıktısının çalışma sayfası başına bir sayfa göstermesini isteyebilirsiniz. . Bu, her sayfanın kökten farklı bir sayfa boyutuna sahip olabileceği anlamına gelir. Bu, Aspose.Cells for .NET kullanılarak elde edilebilir.

{{% /alert %}} 

Birden çok çalışma sayfası içeren bir Excel dosyasını PDF'e dönüştüren aşağıdaki örnek koda bakın.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderOnePdfPagePerExcelWorksheet-1.cs" >}}

{{% alert color="primary" %}} 

 Eğer[Sayfa Başına Bir Sayfa](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/onepagepersheet) seçeneği ayarlandı**doğru**, tüm sayfa içeriği tek bir PDF sayfasına işlenecektir.

{{% /alert %}} {{% alert color="primary" %}} 

E-tablonuz formüller içeriyorsa, aramak en iyisidir[Workbook.CalculateFormula()](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula)elektronik tabloyu PDF olarak oluşturmadan hemen önce. Bu, formüle bağlı değerlerin yeniden hesaplanmasını ve doğru değerlerin PDF'de oluşturulmasını sağlar.

{{% /alert %}}
