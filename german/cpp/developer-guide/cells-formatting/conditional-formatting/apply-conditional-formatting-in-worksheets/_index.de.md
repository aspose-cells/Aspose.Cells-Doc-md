---
title: Bedingte Formatierung in Arbeitsblättern mit C++ anwenden
linktitle: Bedingte Formatierung anwenden
description: So verwenden Sie die Aspose.Cells Bibliothek in C++, um in Arbeitsblättern bedingte Formatierungen anzuwenden. Durch die Anpassung dieser Kriterien haben Sie mehr Kontrolle darüber, wie Zellen aussehen und erscheinen.
keywords: Aspose.Cells, Bedingte Formatierung, C++, Arbeitsblatt, Formatierung
type: docs
weight: 130
url: /de/cpp/apply-conditional-formatting-in-worksheets/
---

{{% alert color="primary" %}}

Dieser Artikel soll ein detailliertes Verständnis dafür vermitteln, wie bedingte Formatierung auf eine Zellenreihe in einem Arbeitsblatt angewendet wird.

Bedingte Formatierung ist eine fortgeschrittene Funktion in Microsoft Excel, die es ermöglicht, Formate auf eine Zellenreihe anzuwenden und diese Formatierung je nach dem Wert der Zelle oder dem Wert einer Formel zu ändern. Zum Beispiel kann der Hintergrund einer Zelle rot sein, um einen negativen Wert hervorzuheben, oder die Textfarbe könnte grün sein, um einen positiven Wert hervorzuheben. Wenn der Wert der Zelle die Formatbedingung erfüllt, wird das Format angewendet. Erfüllt der Wert der Zelle die Formatbedingung nicht, wird das Standardformat der Zelle verwendet.

Es ist möglich, bedingte Formatierungen mit Microsoft Office Automation anzuwenden, aber das hat seine Nachteile. Es gibt mehrere Gründe und Probleme, die damit verbunden sind: zum Beispiel Sicherheit, Stabilität, Skalierbarkeit und Geschwindigkeit. Der Hauptgrund, nach einer anderen Lösung zu suchen, ist, dass Microsoft selbst die Nutzung von Office Automation für Softwarelösungen nachdrücklich ablehnt.

Dieser Artikel zeigt, wie man eine Konsolenanwendung erstellt, bedingte Formatierung auf Zellen mit einigen einfachsten Zeilen Code mithilfe der Aspose.Cells API hinzufügt.

{{% /alert %}}

## **Verwendung von Aspose.Cells zur Anwendung bedingter Formatierung basierend auf Zellenwert**

1. **Aspose.Cells herunterladen und installieren**.
   1. Laden Sie Aspose.Cells for C++ herunter.
1. Installieren Sie es auf Ihrem Entwicklungscomputer.
   Alle Aspose-Komponenten arbeiten im Evaluierungsmodus, wenn sie installiert sind. Der Evaluierungsmodus hat kein Zeitlimit und fügt nur Wasserzeichen in erstellte Dokumente ein.
1. **Ein Projekt erstellen**.
   Starten Sie Ihre C++-Entwicklungsumgebung und erstellen Sie eine neue Konsolenanwendung.
1. **Verweise hinzufügen**.
   Fügen Sie Ihrem Projekt einen Verweis auf Aspose.Cells hinzu, beispielsweise fügen Sie einen Verweis auf ….\Program Files\Aspose\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dll hinzu
1. **Bedingte Formatierung basierend auf Zellwert anwenden**.
   Der unten stehende Code zeigt, wie die Aufgabe umgesetzt wird. Er wendet bedingte Formatierung auf eine Zelle an.

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

    // Instantiating a Workbook object
    Workbook workbook;

    // Get the first worksheet
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Adds an empty conditional formatting
    int index = sheet.GetConditionalFormattings().Add();

    // Get the FormatConditionCollection
    FormatConditionCollection fcs = sheet.GetConditionalFormattings().Get(index);

    // Sets the conditional format range
    CellArea ca = CellArea::CreateCellArea(0, 0, 0, 0);

    // Add the cell area to the format condition collection
    fcs.AddArea(ca);

    // Adds condition
    int conditionIndex = fcs.AddCondition(FormatConditionType::CellValue, OperatorType::Between, u"50", u"100");

    // Get the format condition
    FormatCondition fc = fcs.Get(conditionIndex);

    // Sets the background color
    fc.GetStyle().SetBackgroundColor(Color::Red());

    // Saving the Excel file
    workbook.Save(outDir + u"output.out.xls", SaveFormat::Auto);

    std::cout << "Conditional formatting applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

Wenn der obige Code ausgeführt wird, wird die bedingte Formatierung auf die Zelle „A1“ im ersten Arbeitsblatt der Ausgabedatei (output.xls) angewendet. Die angewendete bedingte Formatierung auf A1 hängt vom Zellwert ab. Wenn der Zellwert von A1 zwischen 50 und 100 liegt, ist die Hintergrundfarbe aufgrund der angewendeten bedingten Formatierung rot.

## **Mit Aspose.Cells bedingte Formatierung basierend auf Formel anwenden**

1. **Anwenden bedingter Formatierung abhängig von einer Formel (Codeausschnitt)**
   Im Folgenden finden Sie den Code zur Durchführung der Aufgabe. Er wendet bedingte Formatierung auf B3 an.

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

    // Create workbook
    Workbook workbook;

    // Get the first worksheet
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Adds an empty conditional formatting
    int index = sheet.GetConditionalFormattings().Add();

    // Get the conditional formatting collection
    FormatConditionCollection fcs = sheet.GetConditionalFormattings().Get(index);

    // Sets the conditional format range
    CellArea ca = CellArea::CreateCellArea(2, 1, 2, 1);

    // Add the area to the conditional formatting
    fcs.AddArea(ca);

    // Adds condition
    int conditionIndex = fcs.AddCondition(FormatConditionType::Expression);

    // Get the format condition
    FormatCondition fc = fcs.Get(conditionIndex);

    // Set the formula for the condition
    fc.SetFormula1(u"=IF(SUM(B1:B2)>100,TRUE,FALSE)");

    // Set the background color
    Style style = fc.GetStyle();
    style.SetBackgroundColor(Color::Red());
    fc.SetStyle(style);

    // Set the formula for cell B3
    sheet.GetCells().Get(u"B3").SetFormula(u"=SUM(B1:B2)");

    // Set the value for cell C4
    sheet.GetCells().Get(u"C4").PutValue(u"If Sum of B1:B2 is greater than 100, B3 will have RED background");

    // Save the Excel file
    workbook.Save(outDir + u"output.out.xls", SaveFormat::Auto);

    std::cout << "Conditional formatting applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

Wenn der obige Code ausgeführt wird, wird die bedingte Formatierung auf die Zelle „B3“ im ersten Arbeitsblatt der Ausgabedatei (output.xls) angewendet. Die bedingte Formatierung hängt von der Formel ab, die den Wert von B3 als Summe von B1 & B2 berechnet.
{{< app/cells/assistant language="cpp" >}}
