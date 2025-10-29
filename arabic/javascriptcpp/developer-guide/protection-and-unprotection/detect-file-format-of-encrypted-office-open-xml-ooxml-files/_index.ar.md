---
title: اكتشاف تنسيق ملف Office Open XML المشفر  ملفات OOXML باستخدام JavaScript عبر C++
linktitle: الكشف عن تنسيق الملف لملفات Office Open XML المُشفرة
type: docs
weight: 340
url: /ar/javascript-cpp/detect-file-format-of-encrypted-office-open-xml-ooxml-files/
description: تعلم كيفية اكتشاف تنسيق ملف ملفات OOXML المشفرة باستخدام Aspose.Cells for JavaScript عبر C++.
---

{{% alert color="primary" %}}  

**Office Open XML** (المعروف أيضًا باسم **OOXML** أو **Microsoft Open XML** (MOX)) هو تنسيق ملف قائم على XML تم تطويره بواسطة Microsoft لتمثيل مستندات المكتب مثل جداول البيانات، المخططات، العروض التقديمية، ومستندات المعالجة النصية.  

{{% /alert %}}  

تقدم Aspose.Cells طريقة لاكتشاف تنسيق ملف ملفات Microsoft Open XML المشفرة. لتحديد نوع الملف، استخدم دالة [FileFormatUtil.detectFileFormat(Uint8Array)](https://reference.aspose.com/cells/javascript-cpp/fileformatutil/#detectFileFormat-uint8array-) كما هو موضح في المثال أدناه.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells FileFormat Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, FileFormatUtil, Utils } = AsposeCells;

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
                // Create a small byte stream equivalent to the original JavaScript Buffer
                const stream = new Uint8Array([0x50, 0x4B, 0x03, 0x04]);

                // Verify password (will propagate errors if any)
                FileFormatUtil.verifyPassword(stream, "1234");

                // Detect file format
                const fileFormatInfo = FileFormatUtil.detectFileFormat(stream);

                // Use property access per universal getter/setter conversion
                document.getElementById('result').innerHTML = '<p>File Format: ' + fileFormatInfo.fileFormatType + '</p>';
                console.log("File Format: " + fileFormatInfo.fileFormatType);
            });
        });
    </script>
</html>
```
