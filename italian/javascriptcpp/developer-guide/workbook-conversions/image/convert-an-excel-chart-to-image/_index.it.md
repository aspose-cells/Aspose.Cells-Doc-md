---
title: Converti un grafico Excel in immagine con JavaScript tramite C++
linktitle: Convertire un grafico Excel in un immagine
type: docs
weight: 20
url: /it/javascript-cpp/convert-an-excel-chart-to-image/
description: Impara come convertire i grafici Excel in immagini usando Aspose.Cells for JavaScript tramite C++.
---

{{% alert color="primary" %}}  

I grafici sono visivamente accattivanti e facilitano la visualizzazione di confronti, modelli e tendenze nei dati. Ad esempio, anziché analizzare colonne di numeri di fogli di lavoro, un grafico mostra in un colpo d'occhio se le vendite stanno aumentando o diminuendo, o come le vendite effettive si confrontano con le vendite previste. Spesso viene chiesto alle persone di presentare informazioni statistiche e grafiche in modo semplice da capire e da mantenere. Un'immagine aiuta.  

A volte, sono necessari grafici in un'applicazione o pagine web. Oppure può essere necessario per un documento Word, un file PDF, una presentazione PowerPoint o altre applicazioni. In ogni caso, vuoi rendere il grafico come immagine in modo da poterlo usare altrove.  

{{% /alert %}}  

## **Conversione di grafici in immagini**  

Negli esempi qui, un grafico a torta e un grafico a colonne vengono convertiti in immagini.  

### **Conversione di un grafico a torta in un file immagine**  

Prima, crea un grafico a torta in Microsoft Excel e poi convertilo in un file immagine con Aspose.Cells for JavaScript tramite C++. Il codice in questo esempio crea un’immagine EMF basata sul grafico a torta nel file Excel modello.  

|**Output: immagine grafico a torta**|  
| :- |  
|![todo:image_alt_text](convert-an-excel-chart-to-image_1.png)|  

1. Crea un grafico a torta in Microsoft Excel:  
   1. Apri un nuovo foglio di lavoro in Microsoft Excel.  
   1. Inserisci alcuni dati in un foglio di lavoro.  
   1. Crea un grafico a torta in base ai dati.  
   1. Salvare il file.  

|**Il file di input.**|  
| :- |  
|![todo:image_alt_text](convert-an-excel-chart-to-image_2.png)|  

1. Scarica e installa Aspose.Cells:  
   1. [Scarica Aspose.Cells for JavaScript tramite C++](https://downloads.aspose.com/cells/javascript-cpp).  
   1. Installalo sul tuo computer di sviluppo.  

Tutti i [componenti Aspose](http://www.aspose.com/) funzionano in modalità di valutazione quando vengono installati per la prima volta. La modalità di valutazione non ha limiti temporali e inserisce solo filigrane nei documenti di output.  

1. Crea un progetto:  
   1. Avvia il tuo IDE preferito.  
   1. Crea una nuova applicazione console. Questo esempio utilizza un'applicazione JavaScript, ma puoi crearlo usando qualsiasi ambiente di runtime JavaScript.  
   1. Aggiungi un riferimento. Questo progetto utilizza Aspose.Cells quindi aggiungi un riferimento a Aspose.Cells for JavaScript tramite C++.  
   1. Scrivi il codice che trova e converte il grafico. Qui di seguito c'è il codice utilizzato dal componente per completare il compito. Vengono utilizzate pochissime righe di codice.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Convert Chart to Image Example</h1>
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

            // Get the designer chart (first chart) in the first worksheet of the workbook.
            const chart = workbook.worksheets.get(0).charts.get(0);

            // Convert the chart to an image (EMF) and prepare download link
            const imageData = chart.toImage(AsposeCells.ImageType.Emf);
            const blob = new Blob([imageData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'PieChart.out.emf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Chart Image';

            document.getElementById('result').innerHTML = '<p style="color: green;">Chart converted to EMF successfully! Click the download link to get the image.</p>';
        });
    </script>
</html>
```  

### **Conversione di un grafico a colonne in un file immagine**  

Per prima cosa, crea un grafico a colonne in Microsoft Excel e convertilo in un file immagine, come sopra. Dopo aver eseguito il codice di esempio, viene creato un file JPEG basato sul grafico a colonne nel file Excel di modello.  

|**File di output: un'immagine del grafico a colonne.**|  
| :- |  
|![todo:image_alt_text](convert-an-excel-chart-to-image_3.png)|  

1. Creare un grafico a colonne in Microsoft Excel:  
   1. Apri un nuovo foglio di lavoro in Microsoft Excel.  
   1. Inserisci alcuni dati in un foglio di lavoro.  
   1. Crea un grafico a colonne basato sui dati.  
   1. Salvare il file.  

|**File di input.**|  
| :- |  
|![todo:image_alt_text](convert-an-excel-chart-to-image_4.png)|  

1. Impostare un progetto, con riferimenti, come descritto sopra.  
1. Convertire il grafico in un'immagine in modo dinamico. Di seguito è riportato il codice utilizzato dal componente per portare a termine il compito. Il codice è simile a quello precedente:  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Convert Chart to Image</title>
    </head>
    <body>
        <h1>Convert Chart to Image</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ImageType, Utils } = AsposeCells;

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

            // Get the designer chart (first chart) in the first worksheet of the workbook.
            const chart = workbook.worksheets.get(0).charts.get(0);

            // Convert the chart to an image (JPEG)
            const imageData = await chart.toImage(ImageType.Jpeg);

            // Create a Blob and provide a download link
            const blob = new Blob([imageData], { type: 'image/jpeg' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'ColumnChart.out.jpeg';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Chart Image';

            document.getElementById('result').innerHTML = '<p style="color: green;">Chart converted to image successfully! Click the download link to get the image.</p>';
        });
    </script>
</html>
```
