---
title: قراءة تسميات المحاور بعد حساب المخطط باستخدام JavaScript عبر C++
linktitle: قراءة تسميات المحور بعد حساب الرسم البياني
description: تعلم كيفية قراءة تسميات المحاور في Aspose.Cells for JavaScript عبر C++ بعد حساب المخطط. سيبين لك دليلنا كيفية الوصول إلى تسميات المحاور واسترجاعها، بما في ذلك تنسيقها وتحديد مكانها.
keywords: Aspose.Cells for JavaScript، مخطط، تسميات المحاور، الحساب، القراءة، الوصول، الاسترجاع، التنسيق، التحديد، JavaScript عبر C++
type: docs
weight: 90
url: /ar/javascript-cpp/read-axis-labels-after-calculating-the-chart/
---

## **سيناريوهات الاستخدام المحتملة**

 يمكنك قراءة تسميات محاور المخطط بعد حساب قيمه باستخدام طريقة [**Chart.calculate()**](https://reference.aspose.com/cells/javascript-cpp/chart/#calculate--). يرجى استخدام الخاصية [**Axis.axisTexts**](https://reference.aspose.com/cells/javascript-cpp/axis/#axisTexts--) لهذا الغرض التي ستُرجع قائمة تسميات المحاور.

## **قراءة تسميات المحور بعد حساب الرسم البياني**

يرجى الاطلاع على رمز العينة التالي الذي يحمل [ملف Excel عيني](ReadAxisLabels.xlsx) ويقرأ تسميات المحور الفئوي للرسم البياني في الورقة العمل الأولى. ثم يقوم بطباعة قيم تسميات المحور على وحدة التحكم. يرجى الاطلاع على الإخراج على وحدة التحكم من رمز العينة الذي يلي للرجوع إليه.

## **الكود المثالي**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Read Axis Labels</title>
    </head>
    <body>
        <h1>Read Chart Category Axis Labels</h1>
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
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access the chart
            const chart = worksheet.charts.get(0);

            // Calculate the chart
            chart.calculate();

            // Read axis labels of category axis
            const lstLabels = chart.categoryAxis.axisTexts;

            // Display axis labels
            let html = '<h2>Category Axis Labels:</h2>';
            html += '<hr/>';
            if (!lstLabels || !lstLabels.length) {
                html += '<p>No axis labels found.</p>';
            } else {
                html += '<ul>';
                for (let i = 0; i < lstLabels.length; i++) {
                    console.log(lstLabels[i]);
                    html += `<li>${lstLabels[i]}</li>`;
                }
                html += '</ul>';
            }
            resultDiv.innerHTML = html;
        });
    </script>
</html>
```

## **مخرجات الوحدة**

{{< highlight javascript >}}  
 Category Axis Labels:  

\---------------------  

Iran  

China  

USA  

Brazil  

England  
{{< /highlight >}}
