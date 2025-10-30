---
title: Arbeitsblattansichten mit Node.js über C++
linktitle: Arbeitsblattansichten
type: docs
weight: 40
url: /de/nodejs-cpp/worksheet-views/
description: Dieser Artikel beschreibt, wie man Node.js und die Node.js API verwendet, um mit der Seitenumbruch Vorschau eines Excel Arbeitsbuchs und Arbeitsblättern zu interagieren. Arbeiten Sie mit geteilten, eingefrorenen Fenstern und Zoom Faktor.
---

## **Seitenwechselvorschau**

Alle Arbeitsblätter können in zwei Modi angezeigt werden:

- Normale Ansicht.
- Seitenwechselvorschau.

Normalansicht ist die Standardansicht eines Arbeitsblatts. Seitenumbruchvorschau ist eine Bearbeitungsansicht, die ein Arbeitsblatt so anzeigt, wie es gedruckt wird. Die Seitenumbruchvorschau zeigt, welche Daten auf jede Seite passen, sodass Sie den Druckbereich und die Seitenumbrüche anpassen können. Mit Aspose.Cells for Node.js via C++ können Entwickler den normalen Ansichtsmodus oder den Seitenumbruchvorschau-Modus aktivieren.

### **Steuerung der Ansichtsmodi**

Aspose.Cells bietet eine [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)-Klasse, die eine Microsoft Excel-Datei darstellt. Die [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)-Klasse enthält eine [**Workbook.getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--)-Sammlung, die den Zugriff auf jedes Arbeitsblatt in einer Excel-Datei ermöglicht.

Ein Arbeitsblatt wird durch die Klasse [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) dargestellt. Die Klasse [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) bietet eine Vielzahl von Eigenschaften und Methoden zum Verwalten von Arbeitsblättern. Um die Normal- oder Seitenumbruchvorschau zu aktivieren, verwenden Sie die Klasse [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) und die Eigenschaft [**Worksheet.isPageBreakPreview()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isPageBreakPreview--). [**Worksheet.isPageBreakPreview()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isPageBreakPreview--) ist eine boolesche Eigenschaft, die nur einen Wert von **true** oder **false** speichern kann.

#### **Normale Ansicht aktivieren**

Legen Sie ein Arbeitsblatt auf Normalansicht, indem Sie die Eigenschaft [**Worksheet.isPageBreakPreview()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isPageBreakPreview--) der Klasse [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) auf **false** setzen.

#### **Aktivieren der Seitenwechselvorschau**

Legen Sie ein Arbeitsblatt auf die Seitenumbruchvorschau, indem Sie die Eigenschaft [**Worksheet.isPageBreakPreview()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isPageBreakPreview--) der Klasse [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) auf **true** setzen. Dadurch wird das Arbeitsblatt von der Normalansicht zur Seitenumbruchvorschau gewechselt.

Im Folgenden finden Sie ein vollständiges Beispiel, das zeigt, wie die Eigenschaft [**Worksheet.isPageBreakPreview()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isPageBreakPreview--) verwendet wird, um den Seitenumbruchvorschau-Modus für das erste Arbeitsblatt einer Excel-Datei zu aktivieren.

Die Datei book1.xls wird durch Erstellen einer Instanz der Klasse [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) geöffnet. Die Ansicht wird für das erste Arbeitsblatt auf die Seitenumbruchvorschau umgeschaltet, indem die Eigenschaft [**Worksheet.isPageBreakPreview()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isPageBreakPreview--) auf **true** gesetzt wird. Die geänderte Datei wird als output.xls gespeichert.

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");


// Instantiating a Workbook object
// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(filePath);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Displaying the worksheet in page break preview
worksheet.setIsPageBreakPreview(true);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xls"));
```

## **Zoom-Faktor**

### **Verwendung von Microsoft Excel**

Microsoft Excel bietet eine Funktion, mit der Benutzer den Zoom- oder Skalierungsfaktor eines Arbeitsblatts festlegen können. Diese Funktion hilft Benutzern, die Arbeitsblattinhalte in kleineren oder größeren Ansichten zu sehen. Benutzer können den Zoom-Faktor auf beliebige Werte setzen.

### **Aspose.Cells & Zoomfaktor**

Aspose.Cells ermöglicht Entwicklern, den Zoomfaktor des Arbeitsblatts festzulegen.
Aspose.Cells bietet eine [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)-Klasse, die eine Microsoft Excel-Datei darstellt. Die [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)-Klasse enthält eine [**Workbook.getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--)-Sammlung, die den Zugriff auf jedes Arbeitsblatt in einer Excel-Datei ermöglicht.

Ein Arbeitsblatt wird durch die Klasse [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) dargestellt. Die Klasse [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) bietet eine Vielzahl von Eigenschaften und Methoden zum Verwalten von Arbeitsblättern. Um den Zoomfaktor eines Arbeitsblatts festzulegen, verwenden Sie die Eigenschaft [**Worksheet.getZoom()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getZoom--) der Klasse [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). Der Zoomfaktor wird durch Zuweisen eines numerischen (ganzzahligen) Werts zur Eigenschaft [**Worksheet.getZoom()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getZoom--) festgelegt.

Ein vollständiges Beispiel wird unten gezeigt, das demonstriert, wie die [**Worksheet.getZoom()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getZoom--)-Eigenschaft verwendet wird, um den Zoomfaktor des ersten Arbeitsblatts in der Excel-Datei einzustellen.

Die Datei book1.xls wird durch Erstellen einer Instanz der Klasse [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) geöffnet. Der Zoomfaktor für das erste Arbeitsblatt wird auf 75 eingestellt und die geänderte Datei wird als output.xls gespeichert.

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Instantiating a Workbook object
// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(filePath);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Setting the zoom factor of the worksheet to 75
worksheet.setZoom(75);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xls"));
```

## **Fenster fixieren**

### **Verwendung von Microsoft Excel**

Freeze panes ist eine Funktion von Microsoft Excel. Durch das Einfrieren von Fenstern können Sie auswählen, dass Daten beim Scrollen in einem Arbeitsblatt sichtbar bleiben.

### **Aspose.Cells & Einfrieren von Fenstern**

Aspose.Cells ermöglicht Entwicklern, das Einfrieren von Zeilen und Spalten in Arbeitsblättern zur Laufzeit anzuwenden.

Aspose.Cells bietet eine Klasse [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), die eine Microsoft Excel-Datei repräsentiert. Die Klasse [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) enthält eine [**Workbook.getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--)-Sammlung, die den Zugriff auf jedes Arbeitsblatt in einer Excel-Datei ermöglicht.

Ein Arbeitsblatt wird durch die [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)-Klasse dargestellt. Die [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)-Klasse bietet eine Vielzahl von Eigenschaften und Methoden zur Verwaltung von Arbeitsblättern. Um Freeze-Panes zu konfigurieren, rufen Sie die Methode [**Worksheet.freezePanes(number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#freezePanes-number-number-number-number-) der Worksheet-Klasse auf. Die [**Worksheet.freezePanes(number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#freezePanes-number-number-number-number-)-Methode nimmt die folgenden Parameter entgegen:

- **Zeile**, der Zeilenindex der Zelle, von der das Einfrieren startet.
- **Spalte**, der Spaltenindex der Zelle, von der das Einfrieren startet.
- **Eingefrorene Zeilen**, die Anzahl der sichtbaren Zeilen im oberen Bereich.
- **Gefrorene Spalten**, die Anzahl der sichtbaren Spalten im linken Bereich.

Die Datei book1.xls wird geöffnet, indem der Konstruktor der Klasse [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) aufgerufen wird, während sie instanziiert wird, und einige Zeilen und Spalten werden im ersten Arbeitsblatt eingefroren. Die modifizierte Datei wird als output.xls gespeichert.

Im folgenden wird ein vollständiges Beispiel gezeigt, das zeigt, wie die Methode [**Worksheet.freezePanes(number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#freezePanes-number-number-number-number-) zum Einfrieren von Zeilen und Spalten (beginnend ab C4, dargestellt durch die 4. Zeile und 3. Spalte, wobei Zeilen und Spalten ab dem Index 0 beginnen) des ersten Arbeitsblatts der Excel-Datei verwendet wird.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Creating a file stream containing the Excel file to be opened
const fs = require("fs");
const fstream = fs.readFileSync(filePath);

// Instantiating a Workbook object
// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(fstream);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Applying freeze panes settings
worksheet.freezePanes(3, 2, 3, 2);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xls"));

// The file stream will be automatically closed after saving
```

## **Geteilte Fenster**

Wenn Sie den Bildschirm teilen müssen, um zwei verschiedene Ansichten im selben Arbeitsblatt zu erhalten, verwenden Sie geteilte Fenster. Microsoft Excel bietet eine sehr praktische Funktion, die es Ihnen ermöglicht, mehr als eine Kopie Ihres Arbeitsblatts anzuzeigen und durch jede Ansicht Ihres Arbeitsblatts unabhängig zu scrollen: geteilte Fenster.

Die Panes arbeiten gleichzeitig. Wenn Sie eine Änderung in einer vornehmen, erscheint die Änderung gleichzeitig in der anderen. Aspose.Cells bietet die Funktion für geteilte Fenster für die Benutzer.

### **Anwenden und Entfernen von geteilten Fenstern**

#### **Teilen von Fenstern**

Aspose.Cells bietet eine Klasse, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), die eine Microsoft Excel-Datei repräsentiert. Die Klasse [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) bietet eine Vielzahl von Eigenschaften und Methoden zum Verwalten einer Excel-Datei. Um Split-Ansichten zu implementieren, verwenden Sie die [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)-Methode der Klasse. Verwenden Sie zum Entfernen der Split-Panes die [**Worksheet.split()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#split--)-Methode.

In dem Beispiel verwenden wir eine einfache Vorlagendatei, die geladen wird, und dann wird das Feature der aufgeteilten Bereiche auf eine Zelle im ersten Arbeitsblatt angewendet. Die aktualisierte Datei wird gespeichert.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xls");

// Instantiate a new workbook and Open a template file
const book = new AsposeCells.Workbook(filePath);

// Set the active cell
book.getWorksheets().get(0).setActiveCell("A20");

// Split the worksheet window
book.getWorksheets().get(0).split();

// Save the excel file
book.save(path.join(dataDir, "output.xls"));
```

Nach Ausführung des obigen Codes hat die generierte Datei eine Split-Ansicht.

#### **Panes entfernen**

Entfernen Sie geteilte Fenster mit der Methode [**Worksheet.removeSplit()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#removeSplit--).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xls");

// Instantiate a new workbook and Open a template file
const workbook = new AsposeCells.Workbook(filePath);

// Set the active cell
workbook.getWorksheets().get(0).setActiveCell("A20");

// Split the worksheet window
workbook.getWorksheets().get(0).removeSplit();

// Save the excel file
workbook.save(path.join(dataDir, "output.xls"));
```

## **Erweiterte Themen**
- [Ausblenden der Anzeige von Nullwerten im Arbeitsblatt](/cells/de/nodejs-cpp/hiding-the-display-of-zero-values-in-the-worksheet/)
- [Arbeitsblattregisterfarbe festlegen](/cells/de/nodejs-cpp/set-worksheet-tab-color/)
- [Gitternetzlinien und Zeilen- und Spaltenüberschriften anzeigen oder ausblenden](/cells/de/nodejs-cpp/show-and-hide-gridlines-and-row-column-headers/)
- [Zeilen, Spalten und Bildlaufleisten anzeigen oder ausblenden](/cells/de/nodejs-cpp/show-and-hide-rows-columns-and-scroll-bars/)
- [Arbeitsblätter und Registerkarten anzeigen oder ausblenden](/cells/de/nodejs-cpp/show-and-hide-worksheets-and-tabs/)
- [Formeln anstelle von Werten im Arbeitsblatt anzeigen](/cells/de/nodejs-cpp/show-formulas-instead-of-values-in-a-worksheet/)
- [Fehlerüberprüfungsoptionen verwenden](/cells/de/nodejs-cpp/use-error-checking-options/)

{{< app/cells/assistant language="nodejs-cpp" >}}
