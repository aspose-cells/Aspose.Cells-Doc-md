---
title: ピボットアイテムの絶対位置を指定する
type: docs
weight: 50
url: /ja/javascript-cpp/specifying-the-absolute-position-of-the-pivot-item/
---

{{% alert color="primary" %}}

場合によっては、ユーザはピボットアイテムの絶対位置を指定する必要があります。Aspose.Cells for JavaScriptはこの要件を満たすための新しいプロパティとメソッドをいくつか公開しています。

- 親ノードに関係なくすべてのPivotItemsの位置インデックスを指定するために使用できる[**PivotItem.position**](https://reference.aspose.com/cells/javascript-cpp/pivotitem/#position-number-)プロパティが追加されました。- 同じ親ノード内のPivotItemsの位置インデックスを指定するために使用できる[**PivotItem.positionInSameParentNode**](https://reference.aspose.com/cells/javascript-cpp/pivotitem/#positionInSameParentNode-number-)プロパティが追加されました。
- PivotItemを移動するための[**PivotItem.move**](https://reference.aspose.com/cells/javascript-cpp/pivotitem/#move-number-boolean-)メソッドが追加されました。こちらでは、移動する位置数（count）に基づいてアイテムを上または下に移動します。count値がゼロ未満の場合、アイテムは上に移動し、count値がゼロより大きい場合は、PivotItemは下に移動します。isSameParentパラメータは、移動操作を同じ親ノード内で実行するかどうかを指定します。
- *PivotItem.move(int count)*メソッドは廃止されたため、新たに追加された[**PivotItem.move(number, boolean)**](https://reference.aspose.com/cells/javascript-cpp/pivotitem/#move-number-boolean-)メソッドを代わりに使用することを推奨します。

{{% /alert %}}

次のサンプルコードは、ピボットテーブルを作成し、その後、同じ親ノード内でのPivot Itemsの位置を指定しています。参照のために、[ソースExcel](5112632.xlsx)および[出力Excel](5112619.xlsx)ファイルをダウンロードできます。出力Excelファイルを開くと、「K11」の親での0番目の位置に「4H12」アイテムが、3番目の位置に「DIF400」が表示されます。同様に、CA32は1番目の位置にあり、AAA3は2番目の位置にあります。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells PivotTable Example</title>
    </head>
    <body>
        <h1>PivotTable Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PivotFieldType, PivotFieldSubtotalType } = AsposeCells;

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

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Add pivot worksheet and get data worksheet
            const wsPivot = workbook.worksheets.add("pvtNew Hardware");
            const wsData = workbook.worksheets.get("New Hardware - Yearly");

            // Get the pivottables collection for the pivot sheet
            const pivotTables = wsPivot.pivotTables;

            // Add PivotTable to the worksheet
            const index = pivotTables.add("='New Hardware - Yearly'!A1:D621", "A3", "HWCounts_PivotTable");

            // Get the PivotTable object
            const pvtTable = pivotTables.get(index);

            // Add vendor row field
            pvtTable.addFieldToArea(PivotFieldType.Row, "Vendor");

            // Add item row field
            pvtTable.addFieldToArea(PivotFieldType.Row, "Item");

            // Add data field
            pvtTable.addFieldToArea(PivotFieldType.Data, "2014");

            // Turn off the subtotals for the vendor row field
            const pivotField = pvtTable.rowFields.get("Vendor");
            pivotField.subtotals = PivotFieldSubtotalType.None;

            // Turn off grand total
            pvtTable.columnGrand = false;

            /*
             * Please call the PivotTable.refreshData() and PivotTable.calculateData()
             * before using PivotItem.setPosition,
             * PivotItem.setPositionInSameParentNode and PivotItem.move methods.
            */
            pvtTable.refreshData();
            pvtTable.calculateData();

            pvtTable.rowFields.get("Item").pivotItems.get("4H12").positionInSameParentNode = 0;
            pvtTable.rowFields.get("Item").pivotItems.get("DIF400").positionInSameParentNode = 3;

            /* 
             * As a result of using PivotItem.setPositionInSameParentNode,
             * it will change the original sort sequence.
             * So when you use PivotItem.setPositionInSameParentNode in another parent node.
             * You need call the method named "calculateData" again. 
            */
            pvtTable.calculateData();

            pvtTable.rowFields.get("Item").pivotItems.get("CA32").positionInSameParentNode = 1;
            pvtTable.rowFields.get("Item").pivotItems.get("AAA3").positionInSameParentNode = 2;

            // Saving the modified Excel file and providing a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">PivotTable created successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

{{% alert color="primary" %}}

注意: [**PivotItem.position**](https://reference.aspose.com/cells/javascript-cpp/pivotitem/#position-number-)、[**PivotItem.positionInSameParentNode**](https://reference.aspose.com/cells/javascript-cpp/pivotitem/#positionInSameParentNode-number-)プロパティおよび[**PivotItem.move**](https://reference.aspose.com/cells/javascript-cpp/pivotitem/#move-number-boolean-)メソッドを使用する前に、PivotTable.RefreshDataおよびPivotTable.CalculateDataメソッドを呼び出す必要があります。

{{% /alert %}}
