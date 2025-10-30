---
title: Come inserire un immagine in una cella
type: docs
weight: 130
url: /it/javascript-cpp/how-to-insert-picture-in-cell/
description: Impara come inserire un immagine in una cella con Aspose.Cells for JavaScript tramite C++.
keywords: Come Inserire un Immagine in una Cella, Inserire un Immagine sopra le Celle, Posizionare un Immagine in una Cella, Posizionare un Immagine sopra le Celle, Come posizionare un immagine in una cella, Come posizionare un immagine sopra le celle, Passare dall Immagine in Cella all Immagine sopra le Celle, Passare dal Posizionamento in Cella al Posizionamento sopra le Celle.
---

## **Possibili Scenari di Utilizzo**
L'immagine aggiunge un tocco di luminosità al foglio di lavoro e fornisce una rappresentazione visiva del contenuto. Facilitano anche la comprensione dei dati e la formulazione di idee. Anche se da molti anni è possibile utilizzare le immagini in Excel, solo di recente excel ha abilitato la funzione delle immagini diventino effettivi valori della cella. Anche se il layout del disegno viene modificato, sarà comunque collegato ai dati. È possibile utilizzarlo in tabelle, ordinare, filtrare, includere nelle formule, e così via!

## **Come inserire un'immagine in una cella utilizzando Excel**
Su come inserire un'immagine in una cella in Excel, segui questi passaggi:

1. Vai alla scheda Inserisci e fai clic sull'opzione Immagini.
2. Seleziona **Posiziona in cella**. Seleziona una delle seguenti fonti dal menu a discesa Inserisci immagine da (**Questo dispositivo**, **Immagini stock** e **Immagini online**). Questo dispositivo per inserire immagini dal tuo dispositivo. Immagini stock per inserire immagini da immagini di archivio. Immagini online per inserire immagini dal web.
<br>
<img src="1.png" width=60% />
3. Seleziona l'immagine e inseriscila in una cella.
<br>
<img src="8.png" width=60% />

## **Come inserire un'immagine sopra le celle utilizzando Excel**
Per inserire un'immagine sopra le celle in Excel, seguire questi passaggi:

1. Vai alla scheda Inserisci e fai clic sull'opzione Immagini.
2. Seleziona **Posiziona sopra le celle**. Scegli una delle seguenti fonti dal menu a discesa Inserisci immagine da (**Questo dispositivo**, **Immagini in stock** e **Immagini online**). Questo dispositivo per inserire un'immagine dal tuo dispositivo. Immagini in stock per inserire un'immagine dalle immagini in stock. Immagini online per inserire un'immagine dal web.
<br>
<img src="2.png" width=60% />
3. Seleziona l'immagine e inseriscila sopra le celle.
<br>
<img src="3.png" width=60% />

## **Come passare da Immagine nella cella a Immagine sopra le celle usando Excel**
È possibile passare facilmente da **Immagine nella cella** a **Immagine sopra le celle**. Seguire questi passaggi:
1. Fare clic con il pulsante destro del mouse sulla cella e selezionare **Immagine nella cella** > **Posiziona sopra le celle**. 
<br>
<img src="4.png" width=60% />
2. Il risultato dopo il passaggio è il seguente:
<br>
<img src="5.png" width=60% />

## **Come passare da Immagine sopra le celle a Immagine nella cella usando Excel**
È possibile passare facilmente da **Immagine sopra le celle** a **Immagine nella cella**. Seguire questi passaggi:
1. Fare clic con il pulsante destro del mouse sull'immagine e selezionare **Posiziona nella cella**. 
<br>
<img src="6.png" width=60% />
2. Il risultato dopo il passaggio è il seguente:
<br>
<img src="7.png" width=60% />

## **Come Inserire Immagine in Cella usando Aspose.Cells for JavaScript tramite C++**
Inserire un'immagine nella cella utilizzando Aspose.Cells. Si prega di vedere il seguente codice di esempio. Dopo aver eseguito il codice di esempio, verrà inserita un'immagine in una cella.
1. Istanziare un oggetto Workbook. 
2. Ottenere la cella in cui si desidera inserire l'immagine.
3. Impostare la proprietà Cell.EmbeddedImage. 
4. Infine, salvare il libro di lavoro nel formato [output XLSX](out.xlsx). 

## **Codice di Esempio**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Embed Image into New Workbook</h1>
        <p>Select an image file to embed into cell D8. A new workbook will be created with "Apple" in A2.</p>
        <input type="file" id="imageInput" accept="image/*" />
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
            const imageInput = document.getElementById('imageInput');
            const resultDiv = document.getElementById('result');

            // Create a new workbook
            const workbook = new Workbook();
            const cells = workbook.worksheets.get(0).cells;

            // Set A2 value to "Apple"
            const a2 = cells.get("A2");
            a2.value = "Apple";

            // Get D8 cell
            const d8 = cells.get("D8");

            // If an image file is selected, read it and embed into D8
            if (imageInput.files.length) {
                const file = imageInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                const imgBuf = new Uint8Array(arrayBuffer);
                d8.embeddedImage = imgBuf;
            }

            // Save workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Workbook created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
