---
title: Çalışma Kitabını Yazdır ve Önizle
linktitle: Yazdır ve Önizle
type: docs
weight: 70
url: /tr/python-net/workbook-and-worksheet-print-preview/
description: Aspose.Cells for Python via .NET, Microsoft Excel kurulumu olmadan Excel dosyalarını yazdırma ve önizleme desteği sağlar.
---

{{% alert color="primary" %}}

Bir çalışma sayfası oluşturduktan sonra, genellikle bir kopyasını yazdırmak istersiniz. Bu makale, Aspose.Cells for Python via .NET kullanarak elektronik tabloları nasıl yazdıracağınızı açıklar.

{{% /alert %}}

## **Yazdırma Girişi**

Microsoft Excel, seçim belirtmediğiniz sürece tüm çalışma sayfası alanını yazdırmak istediğinizi varsayar. Aspose.Cells for Python via .NET kullanarak yazdırmak için önce aspose.cells.rendering isim alanını programa eklemeniz gerekir. Bu alan, [**SheetRender**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender) ve [**WorkbookRender**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/workbookrender) gibi kullanışlı sınıflar içerir.

### **SheetRender Kullanarak Yazdır**

[**SheetRender**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender/) sınıfı bir çalışma sayfasını temsil eder ve [**to_printer**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender/to_printer/) yöntemine sahiptir, bu yöntem bir çalışma sayfasını yazdırabilir. Aşağıdaki örnek kod, bir çalışma sayfasını nasıl yazdıracağınızı gösterir.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-PrintingExcelWorkbookUsingSheetRender.py" >}}

### **WorkbookRender Kullanarak Yazdır**

Bütün çalışma kitabını yazdırmak için sayfalar üzerinde döngü yapın ve onları yazdırın veya [**WorkbookRender**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/workbookrender) sınıfını kullanın.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-PrintingUsingWorkbookRender-1.py" >}}

{{% alert color="primary" %}}

Aspose.Cells for Python via .NET, ayrıca [**WorkbookRender.to_printer()**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender/to_printer/#str-str) ve [**SheetRender.to_printer()**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender/to_printer/#aspose.pydrawing.printing.PrinterSettings) metodlarının aşırı yüklemelerini de sağlar; böylece, Excel elektronik tablolarını yazdırırken yazdırma işleri adını ayarlamak mümkündür. Varsayılan olarak, tüm yazdırma işleri "Belge" adıyla oluşturulur.

{{% /alert %}}

## **Yazdırma Önizlemesi**

Milyonlarca sayfalı Excel dosyalarının PDF veya görüntüye dönüştürülmesi gereken durumlar olabilir. Bu tür dosyaların işlenmesi çok zaman ve kaynak tüketebilir. Bu durumlarda, Çalışma Kitabı ve Çalışma Sayfası Yazdırma Önizlemesi özelliği faydalı olabilir. Kullanıcı, dosyanın dönüştürülmeden önce toplam sayfa sayısını kontrol edebilir ve dönüştürülüp dönüştürülmeyeceğine karar verebilir. Bu makale, toplam sayfa sayısını öğrenmek için [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/workbookprintingpreview) ve [**SheetPrintingPreview**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetprintingpreview) sınıflarını kullanmayı ele almaktadır.

Aspose.Cells for Python via .NET, yazdırma önizleme özelliği sağlar. Bunun için API [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/workbookprintingpreview) ve [**SheetPrintingPreview**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetprintingpreview) sınıflarını sunar. Tüm çalışma kitabının yazdırma önizlemesini oluşturmak için, [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/workbookprintingpreview) sınıfının bir örneğini oluşturun ve yapıcıya [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) ve [**ImageOrPrintOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions) nesnelerini geçirin. [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/workbookprintingpreview) sınıfı, oluşturulan önizlemedeki sayfa sayısını döndüren bir [**evaluated_page_count**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/workbookprintingpreview/evaluated_page_count/) metod sağlar. [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/workbookprintingpreview) sınıfına benzer şekilde, [**SheetPrintingPreview**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetprintingpreview) sınıfı, belirli bir çalışma sayfası için yazdırma önizlemesi oluşturmakta kullanılır. Bir çalışma sayfasının yazdırma önizlemesini oluşturmak için, [**SheetPrintingPreview**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetprintingpreview) sınıfının bir örneğini oluşturun ve yapıcıya [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) ve [**ImageOrPrintOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions) nesnelerini geçirin. [**SheetPrintingPreview**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetprintingpreview) sınıfı ayrıca, oluşturulan önizlemedeki sayfa sayısını döndüren bir [**SheetPrintingPreview.evaluated_page_count**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetprintingpreview/evaluated_page_count/) metod sağlar.

Aşağıdaki kod parçası, [örnek excel dosyası](94896177.xlsx) kullanılarak hem [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/workbookprintingpreview) hem de [**SheetPrintingPreview**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetprintingpreview) sınıflarının nasıl kullanılacağını göstermektedir.

### **Örnek Kod**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-PrintPreview-1.py" >}}

Yukarıdaki kodun yürütülmesiyle oluşturulan çıktı aşağıdaki gibidir.

### **Konsol Çıktısı**

{{< highlight java >}}

Workbook page count: 1
Worksheet page count: 1

{{< /highlight >}}

{{< app/cells/assistant language="python-net" >}}
