---
title: Tüm Çalışma Sayfası Sütunlarını Tek PDF Sayfasına Sığdır
type: docs
weight: 160
url: /tr/net/fit-all-worksheet-columns-on-single-pdf-page/
---
{{% alert color="primary" %}}

Bazen bir çalışma sayfasının tüm sütunlarını tek bir sayfaya sığdıran bir PDF dosyası oluşturmak istersiniz. bu[**PdfSaveOptions.AllColumnsInOnePagePerSheet**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/allcolumnsinonepagepersheet) özelliği bu özelliği kullanımı çok kolay bir şekilde sağlar. Çıktı PDF'sinin yüksekliği ve genişliği gibi karmaşık hesaplamalar dahili olarak yapılır ve çalışma sayfasındaki verilere dayanır.

{{% /alert %}}

## **Çalışma Sayfası Sütunlarını Tek PDF Sayfasına Sığdır**

[**PdfSaveOptions.AllColumnsInOnePagePerSheet**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/allcolumnsinonepagepersheet)çalışma sayfasındaki tüm sütunların tek bir PDF sayfasına dönüştürülmesini sağlar, ancak çalışma sayfasındaki verilere bağlı olarak satırlar birkaç sayfaya genişleyebilir.

Aşağıdaki örnek kod nasıl kullanılacağını gösterir[**PdfSaveOptions.AllColumnsInOnePagePerSheet**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/allcolumnsinonepagepersheet)100 sütunluk büyük bir çalışma sayfası oluşturma özelliği.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FitAllWorksheetColumns-1.cs" >}}

{{% alert color="primary" %}}

Belirli bir çalışma sayfasında çok sayıda sütun olduğunda, oluşturulan PDF dosyası içeriği çok küçük bir boyutta gösterebilir. Acrobat Reader gibi bir görüntüleme uygulamasında büyütüldüğünde yine de okunabilir.

{{% /alert %}} {{% alert color="primary" %}}

 E-tablonuz formüller içeriyorsa, aramak en iyisidir[**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula) elektronik tabloyu PDF formatına dönüştürmeden hemen önce. Bunu yapmak, formüle bağlı değerlerin yeniden hesaplanmasını ve doğru değerlerin PDF'de oluşturulmasını sağlar.

{{% /alert %}}
