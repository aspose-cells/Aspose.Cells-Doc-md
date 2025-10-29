---
title: عرض الأحرف الإضافية Unicode في PDF الناتج بواسطة Aspose.Cells for JavaScript عبر C++
linktitle: تقديم الحروف الأعلى من يونيكود في ملف PDF الناتج باستخدام Aspose.Cells
type: docs
weight: 350
url: /ar/javascript-cpp/render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells/
description: تعلم كيفية عرض الأحرف الإضافية Unicode في PDF الناتج باستخدام Aspose.Cells for JavaScript عبر C++. 
---

{{% alert color="primary" %}}

الحروف اليونيكود العادية طول كل منها 2 بايت بينما الحروف اليونيكود الأعلى طول كل منها 4 بايت. Aspose.Cells الآن يدعم تقديم هذه الحروف اليونيكود الأعلى بطول 4 بايت.

في معيار الحروف اليونيكود، الحروف الأعلى هي الحروف التي تم تخصيص نقاط الرموز لها من U+10000 إلى U+10FFFF. وبمعنى آخر، هذه هي الحروف اليونيكود التي تكون أكبر من U+FFFF.

- في UTF-8 طول كل من هذه الحروف هو 4 بايت.
- في UTF-16، هذه الحروف تتطلب 2 حروف دعائية (وحدات بت بطول 16).

{{% /alert %}}

## عرض الأحرف الإضافية Unicode في PDF الناتج بواسطة Aspose.Cells for JavaScript عبر C++

تُظهر لقطة الشاشة التالية كيفية عرض Aspose.Cells لملف إكسيل المصدر([ملف إكسيل](5115563.xlsx)) في PDF الناتج([ملف PDF](5115564.pdf)). كما ترى، تم عرض جميع الأحرف الفرعية المتمددة الثلاثة بشكل مطابق تمامًا لما قام به Microsoft Excel.

![todo:image_alt_text](output.png)

## كود عينة

يمكنك استخدام هذا الكود العيني لتحويل [ملف Excel المصدر](5115563.xlsx) إلى [PDF الناتج](5115564.pdf).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Render Unicode Supplementary Characters to PDF</title>
    </head>
    <body>
        <h1>Render Unicode Supplementary Characters to PDF</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;

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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Save the workbook as PDF
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'RenderUnicodeInOutput_out.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">PDF generated successfully! Click the download link to get the PDF file.</p>';
        });
    </script>
</html>
```
