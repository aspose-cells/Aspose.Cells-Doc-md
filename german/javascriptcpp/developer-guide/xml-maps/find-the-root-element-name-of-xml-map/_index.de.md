---
title: Finden Sie den Namen des Root Elements der XML Karte mit JavaScript via C++
linktitle: Ermitteln Sie den Root Elementnamen der XML Map
type: docs
weight: 30
url: /de/javascript-cpp/find-the-root-element-name-of-xml-map/
description: Lernen Sie, wie Sie den Namen des Root Elements einer XML Karte in Excel mit Aspose.Cells for JavaScript via C++ finden.
---

## **Mögliche Verwendungsszenarien**

Sie können den *Root-Element-Namen der XML-Karte* mit Aspose.Cells for JavaScript via C++ mit der Eigenschaft [**XmlMap.rootElementName**](https://reference.aspose.com/cells/javascript-cpp/xmlmap/#rootElementName--) finden. Das folgende Screenshot zeigt den Namen des Root-Elements der XML-Karte in Microsoft Excel.

![todo:image_alt_text](find-the-root-element-name-of-xml-map_1.png)

## **Beispielcode**

Der folgenden Beispielcode lädt die [Beispieldatei Excel](55541789.xlsx) und greift auf die erste XML-Karte zu, um deren [**XmlMap.rootElementName**](https://reference.aspose.com/cells/javascript-cpp/xmlmap/#rootElementName--)-Eigenschaft auszugeben. Bitte sehen Sie sich die Konsolenausgabe des Beispielcodes unten an.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Get Root Element Name Of Xml Map</h1>
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

            // Access first Xml Map inside the Workbook
            const xmap = workbook.worksheets.xmlMaps.get(0);

            // Get Root Element Name of Xml Map
            const rootName = xmap.rootElementName;

            // Display result
            resultDiv.innerHTML = `<p>Root Element Name Of Xml Map: ${rootName}</p>`;
            console.log("Root Element Name Of Xml Map: " + rootName);
        });
    </script>
</html>
```

## **Konsolenausgabe**

{{< highlight java >}}

Root Element Name Of Xml Map: MiscData

{{< /highlight >}}
