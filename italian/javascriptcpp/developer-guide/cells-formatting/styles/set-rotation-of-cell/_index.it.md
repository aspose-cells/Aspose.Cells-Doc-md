---
title: Come ruotare il testo della cella
linktitle: Come ruotare il testo della cella  
type: docs  
weight: 80  
url: /it/javascript-cpp/how-to-rotate-text-of-cell/  
description: Impara come ruotare il testo di una cella programmaticamente usando Aspose.Cells for JavaScript via C++.  
keywords: JavaScript via C++ ruota il testo di una cella, JavaScript in modo programmatico ruota il testo di una cella nel workbook, imposta l angolo di rotazione della cella nel workbook in modo programmatico, come ruotare il testo di una cella in Excel con JavaScript  
---

## **Ruota il testo di una cella in Aspose.Cells for JavaScript via C++**

Aspose.Cells è un componente JavaScript potente che consente agli sviluppatori di lavorare con file Excel in modo programmatico. Una delle funzionalità offerte da Aspose.Cells è la possibilità di ruotare le celle, permettendo di personalizzare l'orientamento del testo e migliorare la presentazione visiva dei dati. In questo documento esploreremo come ruotare le celle usando Aspose.Cells.

## **Come ruotare il testo della cella in Excel**
Per ruotare una cella in Excel, è possibile utilizzare i seguenti passaggi:
1. Apri Excel e seleziona la cella o l'intervallo di celle che desideri ruotare.
1. Fai clic con il pulsante destro del mouse sulla cella (o le celle) selezionata(e) e scegli "Formato celle" dal menu contestuale. In alternativa, puoi andare alla scheda "Home" nel nastro di Excel, fare clic sulla visualizzazione a discesa "Formato" nel gruppo "Celle" e selezionare "Formato celle".
1. Nella finestra di dialogo "Formato celle", passa alla scheda "Allineamento".
1. Nella sezione "Orientamento", vedrai le opzioni per ruotare il testo. Puoi inserire direttamente l'angolo di rotazione desiderato in gradi nella casella "Gradi". I valori positivi ruotano il testo in senso antiorario e i valori negativi lo ruotano in senso orario.
<br>
![todo:image_alt_text](alignment.png)
1. Una volta selezionata la rotazione desiderata, fai clic su "OK" per applicare le modifiche. La/e cella/e selezionata/e verranno ora ruotate in base all'angolo di rotazione o orientamento scelto.

## **Come ruotare il testo della cella utilizzando l'API di Aspose.Cells**

La proprietà [**Style.rotationAngle(number)**](https://reference.aspose.com/cells/javascript-cpp/style/#rotationAngle-number-) rende comodo ruotare le celle. Per ruotare le celle in Aspose.Cells, è necessario seguire questi passaggi:
1. Carica il documento di lavoro di Excel  
<br>
Prima di tutto, è necessario caricare il workbook di Excel utilizzando Aspose.Cells. Puoi utilizzare la classe Workbook per aprire un file Excel esistente o crearne uno nuovo. 

1. Accedere al foglio di lavoro  
<br>
Una volta caricato il workbook, è necessario accedere al foglio di lavoro in cui si desidera ruotare le celle. Puoi accedere al foglio di lavoro tramite l'indice o il nome. 

1. Ruotare il testo della cella  
<br>
Ora che hai accesso al foglio di lavoro, puoi ruotare le celle modificando l'oggetto Style delle celle desiderate. L'oggetto Style ti consente di impostare diverse opzioni di formattazione, inclusa la rotazione. 

1. Salvare il workbook  
<br>
Dopo aver ruotato le celle, puoi salvare il workbook modificato su un file o un flusso utilizzando il metodo Save.

## **Codice di esempio JavaScript**

Vedi il seguente codice, crea un oggetto workbook e imposta diversi angoli di rotazione per varie celle. Lo screenshot mostra il risultato dopo l'esecuzione del codice di esempio.
<br>
<img src="rotation.png" width=80% />

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Rotate Text in Cells Example</h1>
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
            // Creating a new Workbook (blank)
            const workbook = new Workbook();

            // Obtaining the reference of the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Row index of the cell
            let row = 0;
            // Column index of the cell
            let column = 0; 

            let a1 = worksheet.cells.get(row, column);
            a1.putValue("a1 rotate text");
            let a1Style = a1.style;

            // Set the rotation angle in degrees
            a1Style.rotationAngle = 45; 
            a1.style = a1Style;

            // set Column index of the cell
            column = 1;
            let b1 = worksheet.cells.get(row, column);
            b1.putValue("b1 rotate text");
            let b1Style = b1.style;

            // Set the rotation angle in degrees
            b1Style.rotationAngle = 255;
            b1.style = b1Style;

            // set Column index of the cell
            column = 2;
            let c1 = worksheet.cells.get(row, column);
            c1.putValue("c1 rotate text");
            let c1Style = c1.style;

            // Set the rotation angle in degrees
            c1Style.rotationAngle = -90;
            c1.style = c1Style;

            // set Column index of the cell
            column = 3;
            let d1 = worksheet.cells.get(row, column);
            d1.putValue("d1 rotate text");
            let d1Style = d1.style;

            // Set the rotation angle in degrees
            d1Style.rotationAngle = -90;
            d1.style = d1Style;

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
