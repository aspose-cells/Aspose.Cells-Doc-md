---
title: C++ ile Çalışma Kitabı veya Çalışma Sayfası Yüklenirken Nesneleri Filtrele
linktitle: Çalışma Kitabı veya Çalışsayfa Yüklenirken Nesneleri Filtrele
type: docs
weight: 330
url: /tr/cpp/filter-objects-while-loading-workbook-or-worksheet/
description: Aspose.Cells for C++ kullanarak çalışma kitapları veya çalışma sayfaları yüklenirken grafikler, şekiller ve koşullu biçimlendirme gibi nesneleri nasıl filtreleyeceğinizi öğrenin.
---

## **Olası Kullanım Senaryoları**
 Lütfen çalışma kitabından verileri filtrelerken [LoadOptions.GetLoadFilter()](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/getloadfilter/) özelliğini kullanın. Ancak, bireysel çalışma sayfalarından veri filtrelemek istiyorsanız, o zaman [LoadFilter.StartSheet](https://reference.aspose.com/cells/cpp/aspose.cells/loadfilter/startsheet/) yöntemini geçersiz kılmalısınız. Lütfen [LoadDataFilterOptions](https://reference.aspose.com/cells/cpp/aspose.cells/loaddatafilteroptions/) elde edileninden uygun değeri sağlayın ve [LoadFilter](https://reference.aspose.com/cells/cpp/aspose.cells/loadfilter/) ile çalışırken veya oluştururken kullanın.

[LoadDataFilterOptions](https://reference.aspose.com/cells/cpp/aspose.cells/loaddatafilteroptions/) dizisi aşağıdaki olası değerlere sahiptir.

- Tümü
- KitapAyarları
- HücreBoş
- HücreBool
- CellData
- CellError
- CellNumeric
- CellString
- CellValue
- Chart
- ConditionalFormatting
- DataValidation
- DefinedNames
- DocumentProperties
- Formula
- Hyperlinkler
- MergedArea
- PivotTable
- Settings
- Shape
- SheetData
- SheetSettings
- Structure
- Style
- Table
- VBA
- XmlMap

## **Çalışma Kitabını Yüklerken Filtreleme Nesneleri**
Aşağıdaki örnek kodlar, çalışma kitabından grafikleri filtrelemenin nasıl yapıldığını göstermektedir. Lütfen bu kodda kullanılan [örnek excel dosyasını](5115258.xlsx) ve bunun tarafından oluşturulan [çıktı PDF'yi](5115257.pdf) kontrol edin. Çıktı PDF'de, tüm grafiklerin çalışma kitabından filtrelenmiş olduğunu görebilirsiniz.

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

    // Filter charts from the workbook
    LoadOptions lOptions;
    lOptions.SetLoadFilter(new LoadFilter(LoadDataFilterOptions::All & ~LoadDataFilterOptions::Chart));

    // Load the workbook with the above filter
    U16String inputFilePath = srcDir + u"sampleFilterCharts.xlsx";
    Workbook workbook(inputFilePath, lOptions);

    // Save worksheet to a single PDF page
    PdfSaveOptions pOptions;
    pOptions.SetOnePagePerSheet(true);

    // Save the workbook in PDF format
    U16String outputFilePath = outDir + u"sampleFilterCharts.pdf";
    workbook.Save(outputFilePath, pOptions);

    std::cout << "Workbook saved successfully with filtered charts!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Çalışma Sayfasını Yüklerken Filtreleme Nesneleri**
Aşağıdaki örnek kod, [kaynak excel dosyasını](5115255.xlsx) yükler ve çalışma sayfalarından aşağıdaki verileri özel bir filtreden geçirir.

- Tablo adı NoCharts olan çalışma sayfasından Grafikleri filtreler.
- Tablo adı NoShapes olan çalışma sayfasından Şekilleri filtreler.
- Tablo adı NoConditionalFormatting olan çalışma sayfasından Koşullu Biçimlendirmeyi filtreler.

Özel bir filtreden sonra [kaynak excel dosyasını](5115255.xlsx) yüklediğinde, tüm çalışma sayfalarının resimlerini sırayla alır. Referansınız için çıktı resimleri aşağıdadır. Görebileceğiniz gibi, ilk resimde grafik yok, ikinci resimde şekiller yok ve üçüncü resimde koşullu biçimlendirme yok.

- [NoCharts.png](5115254.png)
- [NoShapes.png](5115256.png)
- [NoConditionalFormatting.png](5115251.png)

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

class CustomLoadFilter : public LoadFilter
{
public:
    void StartSheet(Worksheet& sheet) override
    {
        U16String sheetName = sheet.GetName();

        if (sheetName == u"NoCharts")
        {
            // Load everything and filter charts
            SetLoadDataFilterOptions(static_cast<LoadDataFilterOptions>(static_cast<int>(LoadDataFilterOptions::All) & ~static_cast<int>(LoadDataFilterOptions::Chart)));
        }

        if (sheetName == u"NoShapes")
        {
            // Load everything and filter shapes
            SetLoadDataFilterOptions(static_cast<LoadDataFilterOptions>(static_cast<int>(LoadDataFilterOptions::All) & ~static_cast<int>(LoadDataFilterOptions::Drawing)));
        }

        if (sheetName == u"NoConditionalFormatting")
        {
            // Load everything and filter conditional formatting
            SetLoadDataFilterOptions(static_cast<LoadDataFilterOptions>(static_cast<int>(LoadDataFilterOptions::All) & ~static_cast<int>(LoadDataFilterOptions::ConditionalFormatting)));
        }
    }
};

// Add main function to serve as entry point
int main() {
    Aspose::Cells::Startup();
    Aspose::Cells::Cleanup();
    return 0;

}
```

Bu, özel filtrenin çalışma sayfası adlarına göre nasıl kullanılacağının örneğidir.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

class CustomLoadFilter : public LoadFilter
{
public:
    CustomLoadFilter() : LoadFilter(LoadDataFilterOptions::All) {}
};

int main()
{
    Aspose::Cells::Startup();

    // Source directory
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Filter worksheets using CustomLoadFilter class
    LoadOptions loadOpts;
    CustomLoadFilter customLoadFilter;
    loadOpts.SetLoadFilter(&customLoadFilter);

    // Load the workbook with filter defined in CustomLoadFilter class
    Workbook workbook(srcDir + u"sampleCustomFilteringPerWorksheet.xlsx", loadOpts);

    // Take the image of all worksheets one by one
    WorksheetCollection sheets = workbook.GetWorksheets();
    for (int i = 0; i < sheets.GetCount(); i++)
    {
        // Access worksheet at index i
        Worksheet worksheet = sheets.Get(i);

        // Create an instance of ImageOrPrintOptions
        // Render entire worksheet to image
        ImageOrPrintOptions imageOpts;
        imageOpts.SetOnePagePerSheet(true);
        imageOpts.SetImageType(Aspose::Cells::Drawing::ImageType::Png);

        // Convert worksheet to image
        SheetRender render(worksheet, imageOpts);
        render.ToImage(0, outDir + u"outputCustomFilteringPerWorksheet_" + worksheet.GetName() + u".png");
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
