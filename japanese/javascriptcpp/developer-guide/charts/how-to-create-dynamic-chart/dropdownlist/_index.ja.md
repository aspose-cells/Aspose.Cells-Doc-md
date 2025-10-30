---
title: ドロップダウンリストを使った動的チャートの作成方法（JavaScript経由、C++）
linktitle: ドロップダウンリストを使用した動的チャートの作成方法
description: Aspose.Cells for JavaScriptを使ったドロップダウンリストによる動的チャートの作成方法を学びます。柔軟なデータ視覚化のためにチャートにドロップダウンリストを組み込むステップバイステップのガイドです。
keywords: Aspose.Cells for JavaScriptを使ったC++の動的チャート、ドロップダウンリスト、データ可視化、統合、柔軟な視覚化。
type: docs
weight: 76
url: /ja/javascript-cpp/create-dynamic-chart-with-dropdownlist/
---

## **可能な使用シナリオ**
Excelでのドロップダウンリストを使用した動的チャートは、選択したデータに基づいてダイナミックに更新されるインタラクティブなチャートをユーザーが作成できる強力なツールです。この機能は、複数のデータセットを分析したり、さまざまなシナリオを比較したりする必要がある状況で特に有用です。

ドロップダウンリストを使用した動的チャートの一般的な応用例は、財務分析です。たとえば、企業には異なる年や部門の複数の財務データがあるかもしれません。ドロップダウンリストを使用することで、ユーザーは分析したい特定のデータセットを選択し、チャートは自動的に対応する情報を表示します。これにより、簡単に比較し、トレンドやパターンを特定できます。

もう1つの応用例は、営業とマーケティングです。企業には異なる製品や地域の販売データがあるかもしれません。ドロップダウンリストを使用した動的チャートでは、ユーザーはドロップダウンリストから特定の製品や地域を選択し、チャートは選択したオプションの販売実績を動的に表示します。これにより、トップのパフォーマンスエリアや製品を特定し、データに基づいた意思決定が行えます。

要するに、Excelでのドロップダウンリストを使用した動的チャートは、データを柔軟にインタラクティブに可視化および分析する手段を提供します。複数のデータセットを比較したり、さまざまなシナリオを探ったりする必要がある状況で価値があり、財務分析、営業とマーケティングなど様々な応用に使える多目的なツールです。

## **Aspose Cellsを使用して動的チャートをドロップダウンリストで作成する**
次の段落では、Aspose.Cells for JavaScriptを使ったC++によるドロップダウンリスト付き動的チャートの作成方法と、その例のコードやこのコードを用いて作成されたExcelファイルについて説明します。

## **サンプルコード**
次のサンプルコードでは、[ドロップダウンリストファイル](DynamicChartWithDropdownlist.xlsx)を生成します。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Dynamic Chart with Dropdown List Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, CellArea, ValidationType, BackgroundType, Color, ChartType } = AsposeCells;

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
            // Create a new workbook and access the first worksheet.
            const workbook = new Workbook();
            const sheets = workbook.worksheets;
            const sheet = sheets.get(0);

            // Populate the data for the chart. Add values to cells and set series names.
            sheet.cells.get("A3").putValue("Tea");
            sheet.cells.get("A4").putValue("Coffee");
            sheet.cells.get("A5").putValue("Sugar");

            // In this example, we will add 12 months of data
            sheet.cells.get("B2").putValue("Jan");
            sheet.cells.get("C2").putValue("Feb");
            sheet.cells.get("D2").putValue("Mar");
            sheet.cells.get("E2").putValue("Apr");
            sheet.cells.get("F2").putValue("May");
            sheet.cells.get("G2").putValue("Jun");
            sheet.cells.get("H2").putValue("Jul");
            sheet.cells.get("I2").putValue("Aug");
            sheet.cells.get("J2").putValue("Sep");
            sheet.cells.get("K2").putValue("Oct");
            sheet.cells.get("L2").putValue("Nov");
            sheet.cells.get("M2").putValue("Dec");
            const allMonths = 12;
            const iCount = 3;
            for (let i = 0; i < iCount; i++) {
                for (let j = 0; j < allMonths; j++) {
                    const _row = i + 2;
                    const _column = j + 1; 
                    sheet.cells.get(_row, _column).putValue(50 * (i % 2) + 20 * (j % 3) + 10 * (i / 3) + 10);
                }
            }

            // This is the Dropdownlist for Dynamic Data
            const ca = CellArea.createCellArea(9, 0, 9, 0);
            const _index = sheet.validations.add(ca);
            const _va = sheet.validations.get(_index);
            _va.type = ValidationType.List;
            _va.inCellDropDown = true;
            _va.formula1 = "=$B$2:$M$2";
            sheet.cells.get("A9").putValue("Current Month");
            sheet.cells.get("A10").putValue("Jan");
            const _style = sheet.cells.get("A10").style;
            _style.font.isBold = true;
            _style.pattern = BackgroundType.Solid;
            _style.foregroundColor = Color.Yellow;
            sheet.cells.get("A10").style = _style;

            // Set the dynamic range for the chart's data source. 
            let index = sheets.names.add("Sheet1!ChtMonthData");
            sheets.names.get(index).refersTo = "=OFFSET(Sheet1!$A$3,0,MATCH($A$10, $B$2:$M$2, 0),3,1)";

            // Set the dynamic range for the chart's data labels. 
            index = sheets.names.add("Sheet1!ChtXLabels");
            sheets.names.get(index).refersTo = "=Sheet1!$A$3:$A$5";

            // Create a chart object and set its data source.
            const chartIndex = sheet.charts.add(ChartType.Column, 8, 2, 20, 8);
            const chart = sheet.charts.get(chartIndex);
            chart.nSeries.add("month", true);
            chart.nSeries.get(0).name = "=Sheet1!$A$10";
            chart.nSeries.get(0).values = "Sheet1!ChtMonthData";
            chart.nSeries.get(0).xValues = "Sheet1!ChtXLabels";

            // Save the workbook as an Excel file.
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'DynamicChartWithDropdownlist.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created successfully. Click the download link to save the file.</p>';
        });
    </script>
</html>
```

## **メモ**
生成されたファイルでは、チャートは選択した月のデータを動的にカウントします。これはサンプルコードでの「OFFSET」式の使用によって行われます。
