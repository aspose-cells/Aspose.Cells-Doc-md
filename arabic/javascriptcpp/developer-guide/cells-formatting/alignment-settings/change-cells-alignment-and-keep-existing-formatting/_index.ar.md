---
title: تغيير توجيه الخلايا والاحتفاظ بالتنسيقات الحالية
linktitle: تغيير توجيه الخلايا والاحتفاظ بالتنسيقات الحالية
description: استخدام مكتبة Aspose.Cells لتغيير محاذاة الخلية والحفاظ على التنسيق الحالي في جافا سكريبت عبر C++
keywords: Aspose.Cells، جافا سكريبت عبر C++، محاذاة الخلية، الحفاظ على التنسيق الحالي
type: docs
weight: 340
url: /ar/javascript-cpp/change-cells-alignment-and-keep-existing-formatting/
---

## **سيناريوهات الاستخدام المحتملة**

في بعض الأحيان، ترغب في تغيير محاذاة عدة خلايا ولكن مع الاحتفاظ بالتنسيق الحالي. يتيح لك Aspose.Cells for JavaScript عبر C++ القيام بذلك باستخدام أسلوب [**StyleFlag.alignments(boolean)**](https://reference.aspose.com/cells/javascript-cpp/styleflag/#alignments-boolean-). إذا قمت بضبطه على **true**، فسيتم تطبيق التغييرات على المحاذاة، وإلا فلن يتم ذلك. يرجى ملاحظة، أن كائن [**StyleFlag**](https://reference.aspose.com/cells/javascript-cpp/styleflag) يُمرر كمعامل إلى أسلوب [**Range.applyStyle(Style, StyleFlag)**](https://reference.aspose.com/cells/javascript-cpp/range/#applyStyle-style-styleflag-) الذي يطبق التنسيق على مجموعة من الخلايا.

## **تغيير توجيه الخلايا والاحتفاظ بالتنسيقات الحالية**

الكود النموذجي التالي يقوم بتحميل الملف الإكسل النموذجي، ينشئ المدى ويضبط توسيطه أفقيا وعموديا ويحتفظ بالتنسيق الحالي. الصورة النموذجية التالية تقارن ملف الإكسل النموذجي وملف الإكسل الناتج وتُظهر أن جميع التنسيقات الحالية للخلايا هي نفسها باستثناء أن الخلايا الآن موجهة في منتصف الخط أفقيًا وعموديًا.

![todo:image_alt_text](change-cells-alignment-and-keep-existing-formatting_1.png)

## **الكود المثالي**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Change Cells Alignment and Keep Existing Formatting</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, StyleFlag, TextAlignmentType, Utils } = AsposeCells;

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
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate Workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Create cells range
            const range = worksheet.cells.createRange("B2:D7");

            // Create style object
            const style = workbook.createStyle();

            // Set the horizontal and vertical alignment to center using property assignments
            style.horizontalAlignment = TextAlignmentType.Center;
            style.verticalAlignment = TextAlignmentType.Center;

            // Create style flag object
            const flag = new StyleFlag();
            flag.alignments = true; // Set style flag alignments true

            // Apply style to range of cells
            range.applyStyle(style, flag);

            // Save the workbook in XLSX format and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputChangeCellsAlignmentAndKeepExistingFormatting.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
