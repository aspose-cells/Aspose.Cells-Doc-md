---  
title: Zugriff auf Tabelle aus Zelle und Hinzufügen von Werten mit Zeilen und Spaltenverschiebungen in C++  
linktitle: Zugriff auf Tabelle von Zelle und Hinzufügen von Werten in sie unter Verwendung von Zeilen und Spaltenversatz  
type: docs  
weight: 230  
url: /de/cpp/accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets/  
description: Greifen Sie auf eine Tabelle aus einer Zelle zu und fügen Sie Werte mit Aspose.Cells in C++ hinzu.  
---  

{{% alert color="primary" %}}  

Normalerweise fügen Sie Werte in die Tabelle oder das Listenobjekt mit der [**Cell.PutValue()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/putvalue/)-Methode ein. Manchmal müssen Sie jedoch Werte in die Tabelle oder das Listenobjekt unter Verwendung des Zeilen- und Spaltenoffsets hinzufügen.  

Um auf eine Tabelle oder Listenobjekt aus einer Zelle zuzugreifen, verwenden Sie die [**Cell.GetTable()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/gettable/)-Methode. Um Werte mit Zeilen- und Spaltenverschiebungen hinzuzufügen, verwenden Sie die [**ListObject.PutCellValue**](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listobject/putcellvalue/)-Methode.  

{{% /alert %}}  

Das folgende Screenshot zeigt die Quell-Excel-Datei, die im Code verwendet wird. Es enthält die leere Tabelle und hebt die Zelle D5 hervor, die innerhalb der Tabelle liegt. Wir greifen auf diese Tabelle über die Zelle D5 mit der [**Cell.GetTable()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/gettable/)-Methode zu und fügen dann die Werte mit den [**Cell.PutValue()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/putvalue/)- und [**ListObject.PutCellValue**](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listobject/putcellvalue/)-Methoden hinzu.  

## Beispiel  

### Screenshots zum Vergleich der Quell- und Ausgabedateien  

|![todo:image_alt_text](accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets_1.png)|  
| :- |  

Der folgende Screenshot zeigt die durch den Code generierte Ausgabedatei. Wie Sie sehen können, hat die Zelle D5 einen Wert und die Zelle F6, die sich im Offset 2,2 der Tabelle befindet, hat ebenfalls einen Wert.  

|![todo:image_alt_text](accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets_2.png)|  
| :- |  

### C++-Code zum Zugriff auf eine Tabelle aus einer Zelle und zum Hinzufügen von Werten mit Zeilen- und Spaltenverschiebungen  

Der folgende Beispielcode lädt die oben gezeigte Excel-Quelldatei und fügt Werte in die Tabelle ein, um die oben gezeigte Ausgabedatei zu generieren.  

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
