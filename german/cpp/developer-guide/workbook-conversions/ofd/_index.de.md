---
title: Konvertieren von Excel in das OFD-Format
linktitle: Konvertieren von Excel in das OFD-Format
description: Aspose.Cells ist eine C++-Bibliothek zur Arbeit mit Tabellenkalkulationsdateien, die das Konvertieren von Excel-Arbeitsmappen in das OFD-Format (Open Fixed-layout Document) unterstützt. Dieser Artikel zeigt, wie Sie Excel-Inhalte erstellen und als OFD exportieren sowie wie Sie vorhandene Excel-Dateien mit Aspose.Cells in OFD konvertieren.
keywords: Aspose.Cells, C++-Bibliothek, Tabellenkalkulation, Excel zu OFD, OFD-Konvertierung, SaveFormat.Ofd, Fixed-Layout-Dokument, Arbeitsmappen-Export
type: docs
weight: 195
url: /de/cpp/converting-excel-to-ofd-format/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells unterstützt die direkte Konvertierung von Excel-Arbeitsmappen in das OFD-Format (Open Fixed-layout Document) unter Verwendung des Enumerationswerts `SaveFormat.Ofd`. Das resultierende OFD-Dokument bewahrt das sichtbare Layout der Arbeitsmappe, den Inhalt, verbundene Zellen, Spaltenbreiten, Zeilenhöhen, Schriftarten, Farben, Rahmen und Zahlenformate. Dies macht Aspose.Cells für die Archivierung, den Druck, regulatorische Einreichungen und Behördenübermittlungen geeignet, die eine Fixed-Layout-Ausgabe erfordern.

{{% /alert %}}
## **Einführung**
OFD (Open Fixed-layout Document) ist ein chinesischer nationaler Standard (GB/T 33190-2016) zur Darstellung digitaler Dokumente in einem festen, seitenbasierten Layout. Es erfüllt eine ähnliche Rolle wie PDF für Anwendungsfälle, in denen das visuelle Erscheinungsbild des Quelldokuments genau wie erstellt erhalten bleiben muss. OFD wird in der Volksrepublik China weitgehend für Behördenübermittlungen, regulatorische Einreichungen, elektronische Rechnungen und langfristige Archivierung verwendet.

Die Konvertierung von Excel-Arbeitsmappen in OFD ist eine häufige Anforderung in Szenarien, in denen Tabellenkalkulationsinhalte als schreibgeschütztes, layoutgesperrtes Artefakt verteilt werden müssen, anstatt als bearbeitbare Tabellenkalkulation. Beispiele umfassen das Versenden einer finalisierten Rechnung an einen Kunden, die Archivierung eines Quartalsfinanzberichts oder die Einreichung einer Budgettabelle bei einer Aufsichtsbehörde. Aspose.Cells adressiert diese Anforderung durch den Enumerationswert `SaveFormat.Ofd`, der die Arbeitsmappe direkt nach OFD schreibt, ohne einen Zwischenschritt zur Konvertierung zu erfordern. Die OFD-Ausgabe bewahrt Zellwerte, verbundene Bereiche, Schriftarten, Farben, Rahmen, Zahlenformate und Seiteneinrichtungsoptionen, die in der Arbeitsmappe konfiguriert sind.

{{% alert color="primary" %}}

Die von Aspose.Cells erzeugte OFD-Ausgabe bewahrt das sichtbare Layout der Quellarbeitsmappe, einschließlich Zellinhalten, verbundener Zellen, Spaltenbreiten und Zeilenhöhen. Zellenformatierungen wie Schriftarten, Farben, Rahmen, Ausrichtung und Zahlenformate werden ebenfalls in der Fixed-Layout-Ausgabe dargestellt. Die im Arbeitsblatt konfigurierten Seiteneinrichtungsoptionen wie Papierformat, Ausrichtung und Druckbereich beeinflussen das Layout des resultierenden OFD-Dokuments.

{{% /alert %}}
## **Erstellen einer Excel-Arbeitsmappe und Speichern als OFD**
Aspose.Cells ermöglicht es Ihnen, eine Arbeitsmappe programmatisch zu erstellen, sie mit Daten zu füllen und sie dann direkt unter Verwendung der Enumeration `SaveFormat.Ofd` im OFD-Format zu speichern. Das folgende Beispiel erstellt eine Rechnung von Grund auf. Es fügt ein Firmenlogo, Kopfinformationen, einen Rechnungsempfängerbereich, Positionen und berechnete Summen hinzu und exportiert dann die Arbeitsmappe in ein OFD-Dokument.
### **Erstellen einer Rechnung mit einem Logo**
Das Beispiel konstruiert ein Rechnungsarbeitsblatt, indem es ein Logobild in den oberen linken Bereich einfügt, den Firmennamen und die Kontaktdaten ausfüllt, einen "INVOICE"-Titel über verbundene Zellen hinzufügt, die Rechnungsnummer und das Datum erfasst, den Rechnungsempfänger auflistet, eine Positionstabelle mit Beschreibung-, Mengen-, Einzelpreis- und Gesamtspalten aufbaut und Zwischensumme, Steuer und Gesamtsumme mithilfe von Zellformeln berechnet. Formatierungen wie fettgedruckte Kopfzeilen, Währungsformat für Preise, Rahmen und Spaltenbreiten werden mithilfe von `Style`- und `Font`-Objekten angewendet. Schließlich wird die Arbeitsmappe mit der Erweiterung `.ofd` unter Verwendung von `SaveFormat.Ofd` gespeichert.

```cpp
// Aspose.Cells für C++ Beispiel
// Kompilieren mit Aspose.Cells 26.6.0 (oder höher) und einem C++17 (oder höher) Compiler

#include "Aspose.Cells.h"
#include <string>
#include <ctime>

using namespace Aspose::Cells;

int main()
{
    // Aspose.Cells initialisieren
    Aspose::Cells::Startup();

    // Verzeichnis für Ressourcen und Ausgabe
    const char16_t* dataDir = u"C:\\Temp\\";

    // Eine neue Arbeitsmappe erstellen
    Workbook workbook;

    // Das erste Arbeitsblatt abrufen
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Cells cells = worksheet.GetCells();

    // Spaltenbreiten festlegen
    cells.SetColumnWidth(0, 5.0);
    cells.SetColumnWidth(1, 35.0);
    cells.SetColumnWidth(2, 12.0);
    cells.SetColumnWidth(3, 15.0);
    cells.SetColumnWidth(4, 15.0);
    cells.SetColumnWidth(5, 5.0);

    // Firmenlogo einfügen
    worksheet.GetPictures().Add(1, 1, U16String(dataDir) + u"logo.png");

    // Firmenname und Kontaktdaten
    cells.Get(u"B3").PutValue(u"Acme Corporation");
    cells.Get(u"B4").PutValue(u"123 Business Street");
    cells.Get(u"B5").PutValue(u"City, State 12345");
    cells.Get(u"B6").PutValue(u"Phone: (555) 123-4567");

    // RECHNUNG Titel - Zellen zusammenführen
    cells.Merge(7, 1, 2, 4);
    Cell titleCell = cells.Get(u"B8");
    titleCell.PutValue(u"INVOICE");

    Style titleStyle = workbook.CreateStyle();
    titleStyle.GetFont().SetIsBold(true);
    titleStyle.GetFont().SetSize(20);
    titleStyle.SetHorizontalAlignment(TextAlignmentType::Center);
    titleCell.SetStyle(titleStyle);

    // Rechnungsnummer und Datum
    cells.Get(u"B11").PutValue(u"Invoice Number:");
    cells.Get(u"C11").PutValue(u"INV-2024-001");
    cells.Get(u"B12").PutValue(u"Date:");

    std::time_t t = std::time(nullptr);
    std::tm* now = std::localtime(&t);
    char dateBuffer[11];
    std::strftime(dateBuffer, sizeof(dateBuffer), "%Y-%m-%d", now);
    cells.Get(u"C12").PutValue(U16String(dateBuffer));

    // Rechnungsempfänger-Abschnitt
    cells.Get(u"B14").PutValue(u"Bill To:");
    cells.Get(u"B15").PutValue(u"Client Name");
    cells.Get(u"B16").PutValue(u"Client Address");
    cells.Get(u"B17").PutValue(u"Client City, State");

    // Positionsüberschrift
    Cell headerDesc = cells.Get(u"B19");
    Cell headerQty = cells.Get(u"C19");
    Cell headerPrice = cells.Get(u"D19");
    Cell headerTotal = cells.Get(u"E19");

    headerDesc.PutValue(u"Description");
    headerQty.PutValue(u"Quantity");
    headerPrice.PutValue(u"Unit Price");
    headerTotal.PutValue(u"Total");

    Style headerStyle = workbook.CreateStyle();
    headerStyle.GetFont().SetIsBold(true);
    headerStyle.GetFont().SetColor(Color::White());
    headerStyle.SetForegroundColor(Color{0, 0, 128});
    headerStyle.SetPattern(BackgroundType::Solid);
    headerStyle.SetHorizontalAlignment(TextAlignmentType::Center);
    headerStyle.GetBorders().Get(BorderType::TopBorder).SetLineStyle(CellBorderType::Thin);
    headerStyle.GetBorders().Get(BorderType::BottomBorder).SetLineStyle(CellBorderType::Thin);
    headerStyle.GetBorders().Get(BorderType::LeftBorder).SetLineStyle(CellBorderType::Thin);
    headerStyle.GetBorders().Get(BorderType::RightBorder).SetLineStyle(CellBorderType::Thin);

    headerDesc.SetStyle(headerStyle);
    headerQty.SetStyle(headerStyle);
    headerPrice.SetStyle(headerStyle);
    headerTotal.SetStyle(headerStyle);

    // Währungsstil mit Rahmen
    Style currencyStyle = workbook.CreateStyle();
    currencyStyle.SetCustom(u"\"$\"#,##0.00");
    currencyStyle.GetBorders().Get(BorderType::TopBorder).SetLineStyle(CellBorderType::Thin);
    currencyStyle.GetBorders().Get(BorderType::BottomBorder).SetLineStyle(CellBorderType::Thin);
    currencyStyle.GetBorders().Get(BorderType::LeftBorder).SetLineStyle(CellBorderType::Thin);
    currencyStyle.GetBorders().Get(BorderType::RightBorder).SetLineStyle(CellBorderType::Thin);

    // Einfacher Rahmenstil für Beschreibungs-/Mengenzellen
    Style borderStyle = workbook.CreateStyle();
    borderStyle.GetBorders().Get(BorderType::TopBorder).SetLineStyle(CellBorderType::Thin);
    borderStyle.GetBorders().Get(BorderType::BottomBorder).SetLineStyle(CellBorderType::Thin);
    borderStyle.GetBorders().Get(BorderType::LeftBorder).SetLineStyle(CellBorderType::Thin);
    borderStyle.GetBorders().Get(BorderType::RightBorder).SetLineStyle(CellBorderType::Thin);

    // Positionszeilen
    struct LineItem { const char16_t* desc; int qty; double price; };
    LineItem lineItems[] = {
        {u"Product A - Widget", 2, 50.00},
        {u"Product B - Gadget", 3, 75.00},
        {u"Product C - Service", 1, 100.00}
    };

    for (int i = 0; i < 3; i++)
    {
        int row = 20 + i;
        Cell descCell = cells.Get(row, 1);
        Cell qtyCell = cells.Get(row, 2);
        Cell priceCell = cells.Get(row, 3);
        Cell totalCell = cells.Get(row, 4);

        descCell.PutValue(lineItems[i].desc);
        qtyCell.PutValue(lineItems[i].qty);
        priceCell.PutValue(lineItems[i].price);

        std::string formula = "C" + std::to_string(row) + "*D" + std::to_string(row);
        totalCell.SetFormula(U16String(formula.c_str()));

        descCell.SetStyle(borderStyle);
        qtyCell.SetStyle(borderStyle);
        priceCell.SetStyle(currencyStyle);
        totalCell.SetStyle(currencyStyle);
    }

    // Zwischensumme, Steuer, Gesamtsumme
    cells.Get(u"B24").PutValue(u"Subtotal:");
    Cell subtotalCell = cells.Get(u"E24");
    subtotalCell.SetFormula(u"SUM(E20:E22)");

    cells.Get(u"B25").PutValue(u"Tax (10%):");
    Cell taxCell = cells.Get(u"E25");
    taxCell.SetFormula(u"E24*0.1");

    cells.Get(u"B26").PutValue(u"Grand Total:");
    Cell grandTotalCell = cells.Get(u"E26");
    grandTotalCell.SetFormula(u"E24+E25");

    // Fett + Währungsstil für Gesamtwerte
    Style totalStyle = workbook.CreateStyle();
    totalStyle.GetFont().SetIsBold(true);
    totalStyle.SetCustom(u"\"$\"#,##0.00");

    subtotalCell.SetStyle(totalStyle);
    taxCell.SetStyle(totalStyle);
    grandTotalCell.SetStyle(totalStyle);

    // Fettstil für Gesamtbeschriftungen
    Style boldStyle = workbook.CreateStyle();
    boldStyle.GetFont().SetIsBold(true);

    cells.Get(u"B24").SetStyle(boldStyle);
    cells.Get(u"B25").SetStyle(boldStyle);
    cells.Get(u"B26").SetStyle(boldStyle);

    // Die Arbeitsmappe als OFD-Datei speichern
    workbook.Save(U16String(dataDir) + u"Invoice.ofd", SaveFormat::Ofd);

    // Aspose.Cells-Ressourcen bereinigen
    Aspose::Cells::Cleanup();

    return 0;
}
```
## **Konvertieren einer vorhandenen Excel-Datei in OFD**
Aspose.Cells kann auch eine vorhandene Excel-Arbeitsmappe von der Festplatte laden und sie direkt in das OFD-Format exportieren. Dies ist nützlich für Batch-Konvertierungspipelines, Archivierungs-Workflows und Szenarien, in denen die Quellarbeitsmappe von einem anderen Tool erstellt wurde und nur als Fixed-Layout-Artefakt neu ausgegeben werden muss. Das folgende Beispiel lädt eine vorhandene `.xlsx`-Arbeitsmappe, liest Daten aus deren Zellen, wendet optionale Seiteneinrichtungsanpassungen an und speichert das Ergebnis als OFD-Dokument.

```cpp
#include "Aspose.Cells.h"
#include <string>
#include <iostream>
#include <ctime>

using namespace Aspose::Cells;

std::string GetCurrentTimestamp() {
    std::time_t t = std::time(nullptr);
    std::tm* now = std::localtime(&t);
    char buffer[20];
    std::strftime(buffer, sizeof(buffer), "%Y-%m-%d %H:%M:%S", now);
    return std::string(buffer);
}

int main() {
    Aspose::Cells::Startup();

    std::string dataDir = "C:\\Examples\\";

    // Eine bestehende Excel-Arbeitsmappe von der Festplatte öffnen
    Workbook workbook(U16String((dataDir + "SampleBook.xlsx").c_str()));

    // (1) Werte aus ausgewählten Zellen lesen und anzeigen, um zu bestätigen, dass die Datei geladen wurde
    Worksheet firstSheet = workbook.GetWorksheets().Get(0);
    U16String sheetName = firstSheet.GetName();
    Cell a1 = firstSheet.GetCells().Get(u"A1");
    Cell b1 = firstSheet.GetCells().Get(u"B1");
    Cell c1 = firstSheet.GetCells().Get(u"C1");

    std::cout << "First sheet name: " << sheetName.ToUtf8() << std::endl;
    std::cout << "Cell A1: " << a1.GetStringValue().ToUtf8() << std::endl;
    std::cout << "Cell B1: " << b1.GetStringValue().ToUtf8() << std::endl;
    std::cout << "Cell C1: " << c1.GetStringValue().ToUtf8() << std::endl;

    // (2) Über die Worksheets-Sammlung iterieren, um verfügbare Blätter aufzulisten
    std::cout << "\nAvailable worksheets:" << std::endl;
    WorksheetCollection sheets = workbook.GetWorksheets();
    int sheetCount = sheets.GetCount();
    for (int i = 0; i < sheetCount; ++i) {
        Worksheet ws = sheets.Get(i);
        U16String wsName = ws.GetName();
        std::cout << "  [" << i << "] " << wsName.ToUtf8() << std::endl;
    }

    // (3) Optional eine Zeitstempel-Zelle aktualisieren, um die Konvertierung widerzuspiegeln
    std::string timestamp1 = GetCurrentTimestamp();
    firstSheet.GetCells().Get(u"A1").PutValue(U16String(("Converted on: " + timestamp1).c_str()));

    // Eine Zusammenfassungs-Kopfzeile oben am Datenblock einfügen
    firstSheet.GetCells().InsertRow(0);
    firstSheet.GetCells().Get(u"A1").PutValue(u"Conversion Summary");

    std::string timestamp2 = GetCurrentTimestamp();
    firstSheet.GetCells().Get(u"A2").PutValue(U16String(("Generated: " + timestamp2).c_str()));

    // (4) PageSetup-Eigenschaften auf dem Arbeitsblatt konfigurieren
    PageSetup pageSetup = firstSheet.GetPageSetup();
    pageSetup.SetOrientation(PageOrientationType::Landscape);
    pageSetup.SetPaperSize(PaperSizeType::PaperA4);
    pageSetup.SetFitToPagesTall(1);
    pageSetup.SetFitToPagesWide(1);

    // (5) Optional den Druckbereich für die OFD-Ausgabe festlegen
    int lastRow = firstSheet.GetCells().GetMaxDataRow();
    int lastCol = firstSheet.GetCells().GetMaxDataColumn();
    U16String lastColLetter = CellsHelper::ColumnIndexToName(lastCol);
    std::string printArea = "A1:" + lastColLetter.ToUtf8() + std::to_string(lastRow + 1);
    firstSheet.GetPageSetup().SetPrintArea(U16String(printArea.c_str()));
    std::cout << "\nPrint area set to: " << printArea << std::endl;

    // (6) Die Arbeitsmappe als OFD-Datei speichern
    workbook.Save(U16String((dataDir + "SampleBook.ofd").c_str()), SaveFormat::Ofd);
    std::cout << "\nFile successfully converted to OFD format: " << dataDir << "SampleBook.ofd" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Verwandte Artikel**
- [Aufteilen von Excel-Dateien in mehrere Dateien](/cells/de/cpp/splitting-excel-files-into-multiple-files/)
- [Einfügen eines Bildes in eine Zelle](/cells/de/cpp/inserting-an-image-into-a-cell/)
- [Lesen und Schreiben von DBF-Dateien](/cells/de/cpp/dbf/)
- [Konvertieren von Sparklines in Bilder und HTML in Aspose.Cells for C++](/cells/de/cpp/convert-sparkline-to-image-and-html/)
{{< app/cells/assistant language="cpp" >}}