---
title: 通过 C++ 阅读和操作 Excel 2016 图表
linktitle: 读取和操作Excel 2016图表
description: 学习如何通过 Aspose.Cells for JavaScript 通过 C++ 阅读和操作 Excel 2016 图表。此指南将展示如何访问和修改各种图表属性。
keywords: Aspose.Cells for JavaScript 通过 C++，Excel 2016 图表，读取，操作，数据标签，系列颜色，布局，分层图表，环状图。
type: docs
weight: 48
url: /zh/javascript-cpp/read-and-manipulate-excel-2016-charts/
---

## **可能的使用场景**  
Aspose.Cells 现在支持读取和操作 Microsoft Excel 2016 图表，而这些图表在 Microsoft Excel 2013 或早期版本中是不存在的。  
## **读取和操作Excel 2016图表**  
以下示例代码加载包含Excel 2016图表的[源Excel文件](22774101.xlsx)，该文件在第一个工作表中。它逐个读取所有图表并根据其图表类型更改标题。以下截图显示代码执行前的源Excel文件。如您所见，所有图表的标题都是相同的。

![todo:image_alt_text](read-and-manipulate-excel-2016-charts_1.png)

下面的屏幕截图显示了代码执行后的 [输出 Excel 文件](22774104.xlsx)。正如您所见，图表标题已根据其图表类型进行了更改。

![todo:image_alt_text](read-and-manipulate-excel-2016-charts_2.png)  
## **示例代码**  
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Read and Update Chart Titles</h1>
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
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            // Read selected file
            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet which contains the charts
            const sheet = workbook.worksheets.get(0);

            // Access all charts one by one and read their types
            const chartsCount = sheet.charts.count;
            let logHtml = '<ul>';
            for (let i = 0; i < chartsCount; i++) {
                // Access the chart
                const ch = sheet.charts.get(i);

                // Read chart type
                const typeStr = ch.type.toString();
                console.log(typeStr);

                // Change the title of the chart
                ch.title.text = "Chart Type is " + typeStr;

                logHtml += `<li>Chart ${i}: ${typeStr}</li>`;
            }
            logHtml += '</ul>';

            // Save the workbook to a downloadable file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out_excel2016Charts.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Charts updated successfully! Click the download link to get the modified file.</p>' + logHtml;
        });
    </script>
</html>
```  
## **控制台输出**  


{{< highlight javascript >}}  

 Waterfall  

Treemap  

Sunburst  

Histogram  

BoxWhisker  

{{< /highlight >}}  

## **高级主题**  
- [创建瀑布图](/cells/zh/javascript-cpp/creating-waterfall-chart/)  
- [创建树状图表](/cells/zh/javascript-cpp/creating-treemap-chart/)  
- [创建旭日图](/cells/zh/javascript-cpp/creating-sunburst-chart/)
