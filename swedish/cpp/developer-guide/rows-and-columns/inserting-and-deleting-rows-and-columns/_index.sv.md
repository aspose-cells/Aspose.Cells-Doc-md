---
title: Infoga och ta bort rader och kolumner i Excel fil med C++
linktitle: Infoga och ta bort rader och kolumner
type: docs
weight: 70
url: /sv/cpp/inserting-and-deleting-rows-and-columns/
description: Denna artikel visar hur man infogar och tar bort rader och kolumner med API et Aspose.Cells for C++.
keywords: Aspose.Cells C++ hanterar rader och kolumner, infogar rader och kolumner, tar bort rader och kolumner.
---

## **Introduktion**

Oavsett om du skapar en ny arbetsbok från grunden eller arbetar med en befintlig arbetsbok kan vi behöva lägga till extra rader eller kolumner för att rymma mer data. Å andra sidan kan det också hända att vi behöver ta bort rader eller kolumner från angivna positioner i arbetsboken.
För att uppfylla dessa krav erbjuder Aspose.Cells en mycket enkel uppsättning klasser och metoder, som diskuteras nedan.

### **Hantera rader och kolumner**

Aspose.Cells tillhandahåller en klass [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), som representerar en Microsoft Excel-fil. Klassen [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) innehåller en [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)-samling som ger åtkomst till varje kalkylblad i en Excel-fil. Ett kalkylblad representeras av klassen [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). Klassen [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) tillhandahåller en [**GetCells()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getcells/)-samling som representerar alla celler i kalkylbladet.

Samlingen [**GetCells()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getcells/) ger flera metoder för att hantera rader och kolumner i ett kalkylblad. Några av dessa diskuteras nedan.

{{% alert color="primary" %}}

När rader eller kolumner läggs till skiftas innehållet i arbetsbladet nedåt eller åt höger, och om rader eller kolumner tas bort skiftas innehållet uppåt eller åt vänster.

{{% /alert %}}

## **Infoga rader och kolumner**

### **Hur man infogar en rad**

Infoga en rad i kalkylbladet på valfri plats genom att anropa [**InsertRow**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrow/)-metoden i [**GetCells()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getcells/)-samlingen. Metoden [**InsertRow**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrow/) tar indexet för raden där den nya raden ska infogas.

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"book1.xls";

    // Instantiating a Workbook object
    Workbook workbook(inputFilePath);

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Inserting a row into the worksheet at 3rd position
    worksheet.GetCells().InsertRow(2);

    // Path of output excel file
    U16String outputFilePath = outDir + u"output.out.xls";

    // Saving the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Row inserted successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Hur man infogar flera rader**

För att infoga flera rader i ett kalkylblad, anropa [**InsertRows**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrows/)-metoden i [**GetCells()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getcells/)-samlingen. Metoden [**InsertRows**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrows/) tar två parametrar:

- Radindex, index för raden från vilken de nya raderna ska infogas.
- Antal rader, det totala antalet rader som ska infogas.

```c++
#include <iostream>
#include <fstream>
#include <memory>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"book1.xls";

    // Create workbook from file
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Insert 10 rows into the worksheet starting from 3rd row
    worksheet.GetCells().InsertRows(2, 10);

    // Path of output excel file
    U16String outputFilePath = srcDir + u"output.out.xls";

    // Save the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Rows inserted successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **Hur man infogar en rad med formatering**

För att infoga en rad med formateringsalternativ, använd överbelastningen [**InsertRows**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrows/) som tar [**InsertOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/insertoptions/) som parameter. Sätt egenskapen [**CopyFormatType**](https://reference.aspose.com/cells/cpp/aspose.cells/insertoptions/getcopyformattype/) för [**InsertOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/insertoptions/)-klassen med [**CopyFormatType**](https://reference.aspose.com/cells/cpp/aspose.cells/insertoptions/getcopyformattype/)-enum. [**CopyFormatType**](https://reference.aspose.com/cells/cpp/aspose.cells/insertoptions/getcopyformattype/) enum har tre medlemmar listade nedan.

- SameAsAbove: Formaterar raden samma som ovanstående rad.
- SameAsBelow: Formaterar raden samma som nedanstående rad.
- Rensa: Rensar formateringen.

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

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"book1.xls";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"InsertingARowWithFormatting_out.xls";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Setting Formatting options
    InsertOptions insertOptions;
    insertOptions.SetCopyFormatType(CopyFormatType::SameAsAbove);

    // Inserting a row into the worksheet at 3rd position
    worksheet.GetCells().InsertRows(2, 1, insertOptions);

    // Save the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Row inserted successfully with formatting!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Hur man infogar en kolumn**

Utvecklare kan också infoga en kolumn i kalkylbladet på valfri plats genom att anropa [**InsertColumn**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertcolumn/)-metoden i [**GetCells()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getcells/)-samlingen. Metoden [**InsertColumn**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertcolumn/) tar indexet för kolumnen där den nya kolumnen ska infogas.

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
    U16String inputFilePath = srcDir + u"book1.xls";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"output.out.xls";

    // Create workbook from the input file
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Insert a column into the worksheet at 2nd position
    worksheet.GetCells().InsertColumn(1);

    // Save the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Column inserted successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Ta bort rader och kolumner**

### **Hur man tar bort flera rader**

För att ta bort flera rader från ett kalkylblad, anropa [**DeleteRows**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deleterows/)-metoden i [**GetCells()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getcells/)-samlingen. Metoden [**DeleteRows**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deleterows/) tar två parametrar:

- Radindex, index för raden från vilken raderna ska tas bort.
- Antal rader, det totala antalet rader som ska tas bort.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Create workbook from the input file
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Delete 10 rows from the worksheet starting from 3rd row
    worksheet.GetCells().DeleteRows(2, 10);

    // Save the modified Excel file
    U16String outputFilePath = srcDir + u"output.xlsx";
    workbook.Save(outputFilePath);

    std::cout << "Rows deleted successfully and file saved!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Hur man tar bort en kolumn**

För att ta bort en kolumn från kalkylbladet på valfri plats, anropa [**DeleteColumn**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deletecolumn/)-metoden i [**GetCells()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getcells/)-samlingen. Metoden [**DeleteColumn**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deletecolumn/) tar indexet för kolumnen som ska tas bort.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Create workbook from file
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Delete a column from the worksheet at 5th position (index 4)
    worksheet.GetCells().DeleteColumn(4);

    // Save the modified Excel file
    U16String outputFilePath = srcDir + u"output.xlsx";
    workbook.Save(outputFilePath);

    std::cout << "Column deleted successfully and file saved!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
