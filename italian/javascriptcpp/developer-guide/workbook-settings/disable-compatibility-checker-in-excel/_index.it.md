---
title: Disabilitare il Controllo Compatibilità in Excel con JavaScript tramite C++
linktitle: Disabilitare il verificatore di compatibilità in Excel
type: docs
weight: 170
url: /it/javascript-cpp/disable-compatibility-checker-in-excel/
description: Scopri come disabilitare il controllo compatibilità tramite lo Script Aspose.Cells for Java con API C++.
keywords: Disabilitare il Controllo Compatibilità in JavaScript, Disabilitare il Controllo Compatibilità in Excel in JavaScript tramite C++, Disabilitare il Controllo Compatibilità nel Workbook.
---

## Disabilitare il Controllo Compatibilità nei fogli di lavoro di Excel in JavaScript  

{{% alert color="primary" %}}  
Il controllo di compatibilità di Microsoft Excel segnala quando il salvataggio di un file in un formato precedente potrebbe causare problemi di funzionalità o perdita di fedeltà. Il Controllo di compatibilità è una funzionalità di Microsoft Office Excel 2007 e Microsoft Excel 2010.  

Quando si salva una cartella di lavoro in una versione precedente, da Excel 2007 o Excel 2010 a Excel 97 attraverso Excel 2003, il Verificatore di Compatibilità analizza la cartella di lavoro per vedere se contiene funzionalità non supportate dalla versione precedente. Per aiutarti a prendere decisioni su come gestire problemi di compatibilità, il Verificatore di Compatibilità visualizza finestre di dialogo con opzioni. Può anche essere utilizzato per creare un rapporto su eventuali problemi nella cartella di lavoro, o disabilitare la funzione.  

A volte, è necessario disabilitare il controllo di compatibilità per un determinato foglio di calcolo. Con le API di Aspose.Cells, puoi farlo programmaticamente in modo che gli utenti non si frustrino o si confondano con la finestra di dialogo del Controllo di Compatibilità che appare quando risalvano manualmente il file in Microsoft Excel.  
{{% /alert %}}  

## **Come disabilitare il Controllo di compatibilità utilizzando Microsoft Excel**  

Per disabilitare il Verificatore di compatibilità in Microsoft Excel (ad esempio Microsoft Excel 2007/2010):  

- (Excel 2007) Fare clic sul pulsante Office, quindi su **Prepara**, poi su **Esegui controllo compatibilità**, e infine deselezionare l'opzione **Esegui controllo compatibilità al salvataggio di questo foglio di lavoro**.  
- (Excel 2010) Nella scheda File, fare clic su **Informazioni**, quindi su **Verifica problemi**, fare clic su **Verifica compatibilità** e, infine, deselezionare l'opzione **Verifica compatibilità quando si salva questa cartella di lavoro**.  

## **Come disabilitare il Controllo di compatibilità utilizzando le API di Aspose.Cells**  

Imposta la proprietà [**Workbook.checkCompatibility**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#checkCompatibility--) a **false** per disabilitare il Controllo di Compatibilità di Microsoft Excel.  

### **Esempi di codice**  

Gli esempi di codice che seguono mostrano come disabilitare il Controllo Compatibilità con lo Script Aspose.Cells for Java tramite C++.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Disable Compatibility Checker Example</h1>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Disable the compatibility checker
            workbook.settings.checkCompatibility = false;

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Output_BK_CompCheck.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Compatibility check disabled. Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
