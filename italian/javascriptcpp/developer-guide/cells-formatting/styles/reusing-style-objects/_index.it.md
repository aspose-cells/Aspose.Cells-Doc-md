---
title: Riutilizzo degli oggetti stile
linktitle: Riutilizzo degli oggetti stile
description: In Aspose.Cells for JavaScript via C++, creandosi e usando oggetti stile riutilizzabili, si può semplificare la gestione degli stili e migliorare l efficienza del codice. La nostra guida ti aiuterà a sfruttare i vantaggi degli oggetti stile riutilizzabili e ad implementarle nella tua applicazione.
keywords: Aspose.Cells for JavaScript via C++, Riutilizzo di Oggetti Stile, Gestione Stili, Efficienza del Codice, Stili Riutilizzabili, Sviluppo di Applicazioni, Riferimento API, Esempio di Codice, Download, Supporto.
type: docs
weight: 3000
url: /it/javascript-cpp/reusing-style-objects/
---

{{% alert color="primary" %}}  
Il riutilizzo degli oggetti stile può risparmiare memoria e rendere un programma più veloce.  
{{% /alert %}}  

Per applicare una formattazione a un'ampia gamma di celle in un foglio di lavoro:

1. Creare un oggetto stile.
1. Specificare gli attributi.
1. Applicare lo stile alle celle nell'intervallo.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Create Workbook and Set Font</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Color } = AsposeCells;

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
            // Creating a new workbook (empty)
            const workbook = new Workbook();

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access cells
            const cell1 = worksheet.cells.get("A1");
            const cell2 = worksheet.cells.get("B1");

            // Set the styles of both cells to Times New Roman
            const styleObject = workbook.createStyle();
            styleObject.font.color = Color.Red;
            styleObject.font.name = "Times New Roman";
            cell1.style = styleObject;
            cell2.style = styleObject;

            // Put the values inside the cell
            cell1.value = "Hello World!";
            cell2.value = "Hello World!!";

            // Save to XLSX
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'SampleOutput_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and saved successfully. Click the download link to get the file.</p>';
        });
    </script>
</html>
```


{{% alert color="primary" %}}  
Poiché il metodo [**Cell.style**](https://reference.aspose.com/cells/javascript-cpp/cell/#style--) / [**Cell.style**](https://reference.aspose.com/cells/javascript-cpp/cell/#style-style-) utilizza molto meno memoria, ed è più efficiente, il vecchio metodo Cell.style che consumava molta memoria inutile è stato rimosso con il rilascio di Aspose.Cells 7.1.0.  
{{% /alert %}}
