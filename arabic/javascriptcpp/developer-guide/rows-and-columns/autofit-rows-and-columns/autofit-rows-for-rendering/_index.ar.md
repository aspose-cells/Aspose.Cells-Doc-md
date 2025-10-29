---
title: التلقائي لضبط الصفوف للعرض باستخدام جافا سكريبت عبر C++
linktitle: تحجيم الصفوف تلقائيًا للتقديم
type: docs
weight: 130
url: /ar/javascript-cpp/autofit-rows-for-rendering/
description: تعلم كيفية التلقائي لضبط صفوف العرض في Excel باستخدام Aspose.Cells for JavaScript عبر C++. منع قطع النص في ملفات PDF المحفوظة.
---

عموماً، عندما تريد عرض كل النص في خلية، يمكنك التمطيط التلقائي للصف في العرض العادي باستخدام تكبير 100% في مايكروسوفت إكسل. هذا يسمح برؤية النص بالكامل بشكل كامل في العرض العادي، وحتى عند الطباعة أو حفظ الملف كـ PDF، سيتم عرض النص بشكل صحيح.

ومع ذلك، في بعض الحالات، يعمل التمطيط التلقائي للصف بشكل جيد في العرض العادي، ولكن عند التبديل إلى عرض الطباعة أو حفظ الملف كـ PDF، يتم قطع النص. يرجى مراجعة الملف المصدر [Book1.xlsx](Book1.xlsx) ولقطات الشاشة.

![تم قص النص في عرض الطباعة](text_clipped_in_printview.png)

إذا كنت ترغب في منع قص النص في ملف PDF المحفوظ، يمكنك ضبط ارتفاع الصف تلقائيًا باستخدام خيار [AutoFitterOptions.forRendering](https://reference.aspose.com/cells/javascript-cpp/autofitteroptions/#forRendering--)،.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Autofit Rows and Save as PDF Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, AutoFitterOptions, SaveFormat, Utils } = AsposeCells;

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

            // Init workbook instance from uploaded file.
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Set autofit options for rendering.
            const autoFitterOptions = new AutoFitterOptions();
            autoFitterOptions.forRendering = true;

            // Autofit rows with options on first worksheet.
            const worksheet = workbook.worksheets.get(0);
            worksheet.autoFitRows(autoFitterOptions);

            // Save to pdf.
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the PDF file.</p>';
        });
    </script>
</html>
```

الآن، لم يتم قص النص في ملف PDF الناتج.

![النص لم يتم قصه في ملف PDF المحفوظ](text_not_clipped_in_saved_pdf.png)
