---
title: Ottenere intestazioni o piè di pagina con JavaScript tramite C++
linktitle: Ottenere Intestazioni o Piè di Pagina
type: docs
weight: 30
url: /it/javascript-cpp/get-headers-or-footers/
description: Questo articolo spiega come ottenere programmaticamente intestazioni e piè di pagina da file Excel o OpenOffice utilizzando l API JavaScript tramite C++.
---

{{% alert color="primary" %}}

Le intestazioni e i piè di pagina vengono visualizzati solo nella visualizzazione Layout di pagina, Anteprima di stampa e sulle pagine stampate. 

È inoltre possibile utilizzare la finestra di dialogo Imposta pagina se si desidera visualizzare le intestazioni o i piè di pagina per più di un foglio di lavoro alla volta. 

Per altri tipi di fogli, come fogli grafico o grafici, è possibile inserire solo intestazioni e piè di pagina utilizzando la finestra di dialogo Imposta pagina.

{{% /alert %}}

## **Ottenere Intestazioni e Piè di Pagina in MS Excel**
1. Fare clic sul foglio di lavoro dove si desidera visualizzare o modificare le intestazioni o i piè di pagina.
2. Nella scheda Visualizza, nel gruppo Visualizzazioni cartella di lavoro, clicca su Layout di pagina.
   Excel visualizza il foglio di lavoro in vista Layout di pagina.
3. Per visualizzare o modificare un'intestazione o un piè di pagina, fare clic sulla casella di testo intestazione o piè di pagina a sinistra, al centro o a destra nella parte superiore o inferiore della pagina del foglio di lavoro (sotto Intestazione o sopra Piè di pagina).


## **Ottenere intestazioni e piè di pagina utilizzando Aspose.Cells for JavaScript tramite C++**
Con i metodi [**PageSetup.header(number)**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#header-number-) e [**PageSetup.footer(number)**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#footer-number-), gli sviluppatori JavaScript possono semplicemente ottenere intestazioni o piè di pagina dal file.

1. Costruisci una cartella di lavoro per aprire il file.
2. Ottieni il foglio di lavoro in cui vuoi ottenere intestazioni o piè di pagina.
3. Ottieni l'intestazione o il piè di pagina con un ID di sezione specifico.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Header/Footer Reader Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell, Utils } = AsposeCells;

        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });

        function escapeHtml(str) {
            if (str === null || str === undefined) return '';
            return String(str)
                .replace(/&/g, '&amp;')
                .replace(/</g, '&lt;')
                .replace(/>/g, '&gt;')
                .replace(/"/g, '&quot;')
                .replace(/'/g, '&#039;');
        }

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate a new Workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));
            const sheet = workbook.worksheets.get(0);

            // Gets left section of header
            const headerLeft = sheet.pageSetup.header(0);
            // Gets center section of header
            const headerCenter = sheet.pageSetup.header(1);
            // Gets right section of header
            const headerRight = sheet.pageSetup.header(2);
            // Gets center section of footer
            const footerCenter = sheet.pageSetup.footer(1);

            const resultHtml = [
                `<p><strong>Left Header:</strong> ${escapeHtml(headerLeft)}</p>`,
                `<p><strong>Center Header:</strong> ${escapeHtml(headerCenter)}</p>`,
                `<p><strong>Right Header:</strong> ${escapeHtml(headerRight)}</p>`,
                `<p><strong>Center Footer:</strong> ${escapeHtml(footerCenter)}</p>`
            ].join('');

            document.getElementById('result').innerHTML = resultHtml;
        });
    </script>
</html>
```

## **Analizza Intestazioni e Piè di Pagina in elenco di comandi**
Il testo dell'intestazione o del piè di pagina può contenere comandi speciali, ad esempio un segnaposto per il numero di pagina, la data corrente o attributi di formattazione del testo.

I comandi speciali sono rappresentati da una singola lettera con un carattere 'e commerciale' iniziale ("&").

Le stringhe di intestazione e piè di pagina sono costruite usando la grammatica ABNF. Non è facile da capire senza un visualizzatore.

Aspose.Cells for JavaScript tramite C++ fornisce il metodo [**PageSetup.commands(string)**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#commands-string-) per analizzare intestazioni e piè di pagina come lista di comandi.

I seguenti codici mostrano come analizzare l'intestazione o il piè di pagina come lista di comandi e processare i comandi:

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Header/Footer Commands Example</title>
    </head>
    <body>
        <h1>Header/Footer Commands Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell, Utils } = AsposeCells;

        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate a Workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));
            const sheet = workbook.worksheets.get(0);

            // Gets left section of header
            const headerSection = sheet.pageSetup.header(0);
            const commands = sheet.pageSetup.commands(headerSection) || [];

            const items = [];
            commands.forEach(c => {
                const type = c.type;
                switch (type) {
                    case AsposeCells.HeaderFooterCommandType.SheetName:
                        // embedded the name of the sheet to header or footer
                        items.push('<li>SheetName command found (embeds sheet name)</li>');
                        break;
                    default:
                        items.push(`<li>Command type: ${type}</li>`);
                        break;
                }
            });

            if (!items.length) {
                items.push('<li>No header/footer commands found.</li>');
            }

            resultDiv.innerHTML = `<ul>${items.join('')}</ul>`;

            // Save the (possibly unchanged) workbook and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'HeaderFooter_result.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Result Workbook';
        });
    </script>
</html>
```
