---
title: Konvertieren von Excel in das OFD-Format
linktitle: Konvertieren von Excel in das OFD-Format
description: Aspose.Cells for JavaScript via C++ ist eine JavaScript-Bibliothek zur Arbeit mit Tabellenkalkulationsdateien und unterstützt die Konvertierung von Excel-Arbeitsmappen in das OFD-Format (Open Fixed-layout Document). Dieser Artikel veranschaulicht, wie Excel-Inhalte erstellt und als OFD exportiert sowie vorhandene Excel-Dateien mithilfe von Aspose.Cells in das OFD-Format konvertiert werden.
keywords: Aspose.Cells, Aspose.Cells for JavaScript via C++, JavaScript-Bibliothek, Tabellenkalkulation, Excel-zu-OFD, OFD-Konvertierung, SaveFormat.Ofd, Dokument mit festem Layout, Export von Arbeitsmappen
type: docs
weight: 195
url: /de/javascript-cpp/converting-excel-to-ofd-format/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells unterstützt die direkte Konvertierung von Excel-Arbeitsmappen in das OFD-Format (Open Fixed-layout Document) mithilfe des Aufzählungswerts `SaveFormat.Ofd`. Das resultierende OFD-Dokument bewahrt das sichtbare Layout, den Inhalt, verbundene Zellen, Spaltenbreiten, Zeilenhöhen, Schriftarten, Farben, Rahmen und Zahlenformate der Arbeitsmappe. Dadurch eignet sich Aspose.Cells für Workflows zur Archivierung und zum Drucken sowie für regulatorische Meldungen und Behördenübermittlungen, die eine Ausgabe mit festem Layout erfordern.
{{% /alert %}}

## **Einführung**
OFD (Open Fixed-layout Document) ist ein chinesischer Nationalstandard (GB/T 33190-2016) zur Darstellung digitaler Dokumente in einem festen, seitenbasierten Layout. Es erfüllt eine dem PDF ähnliche Funktion in Anwendungsfällen, in denen das visuelle Erscheinungsbild des Quelldokuments exakt so erhalten bleiben muss, wie es erstellt wurde. OFD wird in der Volksrepublik China häufig für Behördenübermittlungen, regulatorische Meldungen und elektronische Rechnungen sowie zur langfristigen Archivierung verwendet.
Die Konvertierung von Excel-Arbeitsmappen in OFD ist in Szenarien häufig erforderlich, in denen Inhalte von Tabellenkalkulationsdateien nicht als bearbeitbare Tabelle, sondern als schreibgeschütztes Artefakt mit festem Layout verteilt werden müssen. Beispiele hierfür sind das Versenden einer endgültigen Rechnung an einen Kunden, die Archivierung eines vierteljährlichen Finanzberichts oder die Einreichung einer Budgettabelle bei einer Aufsichtsbehörde. Aspose.Cells erfüllt diese Anforderung mithilfe des Aufzählungswerts `SaveFormat.Ofd`, der die Arbeitsmappe direkt in das OFD-Format schreibt, ohne dass ein Zwischenschritt bei der Konvertierung erforderlich ist. Die OFD-Ausgabe bewahrt Zellwerte, verbundene Bereiche, Schriftarten, Farben, Rahmen, Zahlenformate und die auf der Arbeitsmappe konfigurierten Optionen für die Seiteneinrichtung.

{{% alert color="primary" %}}
Die von Aspose.Cells erzeugte OFD-Ausgabe bewahrt das sichtbare Layout der Quellarbeitsmappe, einschließlich Zelleninhalten, verbundener Zellen, Spaltenbreiten und Zeilenhöhen. Formatierungen von Zellen, etwa Schriftarten, Farben, Rahmen, Ausrichtung und Zahlenformate, werden ebenfalls in der Ausgabe mit festem Layout dargestellt. Auf dem Arbeitsblatt konfigurierte Optionen für die Seiteneinrichtung, etwa Papierformat, Ausrichtung und Druckbereich, beeinflussen das Layout des resultierenden OFD-Dokuments.
{{% /alert %}}

## **Erstellen einer Excel-Arbeitsmappe und Speichern im OFD-Format**
Mit Aspose.Cells können Sie eine Arbeitsmappe programmgesteuert erstellen, mit Daten befüllen und anschließend mithilfe des Aufzählungswerts `SaveFormat.Ofd` direkt im OFD-Format speichern. Das folgende Beispiel erstellt eine Rechnung von Grund auf. Es fügt ein Unternehmenslogo, Kopfangaben, einen Abschnitt für die Rechnungsempfängerangaben, Positionsposten und berechnete Summen hinzu und exportiert die Arbeitsmappe anschließend in ein OFD-Dokument.

### **Erstellen einer Rechnung mit einem Logo**
Das Beispiel erstellt ein Rechnungsarbeitsblatt, indem es ein Logobild oben links einfügt, den Unternehmensnamen und die Kontaktdaten ausfüllt, über verbundene Zellen den Titel „INVOICE“ hinzufügt, Rechnungsnummer und Datum erfasst, den Kunden als Rechnungsempfänger einträgt, eine Tabelle mit Positionsposten und den Spalten Beschreibung, Menge, Stückpreis und Gesamtpreis erstellt und mithilfe von Zellenformeln Zwischensumme, Steuer und Gesamtbetrag berechnet. Formatierungen wie fett formatierte Kopfzeilen, eine Währungsformatierung für Preise, Rahmen und Spaltenbreiten werden mithilfe von `Style`- und `Font`-Objekten angewendet. Schließlich wird die Arbeitsmappe unter Verwendung von `SaveFormat.Ofd` mit der Erweiterung `.ofd` gespeichert.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
        <script src="aspose.cells.js.min.js"></script>
        <script type="text/javascript">
        const { Workbook, Color } = AsposeCells;
        const readyPromise = AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            try {
                // Eine neue Arbeitsmappe erstellen
                const workbook = new Workbook();
                // Das erste Arbeitsblatt abrufen
                const worksheet = workbook.worksheets.get(0);
                const cells = worksheet.cells;
                // Spaltenbreiten festlegen
                cells.setColumnWidth(0, 5);
                cells.setColumnWidth(1, 35);
                cells.setColumnWidth(2, 12);
                cells.setColumnWidth(3, 15);
                cells.setColumnWidth(4, 15);
                cells.setColumnWidth(5, 5);
                // Firmenlogo einfügen
                // Ein PNG im Arbeitsspeicher erstellen, da der Browser keinen Dateisystempfad hat.
                const logoCanvas = document.createElement("canvas");
                logoCanvas.width = 100;
                logoCanvas.height = 30;
                const logoContext = logoCanvas.getContext("2d");
                logoContext.fillStyle = "#000080";
                logoContext.fillRect(0, 0, logoCanvas.width, logoCanvas.height);
                logoContext.fillStyle = "#FFFFFF";
                logoContext.font = "bold 18px Arial";
                logoContext.fillText("ACME", 16, 21);
                const logoBlob = await new Promise(resolve => logoCanvas.toBlob(resolve, "image/png"));
                if (!logoBlob) {
                    throw new Error("Unable to create the company logo.");
                }
                const logoData = new Uint8Array(await logoBlob.arrayBuffer());
                worksheet.pictures.add(1, 1, logoData);
                // Firmenname und Kontaktdaten
                cells.get("B3").value = "Acme Corporation";
                cells.get("B4").value = "123 Business Street";
                cells.get("B5").value = "City, State 12345";
                cells.get("B6").value = "Phone: (555) 123-4567";
                // INVOICE-Titel – Zellen zusammenführen
                cells.merge(7, 1, 2, 4);
                const titleCell = cells.get("B8");
                titleCell.value = "INVOICE";
                const titleStyle = workbook.createStyle();
                titleStyle.font.isBold = true;
                titleStyle.font.size = 20;
                titleStyle.horizontalAlignment = AsposeCells.TextAlignmentType.Center;
                titleCell.style = titleStyle;
                // Rechnungsnummer und Datum
                cells.get("B11").value = "Invoice Number:";
                cells.get("C11").value = "INV-2024-001";
                cells.get("B12").value = "Date:";
                const now = new Date();
                const invoiceDate = [
                    now.getFullYear(),
                    String(now.getMonth() + 1).padStart(2, "0"),
                    String(now.getDate()).padStart(2, "0")
                ].join("-");
                cells.get("C12").value = invoiceDate;
                // Abschnitt für den Rechnungsempfänger
                cells.get("B14").value = "Bill To:";
                cells.get("B15").value = "Client Name";
                cells.get("B16").value = "Client Address";
                cells.get("B17").value = "Client City, State";
                // Tabellenkopf der Positionszeilen
                const headerDesc = cells.get("B19");
                const headerQty = cells.get("C19");
                const headerPrice = cells.get("D19");
                const headerTotal = cells.get("E19");
                headerDesc.value = "Description";
                headerQty.value = "Quantity";
                headerPrice.value = "Unit Price";
                headerTotal.value = "Total";
                const headerStyle = workbook.createStyle();
                headerStyle.font.isBold = true;
                headerStyle.font.color = Color.fromArgb(255, 255, 255);
                headerStyle.foregroundColor = Color.fromArgb(0, 0, 128);
                headerStyle.pattern = AsposeCells.BackgroundType.Solid;
                headerStyle.horizontalAlignment = AsposeCells.TextAlignmentType.Center;
                headerStyle.borders.get(AsposeCells.BorderType.TopBorder).lineStyle = AsposeCells.CellBorderType.Thin;
                headerStyle.borders.get(AsposeCells.BorderType.BottomBorder).lineStyle = AsposeCells.CellBorderType.Thin;
                headerStyle.borders.get(AsposeCells.BorderType.LeftBorder).lineStyle = AsposeCells.CellBorderType.Thin;
                headerStyle.borders.get(AsposeCells.BorderType.RightBorder).lineStyle = AsposeCells.CellBorderType.Thin;
                headerDesc.style = headerStyle;
                headerQty.style = headerStyle;
                headerPrice.style = headerStyle;
                headerTotal.style = headerStyle;
                // Währungsformat mit Rahmen
                const currencyStyle = workbook.createStyle();
                currencyStyle.custom = '"$"#,##0.00';
                currencyStyle.borders.get(AsposeCells.BorderType.TopBorder).lineStyle = AsposeCells.CellBorderType.Thin;
                currencyStyle.borders.get(AsposeCells.BorderType.BottomBorder).lineStyle = AsposeCells.CellBorderType.Thin;
                currencyStyle.borders.get(AsposeCells.BorderType.LeftBorder).lineStyle = AsposeCells.CellBorderType.Thin;
                currencyStyle.borders.get(AsposeCells.BorderType.RightBorder).lineStyle = AsposeCells.CellBorderType.Thin;
                // Einfaches Rahmenformat für Beschreibungs- und Mengenzellen
                const borderStyle = workbook.createStyle();
                borderStyle.borders.get(AsposeCells.BorderType.TopBorder).lineStyle = AsposeCells.CellBorderType.Thin;
                borderStyle.borders.get(AsposeCells.BorderType.BottomBorder).lineStyle = AsposeCells.CellBorderType.Thin;
                borderStyle.borders.get(AsposeCells.BorderType.LeftBorder).lineStyle = AsposeCells.CellBorderType.Thin;
                borderStyle.borders.get(AsposeCells.BorderType.RightBorder).lineStyle = AsposeCells.CellBorderType.Thin;
                // Zeilen der Positionen
                const lineItems = [
                    ["Product A - Widget", 2, 50.00],
                    ["Product B - Gadget", 3, 75.00],
                    ["Product C - Service", 1, 100.00]
                ];
                for (let i = 0; i < lineItems.length; i++) {
                    const row = 20 + i;
                    const descCell = cells.get(row, 1);
                    const qtyCell = cells.get(row, 2);
                    const priceCell = cells.get(row, 3);
                    const totalCell = cells.get(row, 4);
                    descCell.value = lineItems[i][0];
                    qtyCell.value = lineItems[i][1];
                    priceCell.value = lineItems[i][2];
                    totalCell.formula = "C" + (row + 1) + "*D" + (row + 1);
                    descCell.style = borderStyle;
                    qtyCell.style = borderStyle;
                    priceCell.style = currencyStyle;
                    totalCell.style = currencyStyle;
                }
                // Zwischensumme, Steuer und Gesamtsumme
                cells.get("B24").value = "Subtotal:";
                const subtotalCell = cells.get("E24");
                subtotalCell.formula = "SUM(E21:E23)";
                cells.get("B25").value = "Tax (10%):";
                const taxCell = cells.get("E25");
                taxCell.formula = "E24*0.1";
                cells.get("B26").value = "Grand Total:";
                const grandTotalCell = cells.get("E26");
                grandTotalCell.formula = "E24+E25";
                // Fett gedrucktes Währungsformat für Summenwerte
                const totalStyle = workbook.createStyle();
                totalStyle.font.isBold = true;
                totalStyle.custom = '"$"#,##0.00';
                subtotalCell.style = totalStyle;
                taxCell.style = totalStyle;
                grandTotalCell.style = totalStyle;
                // Fett gedrucktes Format für Summenbeschriftungen
                const boldStyle = workbook.createStyle();
                boldStyle.font.isBold = true;
                cells.get("B24").style = boldStyle;
                cells.get("B25").style = boldStyle;
                cells.get("B26").style = boldStyle;
                // Arbeitsmappe als OFD-Datei speichern
                const outputData = workbook.save(AsposeCells.SaveFormat.Ofd);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById('downloadLink');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "Invoice.ofd";
                downloadLink.style.display = "block";
                document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            } catch (error) {
                console.error(error);
                document.getElementById('result').innerHTML = '<p style="color: red;">An error occurred: ' + error.message + '</p>';
            }
        });
        </script>
    </body>
</html>
```

## **Konvertieren einer vorhandenen Excel-Datei in das OFD-Format**
Aspose.Cells kann außerdem eine vorhandene Excel-Arbeitsmappe von der Festplatte laden und sie direkt in das OFD-Format exportieren. Dies ist für Batch-Konvertierungspipelines, Archivierungsworkflows und Szenarien nützlich, in denen die Quellarbeitsmappe von einem anderen Werkzeug erstellt wurde und lediglich erneut in ein Artefakt mit festem Layout exportiert werden muss. Das folgende Beispiel lädt eine vorhandene `.xlsx`-Arbeitsmappe, liest Daten aus ihren Zellen, nimmt optionale Anpassungen an der Seiteneinrichtung vor und speichert das Ergebnis als OFD-Dokument.

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8" />
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
        <script src="aspose.cells.js.min.js"></script>
        <script type="text/javascript">
            const { Workbook, CellsHelper } = AsposeCells;
            const fileInput = document.getElementById("fileInput");
            const runButton = document.getElementById("runExample");
            const downloadLink = document.getElementById("downloadLink");
            const result = document.getElementById("result");
            const readyPromise = AsposeCells.onReady({
                license: "/lic/aspose.cells.enc",
                fontPath: "/fonts/",
                fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
            }).then(() => {
                console.log("Aspose.Cells initialized");
            });
            function formatTimestamp(date) {
                const pad = value => String(value).padStart(2, "0");
                return date.getFullYear() + "-" +
                    pad(date.getMonth() + 1) + "-" +
                    pad(date.getDate()) + " " +
                    pad(date.getHours()) + ":" +
                    pad(date.getMinutes()) + ":" +
                    pad(date.getSeconds());
            }
            function escapeHtml(value) {
                const entities = {
                    "&": "&amp;",
                    "<": "&lt;",
                    ">": "&gt;",
                    '"': "&quot;",
                    "'": "&#39;"
                };
                return String(value).replace(/[&<>"']/g, character => entities[character]);
            }
            runButton.addEventListener("click", async () => {
                try {
                    const file = fileInput.files[0];
                    if (!file) {
                        result.innerHTML = '<p style="color: red;">Please select an Excel file first.</p>';
                        return;
                    }
                    runButton.disabled = true;
                    downloadLink.style.display = "none";
                    downloadLink.removeAttribute("href");
                    // Eine vorhandene Excel-Arbeitsmappe von der Festplatte öffnen
                    const workbook = new Workbook(new Uint8Array(await file.arrayBuffer()));
                    // (1) Werte aus ausgewählten Zellen lesen und anzeigen, um zu bestätigen, dass die Datei geladen wurde
                    const firstSheet = workbook.worksheets.get(0);
                    const cells = firstSheet.cells;
                    const output = [];
                    output.push("First sheet name: " + firstSheet.name);
                    output.push("Cell A1: " + cells.get("A1").stringValue);
                    output.push("Cell B1: " + cells.get("B1").stringValue);
                    output.push("Cell C1: " + cells.get("C1").stringValue);
                    // (2) Über die Worksheets-Sammlung iterieren, um die verfügbaren Blätter aufzulisten
                    output.push("");
                    output.push("Available worksheets:");
                    for (let i = 0; i < workbook.worksheets.count; i++) {
                        const ws = workbook.worksheets.get(i);
                        output.push("  [" + i + "] " + ws.name);
                    }
                    // (3) Optional eine Zeitstempelzelle aktualisieren, um die Konvertierung widerzuspiegeln
                    cells.get("A1").value = "Converted on: " + formatTimestamp(new Date());
                    // Eine Zusammenfassungs-Kopfzeile oben im Datenblock einfügen
                    cells.insertRow(0);
                    cells.get("A1").value = "Conversion Summary";
                    cells.get("A2").value = "Generated: " + formatTimestamp(new Date());
                    // (4) PageSetup-Eigenschaften für das Arbeitsblatt konfigurieren
                    const pageSetup = firstSheet.pageSetup;
                    pageSetup.orientation = AsposeCells.PageOrientationType.Landscape;
                    pageSetup.paperSize = AsposeCells.PaperSizeType.PaperA4;
                    pageSetup.fitToPagesTall = 1;
                    pageSetup.fitToPagesWide = 1;
                    // (5) Optional den Druckbereich für die OFD-Ausgabe festlegen
                    const lastRow = cells.maxDataRow;
                    const lastCol = cells.maxDataColumn;
                    const lastColLetter = CellsHelper.columnIndexToName(lastCol);
                    const printArea = "A1:" + lastColLetter + (lastRow + 1);
                    pageSetup.printArea = printArea;
                    output.push("");
                    output.push("Print area set to: " + printArea);
                    // (6) Die Arbeitsmappe als OFD-Datei speichern
                    const outputData = workbook.save(AsposeCells.SaveFormat.Ofd);
                    const blob = new Blob([outputData]);
                    downloadLink.href = URL.createObjectURL(blob);
                    downloadLink.download = "SampleBook.ofd";
                    downloadLink.textContent = "Download SampleBook.ofd";
                    downloadLink.style.display = "block";
                    output.push("");
                    output.push("File successfully converted to OFD format: SampleBook.ofd");
                    result.innerHTML =
                        '<pre style="white-space: pre-wrap;">' +
                        escapeHtml(output.join("\n")) +
                        "</pre>" +
                        '<p style="color: green;">Done! Click the download link to get the result file.</p>';
                } catch (error) {
                    console.error(error);
                    const message = error && error.message ? error.message : String(error);
                    result.innerHTML = '<p style="color: red;">Error: ' + escapeHtml(message) + "</p>";
                } finally {
                    runButton.disabled = false;
                }
            });
        </script>
    </body>
</html>
```

## **Verwandte Artikel**

{{< app/cells/assistant language="javascript-cpp" >}}