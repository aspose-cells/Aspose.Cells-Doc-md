---
title: التحقق من كلمة المرور المستخدمة لحماية ورقة العمل باستخدام جافا سكريبت عبر C++
linktitle: التحقق من الكلمة المستخدمة لحماية ورقة العمل
type: docs
weight: 370
url: /ar/javascript-cpp/verify-password-used-to-protect-the-worksheet/
description: تعلم كيفية التحقق من كلمة المرور المستخدمة لحماية ورقة العمل باستخدام Aspose.Cells for JavaScript عبر C++.
---

{{% alert color="primary" %}}

قامت واجهات برمجة تطبيقات Aspose.Cells بتحسين فئة [**Protection**](https://reference.aspose.com/cells/javascript-cpp/protection) من خلال تقديم بعض الخصائص والطرق المفيدة. أحد هذه الطرق هو [**Protection.verifyPassword(string)**](https://reference.aspose.com/cells/javascript-cpp/protection/#verifyPassword-string-) الذي يسمح بتحديد كلمة مرور كمثال على *السلسلة* ويقوم بالتحقق مما إذا تم استخدام نفس كلمة المرور لحماية [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet).

{{% /alert %}}

ترجع طريقة [**Protection.verifyPassword(string)**](https://reference.aspose.com/cells/javascript-cpp/protection/#verifyPassword-string-) **true** إذا كانت كلمة المرور المحددة تتطابق مع كلمة المرور المستخدمة لحماية ورقة العمل المعطاة، وتُرجع **false** إذا لم تتطابق. يستخدم الكود التالي طريقة [**Protection.verifyPassword(string)**](https://reference.aspose.com/cells/javascript-cpp/protection/#verifyPassword-string-) مع الخاصية [**Protection.isProtectedWithPassword()**](https://reference.aspose.com/cells/javascript-cpp/protection/#isProtectedWithPassword--) لاكتشاف حماية بكلمة مرور والتحقق من كلمة المرور.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Check Worksheet Password Protection</h1>
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

            // Instantiate Workbook with file bytes
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet in the Excel file
            const sheet = workbook.worksheets.get(0);

            // Check if Worksheet is password protected
            if (sheet.protection.isProtectedWithPassword()) {
                // Verify the password used to protect the Worksheet
                if (sheet.protection.verifyPassword("1234")) {
                    resultDiv.innerHTML = '<p style="color: green;">Specified password has matched</p>';
                } else {
                    resultDiv.innerHTML = '<p style="color: red;">Specified password has not matched</p>';
                }
            } else {
                resultDiv.innerHTML = '<p style="color: blue;">Worksheet is not password protected</p>';
            }
        });
    </script>
</html>
```
