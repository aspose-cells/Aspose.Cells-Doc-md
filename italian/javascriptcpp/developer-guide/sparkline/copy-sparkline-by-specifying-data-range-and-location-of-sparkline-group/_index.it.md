---
title: Copia Sparkline specificando l intervallo di dati e la posizione del gruppo di Sparkline con JavaScript tramite C++
linktitle: Copia Sparkline specificando intervallo dati e posizione del gruppo di Sparkline
type: docs
weight: 300
url: /it/javascript-cpp/copy-sparkline-by-specifying-data-range-and-location-of-sparkline-group/
description: Impara come copiare uno Sparkline in Excel specificando l intervallo di dati e la posizione del gruppo di Sparkline usando Aspose.Cells for JavaScript tramite C++.
---

{{% alert color="primary" %}}
Microsoft Excel consente di copiare una linea di tendenza specificando l'intervallo di dati e la posizione di un gruppo di linee di tendenza. Aspose.Cells supporta questa funzionalità
{{% /alert %}}

Per copiare una linea di tendenza in altre celle in Microsoft Excel

1. Selezionare la cella contenente la linea di tendenza  
1. Selezionare **Modifica dati** dalla sezione **Linee di tendenza** della scheda **Progettazione**  
1. Selezionare **Modifica posizione gruppo e dati**  
1. Specificare l'intervallo di dati e la posizione  
1. Fai clic su **OK**.

Aspose.Cells fornisce il metodo `SparklineCollection.add(dataRange, riga, colonna)` per specificare l'intervallo di dati e la posizione di un gruppo di sparklines. Il seguente esempio di codice carica il file excel di origine come mostrato nello screenshot sopra, poi accede al primo gruppo di sparklines e aggiunge intervalli di dati e posizioni nel gruppo di sparklines. Infine, scrive il file excel di output su disco, come mostrato sopra nello screenshot.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Sparkline Example</h1>
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

            // Create workbook from uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access the first sparkline group
            const group = worksheet.sparklineGroups.get(0);

            // Add Data Ranges and Locations inside this sparkline group
            group.sparklines.add("Sheet1!D5:O5", 4, 15);
            group.sparklines.add("Sheet1!D6:O6", 5, 15);
            group.sparklines.add("Sheet1!D7:O7", 6, 15);
            group.sparklines.add("Sheet1!D8:O8", 7, 15);

            // Save the workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Sparklines added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
