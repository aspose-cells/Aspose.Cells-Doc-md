---
title: الكشف عما إذا كانت ورقة العمل محمية بكلمة مرور باستخدام جافا سكريبت عبر C++
linktitle: الكشف عما إذا كانت ورقة العمل محمية بكلمة مرور
type: docs
weight: 360
url: /ar/javascript-cpp/detect-if-worksheet-is-password-protected/
description: تعلم كيفية اكتشاف ما إذا كانت ورقة العمل محمية بكلمة مرور باستخدام Aspose.Cells for JavaScript عبر C++. 
keywords: اكتشاف حماية كلمة مرور ورقة العمل جافا سكريبت عبر C++، التحقق مما إذا كانت ورقة العمل محمية بكلمة مرور جافا سكريبت عبر C++، Aspose.Cells for JavaScript عبر C++
---

{{% alert color="primary" %}}

من الممكن حماية دفاتر العمل وأوراق العمل بشكل منفصل. على سبيل المثال، قد يحتوي جدول البيانات على ورقة عمل واحدة أو أكثر محمية بكلمة مرور، ومع ذلك، قد يكون جدول البيانات نفسه محميًا أو غير محمي. توفر واجهات برمجة تطبيقات Aspose.Cells الوسائل للكشف عما إذا كانت ورقة العمل معينة محمية بكلمة مرور أم لا. يوضح هذا المقال استخدام Aspose.Cells for JavaScript عبر واجهة برمجة تطبيقات C++ لتحقيق ذلك.

{{% /alert %}}

كشف Aspose.Cells for JavaScript عبر C++ عن خاصية [**Protection.isProtectedWithPassword()**](https://reference.aspose.com/cells/javascript-cpp/protection/#isProtectedWithPassword--) للكشف عما إذا كانت ورقة العمل محمية بكلمة مرور أم لا. تُعيد الخاصية من نوع بولياني [**Protection.isProtectedWithPassword()**](https://reference.aspose.com/cells/javascript-cpp/protection/#isProtectedWithPassword--) القيمة **true** إذا كانت [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) محمية بكلمة مرور وتُعيد **false** إذا لم تكن كذلك.

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

            // Create an instance of Workbook and load a spreadsheet
            const book = new Workbook(new Uint8Array(arrayBuffer));

            // Access the protected Worksheet
            const sheet = book.worksheets.get(0);

            // Check if Worksheet is password protected
            if (sheet.protection.isProtectedWithPassword()) {
                resultDiv.innerHTML = '<p>Worksheet is password protected</p>';
                console.log("Worksheet is password protected");
            } else {
                resultDiv.innerHTML = '<p>Worksheet is not password protected</p>';
                console.log("Worksheet is not password protected");
            }
        });
    </script>
</html>
```
