---
title: تحديد كيفية عبور السلسلة في ملف PDF والصورة الناتجة باستخدام جافا سكريبت عبر C++
linktitle: تحديد كيفية عبور السلسلة في ملف PDF الناتج والصورة
type: docs
weight: 120
url: /ar/javascript-cpp/specify-how-to-cross-string-in-output-pdf-and-image/
description: تعلم التحكم في تجاوز النص في PDF / صورة الناتجة عن طريق تحديد نوع العبور باستخدام Aspose.Cells for JavaScript عبر C++.
---

## **سيناريوهات الاستخدام المحتملة**

 عندما يحتوي خلية على نص أو سلسلة أكبر من عرض الخلية، فإن السلسلة تتجاوز إذا كانت الخلية التالية في العمود التالي فارغة أو غير موجودة. عند حفظ ملف Excel الخاص بك كـ PDF/صورة، يمكنك التحكم في هذا التجاوز عن طريق تحديد نوع العبور باستخدام تعداد [**TextCrossType**](https://reference.aspose.com/cells/javascript-cpp/textcrosstype). وله القيم التالية:

- **نوع تمرير النصافتراضي**: عرض النص مثل MS Excel يعتمد على الخلية التالية. إذا كانت الخلية التالية فارغة، فسيتم تجاوز النص أو قطعه.

- **TextCrossType.CrossKeep**: عرض النص مثل تصدير MS Excel إلى PDF/صور.

- **TextCrossType.CrossOverride**: عرض كل النص عن طريق عبور خلايا أخرى وتجاوز نص الخلايا المعترضة.

- **TextCrossType.StrictInCell**: عرض السلسلة فقط ضمن عرض الخلية.

## **تحديد كيفية عبور السلسلة في ملف PDF/صورة الناتج باستخدام TextCrossType**

يعرض الرمز النموذجي التالي تحميل ملف Excel النموذجي وحفظه إلى تنسيق PDF/صور عن طريق تحديد قيم مختلفة [**TextCrossType**](https://reference.aspose.com/cells/javascript-cpp/textcrosstype). يمكن تنزيل ملف Excel النموذجي والملفات الناتجة من الروابط التالية:

[sampleCrossType.xlsx](81920905.xlsx)  

[outputCrossType.pdf](81920903.pdf)  

[outputCrossType.png](81920904.png)  

### مثال على الكود

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Cross Text Type to PDF and Image</title>
    </head>
    <body>
        <h1>Convert Excel to PDF and PNG (Text Cross Type)</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <div>
            <a id="downloadLinkPdf" style="display: none; margin-right: 10px;">Download PDF</a>
            <a id="downloadLinkPng" style="display: none;">Download PNG</a>
        </div>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PdfSaveOptions, ImageOrPrintOptions, SheetRender, TextCrossType, Utils } = AsposeCells;

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
            const downloadLinkPdf = document.getElementById('downloadLinkPdf');
            const downloadLinkPng = document.getElementById('downloadLinkPng');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            // Clear previous links/messages
            downloadLinkPdf.style.display = 'none';
            downloadLinkPng.style.display = 'none';
            resultDiv.innerHTML = '';

            // Read file from input
            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Initialize PDF save options
            const pdfSaveOptions = new PdfSaveOptions();
            // Set text cross type (converted setter -> property)
            pdfSaveOptions.textCrossType = TextCrossType.StrictInCell;

            // Save PDF file data
            const pdfData = workbook.save(SaveFormat.Pdf, pdfSaveOptions);
            const pdfBlob = new Blob([pdfData], { type: 'application/pdf' });
            downloadLinkPdf.href = URL.createObjectURL(pdfBlob);
            downloadLinkPdf.download = 'outputCrosssType.pdf';
            downloadLinkPdf.style.display = 'inline-block';
            downloadLinkPdf.textContent = 'Download PDF File';

            // Initialize image or print options
            const imageSaveOptions = new ImageOrPrintOptions();
            // Set text cross type (converted setter -> property)
            imageSaveOptions.textCrossType = TextCrossType.StrictInCell;

            // Initialize sheet renderer for first worksheet
            const sheetRenderer = new SheetRender(workbook.worksheets.get(0), imageSaveOptions);

            // Render the first page/image of the sheet to image data
            const imageData = sheetRenderer.toImage(0);
            const imageBlob = new Blob([imageData], { type: 'image/png' });
            downloadLinkPng.href = URL.createObjectURL(imageBlob);
            downloadLinkPng.download = 'outputCrosssType.png';
            downloadLinkPng.style.display = 'inline-block';
            downloadLinkPng.textContent = 'Download PNG File';

            resultDiv.innerHTML = '<p style="color: green;">Conversion completed! Download links are ready.</p>';
        });
    </script>
</html>
```
