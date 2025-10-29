---
title: 数字设置
linktitle: 数字设置
description: Aspose.Cells 是一个用于处理电子表格文件的 JavaScript 库，支持多种不同的单元格数字设置。本文介绍如何使用 Aspose.Cells 库管理单元格的数字设置以调整电子表格中的数字格式。
keywords: Aspose.Cells，JavaScript库，电子表格，单元格数字设置，格式化，管理，数字与日期格式
type: docs
weight: 10
url: /zh/javascript-cpp/cells-number-settings/
---

## **如何设置数字和日期的显示格式**  

微软Excel的一个非常强大的功能是允许用户设置数字值和日期的显示格式。我们知道数字数据可以代表不同的值，包括十进制、货币、百分比、小数或会计值等。这些数值的显示格式根据所表示的信息类型而不同。同样，日期或时间也可以以多种格式显示。  
Aspose.Cells支持此功能，并允许开发人员为数字或日期设置任何显示格式。  

### **如何在Microsoft Excel中设置显示格式**  

在Microsoft Excel中设置显示格式：  

1. 右键单击任何单元格。  
2. 选择**单元格格式**。将弹出一个对话框，用于设置任何值的显示格式。  

对话框左侧有许多类别，如**常规**、**数字**、**货币**、**会计**、**日期**、**时间**、**百分比**等。Aspose.Cells支持所有这些显示格式。  

Aspose.Cells提供了一个模块，[**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)，代表一个Excel文件。[**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)模块包含一个[**Worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--)集合，可以访问Excel文件中的每个工作表。工作表由[**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)模块表示。[**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)模块提供一个[**Cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--)集合，每个[**Cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--)集合中的项目代表[**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell)模块的对象。  

Aspose.Cells 提供 [**style**](https://reference.aspose.com/cells/javascript-cpp/cell/#style--) 属性用于 [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell) 模块。该属性用于获取和设置单元格的格式。[**Style**](https://reference.aspose.com/cells/javascript-cpp/style) 模块提供一些有用的属性，用于处理数字和日期的显示格式。  

### **如何使用内置数字格式**  

Aspose.Cells 提供一些内置的数字格式来配置数字和日期的显示格式。这些内置数字格式可以通过使用 [**number**](https://reference.aspose.com/cells/javascript-cpp/style/#number-number-) 属性在 [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) 对象中应用。所有内置数字格式都具有唯一的数值。开发者可以为 [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) 对像的 [**number**](https://reference.aspose.com/cells/javascript-cpp/style/#number-number-) 属性分配任何想要的数字值以应用显示格式。这种方法速度快。Aspose.Cells 支持的内置数字格式如下：  

|**数值**|**类型**|**格式字符串**|  
| :- | :- | :- |  
|0|General|General|  
|1|Decimal|0|  
|2|Decimal|0.00|  
|3|Decimal|#,##0|  
|4|Decimal|#,##0.00|  
|5|Currency|$#,##0;$-#,##0|  
|6|Currency|$#,##0;[Red]$-#,##0|  
|7|Currency|$#,##0.00;$-#,##0.00|  
|8|Currency|$#,##0.00;[Red]$-#,##0.00|  
|9|Percentage|0%|  
|10|Percentage|0.00%|  
|11|Scientific|0.00E+00|  
|12|Fraction|# ?/?|  
|13|Fraction|# */*|  
|14|Date|m/d/yyyy|  
|15|Date|d-mmm-yy|  
|16|Date|d-mmm|  
|17|Date|mmm-yy|  
|18|Time|h:mm AM/PM|  
|19|Time|h:mm:ss AM/PM|  
|20|Time|h:mm|  
|21|Time|h:mm:ss|  
|22|Time|m/d/yy h:mm|  
|37|Currency|#,##0;-#,##0|  
|38|Currency|#,##0;[Red]-#,##0|  
|39|Currency|#,##0.00;-#,##0.00|  
|40|Currency|#,##0.00;[Red]-#,##0.00|  
|41|Accounting|_ * #,##0_ ;_ * "_ ;_ @_|  
|42|Accounting|_ $* #,##0_ ;_ $* "_ ;_ @_|  
|43|Accounting|_ * #,##0.00_ ;_ * "??_ ;_ @_|  
|44|Accounting|_ $* #,##0.00_ ;_ $* "??_ ;_ @_|  
|45|Time|mm:ss|  
|46|Time|h:mm:ss|  
|47|Time|mm:ss.0|  
|48|Scientific|##0.0E+00|  
|49|Text|@|  


```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Create/Modify Workbook</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell } = AsposeCells;

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
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Obtaining the reference of the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Adding the current system date to "A1" cell
            const cellA1 = worksheet.cells.get("A1");
            cellA1.value = new Date();

            // Getting the Style of the A1 Cell
            let style = cellA1.style;

            // Setting the display format to number 15 to show date as "d-mmm-yy"
            style.number = 15;

            // Applying the style to the A1 cell
            cellA1.style = style;

            // Adding a numeric value to "A2" cell
            const cellA2 = worksheet.cells.get("A2");
            cellA2.value = 20;

            // Getting the Style of the A2 Cell
            style = cellA2.style;

            // Setting the display format to number 9 to show value as percentage
            style.number = 9;

            // Applying the style to the A2 cell
            cellA2.style = style;

            // Adding a numeric value to "A3" cell
            const cellA3 = worksheet.cells.get("A3");
            cellA3.value = 2546;

            // Getting the Style of the A3 Cell
            style = cellA3.style;

            // Setting the display format to number 6 to show value as currency
            style.number = 6;

            // Applying the style to the A3 cell
            cellA3.style = style;

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook processed successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```  


### **如何使用自定义数字格式**  

要定义自定义的格式字符串以设置显示格式，请使用 [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) 对象的 [**custom**](https://reference.aspose.com/cells/javascript-cpp/style/#custom-string-) 属性。这种方法不如使用预设格式那样快，但更灵活。  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
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

            // Instantiate or open workbook depending on whether a file is provided
            let workbook;
            if (fileInput.files && fileInput.files.length > 0) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Obtaining the reference of the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Adding the current system date to "A1" cell
            const cellA1 = worksheet.cells.get("A1");
            cellA1.putValue(new Date());

            // Getting the Style of the A1 Cell
            let style = cellA1.style;

            // Setting the display format to number 15 to show date as "d-mmm-yy"
            style.number = 15;

            // Applying the style to the A1 cell
            cellA1.style = style;

            // Adding a numeric value to "A2" cell
            const cellA2 = worksheet.cells.get("A2");
            cellA2.putValue(20);

            // Getting the Style of the A2 Cell
            style = cellA2.style;

            // Setting the display format to number 9 to show value as percentage
            style.number = 9;

            // Applying the style to the A2 cell
            cellA2.style = style;

            // Adding a numeric value to "A3" cell
            const cellA3 = worksheet.cells.get("A3");
            cellA3.putValue(2546);

            // Getting the Style of the A3 Cell
            style = cellA3.style;

            // Setting the display format to number 6 to show value as currency
            style.number = 6;

            // Applying the style to the A3 cell
            cellA3.style = style;

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  


{{% alert color="primary" %}}  

如果你使用 [**custom**](https://reference.aspose.com/cells/javascript-cpp/style/#custom-string-) 属性设置数字格式，任何之前通过 [**number**](https://reference.aspose.com/cells/javascript-cpp/style/#number-number-) 属性设置的格式都将被覆盖，反之亦然。  

{{% /alert %}}  

## **高级主题**  
- [在设置Style.Custom属性时检查自定义数字格式](/cells/zh/javascript-cpp/check-custom-number-format-when-setting-style-custom-property/)  
- [支持的数字格式列表](/cells/zh/javascript-cpp/list-of-supported-number-formats/)  
- [呈现自定义日期格式模式g和ge mm dd](/cells/zh/javascript-cpp/render-custom-date-format-pattern-g-and-ge-mm-dd/)  
- [为工作簿指定自定义数值小数和分组分隔符](/cells/zh/javascript-cpp/specify-custom-number-decimal-and-group-separators-for-workbook/)  
- [指定DBNum自定义模式格式化](/cells/zh/javascript-cpp/specifying-dbnum-custom-pattern-formatting/)
