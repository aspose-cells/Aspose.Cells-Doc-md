---
title: Skapa, få tillgång till och kopiera namngivna områden med C++
linktitle: Skapa, få tillgång till och kopiera namngivna områden
type: docs
weight: 200
url: /sv/cpp/create-access-and-copy-named-ranges/
description: Lär dig hur du skapar, får tillgång till och kopierar namngivna områden i Excel filer med Aspose.Cells och C++.
---

## **Introduktion**

Vanligtvis används kolumn- och radetiketter för att referera till enskilda celler. Det är möjligt att skapa beskrivande namn för att representera celler, cellområden, formler eller konstanta värden. Ordet **namn** kan referera till en sträng av tecken som representerar en cell, cellområde, formel eller konstant värde. Att tilldela ett namn till ett område innebär att det området kan refereras till med det namnet. Använd lättförståeliga namn, som Produkter, för att referera till svårförståeliga områden, som Sales!C20:C30. Etiketter kan användas i formler som hänvisar till data på samma blad; om du vill representera ett område på ett annat blad, kan du använda ett namn. *Namngivna områden är bland de mest kraftfulla funktionerna i Microsoft Excel, speciellt när de används som datakälla för listkontroller, pivot-tabeller, diagram och liknande.

## **Arbeta med namngivet intervall med Microsoft Excel**

### **Skapa namngivna intervall**

Följande steg beskriver hur du namnger en cell eller ett cellområde med **MS Excel**. Denna metod gäller för **Microsoft Office Excel 2003**, **Microsoft Excel 97**, **2000** och **2002**.

1. Välj den cell eller det cellområde som du vill namnge.
1. Klicka på **Namnboxen** i vänstra änden av formelfältet.
1. Skriv namnet för cellerna.
1. Tryck på ENTER.

{{% alert color="primary" %}}

Du kan inte namnge en cell medan du ändrar innehållet i cellen.

{{% /alert %}}

## **Arbeta med namngivna områden med hjälp av Aspose.Cells**

Här använder vi Aspose.Cells API för att utföra uppgiften.
Aspose.Cells tillhandahåller en klass, [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), som representerar en Microsoft Excel-fil. Klassen [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) innehåller en [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)-samling som möjliggör åtkomst till varje arbetsblad i en Excel-fil. Ett arbetsblad representeras av klassen [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). Klassen [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) tillhandahåller en [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)-samling.

### **Skapa namngivet område**

Det är möjligt att skapa ett namngivet område genom att anropa den överlagrade [**CreateRange**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/createrange/)-metoden i [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)-samlingen. En typisk version av [**CreateRange**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/createrange/)-metoden tar följande parametrar:

- Namn på övre vänstra cell, namnet på den översta vänstra cellen i området.
- Namnet på den nedre högra cellen, namnet på den längst ner till höger i området.

När metoden [**CreateRange**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/createrange/) kallas returneras det nysskapade området som en instans av klassen [**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/). Använd detta [**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/)-objekt för att konfigurera det namngivna området. Till exempel, ställ in namnet på området med hjälp av egenskapen [**GetName()**](https://reference.aspose.com/cells/cpp/aspose.cells/range/getname/). Följande exempel visar hur man skapar ett namngivet område av celler som sträcker sig över B4:G14.

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

    // Create workbook
    Workbook workbook(inputFilePath);

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Creating a named range
    Range range = worksheet.GetCells().CreateRange(u"B4", u"G14");

    // Setting the name of the named range
    range.SetName(u"TestRange");

    // Saving the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Named range created and file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Ange data i cellerna i det namngivna området**

Du kan sätta in data i de individuella cellerna i ett område enligt mönstret:

- **C++**: Område(rad, kolumn)

Antag att du har ett namngivet område av celler som sträcker sig från A1 till C4. Matrisen omfattar 4 * 3 = 12 celler. De enskilda cellerna i området är ordnade sekventiellt: Range(0, 0), Range(0, 1), Range(0, 2), Range(1, 0), Range(1, 1), Range(1, 2), Range(2, 0), Range(2, 1), Range(2, 2), Range(3, 0), Range(3, 1), Range(3, 2).

Använd följande egenskaper för att identifiera cellerna i området:

- FirstRow returnerar indexet för den första raden i det namngivna området.
- FirstColumn returnerar indexet för den första kolumnen i det namngivna området.
- RowCount returnerar det totala antalet rader i det namngivna området.
- ColumnCount returnerar det totala antalet kolumner i det namngivna området.

Följande exempel visar hur man anger några värden i cellerna i ett specificerat område.

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

    // Instantiate a new Workbook
    Workbook workbook;

    // Get the first worksheet in the workbook
    Worksheet worksheet1 = workbook.GetWorksheets().Get(0);

    // Create a range of cells based on H1:J4
    Range range = worksheet1.GetCells().CreateRange(u"H1", u"J4");

    // Name the range
    range.SetName(u"MyRange");

    // Input some data into cells in the range
    range.Get(0, 0).PutValue(u"USA");
    range.Get(0, 1).PutValue(u"SA");
    range.Get(0, 2).PutValue(u"Israel");
    range.Get(1, 0).PutValue(u"UK");
    range.Get(1, 1).PutValue(u"AUS");
    range.Get(1, 2).PutValue(u"Canada");
    range.Get(2, 0).PutValue(u"France");
    range.Get(2, 1).PutValue(u"India");
    range.Get(2, 2).PutValue(u"Egypt");
    range.Get(3, 0).PutValue(u"China");
    range.Get(3, 1).PutValue(u"Philipine");
    range.Get(3, 2).PutValue(u"Brazil");

    // Save the excel file
    workbook.Save(outDir + u"rangecells.out.xls");

    std::cout << "Range cells created and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Identifiera celler i det namngivna området**

Du kan sätta in data i de individuella cellerna i ett område enligt mönstret:

- **C++**: Område(rad, kolumn)

Om du har ett namngivet område som sträcker sig över A1:C4. Matrisen består av 4 * 3 = 12 celler. De enskilda områdecellerna är ordnade i följd: Range(0, 0), Range(0, 1), Range(0, 2), Range(1, 0), Range(1, 1), Range(1, 2), Range(2, 0), Range(2, 1), Range(2, 2), Range(3, 0), Range(3, 1), Range(3, 2).

Använd följande egenskaper för att identifiera cellerna i området:

- FirstRow returnerar indexet för den första raden i det namngivna området.
- FirstColumn returnerar indexet för den första kolumnen i det namngivna området.
- RowCount returnerar det totala antalet rader i det namngivna området.
- ColumnCount returnerar det totala antalet kolumner i det namngivna området.

Följande exempel visar hur man anger några värden i cellerna i ett specificerat område.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"book1.xls";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Get the specified named range
    Range range = workbook.GetWorksheets().GetRangeByName(u"TestRange");

    // Identify range cells
    std::cout << "First Row : " << range.GetFirstRow() << std::endl;
    std::cout << "First Column : " << range.GetFirstColumn() << std::endl;
    std::cout << "Row Count : " << range.GetRowCount() << std::endl;
    std::cout << "Column Count : " << range.GetColumnCount() << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Åtkomst till namngivna områden**

#### **Åtkomst till ett specifikt namngivet område**

Anropa [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)-kollektionens [**GetRangeByName**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/getrangebyname/)-metod för att få ett område med det angivna namnet. En typisk [**GetRangeByName**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/getrangebyname/)-metod tar namnet på det namngivna området och returnerar det angivna namngivna området som en instans av klassen [**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/). Följande exempel visar hur man åtkommer ett angivet område med dess namn.

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"book1.xls";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Getting the specified named range
    Range range = workbook.GetWorksheets().GetRangeByName(u"TestRange");

    if (range)
    {
        std::cout << "Named Range : " << range.GetRefersTo().ToUtf8() << std::endl;
    }

    Aspose::Cells::Cleanup();
}
```

#### **Åtkomst till alla namngivna områden i ett kalkylblad**

Anropa [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) samlingens [**GetNamedRanges**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/getnamedranges/) metod för att få alla namngivna områden i ett kalkylblad. [**GetNamedRanges**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/getnamedranges/) metoden returnerar en array av alla namngivna områden i [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) samlingen.

Följande exempel visar hur man åtkommer alla namngivna områden i en arbetsbok.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String inputFilePath = srcDir + u"book1.xls";

    Workbook workbook(inputFilePath);
    WorksheetCollection sheets = workbook.GetWorksheets();
    Vector<Range> ranges = sheets.GetNamedRanges();

    std::cout << "Total Number of Named Ranges: " << ranges.GetLength() << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Kopiera namngivna områden**

Aspose.Cells erbjuder [**Range.Copy()**](https://reference.aspose.com/cells/cpp/aspose.cells/range/copy/) metod för att kopiera ett cellområde med formatering till ett annat område.

Följande exempel visar hur man kopierar en källräcka med celler till ett annat namngivet område.

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    Range range1 = worksheet.GetCells().CreateRange(u"E12", u"I12");
    range1.SetName(u"MyRange");

	Color borderColor = Color{ 0,0, 0, 128 };
    range1.SetOutlineBorder(BorderType::TopBorder, CellBorderType::Medium, borderColor);
    range1.SetOutlineBorder(BorderType::BottomBorder, CellBorderType::Medium, borderColor);
    range1.SetOutlineBorder(BorderType::LeftBorder, CellBorderType::Medium, borderColor);
    range1.SetOutlineBorder(BorderType::RightBorder, CellBorderType::Medium, borderColor);

    range1.Get(0, 0).PutValue(u"Test");
    range1.Get(0, 4).PutValue(u"123");

    Range range2 = worksheet.GetCells().CreateRange(u"B3", u"F3");
    range2.SetName(u"testrange");
    range2.Copy(range1);

    workbook.Save(outDir + u"copyranges.out.xls");

    std::cout << "Ranges copied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
