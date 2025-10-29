---
title: اكتشف هل نقاط البيانات موجودة في الدائرة الثانية أو العمود في مخطط Pie of Pie أو Bar of Pie باستخدام JavaScript عبر C++  
linktitle: العثور على ما إذا كانت نقاط البيانات في الرسم البياني الدائري الثاني أو الرسم البياني الشريطي الثاني  
description: تعلم كيفية استخدام Aspose.Cells for JavaScript عبر C++ لمعرفة ما إذا كانت نقاط البيانات في الدائرة الثانية أو العمود في مخطط Pie of Pie أو Bar of Pie. ستوضح هذه الدليل كيف تتعرف وتصل إلى الدائرة أو العمود الثانوي في مخطط مركب، مما يسمح لك بتحليل ومعالجة البيانات بفعالية.  
keywords: Aspose.Cells for JavaScript عبر C++، مخطط Pie of Pie، مخطط Bar of Pie، الدائرة الثانوية، العمود الثانوي، تحليل البيانات، معالجة البيانات.  
type: docs  
weight: 180  
url: /ar/javascript-cpp/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/  
---  

## **سيناريوهات الاستخدام المحتملة**  
يمكنك معرفة ما إذا كانت نقاط بيانات السلسلة في الدائرة الثانية على *Pie of Pie* أو في العمود من *Bar of Pie* باستخدام Aspose.Cells for JavaScript عبر C++. يرجى استخدام الخاصية [ChartPoint.isInSecondaryPlot()](https://reference.aspose.com/cells/javascript-cpp/chartpoint/#isInSecondaryPlot--) لتحديد ذلك.  

 يرجى تحميل [ملف Excel النموذجي](5115193.xlsx) المستخدم في كود المثال التالي ومراجعة ناتج وحدة التحكم الخاصة به. إذا قمت بفتح [ملف Excel النموذجي](5115193.xlsx)، ستجد أن جميع نقاط البيانات التي أقل من 10 تقع داخل الشريط على مخطط *الشريط من دائري* كما يظهر أيضًا في الناتج الخاص بوحدة التحكم.  
## **العثور على ما إذا كانت نقاط البيانات في الفقاعة الثانية أو العمود على مخطط 'بي of بي' أو 'عمود من بي'**  
 يظهر الكود المثال التالي كيفية تحديد ما إذا كانت نقاط البيانات في الدائري الثاني أو الشريط على مخطط *الدائري من دائري* أو *شريطي من دائري*.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Bar of Pie Chart Data Points Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell, Utils } = AsposeCells;

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
            resultDiv.innerHTML = '';
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file (e.g., PieBars.xlsx).</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access first chart which is Bar of Pie chart and calculate it
            const chart = worksheet.charts.get(0);
            chart.calculate();

            // Access the chart series
            const series = chart.nSeries.get(0);

            // Iterate and collect output
            let outputLines = [];
            for (let i = 0; i < series.points.count; i++) {
                // Access chart point
                const chartPoint = series.points.get(i);

                // Skip null values
                if (chartPoint.yValue === null) continue;

                // Print the chart point value and see if it is inside bar or pie.
                // If the IsInSecondaryPlot is true, then the data point is inside bar 
                // otherwise it is inside the pie. 
                const valueLine = "Value: " + chartPoint.yValue;
                const inSecondaryLine = "IsInSecondaryPlot: " + chartPoint.isInSecondaryPlot();
                console.log(valueLine);
                console.log(inSecondaryLine);
                console.log();

                outputLines.push(valueLine);
                outputLines.push(inSecondaryLine);
                outputLines.push("");
            }

            if (outputLines.length === 0) {
                resultDiv.innerHTML = '<p style="color: orange;">No data points found or all values are null.</p>';
            } else {
                resultDiv.innerHTML = '<pre>' + outputLines.join('\n') + '</pre>';
            }
        });
    </script>
</html>
```  
## **مخرجات الوحدة**  
يرجى مراجعة مخرجات وحدة التحكم التالية الناتجة بعد تنفيذ الرمز النموذجي أعلاه باستخدام [ملف إكسل النموذجي](5115193.xlsx). إذا كانت [ChartPoint.isInSecondaryPlot()](https://reference.aspose.com/cells/javascript-cpp/chartpoint/#isInSecondaryPlot--) **خاطئة**، فإن نقطة البيانات داخل الدائرة، وإذا كانت **صحيحة**، فإن نقطة البيانات داخل العمود.  

{{< highlight javascript >}}  
 Value: 15  
IsInSecondaryPlot: false  

Value: 9  
IsInSecondaryPlot: true  

Value: 2  
IsInSecondaryPlot: true  

Value: 40  
IsInSecondaryPlot: false  

Value: 5  
IsInSecondaryPlot: true  

Value: 4  
IsInSecondaryPlot: true  

Value: 25  
IsInSecondaryPlot: false  
{{< /highlight >}}
