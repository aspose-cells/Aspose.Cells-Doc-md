---
title: Konvertering av Excel till OFD-format
linktitle: Konvertering av Excel till OFD-format
description: Aspose.Cells for JavaScript via C++ är ett JavaScript-bibliotek för arbete med kalkylarksfiler som stöder konvertering av Excel-arbetsböcker till OFD-formatet (Open Fixed-layout Document). Den här artikeln visar hur du skapar Excel-innehåll och exporterar det som OFD, samt hur du konverterar befintliga Excel-filer till OFD med hjälp av Aspose.Cells.
keywords: Aspose.Cells, Aspose.Cells for JavaScript via C++, JavaScript-bibliotek, kalkylark, Excel till OFD, OFD-konvertering, SaveFormat.Ofd, dokument med fast layout, export av arbetsbok
type: docs
weight: 195
url: /sv/javascript-cpp/converting-excel-to-ofd-format/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells stöder direkt konvertering av Excel-arbetsböcker till OFD-formatet (Open Fixed-layout Document) med hjälp av uppräkningsvärdet `SaveFormat.Ofd`. Det resulterande OFD-dokumentet bevarar arbetsbokens synliga layout, innehåll, sammanfogade celler, kolumnbredder, radhöjder, teckensnitt, färger, ramar och talformat. Därmed lämpar sig Aspose.Cells för arbetsflöden för arkivering, tryckning, regulatoriska inlämningar och myndighetsinlämningar som kräver utdata med fast layout.
{{% /alert %}}

## **Introduktion**
OFD (Open Fixed-layout Document) är en kinesisk nationell standard (GB/T 33190-2016) för att representera digitala dokument med en fast, sidbaserad layout. OFD fyller samma roll som PDF i användningsfall där källodumentets visuella utseende måste bevaras exakt som det är utformat. OFD används i stor utsträckning för myndighetsinlämningar, regulatoriska inlämningar, elektroniska fakturor och långtidsarkivering i Folkrepubliken Kina.
Konvertering av Excel-arbetsböcker till OFD är ett vanligt behov i situationer där kalkylarksinnehåll måste distribueras som ett skrivskyddat, layoutlåst dokument i stället för som ett redigerbart kalkylblad. Exempel är att skicka en färdig faktura till en kund, arkivera en kvartalsvis finansiell rapport eller lämna in ett budgetkalkylblad till en tillsynsmyndighet. Aspose.Cells hanterar detta behov med uppräkningsvärdet `SaveFormat.Ofd`, som skriver arbetsboken direkt till OFD utan ett mellanliggande konverteringssteg. OFD-utdatan bevarar cellvärden, sammanfogade intervall, teckensnitt, färger, ramar, talformat och sidinställningar som har konfigurerats på arbetsboken.

{{% alert color="primary" %}}
OFD-utdata som skapas av Aspose.Cells bevarar källarbetsbokens synliga layout, inklusive cellinnehåll, sammanfogade celler, kolumnbredder och radhöjder. Cellformatering, till exempel teckensnitt, färger, ramar, justering och talformat, återges också i utdatan med fast layout. Sidinställningar som har konfigurerats i kalkylbladet, till exempel pappersstorlek, orientering och utskriftsområde, påverkar det resulterande OFD-dokumentets layout.
{{% /alert %}}

## **Skapa en Excel-arbetsbok och spara som OFD**
Aspose.Cells låter dig skapa en arbetsbok programmatiskt, fylla i den med data och sedan spara den direkt i OFD-format med hjälp av uppräkningsvärdet `SaveFormat.Ofd`. Det följande exemplet skapar en faktura från grunden med en företagslogotyp, rubrikuppgifter, ett avsnitt med fakturamottagare, fakturarader och beräknade summor. Arbetsboken exporteras sedan till ett OFD-dokument.

### **Bygga en faktura med en logotyp**
Exemplet skapar ett fakturakalkylblad. En logotypbild infogas i det övre vänstra hörnet, företagets namn och kontaktuppgifter fylls i och en "FAKTURA"-rubrik läggs till över sammanfogade celler. Därefter anges fakturanummer och datum, fakturamottagaren listas och en tabell skapas med kolumnerna beskrivning, antal, enhetspris och totalt för fakturaraderna. Delsumma, moms och totalsumma beräknas med cellformler. Formatering, till exempel fetstilta rubriker, valutaformat för priser, ramar och kolumnbredder, tillämpas med hjälp av objekten `Style` och `Font`. Slutligen sparas arbetsboken med filnamnstillägget `.ofd` med hjälp av `SaveFormat.Ofd`.

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
                // Skapa en ny arbetsbok
                const workbook = new Workbook();
                // Hämta det första kalkylarket
                const worksheet = workbook.worksheets.get(0);
                const cells = worksheet.cells;
                // Ange kolumnbredder
                cells.setColumnWidth(0, 5);
                cells.setColumnWidth(1, 35);
                cells.setColumnWidth(2, 12);
                cells.setColumnWidth(3, 15);
                cells.setColumnWidth(4, 15);
                cells.setColumnWidth(5, 5);
                // Infoga företagets logotyp
                // Skapa en PNG i minnet eftersom webbläsaren inte har någon filsystemsökväg.
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
                // Företagsnamn och kontaktuppgifter
                cells.get("B3").value = "Acme Corporation";
                cells.get("B4").value = "123 Business Street";
                cells.get("B5").value = "City, State 12345";
                cells.get("B6").value = "Phone: (555) 123-4567";
                // INVOICE-titel - sammanfoga celler
                cells.merge(7, 1, 2, 4);
                const titleCell = cells.get("B8");
                titleCell.value = "INVOICE";
                const titleStyle = workbook.createStyle();
                titleStyle.font.isBold = true;
                titleStyle.font.size = 20;
                titleStyle.horizontalAlignment = AsposeCells.TextAlignmentType.Center;
                titleCell.style = titleStyle;
                // Fakturanummer och datum
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
                // Avsnitt för betalningsmottagare
                cells.get("B14").value = "Bill To:";
                cells.get("B15").value = "Client Name";
                cells.get("B16").value = "Client Address";
                cells.get("B17").value = "Client City, State";
                // Rubrik för fakturarader
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
                // Valutastil med ramar
                const currencyStyle = workbook.createStyle();
                currencyStyle.custom = '"$"#,##0.00';
                currencyStyle.borders.get(AsposeCells.BorderType.TopBorder).lineStyle = AsposeCells.CellBorderType.Thin;
                currencyStyle.borders.get(AsposeCells.BorderType.BottomBorder).lineStyle = AsposeCells.CellBorderType.Thin;
                currencyStyle.borders.get(AsposeCells.BorderType.LeftBorder).lineStyle = AsposeCells.CellBorderType.Thin;
                currencyStyle.borders.get(AsposeCells.BorderType.RightBorder).lineStyle = AsposeCells.CellBorderType.Thin;
                // Enkel ramstil för beskrivnings- och antalsceller
                const borderStyle = workbook.createStyle();
                borderStyle.borders.get(AsposeCells.BorderType.TopBorder).lineStyle = AsposeCells.CellBorderType.Thin;
                borderStyle.borders.get(AsposeCells.BorderType.BottomBorder).lineStyle = AsposeCells.CellBorderType.Thin;
                borderStyle.borders.get(AsposeCells.BorderType.LeftBorder).lineStyle = AsposeCells.CellBorderType.Thin;
                borderStyle.borders.get(AsposeCells.BorderType.RightBorder).lineStyle = AsposeCells.CellBorderType.Thin;
                // Fakturarader
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
                // Delsumma, skatt och totalsumma
                cells.get("B24").value = "Subtotal:";
                const subtotalCell = cells.get("E24");
                subtotalCell.formula = "SUM(E21:E23)";
                cells.get("B25").value = "Tax (10%):";
                const taxCell = cells.get("E25");
                taxCell.formula = "E24*0.1";
                cells.get("B26").value = "Grand Total:";
                const grandTotalCell = cells.get("E26");
                grandTotalCell.formula = "E24+E25";
                // Fetstil + valutastil för totalvärden
                const totalStyle = workbook.createStyle();
                totalStyle.font.isBold = true;
                totalStyle.custom = '"$"#,##0.00';
                subtotalCell.style = totalStyle;
                taxCell.style = totalStyle;
                grandTotalCell.style = totalStyle;
                // Fetstil för totaletiketter
                const boldStyle = workbook.createStyle();
                boldStyle.font.isBold = true;
                cells.get("B24").style = boldStyle;
                cells.get("B25").style = boldStyle;
                cells.get("B26").style = boldStyle;
                // Spara arbetsboken som en OFD-fil
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

## **Konvertera en befintlig Excel-fil till OFD**
Aspose.Cells kan också läsa in en befintlig Excel-arbetsbok från disken och exportera den direkt till OFD-formatet. Det är användbart i flöden för batchkonvertering och arkivering samt i situationer där källarbetsboken har skapats med ett annat verktyg och endast behöver exporteras på nytt som en artefakt med fast layout. Det följande exemplet läser in en befintlig `.xlsx`-arbetsbok, läser data från dess celler, tillämpar valfria justeringar av sidinställningarna och sparar resultatet som ett OFD-dokument.

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
                    // Öppna en befintlig Excel-arbetsbok från disken
                    const workbook = new Workbook(new Uint8Array(await file.arrayBuffer()));
                    // (1) Läs och visa värden från valda celler för att bekräfta att filen har lästs in
                    const firstSheet = workbook.worksheets.get(0);
                    const cells = firstSheet.cells;
                    const output = [];
                    output.push("First sheet name: " + firstSheet.name);
                    output.push("Cell A1: " + cells.get("A1").stringValue);
                    output.push("Cell B1: " + cells.get("B1").stringValue);
                    output.push("Cell C1: " + cells.get("C1").stringValue);
                    // (2) Iterera över Worksheets-samlingen för att lista tillgängliga kalkylblad
                    output.push("");
                    output.push("Available worksheets:");
                    for (let i = 0; i < workbook.worksheets.count; i++) {
                        const ws = workbook.worksheets.get(i);
                        output.push("  [" + i + "] " + ws.name);
                    }
                    // (3) Uppdatera vid behov en tidsstämpelcell för att återspegla konverteringen
                    cells.get("A1").value = "Converted on: " + formatTimestamp(new Date());
                    // Lägg till en sammanfattningsrubrikrad överst i datablocket
                    cells.insertRow(0);
                    cells.get("A1").value = "Conversion Summary";
                    cells.get("A2").value = "Generated: " + formatTimestamp(new Date());
                    // (4) Konfigurera PageSetup-egenskaper för kalkylbladet
                    const pageSetup = firstSheet.pageSetup;
                    pageSetup.orientation = AsposeCells.PageOrientationType.Landscape;
                    pageSetup.paperSize = AsposeCells.PaperSizeType.PaperA4;
                    pageSetup.fitToPagesTall = 1;
                    pageSetup.fitToPagesWide = 1;
                    // (5) Ange vid behov utskriftsområdet för OFD-utdata
                    const lastRow = cells.maxDataRow;
                    const lastCol = cells.maxDataColumn;
                    const lastColLetter = CellsHelper.columnIndexToName(lastCol);
                    const printArea = "A1:" + lastColLetter + (lastRow + 1);
                    pageSetup.printArea = printArea;
                    output.push("");
                    output.push("Print area set to: " + printArea);
                    // (6) Spara arbetsboken som en OFD-fil
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

## **Relaterade artiklar**
- [Infoga en bild i en cell](/cells/sv/javascript-cpp/inserting-an-image-into-a-cell/)

{{< app/cells/assistant language="javascript-cpp" >}}