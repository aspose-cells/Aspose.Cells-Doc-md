---
title: Ottieni DrawObject e Bound durante il rendering in PDF utilizzando la classe DrawObjectEventHandler con JavaScript via C++
linktitle: Ottieni DrawObject e Bound durante la resa in PDF utilizzando la classe DrawObjectEventHandler
type: docs
weight: 70
url: /it/javascript-cpp/get-drawobject-and-bound-while-rendering-to-pdf-using-drawobjecteventhandler-class/
---

## **Possibili Scenari di Utilizzo**

Aspose.Cells fornisce una classe astratta [**DrawObjectEventHandler**](https://reference.aspose.com/cells/javascript-cpp/drawobjecteventhandler) che ha un metodo [**DrawObjectEventHandler.draw(DrawObject, number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/drawobjecteventhandler/#draw-drawobject-number-number-number-number-). L'utente può implementare [**DrawObjectEventHandler**](https://reference.aspose.com/cells/javascript-cpp/drawobjecteventhandler) e utilizzare il metodo [**DrawObjectEventHandler.draw(DrawObject, number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/drawobjecteventhandler/#draw-drawobject-number-number-number-number-) per ottenere l'oggetto [**DrawObject**](https://reference.aspose.com/cells/javascript-cpp/drawobject) e Bound durante il rendering di Excel in PDF o immagine. Di seguito una breve descrizione dei parametri del metodo [**DrawObjectEventHandler.draw(DrawObject, number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/drawobjecteventhandler/#draw-drawobject-number-number-number-number-).

- drawObject: [**DrawObject**](https://reference.aspose.com/cells/javascript-cpp/drawobject) verrà inizializzato e restituito durante il rendering.

- x: Sinistra di [**DrawObject**](https://reference.aspose.com/cells/javascript-cpp/drawobject).

- y: Sopra di [**DrawObject**](https://reference.aspose.com/cells/javascript-cpp/drawobject).

- width: Larghezza di [**DrawObject**](https://reference.aspose.com/cells/javascript-cpp/drawobject).

- height: Altezza di [**DrawObject**](https://reference.aspose.com/cells/javascript-cpp/drawobject).

Se stai renderizzando un file Excel in PDF, puoi utilizzare la classe [**DrawObjectEventHandler**](https://reference.aspose.com/cells/javascript-cpp/drawobjecteventhandler) con la proprietà [**PdfSaveOptions.drawObjectEventHandler**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#drawObjectEventHandler--). Similmente, se stai renderizzando un file Excel in immagine, puoi utilizzare la classe [**DrawObjectEventHandler**](https://reference.aspose.com/cells/javascript-cpp/drawobjecteventhandler) con la proprietà [**ImageOrPrintOptions.drawObjectEventHandler**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/#drawObjectEventHandler--).

## **Ottieni DrawObject e Bound durante il rendering in PDF utilizzando la classe DrawObjectEventHandler**

Consulta il seguente esempio di codice. Carica il [file Excel di esempio](64716821.xlsx) e lo salva come [output PDF](64716822.pdf). Durante il rendering in PDF, utilizza la proprietà [**PdfSaveOptions.drawObjectEventHandler**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#drawObjectEventHandler--) e cattura il [**DrawObject**](https://reference.aspose.com/cells/javascript-cpp/drawobject) e il Bound delle celle ed oggetti esistenti, ad esempio immagini. Se il tipo [**DrawObject**](https://reference.aspose.com/cells/javascript-cpp/drawobject) è Cell, stampa il suo Bound e StringValue. Se il tipo [**DrawObject**](https://reference.aspose.com/cells/javascript-cpp/drawobject) è Immagine, stampa il suo Bound e il nome della forma. Per maggiori dettagli, consulta l'output della console dell'esempio di codice di seguito.

## **Codice di Esempio**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Get Draw Object and Bound Using DrawObjectEventHandler</title>
    </head>
    <body>
        <h1>Get Draw Object and Bound Using DrawObjectEventHandler</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PdfSaveOptions, DrawObjectEventHandler, DrawObjectEnum } = AsposeCells;

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

        class ClsDrawObjectEventHandler extends DrawObjectEventHandler {
            draw(drawObject, x, y, width, height) {
                console.log("");

                // Print the coordinates and the value of Cell object
                if (drawObject.type === DrawObjectEnum.Cell) {
                    console.log(`[X]: ${x} [Y]: ${y} [Width]: ${width} [Height]: ${height} [Cell Value]: ${drawObject.cell.stringValue}`);
                }

                // Print the coordinates and the shape name of Image object
                if (drawObject.type === DrawObjectEnum.Image) {
                    console.log(`[X]: ${x} [Y]: ${y} [Width]: ${width} [Height]: ${height} [Shape Name]: ${drawObject.shape.name}`);
                }

                console.log("----------------------");
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

            // Load sample Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Specify Pdf save options
            const opts = new PdfSaveOptions();

            // Assign the instance of DrawObjectEventHandler class
            opts.drawObjectEventHandler = new ClsDrawObjectEventHandler();

            // Save to Pdf format with Pdf save options
            const outputData = workbook.save(SaveFormat.Pdf, opts);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputGetDrawObjectAndBoundUsingDrawObjectEventHandler.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            resultDiv.innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the PDF file.</p>';
        });
    </script>
</html>
```

## **Output della console**

{{< highlight java >}}

 [X]: 153.6035 [Y]: 82.94118 [Width]: 103.2035 [Height]: 14.47059 [Cell Value]: This is sample text.

----------------------

[X]: 267.6917 [Y]: 153.4853 [Width]: 160.4491 [Height]: 128.0647 [Shape Name]: Sun

----------------------

{{< /highlight >}}
