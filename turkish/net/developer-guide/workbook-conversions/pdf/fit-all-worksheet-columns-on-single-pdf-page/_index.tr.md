---
title: Tüm Çalışsayfa Sütunlarını Tek PDF Sayfasına Sığdır
type: docs
weight: 160
url: /tr/net/fit-all-worksheet-columns-on-single-pdf-page/
---

{{% alert color="primary" %}}

Bazı durumlarda, bir çalışsayfanın tüm sütunlarını tek bir sayfaya sığdıran bir PDF dosyası oluşturmak isteyebilirsiniz. [**PdfSaveOptions.AllColumnsInOnePagePerSheet**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/allcolumnsinonepagepersheet) özelliği bu özelliği çok kullanışlı bir şekilde sağlar. Çıktı PDF'in yükseklik ve genişliği gibi karmaşık hesaplamalar dahili olarak işlenir ve çalışsayfadaki verilere göre belirlenir.

{{% /alert %}}

## **Tüm Çalışsayfa Sütunlarını Tek PDF Sayfasına Sığdır**

[**PdfSaveOptions.AllColumnsInOnePagePerSheet**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/allcolumnsinonepagepersheet), bir çalışsayfadaki tüm sütunların tek bir PDF sayfasına render edilmesini sağlar, ancak satırlar çalışsayfadaki verilere bağlı olarak birden fazla sayfaya genişleyebilir.

Aşağıdaki örnek kod, 100 sütunu olan büyük bir çalışsayfayı render etmek için [**PdfSaveOptions.AllColumnsInOnePagePerSheet**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/allcolumnsinonepagepersheet) özelliğini nasıl kullanacağını göstermektedir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FitAllWorksheetColumns-1.cs" >}}

{{% alert color="primary" %}}

Verilen bir çalışsayfada çok sayıda sütun bulunduğunda, render edilen PDF dosyası içeriği çok küçük bir boyutta görülebilir. Acrobat Reader gibi bir görüntüleme uygulamasında büyütüldüğünde hala okunabilir.

{{% /alert %}} {{% alert color="primary" %}}

Eğer elektronik tablonuz formüller içeriyorsa, PDF formatına dönüştürmeden hemen önce [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula) çağrısını yapmanız en iyisidir. Böyle yaparak formüle bağımlı değerler yeniden hesaplanacak ve doğru değerler PDF'de gösterilecektir.

{{% /alert %}}
