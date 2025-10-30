---
title: Druckoptionen mit Node.js über C++ festlegen
linktitle: Druckoptionen festlegen
type: docs
weight: 40
url: /de/nodejs-cpp/setting-print-options/
description: Dieser Artikel zeigt, wie man die Druckoptionen der Excel Arbeitsblattseiten Setup Funktion programmgesteuert mit der Node.js API und der C++ Bibliothek festlegt. Sie können den Druckbereich, Drucktitel und Seitenreihenfolge einstellen.
keywords: Druckbereich in Excel mit Node.js über C++ festlegen, Drucktitel in Excel mit Node.js festlegen, Seitenreihenfolge in Excel mit Node.js festlegen
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

Aspose.Cells for Node.js via C++ unterstützt alle Druckoptionen, die von Microsoft Excel angeboten werden. Entwickler können diese Optionen für Arbeitsblätter einfach mit den Eigenschaften der [**PageSetup**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup)-Klasse konfigurieren. Wie diese Eigenschaften verwendet werden, wird nachfolgend im Detail erläutert.

### **Druckbereich festlegen**

Standardmäßig umfasst der Druckbereich alle Bereiche des Arbeitsblatts, die Daten enthalten. Entwickler können einen bestimmten Druckbereich des Arbeitsblatts festlegen.

Um einen spezifischen Druckbereich auszuwählen, verwenden Sie die Eigenschaft [**PageSetup.getPrintArea()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPrintArea--) der Klasse [**PageSetup**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup). Weisen Sie dieser Eigenschaft einen Zellenbereich zu, der den Druckbereich definiert.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Obtaining the reference of the PageSetup of the worksheet
const pageSetup = workbook.getWorksheets().get(0).getPageSetup();

// Specifying the cells range (from A1 cell to T35 cell) of the print area
pageSetup.setPrintArea("A1:T35");

// Save the workbook.
workbook.save(path.join(dataDir, "SetPrintArea_out.xls"));
```

### **Drucktitel festlegen**

Aspose.Cells ermöglicht es Ihnen, Zeilen- und Spaltenüberschriften auf allen Seiten eines gedruckten Arbeitsblatts zu wiederholen. Verwenden Sie dazu die Eigenschaften [**PageSetup.getPrintTitleColumns()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPrintTitleColumns--) und [**PageSetup.getPrintTitleRows()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPrintTitleRows--) der Klasse [**PageSetup**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup).

Die zu wiederholenden Zeilen oder Spalten werden durch Übergabe ihrer Zeilen- oder Spaltennummern definiert. Zum Beispiel werden Zeilen als $1:$2 und Spalten als $A:$B definiert.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Obtaining the reference of the PageSetup of the worksheet
const pageSetup = workbook.getWorksheets().get(0).getPageSetup();

// Defining column numbers A & B as title columns
pageSetup.setPrintTitleColumns("$A:$B");

// Defining row numbers 1 & 2 as title rows
pageSetup.setPrintTitleRows("$1:$2");

// Save the workbook.
workbook.save(path.join(dataDir, "SetPrintTitle_out.xls"));
```

### **Andere Druckoptionen festlegen**

Die Klasse [**PageSetup**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup) bietet auch mehrere andere Eigenschaften zur Festlegung allgemeiner Druckoptionen wie folgt:

- [**PageSetup.getPrintGridlines()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPrintGridlines--): eine boolesche Eigenschaft, die festlegt, ob Gitterlinien gedruckt werden sollen oder nicht.
- [**PageSetup.getPrintHeadings()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPrintHeadings--): eine boolesche Eigenschaft, die festlegt, ob Zeilen- und Spaltenüberschriften gedruckt werden sollen oder nicht.
- [**PageSetup.getBlackAndWhite()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getBlackAndWhite--): eine boolesche Eigenschaft, die festlegt, ob das Arbeitsblatt in Schwarz-Weiß-Modus gedruckt wird oder nicht.
- [**PageSetup.getPrintComments()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPrintComments--): legt fest, ob die Druckkommentare im Arbeitsblatt oder am Ende des Arbeitsblatts angezeigt werden sollen.
- [**PageSetup.getPrintDraft()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPrintDraft--): eine boolesche Eigenschaft, die festlegt, ob das Blatt ohne Grafiken gedruckt wird.
- [**PageSetup.getPrintErrors()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPrintErrors--): definiert, ob Zellfehler wie angezeigt, leer, Strich oder N/V gedruckt werden sollen.

Um die Eigenschaften [**PageSetup.getPrintComments()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPrintComments--) und [**PageSetup.getPrintErrors()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPrintErrors--) festzulegen, bietet Aspose.Cells for Node.js via C++ auch zwei Aufzählungen, [**PrintCommentsType**](https://reference.aspose.com/cells/nodejs-cpp/printcommentstype) und [**PrintErrorsType**](https://reference.aspose.com/cells/nodejs-cpp/printerrorstype), die vordefinierte Werte enthalten, die den Eigenschaften [**PageSetup.getPrintComments()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPrintComments--) und [**PageSetup.getPrintErrors()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPrintErrors--) zugewiesen werden sollen.

Die vordefinierten Werte der [**PrintCommentsType**](https://reference.aspose.com/cells/nodejs-cpp/printcommentstype)-Aufzählung sind nachfolgend mit ihren Beschreibungen aufgelistet.

|**Druckkommentartypen**|**Beschreibung**|
| :- | :- |
|PrintInPlace| Gibt an, Kommentare so zu drucken, wie sie auf dem Arbeitsblatt angezeigt werden.|
|PrintNoComments| Gibt an, Kommentare nicht zu drucken.|
|PrintSheetEnd| Gibt an, Kommentare am Ende des Arbeitsblatts zu drucken.|

Die vordefinierten Werte der [**PrintErrorsType**](https://reference.aspose.com/cells/nodejs-cpp/printerrorstype)-Aufzählung sind nachfolgend mit ihren Beschreibungen aufgelistet.

|**Druckfehlertypen**|**Beschreibung**|
| :- | :- |
|PrintErrorsBlank| Gibt an, Fehler nicht zu drucken.|
|PrintErrorsDash| Gibt an, Fehler als "--" zu drucken.|
|PrintErrorsDisplayed| Gibt an, Fehler wie angezeigt zu drucken.|
|PrintErrorsNA| Gibt an, Fehler als "#N/A" zu drucken.|

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Obtaining the reference of the PageSetup of the worksheet
const pageSetup = workbook.getWorksheets().get(0).getPageSetup();

// Allowing to print gridlines
pageSetup.setPrintGridlines(true);

// Allowing to print row/column headings
pageSetup.setPrintHeadings(true);

// Allowing to print worksheet in black & white mode
pageSetup.setBlackAndWhite(true);

// Allowing to print comments as displayed on worksheet
pageSetup.setPrintComments(AsposeCells.PrintCommentsType.PrintInPlace);

// Allowing to print worksheet with draft quality
pageSetup.setPrintDraft(true);

// Allowing to print cell errors as N/A
pageSetup.setPrintErrors(AsposeCells.PrintErrorsType.PrintErrorsNA);

// Save the workbook.
workbook.save(path.join(dataDir, "OtherPrintOptions_out.xls"));
```

### **Seitenreihenfolge festlegen**

Die [**PageSetup**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup)-Klasse stellt die [**PageSetup.getOrder()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getOrder--)-Eigenschaft bereit, mit der mehrere Seiten Ihres Arbeitsblatts zum Drucken geordnet werden können. Es gibt zwei Möglichkeiten, die Seiten zu ordnen, wie folgt.

- **Zuerst nach unten:** druckt alle Seiten nach unten, bevor Seiten rechts gedruckt werden.
- **Zuerst nach rechts:** druckt Seiten von links nach rechts, bevor die Seiten unterhalb gedruckt werden.

Aspose.Cells stellt eine Aufzählung [**PrintOrderType**](https://reference.aspose.com/cells/nodejs-cpp/printordertype) bereit, die alle vordefinierten Ordnungstypen enthält.

Die vordefinierten Werte der [**PrintOrderType**](https://reference.aspose.com/cells/nodejs-cpp/printordertype)-Aufzählung sind nachfolgend aufgelistet.

|**Druckreihenfolgetypen**|**Beschreibung**|
| :- | :- |
|DownThenOver|Stellt die Druckreihenfolge als zuerst nach unten und dann nach rechts dar.
|OverThenDown|Stellt die Druckreihenfolge als über dann nach unten dar.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Obtaining the reference of the PageSetup of the worksheet
const pageSetup = workbook.getWorksheets().get(0).getPageSetup();

// Setting the printing order of the pages to over then down
pageSetup.setOrder(AsposeCells.PrintOrderType.OverThenDown);

// Save the workbook.
workbook.save(path.join(dataDir, "SetPageOrder_out.xls"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
