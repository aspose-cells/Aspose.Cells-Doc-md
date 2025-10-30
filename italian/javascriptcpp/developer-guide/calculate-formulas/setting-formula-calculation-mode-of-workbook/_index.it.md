---
title: Impostare la modalità di calcolo delle formule del Workbook con JavaScript tramite C++
linktitle: Impostazione della modalità di calcolo delle formule di Workbook
description: Quest articolo introduce come impostare la modalità di calcolo delle formule di un workbook in Microsoft Excel con Script Aspose.Cells for Java tramite C++. Caricando un file Excel esistente o creando uno nuovo, è possibile usare la proprietà fornita da Aspose.Cells per impostare la modalità di calcolo delle formule e ottenere il risultato. Infine, salviamo il file Excel modificato su disco.
keywords: Aspose.Cells, Excel, cartella di lavoro, modalità di calcolo delle formule, impostazioni, JavaScript tramite C++
type: docs
weight: 110
url: /it/javascript-cpp/setting-formula-calculation-mode-of-workbook/
---

{{% alert color="primary" %}}  
Microsoft Excel consente di impostare la modalità di calcolo delle formule, cioè il modo in cui le formule vengono calcolate. Ci sono tre possibili valori:  

- Automatico - ricalcola ogni volta che qualcosa viene modificato e ogni volta che viene aperto un workbook.  
- Automatico tranne per le tabelle dati - ricalcola ogni volta che qualcosa viene modificato, ma tralasciando le tabelle dati.  
- Manuale - ricalcola solo quando l'utente lo richiede esplicitamente premendo F9 o CTRL+ALT+F9, o quando il workbook viene salvato.  
{{% /alert %}}  

Per impostare la modalità di calcolo delle formule in Microsoft Excel:  

1. Selezionare **Formule** e quindi **Opzioni di calcolo**.  
1. Seleziona una delle opzioni.  

Aspose.Cells for JavaScript tramite C++ permette anche di impostare la **Modalità di calcolo delle formule** utilizzando la proprietà [**FormulaSettings.calculationMode**](https://reference.aspose.com/cells/javascript-cpp/formulasettings/#calculationMode--) modalità. Puoi assegnarle l'enumerazione [**CalcModeType**](https://reference.aspose.com/cells/javascript-cpp/calcmodetype) che ha uno dei seguenti valori:  

- CalcModeType.Automatic  
- CalcModeType.AutomaticExceptTable  
- CalcModeType.Manual  

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
            // Creating a workbook
            const workbook = new Workbook();

            // Set the Formula Calculation Mode to Manual
            workbook.settings.formulaSettings.calculationMode = AsposeCells.CalcModeType.Manual;

            // Save the workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and saved successfully. Click the download link to get the file.</p>';
        });
    </script>
</html>
```
