---
title: Wie man Excel als passende Seiten breit und hoch druckt mit C++
linktitle: Wie drucke ich Excel auf zugeschnittenen Seiten breit und hoch
type: docs
weight: 200
url: /de/cpp/how-to-print-excel-as-fitted-pages-wide-and-tall/
description: Dieser Artikel zeigt Ihnen Code, der erklärt, wie man mit Aspose.Cells Bibliothek mit C++ die Einstellungen FitToPagesWide und FitToPagesTall festlegt.
keywords: C++ Wie man FitToPagesWide und FitToPagesTall festlegt, Wie man FitToPagesWide und FitToPagesTall in C++ hinzufügt, Wie man FitToPagesWide und FitToPagesTall in Excel setzt, Wie man FitToPagesWide und FitToPagesTall in Excel löscht, Wie man Excel als passende Seiten breit und hoch druckt, Wie man Arbeitsblatt als eine Seite druckt, Wie man alle Spalten des Arbeitsblatts auf einer Seite druckt.
---

## **Einführung**

Die Einstellungen FitToPagesWide und FitToPagesTall werden in Tabellenkalkulationsanwendungen (wie Microsoft Excel) verwendet, um die Skalierung eines Tabellenblatts beim Drucken zu steuern. Diese Einstellungen helfen sicherzustellen, dass Ihre gedruckte Ausgabe innerhalb einer festgelegten Anzahl von Seiten passt, sowohl horizontal als auch vertikal. Hier eine Aufschlüsselung: 

1. FitToPagesWide: Diese Einstellung gibt die Anzahl der Seiten an, in die die gedruckte Ausgabe horizontal passt. Zum Beispiel bedeutet das Setzen von FitToPagesWide auf 1, dass der Inhalt auf die Breite einer Seite skaliert wird, egal wie breit das Tabellenblatt ist.
1. FitToPagesTall: Diese Einstellung gibt die Anzahl der Seiten an, in die die gedruckte Ausgabe vertikal passt. Zum Beispiel bedeutet das Setzen von FitToPagesTall auf 1, dass der Inhalt auf die Höhe einer Seite skaliert wird, unabhängig von der Anzahl der Zeilen.

## **Warum FitToPagesWide und FitToPagesTall verwenden**
Hier sind einige Gründe, warum Sie FitToPagesWide und FitToPagesTall einstellen sollten:
1. Kontrolle über das gedruckte Layout: Durch die Angabe der Anzahl der Seiten in der Breite und Höhe können Sie sicherstellen, dass Ihr gedrucktes Dokument leicht lesbar und gut organisiert ist, ohne dass Spalten oder Zeilen ungünstig auf mehrere Seiten aufgeteilt werden.
1. Konsistenz: Wenn Sie mehrere Blätter oder Berichte drucken, tragen diese Einstellungen dazu bei, ein einheitliches Format beizubehalten, was das Vergleichen und Analysieren gedruckter Dokumente erleichtert.
1. Professionelle Präsentation: Das richtige Skalieren und Anpassen des Inhalts an eine festgelegte Seitenzahl kann zu einer professionelleren und gepflegteren Präsentation Ihrer Daten führen.

## **So drucken Sie eine Datei als angepasste Seiten breit und hoch in Excel**

Um die Einstellungen FitToPagesWide und FitToPagesTall in Microsoft Excel festzulegen, befolgen Sie diese Schritte:

1. Öffnen Sie Ihre Excel-Arbeitsmappe und wechseln Sie auf das Blatt, das Sie drucken möchten.
1. Gehen Sie auf die Registerkarte Seitenlayout im Menüband.
1. Klicken Sie im Bereich Seite einrichten auf den kleinen Pfeil in der unteren rechten Ecke, um das Dialogfeld Seite einrichten zu öffnen.
1. Gehen Sie im Dialogfeld Seite einrichten auf die Registerkarte Seite.
1. Unter Skalierung wählen Sie die Option "Anpassen an" aus und geben Sie dann die Anzahl der Seiten in der Breite und Höhe an, die Sie möchten: Geben Sie die Anzahl der Seiten in der ersten Box (Anpassen an x Seiten breits) ein. Geben Sie die Anzahl der Seiten in der zweiten Box (Anpassen an y Seiten hoch) ein.
<br>
<img src="2.png" width=60% />

1. Klicken Sie auf OK, um die Einstellungen zu übernehmen.

## **So drucken Sie Excel als angepasste Seiten breit und hoch mit Aspose.Cells**

Um FitToPagesWide und FitToPagesTall in einem bestimmten Arbeitsblatt festzulegen: Laden Sie zunächst die [Beispiel-Datei](input.xlsx) und ändern Sie dann die Eigenschaften [**Worksheet.GetFitToPagesTall()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getfittopagestall/) und [**Worksheet.GetFitToPagesWide()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getfittopageswide/) des [**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/)-Objekts für das gewünschte Arbeitsblatt. Hier ist ein Beispiel in C++:

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiate a Workbook object
    Workbook workbook(U16String(u"input.xlsx"));

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Set the number of pages to which the length of the worksheet will be spanned
    worksheet.GetPageSetup().SetFitToPagesTall(1);

    // Set the number of pages to which the width of the worksheet will be spanned
    worksheet.GetPageSetup().SetFitToPagesWide(1);

    // Save the workbook
    workbook.Save(U16String(u"out_net.pdf"));

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

Das Ausgabenergebnis:
<br>
<img src="1.png" width=60% />

## **So drucken Sie ein Blatt als eine Seite mit Aspose.Cells**

Um Arbeitsblatt als eine Seite zu drucken: Laden Sie zunächst die [Beispiel-Datei](sample.xlsx) und setzen Sie dann die [**PdfSaveOptions.GetOnePagePerSheet()**](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/getonepagepersheet/)-Eigenschaft des [**PdfSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/)-Objekts. Hier ist ein Beispiel in C++:

```cpp
#include <iostream>
#include "Aspose.Cells.h"
#include "Aspose.Cells/PdfSaveOptions.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiating a Workbook object
    Workbook workbook(u"sample.xlsx");

    // Create PdfSaveOptions object
    PdfSaveOptions options;

    // Set options for exporting PDF
    options.SetOnePagePerSheet(true);

    // Save the workbook to a PDF file
    workbook.Save(u"OnePagePerSheet.pdf", options);

    std::cout << "Workbook saved as OnePagePerSheet.pdf!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

Das Ausgabenergebnis:
<br>
<img src="3.png" width=60% />

## **So drucken Sie alle Spalten eines Arbeitsblatts auf einer Seite mit Aspose.Cells**

Um alle Spalten des Arbeitsblatts auf einer Seite zu drucken: Laden Sie zunächst die [Beispiel-Datei](sample.xlsx) und setzen Sie dann die [**PdfSaveOptions.GetAllColumnsInOnePagePerSheet()**](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/getallcolumnsinonepagepersheet/)-Eigenschaft des [**PdfSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/)-Objekts. Hier ist ein Beispiel in C++:

```c++
#include <iostream>
#include "Aspose.Cells.h"
#include "Aspose.Cells/PdfSaveOptions.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiate a Workbook object with the specified file.
    Workbook workbook(u"sample.xlsx");

    // Create PdfSaveOptions instance.
    PdfSaveOptions options;

    // Set options for saving the workbook as a PDF.
    options.SetAllColumnsInOnePagePerSheet(true);

    // Save the workbook as a PDF file with the specified options.
    workbook.Save(u"AllColumnsInOnePagePerSheet.pdf", options);

    std::cout << "Workbook saved successfully as PDF!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

Das Ausgabenergebnis:
<br>
<img src="4.png" width=60% />
