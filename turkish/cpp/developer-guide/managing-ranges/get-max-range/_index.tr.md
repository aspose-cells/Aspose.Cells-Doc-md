---
title: C++ kullanarak Çalışma Sayfasında Maks Aralık Nasıl Alınır
linktitle: Çalışma sayfasındaki Maksimum Aralığı Al
type: docs
weight: 360
url: /tr/cpp/get-max-range-in-a-worksheet/
description: Bu makale, Aspose.Cells for C++ kütüphanesi ile Excel dosyalarının maksimum aralığını, maksimum veri aralığını ve maksimum görüntüleme aralığını nasıl alacağınızı anlatmaktadır.
---

{{% alert color="primary" %}} 

Çalışma sayfasından veri okurken, maksimum alanı bilmemiz gerekmektedir.

Tüm verileri bir çalışma sayfasından kopyalarken, maksimum alanı bilmemiz gerekmektedir.

Belirli bir alanın HTML ve PDF'ye dışa aktarılırken, maksimum alanı bilmemiz gerekir.

Aspose.Cells for C++, bir çalışma sayfasında maksimum aralığı bulmak için farklı yollar içerir. 

{{% /alert %}} 

## **Maksimum aralığı almak**
Aspose.Cells'te, [**Row**](https://reference.aspose.com/cells/cpp/aspose.cells/row/) ve [**Column**](https://reference.aspose.com/cells/cpp/aspose.cells/column/) nesneleri başlatılmışsa, bunlar boş satır veya sütunlar olmasa bile maksimum alan olarak sayılır.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a workbook object and open the Excel file
    Workbook workbook(u"Book1.xlsx");

    // Get all the worksheets in the workbook
    WorksheetCollection worksheets = workbook.GetWorksheets();
    Worksheet sheet = worksheets.Get(0);

    // Get the max data range
    int maxRow = sheet.GetCells().GetMaxRow();
    int maxColumn = sheet.GetCells().GetMaxColumn();

    // Create a range from A1 to the max data range
    Range range = sheet.GetCells().CreateRange(0, 0, maxRow + 1, maxColumn + 1);

    // Set a null value in cell A10
    sheet.GetCells().Get(u"A10").PutValue(nullptr);

    // Update the max data range after modifying the sheet
    maxRow = sheet.GetCells().GetMaxRow();
    maxColumn = sheet.GetCells().GetMaxColumn();

    // Update the range to include the new data
    range = sheet.GetCells().CreateRange(0, 0, maxRow + 1, maxColumn + 1);

    Aspose::Cells::Cleanup();
}
```

## **Maksimum veri aralığını almak**
Çoğu durumda, yalnızca tüm verileri içeren tüm aralıkları elde etmemiz yeterlidir, aralık dışındaki boş hücreler biçimlendirilse bile.
Ve şekiller, tablolar ve pivot tablolar ile ilgili ayarlar göz ardı edilecektir.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiate a new Workbook
    Workbook workbook(u"Book1.xlsx");

    // Get all the worksheets in the book
    WorksheetCollection worksheets = workbook.GetWorksheets();
    Worksheet sheet = worksheets.Get(0);

    // Gets the max data range
    int maxRow = sheet.GetCells().GetMaxDataRow();
    int maxColumn = sheet.GetCells().GetMaxDataColumn();

    // The range is A1:B3
    Range range = sheet.GetCells().CreateRange(0, 0, maxRow + 1, maxColumn + 1);

    // Put null value in cell A10
    sheet.GetCells().Get(u"A10").PutValue(nullptr);

    // Update max data range after modification
    maxRow = sheet.GetCells().GetMaxDataRow();
    maxColumn = sheet.GetCells().GetMaxDataColumn();

    // The range is still A1:B3
    range = sheet.GetCells().CreateRange(0, 0, maxRow + 1, maxColumn + 1);

    Aspose::Cells::Cleanup();
}
```

## **Maksimum görüntü aralığını almak**
Çalışma sayfasındaki tüm verileri HTML, PDF veya görüntülere dışa aktardığımızda, veri, stiller, grafikler, tablolar ve özet tablolar da dahil olmak üzere tüm görünür nesneleri içeren bir alan elde etmemiz gerekmektedir.
Aşağıdaki kodlar, maksimum görüntüleme alanını HTML'ye nasıl aktaracağını gösterir:

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

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Path of output HTML file
    U16String outputFilePath = outDir + u"html.html";

    // Instantiate a new Workbook
    Workbook workbook(inputFilePath);

    // Get all the worksheets in the book
    WorksheetCollection worksheets = workbook.GetWorksheets();

    // Get the max display range of the first worksheet
    Range range = worksheets.Get(0).GetCells().GetMaxDisplayRange();

    // Create HtmlSaveOptions to configure the export
    HtmlSaveOptions saveOptions;
    saveOptions.SetExportActiveWorksheetOnly(true);

    // Set the export area to the range of the first worksheet
    CellArea exportArea = CellArea::CreateCellArea(range.GetFirstRow(), range.GetFirstColumn(), 
                                                   range.GetFirstRow() + range.GetRowCount() - 1, 
                                                   range.GetFirstColumn() + range.GetColumnCount() - 1);
    saveOptions.SetExportArea(exportArea);

    // Save the range to HTML
    workbook.Save(outputFilePath, saveOptions);

    std::cout << "Range saved to HTML successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

İşte [kaynak excel dosyası](Book1.xlsx).
{{< app/cells/assistant language="cpp" >}}
