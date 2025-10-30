---
title: C++ kullanarak Excel dosyası yüklerken Pivot Önbellek Kayıtlarını Ayrıştırma
linktitle: Pivot Önbellek Kayıtlarını Ayrıştırma
type: docs
weight: 70
url: /tr/cpp/parsing-pivot-cached-records-while-loading-excel-file/
description: Aspose.Cells for C++ kullanarak Excel dosyası yüklerken pivot önbellek kayıtlarını nasıl ayrıştıracağınızı öğrenin.
---

## **Olası Kullanım Senaryoları**

Bir Pivot Tablosu oluşturduğunuzda, Microsoft Excel kaynak verinin bir kopyasını alır ve Pivot Önbelleğine saklar. Pivot Önbelleği, Microsoft Excel'in belleğinin içinde bulunur. Onu göremezsiniz, ancak bu, Pivot Tablonuzu oluştururken veya bir Dilim Seçimi değiştirdiğinizde veya satırlar/sütunlar etrafında hareket ettiğinizde Pivot Tablosunun başvurduğu veridir. Bu, Microsoft Excel'in Pivot Tablosundaki değişikliklere çok duyarlı olmasını sağlar, ancak dosya boyutunun potansiyel olarak iki kat artmasına neden olabilir.

Excel dosyanızı Workbook nesnesi içine yüklerken, Pivot Önbellek kayıtlarını da yüklemek isteyip istemediğinize karar verebilirsiniz. Bunun için [**LoadOptions.GetParsingPivotCachedRecords()**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/getparsingpivotcachedrecords/) özelliğini kullanabilirsiniz. Bu özelliğin varsayılan değeri **false**'dur. Pivot Önbellek oldukça büyükse, performansı artırabilir. Ancak eğer Pivot Önbellek kayıtlarını da yüklemek istiyorsanız, bu özelliği **true** olarak ayarlamalısınız.

## **Excel dosyasını yüklerken Pivot Önbellek Kayıtlarını Ayrıştırın**

Aşağıdaki örnek kod, [**LoadOptions.GetParsingPivotCachedRecords()**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/getparsingpivotcachedrecords/) özelliğinin kullanımını açıklar. Pivot önbellek kayıtları ayrıştırılırken [örnek Excel dosyasını](61767773.xlsx) yükler. Ardından pivot tablosunu yeniler ve [çıktı Excel dosyası olarak](61767774.xlsx) kaydeder.

## **Örnek Kod**

```cpp
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

    // Create load options
    LoadOptions options;

    // Set ParsingPivotCachedRecords true, default value is false
    options.SetParsingPivotCachedRecords(true);

    // Load the sample Excel file containing pivot table cached records
    U16String inputFilePath = srcDir + u"sampleParsingPivotCachedRecordsWhileLoadingExcelFile.xlsx";
    Workbook wb(inputFilePath, options);

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access first pivot table
    PivotTable pt = ws.GetPivotTables().Get(0);

    // Set refresh data flag true
    pt.SetRefreshDataFlag(true);

    // Refresh and calculate pivot table
    pt.RefreshData();
    pt.CalculateData();

    // Set refresh data flag false
    pt.SetRefreshDataFlag(false);

    // Save the output Excel file
    U16String outputFilePath = outDir + u"outputParsingPivotCachedRecordsWhileLoadingExcelFile.xlsx";
    wb.Save(outputFilePath);

    std::cout << "Pivot table cached records parsed and refreshed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
