---
title: Boş Satır ve Sütunları Silme C++ ile bir Çalışma Sayfasında
linktitle: Çalışma Sayfasındaki Boş Satır ve Sütunları Silme
type: docs
weight: 300
url: /tr/cpp/delete-blank-rows-and-columns-in-a-worksheet/
description: Aspose.Cells kullanarak C++ ile çalışma sayfasındaki boş satır ve sütunları sil.
---

{{% alert color="primary" %}}

Bir sayfadan boş satır ve sütunların tamamını silebilmek mümkündür. Bu, örneğin, Microsoft Excel dosyasından PDF dosyası oluştururken, yalnızca veri içerip içermeyen satır ve sütunları dönüştürmek istendiğinde faydalıdır.

Boş satır ve sütunları silmek için aşağıdaki Aspose.Cells yöntemlerini kullanın:

1. Boş satırları silmek için [**Cells.DeleteBlankRows()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deleteblankrows/) yöntemini kullanın. Silinecek boş satırlar için, [**Row.IsBlank**](https://reference.aspose.com/cells/cpp/aspose.cells/row/isblank/) sadece doğru olmalıdır, ayrıca bu satırlarda herhangi bir hücre için görünür bir yorum tanımlanmamış olmalı ve bunlarla kesişen bir pivota tablonun olmaması gerekir.
2. Boş sütunları silmek için [**Cells.DeleteBlankColumns()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deleteblankcolumns/) yöntemini kullanın.

{{% /alert %}}

## Boş Satırları Silmek İçin C++ Kodu

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Open an existing Excel file
    U16String inputFilePath = srcDir + u"SampleInput.xlsx";
    Workbook workbook(inputFilePath);

    // Create a Worksheets object with reference to the sheets of the Workbook
    WorksheetCollection sheets = workbook.GetWorksheets();

    // Get the first Worksheet from WorksheetCollection
    Worksheet sheet = sheets.Get(0);

    // Delete the Blank Rows from the worksheet
    sheet.GetCells().DeleteBlankRows();

    // Save the Excel file
    U16String outputFilePath = outDir + u"mybook.out.xlsx";
    workbook.Save(outputFilePath);

    std::cout << "Blank rows deleted and workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## Boş Sütunları Silmek İçin C++ Kodu

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"SampleInput.xlsx";

    // Create a smart pointer to a new Workbook instance
    std::unique_ptr<Workbook> wb = std::make_unique<Workbook>(inputFilePath);

    // Create a Worksheets object with reference to the sheets of the Workbook
    WorksheetCollection sheets = wb->GetWorksheets();

    // Get the first Worksheet from WorksheetCollection
    Worksheet sheet = sheets.Get(0);

    // Delete the blank columns from the worksheet
    sheet.GetCells().DeleteBlankColumns();

    // Save the excel file
    U16String outputFilePath = srcDir + u"mybook.out.xlsx";
    wb->Save(outputFilePath);

    std::cout << "Blank columns deleted successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
