---
title: Zeigen und Ausblenden von Gitternetzlinien und Zeilen sowie Spaltenüberschriften mit C++
linktitle: Rastlinien und Zeilen / Spaltenüberschriften ein und ausblenden
type: docs
weight: 30
url: /de/cpp/show-and-hide-gridlines-and-row-column-headers/
description: Dieser Artikel enthält Beispielcode für die Verwendung der C++ API oder Bibliothek, um programmgesteuert Gitterlinien sowie Zeilen und Spaltenüberschriften eines Excel Arbeitsblatts auszublenden oder anzuzeigen.
---

{{% alert color="primary" %}}

Aspose.Cells unterstützt das Ausblenden und Anzeigen von Rasterlinien des Arbeitsblatts, die standardmäßig sichtbar sind. Es ermöglicht auch die Kontrolle der Sichtbarkeit von Zeilen- und Spaltenüberschriften des Arbeitsblatts.

{{% /alert %}}

## **Rasterlinien anzeigen und ausblenden**

Alle Excel-Arbeitsblätter haben standardmäßig Rasterlinien. Sie helfen dabei, Zellen abzugrenzen, sodass es einfach ist, Daten in bestimmte Zellen einzugeben. Rasterlinien ermöglichen es uns, ein Arbeitsblatt als eine Sammlung von Zellen zu betrachten, bei der jede Zelle leicht identifizierbar ist.

### **Steuerung der Sichtbarkeit der Rastlinien**

Aspose.Cells bietet eine Klasse, [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), die eine Microsoft Excel-Datei repräsentiert. Die Klasse [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) enthält eine [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)-Sammlung, mit der Entwickler auf jedes Arbeitsblatt in der Excel-Datei zugreifen können. Ein Arbeitsblatt wird durch die Klasse [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) dargestellt. Die Klasse [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) bietet eine Vielzahl von Eigenschaften und Methoden zur Verwaltung eines Arbeitsblatts. Um die Sichtbarkeit der Gitterlinien zu steuern, verwenden Sie die Klasse [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) Eigenschaft [**IsGridlinesVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/isgridlinesvisible/). [**IsGridlinesVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/isgridlinesvisible/) ist eine boolesche Eigenschaft, die bedeutet, dass sie nur einen Wert **true** oder **false** speichern kann.

#### **Anzeigen von Rasterlinien**

Machen Sie die Gitterlinien sichtbar, indem Sie die Eigenschaft [**IsGridlinesVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/isgridlinesvisible/) der Klasse [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) auf **true** setzen.

#### **Rasterspalten ausblenden**

Verstecken Sie die Gitterlinien, indem Sie die Eigenschaft [**IsGridlinesVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/isgridlinesvisible/) der Klasse [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) auf **false** setzen.

Nachfolgend wird ein vollständiges Beispiel gezeigt, das die Verwendung der Eigenschaft [**IsGridlinesVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/isgridlinesvisible/) demonstriert, indem eine Excel-Datei (book1.xls) geöffnet, die Gitterlinien im ersten Arbeitsblatt ausgeblendet und die geänderte Datei als output.xls gespeichert wird.

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
    U16String inputFilePath = srcDir + u"book1.xls";

    // Create workbook from file
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Hide the grid lines of the first worksheet
    worksheet.SetIsGridlinesVisible(false);

    // Save the modified Excel file
    U16String outputFilePath = srcDir + u"output.xls";
    workbook.Save(outputFilePath);

    std::cout << "Grid lines hidden successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Zeigen und Ausblenden der Zeilen- und Spaltenüberschriften**

Alle Arbeitsblätter in einer Excel-Datei bestehen aus Zellen, die in Zeilen und Spalten angeordnet sind. Alle Zeilen und Spalten haben eindeutige Werte, die zur Identifizierung und zum Identifizieren einzelner Zellen verwendet werden. Beispielsweise sind Zeilen nummeriert – 1, 2, 3, 4 usw. – und Spalten sind alphabetisch geordnet – A, B, C, D usw. Die Zeilen- und Spaltenwerte werden in den Überschriften angezeigt. Mit Aspose.Cells können Entwickler die Sichtbarkeit dieser Zeilen- und Spaltenüberschriften steuern.

### **Steuerung der Sichtbarkeit der Arbeitsblätter**

Aspose.Cells bietet eine Klasse, [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), die eine Microsoft Excel-Datei repräsentiert. Die Klasse [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) enthält eine [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)-Sammlung, mit der Entwickler auf jedes Arbeitsblatt in der Excel-Datei zugreifen können. Ein Arbeitsblatt wird durch die Klasse [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) dargestellt. Die Klasse [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) bietet eine Vielzahl von Eigenschaften und Methoden zur Verwaltung eines Arbeitsblatts. Um die Sichtbarkeit der Zeilen- und Spaltenüberschriften zu steuern, verwenden Sie die Klasse [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) Eigenschaft [**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/isrowcolumnheadersvisible/). [**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/isrowcolumnheadersvisible/) ist eine boolesche Eigenschaft, die bedeutet, dass sie nur einen Wert **true** oder **false** speichern kann.

#### **Anzeigen von Zeilen-/Spaltenüberschriften**

Machen Sie Zeilen- und Spaltenüberschriften sichtbar, indem Sie die Eigenschaft [**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/isrowcolumnheadersvisible/) der Klasse [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) auf **true** setzen.

#### **Zeilen-/Spaltenheader ausblenden**

Zeilen- und Spaltenüberschriften ausblenden, indem die [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) Klasse [**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/isrowcolumnheadersvisible/) Eigenschaft auf **false** gesetzt wird.

Ein vollständiges Beispiel unten zeigt, wie die [**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/isrowcolumnheadersvisible/) Eigenschaft verwendet wird, indem eine Excel-Datei (book1.xls) geöffnet, die Zeilen- und Spaltenüberschriften im ersten Arbeitsblatt ausgeblendet und die geänderte Datei als output.xls gespeichert wird.

```cpp
#include <iostream>
#include <memory>
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
    U16String outputFilePath = outDir + u"output.xls";

    // Create workbook from the input file
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Hide the headers of rows and columns
    worksheet.SetIsRowColumnHeadersVisible(false);

    // Save the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Headers hidden successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

Es ist auch möglich, die Methoden [**UnhideRows**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/unhiderows/) und [**UnhideColumns**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/unhidecolumns/) der [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) Klasse zu verwenden, um mehrere Zeilen und Spalten sichtbar zu machen.

{{% /alert %}}
{{< app/cells/assistant language="cpp" >}}
