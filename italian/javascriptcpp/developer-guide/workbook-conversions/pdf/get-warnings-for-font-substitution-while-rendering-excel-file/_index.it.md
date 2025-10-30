---
title: Ottieni avvisi di Sostituzione Font durante il rendering del file Excel con JavaScript via C++
linktitle: Ottieni avvisi per la sostituzione dei font durante il rendering del file Excel
type: docs
weight: 230
url: /it/javascript-cpp/get-warnings-for-font-substitution-while-rendering-excel-file/
description: Impara come ottenere avvisi di sostituzione dei font quando si renderizzano file Excel in PDF usando Aspose.Cells for JavaScript via C++.
---

{{% alert color="primary" %}}  

A volte, durante la conversione di un file Microsoft Excel in PDF, Aspose.Cells sostituisce i font. Aspose.Cells fornisce una funzione che permette agli sviluppatori di sapere quale particolare font è stato sostituito scatenando un avviso. Si tratta di una funzionalità utile che può aiutarti a capire perché un PDF generato da Aspose.Cells appare diverso dal file di origine di Microsoft Excel, in modo da poter adottare azioni appropriate. Ad esempio, installare i font mancanti in modo che i risultati della conversione siano uguali.

{{% /alert %}}  

Per ottenere avvisi per la sostituzione dei font durante il rendering di file Excel in PDF, implementa l'interfaccia IWarningCallback e imposta la proprietà PdfSaveOptions.warningCallback con la tua interfaccia implementata.

La schermata sottostante mostra un file Excel di origine che utilizzeremo nel codice seguente. Contiene del testo nelle celle A6 e A7 con caratteri che non vengono visualizzati correttamente in Microsoft Excel.

|**Non tutti i font vengono visualizzati correttamente**|  
| :- |  
|![todo:image_alt_text](get-warnings-for-font-substitution-while-rendering-excel-file_1.png)|  
Aspose.Cells sostituirà i font nelle celle A6 e A7 con font appropriati come mostrato di seguito.

|**Font sostituiti**|  
| :- |  
|![todo:image_alt_text](get-warnings-for-font-substitution-while-rendering-excel-file_2.png)|  
## **Scarica file di origine e PDF di output**  
È possibile scaricare il file Excel di origine e il PDF di output dai seguenti collegamenti

- [source.xlsx](5112611.xlsx)  
- [output.pdf](5112616.pdf)  
## **Codice**  
Il seguente esempio implementa l'interfaccia IWarningCallback e imposta la proprietà PdfSaveOptions.warningCallback con l'interfaccia implementata. Ora, ogni volta che un font verrà sostituito in una cella, Aspose.Cells genererà un avviso all’interno del metodo WarningCallback.Warning().

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - GetWarningsForFontSubstitution</title>
    </head>
    <body>
        <h1>GetWarningsForFontSubstitution Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PdfSaveOptions } = AsposeCells;

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

        class GetWarningsForFontSubstitution {
            static warning(info) {
                if (info.type === AsposeCells.WarningType.FontSubstitution) {
                    console.log("WARNING INFO: " + info.description);
                }
            }
        }

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();
            // Instantiate workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Prepare PDF save options and assign warning callback
            const options = new PdfSaveOptions();
            options.warningCallback = GetWarningsForFontSubstitution;

            // Save workbook as PDF
            const outputData = workbook.save(SaveFormat.Pdf, options);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            resultDiv.innerHTML = '<p style="color: green;">PDF generated successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```  
## **Output**  
Dopo la conversione del file Excel di origine in PDF, gli avvisi vengono visualizzati sulla console di debug come segue:

{{< highlight java >}}  

 WARNING INFO: Font substitution: Font [ Athene Logos; Regular ] has been substituted in Cell [ A6 ] in Sheet [ Sheet1 ].  

WARNING INFO: Font substitution: Font [ B Traffic; Regular ] has been substituted in Cell [ A7 ] in Sheet [ Sheet1 ].  

{{< /highlight >}}  

{{% alert color="primary" %}}  

Se il foglio di lavoro contiene formule, è meglio chiamare il metodo Workbook.calculateFormula appena prima di rendere il foglio di lavoro nel formato PDF. Farlo garantirà che i valori dipendenti dalle formule vengano ricalcolati e i valori corretti vengano resi nel PDF.

{{% /alert %}}
