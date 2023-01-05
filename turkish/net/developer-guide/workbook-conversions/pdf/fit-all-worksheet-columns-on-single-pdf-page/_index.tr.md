---
title: Tüm Çalışma Sayfası Sütunlarını Tek PDF Sayfaya Sığdır
type: docs
weight: 160
url: /tr/net/fit-all-worksheet-columns-on-single-pdf-page/
---
{{% alert color="primary" %}}

 Bazen bir çalışma sayfasının tüm sütunlarını tek bir sayfaya sığdıran bir PDF dosyası oluşturmak istersiniz. bu[**PdfSaveOptions.AllColumnsInOnePagePerSheet**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/allcolumnsinonepagepersheet) özelliği bu özelliği kullanımı çok kolay bir şekilde sağlar. PDF çıktısının yüksekliği ve genişliği gibi karmaşık hesaplamalar dahili olarak gerçekleştirilir ve çalışma sayfasındaki verilere dayanır.

{{% /alert %}}

## **Çalışma Sayfası Sütunlarını Tek PDF Sayfaya Sığdır**

[**PdfSaveOptions.AllColumnsInOnePagePerSheet**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/allcolumnsinonepagepersheet)bir çalışma sayfasındaki tüm sütunların tek bir PDF sayfasına dönüştürülmesini sağlar, ancak çalışma sayfasındaki verilere bağlı olarak satırlar birkaç sayfaya genişleyebilir.

Aşağıdaki örnek kod nasıl kullanılacağını gösterir[**PdfSaveOptions.AllColumnsInOnePagePerSheet**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/allcolumnsinonepagepersheet)100 sütunluk büyük bir çalışma sayfası oluşturma özelliği.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FitAllWorksheetColumns-1.cs" >}}

{{% alert color="primary" %}}

Belirli bir çalışma sayfasında birçok sütun olduğunda, oluşturulan PDF dosyası içeriği çok küçük bir boyutta gösterebilir. Acrobat Reader gibi bir görüntüleme uygulamasında büyütüldüğünde yine de okunabilir.

{{% /alert %}} {{% alert color="primary" %}}

E-tablonuz formüller içeriyorsa, aramak en iyisidir[**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula)elektronik tabloyu PDF biçimine dönüştürmeden hemen önce. Bunu yapmak, formüle bağlı değerlerin yeniden hesaplanmasını ve PDF'de doğru değerlerin oluşturulmasını sağlar.

{{% /alert %}}
