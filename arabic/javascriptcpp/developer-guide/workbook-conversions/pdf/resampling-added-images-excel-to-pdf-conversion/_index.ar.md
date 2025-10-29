---
title: إعادة عينات الصور المضافة  تحويل Excel إلى PDF باستخدام JavaScript عبر C++
linktitle: إعادة العينات للصور المضافة
type: docs
weight: 150
url: /ar/javascript-cpp/resampling-added-images-excel-to-pdf-conversion/
description: تعلم كيفية ضغط الصور المضافة إلى ملفات Excel لتقليل حجم PDF وتحسين أداء التحويل باستخدام Aspose.Cells for JavaScript عبر C++.
---

{{% alert color="primary" %}}

عند العمل مع ملفات Excel كبيرة تحتوي على العديد من الصور، قد تحتاج إلى ضغط الصور المضافة لتقليل حجم ملف PDF الناتج وتحسين أداء التحويل بشكل عام. يدعم Aspose.Cells for JavaScript عبر C++ إعادة عينات الصور المضافة لتقليل حجم ملف PDF الناتج وتحسين الأداء إلى حد معين.

{{% /alert %}}

يرجى الاطلاع على الكود النموذجي التالي الذي يصف كيفية إجراء المهمة باستخدام واجهة برمجة التطبيقات Aspose.Cells. النموذج يحول ملف Microsoft Excel إلى ملف PDF مع ضغط الصور في الملف.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells - Convert Excel to PDF</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Convert to PDF</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PdfSaveOptions, Utils } = AsposeCells;

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

            // Initialize a new Workbook by opening the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Instantiate the PdfSaveOptions
            const pdfSaveOptions = new PdfSaveOptions();

            // Set Image Resample properties (converted from setImageResample(300, 70))
            // Universal setter->property conversion: setImageResample(...) -> imageResample = [...]
            pdfSaveOptions.imageResample = [300, 70];

            // Save the PDF file (returns binary data)
            const outputData = workbook.save(SaveFormat.Pdf, pdfSaveOptions);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'OutputFile_out_pdf.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">PDF generated successfully! Click the download link to get the PDF file.</p>';
        });
    </script>
</html>
```

{{% alert color="primary" %}}

باستخدام خيار [**imageResample(number, number)**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#imageResample-number-number-) يقلل من حجم ملف PDF الناتج ولكنه قد يؤثر على جودة الصورة قليلاً.

{{% /alert %}} {{% alert color="primary" %}}

إذا كانت جداول البيانات الخاصة بك تحتوي على صيغ، من الأفضل استدعاء [**workbook.calculateFormula()**](https://reference.aspose.com/cells/javascript-cpp/workbook/#calculateFormula--) قبل تحويل جدول البيانات إلى تنسيق PDF. وذلك سيضمن إعادة حساب قيم الصيغ الخاصة وتقديم القيم الصحيحة في الملف الناتج PDF.

{{% /alert %}}
