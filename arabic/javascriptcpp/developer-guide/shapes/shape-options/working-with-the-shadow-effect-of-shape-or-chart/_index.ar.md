---
title: العمل مع تأثير الظل للشكل أو الرسم البياني باستخدام جافا سكريبت عبر C++
linktitle: العمل مع تأثير الظل للشكل أو الرسم البياني
type: docs
weight: 220
url: /ar/javascript-cpp/working-with-the-shadow-effect-of-shape-or-chart/
description: تعلم كيفية العمل مع تأثير الظل للأشكال أو الرسوم البيانية باستخدام Aspose.Cells for JavaScript عبر C++.
---

## **سيناريوهات الاستخدام المحتملة**  
يوفر Aspose.Cells for JavaScript عبر C++ الخاصية [Shape.shadowEffect](https://reference.aspose.com/cells/javascript-cpp/shape/#shadowEffect--) جنبًا إلى جنب مع فئة [ShadowEffect](https://reference.aspose.com/cells/javascript-cpp/shadoweffect) للعمل مع تأثير الظل للشكل أو الرسم البياني. تحتوي فئة [ShadowEffect](https://reference.aspose.com/cells/javascript-cpp/shadoweffect) على Properties التالية التي يمكن ضبطها لتحقيق نتائج مختلفة حسب متطلبات التطبيق.  

- [زاوية تأثير الظل](https://reference.aspose.com/cells/javascript-cpp/shadoweffect/#angle--)  
- [تمويه تأثير الظل](https://reference.aspose.com/cells/javascript-cpp/shadoweffect/#blur--)  
- [لون تأثير الظل](https://reference.aspose.com/cells/javascript-cpp/shadoweffect/#color--)  
- [مسافة تأثير الظل](https://reference.aspose.com/cells/javascript-cpp/shadoweffect/#distance--)  
- [نوع ضبط الظل المسبق](https://reference.aspose.com/cells/javascript-cpp/shadoweffect/#presetType--)  
- [حجم تأثير الظل](https://reference.aspose.com/cells/javascript-cpp/shadoweffect/#size--)  
- [تأثير الظل الشفافية](https://reference.aspose.com/cells/javascript-cpp/shadoweffect/#transparency--)  

## **العمل مع تأثير الظل للشكل أو الرسم البياني**  
يحمّل التعليمات البرمجية النموذجية التالية ملف Excel المصدر (5115425.xlsx) ويصل إلى الشكل الأول في ورقة العمل الأولى ويحدد الخصائص الفرعية لخاصية (Shape.shadowEffect) ثم يحفظ المصنف في ملف Excel الناتج (5115411.xlsx).  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells - Shape Shadow Effect Example</h1>
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
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            const worksheet = workbook.worksheets.get(0);
            const shape = worksheet.shapes.get(0);

            const shadowEffect = shape.shadowEffect;
            shadowEffect.angle = 150;
            shadowEffect.blur = 4;
            shadowEffect.distance = 45;
            shadowEffect.transparency = 0.3;

            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Shadow effect applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
