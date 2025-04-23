---
title: Excel’i Resme Dönüştürme (C++ ile)
linktitle: Excel i Resme Dönüştür
type: docs
weight: 300
url: /tr/cpp/convert-excel-to-image/
description: Excel çalışma sayfalarının TIFF ve SVG formatları dahil olmak üzere görüntülere nasıl dönüştürüleceğini öğrenin, Aspose.Cells for C++ kullanılarak.
---

{{% alert color="primary" %}}

Aspose.Cells, bir çalışma kitabından çalışsayı dışa aktarmanıza ve farklı biçimlere dönüştürmenize olanak tanır. Bu makale, bir çalışsayının farklı biçimlere nasıl dönüştürüleceğini açıklar.

{{% /alert %}}

## Çalışma Kitabını TIFF'e Dönüştürme

Bir Excel dosyası çok sayfa ve çok sayfa içerebilir. [**WorkbookRender**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/workbookrender/) kullanarak Excel’i çok sayfalı TIFF formatına dönüştürebilirsiniz. Ayrıca, TIFF için [Sıkıştırma](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/tiffcompression/), [GetTiffColorDepth()](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/gettiffcolordepth/), Çözünürlük ([GetHorizontalResolution()](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/gethorizontalresolution/), [GetVerticalResolution()](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getverticalresolution/)).

Aşağıdaki kod örneği, birden çok sayfa içeren Excel dosyasını TIFF'e nasıl dönüştüreceğinizi gösterir. [Kaynak Excel dosyası](workbook-to-tiff-with-mulitiple-pages.xlsx) ve [oluşturulan TIFF görüntüsü](workbook-to-tiff-with-mulitiple-pages.tiff) referansınız için ekli.

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main() {
    Aspose::Cells::Startup();

    // Load the workbook
    Workbook wb(u"workbook-to-tiff-with-mulitiple-pages.xlsx");

    // Create image options
    ImageOrPrintOptions imgOptions;
    imgOptions.SetImageType(ImageType::Tiff);

    // Set resolution to 200 DPI
    imgOptions.SetHorizontalResolution(200);
    imgOptions.SetVerticalResolution(200);

    // Set TIFF compression to LZW
    imgOptions.SetTiffCompression(TiffCompression::CompressionLZW);

    // Render the workbook to TIFF
    WorkbookRender workbookRender(wb, imgOptions);
    workbookRender.ToImage(u"workbook-to-tiff-with-mulitiple-pages.tiff");

    std::cout << "Workbook rendered to TIFF successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Çalışsayıyı Görüntüye Dönüştürme**

Çalışma sayfaları analiz etmek istediğiniz verileri içerebilir. Örneğin, bir çalışma sayfası parametreleri, toplamları, yüzdeleri, istisnaları ve hesaplamaları içerebilir.

Bir geliştirici olarak, çalışma sayfalarını görüntü olarak sunmanız gerekebilir. Örneğin, bir çalışma sayfasının bir görüntüsünü bir uygulamada veya web sayfasında kullanmanız gerekebilir. Bir çalışma sayfasını bir Microsoft Word belgesine, bir PDF dosyasına, bir PowerPoint sunumuna veya başka bir belge türüne eklemek isteyebilirsiniz. Basitçe söylemek gerekirse, bir çalışma sayfasını bir görüntü olarak oluşturmak istiyorsunuz ki başka bir yerde kullanabilesiniz.

Aspose.Cells, Excel çalışma sayfalarını görüntüye dönüştürme desteği sağlar. Bu özelliği kullanmak için, programınıza veya projenize [**Aspose.Cells.Rendering**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/) ad alanını içe aktarmanız gerekir. Bu, gösterim ve yazdırma için birkaç değerli sınıfa sahiptir, örneğin [**SheetRender**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/), [**ImageOrPrintOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/), [**WorkbookRender**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/workbookrender/) ve diğerleri.

[**SheetRender**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/) sınıfı, görüntüler olarak render edilecek bir çalışma sayfasını temsil eder. [**ToImage**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/toimage/) adlı aşırı yüklenmiş bir yöntemi vardır; bu, bir çalışma sayfasını farklı özellikler veya seçeneklerle resim dosyasına dönüştürebilir. Bir `System.Drawing.Bitmap` nesnesi döndürür ve bir resim dosyasını disk veya akışa kaydedebilirsiniz. Birkaç resim formatı desteklenir, örneğin BMP, PNG, GIF, JPG, JPEG, TIFF, EMF.

Aşağıdaki kod örneği, bir Excel dosyasındaki bir çalışma sayfasını bir görüntü dosyasına dönüştürmenin nasıl yapıldığını gösterir.

```cpp
#include <iostream>
#include <string>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;
using namespace Aspose::Cells::Rendering;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook book(srcDir + u"sampleConvertWorksheetToImageByPage.xlsx");
    Worksheet sheet = book.GetWorksheets().Get(0);

    ImageOrPrintOptions options;
    options.SetHorizontalResolution(200);
    options.SetVerticalResolution(200);
    options.SetImageType(ImageType::Tiff);

    SheetRender sr(sheet, options);
    for (int j = 0; j < sr.GetPageCount(); j++)
    {
        std::wstring numStr = std::to_wstring(j + 1);
        U16String numU16Str(reinterpret_cast<const char16_t*>(numStr.c_str()));
        U16String outputPath = outDir + U16String(u"outputConvertWorksheetToImageByPage_") + numU16Str + U16String(u".tif");
        sr.ToImage(j, outputPath);
    }

    std::cout << "Worksheet converted to images by page successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

Şu anda, çalışma sayfalarını görüntülere dönüştürmek için API, 3D kabarcık grafiklerini desteklememektedir.

{{% /alert %}}

## **Çalışma Sayfasını SVG'ye Dönüştürme**

SVG, Ölçeklenebilir Vektör Grafikleri anlamına gelir. SVG, iki boyutlu vektör grafikleri için XML standartlarına dayanan bir spesifikasyondur. 1999'dan beri World Wide Web Consortium (W3C) tarafından geliştirilen açık bir standarttır.

Aspose.Cells for C++, sürüm 7.1.0’den itibaren çalışma sayfalarını SVG görüntüsüne dönüştürmeyi başardı. Aşağıdaki kod parçası, bir Excel dosyasındaki çalışma sayfasını SVG dosyasına dönüştürmenin nasıl yapılacağını gösterir.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Output directory
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Instantiate a workbook
    Workbook workbook;

    // Put sample text in the first cell of first worksheet in the newly created workbook
    workbook.GetWorksheets().Get(0).GetCells().Get(u"A1").SetValue(u"DEMO TEXT ON SHEET1");

    // Add second worksheet in the workbook
    workbook.GetWorksheets().Add(SheetType::Worksheet);

    // Set text in first cell of the second sheet
    workbook.GetWorksheets().Get(1).GetCells().Get(u"A1").SetValue(u"DEMO TEXT ON SHEET2");

    // Set currently active sheet index to 1 i.e. Sheet2
    workbook.GetWorksheets().SetActiveSheetIndex(1);

    // Save workbook to SVG. It shall render the active sheet only to SVG
    workbook.Save(outDir + u"ConvertWorksheetToSVG_out.svg");

    std::cout << "Worksheet converted to SVG successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Gelişmiş Konular**
- [Bir Excel Grafiğini Görüntüye Dönüştürme](/cells/tr/cpp/convert-an-excel-chart-to-image/)
- [SVG Biçiminde Grafikleri Görüntüye Dönüştürme](/cells/tr/cpp/converting-chart-to-image-in-svg-format/)
- [Görünüm Kutusu Özelliği ile Grafiksel Bir Ortama Tabloyu Dışa Aktarma](/cells/tr/cpp/export-chart-to-svg-with-viewbox-attribute/)
- [Excel'den TIFF'e Dönüşüm İlerlemesini İzle](/cells/tr/cpp/track-conversion-progress-of-excel-to-tiff/)
