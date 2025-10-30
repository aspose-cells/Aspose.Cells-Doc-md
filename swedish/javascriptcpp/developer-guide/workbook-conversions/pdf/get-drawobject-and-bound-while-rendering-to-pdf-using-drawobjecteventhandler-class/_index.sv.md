---
title: Hämta DrawObject och Bound vid renderering till PDF med DrawObjectEventHandler klassen med JavaScript via C++
linktitle: Hämta DrawObject och Bound vid rendering till PDF med hjälp av DrawObjectEventHandler klassen
type: docs
weight: 70
url: /sv/javascript-cpp/get-drawobject-and-bound-while-rendering-to-pdf-using-drawobjecteventhandler-class/
---

## **Möjliga användningsscenario**

Aspose.Cells tillhandahåller en abstrakt klass [**DrawObjectEventHandler**](https://reference.aspose.com/cells/javascript-cpp/drawobjecteventhandler) som har en [**DrawObjectEventHandler.draw(DrawObject, number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/drawobjecteventhandler/#draw-drawobject-number-number-number-number-) metod. Användaren kan implementera [**DrawObjectEventHandler**](https://reference.aspose.com/cells/javascript-cpp/drawobjecteventhandler) och använda [**DrawObjectEventHandler.draw(DrawObject, number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/drawobjecteventhandler/#draw-drawobject-number-number-number-number-) metoden för att få [**DrawObject**](https://reference.aspose.com/cells/javascript-cpp/drawobject) och Bound under rendering av Excel till PDF eller Bild. Här är en kort beskrivning av parametrarna för [**DrawObjectEventHandler.draw(DrawObject, number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/drawobjecteventhandler/#draw-drawobject-number-number-number-number-) metoden.

- drawObject: [**DrawObject**](https://reference.aspose.com/cells/javascript-cpp/drawobject) kommer att initialiseras och returneras vid rendering.

- x: Vänster om [**DrawObject**](https://reference.aspose.com/cells/javascript-cpp/drawobject).

- y: Toppen av [**DrawObject**](https://reference.aspose.com/cells/javascript-cpp/drawobject).

- width: Bredden på [**DrawObject**](https://reference.aspose.com/cells/javascript-cpp/drawobject).

- height: Höjden på [**DrawObject**](https://reference.aspose.com/cells/javascript-cpp/drawobject).

Om du renderar Excel-fil till PDF kan du använda [**DrawObjectEventHandler**](https://reference.aspose.com/cells/javascript-cpp/drawobjecteventhandler)-klassen med [**PdfSaveOptions.drawObjectEventHandler**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#drawObjectEventHandler--)-egenskapen. På liknande sätt, om du renderar Excel-fil till Bild, kan du använda [**DrawObjectEventHandler**](https://reference.aspose.com/cells/javascript-cpp/drawobjecteventhandler)-klassen med [**ImageOrPrintOptions.drawObjectEventHandler**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/#drawObjectEventHandler--)-egenskapen.

## **Hämta DrawObject och gräns vid rendering till PDF med hjälp av DrawObjectEventHandler-klassen**

Se följande exempel på kod. Den laddar [exempel Excel-fil](64716821.xlsx) och sparar den som [utdata PDF](64716822.pdf). Vid rendering till PDF använder den [**PdfSaveOptions.drawObjectEventHandler**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#drawObjectEventHandler--) egenskapen och fångar [**DrawObject**](https://reference.aspose.com/cells/javascript-cpp/drawobject) och Bound av befintliga celler och objekt, t.ex. bilder. Om [**DrawObject**](https://reference.aspose.com/cells/javascript-cpp/drawobject)-typen är Cell, skriver den ut dess Bound och StringValue. Om [**DrawObject**](https://reference.aspose.com/cells/javascript-cpp/drawobject)-typen är Image, skriver den ut dess Bound och Shapes namn. Se konsolutdata för exemplet nedan för mer hjälp.

## **Exempelkod**

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

## **Konsoloutput**

{{< highlight java >}}

 [X]: 153.6035 [Y]: 82.94118 [Width]: 103.2035 [Height]: 14.47059 [Cell Value]: This is sample text.

----------------------

[X]: 267.6917 [Y]: 153.4853 [Width]: 160.4491 [Height]: 128.0647 [Shape Name]: Sun

----------------------

{{< /highlight >}}
