---
title: C++ ile Çalışma Kitabını Yazdır ve Önizle
linktitle: Yazdır ve Önizle
type: docs
weight: 70
url: /tr/cpp/workbook-and-worksheet-print-preview/
description: Aspose.Cells, C++ kullanarak Microsoft Excel yüklemeye gerek kalmadan Excel dosyalarını yazdırma ve önizleme özelliği destekler.
---

{{% alert color="primary" %}}

Bir çalışma sayfası oluşturduktan sonra genellikle onun kağıt çıktısını almak istersiniz. Bu makale, Aspose.Cells ile elektronik tabloları nasıl yazdıracağınızı açıklar.

{{% /alert %}}

## **Yazdırma Girişi**

Microsoft Excel, bir seçim belirtmediğiniz sürece, bütün çalışma sayfası alanını yazdırmayı varsayar. Aspose.Cells kullanarak yazdırmak için önce Aspose.Cells.Rendering isim alanını programa içe aktarın. Örneğin, [**SheetRender**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/) ve [**WorkbookRender**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/workbookrender/) gibi birçok kullanışlı sınıf bulunmaktadır.


## **Yazdırma Önizlemesi**

Milyonlarca sayfalı Excel dosyalarının PDF veya görüntüye dönüştürülmesi gereken durumlar olabilir. Bu tür dosyaların işlenmesi çok zaman ve kaynak tüketebilir. Bu durumlarda, Çalışma Kitabı ve Çalışma Sayfası Yazdırma Önizlemesi özelliği faydalı olabilir. Kullanıcı, dosyanın dönüştürülmeden önce toplam sayfa sayısını kontrol edebilir ve dönüştürülüp dönüştürülmeyeceğine karar verebilir. Bu makale, toplam sayfa sayısını öğrenmek için [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/workbookprintingpreview/) ve [**SheetPrintingPreview**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetprintingpreview/) sınıflarını kullanmayı ele almaktadır.

Aspose.Cells, yazdırma önizlemesi özelliğini sağlar. Bunun için API, [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/workbookprintingpreview/) ve [**SheetPrintingPreview**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetprintingpreview/) sınıflarını sağlar. Bütün çalışma kitabının yazdırma önizlemesini oluşturmak için, oluşturulan önizlemenin sayılarını almak için [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/workbookprintingpreview/) sınıfından bir örnek oluşturun ve [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) ve [**ImageOrPrintOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/) nesnelerini yapıcıya geçirin. [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/workbookprintingpreview/) sınıfı, oluşturulan ön izlemin sayısını iade eden bir [**GetEvaluatedPageCount()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/workbookprintingpreview/getevaluatedpagecount/) yöntemi sağlar. Benzer şekilde, [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/workbookprintingpreview/) sınıfı, belirli bir çalışma sayfası için bir yazdırma önizlemesi oluşturmak için kullanılır. Bir çalışma sayfasının yazdırma önizlemesini oluşturmak için, [**SheetPrintingPreview**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetprintingpreview/) sınıfından bir örnek oluşturun ve yapıcıya [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) ve [**ImageOrPrintOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/) nesnelerini geçirin. [**SheetPrintingPreview**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetprintingpreview/) sınıfı, ayrıca üretilen ön izlemin sayısını iade eden bir [**GetEvaluatedPageCount()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetprintingpreview/getevaluatedpagecount/) yöntemi sağlar.

Aşağıdaki kod parçası, [örnek excel dosyası](94896177.xlsx) kullanılarak hem [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/workbookprintingpreview/) hem de [**SheetPrintingPreview**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetprintingpreview/) sınıflarının nasıl kullanılacağını göstermektedir.

### **Örnek Kod**

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace std;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Create workbook object
    Workbook workbook(srcDir + u"Book1.xlsx");

    // Create image or print options
    ImageOrPrintOptions imgOptions;

    // Create workbook printing preview
    WorkbookPrintingPreview preview(workbook, imgOptions);
    cout << "Workbook page count: " << preview.GetEvaluatedPageCount() << endl;

    // Create sheet printing preview
    SheetPrintingPreview preview2(workbook.GetWorksheets().Get(0), imgOptions);
    cout << "Worksheet page count: " << preview2.GetEvaluatedPageCount() << endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

Yukarıdaki kodun yürütülmesiyle oluşturulan çıktı aşağıdaki gibidir.

### **Konsol Çıktısı**

{{< highlight java >}}

Workbook page count: 1
Worksheet page count: 1

{{< /highlight >}}

## **Gelişmiş Konular**
- [Elektronik Tabloları Görüntüleme Yazı Tiplerini Yapılandırma](/cells/tr/cpp/configuring-fonts-for-rendering-spreadsheets/)
- [Çalışma Sayfasını Görüntüye Dönüştür - Veri etrafındaki boşlukları kaldır](/cells/tr/cpp/convert-worksheet-to-image-remove-whitespace-around-data/)
- [Çalışsayısı veya Sayfa Görseline ve Sayfa Sayfasına Çalışsayısı Dönüştürme](/cells/tr/cpp/converting-worksheet-to-image-and-worksheet-to-image-by-page/)
- [ImageOrPrint Seçenekleri Kullanarak Çalışma Sayfasını Görüntüye Dönüştürme](/cells/tr/cpp/converting-worksheet-to-image-using-imageorprint-options/)
- [Bir Çalışma Sayfasındaki Hücre Aralığını Görüntüye Aktar](/cells/tr/cpp/export-range-of-cells-in-a-worksheet-to-image/)
- [Belirtilen Genişlik ve Yükseklikte Çalışsayısı veya Tabloyu Resme Dışa Aktarma](/cells/tr/cpp/export-worksheet-or-chart-into-image-with-desired-width-and-height/)
- [ImageOrPrintOptions Kullanarak Çalışma Sayfalarından Resimleri Çıkarma](/cells/tr/cpp/extract-images-from-worksheets-using-imageorprintoptions/)
- [Çalışma Sayfasının Önizlemesini Oluşturun](/cells/tr/cpp/generate-thumbnail-of-the-worksheet/)
- [Hiçbir şey Yazdırılacak Değilken Boş Sayfa Çıktısı](/cells/tr/cpp/output-blank-page-when-there-is-nothing-to-print/)
- [Sayfa Ayarları ve Yazdırma Seçenekleri](/cells/tr/cpp/page-setup-and-printing-options/)
- [Görüntü veya Yazdırma Seçenekleri Kullanılarak Sayfa Dizisi Oluşturma](/cells/tr/cpp/render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions/)
- [Çalışsayısını Grafiksel Ortama Dönüştürme](/cells/tr/cpp/render-worksheet-to-graphic-context/)
- [Çalışma Kitabı Rendeleme İçin Bireysel veya Özel Font Kümesini Belirtin](/cells/tr/cpp/specify-individual-or-private-set-of-fonts-for-workbook-rendering/)
