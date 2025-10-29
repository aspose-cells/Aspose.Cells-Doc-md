---
title: تغيير اتجاه تسميات العلامات باستخدام JavaScript عبر C++
linktitle: تغيير اتجاه التسمية التلقائية
description: تعلم كيفية تغيير اتجاه تسميات العلامات في Aspose.Cells for JavaScript عبر C++. دليلنا سيساعدك في فهم كيفية ضبط توجيه تسميات العلامات على المحاور، بما في ذلك الاتجاه الأفقي، الرأسي، والمائل.
keywords: Aspose.Cells for JavaScript عبر C++، تسميات العلامات، الاتجاه، التوجيه، المحاور، أفقي، رأسي، مائل.
type: docs
weight: 170
url: /ar/javascript-cpp/change-tick-label-direction/
---

## **تغيير اتجاه التسمية التلقائية**

توفر Aspose.Cells إمكانية تغيير اتجاه تسميات العلامات على الرسم البياني باستخدام خاصية [**TickLabels.directionType**](https://reference.aspose.com/cells/javascript-cpp/ticklabels/#directionType--). تقبل الخاصية [**TickLabels.directionType**](https://reference.aspose.com/cells/javascript-cpp/ticklabels/#directionType--) قيمة تعداد [**ChartTextDirectionType**](https://reference.aspose.com/cells/javascript-cpp/charttextdirectiontype). يوفر تعداد [**ChartTextDirectionType**](https://reference.aspose.com/cells/javascript-cpp/charttextdirectiontype) الأعضاء التالية:

- أفقي
- رأسي
- دوران 90
- دوران 270
- مكدس

صورة تقارن بين الملف الأصلي وملف الإخراج

### **صورة الملف الأصلي**

![todo:image_alt_text](change-tick-label-direction_1.jpg)

### **صورة الملف الإخراج**

![todo:image_alt_text](change-tick-label-direction_2.jpg)

مقتطف الكود التالي يغير اتجاه تسمية العلامة المحورية من دوران 90 إلى أفقي.

## **الكود المثالي**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Change Tick Label Direction Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;"></a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ChartTextDirectionType } = AsposeCells;

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
            const result = document.getElementById('result');

            if (!fileInput.files.length) {
                result.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            const worksheet = workbook.worksheets.get(0);

            const chart = worksheet.charts.get(0);

            chart.categoryAxis.tickLabels.directionType = ChartTextDirectionType.Horizontal;

            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputChangeChartDataLableDirection.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            result.innerHTML = '<p style="color: green;">Tick label direction changed. Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

يمكن تحميل ملفات المصدر والإخراج من الروابط التالية.

[ملف المصدر](105480221.xlsx)

[ملف الإخراج](105480223.xlsx)
