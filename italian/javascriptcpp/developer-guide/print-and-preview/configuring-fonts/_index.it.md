---
title: Configurazione dei caratteri per il rendering dei fogli di calcolo con JavaScript tramite C++
linktitle: Configurazione dei Font per la Visualizzazione dei Fogli di Lavoro
type: docs
weight: 10
url: /it/javascript-cpp/configuring-fonts-for-rendering-spreadsheets/
description: Impara come configurare i caratteri per il rendering dei fogli di calcolo usando Aspose.Cells for JavaScript tramite C++. Assicurati che i caratteri siano disponibili per una conversione ottimale.
---

## **Possibili Scenari di Utilizzo**

Le API di Aspose.Cells offrono la possibilità di rendere i fogli di calcolo in formati immagine e di convertirli in formati PDF & XPS. Per massimizzare la fedeltà della conversione, è necessario che i font usati nel foglio di calcolo siano disponibili nella directory font predefinita del sistema operativo. Se i font richiesti non sono presenti, le API di Aspose.Cells tenteranno di sostituirli con quelli disponibili.

## **Selezione dei font**

Di seguito il processo che le API di Aspose.Cells seguono dietro le quinte.

1. L'API cerca di trovare i font nel file system corrispondenti al nome esatto del font utilizzato nel foglio di calcolo.
1. Se l'API non riesce a trovare i font con lo stesso nome esatto, tenta di utilizzare il font predefinito specificato nella proprietà [**DefaultStyle.font**](https://reference.aspose.com/cells/javascript-cpp/style/#font--) del foglio di lavoro.
1. Se l'API non riesce a individuare il font definito nella proprietà [**DefaultStyle.font**](https://reference.aspose.com/cells/javascript-cpp/style/#font--) del foglio di lavoro, tenta di utilizzare il font specificato nelle proprietà [**PdfSaveOptions.defaultFont**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#defaultFont--) o [**ImageOrPrintOptions.defaultFont**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/#defaultFont--).
1. Se l'API non riesce a individuare il font definito nelle proprietà [**PdfSaveOptions.defaultFont**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#defaultFont--) o [**ImageOrPrintOptions.defaultFont**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/#defaultFont--), tenta di utilizzare il font specificato nella proprietà [**FontConfigs.defaultFontName**](https://reference.aspose.com/cells/javascript-cpp/fontconfigs/#defaultFontName--).
1. Se l'API non riesce a individuare il font definito nella proprietà [**FontConfigs.defaultFontName**](https://reference.aspose.com/cells/javascript-cpp/fontconfigs/#defaultFontName--), tenta di selezionare i font più adatti tra tutti i font disponibili.
1. Infine, se l'API non riesce a trovare alcun font nel file system, renderizza il foglio di calcolo utilizzando Arial.

## **Impostazione delle cartelle dei font personalizzate**

Le API di Aspose.Cells cercano i font richiesti nella directory font predefinita del sistema operativo. Se i font richiesti non sono disponibili, le API cercano nelle directory personalizzate (definite dall’utente). La classe [**FontConfigs**](https://reference.aspose.com/cells/javascript-cpp/fontconfigs) ha esposto diversi modi per impostare directory personalizzate dei font come dettagliato di seguito.

1. [**FontConfigs.fontFolder(string, boolean)**](https://reference.aspose.com/cells/javascript-cpp/fontconfigs/#fontFolder-string-boolean-): Questo metodo è utile se c'è solo una cartella da impostare.
1. [**FontConfigs.fontFolders(string[], boolean)**](https://reference.aspose.com/cells/javascript-cpp/fontconfigs/#fontFolders-stringarray-boolean-): Questo metodo è utile quando i font risiedono in più cartelle e l'utente desidera impostare tutte le cartelle separatamente anziché combinare tutti i font in una singola cartella.
1. [**FontConfigs.fontSources(FontSourceBase[])**](https://reference.aspose.com/cells/javascript-cpp/fontconfigs/#fontSources-fontsourcebasearray-): Questo meccanismo è utile quando l'utente desidera caricare i font da più cartelle o un singolo file font o dati font da un array di byte.

{{% alert color="primary" %}}

Sia i metodi [**FontConfigs.fontFolder(string, boolean)**](https://reference.aspose.com/cells/javascript-cpp/fontconfigs/#fontFolder-string-boolean-) che [**FontConfigs.fontFolders(string[], boolean)**](https://reference.aspose.com/cells/javascript-cpp/fontconfigs/#fontFolders-stringarray-boolean-) accettano un secondo parametro di tipo Boolean. Passare **true** come secondo parametro indirizzerà le API di Aspose.Cells a cercare i file dei font nelle sottocartelle.

{{% /alert %}}

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Font Configuration Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Font Configuration Example</h1>
        <p>Select an Excel file (optional) and font resources to configure Aspose.Cells font sources in the browser.</p>

        <label>Excel File (optional):</label>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <br/><br/>

        <label>Font File (.ttf/.otf) (optional):</label>
        <input type="file" id="fontFileInput" accept=".ttf,.otf" />
        <br/><br/>

        <label>Font Folder (optional, select a folder):</label>
        <input type="file" id="fontFolderInput" webkitdirectory directory multiple />
        <br/><br/>

        <button id="runExample">Configure Fonts</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Utils } = AsposeCells;

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
            const fontFileInput = document.getElementById('fontFileInput');
            const fontFolderInput = document.getElementById('fontFolderInput');
            const resultDiv = document.getElementById('result');

            // Basic validation: ensure at least one font resource is provided (file or folder)
            if (!fontFileInput.files.length && !fontFolderInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select at least one font file or a font folder.</p>';
                return;
            }

            // Defining string variables to store paths/names to font folders & font file
            // (In browser environment we use simple names or uploaded file names)
            const fontFolder1 = "Arial";
            const fontFolder2 = "Calibri";
            const fontFile = "arial.ttf";

            // Setting first font folder (converted from setFontFolder)
            AsposeCells.FontConfigs.fontFolder = fontFolder1;
            // Preserve the subfolder-search flag from original API call as a separate property
            AsposeCells.FontConfigs.fontFolderSearchSubFolders = true;

            // Setting both font folders (converted from setFontFolders)
            AsposeCells.FontConfigs.fontFolders = [fontFolder1, fontFolder2];
            // Preserve the subfolder-search flag as a separate property
            AsposeCells.FontConfigs.fontFoldersSearchSubFolders = false;

            // Defining FolderFontSource
            const sourceFolder = new AsposeCells.FolderFontSource(fontFolder1, false);

            // Defining FileFontSource
            const sourceFile = new AsposeCells.FileFontSource(fontFile);

            // Defining MemoryFontSource
            let memoryFontBytes = new Uint8Array([]);
            if (fontFileInput.files.length) {
                const ff = fontFileInput.files[0];
                const arrayBuffer = await ff.arrayBuffer();
                memoryFontBytes = new Uint8Array(arrayBuffer);
            } else if (fontFolderInput.files.length) {
                // If a folder was provided, try to find a .ttf/.otf inside it and use the first found
                const files = Array.from(fontFolderInput.files);
                const fontCandidate = files.find(f => f.name.toLowerCase().endsWith('.ttf') || f.name.toLowerCase().endsWith('.otf'));
                if (fontCandidate) {
                    const arrayBuffer = await fontCandidate.arrayBuffer();
                    memoryFontBytes = new Uint8Array(arrayBuffer);
                }
            }
            const sourceMemory = new AsposeCells.MemoryFontSource(memoryFontBytes);

            // Setting font sources (converted from setFontSources)
            AsposeCells.FontConfigs.fontSources = [sourceFolder, sourceFile, sourceMemory];

            // Provide feedback to the user
            resultDiv.innerHTML = '<p style="color: green;">Font configuration applied successfully.</p>';
        });
    </script>
</html>
```

{{% alert color="primary" %}}

Si prega di utilizzare uno qualsiasi dei metodi sopra menzionati all'inizio dell'applicazione, cioè; prima di invocare altri oggetti delle API di Aspose.Cells.

{{% /alert %}} {{% alert color="primary" %}}

Se tutti i metodi sopra menzionati vengono utilizzati per impostare le origini dei font, solo le ultime impostazioni avranno effetto.

{{% /alert %}}

## **Meccanismo di sostituzione del font**

Le API di Aspose.Cells offrono anche la possibilità di specificare il font di sostituzione per scopi di rendering. Questo meccanismo è utile quando un font richiesto non è disponibile sulla macchina utilizzata per la conversione. Gli utenti possono fornire una lista di nomi di font come alternativa al font originale. Per fare ciò, le API di Aspose.Cells hanno esposto il metodo [**FontConfigs.fontSubstitutes(string, string[])**](https://reference.aspose.com/cells/javascript-cpp/fontconfigs/#fontSubstitutes-string-stringarray-) che accetta 2 parametri. Il primo è di tipo **string**, indicante il nome del font da sostituire. Il secondo è un array di tipo **string**, nel quale gli utenti possono fornire una lista di nomi di font come sostituzione del font originale (specificato nel primo parametro).

Ecco uno scenario d'uso semplice.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Example Title</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Utils } = AsposeCells;

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

            // Instantiating a Workbook object by opening the Excel file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Substituting the Arial font with Times New Roman & Calibri
            // Converted from: AsposeCells.FontConfigs.setFontSubstitutes("Arial", ["Times New Roman", "Calibri"]);
            AsposeCells.FontConfigs.fontSubstitutes = { "Arial": ["Times New Roman", "Calibri"] };

            // Saving the (possibly modified) workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the processed file.</p>';
        });
    </script>
</html>
```

## **Raccolta informazioni**

Oltre ai metodi sopra menzionati, le API di Aspose.Cells forniscono anche strumenti per raccogliere informazioni sulle fonti e sostituzioni impostate.

1. Il metodo [**FontConfigs.fontSources**](https://reference.aspose.com/cells/javascript-cpp/fontconfigs/#fontSources--) restituisce un array di tipo [**FontSourceBase**](https://reference.aspose.com/cells/javascript-cpp/fontsourcebase) contenente l’elenco delle fonti specificate. Se nessuna fonte è stata impostata, il metodo [**FontConfigs.fontSources**](https://reference.aspose.com/cells/javascript-cpp/fontconfigs/#fontSources--) restituirà un array vuoto.
1. Il metodo [**FontConfigs.fontSubstitutes(string)**](https://reference.aspose.com/cells/javascript-cpp/fontconfigs/#fontSubstitutes-string-) accetta un parametro di tipo **string** per specificare il nome del font per il quale è stato impostato il substitution. Se non è stato impostato alcun substitution per il nome del font specificato, il metodo [**FontConfigs.fontSubstitutes(string)**](https://reference.aspose.com/cells/javascript-cpp/fontconfigs/#fontSubstitutes-string-) restituirà null.

## **Argomenti avanzati**
- [Imposta il carattere predefinito durante il rendering del foglio elettronico in immagini](/cells/it/javascript-cpp/set-default-font-while-rendering-spreadsheet-to-images/)
- [Imposta la proprietà DefaultFont di PdfSaveOptions e ImageOrPrintOptions per dare priorità](/cells/it/javascript-cpp/set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority/)
- [Formati di carattere supportati](/cells/it/javascript-cpp/supported-font-formats/)
- [Foglio elettronico in immagine - Imposta il formato pixel per l'immagine renderizzata](/cells/it/javascript-cpp/worksheet-to-image-set-pixel-format-for-the-rendered-image/)
