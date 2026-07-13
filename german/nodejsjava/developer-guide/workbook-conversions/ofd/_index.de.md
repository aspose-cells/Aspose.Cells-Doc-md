---
title: Konvertieren von Excel in das OFD-Format
linktitle: Konvertieren von Excel in das OFD-Format
description: Aspose.Cells for Node.js via Java ist eine Tabellenkalkulationsbibliothek zum Arbeiten mit Tabellenkalkulationsdateien, die das Konvertieren von Excel-Arbeitsmappen in das OFD-Format (Open Fixed-layout Document) unterstützt. Dieser Artikel zeigt, wie Excel-Inhalte erstellt und als OFD exportiert werden sowie wie vorhandene Excel-Dateien mit Aspose.Cells in OFD konvertiert werden.
keywords: Aspose.Cells, Node.js via Java Bibliothek, Tabellenkalkulation, Excel zu OFD, OFD-Konvertierung, SaveFormat.Ofd, Fixed-Layout-Dokument, Arbeitsmappen-Export
type: docs
weight: 195
url: /de/nodejs-java/converting-excel-to-ofd-format/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells unterstützt die direkte Konvertierung von Excel-Arbeitsmappen in das OFD-Format (Open Fixed-layout Document) unter Verwendung des Enumerationswerts `SaveFormat.Ofd`. Das resultierende OFD-Dokument bewahrt das sichtbare Layout der Arbeitsmappe, den Inhalt, verbundene Zellen, Spaltenbreiten, Zeilenhöhen, Schriftarten, Farben, Rahmen und Zahlenformate. Dies macht Aspose.Cells geeignet für Archivierungs-, Druck-, regulatorische Einreichungs- und Behördenübermittlungs-Workflows, die eine Fixed-Layout-Ausgabe erfordern.

{{% /alert %}}
## **Einführung**
OFD (Open Fixed-layout Document) ist ein chinesischer nationaler Standard (GB/T 33190-2016) zur Darstellung digitaler Dokumente in einem festen, seitenbasierten Layout. Es erfüllt eine ähnliche Rolle wie PDF für Anwendungsfälle, in denen das visuelle Erscheinungsbild des Quelldokuments genau wie erstellt erhalten bleiben muss. OFD ist in der Volksrepublik China weit verbreitet für Behördenübermittlungen, regulatorische Einreichungen, elektronische Rechnungen und langfristige Archivierung.

Das Konvertieren von Excel-Arbeitsmappen in OFD ist eine häufige Anforderung in Szenarien, in denen Tabellenkalkulationsinhalte als schreibgeschütztes, layoutfixiertes Artefakt verteilt werden müssen, anstatt als bearbeitbare Tabellenkalkulation. Beispiele umfassen das Versenden einer finalisierten Rechnung an einen Kunden, das Archivieren eines Quartalsfinanzberichts oder das Einreichen einer Budgettabelle bei einer Aufsichtsbehörde. Aspose.Cells erfüllt diese Anforderung durch den Enumerationswert `SaveFormat.Ofd`, der die Arbeitsmappe direkt in OFD schreibt, ohne einen zwischengeschalteten Konvertierungsschritt zu erfordern. Die OFD-Ausgabe bewahrt Zellwerte, verbundene Bereiche, Schriftarten, Farben, Rahmen, Zahlenformate und Seitenlayoutoptionen, die in der Arbeitsmappe konfiguriert sind.

{{% alert color="primary" %}}

Die von Aspose.Cells erzeugte OFD-Ausgabe bewahrt das sichtbare Layout der Quellarbeitsmappe, einschließlich Zellinhalten, verbundenen Zellen, Spaltenbreiten und Zeilenhöhen. Zellformatierungen wie Schriftarten, Farben, Rahmen, Ausrichtung und Zahlenformate werden ebenfalls in der Fixed-Layout-Ausgabe dargestellt. Seitenlayoutoptionen, die im Arbeitsblatt konfiguriert sind, wie Papiergröße, Ausrichtung und Druckbereich, beeinflussen das Layout des resultierenden OFD-Dokuments.

{{% /alert %}}
## **Erstellen einer Excel-Arbeitsmappe und Speichern als OFD**
Aspose.Cells ermöglicht es Ihnen, eine Arbeitsmappe programmatisch zu erstellen, sie mit Daten zu füllen und sie dann unter Verwendung der Enumeration `SaveFormat.Ofd` direkt im OFD-Format zu speichern. Das folgende Beispiel erstellt eine Rechnung von Grund auf. Es fügt ein Firmenlogo, Kopfinformationen, einen Rechnungsempfängerbereich, Positionen und berechnete Summen hinzu und exportiert dann die Arbeitsmappe in ein OFD-Dokument.
### **Erstellen einer Rechnung mit einem Logo**
Das Beispiel konstruiert ein Rechnungsarbeitsblatt, indem es ein Logobild in den oberen linken Bereich einfügt, den Firmennamen und die Kontaktdaten ausfüllt, einen „INVOICE"-Titel über verbundene Zellen hinzufügt, die Rechnungsnummer und das Datum erfasst, den Rechnungsempfänger auflistet, eine Positionstabelle mit Beschreibung, Menge, Einzelpreis und Gesamtspalten aufbaut und die Zwischensumme, die Steuer und den Gesamtbetrag mithilfe von Zellformeln berechnet. Formatierungen wie fettgedruckte Kopfzeilen, Währungsformat für Preise, Rahmen und Spaltenbreiten werden mit `Style`- und `Font`-Objekten angewendet. Schließlich wird die Arbeitsmappe mit der Erweiterung `.ofd` unter Verwendung von `SaveFormat.Ofd` gespeichert.

```javascript
let dataDir = "C:\\Temp\\";

// Eine neue Arbeitsmappe erstellen
let workbook = new AsposeCells.Workbook();

// Das erste Arbeitsblatt abrufen
let worksheet = workbook.getWorksheets().get(0);

// Spaltenbreiten festlegen
worksheet.getCells().setColumnWidth(0, 5);
worksheet.getCells().setColumnWidth(1, 35);
worksheet.getCells().setColumnWidth(2, 12);
worksheet.getCells().setColumnWidth(3, 15);
worksheet.getCells().setColumnWidth(4, 15);
worksheet.getCells().setColumnWidth(5, 5);

// Firmenlogo einfügen
worksheet.getPictures().add(1, 1, dataDir + "logo.png");

// Firmenname und Kontaktdaten
worksheet.getCells().get("B3").putValue("Acme Corporation");
worksheet.getCells().get("B4").putValue("123 Business Street");
worksheet.getCells().get("B5").putValue("City, State 12345");
worksheet.getCells().get("B6").putValue("Phone: (555) 123-4567");

// RECHNUNG Titel - Zellen verbinden
worksheet.getCells().merge(7, 1, 2, 4);
let titleCell = worksheet.getCells().get("B8");
titleCell.putValue("INVOICE");

let titleStyle = workbook.createStyle();
titleStyle.getFont().setIsBold(true);
titleStyle.getFont().setSize(20);
titleStyle.setHorizontalAlignment(AsposeCells.TextAlignmentType.CENTER);
titleCell.setStyle(titleStyle);

// Rechnungsnummer und Datum
worksheet.getCells().get("B11").putValue("Invoice Number:");
worksheet.getCells().get("C11").putValue("INV-2024-001");
worksheet.getCells().get("B12").putValue("Date:");
worksheet.getCells().get("C12").putValue(new Date().toISOString().slice(0, 10));

// Rechnungsempfänger-Abschnitt
worksheet.getCells().get("B14").putValue("Bill To:");
worksheet.getCells().get("B15").putValue("Client Name");
worksheet.getCells().get("B16").putValue("Client Address");
worksheet.getCells().get("B17").putValue("Client City, State");

// Kopfzeile der Positionen
let headerDesc = worksheet.getCells().get("B19");
let headerQty = worksheet.getCells().get("C19");
let headerPrice = worksheet.getCells().get("D19");
let headerTotal = worksheet.getCells().get("E19");

headerDesc.putValue("Description");
headerQty.putValue("Quantity");
headerPrice.putValue("Unit Price");
headerTotal.putValue("Total");

let headerStyle = workbook.createStyle();
headerStyle.getFont().setIsBold(true);
headerStyle.getFont().setColor(AsposeCells.Color.getWhite());
headerStyle.setBackgroundColor(AsposeCells.Color.getNavy());
headerStyle.setHorizontalAlignment(AsposeCells.TextAlignmentType.CENTER);
headerStyle.getBorders().get(AsposeCells.BorderType.TOP_BORDER).setLineStyle(AsposeCells.CellBorderType.THIN);
headerStyle.getBorders().get(AsposeCells.BorderType.BOTTOM_BORDER).setLineStyle(AsposeCells.CellBorderType.THIN);
headerStyle.getBorders().get(AsposeCells.BorderType.LEFT_BORDER).setLineStyle(AsposeCells.CellBorderType.THIN);
headerStyle.getBorders().get(AsposeCells.BorderType.RIGHT_BORDER).setLineStyle(AsposeCells.CellBorderType.THIN);

headerDesc.setStyle(headerStyle);
headerQty.setStyle(headerStyle);
headerPrice.setStyle(headerStyle);
headerTotal.setStyle(headerStyle);

// Währungsstil mit Rahmen
let currencyStyle = workbook.createStyle();
currencyStyle.setCustom("\"$\"#,##0.00");
currencyStyle.getBorders().get(AsposeCells.BorderType.TOP_BORDER).setLineStyle(AsposeCells.CellBorderType.THIN);
currencyStyle.getBorders().get(AsposeCells.BorderType.BOTTOM_BORDER).setLineStyle(AsposeCells.CellBorderType.THIN);
currencyStyle.getBorders().get(AsposeCells.BorderType.LEFT_BORDER).setLineStyle(AsposeCells.CellBorderType.THIN);
currencyStyle.getBorders().get(AsposeCells.BorderType.RIGHT_BORDER).setLineStyle(AsposeCells.CellBorderType.THIN);

// Einfacher Rahmenstil für Beschreibungs-/Mengenzellen
let borderStyle = workbook.createStyle();
borderStyle.getBorders().get(AsposeCells.BorderType.TOP_BORDER).setLineStyle(AsposeCells.CellBorderType.THIN);
borderStyle.getBorders().get(AsposeCells.BorderType.BOTTOM_BORDER).setLineStyle(AsposeCells.CellBorderType.THIN);
borderStyle.getBorders().get(AsposeCells.BorderType.LEFT_BORDER).setLineStyle(AsposeCells.CellBorderType.THIN);
borderStyle.getBorders().get(AsposeCells.BorderType.RIGHT_BORDER).setLineStyle(AsposeCells.CellBorderType.THIN);

// Zeilen mit Positionen
let lineItems = [
    ["Product A - Widget", 2, 50.00],
    ["Product B - Gadget", 3, 75.00],
    ["Product C - Service", 1, 100.00]
];

for (let i = 0; i < lineItems.length; i++)
{
    let row = 20 + i;
    let descCell = worksheet.getCells().get(row, 1);
    let qtyCell = worksheet.getCells().get(row, 2);
    let priceCell = worksheet.getCells().get(row, 3);
    let totalCell = worksheet.getCells().get(row, 4);

    descCell.putValue(lineItems[i][0]);
    qtyCell.putValue(lineItems[i][1]);
    priceCell.putValue(lineItems[i][2]);
    totalCell.setFormula("C" + row + "*D" + row);

    descCell.setStyle(borderStyle);
    qtyCell.setStyle(borderStyle);
    priceCell.setStyle(currencyStyle);
    totalCell.setStyle(currencyStyle);
}

// Zwischensumme, Steuer, Gesamtsumme
worksheet.getCells().get("B24").putValue("Subtotal:");
let subtotalCell = worksheet.getCells().get("E24");
subtotalCell.setFormula("SUM(E20:E22)");

worksheet.getCells().get("B25").putValue("Tax (10%):");
let taxCell = worksheet.getCells().get("E25");
taxCell.setFormula("E24*0.1");

worksheet.getCells().get("B26").putValue("Grand Total:");
let grandTotalCell = worksheet.getCells().get("E26");
grandTotalCell.setFormula("E24+E25");

// Fett + Währungsstil für Gesamtwerte
let totalStyle = workbook.createStyle();
totalStyle.getFont().setIsBold(true);
totalStyle.setCustom("\"$\"#,##0.00");

subtotalCell.setStyle(totalStyle);
taxCell.setStyle(totalStyle);
grandTotalCell.setStyle(totalStyle);

// Fettstil für Gesamtbeschriftungen
let boldStyle = workbook.createStyle();
boldStyle.getFont().setIsBold(true);

worksheet.getCells().get("B24").setStyle(boldStyle);
worksheet.getCells().get("B25").setStyle(boldStyle);
worksheet.getCells().get("B26").setStyle(boldStyle);

// Die Arbeitsmappe als OFD-Datei speichern
workbook.save(dataDir + "Invoice.ofd", AsposeCells.SaveFormat.Ofd);
```
## **Konvertieren einer vorhandenen Excel-Datei in OFD**
Aspose.Cells kann auch eine vorhandene Excel-Arbeitsmappe von der Festplatte laden und sie direkt in das OFD-Format exportieren. Dies ist nützlich für Stapelkonvertierungs-Pipelines, Archivierungs-Workflows und Szenarien, in denen die Quellarbeitsmappe von einem anderen Tool erstellt wurde und nur als Fixed-Layout-Artefakt erneut ausgegeben werden muss. Das folgende Beispiel lädt eine vorhandene `.xlsx`-Arbeitsmappe, liest Daten aus ihren Zellen, wendet optionale Seitenlayout-Anpassungen an und speichert das Ergebnis als OFD-Dokument.

```javascript
const AsposeCells = require("aspose.cells");

const dataDir = "C:\\Examples\\";

// Vorhandene Excel-Arbeitsmappe von der Festplatte öffnen
const workbook = new AsposeCells.Workbook(dataDir + "SampleBook.xlsx");

// (1) Werte aus ausgewählten Zellen lesen und anzeigen, um zu bestätigen, dass die Datei geladen wurde
const firstSheet = workbook.getWorksheets().get(0);
console.log("First sheet name: " + firstSheet.getName());
console.log("Cell A1: " + firstSheet.getCells().get("A1").getStringValue());
console.log("Cell B1: " + firstSheet.getCells().get("B1").getStringValue());
console.log("Cell C1: " + firstSheet.getCells().get("C1").getStringValue());

// (2) Über die Worksheets-Sammlung iterieren, um verfügbare Blätter aufzulisten
console.log("\nAvailable worksheets:");
for (let i = 0; i < workbook.getWorksheets().getCount(); i++)
{
    const ws = workbook.getWorksheets().get(i);
    console.log("  [" + i + "] " + ws.getName());
}

// (3) Optional eine Zeitstempelzelle aktualisieren, um die Konvertierung widerzuspiegeln
firstSheet.getCells().get("A1").putValue("Converted on: " + formatDate(new Date()));

// Eine Zusammenfassungs-Kopfzeile oben im Datenblock einfügen
firstSheet.getCells().insertRow(0);
firstSheet.getCells().get("A1").putValue("Conversion Summary");
firstSheet.getCells().get("A2").putValue("Generated: " + formatDate(new Date()));

// (4) PageSetup-Eigenschaften auf dem Arbeitsblatt konfigurieren
const pageSetup = firstSheet.getPageSetup();
pageSetup.setOrientation(AsposeCells.PageOrientationType.Landscape);
pageSetup.setPaperSize(AsposeCells.PaperSizeType.PaperA4);
pageSetup.setFitToPagesTall(1);
pageSetup.setFitToPagesWide(1);

// (5) Optional den Druckbereich für die OFD-Ausgabe festlegen
const lastRow = firstSheet.getCells().getMaxDataRow();
const lastCol = firstSheet.getCells().getMaxDataColumn();
const lastColLetter = AsposeCells.CellsHelper.columnIndexToName(lastCol);
const printArea = "A1:" + lastColLetter + (lastRow + 1);
firstSheet.getPageSetup().setPrintArea(printArea);
console.log("\nPrint area set to: " + printArea);

// (6) Arbeitsmappe als OFD-Datei speichern
workbook.save(dataDir + "SampleBook.ofd", AsposeCells.SaveFormat.Ofd);
console.log("\nFile successfully converted to OFD format: " + dataDir + "SampleBook.ofd");

function formatDate(date) {
    const pad = (n) => n.toString().padStart(2, '0');
    return date.getFullYear() + "-" + pad(date.getMonth() + 1) + "-" + pad(date.getDate()) + " " + pad(date.getHours()) + ":" + pad(date.getMinutes()) + ":" + pad(date.getSeconds());
}
```

## **Verwandte Artikel**
- [Aufteilen von Excel-Dateien in mehrere Dateien](/cells/de/nodejs-java/splitting-excel-files-into-multiple-files/)
- [Einfügen eines Bildes in eine Zelle](/cells/de/nodejs-java/inserting-an-image-into-a-cell/)
- [Lesen und Schreiben von DBF-Dateien](/cells/de/nodejs-java/dbf/)
- [Konvertieren von Sparklines in Bilder und HTML in Aspose.Cells for Node.js via Java](/cells/de/nodejs-java/convert-sparkline-to-image-and-html/)
{{< app/cells/assistant language="javascript" >}}