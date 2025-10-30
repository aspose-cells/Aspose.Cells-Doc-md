---
title: Protezione dei fogli di lavoro con JavaScript tramite C++
linktitle: Protezione dei fogli di lavoro
type: docs
weight: 10
url: /it/javascript-cpp/protecting-worksheets/
description: Impara come proteggere i fogli di lavoro in Excel usando Aspose.Cells for JavaScript via C++, inclusa la protezione di righe, colonne e celle specifiche.
---

{{% alert color="primary" %}}

Quando un foglio di lavoro è protetto, le azioni che l'utente può eseguire sono limitate. Ad esempio, non può inserire dati, inserire o eliminare righe o colonne, ecc.

{{% /alert %}}

## **Proteggere i fogli di lavoro**

### **Introduzione**

Le opzioni generali di protezione in Microsoft Excel sono:

- Contenuti
- Oggetti
- Scenari

I fogli di lavoro protetti non nascondono o proteggono dati sensibili, quindi è diverso dalla crittografia dei file. In generale, la protezione del foglio di lavoro è adatta per scopi di presentazione. Impedisce all'utente finale di modificare i dati, il contenuto e la formattazione nel foglio di lavoro.

### **Proteggere un foglio di lavoro**

Aspose.Cells fornisce una classe, [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) che rappresenta un file Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) contiene una collezione [**worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--) che consente l'accesso a ogni foglio di lavoro in un file Excel. Un foglio di lavoro è rappresentato dalla classe [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet).

La classe [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) fornisce il metodo [**protect(ProtectionType)**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#protect-protectiontype-) che viene utilizzato per applicare la protezione sul foglio di lavoro. Il metodo [**protect(ProtectionType)**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#protect-protectiontype-) accetta i seguenti parametri:

- Tipo di Protezione, il tipo di protezione da applicare al foglio di lavoro. Il tipo di protezione è applicato con l'aiuto dell'enumerazione [**ProtectionType**](https://reference.aspose.com/cells/javascript-cpp/protectiontype).
- Nuova password, la nuova password utilizzata per proteggere il foglio di lavoro.
- Vecchia password, la vecchia password, se il foglio di lavoro è già protetto da password. Se il foglio di lavoro non è già protetto, passare semplicemente null.

L'enumerazione [**ProtectionType**](https://reference.aspose.com/cells/javascript-cpp/protectiontype) contiene i seguenti tipi di protezione predefiniti:

|**Tipi di protezione**|**Descrizione**|
| :- | :- |
|All|L'utente non può modificare nulla in questo foglio di lavoro|
|Contents|L'utente non può inserire dati in questo foglio di lavoro|
|Objects|L'utente non può modificare oggetti disegno|
|Scenarios|L'utente non può modificare scenari salvati|
|Structure|L'utente non può modificare la struttura|
|Windows|La protezione è applicata alle finestre|
|None|Nessuna protezione è applicata|

L'esempio seguente mostra come proteggere un foglio di lavoro con una password.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Protect Worksheet Example</title>
    </head>
    <body>
        <h1>Protect Worksheet Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ProtectionType, Utils } = AsposeCells;

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

            // Ensure Aspose.Cells is initialized before proceeding
            await AsposeCells.onReady();

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object with file buffer
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Protecting the worksheet with a password
            worksheet.protect(ProtectionType.All, "aspose", null);

            // Saving the modified Excel file in Excel 97-2003 format
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Worksheet protected successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

Dopo che il codice sopra è utilizzato per proteggere il foglio di lavoro, è possibile verificare la protezione sul foglio di lavoro aprendolo. Una volta aperto il file e tentato di aggiungere alcuni dati al foglio di lavoro, si vedrà il seguente dialogo:

|**Un avviso di dialogo che l'utente non può modificare il foglio di lavoro**|
| :- |
|![todo:image_alt_text](protecting-worksheets_1.png)|

Per lavorare sul foglio di lavoro, sblocca il foglio di lavoro selezionando **Protezione**, poi **Sblocca foglio** dal menu **Strumenti**.

Dopo aver selezionato Sblocca foglio nel menu, si aprirà una finestra di dialogo che richiederà di inserire la password in modo da poter lavorare sul foglio di lavoro come mostrato di seguito:

|![todo:image_alt_text](protecting-worksheets_2.png)|

### **Proteggere alcune celle nel foglio di lavoro utilizzando Microsoft Excel**

Potrebbero esserci scenari in cui è necessario bloccare solo alcune celle del foglio di lavoro. Se si desidera bloccare alcune celle specifiche, bisogna sbloccare tutte le altre. Tutte le celle di un foglio di lavoro sono già inizializzate per essere bloccate; è possibile verificare aprendo un file Excel con MS Excel e cliccando su **Formato | Celle...** per mostrare la finestra di dialogo **Formato celle** e poi cliccare sulla scheda **Protezione** e vedere che la casella di controllo "Bloccato" è selezionata di default.

I punti seguenti descrivono come bloccare alcune celle usando MS Excel. Questo metodo si applica a Microsoft Office Excel 97, 2000, 2002, 2003 e versioni successive.

1. Selezionare l'intero foglio di lavoro facendo clic sul pulsante **Seleziona tutto** (il rettangolo grigio direttamente sopra il numero di riga per la riga 1 e alla sinistra della lettera della colonna A).
2. Clicca su **Celle** nel menu **Formato**, clicca sulla scheda **Protezione** e poi deseleziona la casella **Bloccato**.
   Questo sblocca tutte le celle del foglio di lavoro.
   Se il comando **Celle** non è disponibile, parti del foglio di lavoro potrebbero già essere bloccate. Nel menu **Strumenti**, posizionarsi su **Protezione**, e quindi fare clic su **Sblocca foglio**.
3. Seleziona solo le celle che desideri bloccare e ripeti il passaggio 2, ma questa volta seleziona la casella **Bloccato**.
4. Dal menu **Strumenti**, punta su **Protezione**, clicca su **Proteggi foglio** e poi su **OK**.
5. Nella finestra di dialogo **Proteggi foglio**, puoi specificare una password e selezionare gli elementi che desideri che gli utenti possano modificare.

### **Proteggi alcune celle nel foglio di lavoro usando Aspose.Cells**

In questo metodo, utilizziamo l'API Aspose.Cells esclusivamente per eseguire il compito.

Esempio: il seguente esempio mostra come proteggere alcune celle del foglio di lavoro. Sblocca tutte le celle del foglio prima e poi blocca 3 celle (A1, B1, C1). Infine, protegge il foglio di lavoro. L'oggetto [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) contiene una proprietà booleana, [**isLocked()**](https://reference.aspose.com/cells/javascript-cpp/style/#isLocked--). Puoi impostare la proprietà [**isLocked()**](https://reference.aspose.com/cells/javascript-cpp/style/#isLocked--) su true o false e applicare il metodo *Column/Row.applyStyle()* per bloccare o sbloccare la riga/colonna con gli attributi desiderati.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Unlock Columns and Protect Specific Cells Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, StyleFlag, ProtectionType } = AsposeCells;

        const readyPromise = AsposeCells.onReady({
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
            await readyPromise;

            // Create a new workbook.
            const wb = new Workbook();

            // Create a worksheet object and obtain the first sheet.
            const sheet = wb.worksheets.get(0);

            // Define the style object.
            let style;

            // Define the styleflag object
            const styleflag = new StyleFlag();

            // Loop through all the columns in the worksheet and unlock them.
            for (let i = 0; i <= 255; i++) {
                style = sheet.cells.columns.get(i).style;
                style.isLocked = false;
                styleflag.locked = true;
                sheet.cells.columns.get(i).applyStyle(style, styleflag);
            }

            // Lock the three cells...i.e. A1, B1, C1.
            style = sheet.cells.get("A1").style;
            style.isLocked = true;
            sheet.cells.get("A1").style = style;

            style = sheet.cells.get("B1").style;
            style.isLocked = true;
            sheet.cells.get("B1").style = style;

            style = sheet.cells.get("C1").style;
            style.isLocked = true;
            sheet.cells.get("C1").style = style;

            // Finally, Protect the sheet now.
            sheet.protect(ProtectionType.All);

            // Save the excel file and provide download link
            const outputData = wb.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### **Proteggere una riga nel foglio di lavoro**

Aspose.Cells permette di bloccare facilmente qualsiasi riga nel foglio di lavoro. Qui, possiamo utilizzare il metodo [**applyStyle(Style, StyleFlag)**](https://reference.aspose.com/cells/javascript-cpp/row/#applyStyle-style-styleflag-) della classe [**Aspose.Cells.Row**](https://reference.aspose.com/cells/javascript-cpp/row) per applicare [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) a una riga specifica del foglio. Questo metodo accetta due argomenti: un oggetto [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) e un oggetto [**StyleFlag**](https://reference.aspose.com/cells/javascript-cpp/styleflag) che contiene tutti i membri relativi alla formattazione applicata.

Il seguente esempio mostra come proteggere una riga nel foglio di lavoro. Sblocca tutte le celle del foglio prima e poi blocca la prima riga. Infine, protegge il foglio. L'oggetto [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) contiene una proprietà booleana, [**isLocked()**](https://reference.aspose.com/cells/javascript-cpp/style/#isLocked--). Puoi impostare [**isLocked()**](https://reference.aspose.com/cells/javascript-cpp/style/#isLocked--) su true o false per bloccare o sbloccare la riga/colonna usando l'oggetto [**StyleFlag**](https://reference.aspose.com/cells/javascript-cpp/styleflag).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Protect Worksheet Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, StyleFlag, ProtectionType, Utils } = AsposeCells;

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
            // Create a new workbook.
            const wb = new Workbook();

            // Create a worksheet object and obtain the first sheet.
            const sheet = wb.worksheets.get(0);

            // Define the style object.
            let style;

            // Define the styleflag object.
            const flag = new StyleFlag();

            // Loop through all the columns in the worksheet and unlock them.
            for (let i = 0; i <= 255; i++) {
                style = sheet.cells.columns.get(i).style;
                style.isLocked = false;
                flag.locked = true;
                sheet.cells.columns.get(i).applyStyle(style, flag);
            }

            // Get the first row style.
            style = sheet.cells.rows.get(0).style;

            // Lock it.
            style.isLocked = true;

            // Set the lock setting.
            flag.locked = true;

            // Apply the style to the first row.
            sheet.cells.applyRowStyle(0, style, flag);

            // Protect the sheet.
            sheet.protect(ProtectionType.All);

            // Save the excel file.
            const outputData = wb.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and protected. Click the download link to get the file.</p>';
        });
    </script>
</html>
```

### **Proteggere una colonna nel foglio di lavoro**

Aspose.Cells permette di bloccare facilmente qualsiasi colonna nel foglio di lavoro. Qui, possiamo utilizzare il metodo [**applyStyle(Style, StyleFlag)**](https://reference.aspose.com/cells/javascript-cpp/column/#applyStyle-style-styleflag-) della classe [**Aspose.Cells.Column**](https://reference.aspose.com/cells/javascript-cpp/column) per applicare [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) a una colonna specifica del foglio. Questo metodo accetta due argomenti: un oggetto [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) e un oggetto [**StyleFlag**](https://reference.aspose.com/cells/javascript-cpp/styleflag) che contiene tutti i membri relativi alla formattazione applicata.

Il seguente esempio mostra come proteggere una colonna nel foglio di lavoro. Sblocca tutte le celle del foglio prima e poi blocca la prima colonna. Infine, protegge il foglio. L'oggetto [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) contiene una proprietà booleana, [**isLocked()**](https://reference.aspose.com/cells/javascript-cpp/style/#isLocked--). Puoi impostare [**isLocked()**](https://reference.aspose.com/cells/javascript-cpp/style/#isLocked--) su true o false per bloccare o sbloccare la riga/colonna usando l'oggetto [**StyleFlag**](https://reference.aspose.com/cells/javascript-cpp/styleflag).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Unlock Columns and Protect Sheet</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, StyleFlag, ProtectionType } = AsposeCells;

        const readyPromise = AsposeCells.onReady({
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
                // If no file provided, a new workbook will be created
                document.getElementById('result').innerHTML = '<p style="color: orange;">No file selected. A new workbook will be created and processed.</p>';
            } else {
                document.getElementById('result').innerHTML = '<p>Processing selected file...</p>';
            }

            await readyPromise;

            // Load workbook from file if provided, otherwise create new workbook
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Create a worksheet object and obtain the first sheet.
            const sheet = workbook.worksheets.get(0);

            // Define the style object.
            let style;

            // Define the styleflag object.
            const flag = new StyleFlag();

            // Loop through all the columns in the worksheet and unlock them.
            for (let i = 0; i <= 255; i++) {
                style = sheet.cells.columns.get(i).style;
                style.isLocked = false;
                flag.locked = true;
                sheet.cells.columns.get(i).applyStyle(style, flag);
            }

            // Get the first column style.
            style = sheet.cells.columns.get(0).style;

            // Lock it.
            style.isLocked = true;

            // Apply the style to the first column.
            sheet.cells.columns.get(0).applyStyle(style, flag);

            // Protect the sheet.
            sheet.protect(ProtectionType.All);

            // Save the excel file.
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### **Consenti agli utenti di modificare intervalli**

L'esempio seguente mostra come consentire agli utenti di modificare un intervallo in un foglio di lavoro protetto.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Protect Range</title>
    </head>
    <body>
        <h1>Protect Range Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ProtectionType, Utils } = AsposeCells;

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

            // Instantiate a new or loaded Workbook
            let book;
            if (fileInput.files && fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                book = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                book = new Workbook();
            }

            // Get the first (default) worksheet
            const sheet = book.worksheets.get(0);

            // Get the Allow Edit Ranges
            const allowRanges = sheet.allowEditRanges;

            // Define ProtectedRange
            let protected_range;

            // Create the range
            const idx = allowRanges.add("r2", 1, 1, 3, 3);
            protected_range = allowRanges.get(idx);

            // Specify the password
            protected_range.password = "123";

            // Protect the sheet
            sheet.protect(ProtectionType.All);

            // Save the Excel file
            const outputData = book.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'protectedrange.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Protected Range Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Protected range added and sheet protected successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
