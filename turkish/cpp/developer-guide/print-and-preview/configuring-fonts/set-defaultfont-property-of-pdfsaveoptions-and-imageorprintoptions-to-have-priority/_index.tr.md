---
title: C++ ile PdfSaveOptions ve ImageOrPrintOptions un DefaultFont özelliğini öncelikli hale getirin
linktitle: PdfSaveOptions ve ImageOrPrintOptions ın DefaultFont özelliğinin önceliği olması
type: docs
weight: 30
url: /tr/cpp/set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority/
description: Aspose.Cells ile belgeleri kaydederken yazı tipi ayarlarını önceliklendirmeyi öğrenin.
---

## **Olası Kullanım Senaryoları**

[**PdfSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/) ve [**ImageOrPrintOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/) **DefaultFont** özelliğini ayarlarken, PDF veya görüntüye kaydetmenin eksik (yüklü olmayan) bir yazı tipi karakterine sahip çalışma kitabındaki tüm metni ayarlayacağınızı bekleyebilirsiniz.

Genellikle PDF veya görsel olarak kaydederken, Aspose.Cells ilk olarak çalışma kitabının varsayılan yazı tipi (yani, Workbook.DefaultStyle.Font) ayarlamaya çalışır. Eğer çalışma kitabının varsayılan yazı tipi metni düzgün gösteremiyorsa veya render etmedi ise, Aspose.Cells, [**PdfSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/) içindeki DefaultFont öznitesi karşısında belirtilen yazı tipiyle render etmeye çalışacaktır.

İsteğinize uygun olarak, [**PdfSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/) içerisinde "**CheckWorkbookDefaultFont**" adlı bir Boolean özelliği bulunmaktadır. Bu özelliği **false** yaparak çalışma kitabının varsayılan yazı tipini denemeyi devre dışı bırakabilir veya [**PdfSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/) içindeki **DefaultFont** ayarına öncelik tanıyabilirsiniz.

## **PdfSaveOptions/ImageOrPrintOptions'ın DefaultFont özelliğini ayarlayın**

Aşağıdaki örnek kod, bir Excel dosyasını açar. İlk çalışma sayfasındaki A1 hücresinde "Christmas Time Font text" metni ayarlanmıştır. Yazı tipi adı "Christmas Time Personal Use" olup, makineye yüklenmemiştir. {0}/{1} içindeki **DefaultFont** özniteliğini "Times New Roman" olarak ayarlarız. Ayrıca, {2}/{3} içindeki Boolean özellik olan **CheckWorkbookDefaultFont**'u **"false"** olarak ayarlarız, böylece A1 hücresinin metni "Times New Roman" fontu ile render edilir ve çalışma kitabının varsayılan fontu (bu durumda "Calibri") kullanılmaz. Kod, ilk çalışma sayfasını PNG ve TIFF görüntü formatlarına render eder. Son olarak, PDF dosya formatına render edilir.

{{% alert color="primary" %}}

**CheckWorkbookDefaultFont** özelliğinin varsayılan değeri **true**'dur.

{{% /alert %}}

Bu, örnek kodda kullanılan [şablon dosyası](49446913.xlsx) ekran görüntüsüdür.

![todo:image_alt_text](set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority_1.png)

Bu, [**ImageOrPrintOptions.GetDefaultFont()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getdefaultfont/) özelliği "Times New Roman" olarak ayarlandıktan sonra oluşan çıktı PNG görüntüsüdür.

![todo:image_alt_text](set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority_2.png)

[**ImageOrPrintOptions.GetDefaultFont()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getdefaultfont/) özelliği "Times New Roman" olarak ayarlandıktan sonra ortaya çıkan [TIFF](48496672.tiff) görüntüsüne bakın.

[PDF](48496673.pdf) dosya çıktıktan sonra, [**PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)**](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/~paginatedsaveoptions/) özelliği "Times New Roman" olarak ayarlandığında.

## **Örnek Kod**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Input and output directory path
    U16String sourceDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outputDir(u"..\\Data\\02_OutputDirectory\\");

    // Open an Excel file
    Workbook workbook(sourceDir + u"sampleSetDefaultFontPropertyOfPdfSaveOptionsAndImageOrPrintOptions.xlsx");

    // Rendering to PNG file format while setting the CheckWorkbookDefaultFont attribute to false.
    // So, "Times New Roman" font would be used for any missing (not installed) font in the workbook.
    ImageOrPrintOptions imgOpt;
    imgOpt.SetImageType(ImageType::Png);
    imgOpt.SetCheckWorkbookDefaultFont(false);
    imgOpt.SetDefaultFont(u"Times New Roman");

    // Create a SheetRender instance for the first worksheet and render to PNG.
    SheetRender sr(workbook.GetWorksheets().Get(0), imgOpt);
    sr.ToImage(0, outputDir + u"out1_imagePNG.png");

    // Rendering to TIFF file format while setting the CheckWorkbookDefaultFont attribute to false.
    imgOpt.SetImageType(ImageType::Tiff);
    WorkbookRender wr(workbook, imgOpt);
    wr.ToImage(outputDir + u"out1_imageTIFF.tiff");

    // Rendering to PDF file format while setting the CheckWorkbookDefaultFont attribute to false.
    PdfSaveOptions saveOptions;
    saveOptions.SetDefaultFont(u"Times New Roman");
    saveOptions.SetCheckWorkbookDefaultFont(false);

    // Save the workbook as PDF
    workbook.Save(outputDir + u"out1_pdf.pdf", saveOptions);

    std::cout << "Files exported successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
