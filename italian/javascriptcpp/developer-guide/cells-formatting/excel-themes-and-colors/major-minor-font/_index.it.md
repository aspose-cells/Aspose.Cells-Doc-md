---
title: Tema dei Titoli e del Testo
linktitle: Tema dei Titoli e del Testo
description: Aspose.Cells è una libreria JavaScript via C++ per lavorare con file di fogli di calcolo. Supporta la configurazione dei font di tema per intestazioni e corpo nei documenti Excel, permettendo agli utenti di personalizzare l aspetto e lo stile del documento. Questo articolo introdurrà come usare la libreria Aspose.Cells per lavorare con i font di tema di intestazioni e corpo nei documenti Excel.
keywords: Aspose.Cells, Documento Excel, Intestazione, Corpo, Font del tema, Aspetto, Stile, JavaScript via C++
type: docs
weight: 120
url: /it/javascript-cpp/headings-and-body-theme-font/
---

{{% alert color="primary" %}}

Il font predefinito cambierà automaticamente quando viene modificata l'impostazione della regione.

Se viene modificato il font predefinito, verrà modificata anche l'altezza della riga e la larghezza della colonna, e potrebbe persino disordinare la disposizione della pagina.

Cos'ha causato il cambiamento del font predefinito?

Se il font del tema di Excel è impostato, Excel passerà automaticamente tra diversi font in base all'ambiente linguistico corrente.

{{% /alert %}}

## **Titoli e Corpo del Tema del Testo in Excel**

In Excel, seleziona la scheda Home, clicca sulla casella a discesa del carattere, vedrai "Caratteri del tema" con due caratteri di tema: Calibri Light (Intestazioni) e Calibri (Corpo) nella parte superiore con impostazione della regione in inglese.

**![Font del Tema](Theme-Fonts.png)**

Se è selezionato il Carattere del tema, il nome del carattere verrà visualizzato diversamente in diverse regioni. Se non vuoi che il carattere cambi automaticamente nelle diverse regioni, non selezionare i due caratteri del tema.

## **Modifica dei font di intestazioni e corpo tramite codice**
Con Aspose.Cells for JavaScript via C++, possiamo verificare se il font predefinito è un font del tema o impostare il font del tema con il metodo [**Font.schemeType**](https://reference.aspose.com/cells/javascript-cpp/font/#schemeType-fontschemetype-).

Il codice di esempio seguente mostra come manipolare il carattere del tema.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Change Theme Font Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, FontSchemeType, Utils } = AsposeCells;

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

            // Accessing and modifying the default style and its font scheme
            let defaultStyle = workbook.defaultStyle;
            let font = defaultStyle.font;
            let schemeType = font.schemeType;

            if (schemeType === FontSchemeType.Major || schemeType === FontSchemeType.Minor) {
                console.log("It's theme font");
            }

            // Change theme font to normal font
            font.schemeType = FontSchemeType.None;

            // Assign the modified default style back to the workbook
            workbook.defaultStyle = defaultStyle;

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Book1.modified.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Theme font changed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```



## **Ottieni dinamicamente il font del tema locale tramite codice**
A volte, i nostri server e i computer degli utenti non si trovano nella stessa regione. Come possiamo ottenere lo stesso font desiderato dagli utenti per l'elaborazione dei file?

Dobbiamo impostare le impostazioni regionali del sistema prima di caricare il file con il metodo [**LoadOptions.region**](https://reference.aspose.com/cells/javascript-cpp/loadoptions/#region-countrycode-).

Il codice di esempio seguente mostra come ottenere il font del tema locale.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Get Default Style Local Font Example</h1>
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

            // Instantiate a new LoadOptions.
            const options = new AsposeCells.LoadOptions();
            // Sets the customer's region
            options.region = AsposeCells.CountryCode.Japan;

            // Instantiate a new Workbook using the uploaded file and load options.
            const workbook = new Workbook(new Uint8Array(arrayBuffer), options);

            // Get the default style
            const defaultStyle = workbook.defaultStyle;

            // Gets customer's local font.
            const localFontName = defaultStyle.font.name;

            resultDiv.innerHTML = `<p style="color: green;">Local font name: ${localFontName}</p>`;
        });
    </script>
</html>
```
