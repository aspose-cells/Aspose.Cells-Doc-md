---
title: Konvertieren von Excel in das OFD-Format
linktitle: Konvertieren von Excel in das OFD-Format
description: Aspose.Cells ist eine Java-Bibliothek zur Arbeit mit Tabellenkalkulationsdateien, die das Konvertieren von Excel-Arbeitsmappen in das OFD-Format (Open Fixed-layout Document) unterstützt. Dieser Artikel zeigt, wie Excel-Inhalte erstellt und als OFD exportiert werden sowie wie vorhandene Excel-Dateien mit Aspose.Cells in OFD konvertiert werden.
keywords: Aspose.Cells, Java-Bibliothek, Tabellenkalkulation, Excel zu OFD, OFD-Konvertierung, SaveFormat.Ofd, Fixed-Layout-Dokument, Arbeitsmappen-Export
type: docs
weight: 195
url: /de/java/converting-excel-to-ofd-format/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells unterstützt die direkte Konvertierung von Excel-Arbeitsmappen in das OFD-Format (Open Fixed-layout Document) mithilfe des Enumerationswerts `SaveFormat.Ofd`. Das resultierende OFD-Dokument bewahrt das sichtbare Layout der Arbeitsmappe, den Inhalt, verbundene Zellen, Spaltenbreiten, Zeilenhöhen, Schriftarten, Farben, Rahmen und Zahlenformate. Dadurch eignet sich Aspose.Cells für Archivierungs-, Druck-, regulatorische Einreichungs- und Behörden-Workflows, die eine Fixed-Layout-Ausgabe erfordern.

{{% /alert %}}
## **Einführung**
OFD (Open Fixed-layout Document) ist ein chinesischer nationaler Standard (GB/T 33190-2016) zur Darstellung digitaler Dokumente in einem festen, seitenbasierten Layout. Es erfüllt eine ähnliche Rolle wie PDF für Anwendungsfälle, in denen das visuelle Erscheinungsbild des Quelldokuments genau so erhalten bleiben muss, wie es erstellt wurde. OFD wird in der Volksrepublik China häufig für Behördeneinreichungen, regulatorische Meldungen, elektronische Rechnungen und langfristige Archivierung verwendet.

Die Konvertierung von Excel-Arbeitsmappen in OFD ist eine häufige Anforderung in Szenarien, in denen Tabellenkalkulationsinhalte als schreibgeschütztes, layoutfixiertes Artefakt verteilt werden müssen, anstatt als bearbeitbare Tabellenkalkulation. Beispiele hierfür sind der Versand einer finalisierten Rechnung an einen Kunden, die Archivierung eines Quartalsfinanzberichts oder die Einreichung einer Budgettabelle bei einer Aufsichtsbehörde. Aspose.Cells erfüllt diese Anforderung durch den Enumerationswert `SaveFormat.Ofd`, der die Arbeitsmappe direkt in OFD schreibt, ohne einen Zwischenschritt zur Konvertierung zu erfordern. Die OFD-Ausgabe bewahrt Zellwerte, verbundene Bereiche, Schriftarten, Farben, Rahmen, Zahlenformate und die auf der Arbeitsmappe konfigurierten Seiteneinrichtungsoptionen.

{{% alert color="primary" %}}

Die von Aspose.Cells erzeugte OFD-Ausgabe bewahrt das sichtbare Layout der Quellarbeitsmappe, einschließlich Zellinhalten, verbundenen Zellen, Spaltenbreiten und Zeilenhöhen. Zellformatierungen wie Schriftarten, Farben, Rahmen, Ausrichtung und Zahlenformate werden ebenfalls in der Fixed-Layout-Ausgabe dargestellt. Die auf dem Arbeitsblatt konfigurierten Seiteneinrichtungsoptionen wie Papierformat, Ausrichtung und Druckbereich beeinflussen das Layout des resultierenden OFD-Dokuments.

{{% /alert %}}
## **Erstellen einer Excel-Arbeitsmappe und Speichern als OFD**
Aspose.Cells ermöglicht es Ihnen, eine Arbeitsmappe programmatisch zu erstellen, mit Daten zu füllen und sie dann unter Verwendung der Enumeration `SaveFormat.Ofd` direkt im OFD-Format zu speichern. Das folgende Beispiel erstellt eine Rechnung von Grund auf. Es fügt ein Firmenlogo, Kopfinformationen, einen Rechnungsempfängerbereich, Positionszeilen und berechnete Summen hinzu und exportiert anschließend die Arbeitsmappe in ein OFD-Dokument.
### **Erstellen einer Rechnung mit einem Logo**
Das Beispiel erstellt ein Rechnungsarbeitsblatt, indem ein Logobild in den oberen linken Bereich eingefügt, der Firmenname und die Kontaktdaten eingetragen, ein „INVOICE"-Titel über verbundene Zellen hinzugefügt, die Rechnungsnummer und das Datum erfasst, der Rechnungsempfänger aufgelistet, eine Tabelle für Positionszeilen mit Beschreibung, Menge, Einzelpreis und Gesamtspalten erstellt und Zwischensumme, Steuer und Gesamtbetrag mithilfe von Zellformeln berechnet werden. Formatierungen wie fettgedruckte Kopfzeilen, Währungsformat für Preise, Rahmen und Spaltenbreiten werden mithilfe von `Style`- und `Font`-Objekten angewendet. Abschließend wird die Arbeitsmappe mit der Erweiterung `.ofd` unter Verwendung von `SaveFormat.Ofd` gespeichert.

```java
import com.aspose.cells.*;
import java.text.SimpleDateFormat;
import java.util.Date;

String dataDir = "C:\\Temp\\";

// Eine neue Arbeitsmappe erstellen
Workbook workbook = new Workbook();

// Das erste Arbeitsblatt abrufen
Worksheet worksheet = workbook.getWorksheets().get(0);

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

// RECHNUNG Titel - Zellen zusammenführen
worksheet.getCells().merge(7, 1, 2, 4);
Cell titleCell = worksheet.getCells().get("B8");
titleCell.putValue("INVOICE");

Style titleStyle = workbook.createStyle();
titleStyle.getFont().setBold(true);
titleStyle.getFont().setSize(20);
titleStyle.setHorizontalAlignment(TextAlignmentType.CENTER);
titleCell.setStyle(titleStyle);

// Rechnungsnummer und Datum
worksheet.getCells().get("B11").putValue("Invoice Number:");
worksheet.getCells().get("C11").putValue("INV-2024-001");
worksheet.getCells().get("B12").putValue("Date:");
worksheet.getCells().get("C12").putValue(new SimpleDateFormat("yyyy-MM-dd").format(new Date()));

// Rechnungsempfänger-Abschnitt
worksheet.getCells().get("B14").putValue("Bill To:");
worksheet.getCells().get("B15").putValue("Client Name");
worksheet.getCells().get("B16").putValue("Client Address");
worksheet.getCells().get("B17").putValue("Client City, State");

// Positionsüberschriften
Cell headerDesc = worksheet.getCells().get("B19");
Cell headerQty = worksheet.getCells().get("C19");
Cell headerPrice = worksheet.getCells().get("D19");
Cell headerTotal = worksheet.getCells().get("E19");

headerDesc.putValue("Description");
headerQty.putValue("Quantity");
headerPrice.putValue("Unit Price");
headerTotal.putValue("Total");

Style headerStyle = workbook.createStyle();
headerStyle.getFont().setBold(true);
headerStyle.getFont().setColor(Color.getWhite());
headerStyle.setBackgroundColor(Color.getNavy());
headerStyle.setHorizontalAlignment(TextAlignmentType.CENTER);
headerStyle.getBorders().getByBorderType(BorderType.TOP_BORDER).setLineStyle(CellBorderType.THIN);
headerStyle.getBorders().getByBorderType(BorderType.BOTTOM_BORDER).setLineStyle(CellBorderType.THIN);
headerStyle.getBorders().getByBorderType(BorderType.LEFT_BORDER).setLineStyle(CellBorderType.THIN);
headerStyle.getBorders().getByBorderType(BorderType.RIGHT_BORDER).setLineStyle(CellBorderType.THIN);

headerDesc.setStyle(headerStyle);
headerQty.setStyle(headerStyle);
headerPrice.setStyle(headerStyle);
headerTotal.setStyle(headerStyle);

// Währungsstil mit Rahmen
Style currencyStyle = workbook.createStyle();
currencyStyle.setCustom("\"$\"#,##0.00");
currencyStyle.getBorders().getByBorderType(BorderType.TOP_BORDER).setLineStyle(CellBorderType.THIN);
currencyStyle.getBorders().getByBorderType(BorderType.BOTTOM_BORDER).setLineStyle(CellBorderType.THIN);
currencyStyle.getBorders().getByBorderType(BorderType.LEFT_BORDER).setLineStyle(CellBorderType.THIN);
currencyStyle.getBorders().getByBorderType(BorderType.RIGHT_BORDER).setLineStyle(CellBorderType.THIN);

// Einfacher Rahmenstil für Beschreibungs-/Mengenzellen
Style borderStyle = workbook.createStyle();
borderStyle.getBorders().getByBorderType(BorderType.TOP_BORDER).setLineStyle(CellBorderType.THIN);
borderStyle.getBorders().getByBorderType(BorderType.BOTTOM_BORDER).setLineStyle(CellBorderType.THIN);
borderStyle.getBorders().getByBorderType(BorderType.LEFT_BORDER).setLineStyle(CellBorderType.THIN);
borderStyle.getBorders().getByBorderType(BorderType.RIGHT_BORDER).setLineStyle(CellBorderType.THIN);

// Positionszeilen
Object[][] lineItems = new Object[][] {
    {"Product A - Widget", 2, 50.00},
    {"Product B - Gadget", 3, 75.00},
    {"Product C - Service", 1, 100.00}
};

for (int i = 0; i < lineItems.length; i++)
{
    int row = 20 + i;
    Cell descCell = worksheet.getCells().get(row, 1);
    Cell qtyCell = worksheet.getCells().get(row, 2);
    Cell priceCell = worksheet.getCells().get(row, 3);
    Cell totalCell = worksheet.getCells().get(row, 4);

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
Cell subtotalCell = worksheet.getCells().get("E24");
subtotalCell.setFormula("SUM(E20:E22)");

worksheet.getCells().get("B25").putValue("Tax (10%):");
Cell taxCell = worksheet.getCells().get("E25");
taxCell.setFormula("E24*0.1");

worksheet.getCells().get("B26").putValue("Grand Total:");
Cell grandTotalCell = worksheet.getCells().get("E26");
grandTotalCell.setFormula("E24+E25");

// Fett + Währungsstil für Gesamtwerte
Style totalStyle = workbook.createStyle();
totalStyle.getFont().setBold(true);
totalStyle.setCustom("\"$\"#,##0.00");

subtotalCell.setStyle(totalStyle);
taxCell.setStyle(totalStyle);
grandTotalCell.setStyle(totalStyle);

// Fettstil für Gesamtbeschriftungen
Style boldStyle = workbook.createStyle();
boldStyle.getFont().setBold(true);

worksheet.getCells().get("B24").setStyle(boldStyle);
worksheet.getCells().get("B25").setStyle(boldStyle);
worksheet.getCells().get("B26").setStyle(boldStyle);

// Die Arbeitsmappe als OFD-Datei speichern
workbook.save(dataDir + "Invoice.ofd", SaveFormat.Ofd);
```
## **Konvertieren einer vorhandenen Excel-Datei in OFD**
Aspose.Cells kann auch eine vorhandene Excel-Arbeitsmappe von der Festplatte laden und sie direkt in das OFD-Format exportieren. Dies ist nützlich für Stapelkonvertierungspipelines, Archivierungsworkflows und Szenarien, in denen die Quellarbeitsmappe von einem anderen Tool erstellt wurde und lediglich als Fixed-Layout-Artefakt neu ausgegeben werden muss. Das folgende Beispiel lädt eine vorhandene `.xlsx`-Arbeitsmappe, liest Daten aus ihren Zellen, wendet optionale Anpassungen der Seiteneinrichtung an und speichert das Ergebnis als OFD-Dokument.

```java
import com.aspose.cells.*;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

String dataDir = "C:\\Examples\\";

// Eine vorhandene Excel-Arbeitsmappe von der Festplatte öffnen
Workbook workbook = new Workbook(dataDir + "SampleBook.xlsx");

// (1) Werte aus ausgewählten Zellen lesen und anzeigen, um zu bestätigen, dass die Datei geladen wurde
Worksheet firstSheet = workbook.getWorksheets().get(0);
System.out.println("First sheet name: " + firstSheet.getName());
System.out.println("Cell A1: " + firstSheet.getCells().get("A1").getStringValue());
System.out.println("Cell B1: " + firstSheet.getCells().get("B1").getStringValue());
System.out.println("Cell C1: " + firstSheet.getCells().get("C1").getStringValue());

// (2) Über die Worksheets-Sammlung iterieren, um verfügbare Blätter aufzulisten
System.out.println("\nAvailable worksheets:");
for (int i = 0; i < workbook.getWorksheets().getCount(); i++)
{
    Worksheet ws = workbook.getWorksheets().get(i);
    System.out.println("  [" + i + "] " + ws.getName());
}

// (3) Optional eine Zeitstempelzelle aktualisieren, um die Konvertierung widerzuspiegeln
String timestamp1 = LocalDateTime.now().format(DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss"));
firstSheet.getCells().get("A1").putValue("Converted on: " + timestamp1);

// Eine Zusammenfassungs-Kopfzeile oben am Datenblock einfügen
firstSheet.getCells().insertRow(0);
firstSheet.getCells().get("A1").putValue("Conversion Summary");

String timestamp2 = LocalDateTime.now().format(DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss"));
firstSheet.getCells().get("A2").putValue("Generated: " + timestamp2);

// (4) PageSetup-Eigenschaften auf dem Arbeitsblatt konfigurieren
PageSetup pageSetup = firstSheet.getPageSetup();
pageSetup.setOrientation(PageOrientationType.LANDSCAPE);
pageSetup.setPaperSize(PaperSizeType.PAPER_A_4);
pageSetup.setFitToPagesTall(1);
pageSetup.setFitToPagesWide(1);

// (5) Optional den Druckbereich für die OFD-Ausgabe festlegen
int lastRow = firstSheet.getCells().getMaxDataRow();
int lastCol = firstSheet.getCells().getMaxDataColumn();
String lastColLetter = CellsHelper.columnIndexToName(lastCol);
String printArea = "A1:" + lastColLetter + (lastRow + 1);
firstSheet.getPageSetup().setPrintArea(printArea);
System.out.println("\nPrint area set to: " + printArea);

// (6) Die Arbeitsmappe als OFD-Datei speichern
workbook.save(dataDir + "SampleBook.ofd", SaveFormat.Ofd);
System.out.println("\nFile successfully converted to OFD format: " + dataDir + "SampleBook.ofd");
```

## **Verwandte Artikel**
- [Aufteilen von Excel-Dateien in mehrere Dateien](/cells/de/java/splitting-excel-files-into-multiple-files/)
- [Einfügen eines Bildes in eine Zelle](/cells/de/java/inserting-an-image-into-a-cell/)
- [Lesen und Schreiben von DBF-Dateien](/cells/de/java/dbf/)
- [Sparkline in Bild und HTML konvertieren in Aspose.Cells for Java](/cells/de/java/convert-sparkline-to-image-and-html/)
{{< app/cells/assistant language="java" >}}