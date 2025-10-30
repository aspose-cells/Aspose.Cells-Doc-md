---
title: Modificare uno stile esistente
linktitle: Modificare uno stile esistente
description: Aspose.Cells è una libreria per JavaScript via C++ che consente di lavorare con file di fogli di calcolo permettendo agli utenti di modificare gli stili delle celle esistenti. Questo articolo introdurrà come modificare uno stile di cella esistente con Aspose.Cells in modo che gli utenti possano cambiare l aspetto delle celle secondo necessità.
keywords: Modificare stili esistenti, personalizzare l aspetto e la sensazione della tua applicazione, guide, tutorial, documentazione di aiuto, documentazione di sviluppo, riferimenti API, codice di esempio, download, supporto.
type: docs
weight: 90
url: /it/javascript-cpp/modify-an-existing-style/
---

{{% alert color="primary" %}}

Per applicare le stesse opzioni di formattazione alle celle, creare un nuovo oggetto di stile di formattazione. Un oggetto di stile di formattazione è una combinazione di caratteristiche di formattazione, come font, dimensione del font, rientro, numero, bordo, pattern, ecc., denominati e memorizzati come un insieme. Quando applicato, tutte le formattazioni in quel formato vengono applicate.

È anche possibile utilizzare uno stile esistente, salvarlo con il foglio di lavoro e utilizzarlo per formattare le informazioni con gli stessi attributi.

Quando le celle non sono esplicitamente formattate, viene applicato lo stile **Normale** (lo stile predefinito del foglio di lavoro). Microsoft Excel predefinisce diversi stili oltre allo stile Normale, tra cui Virgola, Valuta e Percentuale.

Aspose.Cells consente di modificare uno qualsiasi di questi stili o qualsiasi altro stile che si definisce con i propri attributi desiderati.

{{% /alert %}}

## **Utilizzando Microsoft Excel**

Per aggiornare uno stile in Microsoft Excel 97-2003:

1. Nel menu **Formato**, fare clic su **Stile**.
1. Selezionare lo stile che si desidera modificare dall'elenco **Nome stile**.
1. Fare clic su **Modifica**.
1. Selezionare le opzioni di stile desiderate utilizzando le schede nella finestra di dialogo Formato celle.
1. Fai clic su **OK**.
1. In **Lo stile include**, specificare le caratteristiche dello stile desiderate.
1. Fare clic su **OK** per salvare lo stile e applicarlo all'intervallo selezionato.

## **Utilizzando Aspose.Cells for JavaScript via C++**

Gli esempi seguenti dimostrano come utilizzare il metodo [**Style.update()**](https://reference.aspose.com/cells/javascript-cpp/style/#update--).

### **Creazione e modifica di uno stile**

Questo esempio crea un oggetto [**Style**](https://reference.aspose.com/cells/javascript-cpp/style), lo applica a un intervallo di celle e modifica l'oggetto [**Style**](https://reference.aspose.com/cells/javascript-cpp/style). Le modifiche vengono applicate automaticamente alle celle e all'intervallo a cui lo stile è stato applicato.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
        <meta charset="utf-8" />
    </head>
    <body>
        <h1>Aspose.Cells Style Example</h1>
        <p>Select an existing Excel file to modify or leave empty to create a new workbook.</p>
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
            const resultDiv = document.getElementById('result');

            // Instantiate workbook from uploaded file or create a new one
            let workbook;
            if (fileInput.files && fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Create a new style object.
            const style = workbook.createStyle();

            // Set the number format.
            style.number = 14;

            // Set the font color to red color.
            style.font.color = AsposeCells.Color.Red;

            // Name the style.
            style.name = "Date1";

            // Get the first worksheet cells.
            const cells = workbook.worksheets.get(0).cells;

            // Specify the style (described above) to A1 cell.
            const cellA1 = cells.get("A1");
            cellA1.style = style;

            // Create a range (B1:D1).
            const range = cells.createRange("B1", "D1");

            // Initialize styleflag object.
            const flag = new AsposeCells.StyleFlag();

            // Set all formatting attributes on.
            flag.all = true;

            // Apply the style (described above) to the range.
            range.applyStyle(style, flag);

            // Modify the style (described above) and change the font color from red to black.
            style.font.color = AsposeCells.Color.Black;

            // Done! Since the named style (described above) has been set to a cell and range, 
            // The change would be reflected(new modification is implemented) to cell(A1) and 
            // Range (B1:D1).
            style.update();

            // Save the excel file. 
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book_styles.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```


### **Modifica di uno stile esistente**

Questo esempio utilizza un semplice file di modello Excel in cui è già stato applicato uno stile chiamato Percentuale a un intervallo. L'esempio:

1. ottiene lo stile,
1. crea un oggetto stile e
1. modifica la formattazione dello stile.

Le modifiche vengono applicate automaticamente all'intervallo a cui è stato applicato lo stile.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Apply Named Style Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Color, Utils } = AsposeCells;

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

            // Create a workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the named style "Percent" via the styles collection
            const style = workbook.styles.get("Percent");

            // Change the number format to "0.00%".
            style.number = 11;

            // Set the font color.
            style.font.color = Color.Red;

            // Update the style so ranges using this named style are updated.
            style.update();

            // Save the workbook and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book2.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Style updated successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
