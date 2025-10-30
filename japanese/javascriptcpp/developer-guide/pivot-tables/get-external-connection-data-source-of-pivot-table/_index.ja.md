---
title: ピボットテーブルの外部接続データソースの取得
type: docs
weight: 150
url: /ja/javascript-cpp/get-external-connection-data-source-of-pivot-table/
description: Aspose.Cells for JavaScriptを使用してピボットテーブルの外部接続データソースを取得する方法。
keywords: Excel、Excel JavaScriptライブラリを使用したAspose.Cells for JavaScriptによるピボットテーブルの外部接続データソース取得。
---

## **Pivot Table の外部接続データソースの取得方法**

 Aspose.Cells for JavaScriptは、ピボットテーブルの外部接続データソースを取得する機能を提供しています。このために、APIは[**externalConnectionDataSource**](https://reference.aspose.com/cells/javascript-cpp/pivottable/#externalConnectionDataSource--)プロパティを持つ[**PivotTable**](https://reference.aspose.com/cells/javascript-cpp/pivottable/)クラスを提供します。[**externalConnectionDataSource**](https://reference.aspose.com/cells/javascript-cpp/pivottable/#externalConnectionDataSource--)プロパティは[**ExternalConnection**](https://reference.aspose.com/cells/javascript-cpp/externalconnection/)オブジェクトを返します。以下のコードスニペットは、[**externalConnectionDataSource**](https://reference.aspose.com/cells/javascript-cpp/pivottable/#externalConnectionDataSource--)プロパティを使用してピボットテーブルの外部接続データソースを取得する例です。

## **サンプルコード**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Pivot Table External Connection Example</title>
    </head>
    <body>
        <h1>Pivot Table External Connection Example</h1>
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
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by opening the selected Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Get the pivot table
            const pivotTable = worksheet.pivotTables.get(0);

            // Get external connection data source
            const externalConnection = pivotTable.externalConnectionDataSource;

            const name = externalConnection.name;
            const type = externalConnection.type;

            console.log("External Connection Data Source");
            console.log("Name: " + name);
            console.log("Type: " + type);

            resultDiv.innerHTML = `<p style="color: green;">External Connection Data Source</p>
                                   <p>Name: ${name}</p>
                                   <p>Type: ${type}</p>`;
        });
    </script>
</html>
```

コードスニペットで使用されるソースファイルは、参照用に添付されています。

[ソースファイル](104398862.xlsx)
