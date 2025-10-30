---
title: Çalışma Sayfasını Görüntüye Dönüştür  Veri Çevresindeki Boşlukları Kaldırma  C++
linktitle: Çalışma Sayfasını Görüntüye Dönüştür  Veri Çevresindeki Boşlukları Kaldırma
type: docs
weight: 40
url: /tr/cpp/convert-worksheet-to-image-remove-whitespace-around-data/
description: Aspose.Cells for C++ kullanarak bir çalışma sayfasını görüntüye dönüştürmeyi ve verilerin etrafındaki boşlukları kaldırmayı nasıl yapacağınızı öğrenin.
---

{{% alert color="primary" %}}

Bazen, çalışma sayfalarını uygulamalarda veya web sayfalarında sunmanız gerekebilir. Örneğin, çalışma sayfalarını bir Word belgesine, bir PDF dosyasına, bir PowerPoint sunumuna veya başka bir belgeye yerleştirmeniz gerekebilir. Temelde, bir çalışma sayfasını bir görüntü olarak oluşturmak ve başka uygulamalara yapıştırmak istersiniz. Aspose.Cells, Microsoft Excel çalışma sayfalarını görüntülere dönüştürmenizi sağlar.

{{% /alert %}}

## **Veri Etrafındaki Boşlukları Kaldır**

[**SheetRender**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/) API'si, örneğin görüntü biçimi, sayfa sayfalama çalışma sayfaları vb. gibi belirli özelliklere sahip bir çalışma sayfasını bir görüntü dosyasına dönüştürür. BMP, GIF, JPG, TIFF ve EMF gibi birçok görüntü formatı desteklenir.

Sayfa dolu olduğunda, varsayılan olarak çıktıya boşluk yani kenarlık eklenir. Bunu kaldırmak için, kaynak çalışma sayfası için üst, alt, sol ve sağ sayfa ayar marjlarını 0 yapabilir ve [**ImageOrPrintOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/) özelliklerini uygun şekilde belirleyebilirsiniz.

Aşağıdaki kod parçası, çıktı görüntüsündeki veri etrafındaki boşluğu kaldırır.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Open the template file
    Workbook book(srcDir + u"Book1.xlsx");

    // Get the first worksheet
    Worksheet sheet = book.GetWorksheets().Get(0);

    // Define LoadOptions and set LoadFilter
    LoadOptions options;
    options.SetLoadFilter(new LoadFilter(LoadDataFilterOptions::All));

    // Specify your print area if you want
    // sheet.GetPageSetup().SetPrintArea(u"A1:H8");

    // To remove the white border around the image.
    sheet.GetPageSetup().SetLeftMargin(0);
    sheet.GetPageSetup().SetRightMargin(0);
    sheet.GetPageSetup().SetBottomMargin(0);
    sheet.GetPageSetup().SetTopMargin(0);

    // Define ImageOrPrintOptions
    ImageOrPrintOptions imgOptions;
    imgOptions.SetImageType(Aspose::Cells::Drawing::ImageType::Emf);

    // Set only one page would be rendered for the image
    imgOptions.SetOnePagePerSheet(true);
    imgOptions.SetPrintingPage(PrintingPageType::IgnoreBlank);

    // Create the SheetRender object based on the sheet with its
    // ImageOrPrintOptions attributes
    SheetRender sr(sheet, imgOptions);

    // Convert the image
    sr.ToImage(0, outDir + u"outputRemoveWhitespaceAroundData.emf");

    std::cout << "Image converted successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
