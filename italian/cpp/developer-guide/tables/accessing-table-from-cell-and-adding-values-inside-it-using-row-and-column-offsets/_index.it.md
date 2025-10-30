---  
title: Accesso a una tabella da una cella e aggiunta di valori al suo interno usando offset di riga e colonna con C++  
linktitle: Accesso alla Tabella da una Cella e Aggiunta di Valori al suo Interno utilizzando Offset di Riga e Colonna  
type: docs  
weight: 230  
url: /it/cpp/accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets/  
description: Accedi a una tabella da una cella e aggiungi valori usando Aspose.Cells con C++.  
---  

{{% alert color="primary" %}}  

Normalmente, si aggiungono valori all'interno della Tabella o dell'oggetto Lista utilizzando il metodo [**Cell.PutValue()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/putvalue/). Ma a volte potresti dover aggiungere valori all'interno della Tabella o dell'oggetto Lista utilizzando gli offset di riga e colonna.  

Per accedere a una tabella o oggetto Lista da una cella, utilizza il metodo [**Cell.GetTable()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/gettable/). Per aggiungere valori al suo interno usando offset di riga e colonna, utilizza il metodo [**ListObject.PutCellValue**](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listobject/putcellvalue/).  

{{% /alert %}}  

Il seguente screenshot mostra il file Excel di origine usato nel codice. Contiene la tabella vuota e evidenzia la cella D5 che si trova all’interno della tabella. Accederemo a questa tabella dalla cella D5 usando il metodo [**Cell.GetTable()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/gettable/) e poi aggiungeremo i valori al suo interno usando entrambi i metodi [**Cell.PutValue()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/putvalue/) e [**ListObject.PutCellValue**](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listobject/putcellvalue/).  

## Esempio  

### Screenshots che confrontano i file di origine e di output  

|![todo:image_alt_text](accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets_1.png)|  
| :- |  

Lo screenshot seguente mostra il file Excel di output generato dal codice. Come puoi vedere, la cella D5 ha un valore e la cella F6 che si trova all'offset 2,2 della tabella ha un valore.  

|![todo:image_alt_text](accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets_2.png)|  
| :- |  

### Codice C++ per accedere a una tabella da una cella e aggiungere valori al suo interno usando offset di riga e colonna  

Il codice di esempio seguente carica il file Excel di origine come mostrato nello screenshot precedente e aggiunge valori all'interno della tabella e genera il file Excel di output come mostrato sopra.  

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
