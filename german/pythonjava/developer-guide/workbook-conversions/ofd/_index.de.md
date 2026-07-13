---
title: Konvertieren von Excel in das OFD-Format
linktitle: Konvertieren von Excel in das OFD-Format
description: Aspose.Cells for Python via Java ist eine Bibliothek für die Arbeit mit Tabellenkalkulationsdateien, die das Konvertieren von Excel-Arbeitsmappen in das OFD-Format (Open Fixed-layout Document) unterstützt. Dieser Artikel zeigt, wie Excel-Inhalte erstellt und als OFD exportiert werden sowie wie vorhandene Excel-Dateien mit Aspose.Cells for Python via Java in OFD konvertiert werden.
keywords: Aspose.Cells, Python via Java Bibliothek, Tabellenkalkulation, Excel zu OFD, OFD-Konvertierung, SaveFormat.Ofd, Fixed-Layout-Dokument, Arbeitsmappen-Export
type: docs
weight: 195
url: /de/python-java/converting-excel-to-ofd-format/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells for Python via Java unterstützt die direkte Konvertierung von Excel-Arbeitsmappen in das OFD-Format (Open Fixed-layout Document) mithilfe des Enumerationswerts `SaveFormat.Ofd`. Das resultierende OFD-Dokument bewahrt das sichtbare Layout der Arbeitsmappe, die Inhalte, verbundene Zellen, Spaltenbreiten, Zeilenhöhen, Schriftarten, Farben, Rahmen und Zahlenformate. Dies macht Aspose.Cells for Python via Java geeignet für Archivierung, Druck, regulatorische Einreichung und Workflows zur Behördenübermittlung, die eine Fixed-Layout-Ausgabe erfordern.

{{% /alert %}}
## **Einführung**
OFD (Open Fixed-layout Document) ist ein chinesischer nationaler Standard (GB/T 33190-2016) zur Darstellung digitaler Dokumente in einem festen, seitenbasierten Layout. Es erfüllt eine ähnliche Rolle wie PDF für Anwendungsfälle, in denen das visuelle Erscheinungsbild des Quelldokuments genau wie erstellt erhalten bleiben muss. OFD ist in der Volksrepublik China weit verbreitet für Behördenübermittlungen, regulatorische Einreichungen, elektronische Rechnungen und Langzeitarchivierung.

Die Konvertierung von Excel-Arbeitsmappen in OFD ist eine häufige Anforderung in Szenarien, in denen Tabellenkalkulationsinhalte als schreibgeschütztes, layoutfixiertes Artefakt und nicht als bearbeitbare Tabellenkalkulation verteilt werden müssen. Beispiele umfassen den Versand einer finalisierten Rechnung an einen Kunden, die Archivierung eines vierteljährlichen Finanzberichts oder die Einreichung einer Budgettabelle bei einer Aufsichtsbehörde. Aspose.Cells for Python via Java erfüllt diese Anforderung durch den Enumerationswert `SaveFormat.Ofd`, der die Arbeitsmappe direkt in OFD schreibt, ohne einen zwischengeschalteten Konvertierungsschritt zu erfordern. Die OFD-Ausgabe bewahrt Zellwerte, verbundene Bereiche, Schriftarten, Farben, Rahmen, Zahlenformate und Seiteneinrichtungsoptionen, die in der Arbeitsmappe konfiguriert sind.

{{% alert color="primary" %}}

Die von Aspose.Cells for Python via Java erzeugte OFD-Ausgabe bewahrt das sichtbare Layout der Quellarbeitsmappe, einschließlich Zelleninhalte, verbundener Zellen, Spaltenbreiten und Zeilenhöhen. Zellformatierungen wie Schriftarten, Farben, Rahmen, Ausrichtung und Zahlenformate werden ebenfalls in der Fixed-Layout-Ausgabe dargestellt. Die auf dem Arbeitsblatt konfigurierten Seiteneinrichtungsoptionen wie Papierformat, Ausrichtung und Druckbereich beeinflussen das Layout des resultierenden OFD-Dokuments.

{{% /alert %}}
## **Erstellen einer Excel-Arbeitsmappe und Speichern als OFD**
Aspose.Cells for Python via Java ermöglicht es Ihnen, eine Arbeitsmappe programmatisch zu erstellen, mit Daten zu füllen und sie dann direkt mithilfe der Enumeration `SaveFormat.Ofd` im OFD-Format zu speichern. Das folgende Beispiel erstellt eine Rechnung von Grund auf. Es fügt ein Firmenlogo, Kopfinformationen, einen Rechnungsempfängerbereich, Positionszeilen und berechnete Summen hinzu und exportiert dann die Arbeitsmappe in ein OFD-Dokument.
### **Erstellen einer Rechnung mit einem Logo**
Das Beispiel konstruiert ein Rechnungsarbeitsblatt, indem es ein Logobild in den oberen linken Bereich einfügt, den Firmennamen und Kontaktdaten einfügt, einen „INVOICE"-Titel über verbundene Zellen hinzufügt, die Rechnungsnummer und das Datum erfasst, den Rechnungsempfänger auflistet, eine Tabelle mit Positionszeilen mit den Spalten Beschreibung, Menge, Einzelpreis und Gesamtpreis erstellt und Zwischensumme, Steuer und Gesamtsumme mithilfe von Zellformeln berechnet. Formatierungen wie fett formatierte Überschriften, Währungsformat für Preise, Rahmen und Spaltenbreiten werden mithilfe von `Style`- und `Font`-Objekten angewendet. Schließlich wird die Arbeitsmappe mit der Erweiterung `.ofd` unter Verwendung von `SaveFormat.Ofd` gespeichert.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, Style, Cell, TextAlignmentType, BorderType, CellBorderType, Color

dataDir = "/tmp/"

# Eine neue Arbeitsmappe erstellen
workbook = Workbook()

# Das erste Arbeitsblatt abrufen
worksheet = workbook.getWorksheets().get(0)

# Spaltenbreiten festlegen
worksheet.getCells().setColumnWidth(0, 5)
worksheet.getCells().setColumnWidth(1, 35)
worksheet.getCells().setColumnWidth(2, 12)
worksheet.getCells().setColumnWidth(3, 15)
worksheet.getCells().setColumnWidth(4, 15)
worksheet.getCells().setColumnWidth(5, 5)

# Firmenlogo einfügen
worksheet.getPictures().add(1, 1, dataDir + "logo.png")

# Firmenname und Kontaktdaten
worksheet.getCells().get("B3").putValue("Acme Corporation")
worksheet.getCells().get("B4").putValue("123 Business Street")
worksheet.getCells().get("B5").putValue("City, State 12345")
worksheet.getCells().get("B6").putValue("Phone: (555) 123-4567")

# RECHNUNG-Titel - Zellen zusammenführen
worksheet.getCells().merge(7, 1, 2, 4)
titleCell = worksheet.getCells().get("B8")
titleCell.putValue("INVOICE")

titleStyle = workbook.createStyle()
titleStyle.getFont().setBold(True)
titleStyle.getFont().setSize(20)
titleStyle.setHorizontalAlignment(TextAlignmentType.CENTER)
titleCell.setStyle(titleStyle)

# Rechnungsnummer und Datum
worksheet.getCells().get("B11").putValue("Invoice Number:")
worksheet.getCells().get("C11").putValue("INV-2024-001")
worksheet.getCells().get("B12").putValue("Date:")
worksheet.getCells().get("C12").putValue(datetime.datetime.now().strftime("%Y-%m-%d"))

# Rechnungsempfänger-Abschnitt
worksheet.getCells().get("B14").putValue("Bill To:")
worksheet.getCells().get("B15").putValue("Client Name")
worksheet.getCells().get("B16").putValue("Client Address")
worksheet.getCells().get("B17").putValue("Client City, State")

# Positionen-Kopfzeile
headerDesc = worksheet.getCells().get("B19")
headerQty = worksheet.getCells().get("C19")
headerPrice = worksheet.getCells().get("D19")
headerTotal = worksheet.getCells().get("E19")

headerDesc.putValue("Description")
headerQty.putValue("Quantity")
headerPrice.putValue("Unit Price")
headerTotal.putValue("Total")

headerStyle = workbook.createStyle()
headerStyle.getFont().setBold(True)
headerStyle.getFont().setColor(Color.getWhite())
headerStyle.setBackgroundColor(Color.getNavy())
headerStyle.setHorizontalAlignment(TextAlignmentType.CENTER)
headerStyle.getBorders().get(BorderType.TOP_BORDER).setLineStyle(CellBorderType.THIN)
headerStyle.getBorders().get(BorderType.BOTTOM_BORDER).setLineStyle(CellBorderType.THIN)
headerStyle.getBorders().get(BorderType.LEFT_BORDER).setLineStyle(CellBorderType.THIN)
headerStyle.getBorders().get(BorderType.RIGHT_BORDER).setLineStyle(CellBorderType.THIN)

headerDesc.setStyle(headerStyle)
headerQty.setStyle(headerStyle)
headerPrice.setStyle(headerStyle)
headerTotal.setStyle(headerStyle)

# Währungsstil mit Rahmen
currencyStyle = workbook.createStyle()
currencyStyle.setCustom("\"$\"#,##0.00")
currencyStyle.getBorders().get(BorderType.TOP_BORDER).setLineStyle(CellBorderType.THIN)
currencyStyle.getBorders().get(BorderType.BOTTOM_BORDER).setLineStyle(CellBorderType.THIN)
currencyStyle.getBorders().get(BorderType.LEFT_BORDER).setLineStyle(CellBorderType.THIN)
currencyStyle.getBorders().get(BorderType.RIGHT_BORDER).setLineStyle(CellBorderType.THIN)

# Einfacher Rahmenstil für Beschreibungs-/Mengenzellen
borderStyle = workbook.createStyle()
borderStyle.getBorders().get(BorderType.TOP_BORDER).setLineStyle(CellBorderType.THIN)
borderStyle.getBorders().get(BorderType.BOTTOM_BORDER).setLineStyle(CellBorderType.THIN)
borderStyle.getBorders().get(BorderType.LEFT_BORDER).setLineStyle(CellBorderType.THIN)
borderStyle.getBorders().get(BorderType.RIGHT_BORDER).setLineStyle(CellBorderType.THIN)

# Positionszeilen
lineItems = [
    ["Product A - Widget", 2, 50.00],
    ["Product B - Gadget", 3, 75.00],
    ["Product C - Service", 1, 100.00]
]

for i in range(len(lineItems)):
    row = 20 + i
    descCell = worksheet.getCells().get(row, 1)
    qtyCell = worksheet.getCells().get(row, 2)
    priceCell = worksheet.getCells().get(row, 3)
    totalCell = worksheet.getCells().get(row, 4)

    descCell.putValue(lineItems[i][0])
    qtyCell.putValue(lineItems[i][1])
    priceCell.putValue(lineItems[i][2])
    totalCell.setFormula("C" + str(row) + "*D" + str(row))

    descCell.setStyle(borderStyle)
    qtyCell.setStyle(borderStyle)
    priceCell.setStyle(currencyStyle)
    totalCell.setStyle(currencyStyle)

# Zwischensumme, Steuer, Gesamtbetrag
worksheet.getCells().get("B24").putValue("Subtotal:")
subtotalCell = worksheet.getCells().get("E24")
subtotalCell.setFormula("SUM(E20:E22)")

worksheet.getCells().get("B25").putValue("Tax (10%):")
taxCell = worksheet.getCells().get("E25")
taxCell.setFormula("E24*0.1")

worksheet.getCells().get("B26").putValue("Grand Total:")
grandTotalCell = worksheet.getCells().get("E26")
grandTotalCell.setFormula("E24+E25")

# Fett + Währungsstil für Gesamtwerte
totalStyle = workbook.createStyle()
totalStyle.getFont().setBold(True)
totalStyle.setCustom("\"$\"#,##0.00")

subtotalCell.setStyle(totalStyle)
taxCell.setStyle(totalStyle)
grandTotalCell.setStyle(totalStyle)

# Fetter Stil für Gesamtbezeichnungen
boldStyle = workbook.createStyle()
boldStyle.getFont().setBold(True)

worksheet.getCells().get("B24").setStyle(boldStyle)
worksheet.getCells().get("B25").setStyle(boldStyle)
worksheet.getCells().get("B26").setStyle(boldStyle)

# Die Arbeitsmappe als OFD-Datei speichern
workbook.save(dataDir + "Invoice.ofd", SaveFormat.Ofd)

jpype.shutdownJVM()
```
## **Konvertieren einer vorhandenen Excel-Datei in OFD**
Aspose.Cells for Python via Java kann auch eine vorhandene Excel-Arbeitsmappe von der Festplatte laden und sie direkt in das OFD-Format exportieren. Dies ist nützlich für Stapelkonvertierungs-Pipelines, Archivierungs-Workflows und Szenarien, in denen die Quellarbeitsmappe von einem anderen Tool erstellt wurde und nur als Fixed-Layout-Artefakt erneut ausgegeben werden muss. Das folgende Beispiel lädt eine vorhandene `.xlsx`-Arbeitsmappe, liest Daten aus deren Zellen, wendet optionale Anpassungen der Seiteneinrichtung an und speichert das Ergebnis als OFD-Dokument.

```python
from datetime import datetime
jpype.startJVM()
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PageOrientationType, PaperSizeType, CellsHelper

dataDir = "C:\\Examples\\"

# Eine vorhandene Excel-Arbeitsmappe von der Festplatte öffnen
workbook = Workbook(dataDir + "SampleBook.xlsx")

# (1) Werte aus ausgewählten Zellen lesen und anzeigen, um zu bestätigen, dass die Datei geladen wurde
firstSheet = workbook.getWorksheets().get(0)
print("First sheet name: " + firstSheet.getName())
print("Cell A1: " + firstSheet.getCells().get("A1").getStringValue())
print("Cell B1: " + firstSheet.getCells().get("B1").getStringValue())
print("Cell C1: " + firstSheet.getCells().get("C1").getStringValue())

# (2) Über die Worksheets-Sammlung iterieren, um die verfügbaren Blätter aufzulisten
print("\nAvailable worksheets:")
for i in range(workbook.getWorksheets().getCount()):
    ws = workbook.getWorksheets().get(i)
    print("  [" + str(i) + "] " + ws.getName())

# (3) Optional eine Zeitstempelzelle aktualisieren, um die Konvertierung widerzuspiegeln
firstSheet.getCells().get("A1").putValue("Converted on: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

# Eine Zusammenfassungs-Kopfzeile oben am Datenblock einfügen
firstSheet.getCells().insertRow(0)
firstSheet.getCells().get("A1").putValue("Conversion Summary")
firstSheet.getCells().get("A2").putValue("Generated: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

# (4) PageSetup-Eigenschaften auf dem Arbeitsblatt konfigurieren
pageSetup = firstSheet.getPageSetup()
pageSetup.setOrientation(PageOrientationType.LANDSCAPE)
pageSetup.setPaperSize(PaperSizeType.PAPER_A_4)
pageSetup.setFitToPagesTall(1)
pageSetup.setFitToPagesWide(1)

# (5) Optional den Druckbereich für die OFD-Ausgabe festlegen
lastRow = firstSheet.getCells().getMaxDataRow()
lastCol = firstSheet.getCells().getMaxDataColumn()
lastColLetter = CellsHelper.columnIndexToName(lastCol)
printArea = "A1:" + lastColLetter + str(lastRow + 1)
firstSheet.getPageSetup().setPrintArea(printArea)
print("\nPrint area set to: " + printArea)

# (6) Die Arbeitsmappe als OFD-Datei speichern
workbook.save(dataDir + "SampleBook.ofd", SaveFormat.Ofd)
print("\nFile successfully converted to OFD format: " + dataDir + "SampleBook.ofd")

jpype.shutdownJVM()
```

## **Verwandte Artikel**
- [Aufteilen von Excel-Dateien in mehrere Dateien](/cells/de/python-java/splitting-excel-files-into-multiple-files/)
- [Einfügen eines Bildes in eine Zelle](/cells/de/python-java/inserting-an-image-into-a-cell/)
- [Lesen und Schreiben von DBF-Dateien](/cells/de/python-java/dbf/)
- [Konvertieren einer Sparkline in Bild und HTML in Aspose.Cells for Python via Java](/cells/de/python-java/convert-sparkline-to-image-and-html/)
{{< app/cells/assistant language="python" >}}