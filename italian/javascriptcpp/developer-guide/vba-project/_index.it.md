---
title: Gestisci i codici VBA del workbook macro abilitato Excel
linktitle: Progetto macro
type: docs
weight: 200
url: /it/javascript-cpp/manage-vba-project/
description: Aggiungi modulo VBA e modifica VBA o Macro con Aspose.Cells for JavaScript tramite C++.
---

## **Aggiungi un modulo VBA in JavaScript tramite C++**
{{% alert color="primary" %}}

Aspose.Cells consente di aggiungere un nuovo modulo VBA e codice macro utilizzando Aspose.Cells for JavaScript tramite C++. Si prega di utilizzare il metodo [**Workbook.add(Worksheet)**](https://reference.aspose.com/cells/javascript-cpp/vbamodulecollection/#add-worksheet-) per aggiungere il nuovo modulo VBA all'interno del workbook

{{% /alert %}}

Il seguente esempio di codice crea un nuovo workbook e aggiunge un nuovo modulo VBA e codice macro e salva l'output in formato XLSM. Una volta aperto il file XLSM in Microsoft Excel e cliccato sui comandi di menu **Sviluppatore > Visual Basic**, vedrai un modulo chiamato "TestModule" e al suo interno vedrai il seguente codice macro.

{{< highlight javascript >}}
Sub ShowMessage() {
    MsgBox "Welcome to Aspose!"
}
{{< /highlight >}}



```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Add VBA Module</title>
    </head>
    <body>
        <h1>Add VBA Module Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.xlsm,.csv" />
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
            // Create new workbook
            const workbook = new Workbook();

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Add VBA Module
            const idx = workbook.vbaProject.modules.add(worksheet);

            // Access the VBA Module, set its name and codes
            const module = workbook.vbaProject.modules.get(idx);
            module.name = "TestModule";
            module.codes = "Sub ShowMessage()\r\n" +
                           "    MsgBox \"Welcome to Aspose!\"\r\n" +
                           "End Sub";

            // Save the workbook as XLSM and prepare download
            const outputData = workbook.save(SaveFormat.Xlsm);
            const blob = new Blob([outputData], { type: "application/vnd.ms-excel.sheet.macroEnabled.12" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsm';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">VBA module added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Modifica VBA o Macro in JavaScript tramite C++**

{{% alert color="primary" %}} 

Puoi modificare il codice VBA o Macro utilizzando Aspose.Cells for JavaScript tramite C++. Aspose.Cells ha aggiunto i seguenti moduli e classi per leggere e modificare il progetto VBA nel file Excel.

- Aspose.Cells.Vba
- VbaProject
- VbaModuleCollection
- VbaModule

Questo articolo ti mostrerà come modificare il codice VBA o Macro all'interno del file Excel di origine usando Aspose.Cells.

{{% /alert %}} 

Il seguente esempio di codice carica il file Excel sorgente che contiene il codice VBA o Macro

{{< highlight javascript >}}
Sub Button1_Click() {
    MsgBox "This is test message."
}
{{< /highlight >}}

Dopo l'esecuzione del codice di esempio di Aspose.Cells, il codice VBA o Macro sarà modificato in questo modo

{{< highlight javascript >}}
Sub Button1_Click() {
    MsgBox "This is Aspose.Cells message."
}
{{< /highlight >}}

Puoi scaricare il [file Excel di origine](5112508.xlsm) e il [file Excel di output](5112511.xlsm) dai link forniti.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Change VBA Module Code Example</title>
    </head>
    <body>
        <h1>Change VBA Module Code Example</h1>
        <input type="file" id="fileInput" accept=".xlsm,.xls,.xlsx" />
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
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file (.xlsm).</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access VBA project modules
            const modules = workbook.vbaProject.modules;
            const moduleCount = modules.count;
            for (let i = 0; i < moduleCount; i++) {
                const module = modules.get(i);
                let code = module.codes;
                if (code && code.includes("This is test message.")) {
                    code = code.replace("This is test message.", "This is Aspose.Cells message.");
                    module.codes = code;
                }
            }

            const outputData = workbook.save(SaveFormat.Xlsm);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsm';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">VBA module code updated successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Argomenti avanzati**
- [Aggiungi un riferimento alla libreria al progetto VBA nel foglio di lavoro](/cells/it/javascript-cpp/add-a-library-reference-to-vba-project-in-workbook/)
- [Assegna una Macro al controllo del modulo](/cells/it/javascript-cpp/assign-macro-to-form-control/)
- [Verifica se la firma digitale del codice VBA è valida](/cells/it/javascript-cpp/check-if-digital-signature-of-vba-code-is-valid/)
- [Verifica se il codice VBA è firmato](/cells/it/javascript-cpp/check-if-vba-code-is-signed/)
- [Verifica se il progetto VBA in un foglio di lavoro è firmato](/cells/it/javascript-cpp/check-if-vba-project-in-a-workbook-is-signed/)
- [Verifica se il progetto VBA è protetto e bloccato per la visualizzazione](/cells/it/javascript-cpp/check-if-vba-project-is-protected-and-locked-for-viewing/)
- [Copia il DesignerStorage del modulo utente VBA Macro dal modello al foglio di lavoro di destinazione](/cells/it/javascript-cpp/copy-vba-macro-userform-designerstorage-from-template-to-target-workbook/)
- [Firma digitalmente un progetto di codice VBA con un certificato](/cells/it/javascript-cpp/digitally-sign-a-vba-code-project-with-certificate/)
- [Esporta il certificato VBA su file o flusso](/cells/it/javascript-cpp/export-vba-certificate-to-file-or-stream/)
- [Filtra il progetto VBA durante il caricamento di un libro di lavoro](/cells/it/javascript-cpp/filter-vba-project-while-loading-a-workbook/)
- [Scopri se il progetto VBA è protetto](/cells/it/javascript-cpp/find-out-if-vba-project-is-protected/)
- [Proteggi con password il progetto VBA del foglio di lavoro Excel](/cells/it/javascript-cpp/password-protect-the-vba-project-of-excel-workbook/)
