---
title: JavaScriptとC++を使用してXMLマップのルート要素名を見つける方法
linktitle: XML Mapのルート要素名を検索する
type: docs
weight: 30
url: /ja/javascript-cpp/find-the-root-element-name-of-xml-map/
description: C++のAspose.Cells for JavaScriptを使用してExcelのXMLマップのルート要素名を見つける方法を学びます。
---

## **可能な使用シナリオ**

C++のAspose.Cells for JavaScriptを使ってXMLマップのルート要素名を見つけることができます。以下のスクリーンショットはMicrosoft ExcelにおけるXMLマップのルート要素名を示しています。

![todo:image_alt_text](find-the-root-element-name-of-xml-map_1.png)

## **サンプルコード**

以下のサンプルコードは[サンプルExcelファイル](55541789.xlsx)をロードし、最初のXMLマップにアクセスしてその[**XmlMap.rootElementName**](https://reference.aspose.com/cells/javascript-cpp/xmlmap/#rootElementName--)プロパティを出力します。結果のコンソール出力も合わせてご覧ください。

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

## **コンソール出力**

{{< highlight java >}}

Root Element Name Of Xml Map: MiscData

{{< /highlight >}}
