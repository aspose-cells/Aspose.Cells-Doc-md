---
title: Formattare celle con JavaScript tramite C++
description: Impara come formattare e stilizzare le celle in Aspose.Cells for JavaScript tramite C++, inclusi formattazione numeri, formattazione date, stili di carattere e altre opzioni di stile delle celle. La nostra guida ti aiuterà a creare fogli di calcolo attraenti e dall aspetto professionale.
keywords: Aspose.Cells for JavaScript tramite C++, formattazione celle, styling, formattazione numeri, formattazione date, stile carattere, opzioni di stile delle celle, foglio di calcolo, creare, aspetto professionale, formattare righe e colonne.
linktitle: Formattare celle
type: docs
weight: 120
url: /it/javascript-cpp/cells-formatting/
---

## **Introduzione**

{{% alert color="primary" %}}

Aspose.Cells fornisce i metodi [**style**](https://reference.aspose.com/cells/javascript-cpp/cell/#style--) e [**style**](https://reference.aspose.com/cells/javascript-cpp/cell/#style-style-) della classe [Cell](https://reference.aspose.com/cells/javascript-cpp/cell), usati per ottenere/impostare lo stile di formattazione di una cella. Aspose.Cells fornisce anche una classe [**Style**](https://reference.aspose.com/cells/javascript-cpp/style).

{{% /alert %}}

## **Come formattare le celle usando i metodi di stile**

Applicare diversi tipi di stili di formattazione alle celle per impostare colori di sfondo o primo piano, bordi, caratteri, allineamenti orizzontali e verticali, livello di rientro, direzione del testo, angolo di rotazione e molto altro.

### **Come usare i metodi di stile**

Se gli sviluppatori devono applicare stili di formattazione diversi a diverse celle, è meglio ottenere [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) della cella usando il metodo [**Cell.style**](https://reference.aspose.com/cells/javascript-cpp/cell/#style--), specificare gli attributi di stile e poi applicare la formattazione usando il metodo [**Cell.style**](https://reference.aspose.com/cells/javascript-cpp/cell/#style-style-). Un esempio viene mostrato di seguito per dimostrare questo approccio di applicazione di varie formattazioni su una cella.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Styling Example</h1>
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

            // Instantiate or load workbook
            let workbook;
            if (fileInput.files && fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Obtaining the reference of the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Accessing the "A1" cell from the worksheet
            const cell = worksheet.cells.get("A1");

            // Adding some value to the "A1" cell
            cell.value = "Hello Aspose!";

            // Defining a Style object
            let style;

            // Get the style from A1 cell
            style = cell.style;

            // Setting the vertical alignment
            style.verticalAlignment = AsposeCells.TextAlignmentType.Center;

            // Setting the horizontal alignment
            style.horizontalAlignment = AsposeCells.TextAlignmentType.Center;

            // Setting the font color of the text
            style.font.color = AsposeCells.Color.Green;

            // Setting to shrink according to the text contained in it
            style.shrinkToFit = true;

            // Setting the bottom border color to red
            style.borders.get(AsposeCells.BorderType.BottomBorder).color = AsposeCells.Color.Red;

            // Setting the bottom border type to medium
            style.borders.get(AsposeCells.BorderType.BottomBorder).lineStyle = AsposeCells.CellBorderType.Medium;

            // Applying the style to A1 cell
            cell.style = style;

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### **Come utilizzare l'oggetto stile per formattare celle diverse**

Se gli sviluppatori devono applicare lo stesso stile di formattazione a celle diverse, possono utilizzare l'oggetto [**Style**](https://reference.aspose.com/cells/javascript-cpp/style). Seguire i passaggi di seguito per usare l'oggetto [**Style**](https://reference.aspose.com/cells/javascript-cpp/style):

1. Aggiungere un oggetto [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) chiamando il metodo [**createStyle()**](https://reference.aspose.com/cells/javascript-cpp/workbook/#createStyle--) della classe [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)
2. Accedere all'oggetto [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) appena aggiunto
3. Impostare le proprietà/attributi desiderati dell'oggetto [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) per applicare le impostazioni di formattazione desiderate
4. Assegnare l'oggetto [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) configurato alle celle desiderate

Questo approccio può migliorare notevolmente l'efficienza delle tue applicazioni e risparmiare memoria anche.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Create Workbook and Style Cells</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, TextAlignmentType, Color, BorderType, CellBorderType } = AsposeCells;

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
            // Instantiate a new Workbook
            const workbook = new Workbook();

            // Add a new worksheet to the workbook
            const i = workbook.worksheets.add();

            // Obtain the newly added worksheet by index
            const worksheet = workbook.worksheets.get(i);

            // Access cell A1
            const cell = worksheet.cells.get("A1");

            // Set value of A1
            cell.value = "Hello Aspose!";

            // Create a new style
            const style = workbook.createStyle();

            // Set vertical and horizontal alignment
            style.verticalAlignment = TextAlignmentType.Center;
            style.horizontalAlignment = TextAlignmentType.Center;

            // Set font color
            style.font.color = Color.Green;

            // Shrink to fit
            style.shrinkToFit = true;

            // Set bottom border color and style
            style.borders.get(BorderType.BottomBorder).color = Color.Red;
            style.borders.get(BorderType.BottomBorder).lineStyle = CellBorderType.Medium;

            // Apply style to A1
            cell.style = style;

            // Apply same style to B1, C1, D1
            worksheet.cells.get("B1").style = style;
            worksheet.cells.get("C1").style = style;
            worksheet.cells.get("D1").style = style;

            // Save workbook to XLS format and provide download link
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and styled successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

### **Come utilizzare gli stili predefiniti di Microsoft Excel 2007**

Se è necessario applicare stili di formattazione diversi per Microsoft Excel 2007, applicare gli stili utilizzando l'API Aspose.Cells. Di seguito viene fornito un esempio per dimostrare questo approccio per applicare uno stile predefinito su una cella.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Create Workbook and Set Cell Style Example</h1>
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
            // Instantiate a new Workbook.
            const workbook = new Workbook();

            // Create a style object.
            const style = workbook.createStyle();

            // Access the first worksheet in the workbook
            const worksheet = workbook.worksheets.get(0);

            // Access cell A1
            const cell = worksheet.cells.get("A1");

            // Input a value to A1 cell.
            cell.putValue("Test");

            // Apply the style to the cell.
            cell.style = style;

            // Saving the Excel 2007 file.
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```



## **Come formattare i caratteri selezionati in una cella**

Il trattamento delle impostazioni del carattere spiega come formattare il testo nelle celle, ma spiega solo come formattare tutto il contenuto della cella. E se si vuole formattare solo alcuni caratteri?

Anche Aspose.Cells supporta questa funzione. Questo argomento spiega come utilizzare questa funzione efficacemente.

### **Come formattare caratteri selezionati**

Aspose.Cells fornisce una classe, [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) che rappresenta un file Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) contiene la collezione [**worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--) che consente l'accesso a ogni foglio di lavoro in un file Excel. Un foglio di lavoro è rappresentato dalla classe [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) offre una collezione [**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--). Ogni elemento della collezione [**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--) rappresenta un oggetto della classe [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell).

La classe [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell) fornisce il metodo [**characters(number, number)**](https://reference.aspose.com/cells/javascript-cpp/cell/#characters-number-number-) che accetta i seguenti parametri per selezionare una gamma di caratteri all’interno di una cella:

- **Indice di inizio**, l'indice del carattere da cui inizia la selezione.
- **Numero di caratteri**, il numero di caratteri da selezionare.

Il metodo [**characters(number, number)**](https://reference.aspose.com/cells/javascript-cpp/cell/#characters-number-number-) restituisce un'istanza della classe [**FontSetting**](https://reference.aspose.com/cells/javascript-cpp/fontsetting) che consente agli sviluppatori di formattare i caratteri nello stesso modo in cui si formattava una cella, come mostrato nell'esempio di codice sottostante. Nel file di output, nella cella A1, la parola 'Visit' sarà formattata con il font predefinito, mentre 'Aspose!' sarà in grassetto e blu.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
        <meta charset="utf-8" />
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
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

            // If a file is provided, open it; otherwise create a new workbook
            let workbook;
            if (fileInput.files && fileInput.files.length > 0) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Obtaining the reference of the first (default) worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(0);

            // Accessing the "A1" cell from the worksheet
            const cell = worksheet.cells.get("A1");

            // Adding some value to the "A1" cell
            cell.value = "Visit Aspose!";

            // Setting the font of selected characters to bold and color to blue
            const charRange = cell.characters(6, 7);
            charRange.font.isBold = true;
            charRange.font.color = AsposeCells.Color.Blue;

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

{{% alert color="primary" %}}

Se si desidera formattare una parte del testo arricchito (Rich Text) in una cella, considerare l’uso dei metodi [**Cell.characters**](https://reference.aspose.com/cells/javascript-cpp/cell/#characters--) e [**Cell.characters**](https://reference.aspose.com/cells/javascript-cpp/cell/#characters-fontsettingarray-). Il metodo [**Cell.characters**](https://reference.aspose.com/cells/javascript-cpp/cell/#characters--) viene utilizzato per accedere alle parti del testo e quindi apportare modifiche tramite il metodo [**Cell.characters**](https://reference.aspose.com/cells/javascript-cpp/cell/#characters-fontsettingarray-), mentre il metodo **Get** restituisce un array di oggetti [**FontSetting**](https://reference.aspose.com/cells/javascript-cpp/fontsetting) che possono essere manipolati per impostare varie proprietà come nome del font, colore del font, grassetto, ecc. e il metodo **Set** può essere usato per applicare le modifiche.

{{% /alert %}}

## **Come formattare righe e colonne**

A volte i developer devono applicare la stessa formattazione su righe o colonne. Applicare la formattazione alle celle una per una richiede spesso più tempo e non è una buona soluzione.
Per affrontare questo problema, Aspose.Cells fornisce un modo semplice e veloce discusso dettagliatamente in questo articolo.

### **Formattare Righe e Colonne**

Aspose.Cells fornisce una classe, [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) che rappresenta un file Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) contiene una collezione [**worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--) che consente l'accesso a ogni foglio di lavoro nel file Excel. Un foglio di lavoro è rappresentato dalla classe [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) fornisce una collezione [**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--). La collezione [**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--) fornisce una collezione [**rows**](https://reference.aspose.com/cells/javascript-cpp/cells/#rows--).

### **Come formattare una riga**

Ogni elemento della collezione [**rows**](https://reference.aspose.com/cells/javascript-cpp/cells/#rows--) rappresenta un oggetto [**Row**](https://reference.aspose.com/cells/javascript-cpp/row). L'oggetto [**Row**](https://reference.aspose.com/cells/javascript-cpp/row) offre il metodo [**applyStyle(Style, StyleFlag)**](https://reference.aspose.com/cells/javascript-cpp/row/#applyStyle-style-styleflag-) usato per impostare la formattazione della riga. Per applicare la stessa formattazione a una riga, utilizzare l’oggetto [**Style**](https://reference.aspose.com/cells/javascript-cpp/style). I passaggi seguenti mostrano come utilizzarlo.

1. Aggiungere un oggetto [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) alla classe [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) chiamando il suo metodo [**createStyle()**](https://reference.aspose.com/cells/javascript-cpp/workbook/#createStyle--).
2. Impostare le proprietà dell’oggetto [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) per applicare le impostazioni di formattazione.
3. Rendere attivi gli attributi rilevanti per l’oggetto [**StyleFlag**](https://reference.aspose.com/cells/javascript-cpp/styleflag).
4. Assegnare l’oggetto [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) configurato all’oggetto [**Row**](https://reference.aspose.com/cells/javascript-cpp/row).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
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
            // Instantiating a Workbook object
            const workbook = new Workbook();

            // Obtaining the reference of the first (default) worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(0);

            // Adding a new Style to the styles
            const style = workbook.createStyle();

            // Setting the vertical alignment of the text in the "A1" cell
            style.verticalAlignment = AsposeCells.TextAlignmentType.Center;

            // Setting the horizontal alignment of the text in the "A1" cell
            style.horizontalAlignment = AsposeCells.TextAlignmentType.Center;

            // Setting the font color of the text in the "A1" cell
            style.font.color = AsposeCells.Color.Green;

            // Shrinking the text to fit in the cell
            style.shrinkToFit = true;

            // Setting the bottom border color of the cell to red
            style.borders.get(AsposeCells.BorderType.BottomBorder).color = AsposeCells.Color.Red;

            // Setting the bottom border type of the cell to medium
            style.borders.get(AsposeCells.BorderType.BottomBorder).lineStyle = AsposeCells.CellBorderType.Medium;

            // Creating StyleFlag
            const styleFlag = new AsposeCells.StyleFlag();
            styleFlag.horizontalAlignment = true;
            styleFlag.verticalAlignment = true;
            styleFlag.shrinkToFit = true;
            styleFlag.borders = true;
            styleFlag.fontColor = true;

            // Accessing a row from the Rows collection
            const row = worksheet.cells.rows.get(0);

            // Assigning the Style object to the Style property of the row
            row.applyStyle(style, styleFlag);

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### **Come formattare una colonna**

La collezione [**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--) fornisce anche una collezione [**columns**](https://reference.aspose.com/cells/javascript-cpp/cells/#columns--). Ogni elemento della collezione [**columns**](https://reference.aspose.com/cells/javascript-cpp/cells/#columns--) rappresenta un oggetto [**Column**](https://reference.aspose.com/cells/javascript-cpp/column). Similmente a un oggetto [**Row**](https://reference.aspose.com/cells/javascript-cpp/row), anche l’oggetto [**Column**](https://reference.aspose.com/cells/javascript-cpp/column) offre il metodo [**applyStyle(Style, StyleFlag)**](https://reference.aspose.com/cells/javascript-cpp/row/#applyStyle-style-styleflag-) per formattare una colonna.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Style and Column Apply Example</h1>
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
            // Instantiate a new Workbook
            const workbook = new Workbook();

            // Obtain the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Add a new Style to the styles
            const style = workbook.createStyle();

            // Set vertical and horizontal alignment
            style.verticalAlignment = AsposeCells.TextAlignmentType.Center;
            style.horizontalAlignment = AsposeCells.TextAlignmentType.Center;

            // Set font color
            style.font.color = AsposeCells.Color.Green;

            // Shrink to fit
            style.shrinkToFit = true;

            // Set bottom border color and style
            style.borders.get(AsposeCells.BorderType.BottomBorder).color = AsposeCells.Color.Red;
            style.borders.get(AsposeCells.BorderType.BottomBorder).lineStyle = AsposeCells.CellBorderType.Medium;

            // Create and configure StyleFlag
            const styleFlag = new AsposeCells.StyleFlag();
            styleFlag.horizontalAlignment = true;
            styleFlag.verticalAlignment = true;
            styleFlag.shrinkToFit = true;
            styleFlag.borders = true;
            styleFlag.fontColor = true;

            // Access first column and apply style
            const column = worksheet.cells.getColumns().get(0);
            column.applyStyle(style, styleFlag);

            // Save the workbook and provide download link
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Style applied to column successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Argomenti avanzati**
- [Impostazioni di Allineamento](/cells/it/javascript-cpp/cells-alignment-settings/)
- [Impostazioni dei Bordi](/cells/it/javascript-cpp/cells-border-settings/)
- [Imposta Formati Condizionali di file Excel e ODS.](/cells/it/javascript-cpp/conditional-formatting/)
- [Temi e Colori di Excel](/cells/it/javascript-cpp/excel-themes-and-colors/)
- [Impostazioni di Riempimento](/cells/it/javascript-cpp/cells-fill-settings/)
- [Impostazioni dei Caratteri](/cells/it/javascript-cpp/cells-font-settings/)
- [Formattare le Celle di un Foglio di Lavoro in un Documento di Lavoro](/cells/it/javascript-cpp/format-worksheet-cells-in-a-workbook/)
- [Implementare il Sistema di Data 1904](/cells/it/javascript-cpp/implement-1904-date-system/)
- [Unione e separazione di celle](/cells/it/javascript-cpp/merging-and-unmerging-cells/)
- [Impostazioni dei numeri](/cells/it/javascript-cpp/cells-number-settings/)
- [Ottenere e impostare lo stile delle celle](/cells/it/javascript-cpp/evaluating-cell-getstyle-and-setstyle-methods-against-cell-style-property/)
