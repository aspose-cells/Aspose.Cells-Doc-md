---
title: التحقق من كلمة مرور الملفات المشفرة باستخدام جافا سكريبت عبر C++
linktitle: التحقق من كلمة مرور الملفات المشفرة
type: docs
weight: 10
url: /ar/javascript-cpp/verify-password-of-encrypted-excel-and-ods-files/
description: التحقق من كلمة مرور ملفات إكسل المشفرة (xlsx، xlsb، xls، xlsm) وملفات أوبن أوفيس (ODS) باستخدام Aspose.Cells for JavaScript عبر C++.
---

{{% alert color="primary" %}}  
إذا كانت ملفات Excel (xlsx، xlsb، xls، xlsm) وOpen Office (ODS) مقفلة بكلمة مرور، يدعم Aspose التحقق البسيط من كلمة المرور دون تحليل بيانات محددة من الملفات.  
{{% /alert %}}  

## **تحقق من كلمة المرور للملف المُشفر**  

للتحقق من كلمة مرور الملف المشفر، توفر Aspose.Cells for JavaScript عبر C++ طريقة [**FileFormatUtil.verifyPassword(Uint8Array, string)**](https://reference.aspose.com/cells/javascript-cpp/fileformatutil/#verifyPassword-uint8array-string-). تقبل هذه الطريقة معلمتين، تدفق الملف وكلمة المرور التي يجب التحقق منها.  
يوضح مقتطف الشيفرة التالي استخدام الطريقة [**FileFormatUtil.verifyPassword(Uint8Array, string)**](https://reference.aspose.com/cells/javascript-cpp/fileformatutil/#verifyPassword-uint8array-string-) للتحقق مما إذا كانت كلمة المرور المقدمة صالحة أم لا.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Verify Excel Password Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Verify Password</button>
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
        });

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();
            const bytes = new Uint8Array(arrayBuffer);

            const isPasswordValid = FileFormatUtil.verifyPassword(bytes, "1234");

            document.getElementById('result').innerHTML = '<p>Password is Valid: ' + isPasswordValid + '</p>';
        });
    </script>
</html>
```
