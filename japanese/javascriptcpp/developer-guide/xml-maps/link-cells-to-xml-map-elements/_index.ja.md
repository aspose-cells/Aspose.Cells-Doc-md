---
title: JavaScriptとC++を使用してセルとXMLマップの要素をリンクします。
linktitle: セルをXML Map要素にリンク
type: docs
weight: 50
url: /ja/javascript-cpp/link-cells-to-xml-map-elements/
---

## **可能な使用シナリオ**

C++のAspose.Cells for JavaScriptを使用してセルをXMLマップ要素にリンクできます。この目的には[**Cells.linkToXmlMap(string, number, number, string)**](https://reference.aspose.com/cells/javascript-cpp/cells/#linkToXmlMap-string-number-number-string-)メソッドを使用してください。

## **セルをXMLマップ要素にリンクする**

次のサンプルコードは、XML Mapを含む[source excel file](5115471.xlsx)を読み込み、セルA1、B2、C3、D4、E5、F6をそれぞれXML Map要素FIELD1、FIELD2、FIELD4、FIELD5、FIELD7、FIELD8にリンクし、[output excel file](5115467.xlsx)としてブックを保存します。

[output excel file](5115467.xlsx)を開いて、開発者 > ソース ボタンをクリックすると、セルがXMLマップの要素にリンクされ、Microsoft Excelによって強調表示されます。

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
