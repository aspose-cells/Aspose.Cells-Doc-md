---
title: Crittografa e Decrittografa file Excel con JavaScript via C++
linktitle: Crittografa e Decrittografa file Excel
type: docs
weight: 10
url: /it/javascript-cpp/encrypt-and-decrypt-excel-files/
description: Come crittografare e decrittografare file Excel usando JavaScript via C++. Blocca e sblocca file Excel.
---

{{% alert color="primary" %}}  
Microsoft Excel (97 - 365) ti consente di crittare e proteggere con password i tuoi fogli di calcolo. Utilizza algoritmi forniti da un fornitore di servizi crittografici, o CSP, un insieme di algoritmi crittografici con proprietà diverse. Il CSP predefinito è 'Office 97/2000 Compatible' o 'Crittografia debole (XOR)'. È importante scegliere la corretta lunghezza della chiave di crittografia. Alcuni CSP non supportano più di 40 o 56 bit. Questo è considerato una crittografia debole. Per una crittografia forte, è richiesta una lunghezza minima della chiave di 128 bit. Microsoft Windows contiene CSP che offrono tipi di crittografia forte, ad esempio il 'Microsoft Strong Cryptographic Provider'. Per darti un'idea, la crittografia a 128 bit è ciò che le banche usano per crittografare la connessione con i loro sistemi di Internet Banking.  

Aspose.Cells consente di crittografare e proteggere con password file Microsoft Excel con il tipo di crittografia desiderato.  
{{% /alert %}}  

## **Utilizzando Microsoft Excel**  

Per impostare le impostazioni di crittografia del file in Microsoft Excel (qui Microsoft Excel 2003):  

1. Dal menu **Strumenti**, seleziona **Opzioni**. Verrà visualizzata una finestra di dialogo.  
2. Seleziona la scheda **Sicurezza**.  
3. Inserisci una password e fai clic su **Avanzate**  
4. Scegli il tipo di crittografia e conferma la password.  

## ** Crittografare file Excel con Aspose.Cells for JavaScript via C++**  

Il seguente esempio mostra come criptare e proteggere con password un file Excel usando l'API Aspose.Cells.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Encrypt Workbook</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate a Workbook object by opening the uploaded excel file.
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Specify XOR encryption type.
            workbook.encryptionOptions = { type: AsposeCells.EncryptionType.XOR, keyLength: 40 };

            // Specify Strong Encryption type (RC4, Microsoft Strong Cryptographic Provider).
            workbook.encryptionOptions = { type: AsposeCells.EncryptionType.StrongCryptographicProvider, keyLength: 128 };

            // Password protect the file.
            workbook.settings.password = "1234";

            // Save the excel file.
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'encryptedBook1.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Encrypted Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook encrypted and ready for download.</p>';
        });
    </script>
</html>
```  

### **Specificare l'opzione Password per modificare**  

L'esempio seguente mostra come impostare l'opzione **Password per modificare** per un file esistente utilizzando l'API Aspose.Cells di Microsoft Excel.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Specify Password To Modify Example</h1>
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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Set the password for modification.
            workbook.settings.writeProtection.password = "1234";

            // Save the excel file.
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'SpecifyPasswordToModifyOption.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Password-to-modify set successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  


## ** Decrittografare file Excel con Aspose.Cells for JavaScript via C++**  
È molto facile aprire un file Excel protetto da password e decriptarlo usando l'API Aspose.Cells come mostrato nel codice seguente:  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Open Encrypted Excel and Remove Password</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, LoadOptions, SaveFormat, Utils } = AsposeCells;

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
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an encrypted Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Prepare load options with password to open encrypted file
            const loadOptions = new LoadOptions();
            loadOptions.password = "password";

            // Instantiate workbook from uploaded file with load options
            const workbook = new Workbook(new Uint8Array(arrayBuffer), loadOptions);

            // Remove password from workbook settings
            workbook.settings.password = null;

            // Save the workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            // Use original filename with suffix to indicate password removed
            const originalName = file.name || 'output.xlsx';
            const baseName = originalName.replace(/(\.xls[xm]?|\.csv)$/i, '') || 'output';
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = baseName + '.unlocked.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Unlocked Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Password removed successfully! Click the download link to get the unlocked file.</p>';
        });
    </script>
</html>
```  


## **Argomenti avanzati**  
- [Crittografa e Decrittografa file ODS](/cells/it/javascript-cpp/encrypt-and-decrypt-ods-files/)  
- [Impostazione del tipo di crittografia forte](/cells/it/javascript-cpp/setting-strong-encryption-type/)  
- [Specificare l'autore durante la protezione in scrittura del workbook](/cells/it/javascript-cpp/specify-author-while-write-protecting-workbook/)  
- [Verifica password dei file crittografati](/cells/it/javascript-cpp/verify-password-of-encrypted-excel-and-ods-files/)
