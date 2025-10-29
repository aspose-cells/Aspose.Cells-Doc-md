---
title: تحويل المخطط إلى صورة بصيغة SVG باستخدام JavaScript عبر C++
linktitle: تحويل الرسم البياني إلى صورة بتنسيق SVG
type: docs
weight: 240
url: /ar/javascript-cpp/converting-chart-to-image-in-svg-format/
description: تعلم كيفية تحويل مخطط إلى صورة بصيغة SVG باستخدام Aspose.Cells for JavaScript عبر C++.
---

{{% alert color="primary" %}}

تعتبر الرسومات البيانية القابلة للتحجيم (SVG) تنسيق صورة ناقل معتمد على XML للرسوميات ثنائية الأبعاد والتي تدعم أيضًا التفاعل والرسوم المتحركة. مواصفات SVG هي معيار مفتوح تم تطويره من قبل W3C (المؤتمر العالمي للشبكة العنكبوتية) منذ عام 1999.

تم تعريف صور SVG وسلوكها في ملفات نص XML. وهذا يعني أنه يمكن البحث عنها وفهرستها وتدوينها وضغطها. كملفات XML، يمكن إنشاء وتحرير صور SVG باستخدام أي محرر نص، ولكن غالبًا ما يتم إنشاؤها باستخدام برمجيات الرسم.

يمكن لـ Aspose.Cells حفظ المخططات كصور بصيغ مختلفة مثل BMP، JPEG، PNG، GIF، SVG، وغيرها. يوضح هذا المقال كيفية حفظ مخطط بتنسيق SVG.

{{% /alert %}}

يشرح الرمز العينة التالي كيفية استخدام Aspose.Cells لتحويل الرسم البياني إلى صورة في تنسيق SVG. يحمل الرمز ملف Microsoft Excel المصدر ثم يحفظ الرسم البياني الأول الذي تم العثور عليه في الورقة العمل الأولى إلى SVG.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Export Chart to SVG</title>
    </head>
    <body>
        <h1>Export First Chart to SVG</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, ImageOrPrintOptions, ImageType } = AsposeCells;

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

            // Create workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access first chart inside the worksheet
            const chart = worksheet.charts.get(0);

            // Set image or print options
            const opts = new ImageOrPrintOptions();
            opts.imageType = ImageType.Svg;

            // Export the chart to SVG format (returns image bytes)
            const imageData = chart.toImage(opts);

            // Create downloadable SVG blob
            const blob = new Blob([imageData], { type: 'image/svg+xml' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Image_out.svg';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download SVG Image';

            document.getElementById('result').innerHTML = '<p style="color: green;">Chart exported to SVG. Click the download link to download the SVG file.</p>';
        });
    </script>
</html>
```
