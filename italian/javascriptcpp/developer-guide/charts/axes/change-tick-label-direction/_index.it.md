---
title: Cambia la direzione delle etichette dei tick con JavaScript tramite C++
linktitle: Cambiare la direzione delle etichette degli intervalli
description: Impara come cambiare la direzione delle etichette dei tick in Aspose.Cells for JavaScript tramite C++. La nostra guida ti aiuterà a capire come regolare l’orientamento delle etichette sui assi, inclusi orientamenti orizzontale, verticale e inclinato.
keywords: Aspose.Cells for JavaScript tramite C++, etichette dei tick, direzione, orientamento, assi, orizzontale, verticale, inclinato.
type: docs
weight: 170
url: /it/javascript-cpp/change-tick-label-direction/
---

## **Cambia la direzione delle etichette di graduazione**

Aspose.Cells ti permette di cambiare la direzione delle etichette dei tick dell'asse utilizzando la proprietà [**TickLabels.directionType**](https://reference.aspose.com/cells/javascript-cpp/ticklabels/#directionType--). La proprietà [**TickLabels.directionType**](https://reference.aspose.com/cells/javascript-cpp/ticklabels/#directionType--) accetta il valore dell'enumerazione [**ChartTextDirectionType**](https://reference.aspose.com/cells/javascript-cpp/charttextdirectiontype). L'enumerazione [**ChartTextDirectionType**](https://reference.aspose.com/cells/javascript-cpp/charttextdirectiontype) include i seguenti membri:

- Orizzontale
- Verticale
- Ruota90
- Ruota270
- Impilato

L'immagine seguente confronta i file sorgente e di output

### **Immagine del file sorgente**

![todo:image_alt_text](change-tick-label-direction_1.jpg)

### **Immagine del file di output**

![todo:image_alt_text](change-tick-label-direction_2.jpg)

Il seguente frammento di codice cambia la direzione dell'etichetta dell'asse da Rotate90 a Orizzontale.

## **Codice di Esempio**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Change Tick Label Direction Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;"></a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ChartTextDirectionType } = AsposeCells;

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
            const result = document.getElementById('result');

            if (!fileInput.files.length) {
                result.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            const worksheet = workbook.worksheets.get(0);

            const chart = worksheet.charts.get(0);

            chart.categoryAxis.tickLabels.directionType = ChartTextDirectionType.Horizontal;

            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputChangeChartDataLableDirection.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            result.innerHTML = '<p style="color: green;">Tick label direction changed. Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

I file sorgente e di output possono essere scaricati dai seguenti link.

[File sorgente](105480221.xlsx)

[File di output](105480223.xlsx)
