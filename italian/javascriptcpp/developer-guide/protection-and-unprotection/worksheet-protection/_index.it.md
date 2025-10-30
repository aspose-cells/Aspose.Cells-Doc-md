---
title: Proteggi e Sblocca il Foglio di Lavoro con JavaScript tramite C++
linktitle: Proteggere e Difendere il Foglio di Lavoro
type: docs
weight: 40
url: /it/javascript-cpp/protect-and-unprotect-worksheets/
description: Proteggi e sblocca il foglio di lavoro dei file Excel con Aspose.Cells for JavaScript tramite C++.
---

{{% alert color="primary" %}}  
Per impedire ad altri utenti di modificare, spostare o eliminare accidentalmente o deliberatamente i dati in un foglio di lavoro, è possibile bloccare le celle nel foglio di lavoro di Excel e quindi proteggere il foglio con una password.  
{{% /alert %}}  

## **Proteggere e proteggere il foglio di lavoro in MS Excel**  

**![proteggere e proteggere il foglio di lavoro](protect-and-unprotect-worksheet.png)**  

1. Fare clic su **Revisione > Proteggi foglio di lavoro**.  
1. Inserire una password nella **casella di Password**.  
1. Selezionare le opzioni **consenti**.  
1. Selezionare **OK**, reinserire la password per confermarla e quindi selezionare di nuovo **OK**.  

## **Proteggi il Foglio di Lavoro usando Aspose.Cells for JavaScript tramite C++**  
È sufficiente utilizzare le seguenti linee di codice per implementare la protezione della struttura della cartella di lavoro dei file di Excel.  

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
        const { Workbook, SaveFormat, ProtectionType } = AsposeCells;

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
            // Create a new file (workbook)
            const workbook = new Workbook();

            // Gets the first worksheet.
            const sheet = workbook.worksheets.get(0);

            // Protect contents of the worksheet.
            sheet.protect(ProtectionType.Contents);

            // Protect worksheet with password.
            sheet.protection.password = "test";

            // Save as Excel file and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Book1.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Worksheet protected and file is ready. Click the download link to get the file.</p>';
        });
    </script>
</html>
```  

## **Sblocca il Foglio di Lavoro usando Aspose.Cells for JavaScript tramite C++**  
Rimuovere la protezione dal foglio di lavoro è facile con l'API Aspose.Cells. Se il foglio di lavoro è protetto da password, è richiesta la password corretta.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Unprotect Worksheet Example</title>
    </head>
    <body>
        <h1>Unprotect Worksheet Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Unprotect Worksheet</button>
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

            // Instantiate Workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet
            const sheet = workbook.worksheets.get(0);

            // Unprotect contents of the worksheet using password
            sheet.unprotect("password");

            // Save the modified workbook to XLSX format and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Book1.unprotected.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Unprotected Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Worksheet unprotected successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

## **Argomenti avanzati**  
- [Impostazioni di protezione avanzate da Excel XP in poi](/cells/it/javascript-cpp/advanced-protection-settings-since-excel-xp/)  
- [Verificare se il foglio di lavoro è protetto da password](/cells/it/javascript-cpp/detect-if-worksheet-is-password-protected/)  
- [Protezione dei fogli di lavoro](/cells/it/javascript-cpp/protecting-worksheets/)  
- [Sblocca un foglio di lavoro](/cells/it/javascript-cpp/unprotect-a-worksheet/)  
- [Verificare la password utilizzata per proteggere il foglio di lavoro](/cells/it/javascript-cpp/verify-password-used-to-protect-the-worksheet/)
