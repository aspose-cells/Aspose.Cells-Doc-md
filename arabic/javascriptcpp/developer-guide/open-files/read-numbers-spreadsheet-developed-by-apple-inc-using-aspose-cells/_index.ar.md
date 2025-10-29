---
title: قراءة جدول بيانات Numbers الذي طورته شركة Apple Inc. باستخدام Aspose.Cells for JavaScript عبر C++
linktitle: قراءة جدول بيانات الأرقام المطور من قبل Apple Inc. باستخدام Aspose.Cells
type: docs
weight: 140
url: /ar/javascript-cpp/read-numbers-spreadsheet-developed-by-apple-inc-using-aspose-cells/
description: تعلم كيفية قراءة جداول بيانات Numbers التي طورتها شركة Apple Inc. باستخدام Aspose.Cells for JavaScript عبر C++. 
---

## **سيناريوهات الاستخدام المحتملة**

Numbers هو تطبيق جدول بيانات طورته Apple Inc. يمكن لـ Aspose.Cells قراءة جداول بيانات Numbers، لكنه لا يدعم الكتابة إليها. يمكنه قراءة بيانات، وأنماط، وصيغ جداول بيانات Numbers.

## **قراءة جدول بيانات Numbers الذي طورته شركة Apple Inc. باستخدام Aspose.Cells for JavaScript عبر C++**

الرمز النموذجي التالي يُحمّل [Sample Numbers Spreadsheet](sampleNumbersByAppleInc.numbers) ويحوّله إلى [Output PDF Format](outputNumbersByAppleInc.pdf). ستحتاج إلى استخدام فئة [**LoadOptions**](https://reference.aspose.com/cells/javascript-cpp/loadoptions) وتحديد [**LoadFormat.Numbers**](https://reference.aspose.com/cells/javascript-cpp/loadformat) كمعامل في منشئها لتحميله بنجاح. يرجى تنزيل كلاهما من الروابط المقدمة. يمكنك تجربة الكود مع أي جدول بيانات Numbers. يرجى أيضًا قراءة تعليقات الكود للمزيد من المساعدة.

## **الكود المثالي**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Numbers to PDF Example</title>
    </head>
    <body>
        <h1>Convert Apple Numbers to PDF</h1>
        <input type="file" id="fileInput" accept=".numbers" />
        <button id="runExample">Convert to PDF</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, LoadOptions, LoadFormat } = AsposeCells;

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
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select a .numbers file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Specify load options to load Numbers spreadsheet
            const opts = new LoadOptions(LoadFormat.Numbers);

            // Load the Numbers spreadsheet in workbook with above load options
            const wb = new Workbook(new Uint8Array(arrayBuffer), opts);

            // Save the workbook to PDF format
            const outputData = wb.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputNumbersByAppleInc.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Conversion completed successfully! Click the download link to get the PDF.</p>';
        });
    </script>
</html>
```
