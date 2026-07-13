---
title: Konvertieren von Excel in das OFD-Format
linktitle: Konvertieren von Excel in das OFD-Format
description: Aspose.Cells ist eine .NET-Bibliothek für die Arbeit mit Tabellenkalkulationsdateien, die das Konvertieren von Excel-Arbeitsmappen in das OFD-Format (Open Fixed-layout Document) unterstützt. Dieser Artikel zeigt, wie Excel-Inhalte erstellt und als OFD exportiert werden, sowie wie vorhandene Excel-Dateien mit Aspose.Cells in OFD konvertiert werden.
keywords: Aspose.Cells, NET-Bibliothek, Tabellenkalkulation, Excel zu OFD, OFD-Konvertierung, SaveFormat.Ofd, Fixed-Layout-Dokument, Arbeitsmappen-Export
type: docs
weight: 195
url: /de/net/converting-excel-to-ofd-format/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells unterstützt die direkte Konvertierung von Excel-Arbeitsmappen in das OFD-Format (Open Fixed-layout Document) mithilfe des Enumerationswerts `SaveFormat.Ofd`. Das resultierende OFD-Dokument bewahrt das sichtbare Layout, den Inhalt, die verbundenen Zellen, die Spaltenbreiten, die Zeilenhöhen, die Schriftarten, die Farben, die Rahmen und die Zahlenformate der Arbeitsmappe. Dies macht Aspose.Cells geeignet für Archivierung, Druck, regulatorische Einreichungen und Workflows zur Behördenvorlage, die eine Fixed-Layout-Ausgabe erfordern.

{{% /alert %}}
## **Einführung**
OFD (Open Fixed-layout Document) ist ein chinesischer nationaler Standard (GB/T 33190-2016) zur Darstellung digitaler Dokumente in einem festen, seitenbasierten Layout. Es erfüllt eine ähnliche Rolle wie PDF für Anwendungsfälle, in denen das visuelle Erscheinungsbild des Quelldokuments genau wie erstellt erhalten bleiben muss. OFD ist in der Volksrepublik China weit verbreitet für Behördenvorlagen, regulatorische Einreichungen, elektronische Rechnungen und Langzeitarchivierung.

Die Konvertierung von Excel-Arbeitsmappen in OFD ist eine häufige Anforderung in Szenarien, in denen Tabellenkalkulationsinhalte als schreibgeschütztes, layoutfixiertes Artefakt verteilt werden müssen, und nicht als bearbeitbare Tabellenkalkulation. Beispiele umfassen den Versand einer finalisierten Rechnung an einen Kunden, die Archivierung eines Quartalsfinanzberichts oder die Einreichung einer Budgettabelle bei einer Aufsichtsbehörde. Aspose.Cells erfüllt diese Anforderung durch den Enumerationswert `SaveFormat.Ofd`, der die Arbeitsmappe direkt in OFD schreibt, ohne einen zwischengeschalteten Konvertierungsschritt zu erfordern. Die OFD-Ausgabe bewahrt Zellwerte, verbundene Bereiche, Schriftarten, Farben, Rahmen, Zahlenformate und auf der Arbeitsmappe konfigurierte Optionen zur Seiteneinrichtung.

{{% alert color="primary" %}}

Die von Aspose.Cells erzeugte OFD-Ausgabe bewahrt das sichtbare Layout der Quellarbeitsmappe, einschließlich Zellinhalten, verbundener Zellen, Spaltenbreiten und Zeilenhöhen. Zellenformatierungen wie Schriftarten, Farben, Rahmen, Ausrichtung und Zahlenformate werden ebenfalls in der Fixed-Layout-Ausgabe gerendert. Auf dem Arbeitsblatt konfigurierte Optionen zur Seiteneinrichtung, wie Papierformat, Ausrichtung und Druckbereich, beeinflussen das Layout des resultierenden OFD-Dokuments.

{{% /alert %}}
## **Erstellen einer Excel-Arbeitsmappe und Speichern als OFD**
Aspose.Cells ermöglicht es Ihnen, eine Arbeitsmappe programmatisch zu erstellen, sie mit Daten zu befüllen und sie dann direkt im OFD-Format unter Verwendung der Enumeration `SaveFormat.Ofd` zu speichern. Das folgende Beispiel erstellt eine Rechnung von Grund auf. Es fügt ein Firmenlogo, Kopfinformationen, einen „Rechnungsempfänger"-Abschnitt, Positionszeilen und berechnete Summen hinzu und exportiert anschließend die Arbeitsmappe in ein OFD-Dokument.
### **Erstellen einer Rechnung mit einem Logo**
Das Beispiel konstruiert ein Rechnungsarbeitsblatt, indem es ein Logobild in den oberen linken Bereich einfügt, den Firmennamen und die Kontaktdaten einträgt, einen „INVOICE"-Titel über verbundene Zellen hinweg hinzufügt, die Rechnungsnummer und das Datum erfasst, den Rechnungsempfänger auflistet, eine Tabelle für Positionszeilen mit den Spalten Beschreibung, Menge, Einzelpreis und Gesamtpreis erstellt und die Zwischensumme, die Steuer und den Gesamtbetrag mithilfe von Zellformeln berechnet. Formatierungen wie fettgedruckte Kopfzeilen, Währungsformat für Preise, Rahmen und Spaltenbreiten werden mithilfe der Objekte `Style` und `Font` angewendet. Schließlich wird die Arbeitsmappe mit der Erweiterung `.ofd` unter Verwendung von `SaveFormat.Ofd` gespeichert.

```csharp
using System;
using Aspose.Cells;
using System.Drawing;

string dataDir = "C:\\Temp\\";

// Erstellen Sie eine neue Arbeitsmappe
Workbook workbook = new Workbook();

// Erste Arbeitsblatt abrufen
Worksheet worksheet = workbook.Worksheets[0];

// Spaltenbreiten festlegen
worksheet.Cells.SetColumnWidth(0, 5);
worksheet.Cells.SetColumnWidth(1, 35);
worksheet.Cells.SetColumnWidth(2, 12);
worksheet.Cells.SetColumnWidth(3, 15);
worksheet.Cells.SetColumnWidth(4, 15);
worksheet.Cells.SetColumnWidth(5, 5);

// Firmenlogo einfügen
worksheet.Pictures.Add(1, 1, dataDir + "logo.png");

// Firmenname und Kontaktdetails
worksheet.Cells["B3"].PutValue("Acme Corporation");
worksheet.Cells["B4"].PutValue("123 Business Street");
worksheet.Cells["B5"].PutValue("City, State 12345");
worksheet.Cells["B6"].PutValue("Phone: (555) 123-4567");

// RECHNUNG Titel - Zellen zusammenführen
worksheet.Cells.Merge(7, 1, 2, 4);
Cell titleCell = worksheet.Cells["B8"];
titleCell.PutValue("INVOICE");

Style titleStyle = workbook.CreateStyle();
titleStyle.Font.IsBold = true;
titleStyle.Font.Size = 20;
titleStyle.HorizontalAlignment = TextAlignmentType.Center;
titleCell.SetStyle(titleStyle);

// Rechnungsnummer und Datum
worksheet.Cells["B11"].PutValue("Invoice Number:");
worksheet.Cells["C11"].PutValue("INV-2024-001");
worksheet.Cells["B12"].PutValue("Date:");
worksheet.Cells["C12"].PutValue(DateTime.Now.ToString("yyyy-MM-dd"));

// Rechnungsempfänger-Bereich
worksheet.Cells["B14"].PutValue("Bill To:");
worksheet.Cells["B15"].PutValue("Client Name");
worksheet.Cells["B16"].PutValue("Client Address");
worksheet.Cells["B17"].PutValue("Client City, State");

// Kopfzeile der Positionen
Cell headerDesc = worksheet.Cells["B19"];
Cell headerQty = worksheet.Cells["C19"];
Cell headerPrice = worksheet.Cells["D19"];
Cell headerTotal = worksheet.Cells["E19"];

headerDesc.PutValue("Description");
headerQty.PutValue("Quantity");
headerPrice.PutValue("Unit Price");
headerTotal.PutValue("Total");

Style headerStyle = workbook.CreateStyle();
headerStyle.Font.IsBold = true;
headerStyle.Font.Color = Color.White;
headerStyle.BackgroundColor = Color.Navy;
headerStyle.HorizontalAlignment = TextAlignmentType.Center;
headerStyle.Borders[BorderType.TopBorder].LineStyle = CellBorderType.Thin;
headerStyle.Borders[BorderType.BottomBorder].LineStyle = CellBorderType.Thin;
headerStyle.Borders[BorderType.LeftBorder].LineStyle = CellBorderType.Thin;
headerStyle.Borders[BorderType.RightBorder].LineStyle = CellBorderType.Thin;

headerDesc.SetStyle(headerStyle);
headerQty.SetStyle(headerStyle);
headerPrice.SetStyle(headerStyle);
headerTotal.SetStyle(headerStyle);

// Währungsstil mit Rahmen
Style currencyStyle = workbook.CreateStyle();
currencyStyle.Custom = "\"$\"#,##0.00";
currencyStyle.Borders[BorderType.TopBorder].LineStyle = CellBorderType.Thin;
currencyStyle.Borders[BorderType.BottomBorder].LineStyle = CellBorderType.Thin;
currencyStyle.Borders[BorderType.LeftBorder].LineStyle = CellBorderType.Thin;
currencyStyle.Borders[BorderType.RightBorder].LineStyle = CellBorderType.Thin;

// Einfacher Rahmenstil für Beschreibungs-/Mengenzellen
Style borderStyle = workbook.CreateStyle();
borderStyle.Borders[BorderType.TopBorder].LineStyle = CellBorderType.Thin;
borderStyle.Borders[BorderType.BottomBorder].LineStyle = CellBorderType.Thin;
borderStyle.Borders[BorderType.LeftBorder].LineStyle = CellBorderType.Thin;
borderStyle.Borders[BorderType.RightBorder].LineStyle = CellBorderType.Thin;

// Positionszeilen
object[,] lineItems = new object[,] {
    {"Product A - Widget", 2, 50.00},
    {"Product B - Gadget", 3, 75.00},
    {"Product C - Service", 1, 100.00}
};

for (int i = 0; i < lineItems.GetLength(0); i++)
{
    int row = 20 + i;
    Cell descCell = worksheet.Cells[row, 1];
    Cell qtyCell = worksheet.Cells[row, 2];
    Cell priceCell = worksheet.Cells[row, 3];
    Cell totalCell = worksheet.Cells[row, 4];

    descCell.PutValue(lineItems[i, 0]);
    qtyCell.PutValue(lineItems[i, 1]);
    priceCell.PutValue(lineItems[i, 2]);
    totalCell.Formula = "C" + row + "*D" + row;

    descCell.SetStyle(borderStyle);
    qtyCell.SetStyle(borderStyle);
    priceCell.SetStyle(currencyStyle);
    totalCell.SetStyle(currencyStyle);
}

// Zwischensumme, Steuer, Gesamtsumme
worksheet.Cells["B24"].PutValue("Subtotal:");
Cell subtotalCell = worksheet.Cells["E24"];
subtotalCell.Formula = "SUM(E20:E22)";

worksheet.Cells["B25"].PutValue("Tax (10%):");
Cell taxCell = worksheet.Cells["E25"];
taxCell.Formula = "E24*0.1";

worksheet.Cells["B26"].PutValue("Grand Total:");
Cell grandTotalCell = worksheet.Cells["E26"];
grandTotalCell.Formula = "E24+E25";

// Fett + Währungsstil für Gesamtwerte
Style totalStyle = workbook.CreateStyle();
totalStyle.Font.IsBold = true;
totalStyle.Custom = "\"$\"#,##0.00";

subtotalCell.SetStyle(totalStyle);
taxCell.SetStyle(totalStyle);
grandTotalCell.SetStyle(totalStyle);

// Fettstil für Gesamtbeschriftungen
Style boldStyle = workbook.CreateStyle();
boldStyle.Font.IsBold = true;

worksheet.Cells["B24"].SetStyle(boldStyle);
worksheet.Cells["B25"].SetStyle(boldStyle);
worksheet.Cells["B26"].SetStyle(boldStyle);

// Arbeitsmappe als OFD-Datei speichern
workbook.Save(dataDir + "Invoice.ofd", SaveFormat.Ofd);
```
## **Konvertieren einer vorhandenen Excel-Datei in OFD**
Aspose.Cells kann auch eine vorhandene Excel-Arbeitsmappe von der Festplatte laden und sie direkt in das OFD-Format exportieren. Dies ist nützlich für Stapelkonvertierungspipelines, Archivierungsworkflows und Szenarien, in denen die Quellarbeitsmappe von einem anderen Tool erstellt wurde und nur als Fixed-Layout-Artefakt erneut ausgegeben werden muss. Das folgende Beispiel lädt eine vorhandene `.xlsx`-Arbeitsmappe, liest Daten aus ihren Zellen, wendet optionale Anpassungen der Seiteneinrichtung an und speichert das Ergebnis als OFD-Dokument.

```csharp
using System;
using Aspose.Cells;

string dataDir = "C:\\Examples\\";

// Öffnen einer vorhandenen Excel-Arbeitsmappe von der Festplatte
Workbook workbook = new Workbook(dataDir + "SampleBook.xlsx");

// (1) Werte aus ausgewählten Zellen lesen und anzeigen, um zu bestätigen, dass die Datei geladen wurde
Worksheet firstSheet = workbook.Worksheets[0];
Console.WriteLine("First sheet name: " + firstSheet.Name);
Console.WriteLine("Cell A1: " + firstSheet.Cells["A1"].StringValue);
Console.WriteLine("Cell B1: " + firstSheet.Cells["B1"].StringValue);
Console.WriteLine("Cell C1: " + firstSheet.Cells["C1"].StringValue);

// (2) Über die Worksheets-Sammlung iterieren, um verfügbare Blätter aufzulisten
Console.WriteLine("\nAvailable worksheets:");
for (int i = 0; i < workbook.Worksheets.Count; i++)
{
    Worksheet ws = workbook.Worksheets[i];
    Console.WriteLine("  [" + i + "] " + ws.Name);
}

// (3) Optional eine Zeitstempelzelle aktualisieren, um die Konvertierung widerzuspiegeln
firstSheet.Cells["A1"].PutValue("Converted on: " + DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss"));

// Eine Zusammenfassungs-Kopfzeile oben am Datenblock einfügen
firstSheet.Cells.InsertRow(0);
firstSheet.Cells["A1"].PutValue("Conversion Summary");
firstSheet.Cells["A2"].PutValue("Generated: " + DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss"));

// (4) PageSetup-Eigenschaften auf dem Arbeitsblatt konfigurieren
PageSetup pageSetup = firstSheet.PageSetup;
pageSetup.Orientation = PageOrientationType.Landscape;
pageSetup.PaperSize = PaperSizeType.PaperA4;
pageSetup.FitToPagesTall = 1;
pageSetup.FitToPagesWide = 1;

// (5) Optional den Druckbereich für die OFD-Ausgabe festlegen
int lastRow = firstSheet.Cells.MaxDataRow;
int lastCol = firstSheet.Cells.MaxDataColumn;
string lastColLetter = CellsHelper.ColumnIndexToName(lastCol);
string printArea = "A1:" + lastColLetter + (lastRow + 1);
firstSheet.PageSetup.PrintArea = printArea;
Console.WriteLine("\nPrint area set to: " + printArea);

// (6) Die Arbeitsmappe als OFD-Datei speichern
workbook.Save(dataDir + "SampleBook.ofd", SaveFormat.Ofd);
Console.WriteLine("\nFile successfully converted to OFD format: " + dataDir + "SampleBook.ofd");
```

## **Verwandte Artikel**
- [Aufteilen von Excel-Dateien in mehrere Dateien](/cells/de/net/splitting-excel-files-into-multiple-files/)
- [Einfügen eines Bildes in eine Zelle](/cells/de/net/inserting-an-image-into-a-cell/)
- [Lesen und Schreiben von DBF-Dateien](/cells/de/net/dbf/)
- [Konvertieren einer Sparkline in Bild und HTML in Aspose.Cells for .Net](/cells/de/net/convert-sparkline-to-image-and-html/)
{{< app/cells/assistant language="csharp" >}}