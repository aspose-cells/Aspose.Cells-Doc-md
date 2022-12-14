---
title: Çalışma kitabını Yazdır ve Önizle
linktitle: Yazdır ve Önizle
type: docs
weight: 70
url: /tr/net/workbook-and-worksheet-print-preview/
description: Aspose.Cells, Microsoft Excel kurulumu olmadan Excel dosyalarını yazdırmayı ve önizlemeyi destekler.
---
{{% alert color="primary" %}}

Bir çalışma sayfası oluşturduktan sonra, genellikle bunun basılı bir kopyasını yazdırmak istersiniz. Bu makalede, Aspose.Cells ile elektronik tabloların nasıl yazdırılacağı açıklanmaktadır.

{{% /alert %}}

## **Basılı Tanıtım**

Microsoft Excel, bir seçim belirtmediğiniz sürece tüm çalışma sayfası alanını yazdırmak istediğinizi varsayar. Aspose.Cells kullanarak yazdırmak için önce Aspose.Cells.Rendering ad alanını programa alın. Birkaç faydalı sınıfı vardır, örneğin,[**SheetRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender) ve[**Çalışma KitabıRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookrender).

### **SheetRender Kullanarak Yazdırma**

 bu[**Aspose.Cells.Rendering.SheetRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender) class bir çalışma sayfasını temsil eder ve[**Yazıcıya**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender/methods/toprinter/index)bir çalışma sayfası yazdırabilen yöntem. Aşağıdaki örnek kod, bir çalışma sayfasının nasıl yazdırılacağını gösterir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-PrintingUsingSheetRender-PrintingExcelWorkbookUsingSheetRender.cs" >}}

### **WorkbookRender'ı Kullanarak Yazdırma**

 Bütün bir çalışma kitabını yazdırmak için, sayfaları yineleyin ve yazdırın veya[**Çalışma KitabıRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookrender)sınıf.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-PrintingUsingWorkbookRender-1.cs" >}}

{{% alert color="primary" %}}

 Aspose.Cells ayrıca aşırı yükleme sağlar.[**WorkbookRender.ToPrinter()**](https://reference.aspose.com/cells/net/aspose.cells.rendering.workbookrender/toprinter/methods/3) ve[**SheetRender.ToPrinter()**](https://reference.aspose.com/cells/net/aspose.cells.rendering.sheetrender/toprinter/methods/2) yöntemleri, böylece Excel elektronik tablolarını yazdırırken yazdırma işi adını ayarlamak mümkündür. Varsayılan olarak, tüm yazdırma işleri "Belge" adıyla oluşturulur.

{{% /alert %}}

## **Baskı Önizleme**

Milyonlarca sayfa içeren Excel dosyalarının PDF'ye veya resimlere dönüştürülmesi gereken durumlar olabilir. Bu tür dosyaların işlenmesi çok fazla zaman ve kaynak tüketecektir. Bu gibi durumlarda, Çalışma Kitabı ve Çalışma Sayfası Baskı Önizleme özelliği yararlı olabilir. Bu tür dosyaları dönüştürmeden önce, kullanıcı toplam sayfa sayısını kontrol edebilir ve ardından dosyanın dönüştürülüp dönüştürülmeyeceğine karar verebilir. Bu makale,[**Çalışma KitabıYazdırmaÖnizleme**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookprintingpreview)ve[**SheetPrintingÖnizleme**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetprintingpreview)toplam sayfa sayısını öğrenmek için sınıflar.

 Aspose.Cells, baskı ön izleme özelliği sağlar. Bunun için API şunları sağlar:[**Çalışma KitabıYazdırmaÖnizleme**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookprintingpreview) ve[**SheetPrintingÖnizleme**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetprintingpreview) sınıflar. Tüm çalışma kitabının baskı ön izlemesini oluşturmak için,[**Çalışma KitabıYazdırmaÖnizleme**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookprintingpreview) geçerek sınıf[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook) ve[**ResimVeyaBaskıSeçenekleri**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions) yapıcıya nesneler. bu[**Çalışma KitabıYazdırmaÖnizleme**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookprintingpreview) sınıf bir sağlar[**Değerlendirilen Sayfa Sayısı**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookprintingpreview/properties/evaluatedpagecount) oluşturulan önizlemedeki sayfa sayısını döndüren yöntem. Benzer[**Çalışma KitabıYazdırmaÖnizleme**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookprintingpreview)sınıf,[**SheetPrintingÖnizleme**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetprintingpreview)class, belirli bir çalışma sayfası için bir baskı ön izleme oluşturmak için kullanılır. Bir çalışma sayfasının baskı ön izlemesini oluşturmak için,[**SheetPrintingÖnizleme**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetprintingpreview)geçerek sınıf[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)ve[**ResimVeyaBaskıSeçenekleri**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions)yapıcıya nesneler. bu[**SheetPrintingÖnizleme**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetprintingpreview)sınıf ayrıca bir[**Değerlendirilen Sayfa Sayısı**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetprintingpreview/properties/evaluatedpagecount)oluşturulan önizlemedeki sayfa sayısını döndüren yöntem.

Aşağıdaki kod parçacığı, her ikisinin de kullanımını gösterir.[**Çalışma KitabıYazdırmaÖnizleme**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookprintingpreview)ve[**SheetPrintingÖnizleme**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetprintingpreview) sınıfları kullanarak[örnek excel dosyası](94896177.xlsx).

### **Basit kod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-PrintPreview-1.cs" >}}

Yukarıdaki kod yürütülerek oluşturulan çıktı aşağıdadır.

### **Konsol Çıkışı**

Çalışma kitabı sayfa sayısı: 1
Çalışma sayfası sayfa sayısı: 1


## **ileri konular**
- [Elektronik Tabloları Oluşturmak için Yazı Tiplerini Yapılandırma](/cells/tr/net/configuring-fonts-for-rendering-spreadsheets/)
- [Çalışma Sayfasını Görüntüye Dönüştür - Verilerin etrafındaki boşlukları kaldırın](/cells/tr/net/convert-worksheet-to-image-remove-whitespace-around-data/)
- [Çalışma Sayfasını Görüntüye ve Çalışma Sayfasını Görüntüye Sayfa Sayfa Dönüştürme](/cells/tr/net/converting-worksheet-to-image-and-worksheet-to-image-by-page/)
- [ImageOrPrint Seçeneklerini Kullanarak Çalışma Sayfasını Görüntüye Dönüştürme](/cells/tr/net/converting-worksheet-to-image-using-imageorprint-options/)
- [Çalışma Sayfasındaki Cells Aralığını Görüntüye Dışa Aktar](/cells/tr/net/export-range-of-cells-in-a-worksheet-to-image/)
- [Çalışma Sayfasını veya Grafiği İstenilen Genişlik ve Yükseklikte Görüntüye Aktarın](/cells/tr/net/export-worksheet-or-chart-into-image-with-desired-width-and-height/)
- [ImageOrPrintOptions kullanarak Çalışma Sayfalarından Görüntüleri Çıkarın](/cells/tr/net/extract-images-from-worksheets-using-imageorprintoptions/)
- [Çalışma Sayfasının Küçük Resmini Oluştur](/cells/tr/net/generate-thumbnail-of-the-worksheet/)
- [Yazdırılacak Hiçbir Şey Olmadığında Boş Sayfa Çıktısı](/cells/tr/net/output-blank-page-when-there-is-nothing-to-print/)
- [Sayfa Yapısı ve Yazdırma Seçenekleri](/cells/tr/net/page-setup-and-printing-options/)
- [SheetRender ve WorkbookRender kullanarak Sayfa Aralığını Yazdırma](/cells/tr/net/printing-range-of-pages-using-sheetrender-and-workbookrender/)
- [ImageOrPrintOptions'ın PageIndex ve PageCount Özelliklerini Kullanarak Sayfa Sırasını Oluşturun](/cells/tr/net/render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions/)
- [Çalışma Sayfasını Grafik Bağlamına Dönüştür](/cells/tr/net/render-worksheet-to-graphic-context/)
- [Çalışma Kitabı Oluşturma için Bireysel veya Özel Yazı Tipi Kümesi Belirtin](/cells/tr/net/specify-individual-or-private-set-of-fonts-for-workbook-rendering/)
- [Aspose.Cells ile yazdırırken İş veya Belge Adını belirtin](/cells/tr/net/specify-job-or-document-name-while-printing-with-aspose-cells/)
