---
title: Zeilen und Spalten mit C++ automatisch anpassen
linktitle: Zeilen und Spalten automatisch anpassen
type: docs
weight: 20
url: /de/cpp/autofit-rows-and-columns/
description: Dieser Artikel zeigt, wie man Zeilen, Spalten, Zeilen von zusammengeführten Zellen und Zeilen in einem Zellbereich automatisch anpasst, indem die API Aspose.Cells for C++ verwendet wird.
keywords: Zeilen automatisch anpassen, Spalten automatisch anpassen, Zeile in einem Zellenbereich automatisch anpassen, Zeilen von zusammengeführten Zellen automatisch anpassen
---

{{% alert color="primary" %}}

Microsoft Excel ermöglicht es Nutzern, die Breite und Höhe der Zellen automatisch der jeweiligen Inhalte anzupassen. Diese Funktion ist auch über Aspose.Cells verfügbar, sodass Entwickler die Abmessungen einer Zelle zur Laufzeit automatisch anpassen können.

{{% /alert %}}

## **Automatische Anpassung**

Aspose.Cells stellt die Klasse [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) bereit, die eine Microsoft Excel-Datei repräsentiert. Die Klasse [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) enthält eine Sammlung [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/), die den Zugriff auf jedes Arbeitsblatt in einer Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch die Klasse [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) dargestellt. Die Klasse [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) bietet eine Vielzahl von Methoden zur Verwaltung eines Arbeitsblatts. Dieser Artikel behandelt die Verwendung der [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)-Klasse zum automatischen Anpassen von Zeilen oder Spalten.

### **AutoFit Zeile - Einfach**

Der einfachste Ansatz, um die Breite und Höhe einer Zeile automatisch anzupassen, besteht darin, die Methode [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) der [**AutoFitRow**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/autofitrow/)-Klasse aufzurufen. Die [**AutoFitRow**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/autofitrow/)-Methode nimmt einen Zeilenindex (der Zeile, die angepasst werden soll) als Parameter.

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

    // Auto-fit the 2nd row (index 1) of the worksheet
    worksheet.AutoFitRow(1);

    // Save the modified Excel file
    U16String outputFilePath = srcDir + u"output.xlsx";
    workbook.Save(outputFilePath);

    std::cout << "Row auto-fitted and file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **Wie man eine Zeile in einem Zellenbereich automatisch anpasst**

Eine Zeile besteht aus vielen Spalten. Aspose.Cells ermöglicht es Entwicklern, eine Zeile basierend auf den Inhalten innerhalb eines Zellbereichs in der Zeile automatisch anzupassen, indem eine überladene Version der Methode [**AutoFitRow**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/autofitrow/) aufgerufen wird. Diese nimmt die folgenden Parameter entgegen:

- **Zeilenindex**, der Index der zu automatisch anzupassenden Zeile.
- **Erster Spaltenindex**, der Index der ersten Spalte der Zeile.
- **Letzter Spaltenindex**, der Index der letzten Spalte der Zeile.

Die [**AutoFitRow**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/autofitrow/)-Methode überprüft den Inhalt aller Spalten in der Zeile und passt die Zeile entsprechend an.

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

    // Path of output Excel file
    U16String outputFilePath = outDir + u"output.xlsx";

    // Open the Excel file
    Workbook workbook(inputFilePath);

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Auto-fitting the 3rd row of the worksheet
    worksheet.AutoFitRow(1, 0, 5);

    // Save the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Row auto-fitted and file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Wie man eine Spalte in einem Zellenbereich automatisch anpasst**

Eine Spalte besteht aus vielen Zeilen. Es ist möglich, eine Spalte basierend auf den Inhalten in einem Zellbereich in der Spalte automatisch anzupassen, indem eine überladene Version der [**AutoFitColumn**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/autofitcolumn/)-Methode aufgerufen wird, die die folgenden Parameter akzeptiert:

- **Spaltenindex**, der Index der zu automatisch anzupassenden Spalte.
- **Erster Zeilenindex**, der Index der ersten Zeile der Spalte.
- **Letzter Zeilenindex**, der Index der letzten Zeile der Spalte.

Die [**AutoFitColumn**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/autofitcolumn/)-Methode überprüft den Inhalt aller Zeilen in der Spalte und passt die Spalte entsprechend an.

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

    // Auto-fit the 5th column (index 4) from row 4 to 6
    worksheet.AutoFitColumn(4, 4, 6);

    // Save the modified Excel file
    U16String outputFilePath = srcDir + u"output.xlsx";
    workbook.Save(outputFilePath);

    std::cout << "Column auto-fitted and file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Wie man Zeilen für zusammengeführte Zellen automatisch anpasst**

Mit Aspose.Cells ist es möglich, Zeilen auch bei zusammengeführten Zellen mit Hilfe der [**AutoFitterOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/autofitteroptions/)-API automatisch anzupassen. Die [**AutoFitterOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/autofitteroptions/)-Klasse bietet die Eigenschaft [**GetAutoFitMergedCellsType()**](https://reference.aspose.com/cells/cpp/aspose.cells/autofitteroptions/getautofitmergedcellstype/), mit der Zeilen für zusammengeführte Zellen automatisch angepasst werden können. [**GetAutoFitMergedCellsType()**](https://reference.aspose.com/cells/cpp/aspose.cells/autofitteroptions/getautofitmergedcellstype/) akzeptiert die [**AutoFitMergedCellsType**](https://reference.aspose.com/cells/cpp/aspose.cells/autofitmergedcellstype/)-Aufzählung, die folgende Mitglieder hat:

- Keine: Zusammengeführte Zellen ignorieren.
- ErsteZeile: Erweitert nur die Höhe der ersten Zeile.
- LetzteZeile: Erweitert nur die Höhe der letzten Zeile.
- JedeZeile: Erweitert nur die Höhe jeder Zeile.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Output directory
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Instantiate a new Workbook
    Workbook wb;

    // Get the first (default) worksheet
    Worksheet worksheet = wb.GetWorksheets().Get(0);

    // Create a range A1:B1
    Range range = worksheet.GetCells().CreateRange(0, 0, 1, 2);

    // Merge the cells
    range.Merge();

    // Insert value to the merged cell A1
    worksheet.GetCells().Get(0, 0).SetValue(u"A quick brown fox jumps over the lazy dog. A quick brown fox jumps over the lazy dog....end");

    // Create a style object
    Style style = worksheet.GetCells().Get(0, 0).GetStyle();

    // Set wrapping text on
    style.SetIsTextWrapped(true);

    // Apply the style to the cell
    worksheet.GetCells().Get(0, 0).SetStyle(style);

    // Create an object for AutoFitterOptions
    AutoFitterOptions options;

    // Set auto-fit for merged cells
    options.SetAutoFitMergedCellsType(AutoFitMergedCellsType::EachLine);

    // Autofit rows in the sheet (including the merged cells)
    worksheet.AutoFitRows(options);

    // Save the Excel file
    wb.Save(outDir + u"AutofitRowsforMergedCells.xlsx");

    std::cout << "Autofit rows for merged cells completed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

Sie können auch versuchen, die überladenen Versionen der Methoden [**AutoFitRows**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/autofitrows/) und [**AutoFitColumns**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/autofitcolumns/) zu verwenden, die einen Zellbereich und eine Instanz von [**AutoFitterOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/autofitteroptions/) akzeptieren, um die ausgewählten Zeilen/Spalten entsprechend Ihrem gewünschten [**AutoFitterOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/autofitteroptions/) automatisch anzupassen.

Die Signaturen der genannten Methoden sind wie folgt:

1. AutoFitRows(int startRow, int endRow, [**AutoFitterOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/autofitteroptions/) options)
1. AutoFitColumns(int firstColumn, int lastColumn, [**AutoFitterOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/autofitteroptions/) options)

{{% /alert %}}

## **Wichtig zu wissen**

{{% alert color="primary" %}}

Wenn eine Zelle zusammengeführt ist, werden die AutoFit-Methoden nicht angewendet, was dem Verhalten in Microsoft Excel entspricht. Sie können dies umgehen, indem Sie die AutoFilter-API verwenden. Außerdem wird die [**AutoFitColumn**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/autofitcolumn/)-Methode nicht ausgeführt, wenn der Text in einer Zelle umbrochen ist. Eine weitere wichtige Information ist, dass die *AutoFit*-Methoden sehr zeitaufwendig sind. Daher sollten Sie diese Methoden nur sparsam aufrufen, um die Effizienz Ihrer Anwendung zu gewährleisten.

{{% /alert %}}

## **Fortgeschrittene Themen**
- [Automatisches Anpassen von Zeilen für zusammengeführte Zellen](/cells/de/cpp/autofit-rows-for-merged-cells/)
