---
title: Seitenlayout Funktionen mit C++
linktitle: Seiteneinrichtungsfunktionen
type: docs
weight: 60
url: /de/cpp/page-setup-features/
description: Erfahren Sie, wie Sie die Seiteneinrichtungsfunktionen in Excel Dateien mit Aspose.Cells und C++ konfigurieren.
---

## **Seiteneinrichtungsfunktionen**

Aspose.Cells bietet eine umfassende Reihe von Funktionen zur Konfiguration der Seiteneinrichtung von Excel-Dateien. Diese Funktionen ermöglichen es Ihnen, verschiedene Aspekte des Seitenlayouts zu steuern, wie Ränder, Ausrichtung, Papiergröße und mehr.

### **Seitenränder einstellen**

Sie können die Seitenränder für ein Arbeitsblatt mit der Klasse `PageSetup` einstellen. Das folgende Beispiel zeigt, wie man die oberen, unteren, linken und rechten Ränder festlegt:

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPageMargins() {
    // Create a new workbook
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Set page margins
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetTopMargin(1.0);
    pageSetup.SetBottomMargin(1.0);
    pageSetup.SetLeftMargin(0.75);
    pageSetup.SetRightMargin(0.75);

    // Save the workbook
    workbook.Save("PageMargins.xlsx");
}
```

### **Seitenorientierung einstellen**

Sie können die Seitenorientierung entweder auf Hochformat oder Querformat mit der Klasse `PageSetup` einstellen. Das folgende Beispiel zeigt, wie man die Seitenorientierung auf Querformat setzt:

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPageOrientation() {
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetOrientation(PageOrientationType::Landscape);
    workbook.Save("PageOrientation.xlsx");
}
```

### **Papiergröße einstellen**

Sie können die Papiergröße für den Druck mit der Klasse `PageSetup` einstellen. Das folgende Beispiel zeigt, wie man die Papiergröße auf A4 setzt:

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPaperSize() {
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetPaperSize(PaperSizeType::PaperA4);
    workbook.Save("PaperSize.xlsx");
}
```

### **Druckbereich festlegen**

Sie können einen bestimmten Zellbereich zum Drucken mit der Klasse `PageSetup` definieren. Das folgende Beispiel zeigt, wie man den Druckbereich festlegt:

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPrintArea() {
    // Create a new workbook
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Set print area
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetPrintArea("A1:D10");

    // Save the workbook
    workbook.Save("PrintArea.xlsx");
}
```

### **Seitenumbrüche einstellen**

Sie können Seitenumbrüche in einem Arbeitsblatt einfügen, um zu steuern, wo die Seiten enden und neue beginnen. Das folgende Beispiel zeigt, wie man einen horizontalen Seitenumbruch einfügt:

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPageBreaks() {
    // Create a new workbook
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Insert a horizontal page break at row 10
    worksheet.GetHorizontalPageBreaks().Add("A10");

    // Save the workbook
    workbook.Save("PageBreaks.xlsx");
}
```

### **Kopf- und Fußzeile einstellen**

Sie können die Kopf- und Fußzeile eines Arbeitsblatts mit der Klasse `PageSetup` anpassen. Das folgende Beispiel zeigt, wie man eine benutzerdefinierte Kopf- und Fußzeile festlegt:

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetHeaderFooter() {
    // Create a new workbook
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Set custom header and footer
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetHeader(0, "&CHeader Text");
    pageSetup.SetFooter(0, "&CFooter Text");

    // Save the workbook
    workbook.Save("HeaderFooter.xlsx");
}
```

### **Drucktitel einstellen**

Sie können Zeilen oder Spalten festlegen, die bei jedem Druckvorgang oben oder links wiederholt werden sollen, mit der Klasse `PageSetup`. Das folgende Beispiel zeigt, wie man Drucktitel einstellt:

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPrintTitles() {
    // Create a new workbook
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Set print titles
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetPrintTitleRows("$1:$1");
    pageSetup.SetPrintTitleColumns("$A:$A");

    // Save the workbook
    workbook.Save("PrintTitles.xlsx");
}
```

### **Druckqualität einstellen**

Sie können die Druckqualität für ein Arbeitsblatt mit der Klasse `PageSetup` festlegen. Das folgende Beispiel zeigt, wie man die Druckqualität einstellt:

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPrintQuality() {
    // Create a new workbook
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Set print quality
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetPrintQuality(600);

    // Save the workbook
    workbook.Save("PrintQuality.xlsx");
}
```

### **Druckreihenfolge einstellen**

Sie können die Druckreihenfolge für ein Arbeitsblatt mit der Klasse `PageSetup` festlegen. Das folgende Beispiel zeigt, wie man die Druckreihenfolge auf "Über, dann Nach" setzt:

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPrintOrder() {
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetOrder(PrintOrderType::OverThenDown);
    workbook.Save("PrintOrder.xlsx");
}
```

### **Druckrasterlinien einstellen**

Sie können steuern, ob Rasterlinien mit der `PageSetup`-Klasse gedruckt werden. Das folgende Beispiel zeigt, wie der Druck von Rasterlinien aktiviert wird:

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPrintGridlines() {
    // Create a new workbook
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Enable printing of gridlines
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetPrintGridlines(true);

    // Save the workbook
    workbook.Save("PrintGridlines.xlsx");
}
```

### **Seitenüberschriften beim Drucken einstellen**

Sie können steuern, ob Zeilen- und Spaltenüberschriften mit der `PageSetup`-Klasse gedruckt werden. Das folgende Beispiel zeigt, wie der Druck von Überschriften aktiviert wird:

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPrintHeadings() {
    // Create a new workbook
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Enable printing of headings
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetPrintHeadings(true);

    // Save the workbook
    workbook.Save("PrintHeadings.xlsx");
}
```

### **Schwarz-Weiß-Druck einstellen**

Sie können steuern, ob das Arbeitsblatt mit der `PageSetup`-Klasse in Schwarz-Weiß gedruckt wird. Das folgende Beispiel zeigt, wie der Schwarz-Weiß-Druck aktiviert wird:

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPrintBlackAndWhite() {
    // Create a new workbook
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Enable black and white printing
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetBlackAndWhite(true);

    // Save the workbook
    workbook.Save("PrintBlackAndWhite.xlsx");
}
```

### **Druckentwurf einstellen**

Sie können steuern, ob das Arbeitsblatt in Entwurfsqualität gedruckt wird, mithilfe der `PageSetup`-Klasse. Das folgende Beispiel zeigt, wie der Druck in Entwurfsqualität aktiviert wird:

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPrintDraft() {
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetPrintDraft(true);
    workbook.Save("PrintDraft.xlsx");
}
```

### **Kommentare drucken einstellen**

Sie können steuern, ob Kommentare mit der `PageSetup`-Klasse gedruckt werden. Das folgende Beispiel zeigt, wie der Druck von Kommentaren aktiviert wird:

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPrintComments() {
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetPrintComments(PrintCommentsType::PrintInPlace);
    workbook.Save("PrintComments.xlsx");
}
```

### **Fehler drucken einstellen**

Sie können steuern, wie Fehler mit der `PageSetup`-Klasse gedruckt werden. Das folgende Beispiel zeigt, wie die Fehlerdruckoption festgelegt wird:

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPrintErrors() {
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetPrintErrors(PrintErrorsType::PrintErrorsBlank);
    workbook.Save("PrintErrors.xlsx");
}
```

### **Druckbereich auf Seitenanzahl anpassen**

Sie können steuern, ob der Druckbereich mithilfe der `PageSetup`-Klasse skaliert wird, um auf eine bestimmte Anzahl von Seiten zu passen. Das folgende Beispiel zeigt, wie der Druckbereich auf eine Seite breit und eine Seite hoch eingestellt wird:

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPrintAreaFitToPages() {
    // Create a new workbook
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Set print area to fit to one page wide and one page tall
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetFitToPagesWide(1);
    pageSetup.SetFitToPagesTall(1);

    // Save the workbook
    workbook.Save("PrintAreaFitToPages.xlsx");
}
```

### **Druckskalierung einstellen**

Sie können die Druckskalierung für ein Arbeitsblatt mit der `PageSetup`-Klasse festlegen. Das folgende Beispiel zeigt, wie die Druckskalierung auf 50% eingestellt wird:

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPrintScale() {
    // Create a new workbook
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Set print scale to 50%
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetZoom(50);

    // Save the workbook
    workbook.Save("PrintScale.xlsx");
}
```

### **Druckzentrum horizontal und vertikal einstellen**

Sie können steuern, ob das Arbeitsblatt mithilfe der `PageSetup`-Klasse horizontal und vertikal auf der gedruckten Seite zentriert wird. Das folgende Beispiel zeigt, wie das Arbeitsblatt horizontal und vertikal zentriert wird:

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPrintCenterHorizontallyAndVertically() {
    // Create a new workbook
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Center the worksheet horizontally and vertically
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetCenterHorizontally(true);
    pageSetup.SetCenterVertically(true);

    // Save the workbook
    workbook.Save("PrintCenterHorizontallyAndVertically.xlsx");
}
```

### **Erste Seitennummer festlegen**

Sie können die erste Seitennummer für den Druck mit der `PageSetup`-Klasse festlegen. Das folgende Beispiel zeigt, wie die erste Seitennummer eingestellt wird:

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPrintFirstPageNumber() {
    // Create a new workbook
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Set the first page number
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetFirstPageNumber(2);

    // Save the workbook
    workbook.Save("PrintFirstPageNumber.xlsx");
}
```

### **Seitenzahl drucken einstellen**

Sie können steuern, ob die Seitenzahl mit der `PageSetup`-Klasse gedruckt wird. Das folgende Beispiel zeigt, wie der Druck der Seitenzahl aktiviert wird:

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPrintPrintPageNumber() {
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetHeader(0, "&P");
    workbook.Save("PrintPageNumber.xlsx");
}
```

### **Seitenreihenfolge einstellen**

Sie können die Reihenfolge festlegen, in der die Seiten mit der `PageSetup`-Klasse gedruckt werden. Das folgende Beispiel zeigt, wie die Seitennummerierung auf "Runter, dann Über" eingestellt wird:

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPrintPageOrder() {
    // Create a new workbook
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Set the page order to "Down, then Over"
    PageSetup
{{< app/cells/assistant language="cpp" >}}
