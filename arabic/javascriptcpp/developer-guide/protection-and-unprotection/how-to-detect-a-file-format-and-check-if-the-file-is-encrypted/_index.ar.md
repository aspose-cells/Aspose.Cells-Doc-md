---
title: كيفية اكتشاف تنسيق ملف والتحقق مما إذا كان الملف مشفرًا باستخدام JavaScript عبر C++
linktitle: كيفية اكتشاف تنسيق الملف والتحقق مما إذا كان الملف مشفرًا
type: docs
weight: 2700
url: /ar/javascript-cpp/how-to-detect-a-file-format-and-check-if-the-file-is-encrypted/
description: تعلم كيفية اكتشاف تنسيق ملف والتحقق مما إذا كان الملف مشفرًا باستخدام Aspose.Cells for JavaScript عبر C++.
---

{{% alert color="primary" %}}  
أحيانًا تحتاج إلى اكتشاف تنسيق الملف قبل فتحه لأن ملحق الملف لا يضمن أن محتوى الملف مناسب. قد يكون الملف مشفرًا (ملف محمي بكلمة مرور) لذا لا يمكن قراءته مباشرة، أو يجب ألا نقرأه. يوفر Aspose.Cells for JavaScript عبر C++ الطريقة [**FileFormatUtil.detectFileFormat(Uint8Array)**](https://reference.aspose.com/cells/javascript-cpp/fileformatutil/#detectFileFormat-uint8array-) الثابتة وبعض واجهات برمجة التطبيقات ذات الصلة التي يمكنك استخدامها لمعالجة المستندات.  
{{% /alert %}}  

الرمز البريدي العيني التالي يوضح كيفية اكتشاف تنسيق الملف (باستخدام مسار الملف) والتحقق من امتداده. يمكنك أيضًا تحديد ما إذا كان الملف مشفرًا.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells File Format Detection Example</h1>
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

            // Detect file format
            const info = AsposeCells.FileFormatUtil.detectFileFormat(new Uint8Array(arrayBuffer));

            // Gets the detected load format (converted getter -> property)
            const extension = AsposeCells.FileFormatUtil.loadFormatToExtension(info.loadFormat);
            const encrypted = info.isEncrypted;

            console.log("The spreadsheet format is: " + extension);
            console.log("The file is encrypted: " + encrypted);

            resultDiv.innerHTML = `<p>The spreadsheet format is: <strong>${extension}</strong></p>
                                   <p>The file is encrypted: <strong>${encrypted}</strong></p>`;
        });
    </script>
</html>
```
