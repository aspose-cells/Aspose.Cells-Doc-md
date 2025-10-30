---
title: Zellen zusammenführen und aufheben mit C++
linktitle: Zusammenführen und Aufteilen von Zellen
description: Aspose.Cells ist eine C++ Bibliothek zum Arbeiten mit Tabellenkalkulationsdateien, die das Zusammenführen und Aufheben von Zellen unterstützt. Dieser Artikel führt ein, wie man Zellen mit der Aspose.Cells Bibliothek zusammenführt und aufhebt, und wie man den Stil der zusammengeführten Zelle anpasst.
keywords: Aspose.Cells, C++ Bibliothek, Tabellenkalkulation, Zellen zusammenführen, Zellen aufheben, Stileinstellungen, benutzerdefinierte Stile
type: docs
weight: 190
url: /de/cpp/merging-and-unmerging-cells/
---

{{% alert color="primary" %}} 

Aspose.Cells unterstützt diese Funktion und kann auch Zellen in einem Arbeitsblatt zusammenführen. Sie können auch Zellen trennen oder aufteilen. Der Zellenbezug einer zusammengeführten Zelle ist der Bezug der links oben Zelle im ursprünglich ausgewählten Bereich.

{{% /alert %}} 

## **Einführung**
Nicht immer benötigen Sie dieselbe Anzahl von Zellen in jeder Zeile oder Spalte. Zum Beispiel möchten Sie möglicherweise einen Titel in einer Zelle haben, die mehrere Spalten umspannt. Oder wenn Sie eine Rechnung erstellen, möchten Sie weniger Spalten für die Gesamtsumme haben. Um eine Zelle aus zwei oder mehr Zellen zu machen, führen Sie sie zusammen. Microsoft Excel ermöglicht es Benutzern, Zellen auszuwählen und zu verschmelzen, um die Tabelle nach ihren Wünschen zu strukturieren.

{{% alert color="primary" %}} 

Beachten Sie, dass beim Zusammenführen von Zellen nur die Daten in den links oben Zellen erhalten bleiben. Wenn Daten in den anderen Zellen im Bereich vorhanden sind, werden diese gelöscht.
Ebenso basiert die Formatierung auf der Bezugszelle, sodass beim Zusammenführen von Zellen die Formatierungseinstellungen der links oben Zelle im Bereich auf die zusammengeführte Zelle angewendet werden. Wenn die Zelle getrennt ist, behalten die neuen Zellen ihre ursprünglichen Formatierungseinstellungen bei.

{{% /alert %}} 

## **Zellen in einem Arbeitsblatt zusammenführen**
### **Zusammenführen von Zellen in Microsoft Excel**
Die folgenden Schritte beschreiben, wie Sie Zellen im Arbeitsblatt mit MS Excel zusammenführen können.

1. Kopieren Sie die Daten, die Sie in die oberste linke Zelle innerhalb des Bereichs einfügen möchten.
1. Wählen Sie die Zellen aus, die Sie zusammenführen möchten.
1. Um Zellen in einer Zeile oder Spalte zusammenzuführen und den Zellinhalt zu zentrieren, klicken Sie auf das Icon **Zusammenführen und Zentrieren** in der **Formatierung**-Symbolleiste.

### **Zellen zusammenführen mit Aspose.Cells**
Die Klasse `Aspose::Cells::Cells` bietet einige nützliche Methoden für diese Aufgabe. Zum Beispiel verbindet die Methode `Merge()` die Zellen zu einer einzelnen Zelle innerhalb eines bestimmten Bereichs.

Das folgende Beispiel zeigt, wie Zellen (C6:E7) in einem Arbeitsblatt zusammengeführt werden.

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

    // Create a Workbook
    Workbook wbk;

    // Create a Worksheet and get the first sheet
    Worksheet worksheet = wbk.GetWorksheets().Get(0);

    // Create a Cells object to fetch all the cells
    Cells cells = worksheet.GetCells();

    // Merge some Cells (C6:E7) into a single C6 Cell
    cells.Merge(5, 2, 2, 3);

    // Input data into C6 Cell
    worksheet.GetCells().Get(5, 2).PutValue(u"This is my value");

    // Create a Style object to fetch the Style of C6 Cell
    Style style = worksheet.GetCells().Get(5, 2).GetStyle();

    // Create a Font object
    Font font = style.GetFont();

    // Set the name
    font.SetName(u"Times New Roman");

    // Set the font size
    font.SetSize(18);

    // Set the font color
    font.SetColor(Color::Blue());

    // Bold the text
    font.SetIsBold(true);

    // Make it italic
    font.SetIsItalic(true);

    // Set the background color of C6 Cell to Red
    style.SetForegroundColor(Color::Red());
    style.SetPattern(BackgroundType::Solid);

    // Apply the Style to C6 Cell
    worksheet.GetCells().Get(5, 2).SetStyle(style);

    // Save the Workbook
    wbk.Save(outDir + u"mergingcells.out.xls");

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Aufsplitten (Teilen) von zusammengeführten Zellen**
### **Verwendung von Microsoft Excel**
Die folgenden Schritte beschreiben, wie Sie zusammengeführte Zellen mit Microsoft Excel aufspalten können.

1. Wählen Sie die zusammengeführte Zelle aus.
   Wenn Zellen kombiniert wurden, ist **Zusammenführen und Zentrieren** in der **Formatierung**-Symbolleiste ausgewählt.
1. Klicken Sie auf **Zusammenführen und Zentrieren** in der **Formatierung**-Symbolleiste.

### **Verwendung von Aspose.Cells**
Die Klasse `Aspose::Cells::Cells` hat eine Methode namens `UnMerge()`, die die Zellen in ihren ursprünglichen Zustand zurücksetzt. Die Methode hebt die Zusammenführung der Zellen auf, indem sie die Referenz der Zelle im Bereich der zusammengeführten Zellen verwendet.

Das folgende Beispiel zeigt, wie die zusammengeführten Zellen (C6) aufgeteilt werden. Das Beispiel verwendet die Datei, die im vorherigen Beispiel erstellt wurde, und teilt die zusammengeführten Zellen auf.

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"mergingcells.xls";

    // Path of output excel file
    U16String outputFilePath = outDir + u"unmergingcells.out.xls";

    // Create a Workbook and open the excel file
    Workbook wbk(inputFilePath);

    // Get the first worksheet
    Worksheet worksheet = wbk.GetWorksheets().Get(0);

    // Get the Cells object to fetch all the cells
    Cells cells = worksheet.GetCells();

    // Unmerge the cells
    cells.UnMerge(5, 2, 2, 3);

    // Save the file
    wbk.Save(outputFilePath);

    std::cout << "Cells unmerged successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Erweiterte Themen**
- [Erkennen von zusammengeführten Zellen in einem Arbeitsblatt](/cells/de/cpp/detect-merged-cells-in-a-worksheet/)
{{< app/cells/assistant language="cpp" >}}
