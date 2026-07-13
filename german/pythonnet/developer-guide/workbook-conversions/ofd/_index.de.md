---
title: Konvertieren von Excel in das OFD-Format
linktitle: Konvertieren von Excel in das OFD-Format
description: Aspose.Cells for Python via .NET ist eine Tabellenverarbeitungsbibliothek, die das Konvertieren von Excel-Arbeitsmappen in das OFD-Format (Open Fixed-layout Document) unterstützt. Dieser Artikel zeigt, wie Excel-Inhalte erstellt und als OFD exportiert werden, sowie wie vorhandene Excel-Dateien mit Aspose.Cells in OFD konvertiert werden.
keywords: Aspose.Cells, Python via .NET-Bibliothek, Tabellenkalkulation, Excel zu OFD, OFD-Konvertierung, SaveFormat.Ofd, Fixed-Layout-Dokument, Arbeitsmappen-Export
type: docs
weight: 195
url: /de/python-net/converting-excel-to-ofd-format/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells unterstützt die direkte Konvertierung von Excel-Arbeitsmappen in das OFD-Format (Open Fixed-layout Document) unter Verwendung des Enumerationswerts `SaveFormat.Ofd`. Das resultierende OFD-Dokument bewahrt das sichtbare Layout der Arbeitsmappe, den Inhalt, verbundene Zellen, Spaltenbreiten, Zeilenhöhen, Schriftarten, Farben, Rahmen und Zahlenformate. Dies macht Aspose.Cells geeignet für Archivierungs-, Druck-, regulatorische Einreichungs- und Behördenübermittlungs-Workflows, die eine Fixed-Layout-Ausgabe erfordern.

{{% /alert %}}
## **Einführung**
OFD (Open Fixed-layout Document) ist ein chinesischer nationaler Standard (GB/T 33190-2016) zur Darstellung digitaler Dokumente in einem festen, seitenbasierten Layout. Es erfüllt eine ähnliche Rolle wie PDF für Anwendungsfälle, in denen das visuelle Erscheinungsbild des Quelldokuments genau wie erstellt erhalten bleiben muss. OFD wird in der Volksrepublik China häufig für Behördenübermittlungen, regulatorische Einreichungen, elektronische Rechnungen und Langzeitarchivierung verwendet.

Das Konvertieren von Excel-Arbeitsmappen in OFD ist eine häufige Anforderung in Szenarien, in denen Tabellenkalkulationsinhalte als schreibgeschütztes, layout-gesperrtes Artefakt verteilt werden müssen, anstatt als bearbeitbare Tabellenkalkulation. Beispiele umfassen das Versenden einer finalisierten Rechnung an einen Kunden, die Archivierung eines Quartalsfinanzberichts oder die Einreichung einer Budgettabelle bei einer Aufsichtsbehörde. Aspose.Cells adressiert diese Anforderung durch den Enumerationswert `SaveFormat.Ofd`, der die Arbeitsmappe direkt in OFD schreibt, ohne einen zwischengeschalteten Konvertierungsschritt zu erfordern. Die OFD-Ausgabe bewahrt Zellwerte, verbundene Bereiche, Schriftarten, Farben, Rahmen, Zahlenformate und Seitenlayoutoptionen, die in der Arbeitsmappe konfiguriert sind.

{{% alert color="primary" %}}

Die von Aspose.Cells generierte OFD-Ausgabe bewahrt das sichtbare Layout der Quellarbeitsmappe, einschließlich Zellinhalten, verbundenen Zellen, Spaltenbreiten und Zeilenhöhen. Zellenformatierungen wie Schriftarten, Farben, Rahmen, Ausrichtung und Zahlenformate werden ebenfalls in der Fixed-Layout-Ausgabe dargestellt. Seitenlayoutoptionen, die auf dem Arbeitsblatt konfiguriert sind, wie Papierformat, Ausrichtung und Druckbereich, beeinflussen das Layout des resultierenden OFD-Dokuments.

{{% /alert %}}
## **Erstellen einer Excel-Arbeitsmappe und Speichern als OFD**
Aspose.Cells ermöglicht es Ihnen, eine Arbeitsmappe programmatisch zu erstellen, sie mit Daten zu befüllen und sie dann direkt im OFD-Format unter Verwendung der `SaveFormat.Ofd`-Enumeration zu speichern. Das folgende Beispiel erstellt eine Rechnung von Grund auf. Es fügt ein Firmenlogo, Kopfinformationen, einen Rechnungsempfängerbereich, Positionen und berechnete Summen hinzu und exportiert dann die Arbeitsmappe in ein OFD-Dokument.
### **Erstellen einer Rechnung mit einem Logo**
Das Beispiel erstellt ein Rechnungsarbeitsblatt, indem ein Logobild in den oberen linken Bereich eingefügt wird, der Firmenname und die Kontaktdaten ausgefüllt werden, ein "INVOICE"-Titel über verbundene Zellen hinzugefügt wird, die Rechnungsnummer und das Datum erfasst werden, der Rechnungsempfänger aufgelistet wird, eine Positionstabelle mit Spalten für Beschreibung, Menge, Einzelpreis und Summe aufgebaut wird und die Zwischensumme, die Steuer und die Gesamtsumme mithilfe von Zellformeln berechnet werden. Formatierungen wie fette Überschriften, Währungsformat für Preise, Rahmen und Spaltenbreiten werden mit `Style`- und `Font`-Objekten angewendet. Schließlich wird die Arbeitsmappe mit der Erweiterung `.ofd` unter Verwendung von `SaveFormat.Ofd` gespeichert.

```python
from datetime import datetime

data_dir = "C:\\Temp\\"

# Erstellen einer neuen Arbeitsmappe
workbook = ac.Workbook()

# Erstes Arbeitsblatt abrufen
worksheet = workbook.worksheets[0]

# Spaltenbreiten festlegen
worksheet.cells.set_column_width(0, 5)
worksheet.cells.set_column_width(1, 35)
worksheet.cells.set_column_width(2, 12)
worksheet.cells.set_column_width(3, 15)
worksheet.cells.set_column_width(4, 15)
worksheet.cells.set_column_width(5, 5)

# Firmenlogo einfügen
worksheet.pictures.add(1, 1, data_dir + "logo.png")

# Firmenname und Kontaktdaten
worksheet.cells["B3"].put_value("Acme Corporation")
worksheet.cells["B4"].put_value("123 Business Street")
worksheet.cells["B5"].put_value("City, State 12345")
worksheet.cells["B6"].put_value("Phone: (555) 123-4567")

# RECHNUNG Titel - Zellen zusammenführen
worksheet.cells.merge(7, 1, 2, 4)
title_cell = worksheet.cells["B8"]
title_cell.put_value("INVOICE")

title_style = workbook.create_style()
title_style.font.is_bold = True
title_style.font.size = 20
title_style.horizontal_alignment = ac.TextAlignmentType.CENTER
title_cell.set_style(title_style)

# Rechnungsnummer und Datum
worksheet.cells["B11"].put_value("Invoice Number:")
worksheet.cells["C11"].put_value("INV-2024-001")
worksheet.cells["B12"].put_value("Date:")
worksheet.cells["C12"].put_value(datetime.now().strftime("%Y-%m-%d"))

# Rechnungsempfänger-Abschnitt
worksheet.cells["B14"].put_value("Bill To:")
worksheet.cells["B15"].put_value("Client Name")
worksheet.cells["B16"].put_value("Client Address")
worksheet.cells["B17"].put_value("Client City, State")

# Kopfzeile der Positionen
header_desc = worksheet.cells["B19"]
header_qty = worksheet.cells["C19"]
header_price = worksheet.cells["D19"]
header_total = worksheet.cells["E19"]

header_desc.put_value("Description")
header_qty.put_value("Quantity")
header_price.put_value("Unit Price")
header_total.put_value("Total")

header_style = workbook.create_style()
header_style.font.is_bold = True
header_style.font.color = drawing.Color.white
header_style.background_color = drawing.Color.navy
header_style.horizontal_alignment = ac.TextAlignmentType.CENTER
header_style.borders[ac.BorderType.TOP_BORDER].line_style = ac.CellBorderType.THIN
header_style.borders[ac.BorderType.BOTTOM_BORDER].line_style = ac.CellBorderType.THIN
header_style.borders[ac.BorderType.LEFT_BORDER].line_style = ac.CellBorderType.THIN
header_style.borders[ac.BorderType.RIGHT_BORDER].line_style = ac.CellBorderType.THIN

header_desc.set_style(header_style)
header_qty.set_style(header_style)
header_price.set_style(header_style)
header_total.set_style(header_style)

# Währungsstil mit Rahmen
currency_style = workbook.create_style()
currency_style.custom = "\"$\"#,##0.00"
currency_style.borders[ac.BorderType.TOP_BORDER].line_style = ac.CellBorderType.THIN
currency_style.borders[ac.BorderType.BOTTOM_BORDER].line_style = ac.CellBorderType.THIN
currency_style.borders[ac.BorderType.LEFT_BORDER].line_style = ac.CellBorderType.THIN
currency_style.borders[ac.BorderType.RIGHT_BORDER].line_style = ac.CellBorderType.THIN

# Einfacher Rahmenstil für Beschreibungs-/Mengenzellen
border_style = workbook.create_style()
border_style.borders[ac.BorderType.TOP_BORDER].line_style = ac.CellBorderType.THIN
border_style.borders[ac.BorderType.BOTTOM_BORDER].line_style = ac.CellBorderType.THIN
border_style.borders[ac.BorderType.LEFT_BORDER].line_style = ac.CellBorderType.THIN
border_style.borders[ac.BorderType.RIGHT_BORDER].line_style = ac.CellBorderType.THIN

# Zeilen der Positionen
line_items = [
    ["Product A - Widget", 2, 50.00],
    ["Product B - Gadget", 3, 75.00],
    ["Product C - Service", 1, 100.00]
]

for i in range(len(line_items)):
    row = 20 + i
    desc_cell = worksheet.cells[row, 1]
    qty_cell = worksheet.cells[row, 2]
    price_cell = worksheet.cells[row, 3]
    total_cell = worksheet.cells[row, 4]

    desc_cell.put_value(line_items[i][0])
    qty_cell.put_value(line_items[i][1])
    price_cell.put_value(line_items[i][2])
    total_cell.formula = "C" + str(row) + "*D" + str(row)

    desc_cell.set_style(border_style)
    qty_cell.set_style(border_style)
    price_cell.set_style(currency_style)
    total_cell.set_style(currency_style)

# Zwischensumme, Steuer, Gesamtbetrag
worksheet.cells["B24"].put_value("Subtotal:")
subtotal_cell = worksheet.cells["E24"]
subtotal_cell.formula = "SUM(E20:E22)"

worksheet.cells["B25"].put_value("Tax (10%):")
tax_cell = worksheet.cells["E25"]
tax_cell.formula = "E24*0.1"

worksheet.cells["B26"].put_value("Grand Total:")
grand_total_cell = worksheet.cells["E26"]
grand_total_cell.formula = "E24+E25"

# Fett + Währungsstil für Summenwerte
total_style = workbook.create_style()
total_style.font.is_bold = True
total_style.custom = "\"$\"#,##0.00"

subtotal_cell.set_style(total_style)
tax_cell.set_style(total_style)
grand_total_cell.set_style(total_style)

# Fettstil für Summenbeschriftungen
bold_style = workbook.create_style()
bold_style.font.is_bold = True

worksheet.cells["B24"].set_style(bold_style)
worksheet.cells["B25"].set_style(bold_style)
worksheet.cells["B26"].set_style(bold_style)

# Arbeitsmappe als OFD-Datei speichern
workbook.save(data_dir + "Invoice.ofd", ac.SaveFormat.Ofd)
```
## **Konvertieren einer vorhandenen Excel-Datei in OFD**
Aspose.Cells kann auch eine vorhandene Excel-Arbeitsmappe von der Festplatte laden und direkt in das OFD-Format exportieren. Dies ist nützlich für Batch-Konvertierungspipelines, Archivierungs-Workflows und Szenarien, in denen die Quellarbeitsmappe von einem anderen Tool erstellt wurde und nur als Fixed-Layout-Artefakt erneut ausgegeben werden muss. Das folgende Beispiel lädt eine vorhandene `.xlsx`-Arbeitsmappe, liest Daten aus ihren Zellen, wendet optionale Seitenlayoutanpassungen an und speichert das Ergebnis als OFD-Dokument.

```python
from datetime import datetime

dataDir = "C:\\Examples\\"

# Eine bestehende Excel-Arbeitsmappe von der Festplatte öffnen
workbook = ac.Workbook(dataDir + "SampleBook.xlsx")

# (1) Werte aus ausgewählten Zellen lesen und anzeigen, um zu bestätigen, dass die Datei geladen wurde
firstSheet = workbook.worksheets[0]
print("First sheet name: " + firstSheet.name)
print("Cell A1: " + firstSheet.cells["A1"].string_value)
print("Cell B1: " + firstSheet.cells["B1"].string_value)
print("Cell C1: " + firstSheet.cells["C1"].string_value)

# (2) Über die Worksheets-Sammlung iterieren, um verfügbare Blätter aufzulisten
print("\nAvailable worksheets:")
for i in range(workbook.worksheets.count):
    ws = workbook.worksheets[i]
    print("  [" + str(i) + "] " + ws.name)

# (3) Optional eine Zeitstempelzelle aktualisieren, um die Konvertierung widerzuspiegeln
firstSheet.cells["A1"].put_value("Converted on: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

# Eine Zusammenfassungs-Kopfzeile oben im Datenblock einfügen
firstSheet.cells.insert_row(0)
firstSheet.cells["A1"].put_value("Conversion Summary")
firstSheet.cells["A2"].put_value("Generated: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

# (4) PageSetup-Eigenschaften auf dem Arbeitsblatt konfigurieren
pageSetup = firstSheet.page_setup
pageSetup.orientation = ac.PageOrientationType.LANDSCAPE
pageSetup.paper_size = ac.PaperSizeType.PAPER_A4
pageSetup.fit_to_pages_tall = 1
pageSetup.fit_to_pages_wide = 1

# (5) Optional den Druckbereich für die OFD-Ausgabe festlegen
lastRow = firstSheet.cells.max_data_row
lastCol = firstSheet.cells.max_data_column
lastColLetter = ac.CellsHelper.column_index_to_name(lastCol)
printArea = "A1:" + lastColLetter + str(lastRow + 1)
firstSheet.page_setup.print_area = printArea
print("\nPrint area set to: " + printArea)

# (6) Die Arbeitsmappe als OFD-Datei speichern
workbook.save(dataDir + "SampleBook.ofd", ac.SaveFormat.Ofd)
print("\nFile successfully converted to OFD format: " + dataDir + "SampleBook.ofd")
```

## **Verwandte Artikel**
- [Excel-Dateien in mehrere Dateien aufteilen](/cells/de/python-net/splitting-excel-files-into-multiple-files/)
- [Einfügen eines Bildes in eine Zelle](/cells/de/python-net/inserting-an-image-into-a-cell/)
- [Lesen und Schreiben von DBF-Dateien](/cells/de/python-net/dbf/)
- [Sparkline in Bild und HTML konvertieren in Aspose.Cells for Python via .NET](/cells/de/python-net/convert-sparkline-to-image-and-html/)
{{< app/cells/assistant language="python" >}}