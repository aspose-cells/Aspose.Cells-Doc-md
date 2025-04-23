---
title: Çalışma Kitabını Yazdır ve Önizle
linktitle: Yazdır ve Önizle
type: docs
weight: 70
url: /tr/net/workbook-and-worksheet-print-preview/
description: Aspose.Cells, Microsoft Excel kurulumu olmadan Excel dosyalarını yazdırmayı ve önizlemeyi destekler.
---

{{% alert color="primary" %}}

Bir çalışma sayfası oluşturduktan sonra genellikle onun kağıt çıktısını almak istersiniz. Bu makale, Aspose.Cells ile elektronik tabloları nasıl yazdıracağınızı açıklar.

{{% /alert %}}

## **Yazdırma Girişi**

Microsoft Excel, bir seçim belirtmediğiniz sürece, bütün çalışma sayfası alanını yazdırmayı varsayar. Aspose.Cells kullanarak yazdırmak için önce Aspose.Cells.Rendering isim alanını programa içe aktarın. Örneğin, [**SheetRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender) ve [**WorkbookRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookrender) gibi birçok kullanışlı sınıf bulunmaktadır.

### **SheetRender Kullanarak Yazdır**

[**Aspose.Cells.Rendering.SheetRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender) sınıfı bir çalışma sayfasını temsil eder ve [**ToPrinter**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender/methods/toprinter/index) yöntemine sahiptir, bu yöntem bir çalışma sayfasını yazdırabilir. Aşağıdaki örnek kod, bir çalışma sayfasını nasıl yazdıracağınızı gösterir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-PrintingUsingSheetRender-PrintingExcelWorkbookUsingSheetRender.cs" >}}

### **WorkbookRender Kullanarak Yazdır**

Bütün çalışma kitabını yazdırmak için sayfalar üzerinde döngü yapın ve onları yazdırın veya [**WorkbookRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookrender) sınıfını kullanın.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-PrintingUsingWorkbookRender-1.cs" >}}

{{% alert color="primary" %}}

Aspose.Cells, [**WorkbookRender.ToPrinter()**](https://reference.aspose.com/cells/net/aspose.cells.rendering.workbookrender/toprinter/methods/3) ve [**SheetRender.ToPrinter()**](https://reference.aspose.com/cells/net/aspose.cells.rendering.sheetrender/toprinter/methods/2) yöntemleri için aşırı yüklemeler de sağlar, bu sayede Excel elektronik tabloları yazdırılırken yazdırma işi adı belirlenebilir. Varsayılan olarak, tüm yazdırma işlemleri "Belge" adı ile oluşturulur.

{{% /alert %}}

## **Yazdırma Önizlemesi**

Milyonlarca sayfalı Excel dosyalarının PDF veya görüntüye dönüştürülmesi gereken durumlar olabilir. Bu tür dosyaların işlenmesi çok zaman ve kaynak tüketebilir. Bu durumlarda, Çalışma Kitabı ve Çalışma Sayfası Yazdırma Önizlemesi özelliği faydalı olabilir. Kullanıcı, dosyanın dönüştürülmeden önce toplam sayfa sayısını kontrol edebilir ve dönüştürülüp dönüştürülmeyeceğine karar verebilir. Bu makale, toplam sayfa sayısını öğrenmek için [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookprintingpreview) ve [**SheetPrintingPreview**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetprintingpreview) sınıflarını kullanmayı ele almaktadır.

Aspose.Cells, yazdırma önizlemesi özelliğini sağlar. Bunun için API, [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookprintingpreview) ve [**SheetPrintingPreview**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetprintingpreview) sınıflarını sağlar. Bütün çalışma kitabının yazdırma önizlemesini oluşturmak için, oluşturulan önizlemenin sayılarını almak için [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookprintingpreview) sınıfından bir örnek oluşturun ve [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) ve [**ImageOrPrintOptions**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions) nesnelerini yapıcıya geçirin. [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookprintingpreview) sınıfı, oluşturulan ön izlemin sayısını iade eden bir [**EvaluatedPageCount**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookprintingpreview/properties/evaluatedpagecount) yöntemi sağlar. Benzer şekilde, [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookprintingpreview) sınıfı, belirli bir çalışma sayfası için bir yazdırma önizlemesi oluşturmak için kullanılır. Bir çalışma sayfasının yazdırma önizlemesini oluşturmak için, [**SheetPrintingPreview**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetprintingpreview) sınıfından bir örnek oluşturun ve yapıcıya [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) ve [**ImageOrPrintOptions**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions) nesnelerini geçirin. [**SheetPrintingPreview**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetprintingpreview) sınıfı, ayrıca üretilen ön izlemin sayısını iade eden bir [**EvaluatedPageCount**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetprintingpreview/properties/evaluatedpagecount) yöntemi sağlar.

Aşağıdaki kod parçası, [örnek excel dosyası](94896177.xlsx) kullanılarak hem [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookprintingpreview) hem de [**SheetPrintingPreview**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetprintingpreview) sınıflarının nasıl kullanılacağını göstermektedir.

### **Örnek Kod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-PrintPreview-1.cs" >}}

Yukarıdaki kodun yürütülmesiyle oluşturulan çıktı aşağıdaki gibidir.

### **Konsol Çıktısı**

{{< highlight java >}}

Workbook page count: 1
Worksheet page count: 1

{{< /highlight >}}

## **Gelişmiş Konular**
- [Elektronik Tabloları Görüntüleme Yazı Tiplerini Yapılandırma](/cells/tr/net/configuring-fonts-for-rendering-spreadsheets/)
- [Çalışma Sayfasını Görüntüye Dönüştür - Veri etrafındaki boşlukları kaldır](/cells/tr/net/convert-worksheet-to-image-remove-whitespace-around-data/)
- [Çalışsayısı veya Sayfa Görseline ve Sayfa Sayfasına Çalışsayısı Dönüştürme](/cells/tr/net/converting-worksheet-to-image-and-worksheet-to-image-by-page/)
- [ImageOrPrint Seçenekleri Kullanarak Çalışma Sayfasını Görüntüye Dönüştürme](/cells/tr/net/converting-worksheet-to-image-using-imageorprint-options/)
- [Bir Çalışma Sayfasındaki Hücre Aralığını Görüntüye Aktar](/cells/tr/net/export-range-of-cells-in-a-worksheet-to-image/)
- [Belirtilen Genişlik ve Yükseklikte Çalışsayısı veya Tabloyu Resme Dışa Aktarma](/cells/tr/net/export-worksheet-or-chart-into-image-with-desired-width-and-height/)
- [ImageOrPrintOptions Kullanarak Çalışma Sayfalarından Resimleri Çıkarma](/cells/tr/net/extract-images-from-worksheets-using-imageorprintoptions/)
- [Çalışma Sayfasının Önizlemesini Oluşturun](/cells/tr/net/generate-thumbnail-of-the-worksheet/)
- [Hiçbir şey Yazdırılacak Değilken Boş Sayfa Çıktısı](/cells/tr/net/output-blank-page-when-there-is-nothing-to-print/)
- [Sayfa Ayarları ve Yazdırma Seçenekleri](/cells/tr/net/page-setup-and-printing-options/)
- [SheetRender ve WorkbookRender Kullanarak Sayfaların Aralığını Yazdırma](/cells/tr/net/printing-range-of-pages-using-sheetrender-and-workbookrender/)
- [Görüntü veya Yazdırma Seçenekleri Kullanılarak Sayfa Dizisi Oluşturma](/cells/tr/net/render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions/)
- [Çalışsayısını Grafiksel Ortama Dönüştürme](/cells/tr/net/render-worksheet-to-graphic-context/)
- [Çalışma Kitabı Rendeleme İçin Bireysel veya Özel Font Kümesini Belirtin](/cells/tr/net/specify-individual-or-private-set-of-fonts-for-workbook-rendering/)
- [Aspose.Cells ile yazdırırken İş veya Belge Adı belirtin](/cells/tr/net/specify-job-or-document-name-while-printing-with-aspose-cells/)
{{< app/cells/assistant language="csharp" >}}
