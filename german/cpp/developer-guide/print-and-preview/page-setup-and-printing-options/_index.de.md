---
title: Seitenlayout und Druckoptionen mit C++
linktitle: Seiteneinrichtung und Druckoptionen
type: docs
weight: 60
url: /de/cpp/page-setup-and-printing-options/
description: Konfigurieren Sie Seitenlayout und Druckeinstellungen zur Steuerung des Druckprozesses mit Aspose.Cells für C++.
---

{{% alert color="primary" %}}

Manchmal müssen Entwickler die Seiteneinrichtung und die Druckeinstellungen konfigurieren, um den Druckprozess zu steuern. Die Seiteneinrichtung und Druckeinstellungen bieten verschiedene Optionen und werden von Aspose.Cells vollständig unterstützt.

Dieser Artikel zeigt, wie man eine Konsolenanwendung in Visual Studio erstellt und Seitenlayout- sowie Druckoptionen mit nur wenigen Zeilen Code mithilfe der Aspose.Cells API auf ein Arbeitsblatt anwendet.

{{% /alert %}}

## **Arbeiten mit Seiten- und Druckeinstellungen**

Für dieses Beispiel haben wir eine Arbeitsmappe in Microsoft Excel erstellt und Aspose.Cells verwendet, um die Seiteneinrichtung und Druckoptionen festzulegen.

### **Verwenden von Aspose.Cells zum Festlegen von Seiteneinrichtungsoptionen**

Erstellen Sie zuerst ein einfaches Arbeitsblatt in Microsoft Excel. Wenden Sie dann Seiteneinrichtungsoptionen darauf an. Das Ausführen des Codes ändert die Seiteneinrichtungsoptionen, wie im Screenshot unten dargestellt.

|**Ausgabedatei.**|
| :- |
|![todo:image_alt_text](page-setup-and-printing-options_1.png)|

1. Erstellen Sie ein Arbeitsblatt mit einigen Daten in Microsoft Excel:
   1. Öffnen Sie eine neue Arbeitsmappe in Microsoft Excel.
   1. Fügen Sie einige Daten hinzu.
1. Legen Sie Seiteneinrichtungsoptionen fest:
   Wenden Sie die Seiteneinrichtungsoptionen auf die Datei an. Unten ist ein Screenshot der Standardoptionen vor der Anwendung der neuen Optionen zu sehen.

|**Standardseiteneinrichtungsoptionen.**|
| :- |
|![todo:image_alt_text](page-setup-and-printing-options_2.png)|

1. Laden Sie Aspose.Cells herunter und installieren Sie es:
   1. [Herunterladen](https://downloads.aspose.com/cells/cpp) Aspose.Cells for C++.
   1. Installieren Sie es auf Ihrem Entwicklungscomputer.
      Alle Aspose-Komponenten arbeiten im Evaluierungsmodus, wenn sie installiert sind. Der Evaluierungsmodus hat kein Zeitlimit und fügt nur Wasserzeichen in erstellte Dokumente ein.
1. Ein Projekt erstellen:
   1. Starten Sie Visual Studio.
   1. Erstellen Sie eine neue Konsolenanwendung.
      Dieses Beispiel zeigt eine C++-Konsolenanwendung.
1. Fügen Sie Verweise hinzu:
   1. Dieses Beispiel verwendet Aspose.Cells, fügen Sie daher einen Verweis auf diese Komponente im Projekt hinzu. Zum Beispiel:
      …\Program Files\Aspose\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dll
1. Schreiben Sie die Anwendung, die die API aufruft:

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
    U16String inputFilePath = srcDir + u"CustomerReport.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"PageSetup_out.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Setting the orientation to Portrait
    worksheet.GetPageSetup().SetOrientation(PageOrientationType::Portrait);

    // Setting the number of pages to which the length of the worksheet will be spanned
    worksheet.GetPageSetup().SetFitToPagesTall(1);

    // Setting the number of pages to which the width of the worksheet will be spanned
    worksheet.GetPageSetup().SetFitToPagesWide(1);

    // Setting the paper size to A4
    worksheet.GetPageSetup().SetPaperSize(PaperSizeType::PaperA4);

    // Setting the print quality of the worksheet to 1200 dpi
    worksheet.GetPageSetup().SetPrintQuality(1200);

    // Setting the first page number of the worksheet pages
    worksheet.GetPageSetup().SetFirstPageNumber(2);

    // Save the workbook
    workbook.Save(outputFilePath);

    std::cout << "Page setup applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Druckoptionen festlegen**

Die Seiteneinrichtungseinstellungen bieten auch mehrere Druckoptionen (auch Blattoptionen genannt), mit denen Benutzer steuern können, wie Arbeitsblattseiten gedruckt werden. Sie ermöglichen Benutzern:

- Eine bestimmte Druckbereich eines Arbeitsblatts auswählen.
- Titel drucken.
- Gitternetzlinien drucken.
- Zeilen-/Spaltenüberschriften drucken.
- Entwurfsqualität erreichen.
- Kommentare drucken.
- Zellenfehler drucken.
- Seiteneinteilung definieren.

Das folgende Beispiel wendet Druckoptionen auf die Datei an, die im obigen Beispiel erstellt wurde (PageSetup.xls). Der nachfolgende Screenshot zeigt die Standard-Druckoptionen, bevor neue Optionen angewendet werden.

|**Eingabedokument**|
| :- |
|![todo:image_alt_text](page-setup-and-printing-options_3.png)|
Das Ausführen des Codes ändert die Druckoptionen.

|**Ausgabedatei**|
| :- |
|![todo:image_alt_text](page-setup-and-printing-options_4.png)|

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
    U16String inputFilePath = srcDir + u"PageSetup.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"PageSetup_Print_out.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Get PageSetup object
    PageSetup pageSetup = worksheet.GetPageSetup();

    // Specifying the cells range (from A1 cell to E30 cell) of the print area
    pageSetup.SetPrintArea(u"A1:E30");

    // Defining column numbers A & E as title columns
    pageSetup.SetPrintTitleColumns(u"$A:$E");

    // Defining row numbers 1 as title rows
    pageSetup.SetPrintTitleRows(u"$1:$2");

    // Allowing to print gridlines
    pageSetup.SetPrintGridlines(true);

    // Allowing to print row/column headings
    pageSetup.SetPrintHeadings(true);

    // Allowing to print worksheet in black & white mode
    pageSetup.SetBlackAndWhite(true);

    // Allowing to print comments as displayed on worksheet
    pageSetup.SetPrintComments(PrintCommentsType::PrintInPlace);

    // Allowing to print worksheet with draft quality
    pageSetup.SetPrintDraft(true);

    // Allowing to print cell errors as N/A
    pageSetup.SetPrintErrors(PrintErrorsType::PrintErrorsNA);

    // Setting the printing order of the pages to over then down
    pageSetup.SetOrder(PrintOrderType::OverThenDown);

    // Save the workbook
    workbook.Save(outputFilePath);

    std::cout << "Page setup applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
