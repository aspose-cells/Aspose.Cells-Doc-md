---
title: JavaScriptを使用してOData接続情報を取得する方法（C++経由）
linktitle: OData接続情報を取得する方法
type: docs
weight: 60
url: /ja/javascript-cpp/how-to-get-odata-connection-information/
description: C++経由でAspose.Cells for JavaScriptを使用し、ExcelファイルからOData接続情報を抽出する方法を学びます。
---

## **OData接続情報を取得**

開発者がExcelファイルからOData情報を抽出する必要がある場合があります。Aspose.Cells for JavaScriptをC++で使用すると、DataMashup情報を返す[**Workbook.dataMashup**](https://reference.aspose.com/cells/javascript-cpp/workbook/#dataMashup--)プロパティがあります。この情報は[**DataMashup**](https://reference.aspose.com/cells/javascript-cpp/datamashup)クラスによって表されます。[**DataMashup**](https://reference.aspose.com/cells/javascript-cpp/datamashup)クラスは[**DataMashup.powerQueryFormulas**](https://reference.aspose.com/cells/javascript-cpp/datamashup/#powerQueryFormulas--)プロパティを提供し、[**PowerQueryFormulaCollection**](https://reference.aspose.com/cells/javascript-cpp/powerqueryformulacollection)コレクションを返します。[**PowerQueryFormulaCollection**](https://reference.aspose.com/cells/javascript-cpp/powerqueryformulacollection)からは[**PowerQueryFormula**](https://reference.aspose.com/cells/javascript-cpp/powerqueryformula)と[**PowerQueryFormulaItem**](https://reference.aspose.com/cells/javascript-cpp/powerqueryformulaitem)へアクセスできます。

次のコードスニペットは、これらのクラスを使用してOData情報を取得する方法を示しています。

以下のコードスニペットで使用されるソースファイルは参照用に添付されています。

[ソースファイル](96928098.xlsx)

### **サンプルコード**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Read Power Query Formulas</title>
    </head>
    <body>
        <h1>Read Power Query Formulas Example</h1>
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

            // Instantiating a Workbook object by loading the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access DataMashup and its PowerQueryFormulas collection
            const PQFcoll = workbook.dataMashup.powerQueryFormulas;

            let html = '<h2>Power Query Formulas</h2>';
            if (!PQFcoll || PQFcoll.count === 0) {
                html += '<p>No Power Query formulas found.</p>';
            } else {
                for (let i = 0; i < PQFcoll.count; i++) {
                    const PQF = PQFcoll.get(i);
                    html += `<h3>Connection Name: ${PQF.name}</h3>`;
                    const PQFIcoll = PQF.powerQueryFormulaItems;
                    if (!PQFIcoll || PQFIcoll.count === 0) {
                        html += '<p>No items found for this connection.</p>';
                    } else {
                        html += '<ul>';
                        for (let j = 0; j < PQFIcoll.count; j++) {
                            const PQFI = PQFIcoll.get(j);
                            html += `<li><strong>Name:</strong> ${PQFI.name} <br/><strong>Value:</strong> ${PQFI.value}</li>`;
                        }
                        html += '</ul>';
                    }
                }
            }

            document.getElementById('result').innerHTML = html;
        });
    </script>
</html>
```

### **コンソール出力**

{{< highlight java >}}

Connection Name: Orders

Name: Source

Value: OData.Feed("https://services.odata.org/V3/Northwind/Northwind.svc/", null, [Implementation="2.0"])

Name: Orders_table

Value: Source{[Name="Orders",Signature="table"]}[Data]

{{< /highlight >}}
