---
title: ピボットテーブルを挿入する
linktitle: ピボットテーブル
type: docs
weight: 160
url: /ja/javascript-cpp/create-pivot-table/
description: Excelスプレッドシートファイルのピボットテーブルを作成し、書式を設定する。
---

## **ピボットテーブルの作成**

C++経由のAspose.Cells for JavaScriptを使用して、ピボットテーブルをスプレッドシートにプログラム的に追加することが可能です。

### **ピボットテーブルオブジェクトモデル**

C++経由のAspose.Cells for JavaScriptは、ピボットテーブルを作成および制御するための特別なクラスセットを提供します。これらのクラスは、ピボットテーブルの構築要素である[**PivotTable**](https://reference.aspose.com/cells/javascript-cpp/pivottable)オブジェクトを作成し設定するために使用されます。これらのオブジェクトは：

- [**PivotField**](https://reference.aspose.com/cells/javascript-cpp/pivotfield)は、[**PivotTable**](https://reference.aspose.com/cells/javascript-cpp/pivottable)のフィールドを表します。
- [**PivotFieldCollection**](https://reference.aspose.com/cells/javascript-cpp/pivotfieldcollection)は、[**PivotTable**](https://reference.aspose.com/cells/javascript-cpp/pivottable)のすべての[**PivotField**](https://reference.aspose.com/cells/javascript-cpp/pivotfield)オブジェクトのコレクションを表します。
- [**PivotTable**](https://reference.aspose.com/cells/javascript-cpp/pivottable)は、ワークシート上のPivotTableを表します。
- [**PivotTableCollection**](https://reference.aspose.com/cells/javascript-cpp/pivottablecollection)は、ワークシート上のすべての[**PivotTable**](https://reference.aspose.com/cells/javascript-cpp/pivottable)オブジェクトのコレクションを表します。

### **Aspose.Cellsを使用して簡単なピボットテーブルを作成する**

1. [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell)オブジェクトの[**putValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#putValue-boolean-)メソッドを使用してワークシートにデータを追加します。
   このデータは、ピボットテーブルのデータソースとして使用されます。
1. ワークシートにピボットテーブルを追加するために、[**PivotTables**](https://reference.aspose.com/cells/javascript-cpp/pivottablecollection)コレクションの[**add**](https://reference.aspose.com/cells/javascript-cpp/pivottablecollection/#add-string-string-string-)メソッドを呼び出します。このメソッドはWorksheetオブジェクトでカプセル化されています。
1. 新しい[**PivotTable**](https://reference.aspose.com/cells/javascript-cpp/pivottable)オブジェクトを[**PivotTables**](https://reference.aspose.com/cells/javascript-cpp/pivottablecollection)コレクションから取得します。このコレクションはPivotTableのインデックスを渡すことでアクセスできます。
1. ピボットテーブルを管理するために、上記で説明した[**PivotTable**](https://reference.aspose.com/cells/javascript-cpp/pivottable)のいずれかを使用します。

例のコードを実行すると、ワークシートにピボットテーブルが追加されます。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Create Pivot Table Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;

        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");

            document.getElementById('runExample').addEventListener('click', async () => {
                // Instantiate a new Workbook object
                const workbook = new Workbook();

                // Obtaining the reference of the newly added worksheet
                const sheetIndex = workbook.worksheets.add();
                const sheet = workbook.worksheets.get(sheetIndex);
                const cells = sheet.cells;

                // Setting the value to the cells
                let cell = cells.get("A1");
                cell.value = "Sport";
                cell = cells.get("B1");
                cell.value = "Quarter";
                cell = cells.get("C1");
                cell.value = "Sales";

                cell = cells.get("A2");
                cell.value = "Golf";
                cell = cells.get("A3");
                cell.value = "Golf";
                cell = cells.get("A4");
                cell.value = "Tennis";
                cell = cells.get("A5");
                cell.value = "Tennis";
                cell = cells.get("A6");
                cell.value = "Tennis";
                cell = cells.get("A7");
                cell.value = "Tennis";
                cell = cells.get("A8");
                cell.value = "Golf";

                cell = cells.get("B2");
                cell.value = "Qtr3";
                cell = cells.get("B3");
                cell.value = "Qtr4";
                cell = cells.get("B4");
                cell.value = "Qtr3";
                cell = cells.get("B5");
                cell.value = "Qtr4";
                cell = cells.get("B6");
                cell.value = "Qtr3";
                cell = cells.get("B7");
                cell.value = "Qtr4";
                cell = cells.get("B8");
                cell.value = "Qtr3";

                cell = cells.get("C2");
                cell.value = 1500;
                cell = cells.get("C3");
                cell.value = 2000;
                cell = cells.get("C4");
                cell.value = 600;
                cell = cells.get("C5");
                cell.value = 1500;
                cell = cells.get("C6");
                cell.value = 4070;
                cell = cells.get("C7");
                cell.value = 5000;
                cell = cells.get("C8");
                cell.value = 6430;

                const pivotTables = sheet.pivotTables;

                // Adding a PivotTable to the worksheet
                const index = pivotTables.add("=A1:C8", "E3", "PivotTable2");

                // Accessing the instance of the newly added PivotTable
                const pivotTable = pivotTables.get(index);

                // Unshowing grand totals for rows.
                pivotTable.rowGrand = false;

                // Dragging the first field to the row area.
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, 0);

                // Dragging the second field to the column area.
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, 1);

                // Dragging the third field to the data area.
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, 2);

                // Saving the Excel file
                const outputData = workbook.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById('downloadLink');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = 'CreatePivotTable_out.xlsx';
                downloadLink.style.display = 'block';
                downloadLink.textContent = 'Download Excel File';

                document.getElementById('result').innerHTML = '<p style="color: green;">Pivot table created successfully! Click the download link to get the file.</p>';
            });
        });
    </script>
</html>
```

{{% alert color="primary" %}}

データソースとしてセル範囲を割り当てるときには、範囲は左上から右下に向かっている必要があります。例えば、「A1:C3」は有効ですが、「C3:A1」は無効です。

{{% /alert %}}
