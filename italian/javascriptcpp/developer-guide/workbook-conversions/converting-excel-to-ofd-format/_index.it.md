---
title: Conversione da Excel al formato OFD
linktitle: Conversione da Excel al formato OFD
description: Aspose.Cells for JavaScript via C++ è una libreria JavaScript per la gestione di file di foglio di calcolo che supporta la conversione delle cartelle di lavoro Excel nel formato OFD (Open Fixed-layout Document). Questo articolo dimostra come creare contenuti in Excel ed esportarli in OFD, nonché come convertire i file Excel esistenti in OFD utilizzando Aspose.Cells.
keywords: Aspose.Cells, Aspose.Cells for JavaScript via C++, libreria JavaScript, foglio di calcolo, conversione da Excel a OFD, conversione in OFD, SaveFormat.Ofd, documento a layout fisso, esportazione di cartelle di lavoro
type: docs
weight: 195
url: /it/javascript-cpp/converting-excel-to-ofd-format/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells supporta la conversione diretta delle cartelle di lavoro Excel nel formato OFD (Open Fixed-layout Document) utilizzando il valore di enumerazione `SaveFormat.Ofd`. Il documento OFD risultante preserva il layout visibile della cartella di lavoro, il contenuto, le celle unite, le larghezze delle colonne, le altezze delle righe, i tipi di carattere, i colori, i bordi e i formati numerici. Questo rende Aspose.Cells adatto ai flussi di lavoro di archiviazione, stampa, presentazione alle autorità di vigilanza e invio alle autorità governative che richiedono un output con layout fisso.
{{% /alert %}}

## **Introduzione**
OFD (Open Fixed-layout Document) è uno standard nazionale cinese (GB/T 33190-2016) per la rappresentazione di documenti digitali con un layout fisso basato su pagine. Svolge un ruolo analogo a quello di PDF nei casi in cui l'aspetto visivo del documento di origine deve essere preservato esattamente come definito dall'autore. OFD è utilizzato diffusamente per gli invii alle autorità governative, le presentazioni alle autorità di vigilanza, le fatture elettroniche e l'archiviazione a lungo termine nella Repubblica Popolare Cinese.
La conversione delle cartelle di lavoro Excel in OFD è un requisito comune in scenari in cui il contenuto del foglio di calcolo deve essere distribuito come artefatto di sola lettura con layout bloccato anziché come foglio di calcolo modificabile. Tra gli esempi vi sono l'invio di una fattura finalizzata a un cliente, l'archiviazione di un rapporto finanziario trimestrale e la presentazione di un foglio di calcolo del budget a un'autorità di vigilanza. Aspose.Cells soddisfa questo requisito tramite il valore di enumerazione `SaveFormat.Ofd`, che scrive la cartella di lavoro direttamente nel formato OFD senza richiedere un passaggio di conversione intermedio. L'output OFD preserva i valori delle celle, gli intervalli uniti, i tipi di carattere, i colori, i bordi, i formati numerici e le impostazioni di pagina configurate nella cartella di lavoro.

{{% alert color="primary" %}}
L'output OFD generato da Aspose.Cells preserva il layout visibile della cartella di lavoro di origine, inclusi il contenuto delle celle, le celle unite, le larghezze delle colonne e le altezze delle righe. Anche la formattazione delle celle, come i tipi di carattere, i colori, i bordi, l'allineamento e i formati numerici, viene riprodotta nell'output con layout fisso. Le impostazioni di pagina configurate nel foglio di lavoro, come il formato della carta, l'orientamento e l'area di stampa, influenzano il layout del documento OFD risultante.
{{% /alert %}}

## **Creazione di una cartella di lavoro Excel e salvataggio in OFD**
Aspose.Cells consente di costruire una cartella di lavoro a livello programmatico, riempirla di dati e quindi salvarla direttamente nel formato OFD utilizzando l'enumerazione `SaveFormat.Ofd`. L'esempio seguente crea una fattura da zero. Aggiunge il logo aziendale, i dati di intestazione, una sezione dedicata al destinatario, le voci della fattura e i totali calcolati, quindi esporta la cartella di lavoro in un documento OFD.

### **Costruzione di una fattura con logo**
L'esempio costruisce un foglio di lavoro per una fattura inserendo un'immagine del logo nell'area in alto a sinistra, quindi riportando il nome dell'azienda e i dettagli di contatto, aggiungendo il titolo «INVOICE» su celle unite, registrando il numero e la data della fattura, elencando il cliente destinatario, costruendo una tabella delle voci con le colonne descrizione, quantità, prezzo unitario e totale e calcolando il subtotale, l'imposta e il totale complessivo mediante formule applicate alle celle. La formattazione, come le intestazioni in grassetto, il formato valuta per i prezzi, i bordi e le larghezze delle colonne, viene applicata tramite gli oggetti `Style` e `Font`. Infine, la cartella di lavoro viene salvata con l'estensione `.ofd` utilizzando `SaveFormat.Ofd`.

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
                // Crea un nuovo Workbook
                const workbook = new Workbook();
                // Ottieni il primo foglio di lavoro
                const worksheet = workbook.worksheets.get(0);
                const cells = worksheet.cells;
                // Imposta la larghezza delle colonne
                cells.setColumnWidth(0, 5);
                cells.setColumnWidth(1, 35);
                cells.setColumnWidth(2, 12);
                cells.setColumnWidth(3, 15);
                cells.setColumnWidth(4, 15);
                cells.setColumnWidth(5, 5);
                // Inserisci il logo dell'azienda
                // Crea un PNG in memoria perché il browser non ha un percorso del filesystem.
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
                // Nome dell'azienda e dettagli di contatto
                cells.get("B3").value = "Acme Corporation";
                cells.get("B4").value = "123 Business Street";
                cells.get("B5").value = "City, State 12345";
                cells.get("B6").value = "Phone: (555) 123-4567";
                // Titolo "INVOICE" - unisci le celle
                cells.merge(7, 1, 2, 4);
                const titleCell = cells.get("B8");
                titleCell.value = "INVOICE";
                const titleStyle = workbook.createStyle();
                titleStyle.font.isBold = true;
                titleStyle.font.size = 20;
                titleStyle.horizontalAlignment = AsposeCells.TextAlignmentType.Center;
                titleCell.style = titleStyle;
                // Numero fattura e data
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
                // Sezione del destinatario
                cells.get("B14").value = "Bill To:";
                cells.get("B15").value = "Client Name";
                cells.get("B16").value = "Client Address";
                cells.get("B17").value = "Client City, State";
                // Intestazione delle voci
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
                // Stile valuta con bordi
                const currencyStyle = workbook.createStyle();
                currencyStyle.custom = '"$"#,##0.00';
                currencyStyle.borders.get(AsposeCells.BorderType.TopBorder).lineStyle = AsposeCells.CellBorderType.Thin;
                currencyStyle.borders.get(AsposeCells.BorderType.BottomBorder).lineStyle = AsposeCells.CellBorderType.Thin;
                currencyStyle.borders.get(AsposeCells.BorderType.LeftBorder).lineStyle = AsposeCells.CellBorderType.Thin;
                currencyStyle.borders.get(AsposeCells.BorderType.RightBorder).lineStyle = AsposeCells.CellBorderType.Thin;
                // Stile bordo semplice per le celle di descrizione/quantità
                const borderStyle = workbook.createStyle();
                borderStyle.borders.get(AsposeCells.BorderType.TopBorder).lineStyle = AsposeCells.CellBorderType.Thin;
                borderStyle.borders.get(AsposeCells.BorderType.BottomBorder).lineStyle = AsposeCells.CellBorderType.Thin;
                borderStyle.borders.get(AsposeCells.BorderType.LeftBorder).lineStyle = AsposeCells.CellBorderType.Thin;
                borderStyle.borders.get(AsposeCells.BorderType.RightBorder).lineStyle = AsposeCells.CellBorderType.Thin;
                // Righe delle voci
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
                // Subtotale, imposta, totale complessivo
                cells.get("B24").value = "Subtotal:";
                const subtotalCell = cells.get("E24");
                subtotalCell.formula = "SUM(E21:E23)";
                cells.get("B25").value = "Tax (10%):";
                const taxCell = cells.get("E25");
                taxCell.formula = "E24*0.1";
                cells.get("B26").value = "Grand Total:";
                const grandTotalCell = cells.get("E26");
                grandTotalCell.formula = "E24+E25";
                // Stile grassetto e valuta per i valori totali
                const totalStyle = workbook.createStyle();
                totalStyle.font.isBold = true;
                totalStyle.custom = '"$"#,##0.00';
                subtotalCell.style = totalStyle;
                taxCell.style = totalStyle;
                grandTotalCell.style = totalStyle;
                // Stile grassetto per le etichette dei totali
                const boldStyle = workbook.createStyle();
                boldStyle.font.isBold = true;
                cells.get("B24").style = boldStyle;
                cells.get("B25").style = boldStyle;
                cells.get("B26").style = boldStyle;
                // Salva il workbook come file OFD
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

## **Conversione di un file Excel esistente in OFD**
Aspose.Cells può anche caricare una cartella di lavoro Excel esistente dal disco ed esportarla direttamente nel formato OFD. Ciò è utile per le pipeline di conversione per lotti, per i flussi di lavoro di archiviazione e per gli scenari in cui la cartella di lavoro di origine è stata prodotta da un altro strumento e deve essere semplicemente riesportata come artefatto a layout fisso. L'esempio seguente carica una cartella di lavoro `.xlsx` esistente, legge i dati dalle celle, applica eventuali modifiche facoltative alle impostazioni di pagina e salva il risultato come documento OFD.

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
                    // Aprire una cartella di lavoro Excel esistente dal disco
                    const workbook = new Workbook(new Uint8Array(await file.arrayBuffer()));
                    // (1) Leggere e visualizzare i valori delle celle selezionate per confermare che il file è stato caricato
                    const firstSheet = workbook.worksheets.get(0);
                    const cells = firstSheet.cells;
                    const output = [];
                    output.push("First sheet name: " + firstSheet.name);
                    output.push("Cell A1: " + cells.get("A1").stringValue);
                    output.push("Cell B1: " + cells.get("B1").stringValue);
                    output.push("Cell C1: " + cells.get("C1").stringValue);
                    // (2) Iterare sulla raccolta Worksheets per enumerare i fogli disponibili
                    output.push("");
                    output.push("Available worksheets:");
                    for (let i = 0; i < workbook.worksheets.count; i++) {
                        const ws = workbook.worksheets.get(i);
                        output.push("  [" + i + "] " + ws.name);
                    }
                    // (3) Facoltativamente aggiornare una cella timestamp per riflettere la conversione
                    cells.get("A1").value = "Converted on: " + formatTimestamp(new Date());
                    // Aggiungere una riga di intestazione riassuntiva nella parte superiore del blocco di dati
                    cells.insertRow(0);
                    cells.get("A1").value = "Conversion Summary";
                    cells.get("A2").value = "Generated: " + formatTimestamp(new Date());
                    // (4) Configurare le proprietà PageSetup nel foglio di lavoro
                    const pageSetup = firstSheet.pageSetup;
                    pageSetup.orientation = AsposeCells.PageOrientationType.Landscape;
                    pageSetup.paperSize = AsposeCells.PaperSizeType.PaperA4;
                    pageSetup.fitToPagesTall = 1;
                    pageSetup.fitToPagesWide = 1;
                    // (5) Facoltativamente impostare l'area di stampa per l'output OFD
                    const lastRow = cells.maxDataRow;
                    const lastCol = cells.maxDataColumn;
                    const lastColLetter = CellsHelper.columnIndexToName(lastCol);
                    const printArea = "A1:" + lastColLetter + (lastRow + 1);
                    pageSetup.printArea = printArea;
                    output.push("");
                    output.push("Print area set to: " + printArea);
                    // (6) Salvare la cartella di lavoro come file OFD
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

## **Articoli correlati**
- [Inserimento di un'immagine in una cella](/cells/it/javascript-cpp/inserting-an-image-into-a-cell/)

{{< app/cells/assistant language="javascript-cpp" >}}