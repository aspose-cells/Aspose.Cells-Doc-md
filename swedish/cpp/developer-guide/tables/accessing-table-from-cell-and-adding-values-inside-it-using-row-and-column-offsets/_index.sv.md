---  
title: Åtkomst till tabell från cell och lägga till värden inuti med rad och kolumnförskjutningar med C++  
linktitle: Få åtkomst till tabell från cell och lägg till värden inuti den med hjälp av rad och kolumnförflyttningar  
type: docs  
weight: 230  
url: /sv/cpp/accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets/  
description: Åtkomst till en tabell från en cell och lägg till värden med hjälp av Aspose.Cells och C++.  
---  

{{% alert color="primary" %}}  

Normalt sett lägger du till värden inuti tabellen eller listobjektet med hjälp av [**Cell.PutValue()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/putvalue/)-metoden. Men ibland kan du behöva lägga till värden inuti tabellen eller listobjektet med rad- och kolumnförflyttningar.  

För att komma åt tabell eller lista objekt från en cell, använd [**Cell.GetTable()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/gettable/)-metoden. För att lägga till värden inuti den med hjälp av rad- och kolumnförskjutningar, använd [**ListObject.PutCellValue**](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listobject/putcellvalue/)-metoden.  

{{% /alert %}}  

Följande skärmbild visar käll-Excel-filen som används i koden. Den innehåller den tomma tabellen och markerar cell D5 som ligger inuti tabellen. Vi kommer att komma åt denna tabell från cell D5 med hjälp av [**Cell.GetTable()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/gettable/)-metoden och sedan lägga till värden inuti den med hjälp av både [**Cell.PutValue()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/putvalue/) och [**ListObject.PutCellValue**](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listobject/putcellvalue/)-metoder.  

## Exempel  

### Skärmbilder som jämför käll- och utdatafiler  

|![todo:image_alt_text](accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets_1.png)|  
| :- |  

Följande skärmbild visar den genererade utdata-Excel-filen av koden. Som du kan se har cellen D5 ett värde och cellen F6, som ligger vid förflyttning 2,2 inuti tabellen, har ett värde.  

|![todo:image_alt_text](accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets_2.png)|  
| :- |  

### C++ kod för att komma åt tabell från cell och för att lägga till värden inuti med rad- och kolumnförskjutningar  

Följande provkod laddar den angivna källan Excel-filen som visas i skärmdumpen ovan och lägger till värden inne i tabellen och genererar den resulterande Excel-filen som visas ovan.  

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

    // Create workbook from source Excel file
    Workbook workbook(srcDir + u"source.xlsx");

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access cell D5 which lies inside the table
    Cell cell = worksheet.GetCells().Get(u"D5");

    // Put value inside the cell D5
    cell.PutValue(u"D5 Data");

    // Access the Table from this cell
    ListObject table = cell.GetTable();

    // Add some value using Row and Column Offset
    table.PutCellValue(2, 2, u"Offset [2,2]");

    // Save the workbook
    workbook.Save(outDir + u"output_out.xlsx");

    std::cout << "Workbook saved successfully." << std::endl;

    Aspose::Cells::Cleanup();
}
```  
{{< app/cells/assistant language="cpp" >}}
