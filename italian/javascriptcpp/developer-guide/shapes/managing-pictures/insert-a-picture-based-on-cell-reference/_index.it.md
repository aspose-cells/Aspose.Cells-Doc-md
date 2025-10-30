---
title: Inserisci una immagine basata su riferimento di cella con JavaScript tramite C++
linktitle: Inserisci un immagine basata sul riferimento della cella
type: docs
weight: 150
url: /it/javascript-cpp/insert-a-picture-based-on-cell-reference/
description: Impara come inserire un immagine in un foglio di lavoro basata su un riferimento di cella usando Aspose.Cells for JavaScript tramite C++. Mostra i dati della cella in un immagine.
---

{{% alert color="primary" %}}
A volte hai un'immagine vuota e devi mostrare dati o contenuti nell'immagine impostando un riferimento nella Barra delle formule. Aspose.Cells supporta questa funzionalità (Microsoft Excel 2010).
{{% /alert %}}

## Inserimento di un'immagine basata sul riferimento della cella

Aspose.Cells for JavaScript tramite C++ supporta la visualizzazione del contenuto di una cella del foglio di lavoro in una forma di immagine. Puoi collegare l'immagine alla cella che contiene i dati che desideri mostrare. Poiché la cella o l'intervallo di celle è collegato all'oggetto grafico, le modifiche apportate ai dati in quella cella o intervallo di celle appaiono automaticamente nell'oggetto grafico. Aggiungi un'immagine al foglio di lavoro chiamando il metodo [**ShapeCollection.addPicture(number, number, number, number, Uint8Array)**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/#addPicture-number-number-number-number-uint8array-) della collezione [**ShapeCollection**](https://reference.aspose.com/cells/javascript-cpp/shapecollection) (incapsulato nell'oggetto [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)). Specifica l'intervallo di celle utilizzando l'attributo [**Picture.formula**](https://reference.aspose.com/cells/javascript-cpp/picture/#formula--) dell'oggetto [**Picture**](https://reference.aspose.com/cells/javascript-cpp/picture).

### Esempio di codice

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Referenced Picture Example</h1>
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
            // Instantiate a new Workbook
            const workbook = new Workbook();
            // Get the first worksheet's cells collection
            const cells = workbook.worksheets.get(0).cells;

            // Add string values to the cells
            cells.get("A1").value = "A1";
            cells.get("C10").value = "C10";

            // Get the conditional icon's image data
            const imagedata = AsposeCells.ConditionalFormattingIcon.iconImageData(AsposeCells.IconSetType.TrafficLights31, 0);
            // Create a stream based on the image data
            const stream = Uint8Array.from(imagedata);

            // Add a blank picture to the D1 cell
            const pic = workbook.worksheets.get(0).shapes.addPicture(0, 3, stream, 10, 10);
            // Specify the formula that refers to the source range of cells
            pic.formula = "A1:C10";
            // Update the shapes selected value in the worksheet
            workbook.worksheets.get(0).shapes.updateSelectedValue();

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'referencedpicture.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
