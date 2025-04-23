---
title: Druckoptionen mit C++ festlegen
linktitle: Druckoptionen festlegen
type: docs
weight: 40
url: /de/cpp/setting-print-options/
description: Dieser Artikel demonstriert, wie man die Druckoptionen der Excel Seitenaufbaueinstellungen programmgesteuert mit der C++ API und Bibliothek festlegt. Sie können den Druckbereich, die Drucktitel und die Seitenreihenfolge einstellen.
keywords: Druckbereich in Excel festlegen C++, Drucktitel in Excel festlegen C++, Seitenreihenfolge in Excel festlegen C++
---

{{% alert color="primary" %}}

Die Seiteneinrichtungseinstellungen von Microsoft Excel bieten mehrere Druckoptionen (auch als Bogenoptionen bezeichnet), mit denen Benutzer steuern können, wie Arbeitsblattseiten gedruckt werden.

{{% /alert %}}

## **Druckoptionen einstellen**

Diese Druckoptionen ermöglichen es Benutzern:

- Einen bestimmten Druckbereich auf einem Arbeitsblatt auswählen.
- Titel drucken.
- Gitternetzlinien drucken.
- Zeilen-/Spaltenüberschriften drucken.
- Entwurfsqualität erreichen.
- Kommentare drucken.
- Zellenfehler drucken.
- Seiteneinteilung definieren.

Aspose.Cells unterstützt alle Druckoptionen, die von Microsoft Excel angeboten werden, und Entwickler können diese Optionen für Arbeitsblätter ganz einfach mit den Eigenschaften der Klasse [**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/) konfigurieren. Wie diese Eigenschaften verwendet werden, wird im Folgenden ausführlich erläutert.

### **Druckbereich festlegen**

Standardmäßig umfasst der Druckbereich alle Bereiche des Arbeitsblatts, die Daten enthalten. Entwickler können einen bestimmten Druckbereich des Arbeitsblatts festlegen.

Verwenden Sie zum Auswählen eines bestimmten Druckbereichs die [**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/)-Klasse' [**GetPrintArea()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getprintarea/)-Eigenschaft. Weisen Sie dieser Eigenschaft einen Zellenbereich zu, der den Druckbereich definiert.

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

    // Create a new workbook
    Workbook workbook;

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Get the PageSetup object of the worksheet
    PageSetup pageSetup = worksheet.GetPageSetup();

    // Set the print area to the range A1:T35
    pageSetup.SetPrintArea(u"A1:T35");

    // Save the workbook
    workbook.Save(outDir + u"SetPrintArea_out.xls");

    std::cout << "Print area set successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Drucktitel festlegen**

Aspose.Cells ermöglicht es Ihnen, Zeilen- und Spaltenüberschriften auf allen Seiten eines gedruckten Arbeitsblatts zu wiederholen. Verwenden Sie dazu die [**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/)-Klasse' [**GetPrintTitleColumns()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getprinttitlecolumns/)- und [**GetPrintTitleRows()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getprinttitlerows/)-Eigenschaften.

Die zu wiederholenden Zeilen oder Spalten werden durch Übergabe ihrer Zeilen- oder Spaltennummern definiert. Zum Beispiel werden Zeilen als $1:$2 und Spalten als $A:$B definiert.

```c++
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

    // Path of output excel file
    U16String outputFilePath = outDir + u"SetPrintTitle_out.xls";

    // Create a new workbook
    Workbook workbook;

    // Obtain the reference of the PageSetup of the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    PageSetup pageSetup = worksheet.GetPageSetup();

    // Define column numbers A & B as title columns
    pageSetup.SetPrintTitleColumns(u"$A:$B");

    // Define row numbers 1 & 2 as title rows
    pageSetup.SetPrintTitleRows(u"$1:$2");

    // Save the workbook
    workbook.Save(outputFilePath);

    std::cout << "Print titles set successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **Andere Druckoptionen festlegen**

Die [**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/)-Klasse bietet auch mehrere andere Eigenschaften zur Festlegung allgemeiner Druckoptionen wie folgt:

- [**GetPrintGridlines()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getprintgridlines/): eine boolesche Eigenschaft, die bestimmt, ob Gitterlinien gedruckt werden sollen oder nicht.
- [**GetPrintHeadings()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getprintheadings/): ein Boolescher Wert, der definiert, ob Zeilen- und Spaltenüberschriften gedruckt werden oder nicht.
- [**GetBlackAndWhite()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getblackandwhite/): Eine boolesche Eigenschaft, die definiert, ob das Arbeitsblatt im Schwarz-Weiß-Modus gedruckt werden soll oder nicht.
- [**GetPrintComments()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getprintcomments/): definiert, ob die Druckkommentare auf dem Arbeitsblatt oder am Ende des Arbeitsblatts angezeigt werden sollen.
- [**GetPrintDraft()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getprintdraft/): eine boolesche Eigenschaft, die bestimmt, ob das Blatt ohne Grafiken gedruckt wird.
- [**GetPrintErrors()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getprinterrors/): bestimmt, ob Zellfehler angezeigt, leer, mit Bindestrich oder N/A gedruckt werden.

Um die Eigenschaften [**GetPrintComments()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getprintcomments/) und [**GetPrintErrors()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getprinterrors/) festzulegen, stellt Aspose.Cells auch zwei Enumerationstypen [**PrintCommentsType**](https://reference.aspose.com/cells/cpp/aspose.cells/printcommentstype/) und [**PrintErrorsType**](https://reference.aspose.com/cells/cpp/aspose.cells/printerrorstype/) bereit, die vordefinierte Werte enthalten, die den Eigenschaften [**GetPrintComments()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getprintcomments/) und [**GetPrintErrors()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getprinterrors/) zugewiesen werden.

Die vordefinierten Werte in der [**PrintCommentsType**](https://reference.aspose.com/cells/cpp/aspose.cells/printcommentstype/) Aufzählung sind unten mit ihren Beschreibungen aufgelistet.

|**Druckkommentartypen**|**Beschreibung**|
| :- | :- |
|PrintInPlace| Gibt an, Kommentare so zu drucken, wie sie auf dem Arbeitsblatt angezeigt werden.|
|PrintNoComments| Gibt an, Kommentare nicht zu drucken.|
|PrintSheetEnd| Gibt an, Kommentare am Ende des Arbeitsblatts zu drucken.|

Die vordefinierten Werte der [**PrintErrorsType**](https://reference.aspose.com/cells/cpp/aspose.cells/printerrorstype/) Aufzählung sind unten mit ihren Beschreibungen aufgelistet.

|**Druckfehlertypen**|**Beschreibung**|
| :- | :- |
|PrintErrorsBlank| Gibt an, Fehler nicht zu drucken.|
|PrintErrorsDash| Gibt an, Fehler als "--" zu drucken.|
|PrintErrorsDisplayed| Gibt an, Fehler wie angezeigt zu drucken.|
|PrintErrorsNA| Gibt an, Fehler als "#N/A" zu drucken.|

```c++
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

    // Create a new workbook
    Workbook workbook;

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Get the PageSetup object of the worksheet
    PageSetup pageSetup = worksheet.GetPageSetup();

    // Set print options
    pageSetup.SetPrintGridlines(true);  // Allow printing gridlines
    pageSetup.SetPrintHeadings(true);   // Allow printing row/column headings
    pageSetup.SetBlackAndWhite(true);   // Allow printing in black & white mode
    pageSetup.SetPrintComments(PrintCommentsType::PrintInPlace);  // Print comments as displayed
    pageSetup.SetPrintDraft(true);      // Print with draft quality
    pageSetup.SetPrintErrors(PrintErrorsType::PrintErrorsNA);  // Print cell errors as N/A

    // Save the workbook
    U16String outputPath = outDir + u"OtherPrintOptions_out.xls";
    workbook.Save(outputPath);

    std::cout << "Workbook saved with print options successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Seitenreihenfolge festlegen**

Die [**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/) Klasse bietet die [**GetOrder()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getorder/) Eigenschaft, die verwendet wird, um die Reihenfolge mehrerer Seiten Ihres Arbeitsblatts zum Drucken festzulegen. Es gibt zwei Möglichkeiten, die Seiten wie folgt anzuordnen.

- **Zuerst nach unten:** druckt alle Seiten nach unten, bevor Seiten rechts gedruckt werden.
- **Zuerst nach rechts:** druckt Seiten von links nach rechts, bevor die Seiten unterhalb gedruckt werden.

Aspose.Cells bietet eine Aufzählung, [**PrintOrderType**](https://reference.aspose.com/cells/cpp/aspose.cells/printordertype/), die alle vordefinierten Anordnungstypen enthält.

Die vordefinierten Werte der [**PrintOrderType**](https://reference.aspose.com/cells/cpp/aspose.cells/printordertype/) Aufzählung sind unten aufgeführt.

|**Druckreihenfolgetypen**|**Beschreibung**|
| :- | :- |
|DownThenOver|Stellt die Druckreihenfolge als zuerst nach unten und dann nach rechts dar.
|OverThenDown|Stellt die Druckreihenfolge als über dann nach unten dar.

```c++
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

    // Create a new workbook
    Workbook workbook;

    // Obtain the reference of the PageSetup of the first worksheet
    PageSetup pageSetup = workbook.GetWorksheets().Get(0).GetPageSetup();

    // Set the printing order of the pages to over then down
    pageSetup.SetOrder(PrintOrderType::OverThenDown);

    // Save the workbook
    workbook.Save(outDir + u"SetPageOrder_out.xls");

    std::cout << "Page order set successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
