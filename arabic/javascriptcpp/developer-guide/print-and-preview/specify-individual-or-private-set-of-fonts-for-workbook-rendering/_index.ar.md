---
title: تحديد مجموعة الخطوط الفردية أو الخاصة لعرض المصنف باستخدام JavaScript عبر C++
linktitle: تحديد مجموعة خطوط فردية أو خاصة لتقديم الدفتر
type: docs
weight: 40
url: /ar/javascript-cpp/specify-individual-or-private-set-of-fonts-for-workbook-rendering/
description: تعلم كيف تحدد مجموعات الخطوط الفردية أو الخاصة لعرض المصنف باستخدام Aspose.Cells for JavaScript عبر C++.
---

## **سيناريوهات الاستخدام المحتملة**  

عموماً، تحدد مجلد الخطوط أو قائمة الخطوط لكل المصنفات ولكن أحيانًا، عليك تحديد مجموعة خطوط فردية أو خاصة لمصنفاتك. يوفر Aspose.Cells for JavaScript عبر C++ فئة [**IndividualFontConfigs**](https://reference.aspose.com/cells/javascript-cpp/individualfontconfigs) التي يمكن استخدامها لتحديد مجموعة الخطوط الفردية أو الخاصة لمصنفك.  

## **تحديد مجموعة خطوط فردية أو خاصة لتقديم الدفتر**  

يحمّل المثال التالي ملف Excel النموذجي (67338268.xlsx) باستخدام مجموعة خطوط فردية أو خاصة محددة باستخدام فئة [**IndividualFontConfigs**](https://reference.aspose.com/cells/javascript-cpp/individualfontconfigs). يرجى الاطلاع على الخط (67338271.zip) المستخدم داخل الكود وكذلك ملف PDF الناتج (67338269.pdf). يُظهر لقطة الشاشة التالية كيف يبدو ملف PDF الناتج إذا تم العثور على الخط بنجاح.  

![todo:image_alt_text](specify-individual-or-private-set-of-fonts-for-workbook-rendering_1.png)  

## **الكود المثالي**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Specify Individual Or Private Fonts Example</title>
    </head>
    <body>
        <h1>Specify Individual Or Private Fonts Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, LoadOptions, IndividualFontConfigs } = AsposeCells;

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

            // Path of your custom font directory.
            const customFontsDir = "C:\\TempDir\\CustomFonts";

            // Specify individual font configs custom font directory.
            const fontConfigs = new IndividualFontConfigs();

            // If you comment this line or if custom font directory is wrong or 
            // if it does not contain required font then output pdf will not be rendered correctly.
            // Converted setFontFolder -> property assignment (first argument used)
            fontConfigs.fontFolder = customFontsDir;

            // Specify load options with font configs.
            const opts = new LoadOptions(AsposeCells.LoadFormat.Xlsx);
            // Converted setFontConfigs -> property assignment
            opts.fontConfigs = fontConfigs;

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Load the sample Excel file with individual font configs.
            const wb = new Workbook(new Uint8Array(arrayBuffer), opts);

            // Save to PDF format.
            const outputData = wb.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputSpecifyIndividualOrPrivateSetOfFontsForWorkbookRendering.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">PDF generated successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
