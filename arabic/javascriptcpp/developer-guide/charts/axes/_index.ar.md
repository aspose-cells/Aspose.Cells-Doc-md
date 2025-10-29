---
title: إدارة محاور مخططات إكسل باستخدام جافا سكريبت عبر C++
description: تعلم كيفية تكوين محاور المخططات في Aspose.Cells for JavaScript عبر C++. سيرشدك دليلنا حول كيفية ضبط المحاور الأساسية والثانوية، ضبط نطاقاتها، وتعديل خصائصها لتحسين مخططاتك.
keywords: Aspose.Cells for Javaسكريبت عبر C++، محاور المخططات، التكوين، المحاور الأساسية، المحاور الثانوية، النطاق، الخصائص.
linktitle: المحاور
type: docs
weight: 50
url: /ar/javascript-cpp/chart-axes/
---

{{% alert color="primary" %}}  

في رسوم بيانية Excel، هناك 3 أنواع من المحاور:  
1. المحور الأفقي (الفئة): محور X  
1. المحور الرأسي (القيمة): محور Y  
1. المحور العمق (السلسلة): محور Z  

{{% /alert %}}  

## **خيارات المحور**  
 Aspose.Cells for Javaسكريبت عبر C++ يسمح لك أيضًا بإدارة محاور المخططات أثناء التشغيل. مع كائن [المحور](https://reference.aspose.com/cells/javascript-cpp/axis/)، يمكنك تغيير جميع خيارات المحور كما هو موضح في Excel.  

|![todo:image_alt_text](chart_axes.png)|  

## **إدارة محاور X و Y**  
في مخطط Excel، المحور الأفقي والمحور العمودي هما الأكثر شعبية للاستخدام.  

يوضح مقتطف الشفرة التالي كيفية تعيين خيارات محاور X و Y.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Chart Axes</title>
    </head>
    <body>
        <h1>Chart Axes Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ChartType } = AsposeCells;

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

            // Instantiate a new Workbook
            const workbook = new Workbook();

            // Adding a new worksheet to the Workbook object
            const sheetIndex = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(sheetIndex);

            // Adding sample values to cells
            worksheet.cells.get("A1").value = "Series1";
            worksheet.cells.get("A2").value = 50;
            worksheet.cells.get("A3").value = 100;
            worksheet.cells.get("A4").value = 150;
            worksheet.cells.get("B1").value = "Series2";
            worksheet.cells.get("B2").value = 60;
            worksheet.cells.get("B3").value = 32;
            worksheet.cells.get("B4").value = 50;

            // Adding a chart to the worksheet
            const chartIndex = worksheet.charts.add(ChartType.Column, 5, 0, 15, 5);

            // Accessing the instance of the newly added chart
            const chart = worksheet.charts.get(chartIndex);

            // Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B4"
            chart.chartDataRange = ["A1:B4", true];

            // Hiding X axis
            chart.categoryAxis.isVisible = false;

            // Setting max value of Y axis
            chart.valueAxis.maxValue = 200;
            // Setting major unit
            chart.valueAxis.majorUnit = 50;

            // Save the file and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'chart_axes.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created successfully. Click the download link to download the file.</p>';
        });
    </script>
</html>
```  

## **مواضيع متقدمة**  
- [تغيير اتجاه التسمية التلقائية](/cells/ar/javascript-cpp/change-tick-label-direction/)  
- [تحديد أي محور موجود في الرسم البياني](/cells/ar/javascript-cpp/determine-which-axis-exists-in-the-chart/)  
- [التعامل مع الوحدات التلقائية لمحور الرسم البياني مثل Microsoft Excel](/cells/ar/javascript-cpp/handle-automatic-units-of-chart-axis-like-microsoft-excel/)  
- [قراءة تسميات المحور بعد حساب الرسم البياني](/cells/ar/javascript-cpp/read-axis-labels-after-calculating-the-chart/)  
- [كيفية تعيين محور الفئة في رسم بياني Excel](/cells/ar/javascript-cpp/how-to-set-category-axis/)
