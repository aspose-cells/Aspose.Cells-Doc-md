---
title: العمل مع تأثير الانعكاس للشكل أو المخطط باستخدام جافا سكريبت عبر C++
linktitle: العمل مع تأثير الانعكاس الداخلي للشكل أو الرسم البياني
type: docs
weight: 210
url: /ar/javascript-cpp/working-with-the-reflection-effect-of-shape-or-chart/
description: تعلم كيفية العمل مع تأثير الانعكاس للأشكال أو الرسوم البيانية باستخدام Aspose.Cells for JavaScript عبر C++. اضبط خصائص الانعكاس المختلفة لتحقيق النتائج المطلوبة.
---

## **سيناريوهات الاستخدام المحتملة**
يوفر Aspose.Cells for JavaScript عبر C++ الخاصية [Shape.reflection](https://reference.aspose.com/cells/javascript-cpp/shape/#reflection--) جنبًا إلى جنب مع فئة [ReflectionEffect](https://reference.aspose.com/cells/javascript-cpp/reflectioneffect) للعمل مع تأثير الانعكاس للشكل أو الرسم البياني. تحتوي فئة [ReflectionEffect](https://reference.aspose.com/cells/javascript-cpp/reflectioneffect) على Properties التالية التي يمكن ضبطها لتحقيق نتائج مختلفة حسب متطلبات التطبيق.

- [التأثير الانعكاسي blur](https://reference.aspose.com/cells/javascript-cpp/reflectioneffect/#blur--)
- [اتجاه الانعكاس](https://reference.aspose.com/cells/javascript-cpp/reflectioneffect/#direction--)
- [مسافة الانعكاس](https://reference.aspose.com/cells/javascript-cpp/reflectioneffect/#distance--)
- [اتجاه تلاشي الانعكاس](https://reference.aspose.com/cells/javascript-cpp/reflectioneffect/#fadeDirection--)
- [الانعكاس مع الدوران مع الشكل](https://reference.aspose.com/cells/javascript-cpp/reflectioneffect/#rotWithShape--)
- [حجم الانعكاس](https://reference.aspose.com/cells/javascript-cpp/reflectioneffect/#size--)
- [شفافية الانعكاس](https://reference.aspose.com/cells/javascript-cpp/reflectioneffect/#transparency--)
- [نوع الانعكاس](https://reference.aspose.com/cells/javascript-cpp/reflectioneffect/#type--)

## **العمل مع تأثير الانعكاس للشكل أو الرسم البياني**
يقوم الكود النموذجي التالي بتحميل [ملف الإكسل المصدر](5115424.xlsx) والوصول إلى الشكل الأول في ورقة العمل الافتراضية. يضبط خصائص مختلفة من [Shape.reflection](https://reference.aspose.com/cells/javascript-cpp/shape/#reflection--) ثم يحفظ دفتر العمل في [ملف الإكسل الناتج](5115423.xlsx).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Set Shape Reflection Effect Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;"></a>
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

            // Instantiating a Workbook object by loading the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access first shape
            const shape = worksheet.shapes.get(0);

            // Set the reflection effect of the shape, set its Blur, Size, Transparency and Distance properties
            const reflectionEffect = shape.reflection;
            reflectionEffect.blur = 30;
            reflectionEffect.size = 90;
            reflectionEffect.transparency = 0;
            reflectionEffect.distance = 80;

            // Save the workbook in xlsx format
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Reflection effect updated successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
