---
title: JavaScriptをC++経由で、GlobalizationSettingsクラスを使用して角のサブトータルラベルや円グラフのその他のラベルをカスタマイズする方法
linktitle: ピーグラフのカスタムサブトータルラベルおよびその他のラベル用のGlobalizationSettingsクラスの使用
type: docs
weight: 70
url: /ja/javascript-cpp/using-globalizationsettings-class-for-custom-subtotal-labels-and-other-label-of-pie-chart/
description: Aspose.Cells for JavaScriptをC++で使用して、GlobalizationSettingsクラスを使ったサブトータルラベルや円グラフのその他のラベルのカスタマイズ方法を学びます。
---

## **可能な使用シナリオ**

Aspose.CellsのAPIは、スプレッドシート内で小計のカスタムラベルを使用したい場合のシナリオを処理するための[**GlobalizationSettings**](https://reference.aspose.com/cells/javascript-cpp/globalizationsettings)クラスを公開しています。さらに、[**GlobalizationSettings**](https://reference.aspose.com/cells/javascript-cpp/globalizationsettings)クラスは、ワークシートやチャートをレンダリングする際に**Other**ラベルを修正するためにも使用できます。

## **GlobalizationSettingsクラスの紹介**

[**GlobalizationSettings**](https://reference.aspose.com/cells/javascript-cpp/globalizationsettings)クラスは現在、合計のラベルを取得したり、円グラフの「その他」ラベルのカスタムテキストをレンダリングしたりするためにカスタムクラスでオーバーライドできる次の3つのメソッドを提供しています。

1. [**GlobalizationSettings.totalName(ConsolidationFunction)**](https://reference.aspose.com/cells/javascript-cpp/globalizationsettings/#totalName-consolidationfunction-): 関数の合計名を取得します。
1. [**GlobalizationSettings.grandTotalName(ConsolidationFunction)**](https://reference.aspose.com/cells/javascript-cpp/globalizationsettings/#grandTotalName-consolidationfunction-): 関数のグランドトータル名を取得します。


### **サブトータルのカスタムラベル**

[**GlobalizationSettings**](https://reference.aspose.com/cells/javascript-cpp/globalizationsettings)クラスは、今後示す[**GlobalizationSettings.totalName(ConsolidationFunction)**](https://reference.aspose.com/cells/javascript-cpp/globalizationsettings/#totalName-consolidationfunction-)と[**GlobalizationSettings.grandTotalName(ConsolidationFunction)**](https://reference.aspose.com/cells/javascript-cpp/globalizationsettings/#grandTotalName-consolidationfunction-)のメソッドをオーバーライドすることで、サブトータルラベルをカスタマイズするために使用できます。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Custom GlobalizationSettings Example</title>
    </head>
    <body>
        <h1>Custom GlobalizationSettings Example</h1>
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

        // Defines a custom class derived from GlobalizationSettings class
        class CustomSettings extends AsposeCells.GlobalizationSettings {
            // Overrides the totalName method (converted from getTotalName)
            totalName(functionType) {
                switch (functionType) {
                    case AsposeCells.ConsolidationFunction.Average:
                        return "AVG";
                    default:
                        return super.totalName(functionType);
                }
            }

            // Overrides the grandTotalName method (converted from getGrandTotalName)
            grandTotalName(functionType) {
                switch (functionType) {
                    case AsposeCells.ConsolidationFunction.Average:
                        return "GRD AVG";
                    default:
                        return super.grandTotalName(functionType);
                }
            }
        }

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            // Read the selected file and process with Aspose.Cells
            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate a Workbook object from the file bytes
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Create and assign the custom globalization settings to the workbook
            const customSettings = new CustomSettings();
            workbook.globalizationSettings = customSettings;

            // Save the workbook and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Custom globalization settings applied. Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

カスタムラベルを注入するには、サブトータルをワークシートに追加する前に、上記で定義した**CustomSettings**クラスのインスタンスに[**WorkbookSettings.globalizationSettings**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#globalizationSettings--)プロパティを割り当てる必要があります。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Subtotal with Custom Globalization Settings</h1>
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

        // Defines a custom class derived from GlobalizationSettings class
        class CustomSettings extends AsposeCells.GlobalizationSettings {
            // Overrides the TotalName method (converted from getTotalName)
            totalName(functionType) {
                // Checks the function type used to add the subtotals
                switch (functionType) {
                    // Returns custom value based on the function type used to add the subtotals
                    case AsposeCells.ConsolidationFunction.Average:
                        return "AVG";
                    // Handle other cases as per requirement
                    default:
                        return super.totalName(functionType);
                }
            }

            // Overrides the GrandTotalName method (converted from getGrandTotalName)
            grandTotalName(functionType) {
                // Checks the function type used to add the subtotals
                switch (functionType) {
                    // Returns custom value based on the function type used to add the subtotals
                    case AsposeCells.ConsolidationFunction.Average:
                        return "GRD AVG";
                    // Handle other cases as per requirement
                    default:
                        return super.grandTotalName(functionType);
                }
            }
        }

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

            // Assigns the GlobalizationSettings property of the WorkbookSettings class to a custom class created
            workbook.settings.globalizationSettings = new CustomSettings();

            // Accesses the 1st worksheet from the collection which contains data that resides in the cell range A2:B9
            const sheet = workbook.worksheets.get(0);

            // Adds Subtotal of type Average to the worksheet
            sheet.cells.subtotal(AsposeCells.CellArea.createCellArea("A2", "B9"), 0, AsposeCells.ConsolidationFunction.Average, [1]);

            // Calculates Formulas
            workbook.calculateFormula();

            // Auto fits all columns
            sheet.autoFitColumns();

            // Saving the workbook and preparing download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

{{% alert color="primary" %}}

[**GlobalizationSettings**](https://reference.aspose.com/cells/javascript-cpp/globalizationsettings)クラスは、新しいサブトータルを追加するためだけに機能します。既にサブトータルが含まれているスプレッドシートのラベルは変更できません。

{{% /alert %}}
