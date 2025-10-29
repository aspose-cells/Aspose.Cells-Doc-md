---
title: 使用 C++ 通过 JavaScript 将 Excel 图表转换为图像
linktitle: 将Excel图表转换成图像
type: docs
weight: 20
url: /zh/javascript-cpp/convert-an-excel-chart-to-image/
description: 学习如何使用 Aspose.Cells for JavaScript 通过 C++ 将 Excel 图表转换为图像。
---

{{% alert color="primary" %}}  

图表在视觉上很吸引人，可以帮助用户轻松地观察数据的比较、模式和趋势。例如，与分析工作表数字列相比，图表能够一眼看出销售额是下降还是上升，以及实际销售额与预期销售额的比较如何。人们经常需要以易于理解和维护的方式呈现统计和图形信息。图片有助于解释。  

有时，应用程序或网页中需要图表。或者可能需要在 Word 文档、PDF 文件、PowerPoint 演示文稿或其他应用程序中使用。在每种情况下，你都希望将图表呈现为图像，以便在其他地方使用。  

{{% /alert %}}  

## **将图表转换为图像**  

在此示例中，饼图和柱状图被转换为图像。  

### **将饼图转换为图像文件**  

首先，在 Microsoft Excel 中创建一个饼图，然后使用 Aspose.Cells for JavaScript 通过 C++ 将其转换为图像文件。本示例中的代码基于模板 Microsoft Excel 文件中的饼图创建了一个 EMF 图像。  

|**输出：饼图图像**|  
| :- |  
|![todo:image_alt_text](convert-an-excel-chart-to-image_1.png)|  

1. 在Microsoft Excel中创建饼图：  
   1. 在Microsoft Excel中打开一个新的工作簿。  
   1. 在工作表输入一些数据。  
   1. 根据数据创建饼图。  
   1. 保存文件。  

|**输入文件。**|  
| :- |  
|![todo:image_alt_text](convert-an-excel-chart-to-image_2.png)|  

1. 下载并安装 Aspose.Cells：  
   1. [下载 Aspose.Cells for JavaScript 通过 C++](https://downloads.aspose.com/cells/javascript-cpp)。  
   1. 在您的开发计算机上安装它。  

在首次安装时，所有[Aspose](http://www.aspose.com/)组件均以评估模式运行。 评估模式没有时间限制，只会向输出文档中注入水印。  

1. 创建一个项目：  
   1. 启动你偏好的 IDE。  
   1. 创建一个新的控制台应用程序。本示例使用 JavaScript 应用程序，但你也可以使用任何 JavaScript 运行环境创建。  
   1. 添加引用。本项目使用 Aspose.Cells，因此请添加对 Aspose.Cells for JavaScript 通过 C++ 的引用。  
   1. 编写查找并转换图表的代码。 以下是组件用于完成任务的代码。 使用的代码行很少。  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Convert Chart to Image Example</h1>
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
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the designer chart (first chart) in the first worksheet of the workbook.
            const chart = workbook.worksheets.get(0).charts.get(0);

            // Convert the chart to an image (EMF) and prepare download link
            const imageData = chart.toImage(AsposeCells.ImageType.Emf);
            const blob = new Blob([imageData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'PieChart.out.emf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Chart Image';

            document.getElementById('result').innerHTML = '<p style="color: green;">Chart converted to EMF successfully! Click the download link to get the image.</p>';
        });
    </script>
</html>
```  

### **将柱状图转换为图像文件**  

首先，在Microsoft Excel中创建柱状图并转换为图像文件，如上所述。执行示例代码后，将根据模板Excel文件中的柱状图生成一个JPEG文件。  

|**输出文件：柱状图图像。**|  
| :- |  
|![todo:image_alt_text](convert-an-excel-chart-to-image_3.png)|  

1. 在Microsoft Excel中创建柱状图：  
   1. 在Microsoft Excel中打开一个新的工作簿。  
   1. 在工作表输入一些数据。  
   1. 根据数据创建柱状图。  
   1. 保存文件。  

|**输入文件。**|  
| :- |  
|![todo:image_alt_text](convert-an-excel-chart-to-image_4.png)|  

1. 配置项目及引用，如上所述。  
1. 动态将图表转换为图像。 以下是组件用于完成任务的代码。 该代码与先前的代码类似。  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Convert Chart to Image</title>
    </head>
    <body>
        <h1>Convert Chart to Image</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ImageType, Utils } = AsposeCells;

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

            // Instantiate Workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the designer chart (first chart) in the first worksheet of the workbook.
            const chart = workbook.worksheets.get(0).charts.get(0);

            // Convert the chart to an image (JPEG)
            const imageData = await chart.toImage(ImageType.Jpeg);

            // Create a Blob and provide a download link
            const blob = new Blob([imageData], { type: 'image/jpeg' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'ColumnChart.out.jpeg';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Chart Image';

            document.getElementById('result').innerHTML = '<p style="color: green;">Chart converted to image successfully! Click the download link to get the image.</p>';
        });
    </script>
</html>
```
