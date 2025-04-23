---
title: So skalieren Sie ein Arbeitsblatt mit Node.js via C++
linktitle: So skalieren Sie ein Arbeitsblatt
type: docs
weight: 130
url: /de/nodejs-cpp/how-to-scale-a-worksheet/
description: Dieser Artikel zeigt Ihnen Code, der erklärt, wie man ein Arbeitsblatt mit Aspose.Cells for Node.js via C++ skaliert.
keywords: Node.js Arbeitsblatt skalieren, wie man ein Arbeitsblatt mit Node.js via C++ skaliert, Skalieren eines Arbeitsblatts in Node.js via C++.
---

## **Mögliche Verwendungsszenarien**
Das Skalieren eines Arbeitsblatts kann aus verschiedenen Gründen nützlich sein, abhängig vom Kontext, in dem Sie arbeiten. Hier sind einige häufige Gründe für das Skalieren eines Arbeitsblatts:
1. An Seite anpassen: Damit alle Inhalte auf eine einzelne Seite oder eine bestimmte Anzahl von Seiten passen, beim Drucken, um das Lesen und die Verwaltung zu erleichtern, ohne durch mehrere Seiten blättern zu müssen.

1. Präsentation: Damit das Arbeitsblatt ordentlicher und professioneller aussieht, insbesondere bei der Weitergabe in Meetings oder Berichten.

1. Lesbarkeit: Um die Textgröße und andere Elemente für eine bessere Lesbarkeit anzupassen, insbesondere für Personen, die Schwierigkeiten haben, kleinere Schriftarten zu lesen.

1. Raumausnutzung: Um die Nutzung des Raums auf einem Arbeitsblatt zu optimieren, damit kein unnötiger Leerraum entsteht und alle wichtigen Informationen sichtbar sind, ohne übermäßig zu scrollen.

1. Datenvisualisierung: Bei Diagrammen und Grafiken kann das Skalieren helfen, sie verständlicher zu machen, indem die Größe an den verfügbaren Platz angepasst wird.

1. Konsistenz: Um ein konsistentes Aussehen und Gefühl über mehrere Arbeitsblätter oder Dokumente hinweg zu bewahren, was in professionellen und Bildungskontexten besonders wichtig ist.

## **Wie man ein Arbeitsblatt in Excel skaliert**
Das Skalieren eines Arbeitsblatts in Excel kann dabei helfen, den Inhalt auf eine einzelne Seite oder eine bestimmte Anzahl von Seiten beim Drucken anzupassen. Hier sind die Schritte, um ein Arbeitsblatt zu skalieren:

1. Das Arbeitsblatt öffnen: Öffnen Sie das Excel-Arbeitsblatt, das Sie skalieren möchten.

1. Zum Reiter Seitenlayout gehen: Klicken Sie auf den Reiter Seitenlayout im Menüband.

1. Gruppierung zum Anpassen anpassen: Im Reiter Seitenlayout finden Sie die Gruppe Seitenanpassung. Hier können Sie die Skalierung einstellen. Breite: Hier legen Sie fest, wie viele Seiten breit das gedruckte Arbeitsblatt sein sollen. Höhe: Hier legen Sie fest, wie viele Seiten hoch das gedruckte Arbeitsblatt sein sollen. Skalierung: Hier können Sie auch einen benutzerdefinierten Prozentsatz einstellen.
<br>
<img src="1.png" width=60% />

1. Breite und Höhe anpassen: Stellen Sie Breite und Höhe auf die gewünschte Anzahl an Seiten ein. Beispiel: Beide auf 1 Seite setzen, wenn das Arbeitsblatt auf eine Seite passen soll.

1. Skalierungsprozentsatz anpassen (falls erforderlich): Wenn Sie eine bestimmte Skalierung in Prozent einstellen möchten, passen Sie das Scale-Feld an. Beispiel: 50 % macht alles halb so groß.


## **Wie man ein Arbeitsblatt mit Node.js via C++ skaliert**
Aspose.Cells for Node.js via C++ ist eine leistungsstarke Bibliothek für die programmgesteuerte Arbeit mit Excel-Dateien. Um ein Arbeitsblatt mit Aspose.Cells zu skalieren, folgen Sie diesen Schritten: Laden Sie die [Beispieldatei](sample.xlsx) und passen Sie die Druckeinstellungen an, damit der Inhalt auf die gewünschte Seitenzahl oder einen bestimmten Prozentsatz der Originalgröße passt.

### **Beispiel: Auf Seite anpassen**
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Load the Excel file
const workbook = new AsposeCells.Workbook(filePath);

// Access the first worksheet
const sheet = workbook.getWorksheets().get(0);

// Access the PageSetup object
const pageSetup = sheet.getPageSetup();

// Set the worksheet to fit to 1 page wide and 1 page tall
pageSetup.setFitToPagesWide(1);
pageSetup.setFitToPagesTall(1);

// Save the modified workbook
workbook.save("output_fit_to_page.xlsx");
```
<br>
<img src="3.png" width=60% />

### **Beispiel: Skalierung in Prozent**
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Load the Excel file
const workbook = new AsposeCells.Workbook(filePath);

// Access the first worksheet
const sheet = workbook.getWorksheets().get(0);

// Access the PageSetup object
const pageSetup = sheet.getPageSetup();

// Set the scaling to a specific percentage (e.g., 75%)
pageSetup.setZoom(75);

// Save the modified workbook
workbook.save("output_scaled_percentage.xlsx");
```
<br>
<img src="2.png" width=60% />
