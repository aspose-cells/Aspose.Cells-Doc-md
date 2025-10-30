---
title: Wie man Excel als Anpassbare Seitenbreiten und höhen mit Node.js über C++ druckt
linktitle: Wie drucke ich Excel auf zugeschnittenen Seiten breit und hoch
type: docs
weight: 200
url: /de/nodejs-cpp/how-to-print-excel-as-fitted-pages-wide-and-tall/
description: Dieser Artikel zeigt Ihnen Code, der erklärt, wie man FitToPagesWide und FitToPagesTall mit Aspose.Cells for Node.js via C++ einstellt.
keywords: Node.js über C++ wie man FitToPagesWide und FitToPagesTall festlegt, wie man FitToPagesWide und FitToPagesTall in Node.js hinzufügt, wie man FitToPagesWide und FitToPagesTall in Excel festlegt, wie man FitToPagesWide und FitToPagesTall in Excel löscht, wie man Excel als passende Seitenbreiten und höhen druckt, wie man Arbeitsblatt auf eine Seite druckt, wie man alle Spalten des Arbeitsblatts auf einer Seite druckt.
---

## **Einführung**

Die Einstellungen FitToPagesWide und FitToPagesTall werden in Tabellenkalkulationsanwendungen (wie Microsoft Excel) verwendet, um die Skalierung eines Tabellenblatts beim Drucken zu steuern. Diese Einstellungen helfen sicherzustellen, dass Ihre gedruckte Ausgabe innerhalb einer festgelegten Anzahl von Seiten passt, sowohl horizontal als auch vertikal. Hier eine Aufschlüsselung: 

1. FitToPagesWide: Diese Einstellung gibt die Anzahl der Seiten an, in die die gedruckte Ausgabe horizontal passt. Zum Beispiel bedeutet das Setzen von FitToPagesWide auf 1, dass der Inhalt auf die Breite einer Seite skaliert wird, egal wie breit das Tabellenblatt ist.
2. FitToPagesTall: Diese Einstellung gibt die Anzahl der Seiten an, die die gedruckte Ausgabe in der Höhe einpassen soll. Zum Beispiel bedeutet das Festlegen von FitToPagesTall auf 1, dass der Inhalt so skaliert wird, dass er in einer einzigen Seitengröße passt, unabhängig von der Anzahl der Zeilen.

## **Warum FitToPagesWide und FitToPagesTall verwenden**
Hier sind einige Gründe, warum Sie FitToPagesWide und FitToPagesTall einstellen sollten:
1. Kontrolle über das gedruckte Layout: Durch die Angabe der Anzahl der Seiten in der Breite und Höhe können Sie sicherstellen, dass Ihr gedrucktes Dokument leicht lesbar und gut organisiert ist, ohne dass Spalten oder Zeilen ungünstig auf mehrere Seiten aufgeteilt werden.
2. Konsistenz: Wenn Sie mehrere Blätter oder Berichte drucken, helfen diese Einstellungen, ein einheitliches Format beizubehalten, wodurch der Vergleich und die Analyse gedruckter Dokumente erleichtert werden.
3. Professionelle Präsentation: Das richtige Skalieren und Anpassen des Inhalts auf eine bestimmte Seitenzahl kann zu einer professionelleren und polierten Präsentation Ihrer Daten führen.

## **So drucken Sie eine Datei als angepasste Seiten breit und hoch in Excel**

Um die Einstellungen FitToPagesWide und FitToPagesTall in Microsoft Excel festzulegen, befolgen Sie diese Schritte:

1. Öffnen Sie Ihre Excel-Arbeitsmappe und wechseln Sie auf das Blatt, das Sie drucken möchten.
2. Gehen Sie auf die Registerkarte Seitenlayout im Ribbon.
3. Klicken Sie in der Gruppe Seitenlayout auf den kleinen Pfeil in der unteren rechten Ecke, um das Dialogfeld Seite einrichten zu öffnen.
4. Gehen Sie im Dialogfeld Seite einrichten zur Registerkarte Seite.
5. Unter Skalierung wählen Sie die Option "Anpassen an" und geben dann die Anzahl der Seiten in der Breite und Höhe an, die Sie möchten: Geben Sie die gewünschte Anzahl der Seiten in der ersten Box ein (Anpassen an x Seiten breit). Geben Sie die gewünschte Anzahl der Seiten in der zweiten Box ein (Anpassen an y Seiten hoch).
<br>
<img src="2.png" width=60% />

6. Klicken Sie auf OK, um die Einstellungen anzuwenden.

## **So drucken Sie Excel als angepasste Seitenbreite und -höhe mit Aspose.Cells for Node.js via C++**

Um FitToPagesWide und FitToPagesTall in einem bestimmten Arbeitsblatt einzustellen: Laden Sie zuerst die [Beispieldatei](input.xlsx) und ändern Sie dann die Eigenschaften [**PageSetup.getFitToPagesTall()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getFitToPagesTall--) und [**PageSetup.getFitToPagesWide()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getFitToPagesWide--) des [**PageSetup**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/)-Objekts für das gewünschte Arbeitsblatt. Hier ist ein Beispiel in Node.js:

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "input.xlsx");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook(filePath);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Setting the number of pages to which the length of the worksheet will be spanned
worksheet.getPageSetup().setFitToPagesTall(1);

// Setting the number of pages to which the width of the worksheet will be spanned
worksheet.getPageSetup().setFitToPagesWide(1);

// Save the workbook
workbook.save("out_net.pdf");
```

Das Ausgabenergebnis:
<br>
<img src="1.png" width=60% />

## **So drucken Sie Arbeitsblatt als eine Seite mit Aspose.Cells for Node.js via C++**

Um ein Arbeitsblatt als eine Seite zu drucken: Laden Sie zuerst die [Beispieldatei](sample.xlsx), und setzen Sie dann die Eigenschaft [**PdfSaveOptions.getOnePagePerSheet()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getOnePagePerSheet--) des [**PdfSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/)-Objekts. Hier ist ein Beispiel in Node.js:

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

const options = new AsposeCells.PdfSaveOptions();
options.setOnePagePerSheet(true);

// Save the workbook.
workbook.save("OnePagePerSheet.pdf", options);
```

Das Ausgabenergebnis:
<br>
<img src="3.png" width=60% />

## **So drucken Sie alle Spalten eines Arbeitsblatts auf einer Seite mit Aspose.Cells for Node.js via C++**

Um alle Spalten eines Arbeitsblatts auf einer Seite zu drucken: Laden Sie die [Beispieldatei](sample.xlsx), und setzen Sie dann die Eigenschaft [**PdfSaveOptions.getAllColumnsInOnePagePerSheet()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getAllColumnsInOnePagePerSheet--) des [**PdfSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/)-Objekts. Hier ist ein Beispiel in Node.js:

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

const options = new AsposeCells.PdfSaveOptions();
options.setAllColumnsInOnePagePerSheet(true);

// Save the workbook.
workbook.save("AllColumnsInOnePagePerSheet.pdf", options);
```

Das Ausgabenergebnis:
<br>
<img src="4.png" width=60% />
{{< app/cells/assistant language="nodejs-cpp" >}}
