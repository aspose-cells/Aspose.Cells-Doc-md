---
title: عرض ورقة العمل على السياق الرسومي باستخدام JavaScript عبر C++
linktitle: تقديم ورقة العمل إلى السياق الرسومي
type: docs
weight: 300
url: /ar/javascript-cpp/render-worksheet-to-graphic-context/
description: تعلم كيف تعرض ورقة عمل على السياق الرسومي باستخدام Aspose.Cells for JavaScript عبر C++. يتضمن ذلك العرض إلى ملفات الصور، الشاشات، والطابعات.
---

{{% alert color="primary" %}}

يمكن الآن لـ Aspose.Cells عرض أوراق العمل على سياق رسومي. يمكن أن يكون السياق الرسومي أي شيء مثل ملف صورة، أو شاشة، أو طابعة، وما إلى ذلك. يرجى استخدام أحد الطريقتين التاليين لعرض ورقة العمل على سياق رسومي.

- [**SheetRender.toImage(int pageIndex, Graphics g, float x, float y)**](https://reference.aspose.com/cells/javascript-cpp/sheetrender/#toImage-number-)
- [**SheetRender.toImage(int pageIndex, Graphics g, float x, float y, float width, float height)**](https://reference.aspose.com/cells/javascript-cpp/sheetrender/#toImage-number-)

{{% /alert %}}

يوضح الكود التالي كيفية استخدام Aspose.Cells لعرض ورقة عمل على سياق رسومي. بمجرد تنفيذ الكود، سيتم طباعة كامل ورقة العمل وملء المساحة الفارغة المتبقية باللون الأزرق في السياق الرسومي وحفظ الصورة كملف **OutputImage_out_.png**. يمكنك استخدام أي ملف Excel كمصدر لتجربة هذا الكود. يرجى أيضًا قراءة التعليقات داخل الكود لفهم أفضل.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Render Worksheet to Image</title>
    </head>
    <body>
        <h1>Render Worksheet to Image</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, ImageOrPrintOptions, SheetRender, Utils } = AsposeCells;

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

            // Create empty image buffer options
            const bmpOptions = new ImageOrPrintOptions();
            bmpOptions.onePagePerSheet = true;

            // Render worksheet to image
            const sheetRender = new SheetRender(worksheet, bmpOptions);
            const imageData = sheetRender.toImage(0);

            // Create blob and provide download link for PNG
            const blob = new Blob([imageData], { type: 'image/png' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'OutputImage_out.png';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Image';

            document.getElementById('result').innerHTML = '<p style="color: green;">Image rendered successfully! Click the download link to download the PNG.</p>';
        });
    </script>
</html>
```
