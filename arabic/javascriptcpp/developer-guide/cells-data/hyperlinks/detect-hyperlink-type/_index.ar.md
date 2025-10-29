---
title: اكتشاف نوع الرابط الفائق
type: docs
weight: 160
url: /ar/javascript-cpp/detect-hyperlink-type/
description: تعلم كيفية اكتشاف نوع الرابط التشعبي عبر Aspose.Cells for JavaScript عبر API C++.
keywords: اكتشاف نوع الرابط التشعبي JavaScript عبر C++، اكتشاف نوع الرابط التشعبي JavaScript عبر C++، الحصول على نوع الرابط التشعبي JavaScript عبر C++
---

## **كشف نوع الروابط التشعبية**

يمكن لملف إكسل أن يحتوي على أنواع مختلفة من الروابط التشعبية مثل الخارجية، مرجع الخلية، مسار الملف، وما إلى ذلك. يدعم Aspose.Cells for JavaScript عبر C++ ميزة اكتشاف نوع الرابط التشعبي. تمثل أنواع الروابط التشعبية بواسطة تعداد [**TargetModeType**](https://reference.aspose.com/cells/javascript-cpp/targetmodetype). التعداد [**TargetModeType**](https://reference.aspose.com/cells/javascript-cpp/targetmodetype) يتضمن الأعضاء التالية.

- خارجي: رابط خارجي
- مسار الملف: المسار الكامل والنسبي إلى الملفات/المجلدات.
- بريد إلكتروني: Email
- مرجع الخلية: رابط إلى خلية أو نطاق مسمى.

للتحقق من نوع الرابط التشعبي، يوفر الصنف [**Hyperlink**](https://reference.aspose.com/cells/javascript-cpp/hyperlink) خاصية [**linkType**](https://reference.aspose.com/cells/javascript-cpp/hyperlink/#linkType--) من النوع [**TargetModeType**](https://reference.aspose.com/cells/javascript-cpp/targetmodetype). يوضح مقطع الشفرة التالي استخدام الخاصية [**linkType**](https://reference.aspose.com/cells/javascript-cpp/hyperlink/#linkType--) باستخدام ملف إكسل المصدر ([94896195.xlsx](94896195.xlsx)).

### كود المصدر

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Link Types Example</title>
    </head>
    <body>
        <h1>Link Types Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell, Utils } = AsposeCells;

        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");

            document.getElementById('runExample').addEventListener('click', async () => {
                const fileInput = document.getElementById('fileInput');
                const resultDiv = document.getElementById('result');

                if (!fileInput.files.length) {
                    resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                    return;
                }

                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();

                // Instantiating a Workbook object from the uploaded file
                const workbook = new Workbook(new Uint8Array(arrayBuffer));

                // Get the first (default) worksheet
                const worksheet = workbook.worksheets.get(0);

                // Create a range A1:A7 (original code created A1:B7 but used A1 to A7 in parameters)
                const range = worksheet.cells.createRange("A1", "A7");

                // Get Hyperlinks in range
                const hyperlinks = range.hyperlinks;

                let outputHtml = '<p>Hyperlinks found:</p><ul>';
                if (typeof hyperlinks.forEach === 'function') {
                    hyperlinks.forEach(link => {
                        outputHtml += `<li>${link.textToDisplay}: ${link.linkType}</li>`;
                    });
                } else {
                    for (let i = 0; i < hyperlinks.count; i++) {
                        const link = hyperlinks.get(i);
                        outputHtml += `<li>${link.textToDisplay}: ${link.linkType}</li>`;
                    }
                }
                outputHtml += '</ul>';

                resultDiv.innerHTML = outputHtml;
            });
        });
    </script>
</html>
```


الناتج التالي الذي تم إنشاؤه بواسطة مقتطف الكود أعلاه.

### إخراج الكونسول
