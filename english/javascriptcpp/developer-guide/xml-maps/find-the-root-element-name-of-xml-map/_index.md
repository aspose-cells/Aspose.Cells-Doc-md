---
title: Find the Root Element Name of XML Map with JavaScript via C++
linktitle: Find the Root Element Name of XML Map
type: docs
weight: 30
url: /javascript-cpp/find-the-root-element-name-of-xml-map/
description: Learn how to find the root element name of an XML map in Excel using Aspose.Cells for JavaScript via C++.
---

## **Possible Usage Scenarios**

You can find the *Root Element Name of the XML Map* using Aspose.Cells for JavaScript via C++ with the [**XmlMap.rootElementName**](https://reference.aspose.com/cells/javascript-cpp/xmlmap/#rootElementName--) property. The following screenshot shows the root element name of the XML Map in Microsoft Excel.

![todo:image_alt_text](find-the-root-element-name-of-xml-map_1.png)

## **Sample Code**

The following sample code loads the [sample Excel file](55541789.xlsx) and accesses the first XML Map and prints its [**XmlMap.rootElementName**](https://reference.aspose.com/cells/javascript-cpp/xmlmap/#rootElementName--) property. Please see the console output of the sample code given below.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Get Root Element Name of XML Map</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Get Root Element Name</button>
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
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object using the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first XML Map inside the Workbook
            const xmap = workbook.worksheets.xmlMaps.get(0);

            // Get Root Element Name of XML Map
            const rootName = xmap.rootElementName;

            // Display result
            resultDiv.innerHTML = `<p>Root Element Name of XML Map: ${rootName}</p>`;
            console.log("Root Element Name of XML Map: " + rootName);
        });
    </script>
</html>
```

## **Console Output**

{{< highlight plaintext >}}
Root Element Name of XML Map: MiscData
{{< /highlight >}}