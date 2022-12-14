---
title: Tüm Çalışma Sayfası Sütunlarını Tek PDF Sayfasına Sığdır
type: docs
weight: 70
url: /tr/java/fit-all-worksheet-columns-on-single-pdf-page/
---
{{% alert color="primary" %}}

 Bazen bir çalışma sayfasının tüm sütunlarını tek bir sayfaya sığdıran bir PDF dosyası oluşturmak istersiniz. bu[**PdfSaveOptions.setAllColumnsInOnePagePerSheet**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#AllColumnsInOnePagePerSheet) özelliği bu özelliği kullanımı çok kolay bir şekilde sağlar. Çıktı PDF sayfasının yüksekliği ve genişliği gibi karmaşık hesaplamalar dahili olarak yapılır ve çalışma sayfasındaki verilere dayanır.

{{% /alert %}}

## **Çalışma Sayfası Sütunlarını Tek PDF Sayfasına Sığdır**

[**PdfSaveOptions.setAllColumnsInOnePagePerSheet**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#AllColumnsInOnePagePerSheet)satırlar, çalışma sayfasındaki verilere bağlı olarak birkaç sayfaya genişleyebilse de, bir çalışma sayfasının tüm sütunlarının tek bir PDF sayfasına dönüştürülmesini sağlar.

{{% alert color="primary" %}}

Belirli bir çalışma sayfasında çok sayıda sütun olduğunda, oluşturulan PDF dosyası içeriği çok küçük bir boyutta gösterebilir. Acrobat Reader gibi bir görüntüleme uygulamasında büyütüldüğünde yine de okunabilir.

{{% /alert %}}

 Aşağıdaki örnek kod, nasıl kullanılacağını gösterir.[**PdfSaveOptions.setAllColumnsInOnePagePerSheet**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#AllColumnsInOnePagePerSheet)100 sütunluk büyük bir çalışma sayfası oluşturma özelliği.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-FitAllWorksheetColumns-FitAllWorksheetColumns.java" >}}

{{% alert color="primary" %}}

 E-tablonuz formüller içeriyorsa, aramak en iyisidir[**Workbook.calculateFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula()) yöntemi, elektronik tabloyu PDF biçimine dönüştürmeden hemen önce. Bunu yapmak, formüle bağlı değerlerin yeniden hesaplanmasını ve doğru değerlerin PDF'de oluşturulmasını sağlar.

{{% /alert %}}
