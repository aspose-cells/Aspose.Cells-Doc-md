---
title: Infoga en bild baserad på cellreferens med JavaScript via C++
linktitle: Infoga en bild baserat på cellreferens
type: docs
weight: 150
url: /sv/javascript-cpp/insert-a-picture-based-on-cell-reference/
description: Lär dig hur du infogar en bild i ett arbetsblad baserat på en cellreferens med Aspose.Cells for JavaScript via C++. Visa celldata i en bild.
---

{{% alert color="primary" %}}
Ibland har du en tom bild och behöver visa data eller innehåll i bilden genom att ange en cellreferens i formelfältet. Aspose.Cells stöder den här funktionen (Microsoft Excel 2010).
{{% /alert %}}

## Infoga en bild baserad på cellreferens

Aspose.Cells for JavaScript via C++ stöder att visa innehållet i en arbetsbladscell i en bildform. Du kan länka bilden till cellen som innehåller de data du vill visa. Eftersom cellen eller cellområdet är länkat till grafikobjektet, visas ändringar du gör i datan i den cellen eller cellområdet automatiskt i grafikelementet. Lägg till en bild i arbetsbladet genom att anropa [**ShapeCollection.addPicture(number, number, number, number, Uint8Array)**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/#addPicture-number-number-number-number-uint8array-)-metoden för [**ShapeCollection**](https://reference.aspose.com/cells/javascript-cpp/shapecollection)-samlingen (inkapslad i [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)-objektet). Ange cellområdet med hjälp av [**Picture.formula**](https://reference.aspose.com/cells/javascript-cpp/picture/#formula--)-attributet för [**Picture**](https://reference.aspose.com/cells/javascript-cpp/picture)-objektet.

### Kodexempel

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
