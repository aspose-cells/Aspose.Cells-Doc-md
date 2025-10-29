---
title: استبدال النص في مصنف العمل باستخدام التعبيرات العادية مع جافا سكريبت عبر ++C
linktitle: استبدال النص في دفتر العمل باستخدام التعبير العادي
type: docs
weight: 90
url: /ar/javascript-cpp/replace-text-in-a-workbook-using-regular-expression/
description: استبدال النص في مصنف باستخدام التعبيرات العادية في جافا سكريبت عبر ++C
---

يقدم Aspose.Cells ميزة استبدال النص في دفتر العمل باستخدام التعبيرات العادية. لهذا، توفر API الخاص [**ReplaceOptions.regexKey**](https://reference.aspose.com/cells/javascript-cpp/replaceoptions/#regexKey--) الخاص بفئة [**ReplaceOptions**](https://reference.aspose.com/cells/javascript-cpp/replaceoptions). تحديد [**ReplaceOptions.regexKey**](https://reference.aspose.com/cells/javascript-cpp/replaceoptions/#regexKey--) على أنه **true** يشير إلى أن المفتاح المقصود سيكون تعبيرًا عاديًا.

يوضح مقتطف الكود التالي استخدام الخاصية [**ReplaceOptions.regexKey**](https://reference.aspose.com/cells/javascript-cpp/replaceoptions/#regexKey--) باستخدام ملف Excel النموذجي ([ملف Excel sample](101089318.xlsx)). المخرجات ([ملف الإخراج](101089319.xlsx)) التي تم إنشاؤها بواسطة المقتطف مرفقة للمرجعية.

## **الكود المثالي**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Regex Replace Example</title>
    </head>
    <body>
        <h1>Regex Replace Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ReplaceOptions } = AsposeCells;

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

            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            const replaceOptions = new ReplaceOptions();
            replaceOptions.caseSensitive = false;
            replaceOptions.matchEntireCellContents = false;
            replaceOptions.regexKey = true;

            workbook.replace("\\bKIM\\b", "^^^TIM^^^", replaceOptions);

            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'RegexReplace_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Regex replace completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
