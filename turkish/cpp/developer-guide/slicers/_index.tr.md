---
title: C++ ile Dilimleyici Ekle
linktitle: Dilimleyiciler
type: docs
weight: 170
url: /tr/cpp/create-slicer/
description: Aspose.Cells kullanarak C++ ile Excel dosyalarının dilimleyicilerini yönetin.
---

## **Olası Kullanım Senaryoları**

Dilimleyici, verileri hızlıca filtrelemek için kullanılır. Hem tablo hem de özet tablo içindekileri filtrelemek için kullanılabilir. Microsoft Excel, bir tablo veya özet tablo seçip *Ekle > Dilimleyici* seçeneğiyle dilimleyici oluşturmanıza izin verir. Aspose.Cells, [**Worksheet.Slicers.Add()**](https://reference.aspose.com/cells/cpp/aspose.cells.slicers/slicercollection/add/) yöntemiyle dilimleyici oluşturmanızı sağlar.

## **Pivot Tablosuna Dilimleyici Oluştur**

Lütfen aşağıdaki örnek kodu inceleyin. Özette bir özet tabloyu içeren [örnek Excel dosyasını](67338470.xlsx) yükler. Ardından ilk temel özet alanına dayalı dilimleyici oluşturur. Son olarak, çalışma kitabını [çıktı XLSX](67338471.xlsx) ve [çıktı XLSB](67338472.xlsb) biçimlerinde kaydeder. Aşağıdaki ekran görüntüsü, Aspose.Cells tarafından çıktı Excel dosyasında oluşturulan dilimleyiciyi göstermektedir.

![todo:image_alt_text](create-slicer-to-a-pivot-table_1.png)

### **Örnek Kod**

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
using namespace Aspose::Cells::Slicers;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"sampleCreateSlicerToPivotTable.xlsx";

    // Path of output Excel files
    U16String outputFilePathXlsx = outDir + u"outputCreateSlicerToPivotTable.xlsx";
    U16String outputFilePathXlsb = outDir + u"outputCreateSlicerToPivotTable.xlsb";

    // Load sample Excel file containing pivot table
    Workbook wb(inputFilePath);

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access first pivot table inside the worksheet
    PivotTable pt = ws.GetPivotTables().Get(0);

    // Add slicer relating to pivot table with first base field at cell B22
    int idx = ws.GetSlicers().Add(pt, u"B22", pt.GetBaseFields().Get(0));

    // Access the newly added slicer from slicer collection
    Slicer slicer = ws.GetSlicers().Get(idx);

    // Save the workbook in output XLSX format
    wb.Save(outputFilePathXlsx, SaveFormat::Xlsx);

    // Save the workbook in output XLSB format
    wb.Save(outputFilePathXlsb, SaveFormat::Xlsb);

    std::cout << "Slicer created and workbooks saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Excel Tablosuna Dilimleyici Oluştur**

Lütfen aşağıdaki örnek kodu görün. Bir tabloyu içeren [örnek Excel dosyasını](sampleCreateSlicerToExcelTable.xlsx) yükler. Ardından ilk sütuna dayalı dilimleyici oluşturur ve son olarak çalışma kitabını [çıktı XLSX](outputCreateSlicerToExcelTable.xlsx) formatında kaydeder.

### **Örnek Kod**

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

    // Load sample Excel file containing a table
    Workbook workbook(srcDir + u"sampleCreateSlicerToExcelTable.xlsx");

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access first table inside the worksheet
    ListObject table = worksheet.GetListObjects().Get(0);

    // Add slicer
    int idx = worksheet.GetSlicers().Add(table, 0, u"H5");

    // Save the workbook in output XLSX format
    workbook.Save(outDir + u"outputCreateSlicerToExcelTable.xlsx", SaveFormat::Xlsx);

    std::cout << "Slicer added successfully to the Excel table!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Gelişmiş Konular**
- [Slice Özelliklerini Değiştir](/cells/tr/cpp/change-slicer-properties/)
- [Excel dosyasına bir dilimleyici uygulanmışsa ve bu dilimleyicinin ayarlarını içeren bir Excel dosyasını PDF olarak dışa aktarmak istiyorsanız, Aspose.Cells bunu artık varsayılan olarak destekler. Sadece Excel dosyasını dilimleyici ile birlikte PDF olarak dışa aktarırsınız, oluşturulan PDF uygulanan dilimleyiciyi gösterecektir.](/cells/tr/cpp/draw-slicer-while-rendering-excel-to-pdf/)
- [Dilimleyici Biçimlendirme](/cells/tr/cpp/formatting-slicer/)
- [Süzgeci Kaldırma](/cells/tr/cpp/removing-slicer/)
- [Dilimleyiciyi Oluşturma](/cells/tr/cpp/rendering-slicer/)
- [Dilimleyici Güncelleme](/cells/tr/cpp/updating-slicer/)
