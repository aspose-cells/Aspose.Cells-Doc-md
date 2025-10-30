---
title: JavaScriptを使用したピボットテーブル用のグローバリゼーション設定のカスタマイズ（C++経由）
linktitle: ピボットテーブルのグローバリゼーション設定のカスタマイズ
type: docs
weight: 50
url: /ja/javascript-cpp/customize-globalization-settings-for-pivot-table/
---

## **可能な使用シナリオ**

時には、*ピボット合計、サブ合計、総計、すべてのアイテム、複数アイテム、列ラベル、行ラベル、空白値*のテキストを必要に応じてカスタマイズしたい場合があります。Aspose.Cells for JavaScriptをC++を使用して、ピボットテーブルのグローバリゼーション設定を変更でき、これらのシナリオに対応できます。また、この機能を利用してラベルをアラビア語、ヒンディー語、ポーランド語など他の言語に変更することも可能です。

## **ピボットテーブルのグローバリゼーション設定のカスタマイズ**

以下のサンプルコードは、ピボットテーブルのグローバリゼーション設定をカスタマイズする方法を説明しています。これにより、基本クラス [**PivotGlobalizationSettings**](https://reference.aspose.com/cells/javascript-cpp/pivotglobalizationsettings/) から派生したクラス *CustomPivotTableGlobalizationSettings* を作成し、必要なすべてのメソッドをオーバーライドします。これらのメソッドは、*Pivot Total、Sub Total、Grand Total、All Items、Multiple Items、Column Labels、Row Labels、Blank Values* のカスタマイズされたテキストを返します。次に、そのクラスのオブジェクトを [**WorkbookSettings.pivotSettings**](https://reference.aspose.com/cells/javascript-cpp/globalizationsettings/#pivotSettings--) プロパティに割り当てます。コードは、ピボットテーブルを含む[ソースExcelファイル](40468488.xlsx)をロードし、データを更新・計算し、[出力PDF](40468487.pdf)ファイルとして保存します。次のスクリーンショットは、このサンプルコードの効果を示したもので、出力されたPDF内のピボットテーブルの異なる部分に、[**PivotGlobalizationSettings**](https://reference.aspose.com/cells/javascript-cpp/pivotglobalizationsettings/)クラスのオーバーライドされたメソッドによるカスタマイズされたテキストが表示されています。

![todo:image_alt_text](customize-globalization-settings-for-pivot-table_1.png)

## **サンプルコード**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Pivot Table Globalization Settings Example</title>
    </head>
    <body>
        <h1>Pivot Table Globalization Settings Example</h1>
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

        class CustomPivotTableGlobalizationSettings extends AsposeCells.PivotGlobalizationSettings {
            // Gets the name of "Total" label in the PivotTable.
            getTextOfTotal() {
                console.log("---------GetPivotTotalName-------------");
                return "AsposeGetPivotTotalName";
            }

            // Gets the name of "Grand Total" label in the PivotTable.
            getTextOfGrandTotal() {
                console.log("---------GetPivotGrandTotalName-------------");
                return "AsposeGetPivotGrandTotalName";
            }

            // Gets the name of "(Multiple Items)" label in the PivotTable.
            getTextOfMultipleItems() {
                console.log("---------GetMultipleItemsName-------------");
                return "AsposeGetMultipleItemsName";
            }

            // Gets the name of "(All)" label in the PivotTable.
            getTextOfAll() {
                console.log("---------GetAllName-------------");
                return "AsposeGetAllName";
            }

            // Gets the name of "Column Labels" label in the PivotTable.
            getTextOfColumnLabels() {
                console.log("---------GetColumnLabelsOfPivotTable-------------");
                return "AsposeGetColumnLabelsOfPivotTable";
            }

            // Gets the name of "Row Labels" label in the PivotTable.
            getTextOfRowLabels() {
                console.log("---------GetRowLabelsNameOfPivotTable-------------");
                return "AsposeGetRowLabelsNameOfPivotTable";
            }

            // Gets the name of "(blank)" label in the PivotTable.
            getTextOfEmptyData() {
                console.log("---------GetEmptyDataName-------------");
                return "(blank)AsposeGetEmptyDataName";
            }

            // Gets the name of PivotFieldSubtotalType type in the PivotTable.
            getTextOfSubTotal(subTotalType) {
                console.log("---------GetSubTotalName-------------");

                switch (subTotalType) {
                    case AsposeCells.PivotFieldSubtotalType.Sum:
                        return "AsposeSum";

                    case AsposeCells.PivotFieldSubtotalType.Count:
                        return "AsposeCount";

                    case AsposeCells.PivotFieldSubtotalType.Average:
                        return "AsposeAverage";

                    case AsposeCells.PivotFieldSubtotalType.Max:
                        return "AsposeMax";

                    case AsposeCells.PivotFieldSubtotalType.Min:
                        return "AsposeMin";

                    case AsposeCells.PivotFieldSubtotalType.Product:
                        return "AsposeProduct";

                    case AsposeCells.PivotFieldSubtotalType.CountNums:
                        return "AsposeCount";

                    case AsposeCells.PivotFieldSubtotalType.Stdev:
                        return "AsposeStdDev";

                    case AsposeCells.PivotFieldSubtotalType.Stdevp:
                        return "AsposeStdDevp";

                    case AsposeCells.PivotFieldSubtotalType.Var:
                        return "AsposeVar";

                    case AsposeCells.PivotFieldSubtotalType.Varp:
                        return "AsposeVarp";
                }

                return "AsposeSubTotalName";
            }
        }

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const resultDiv = document.getElementById('result');
            const downloadLink = document.getElementById('downloadLink');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by opening the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Apply globalization settings and custom pivot table globalization settings
            workbook.settings.globalizationSettings = new AsposeCells.GlobalizationSettings();
            workbook.settings.globalizationSettings.pivotSettings = new CustomPivotTableGlobalizationSettings();

            // Hide first worksheet that contains the data of the pivot table
            workbook.worksheets.get(0).isVisible = false;

            // Access second worksheet
            const ws = workbook.worksheets.get(1);

            // Access the pivot table, refresh and calculate its data
            const pt = ws.pivotTables.get(0);
            pt.refreshDataFlag = true;
            pt.refreshData();
            pt.calculateData();
            pt.refreshDataFlag = false;

            // Pdf save options - save entire worksheet on a single pdf page
            const options = new AsposeCells.PdfSaveOptions();
            options.onePagePerSheet = true;

            // Save the output pdf 
            const outputData = workbook.save(SaveFormat.Pdf, options);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputPivotTableGlobalizationSettings.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            resultDiv.innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the PDF file.</p>';
        });
    </script>
</html>
```
