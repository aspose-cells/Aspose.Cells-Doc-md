---
title: تخصيص المخططات باستخدام جافا سكريبت عبر C++
linktitle: تخصيص المخططات
description: تعلم كيفية تخصيص المخططات في Aspose.Cells for Javaسكريبت عبر C++. دليلنا سيظهر لك كيفية تعديل تصاميم المخططات، إضافة وتنسيق سلاسل البيانات، ضبط المحاور، وتطبيق خيارات تنسيق متنوعة لتعزيز مظهر واستخدام مخططاتك.
keywords: Aspose.Cells for Javaسكريبت عبر C++، رسم بياني، تخصيص، التصاميم، سلاسل البيانات، المحاور، التنسيق، المظهر، الاستخدام.
type: docs
weight: 40
url: /ar/javascript-cpp/customizing-charts/
---

## **إنشاء مخططات مخصصة**  

حتى الآن، عند مناقشة المخططات، نظرنا إلى المخططات القياسية التي تحتوي على إعدادات تنسيقها القياسية. نحن فقط نحدد مصدر البيانات، ونضبط بعض الخصائص، ويتم إنشاء المخطط بالتنسيق الافتراضي الخاص به. لكن APIs الخاصة بـ Aspose.Cells تدعم أيضًا إنشاء مخططات مخصصة تتيح للمطورين إنشاء مخططات مع إعداداتهم الخاصة.  

يمكن للمطورين إنشاء مخططات مخصصة أثناء التشغيل باستخدام Aspose.Cells.  

المخطط يتكون من سلسلة بيانات. كل سلسلة بيانات في Aspose.Cells يتم تمثيلها بواسطة كائن [**Series**](https://reference.aspose.com/cells/javascript-cpp/series)، في حين أن كائن [**SeriesCollection**](https://reference.aspose.com/cells/javascript-cpp/seriescollection) يعمل كمجموعة من كائنات [**Series**](https://reference.aspose.com/cells/javascript-cpp/series). عند إنشاء مخطط مخصص، يتمتع المطورون بحرية استخدام أنواع مختلفة من المخططات لسلاسل البيانات المختلفة (المجمعة في كائن [**SeriesCollection**](https://reference.aspose.com/cells/javascript-cpp/seriescollection)).  

الكود المثال أدناه يوضح كيفية إنشاء مخططات مخصصة. في هذا المثال، سنستخدم مخطط عمودي لأول سلسلة بيانات ومخطط خطي للسلسلة الثانية. النتيجة هي أننا نضيف مخطط عمودي، مع مخطط خطي، إلى ورقة العمل.  

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
        const { Workbook, SaveFormat, ChartType } = AsposeCells;

        const readyPromise = AsposeCells.onReady({
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
            // Ensure Aspose.Cells is initialized
            await readyPromise;

            // Instantiate a new Workbook
            const workbook = new Workbook();

            // Adding a new worksheet to the Workbook object
            const sheetIndex = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(sheetIndex);

            // Adding sample values to cells
            worksheet.cells.get("A1").value = 50;
            worksheet.cells.get("A2").value = 100;
            worksheet.cells.get("A3").value = 150;
            worksheet.cells.get("A4").value = 110;
            worksheet.cells.get("B1").value = 260;
            worksheet.cells.get("B2").value = 12;
            worksheet.cells.get("B3").value = 50;
            worksheet.cells.get("B4").value = 100;

            // Adding a chart to the worksheet
            const chartIndex = worksheet.charts.add(ChartType.Column, 5, 0, 15, 5);

            // Accessing the instance of the newly added chart
            const chart = worksheet.charts.get(chartIndex);

            // Adding NSeries (chart data source) to the chart ranging from "A1" cell to "B4"
            chart.nSeries.add("A1:B4", true);

            // Setting the chart type of 2nd NSeries to display as line chart
            chart.nSeries.get(1).type = ChartType.Line;

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```  

{{% alert color="primary" %}}  

حالياً، يدعم Aspose.Cells فقط المخططات المخصصة التي تجمع بين مخططات الفطيرة، والخط، والعمود، والتكديس العمودي، ولكن سيتم دعم المزيد من المخططات في الإصدارات المستقبلية.  

{{% /alert %}}
