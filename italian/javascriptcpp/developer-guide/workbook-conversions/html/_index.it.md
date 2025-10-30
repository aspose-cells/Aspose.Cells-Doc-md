---
title: HTML con JavaScript tramite C++
linktitle: HTML
type: docs
weight: 230
url: /it/javascript-cpp/convert-excel-to-html/
---

## **Conversione di un Workbook Excel in HTML**
L’API Aspose.Cells supporta l’esportazione di fogli di calcolo in formato HTML. Per questo scopo, Aspose.Cells utilizza la classe [**HtmlSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions) per fornire la flessibilità di controllare vari aspetti dell’HTML di output.

 L'esempio di codice di seguito mostra come salvare un workbook come file HTML usando JavaScript tramite C++:

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells - Convert Excel to HTML</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Convert to HTML</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;

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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Saving the workbook to HTML format
            const outputData = workbook.save(SaveFormat.Html);
            const blob = new Blob([outputData], { type: 'text/html' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.html';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download HTML File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Conversion completed! Click the download link to get the HTML file.</p>';
        });
    </script>
</html>
```


## **Conversione della cartella di lavoro Excel in file MHTML**
MHTML combina HTML normale con risorse esterne (ovvero contenuti collegati come immagini, animazioni, audio, ecc.) in un unico file. Sono usati per email con estensione .mht. Aspose.Cells supporta la lettura e la scrittura di file MHTML.

 L'esempio di codice di seguito mostra come salvare un workbook come file MHTML usando JavaScript tramite C++:

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Save as MHT</title>
    </head>
    <body>
        <h1>Save Excel as MHT Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;

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

            // Load your source workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Save file to MHT format
            const outputData = workbook.save(SaveFormat.MHtml);
            const blob = new Blob([outputData], { type: 'application/octet-stream' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.mht';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download MHT File';

            resultDiv.innerHTML = '<p style="color: green;">File converted to MHT successfully! Click the download link to get the result.</p>';
        });
    </script>
</html>
```

## **Argomenti avanzati**
- [Adatta automaticamente colonne e righe durante il caricamento di HTML in Workbook](/cells/it/javascript-cpp/autofit-columns-and-rows-while-loading-html-in-workbook/)
- [Evitare la notazione esponenziale per i grandi numeri durante l'importazione da HTML](/cells/it/javascript-cpp/avoid-exponential-notation-of-large-numbers-while-importing/)
- [Modifica il Tipo di Destinazione del Link HTML](/cells/it/javascript-cpp/change-the-html-link-target-type/)
- [Convertire Excel in HTML con tooltip](/cells/it/javascript-cpp/convert-excel-to-html-with-tooltip/)
- [Create Transparent Image of Excel Worksheet](/cells/it/javascript-cpp/create-transparent-image-of-excel-worksheet/)
- [Eliminare gli spazi ridondanti dopo un'interruzione di riga durante l'importazione di HTML](/cells/it/javascript-cpp/delete-redundant-spaces-after-line-break-while-importing/)
- [Disabilita i Commenti Rivelati di Basso Livello durante il Salvataggio in HTML](/cells/it/javascript-cpp/disable-downlevel-revealed-comments-while-saving-to/)
- [Disabilita l'Esportazione di Script Frame e Proprietà del Documento](/cells/it/javascript-cpp/disable-exporting-frame-scripts-and-document-properties/)
- [Excel to HTML - Utilizzare l'Opzione PresentationPreference per una Migliore Impaginazione](/cells/it/javascript-cpp/excel-to-html-use-presentationpreference-option-for-better-layout/)
- [Escludere Stili Non Utilizzati durante la conversione da Excel a HTML](/cells/it/javascript-cpp/exclude-unused-styles-during-excel-to-html-conversion/)
- [Espansione del testo da destra a sinistra durante l'esportazione di un file Excel in HTML](/cells/it/javascript-cpp/expanding-text-from-right-to-left-while-exporting-excel-file-to/)
- [Esportazione di formattazioni condizionali DataBar, ColorScale e IconSet durante la conversione da Excel in HTML](/cells/it/javascript-cpp/export-databar-colorscale-and-iconset-conditional-formatting-while-excel-to-html-conversion/)
- [Esporta commenti durante il salvataggio del file di Excel in HTML](/cells/it/javascript-cpp/export-comments-while-saving-excel-file-to/)
- [Esportare le Proprietà del Documento Workbook e del Foglio di Lavoro nella conversione da Excel a HTML](/cells/it/javascript-cpp/export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion/)
- [Esportare Excel in HTML con linee della griglia](/cells/it/javascript-cpp/export-excel-to-html-with-gridlines/)
- [Esportare l'intervallo dell'area di stampa in HTML](/cells/it/javascript-cpp/export-print-area-range-to/)
- [Esporta uno stile di bordo simile quando lo stile di bordo non è supportato dai browser Web](/cells/it/javascript-cpp/export-similar-border-style-when-border-style-is-not-supported-by-web-browsers/)
- [Esportare il Foglio di Stile CSS Separatamente nell'HTML di Output](/cells/it/javascript-cpp/export-worksheet-css-separately-in-output/)
- [Nascondere il Contenuto Sovrapposto con CrossHideRight durante il salvataggio in HTML](/cells/it/javascript-cpp/hiding-overlaid-content-with-crosshideright-while-saving-to/)
- [Prefisso degli stili degli elementi della tabella con la proprietà HtmlSaveOptions.TableCssId](/cells/it/javascript-cpp/prefix-table-elements-styles-with-htmlsaveoptions-tablecssid-property/)
- [Impedire l'Esportazione dei Contenuti dei Fogli Nascosti al Salvataggio in HTML](/cells/it/javascript-cpp/prevent-exporting-hidden-worksheet-contents-on-saving-to/)
- [Fornire il percorso del file HTML del foglio di lavoro esportato tramite l'interfaccia IFilePathProvider](/cells/it/javascript-cpp/provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface/)
- [Riconoscere i Tag di Chiusura Automatica](/cells/it/javascript-cpp/recognise-self-closing-tags/)
- [Rendere il Riempimento a Gradiente per WordArt durante la Conversione di Fogli di Calcolo in HTML](/cells/it/javascript-cpp/render-gradient-fill-for-the-wordart-while-converting-spreadsheets-to/)
- [Imposta la larghezza della colonna su un'unità scalabile come em o percentuale](/cells/it/javascript-cpp/set-column-width-to-scalable-unit-like-em-or-percent/)
- [Imposta il carattere predefinito durante la rendering del foglio di calcolo in HTML](/cells/it/javascript-cpp/set-default-font-while-rendering-spreadsheet-to/)
- [Specifica come attraversare la stringa nell'output HTML utilizzando HtmlCrossType](/cells/it/javascript-cpp/specify-how-to-cross-string-in-output-html-using-htmlcrosstype/)
- [Supporta il layout dei tag DIV durante il caricamento di HTML nell'oggetto foglio di calcolo Excel](/cells/it/javascript-cpp/support-the-layout-of-div-tags-while-loading-html-to-excel-workbook/)

- [Abilita le Proprietà CSS Personalizzate durante il salvataggio in HTML](/cells/it/javascript-cpp/enable-css-custom-properties-while-saving-to-html/)
