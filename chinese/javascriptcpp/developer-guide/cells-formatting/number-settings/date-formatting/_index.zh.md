---
title: 如何将数字格式化为日期
type: docs
weight: 10
url: /zh/javascript-cpp/format-number-to-date/
description: 本文将介绍如何使用Aspose.Cells for JavaScript通过C++ API将数字格式化为日期。
keywords: 格式化数字为日期，单元格数字设置，格式化数字为日期，日期设置，日期格式。
---

## **可能的使用场景**
在Excel（或任何电子表格软件）中将数字格式化为日期很重要，原因有多方面，特别是当你处理包含时间或日程信息的数据时。以下是格式化数字为日期的好处：

1. 正确解释日期值：在Excel中，日期以序列号存储（例如，1代表1900年1月1日，44210代表2021年9月6日）。如果这些数字不被格式化为日期，用户可能会看到没有意义的数字而非可识别的日期。正确格式化后，Excel会将它们显示为实际日期（例如，09/06/2021而不是44210）。
1. 简化与时间相关的计算：Excel可以利用日期进行许多计算，如计算两日期之间的天数、加减天数或确定星期几。如果数字未被格式化为日期，Excel将无法有效执行这些操作。例如，若你想知道2023年9月1日到2023年10月1日之间的天数，如果数字是日期格式，Excel能轻松计算。
1. 保持一致性：当所有与日期相关的值都被正确格式化时，确保所有日期都以统一、易读的风格出现。这在商务报告、项目时间表和数据库中尤为重要，因为日期的一致性很关键。
不同地区使用不同的日期格式（例如，美国的MM/DD/YYYY与许多其他国家的DD/MM/YYYY），因此格式化有助于确保日期被正确解释。
1. 提升可读性：采用标准格式（例如，01/01/2024）显示的日期比原始序列号（如45000）更容易阅读。正确的日期格式能让你的电子表格更友好，减少混淆。特别是在日程安排、时间线、事件策划或历史数据中尤为重要。
1. 便于排序和筛选：当日期被正确格式化后，Excel会识别它们为实际日期，从而方便按时间排序或筛选数据。例如，你可以按日期排序事件列表或筛选出特定两个日期之间的记录。未正确格式化的数字可能导致排序基于原始数字而非实际日期。
1. 支持日期函数的使用：Excel提供了强大的日期函数，如：TODAY()、DATEDIF()、WORKDAY()、YEAR()、MONTH()、DAY()。这些函数需要正确格式化的日期以确保计算的准确性。
1. 支持可视化（图表/时间线）：正确格式化的日期可以用于创建以时间为关键轴的图表和图形。例如，在时间线图中，Excel需要以被识别的格式输入日期，以准确绘制事件。格式不正确或未格式化的数字可能导致图表不合理或信息不准确。
1. 避免误解：原始数字容易被误解。例如，44210可以被理解为普通数字，但格式化为日期后，明确表示是2021年9月6日。正确格式化的日期可以避免数据被误解。
1. 促进数据输入：当单元格被格式化为日期后，用户在输入时会看到日期的提示，从而避免输入错误，并确保日期值的正确录入。
1. 对于调度和跟踪非常关键：在任何涉及调度、跟踪或截止日期（如项目管理、财务预测或时间敏感报告）的场景中，将数字格式化为日期都非常重要，以确保准确性和易理解性。这有助于更好的规划和执行。


## **如何在Excel中将数字格式化为日期**
按照以下步骤在Excel中将数字格式化为日期：

### **使用功能区（开始选项卡）**
1. 选择包含要格式化为日期的数字的单元格。
1. 转到功能区中的“开始”选项卡。
1. 在“数字”组中，点击“数字格式”框中的下拉箭头（默认可能显示“常规”或“数字”）。
1. 从下拉菜单中选择“短日期”或“长日期”。短日期：以简洁格式显示日期，例如MM/DD/YYYY（美国格式）或DD/MM/YYYY（国际格式）。长日期：以更详细格式显示日期，例如星期一，2024年1月1日。
<br>
<img src="1.png" width=60% />

### **使用“设置单元格格式”对话框**
1. 选择你想要格式化的单元格。
1. 右键点击已选单元格，选择“设置单元格格式”，或按Ctrl + 1（Windows）或Cmd + 1（Mac）。
1. 在“设置单元格格式”对话框中，切换到“数字”选项卡。
1. 在左侧列表中选择“日期”。
1. 从右侧列表中选择所需的日期格式（如MM/DD/YYYY、DD/MM/YYYY或自定义格式）。
<br>
<img src="2.png" width=60% />
点击确定以应用日期格式。

## **如何在Aspose.Cells中将数字格式化为日期**

 要在Aspose.Cells for JavaScript通过C++库中以日期格式格式化数字，可以以编程方式应用日期格式到单元格。以下是使用Aspose.Cells for JavaScript通过C++的方法：

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Date & Custom Format Example</h1>
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
            // Create a new workbook
            const workbook = new Workbook();

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access the cell you want to format
            const a1 = worksheet.cells.get("A1");

            // Set a numeric value that represents a date (e.g., 44210 represents 09/06/2021 in Excel)
            a1.value = 44210;

            // Create a style object to apply the date format
            const a1Style = a1.style;

            // "14" represents a standard date format in Excel (MM/DD/YYYY)
            a1Style.number = 14;

            // Apply the style to the cell
            a1.style = a1Style;

            // Access the cell where you want to apply the currency format
            const a2 = worksheet.cells.get("A2");

            // Set a numeric value to the cell
            a2.value = 44210;

            // Create a style object to apply the date format
            const a2Style = a2.style;
            // Custom format for YYYY-MM-DD
            a2Style.custom = "YYYY-MM-DD";

            // Apply the style to the cell
            a2.style = a2Style;

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'DateFormatted.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and formatted successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
