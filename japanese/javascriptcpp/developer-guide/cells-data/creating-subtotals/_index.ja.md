---
title: 集計の作成
type: docs
weight: 800
url: /ja/javascript-cpp/creating-subtotals/
description: スプレッドシート内の繰り返し値に対して小計を作成する方法を、Aspose.Cells for JavaScript via C++ APIを使用して学びます。
keywords: サブトータルの追加、サブトータルの設定、サブトータルの追加、サブトータルの作成、ワークシートにサブトータルを追加する方法 
---

{{% alert color="primary" %}}

スプレッドシート内の繰り返し値に対して自動的に小計を作成できます。Aspose.Cells for JavaScript via C++は、プログラムで小計を追加するためのAPI機能を提供します。

{{% /alert %}}

## **Microsoft Excel の使用**

Microsoft Excel でサブトータルを追加する方法:

1. ブック1.xlsとして保存、ブックの最初のワークシートに簡単なデータリストを作成します（以下の図を参照）。
1. リスト内の任意のセルを選択します。
1. **データ** メニューから、**サブトータル** を選択します。サブトータルのダイアログが表示されます。使用する関数とサブトータルを配置する場所を定義します。

## **Aspose.Cells for JavaScript via C++ APIを使用して**

Aspose.Cells for JavaScript via C++は、Microsoft Excelファイルを表す[**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)クラスを提供します。[**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)クラスには、Excelファイル内の各ワークシートにアクセスできる[**worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--)コレクションが含まれています。

ワークシートは[**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)クラスによって表されます。このクラスは、ワークシートやその他のオブジェクトを管理するためのさまざまなプロパティとメソッドを提供します。各ワークシートは[**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells)コレクションから構成されています。ワークシートに小計を追加するには、[**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells)クラスの[**subtotal**](https://reference.aspose.com/cells/javascript-cpp/cells/#subtotal-cellarea-number-consolidationfunction-numberarray-)メソッドを使用します。小計の計算と配置方法を指定するためにパラメータ値を提供します。

以下の例では、[テンプレートファイル](book1.xlsx)の最初のワークシートにAspose.Cells for JavaScript via C++ APIを使用して小計を追加しました。コードを実行すると、小計付きのワークシートが作成されます。

以下のコードスニペットは、Aspose.Cells for JavaScript via C++を使用してワークシートに小計を追加する方法を示しています。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Apply Subtotal Example</h1>
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
        });

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the Cells collection in the first worksheet
            const worksheet = workbook.worksheets.get(0);
            const cells = worksheet.cells;

            // Create a cellarea i.e., B3:C19
            const ca = new AsposeCells.CellArea();
            ca.startRow = 2;
            ca.startColumn = 1;
            ca.endRow = 18;
            ca.endColumn = 2;

            // Apply subtotal, the consolidation function is Sum and it will be applied to
            // Second column (C) in the list
            cells.subtotal(ca, 0, AsposeCells.ConsolidationFunction.Sum, [1]);

            // Save the excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Subtotal applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
