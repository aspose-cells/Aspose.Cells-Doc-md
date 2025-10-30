---
title: Wie man Drucktitel mit C++ festlegt
linktitle: Wie man Drucktitel festlegt
type: docs
weight: 200
url: /de/cpp/how-to-set-print-titles/
description: Dieser Artikel zeigt Ihnen Code, der erklärt, wie man Drucktitel mit der Aspose.Cells Bibliothek in C++ festlegt.
keywords: Zeilen und Spalten wiederholt drucken, C++ Wie man Drucktitel festlegt, Drucktitel mit C++ setzen und löschen, Drucktitel in C++ entfernen, Drucktitel in C++ hinzufügen, Drucktitel in Excel festlegen, Drucktitel in Excel löschen.
---

## **Mögliche Verwendungsszenarien**

Das Festlegen von Drucktiteln in Excel stellt sicher, dass bestimmte Zeilen oder Spalten auf jeder gedruckten Seite wiederholt werden, was besonders bei großen Tabellen, die sich über mehrere Seiten erstrecken, nützlich ist. Hier sind einige Gründe, warum Sie Drucktitel festlegen könnten:

1. Verbesserte Lesbarkeit: Drucktitel helfen den Lesern, die Daten zu verstehen, indem sie Kopfzeilen auf allen Seiten sichtbar halten, was die Interpretation der Informationen auf jeder Seite erleichtert, ohne auf die erste Seite zurückgreifen zu müssen.

1. Professionelles Erscheinungsbild: Das konsequente Anzeigen von Kopfzeilen oder Label auf jeder Seite schafft ein professionelleres und gepflegteres Druckdokument.

1. Verbesserte Navigation: Bei umfangreichen Daten ermöglicht das Wiederholen der Kopfzeilen auf jeder Seite eine schnellere Navigation und Referenzierung, wodurch das Hin- und Herblättern zwischen den Seiten reduziert wird.

1. Weniger Fehler: Wenn Kopfzeilen auf jeder Seite vorhanden sind, minimieren Sie die Chancen für Missinterpretationen oder Eingabefehler, da Benutzer den Datenzusammenhang leicht erkennen können.

1. Konsistenz: Die Sicherstellung, dass wichtige Informationen wie Spaltenüberschriften oder Zeilenbeschriftungen immer sichtbar sind, gewährleistet Konsistenz und Klarheit im gesamten Dokument.

## **So legen Sie Drucktitel in Excel fest**

Um Drucktitel in Excel festzulegen, folgen Sie diesen Schritten:

1. Öffnen Sie die Registerkarte Seitenlayout: Klicken Sie auf die Registerkarte "Seitenlayout" im Menüband oben im Excel-Fenster.
1. Zugriff auf Drucktitel: Klicken Sie im "Seiteneinrichtung"-Bereich auf "Drucktitel".
1. Zeilen zum Wiederholen festlegen: Im Dialogfeld "Seite einrichten" gehen Sie auf die Registerkarte "Blatt". Im Abschnitt "Drucktitel" geben Sie die Zeilen an, die oben wiederholt werden sollen, indem Sie das Kästchen neben "Zeilen, die oben wiederholt werden" aktivieren und die Zeile(n) auswählen, die wiederholt werden sollen.
1. Spalten zum Wiederholen festlegen (falls erforderlich): Ebenso können Sie die Spalten angeben, die links wiederholt werden sollen, indem Sie das Kästchen neben "Spalten, die links wiederholt werden" aktivieren und die Spalte(n) auswählen, die wiederholt werden sollen.
<br>
<img src="3.png" width=60% />

1. Bestätigen und Drucken: Klicken Sie auf "OK", um die Einstellungen anzuwenden. Beim Drucken des Arbeitsblatts erscheinen die angegebenen Zeilen oder Spalten auf jeder gedruckten Seite.

## **So entfernen Sie Drucktitel in Excel**

Um Drucktitel in Excel zu entfernen, müssen Sie die Zeilen oder Spalten löschen, die so eingestellt sind, dass sie auf jeder Seite wiederholt werden. So geht's:

1. Öffnen Sie die Registerkarte Seitenlayout: Klicken Sie auf die Registerkarte "Seitenlayout" im Menüband oben im Excel-Fenster.
1. Zugriff auf Drucktitel: Klicken Sie im "Seiteneinrichtung"-Bereich auf "Drucktitel".
1. Drucktitel entfernen: Im Dialogfeld "Seiteneinrichtung" wechseln Sie zum Reiter "Blatt". Löschen Sie den Text in den Feldern für "Zeilen, die oben wiederholt werden" und "Spalten, die links wiederholt werden", indem Sie den Inhalt löschen.
<br>
<img src="4.png" width=60% />

1. Bestätigen und schließen: Klicken Sie auf "OK", um die Änderungen zu übernehmen.

## **So setzen Sie Drucktitel mit Aspose.Cells**

Um Drucktitel in einem bestimmten Arbeitsblatt festzulegen: Laden Sie zuerst die [Beispieldatei](input.xlsx) und ändern Sie dann die Eigenschaften [**Worksheet.GetPrintTitleRows()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getprinttitlerows/) und [**Worksheet.GetPrintTitleColumns()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getprinttitlecolumns/) des Objekts [**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/) für das gewünschte Arbeitsblatt. Das Festlegen dieser Eigenschaften auf einen Range-String setzt die Drucktitel.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Load the workbook
    Workbook workbook(u"input.xlsx");

    // Access the desired worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Set rows to repeat at the top (e.g., rows 1 and 2)
    worksheet.GetPageSetup().SetPrintTitleRows(u"$1:$2");

    // Set columns to repeat at the left (e.g., columns A and B)
    worksheet.GetPageSetup().SetPrintTitleColumns(u"$A:$B");

    // Save the workbook
    workbook.Save(u"set_print_titles.pdf");

    std::cout << "Print titles set successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

Das Ausgabenergebnis:
<br>
<img src="1.png" width=60% />

## **So entfernen Sie Drucktitel mit Aspose.Cells**

Um Drucktitel in einem bestimmten Arbeitsblatt zu entfernen: Laden Sie zuerst die [Beispieldatei](input.xlsx) und ändern Sie dann die Eigenschaften [**Worksheet.GetPrintTitleRows()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getprinttitlerows/) und [**Worksheet.GetPrintTitleColumns()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getprinttitlecolumns/) des Objekts [**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/) für das gewünschte Arbeitsblatt. Das Festlegen dieser Eigenschaften auf einen leeren String löscht die Drucktitel.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Load the workbook
    U16String inputFilePath = u"input.xlsx";
    Workbook workbook(inputFilePath);

    // Access the desired worksheet
    WorksheetCollection sheets = workbook.GetWorksheets();
    Worksheet worksheet = sheets.Get(0);

    // Clear the rows and columns set to repeat
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetPrintTitleRows(u"");
    pageSetup.SetPrintTitleColumns(u"");

    // Save the workbook
    U16String outputFilePath = u"clear_print_titles.pdf";
    workbook.Save(outputFilePath);

    Aspose::Cells::Cleanup();
}
```

Das Ausgabenergebnis:
<br>
<img src="2.png" width=60% />
{{< app/cells/assistant language="cpp" >}}
