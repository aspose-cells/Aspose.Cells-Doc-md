---
title: تصدير المخطط إلى SVG مع سمة viewBox باستخدام JavaScript عبر C++
linktitle: تصدير الرسم البياني إلى SVG مع خاصية viewBox
type: docs
weight: 280
url: /ar/javascript-cpp/export-chart-to-svg-with-viewbox-attribute/
description: تعلم كيفية تصدير مخطط إلى صيغة SVG مع سمة viewBox باستخدام Aspose.Cells for JavaScript عبر C++.
---

{{% alert color="primary" %}}

بشكل افتراضي، عند تصدير الرسم البياني إلى تنسيق SVG، لا يتم تضمين سمة **viewBox** في XML الخاص به. ومع ذلك، يوفر Aspose.Cells خاصية [**ImageOrPrintOptions.svgFitToViewPort**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/#svgFitToViewPort--) التي عند تعيينها على **true** يقوم بتصدير الرسم البياني إلى SVG مع سمة viewBox.

{{% /alert %}}

## تصدير الرسم البياني إلى SVG بسمة viewBox

الرمز العينة التالي يقوم بتصدير الرسم البياني إلى تنسيق SVG مع سمة viewBox.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Chart to SVG Example</title>
    </head>
    <body>
        <h1>Chart to SVG Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Convert Chart to SVG</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, ImageOrPrintOptions, ImageType, Utils } = AsposeCells;

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

            // Set image or print options with SVGFitToViewPort true
            const opts = new ImageOrPrintOptions();
            opts.imageType = ImageType.Svg;
            opts.svgFitToViewPort = true;

            // Save the chart to svg format (returns data in browser)
            const svgData = await chart.toImage(opts);

            // Create blob and download link for SVG
            const blob = new Blob([svgData], { type: 'image/svg+xml' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Image_out.svg';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download SVG File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Chart converted to SVG successfully! Click the download link to get the SVG file.</p>';
        });
    </script>
</html>
```

{{% alert color="primary" %}}

إذا فتحت ملف SVG الخاص بالرسم البياني في المفكرة، فستجد سمة viewBox مماثلة لهذه.

{{< highlight java >}}

 <svg xmlns="http://www.w3.org/2000/svg"

     xmlns:xlink="http://www.w3.org/1999/xlink"

     width="100%" height="100%"

     viewBox="0 0 480 288">

{{< /highlight >}}

{{% /alert %}}
