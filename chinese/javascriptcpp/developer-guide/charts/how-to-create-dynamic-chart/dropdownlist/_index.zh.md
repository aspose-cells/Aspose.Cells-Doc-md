---
title: 如何使用C++通过JavaScript创建带有下拉列表的动态图表
linktitle: 如何创建具有下拉列表的动态图表
description: 了解如何使用Aspose.Cells for JavaScript通过C++创建根据下拉列表选择更新的动态图表。我们的逐步指南将演示如何将下拉列表集成到图表中以实现灵活的数据可视化。
keywords: Aspose.Cells for JavaScript通过C++、动态图表、下拉列表、数据可视化、集成、灵活展示。
type: docs
weight: 76
url: /zh/javascript-cpp/create-dynamic-chart-with-dropdownlist/
---

## **可能的使用场景**
在Excel中，具有下拉列表的动态图表是一种强大的工具，可以根据所选数据动态更新创建交互式图表。这个功能在需要分析多个数据集或比较不同情况的情况下特别有用。

具有下拉列表的动态图表的一个常见应用是在财务分析中。例如，公司可能对不同年份或部门的多个财务数据集。通过使用下拉列表，用户可以选择他们想要分析的特定数据集，图表会自动更新以显示相应的信息。这有助于轻松比较和识别趋势或模式。

另一个应用是在销售和营销中。公司可能有不同产品或地区的销售数据。使用具有下拉列表的动态图表，用户可以从下拉列表中选择特定产品或区域，图表会动态更新以显示所选选项的销售业绩。这有助于识别高效领域或产品，并做出数据驱动的决策。

总之，Excel中具有下拉列表的动态图表提供了一种灵活而互动的方式来可视化和分析数据。这在需要比较多个数据集或探索不同情况的情况下非常有价值，使其成为财务分析、销售和营销以及许多其他应用的多功能工具。

## **使用Aspose Cells创建具有下拉列表的动态图表**
接下来的段落中，我们将向您展示如何使用Aspose.Cells for JavaScript通过C++创建带有下拉列表的动态图表。我们会展示示例代码以及用此代码生成的Excel文件。

## **示例代码**
以下示例代码将生成[具有下拉列表的动态图表文件](DynamicChartWithDropdownlist.xlsx)。

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

## **备注**
在生成的文件中，图表会根据所选月份动态计算数据。这是通过示例代码中的“OFFSET”公式完成的：
