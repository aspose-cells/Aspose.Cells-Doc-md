---
title: Link Cells to XML Map Elements with JavaScript via C++
linktitle: Link Cells to XML Map Elements
type: docs
weight: 50
url: /javascript-cpp/link-cells-to-xml-map-elements/
---

## **Possible Usage Scenarios**

You can link your cells to XML Map elements using Aspose.Cells for JavaScript via C++. Please use the [**Cells.linkToXmlMap(string, number, number, string)**](https://reference.aspose.com/cells/javascript-cpp/cells/#linkToXmlMap-string-number-number-string-) method for this purpose.

## **Link Cells to XML Map Elements**

The following sample code loads the [source Excel file](5115471.xlsx), which contains an XML Map, and then links cells A1, B2, C3, D4, E5, and F6 to XML Map elements FIELD1, FIELD2, FIELD4, FIELD5, FIELD7, and FIELD8, respectively. It then saves the workbook to the [output Excel file](5115467.xlsx).

If you open the [output Excel file](5115467.xlsx) and click the **Developer > Source** button, you will see the cells are linked with XML Map elements and they will also be highlighted by Microsoft Excel as shown in this image.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Map XML to Cells Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell, Utils } = AsposeCells;
        
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

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the Xml Map inside it
            const map = workbook.worksheets.xmlMaps.get(0);

            // Access first worksheet
            const ws = workbook.worksheets.get(0);

            // Map FIELD1 and FIELD2 to cell A1 and B2
            ws.cells.linkToXmlMap(map.name, 0, 0, "/root/row/FIELD1");
            ws.cells.linkToXmlMap(map.name, 1, 1, "/root/row/FIELD2");

            // Map FIELD4 and FIELD5 to cell C3 and D4
            ws.cells.linkToXmlMap(map.name, 2, 2, "/root/row/FIELD4");
            ws.cells.linkToXmlMap(map.name, 3, 3, "/root/row/FIELD5");

            // Map FIELD7 and FIELD8 to cell E5 and F6
            ws.cells.linkToXmlMap(map.name, 4, 4, "/root/row/FIELD7");
            ws.cells.linkToXmlMap(map.name, 5, 5, "/root/row/FIELD8");

            // Save the workbook in xlsx format
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">XML mapped to cells successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```