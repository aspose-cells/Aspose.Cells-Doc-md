---
title: Bestäm om Shape är en Smart Art Shape med JavaScript via C++
linktitle: Avgöra om en form är Smart Art Shape
type: docs
weight: 400
url: /sv/javascript-cpp/determine-if-shape-is-smart-art-shape/
description: Lär dig hur man avgör om en form i Excel är en Smart Art form med Aspose.Cells for JavaScript via C++.
---

## **Möjliga användningsscenario**  

Smart Art-former är speciella former i Microsoft Excel som tillåter dig att skapa komplexa diagram automatiskt. Du kan ta reda på om formen är en smart art-form eller en vanlig form med hjälp av [**Shape.isSmartArt()**](https://reference.aspose.com/cells/javascript-cpp/shape/#isSmartArt--) egenskapen.  

## **Avgör om formen är en SmartArt-form**  

Följande exempelkod laddar den [provexemplet](55541792.xlsx) som innehåller en smart art-form som visas i denna skärmdump. Den skriver ut värdet av [**Shape.isSmartArt()**](https://reference.aspose.com/cells/javascript-cpp/shape/#isSmartArt--) egenskapen för den första formen. Se vänligen exempelutdata i konsolen nedan.  

![todo:image_alt_text](determine-if-shape-is-smart-art-shape_1.png)  

## **Exempelkod**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Example Title</h1>
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

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Accessing the first shape
            const shape = worksheet.shapes.get(0);

            // Determine if shape is smart art (converted to property access)
            const isSmartArt = shape.isSmartArt;

            document.getElementById('result').innerHTML = `<p>Is Smart Art Shape: ${isSmartArt}</p>`;
        });
    </script>
</html>
```  

## **Konsoloutput**  

{{< highlight java >}}  

Is Smart Art Shape: True  

{{< /highlight >}}
