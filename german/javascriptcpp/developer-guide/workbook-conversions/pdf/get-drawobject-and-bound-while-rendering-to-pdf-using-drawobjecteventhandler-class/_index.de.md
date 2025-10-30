---
title: Verwenden Sie die DrawObjectEventHandler Klasse, um DrawObject und Bound beim Rendern in PDF zu erhalten, mit JavaScript via C++
linktitle: Holen Sie sich DrawObject und Bound während des Renderns im PDF mit der DrawObjectEventHandler Klasse
type: docs
weight: 70
url: /de/javascript-cpp/get-drawobject-and-bound-while-rendering-to-pdf-using-drawobjecteventhandler-class/
---

## **Mögliche Verwendungsszenarien**

Aspose.Cells stellt eine abstrakte Klasse [**DrawObjectEventHandler**](https://reference.aspose.com/cells/javascript-cpp/drawobjecteventhandler) bereit, die eine [**DrawObjectEventHandler.draw(DrawObject, number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/drawobjecteventhandler/#draw-drawobject-number-number-number-number-) Methode hat. Der Benutzer kann [**DrawObjectEventHandler**](https://reference.aspose.com/cells/javascript-cpp/drawobjecteventhandler) implementieren und die [**DrawObjectEventHandler.draw(DrawObject, number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/drawobjecteventhandler/#draw-drawobject-number-number-number-number-) Methode nutzen, um die [**DrawObject**](https://reference.aspose.com/cells/javascript-cpp/drawobject) und Bound beim Rendern von Excel zu PDF oder Bild zu erhalten. Hier ist eine kurze Beschreibung der Parameter der [**DrawObjectEventHandler.draw(DrawObject, number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/drawobjecteventhandler/#draw-drawobject-number-number-number-number-) Methode.

- drawObject: [**DrawObject**](https://reference.aspose.com/cells/javascript-cpp/drawobject) wird initialisiert und beim Rendern zurückgegeben.

- x: Linke Seite von [**DrawObject**](https://reference.aspose.com/cells/javascript-cpp/drawobject).

- y: Obere Seite von [**DrawObject**](https://reference.aspose.com/cells/javascript-cpp/drawobject).

- width: Breite von [**DrawObject**](https://reference.aspose.com/cells/javascript-cpp/drawobject).

- height: Höhe von [**DrawObject**](https://reference.aspose.com/cells/javascript-cpp/drawobject).

Wenn Sie eine Excel-Datei in PDF umwandeln, können Sie die Klasse [**DrawObjectEventHandler**](https://reference.aspose.com/cells/javascript-cpp/drawobjecteventhandler) mit der Eigenschaft [**PdfSaveOptions.drawObjectEventHandler**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#drawObjectEventHandler--) verwenden. Ebenso können Sie bei der Umwandlung in ein Bild die Klasse [**DrawObjectEventHandler**](https://reference.aspose.com/cells/javascript-cpp/drawobjecteventhandler) mit der Eigenschaft [**ImageOrPrintOptions.drawObjectEventHandler**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/#drawObjectEventHandler--) verwenden.

## **Holen Sie sich DrawObject und Bound beim Rendern in PDF mit der DrawObjectEventHandler-Klasse**

Siehe den folgenden Beispielcode. Es lädt die [Beispiel-Excel-Datei](64716821.xlsx) und speichert sie als [Ausgabe-PDF](64716822.pdf). Beim Rendern zu PDF nutzt es die [**PdfSaveOptions.drawObjectEventHandler**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#drawObjectEventHandler--) Eigenschaft und erfasst die [**DrawObject**](https://reference.aspose.com/cells/javascript-cpp/drawobject) und Bound bestehender Zellen und Objekte, z.B. Bilder. Wenn der [**DrawObject**](https://reference.aspose.com/cells/javascript-cpp/drawobject) Typ Cell ist, werden Bound und StringValue ausgegeben. Ist der [**DrawObject**](https://reference.aspose.com/cells/javascript-cpp/drawobject) Typ Image, werden Bound und Shape-Name ausgegeben. Siehe den Konsolenausdruck des unten angegebenen Beispielcodes für mehr Hilfe.

## **Beispielcode**

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

## **Konsolenausgabe**

{{< highlight java >}}

 [X]: 153.6035 [Y]: 82.94118 [Width]: 103.2035 [Height]: 14.47059 [Cell Value]: This is sample text.

----------------------

[X]: 267.6917 [Y]: 153.4853 [Width]: 160.4491 [Height]: 128.0647 [Shape Name]: Sun

----------------------

{{< /highlight >}}
