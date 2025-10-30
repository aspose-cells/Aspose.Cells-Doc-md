--- 
title: C++ ile Excel de Renk Aralıklarını Kopyala 
linktitle: Kopya Aralıkları 
type: docs 
weight: 105 
url: /tr/cpp/copy-ranges-of-excel/ 
description: Aspose.Cells kullanarak C++ ile Excel de aralıkları nasıl kopyalayacağınızı öğrenin. 
--- 

## **Giriş**

Excel'de bir aralığı seçebilir, ardından bu aralığı belirli seçeneklerle aynı çalışma sayfasına, diğer çalışma sayfalarına veya diğer dosyalara yapıştırabilirsiniz.

## **Aspose.Cells Kullanarak Aralıkları Kopyalama**

Aspose.Cells, aralığı kopyalamak için bazı overload [Range.Copy](https://reference.aspose.com/cells/cpp/aspose.cells/range/copy/) metodları sağlar. Ve [Range.CopyStyle](https://reference.aspose.com/cells/cpp/aspose.cells/range/copystyle/) sadece aralığın stilini kopyalar; [Range.CopyData](https://reference.aspose.com/cells/cpp/aspose.cells/range/copydata/) ise sadece aralık değerlerini kopyalar.

## **Aralık Kopyalama**

İki aralık oluşturarak: kaynak aralık, hedef aralık, ardından Range.Copy yöntemi ile kaynak aralığı hedef aralığa kopyalama.

Aşağıdaki kodu görün:

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiate a new Workbook.
    Workbook workbook;

    // Get all the worksheets in the book.
    WorksheetCollection worksheets = workbook.GetWorksheets();

    // Get the first worksheet in the worksheets collection.
    Worksheet worksheet = worksheets.Get(0);

    // Create a range of cells.
    Range sourceRange = worksheet.GetCells().CreateRange(u"A1", u"A2");

    // Input some data with some formattings into
    // A few cells in the range.
    sourceRange.Get(0, 0).PutValue(u"Test");
    sourceRange.Get(1, 0).PutValue(u"123");

    // Create target range of cells.
    Range targetRange = worksheet.GetCells().CreateRange(u"B1", u"B2");

    // Copy source range to target range in the same worksheet 
    targetRange.Copy(sourceRange);

    // Create a new worksheet.
    worksheets.Add();
    worksheet = worksheets.Get(1);

    targetRange = worksheet.GetCells().CreateRange(u"A1", u"A2");
    // Copy source range to target range in another worksheet 
    targetRange.Copy(sourceRange);

    // Copy to another workbook
    Workbook anotherWorkbook;

    worksheet = workbook.GetWorksheets().Get(0);

    targetRange = worksheet.GetCells().CreateRange(u"A1", u"A2");
    // Copy source range to target range in another workbook 
    targetRange.Copy(sourceRange);

    std::cout << "Copy operations completed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Seçeneklerle Aralık Yapıştırma**

Aspose.Cells, belirli bir türle aralığı yapıştırmayı destekler.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiate a new Workbook.
    Workbook workbook;

    // Get all the worksheets in the book.
    WorksheetCollection worksheets = workbook.GetWorksheets();

    // Get the first worksheet in the worksheets collection.
    Worksheet worksheet = worksheets.Get(0);

    // Create a range of cells.
    Range sourceRange = worksheet.GetCells().CreateRange(u"A1", u"A2");

    // Input some data with some formattings into A few cells in the range.
    sourceRange.Get(0, 0).PutValue(u"Test");
    sourceRange.Get(1, 0).PutValue(u"123");

    // Create target range of cells.
    Range targetRange = worksheet.GetCells().CreateRange(u"B1", u"B2");

    // Init paste options.
    PasteOptions options;
    // Set paste type.
    options.SetPasteType(PasteType::ValuesAndFormats);
    options.SetSkipBlanks(true);

    // Copy source range to target range
    targetRange.Copy(sourceRange, options);

    std::cout << "Data copied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Yalnızca Aralık Verilerini Kopyalama**
Ayrıca aşağıdaki kodları kullanarak verileri Range.CopyData yöntemiyle kopyalayabilirsiniz:

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiate a new Workbook.
    Workbook workbook;

    // Get all the worksheets in the book.
    WorksheetCollection worksheets = workbook.GetWorksheets();

    // Get the first worksheet in the worksheets collection.
    Worksheet worksheet = worksheets.Get(0);

    // Create a range of cells.
    Range sourceRange = worksheet.GetCells().CreateRange(u"A1", u"A2");

    // Input some data with some formatting into
    // A few cells in the range.
    sourceRange.Get(0, 0).SetValue(u"Test");
    sourceRange.Get(1, 0).SetValue(123);

    // Create target range of cells.
    Range targetRange = worksheet.GetCells().CreateRange(u"B1", u"B2");

    // Copy the data of source range to target range
    targetRange.CopyData(sourceRange);

    std::cout << "Data copied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Gelişmiş Konular**
- [Kaynak Aralığın Satır Yüksekliklerini Hedef Aralığa Kopyalama](/cells/tr/cpp/copy-row-heights-of-source-range-to-destination-range/)
{{< app/cells/assistant language="cpp" >}}
