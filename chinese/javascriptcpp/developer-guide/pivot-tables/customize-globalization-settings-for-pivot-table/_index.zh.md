---
title: 使用JavaScript通过C++自定义数据透视表的全球化设置
linktitle: 自定义数据透视表的全球化设置
type: docs
weight: 50
url: /zh/javascript-cpp/customize-globalization-settings-for-pivot-table/
---

## **可能的使用场景**

有时您可能想根据需求自定义*数据透视总计、小计、总计、所有项目、多项、列标签、行标签、空值*文本。Aspose.Cells for JavaScript通过C++允许您自定义数据透视表的全球化设置来应对这些场景。您还可以使用此功能将标签更改为阿拉伯语、印地语、波兰语等其他语言。

## **自定义数据透视表的全球化设置**

以下示例代码说明了如何为数据透视表自定义全球化设置。它创建了一个继承自 [**PivotGlobalizationSettings**](https://reference.aspose.com/cells/javascript-cpp/pivotglobalizationsettings/) 基类的 *CustomPivotTableGlobalizationSettings* 类，并重写了所有必要的方法。这些方法返回自定义的 *Pivot Total、Sub Total、Grand Total、All Items、Multiple Items、Column Labels、Row Labels、Blank Values* 的文本。然后将该类的对象分配给 [**WorkbookSettings.pivotSettings**](https://reference.aspose.com/cells/javascript-cpp/globalizationsettings/#pivotSettings--) 属性。该代码加载包含数据透视表的源Excel文件（40468488.xlsx），刷新并计算其数据，然后保存为输出PDF（40468487.pdf）。以下截图显示了示例代码对输出PDF的效果。可以看到，数据透视表的不同部分现在返回了由 [**PivotGlobalizationSettings**](https://reference.aspose.com/cells/javascript-cpp/pivotglobalizationsettings/) 类的重写方法所定制的文本。

![todo:image_alt_text](customize-globalization-settings-for-pivot-table_1.png)

## **示例代码**

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
