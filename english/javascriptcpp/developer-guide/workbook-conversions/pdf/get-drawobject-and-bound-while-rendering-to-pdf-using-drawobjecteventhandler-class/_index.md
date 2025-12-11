---
title: Get DrawObject and Bound while rendering to PDF using DrawObjectEventHandler class with JavaScript via C++
linktitle: Get DrawObject and Bound while rendering to PDF using DrawObjectEventHandler class
type: docs
weight: 70
url: /javascript-cpp/get-drawobject-and-bound-while-rendering-to-pdf-using-drawobjecteventhandler-class/
---

## **Possible Usage Scenarios**

Aspose.Cells provides an abstract class [**DrawObjectEventHandler**](https://reference.aspose.com/cells/javascript-cpp/drawobjecteventhandler) which has a [**DrawObjectEventHandler.draw(DrawObject, number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/drawobjecteventhandler/#draw-drawobject-number-number-number-number-) method. The user can implement [**DrawObjectEventHandler**](https://reference.aspose.com/cells/javascript-cpp/drawobjecteventhandler) and utilize the [**DrawObjectEventHandler.draw(DrawObject, number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/drawobjecteventhandler/#draw-drawobject-number-number-number-number-) method to obtain the **DrawObject** and its bounds while rendering Excel to PDF or image. Here is a brief description of the parameters of the [**DrawObjectEventHandler.draw(DrawObject, number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/drawobjecteventhandler/#draw-drawobject-number-number-number-number-) method.

- **drawObject**: The **DrawObject** that will be initialized and returned during rendering.  
- **x**: Left coordinate of the **DrawObject**.  
- **y**: Top coordinate of the **DrawObject**.  
- **width**: Width of the **DrawObject**.  
- **height**: Height of the **DrawObject**.

If you are rendering an Excel file to PDF, you can utilize the **DrawObjectEventHandler** class with the [**PdfSaveOptions.drawObjectEventHandler**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#drawObjectEventHandler--) property. Similarly, if you are rendering an Excel file to an image, you can use the **DrawObjectEventHandler** class with the [**ImageOrPrintOptions.drawObjectEventHandler**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/#drawObjectEventHandler--) property.

## **Get DrawObject and Bound while rendering to PDF using DrawObjectEventHandler class**

Please see the following sample code. It loads the [sample Excel file](64716821.xlsx) and saves it as [output PDF](64716822.pdf). While rendering to PDF, it utilizes the [**PdfSaveOptions.drawObjectEventHandler**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#drawObjectEventHandler--) property and captures the **DrawObject** and its bounds for existing cells and objects, e.g., images, etc. If the **DrawObject** type is **Cell**, it prints its bounds and string value. If the **DrawObject** type is **Image**, it prints its bounds and shape name. Please see the console output of the sample code below for further clarification.

## **Sample Code**

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

                // Print the coordinates and the value of the cell object
                if (drawObject.type === DrawObjectEnum.Cell) {
                    console.log(`[X]: ${x} [Y]: ${y} [Width]: ${width} [Height]: ${height} [Cell Value]: ${drawObject.cell.stringValue}`);
                }

                // Print the coordinates and the shape name of the image object
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

            // Load the Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Specify PDF save options
            const opts = new PdfSaveOptions();

            // Assign the instance of DrawObjectEventHandler class
            opts.drawObjectEventHandler = new ClsDrawObjectEventHandler();

            // Save to PDF format with the specified options
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

## **Console Output**

{{< highlight java >}}

[X]: 153.6035 [Y]: 82.94118 [Width]: 103.2035 [Height]: 14.47059 [Cell Value]: This is sample text.

----------------------

[X]: 267.6917 [Y]: 153.4853 [Width]: 160.4491 [Height]: 128.0647 [Shape Name]: Sun

----------------------

{{< /highlight >}}