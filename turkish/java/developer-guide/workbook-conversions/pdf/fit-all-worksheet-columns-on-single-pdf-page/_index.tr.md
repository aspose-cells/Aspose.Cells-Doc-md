---
title: Tüm Çalışsayfa Sütunlarını Tek PDF Sayfasına Sığdır
type: docs
weight: 70
url: /tr/java/fit-all-worksheet-columns-on-single-pdf-page/
---

{{% alert color="primary" %}}

Bazı durumlarda, bir çalışsayfanın tüm sütunlarını tek bir sayfaya sığan bir PDF dosyası üretmek isteyebilirsiniz. [**PdfSaveOptions.setAllColumnsInOnePagePerSheet**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#AllColumnsInOnePagePerSheet) özelliği, bu özelliği çok kolay kullanıma sunar. Çıktı PDF sayfasının yüksekliği ve genişliği gibi karmaşık hesaplamalar, çalışma sayfasındaki verilere dayalı olarak içsel şekilde işlenir.

{{% /alert %}}

## **Tüm Çalışsayfa Sütunlarını Tek PDF Sayfasına Sığdır**

[**PdfSaveOptions.setAllColumnsInOnePagePerSheet**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#AllColumnsInOnePagePerSheet), çalışsayfanın tüm sütunlarının tek bir PDF sayfasına render edilmesini sağlar, ancak satırlar çalışma sayfasındaki veriye bağlı olarak Birden fazla sayfaya genişleyebilir.

{{% alert color="primary" %}}

Verilen bir çalışsayfada çok sayıda sütun varsa, oluşturulan PDF dosyası içeriği çok küçük bir boyutta gösterebilir. Acrobat Reader gibi bir görüntüleme uygulamasında büyütülse bile hala okunabilir.

{{% /alert %}}

Aşağıdaki örnek kod, 100 sütunlu büyük bir çalışsayfayı [**PdfSaveOptions.setAllColumnsInOnePagePerSheet**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#AllColumnsInOnePagePerSheet) özelliğini kullanarak render etme yöntemini gösterir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-FitAllWorksheetColumns-FitAllWorksheetColumns.java" >}}

{{% alert color="primary" %}}

Elektronik tablonuzda formüller bulunuyorsa, en iyi şekilde [**Workbook.calculateFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula--) yöntemini elektronik tabloyu PDF biçimine dönüştürmeden hemen önce çağırmanız önerilir. Böylece formül bağımlı değerler yeniden hesaplanır ve doğru değerler PDF'de render edilir.

{{% /alert %}}
