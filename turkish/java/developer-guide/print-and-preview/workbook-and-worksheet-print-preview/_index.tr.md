---
title: Çalışma Kitabı ve Çalışma Sayfası Baskı Önizlemesi
type: docs
weight: 130
url: /tr/java/workbook-and-worksheet-print-preview/
---

## **Kullanım Senaryosu**

Milyonlarca sayfalık Excel dosyalarının PDF veya görüntülere dönüştürülmesi gereken durumlar olabilir. Bu tür dosyaların işlenmesi çok zaman ve kaynak tüketebilir. Bu durumlarda, Çalışma Kitabı ve Çalışma Sayfası Baskı Önizleme özelliği faydalı olabilir. Bu tür dosyalar dönüştürülmeden önce, kullanıcı toplam sayfa sayısını kontrol edebilir ve dosyanın dönüştürülüp dönüştürülmeyeceğine karar verebilir. Bu makale, [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookPrintingPreview) ve [**SheetPrintingPreview**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetPrintingPreview) sınıflarını kullanarak toplam sayfa sayısını bulmaya odaklanmaktadır.

## **Çalışma Kitabı ve Çalışma Sayfası Baskı Önizlemesi**

Aspose.Cells, baskı önizleme özelliği sağlar. Bunun için API, [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookPrintingPreview) ve [**SheetPrintingPreview**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetPrintingPreview) sınıflarını sağlar. Tüm çalışma kitabının baskı önizlemesini oluşturmak için, [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) ve [**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions) nesnelerini yapıcıya geçirerek [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookPrintingPreview) sınıfının bir örneğini oluşturun. [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookPrintingPreview) sınıfı, oluşturulan önizlemedeki sayfa sayısını döndüren bir [**EvaluatedPageCount**](https://reference.aspose.com/cells/java/com.aspose.cells/workbookprintingpreview#EvaluatedPageCount) metodu sağlar. [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookPrintingPreview) sınıfına benzer şekilde, [**SheetPrintingPreview**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetPrintingPreview) sınıfı belirli bir çalışma sayfası için bir baskı önizlemesi oluşturmak için kullanılır. Bir çalışma sayfasının baskı önizlemesini oluşturmak için, [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) ve [**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions) nesnelerini yapıcıya geçirerek [**SheetPrintingPreview**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetPrintingPreview) sınıfının bir örneğini oluşturun. [**SheetPrintingPreview**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetPrintingPreview) sınıfı ayrıca oluşturulan önizlemedeki sayfa sayısını döndüren bir [**EvaluatedPageCount**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetprintingpreview#EvaluatedPageCount) metodu sağlar.

Aşağıdaki kod parçası, [örnek excel dosyasını](Book1.xlsx) kullanarak hem [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookPrintingPreview) hem de [**SheetPrintingPreview**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetPrintingPreview) sınıflarının kullanımını göstermektedir.

### **Örnek Kod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-PrintPreview-1.java" >}}

Yukarıdaki kodun yürütülmesiyle oluşturulan çıktı aşağıdaki gibidir.

### **Konsol Çıktısı**

{{< highlight java >}}

Workbook page count: 1</br>
Worksheet page count: 1

{{< /highlight >}}
