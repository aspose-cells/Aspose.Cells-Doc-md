---
title: Come impedire agli utenti di stampare il file Excel con JavaScript via C++
linktitle: Come Prevenire agli Utenti di Stampare un File Excel
type: docs
weight: 600
url: /it/javascript-cpp/how-to-prevent-printing-excel/
description: Impara come impedire agli utenti di stampare file Excel usando Aspose.Cells for JavaScript via C++.
keywords: stampa excel, impedire la stampa di excel, come impedire agli utenti di stampare excel, excel impedire la stampa, impedire la stampa del workbook, impedire agli utenti di stampare l intero workbook con VBA.
---

## **Possibili Scenari di Utilizzo**  
Nel nostro lavoro quotidiano, potrebbe esserci alcune informazioni importanti nel file Excel; per proteggere i dati interni dalla diffusione, l'azienda non ci permette di stamparli. Questo documento spiega come impedire ad altri di stampare file Excel.  

## **Come impedire agli utenti di stampare file in MS-Excel**  
Puoi applicare il seguente codice VBA per proteggere il tuo file specifico dalla stampa.  
1. Apri il tuo documento di lavoro che non consenti agli altri di stampare.  
1. Seleziona la scheda "Sviluppatore" nel nastro di Excel e clicca sul pulsante "Visualizza codice" nella sezione "Controlli". In alternativa, puoi premere i tasti ALT + F11 per aprire la finestra di Microsoft Visual Basic for Applications.  
<br>  
<img src="1.png" width=70% />  
1. E poi nel Project Explorer di sinistra, fai doppio clic su ThisWorkbook per aprire il modulo, e aggiungi alcuni codici VBA.  
<br>  
<img src="2.png" width=70% />  
1. Poi salva e chiudi questo codice, torna al workbook, e ora quando stampi il file di esempio, questa azione sarà vietata e riceverai il seguente messaggio di avviso:  
<br>  
<img src="3.png" width=70% />  

## ** Come impedire agli utenti di stampare file Excel usando Aspose.Cells for JavaScript via C++**  

Il seguente esempio di codice illustra come impedire agli utenti di stampare un file Excel:  

1. Caricare il [file di esempio](sample.xlsx).  
1. Ottieni l'oggetto VbaModuleCollection dalla proprietà VbaProject di Workbook.  
1. Ottieni l'oggetto VbaModule tramite il nome "ThisWorkbook".  
1. Imposta la proprietà dei codici di VbaModule.  
1. Salva il file di esempio nel formato [xlsm](out.xlsm).  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Update VBA Module Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.xlsm" />
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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing VBA project and its modules
            const modules = workbook.vbaProject.modules;
            const module = modules.get("ThisWorkbook");

            // Setting module codes (converted from setCodes -> codes assignment)
            module.codes = "Private Sub Workbook_BeforePrint(Cancel As Boolean)\r\n  Cancel = True\r\n  MsgBox \"Refusing to print in paperless office\"\r\nEnd Sub\r\n";

            // Saving the modified workbook as macro-enabled workbook
            const outputData = workbook.save(SaveFormat.Xlsm);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsm';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">VBA module updated successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
