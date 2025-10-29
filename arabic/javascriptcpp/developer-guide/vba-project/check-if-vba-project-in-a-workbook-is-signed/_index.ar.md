---
title: التحقق مما إذا كان مشروع VBA في دفتر العمل موقّعًا باستخدام JavaScript عبر C++
linktitle: التحقق مما إذا كان مشروع VBA في كتاب عمل موقع بالتوقيع
type: docs
weight: 70
url: /ar/javascript-cpp/check-if-vba-project-in-a-workbook-is-signed/
description: تعلم كيفية التحقق مما إذا كان مشروع VBA في ملف إكسل موقّعًا باستخدام Aspose.Cells for JavaScript عبر C++.
---

{{% alert color="primary" %}}

يمكنك التحقق مما إذا كان مشروع VBA الخاص بك موقع بالتوقيع أم لا باستخدام Microsoft Excel عبر أمر القائمة **Tools > Digital Signatures...**. على نفس النحو، يمكنك التحقق منه برمجيًا باستخدام خاصية Aspose.Cells [**Workbook.vbaProject**](https://reference.aspose.com/cells/javascript-cpp/workbook/#vbaProject--).

{{% /alert %}}

## **التحقق مما إذا كان مشروع VBA في دفتر عمل موقّعًا باستخدام JavaScript**

يحمّل الكود التالي دفتر العمل ويفحص ما إذا كان مشروع VBA الخاص به موقعًا باستخدام الخاصية [**Workbook.vbaProject**](https://reference.aspose.com/cells/javascript-cpp/workbook/#vbaProject--). ستُرجع الخاصية **true** إذا كان المشروع موقعًا، وإلا ستُرجع **false**.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells VBA Signed Check</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.xlsm" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Utils } = AsposeCells;

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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the VBA project and checking if it's signed
            const isSigned = workbook.vbaProject.isSigned;

            console.log("VBA Project is Signed: " + isSigned);
            document.getElementById('result').innerHTML = `<p>VBA Project is Signed: ${isSigned}</p>`;
        });
    </script>
</html>
```
