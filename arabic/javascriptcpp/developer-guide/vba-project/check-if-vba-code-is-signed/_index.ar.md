---
title: التحقق مما إذا كان رمز VBA موقعًا باستخدام جافا سكريبت عبر C++
linktitle: التحقق مما إذا كان كود VBA موقع بالتوقيع
type: docs
weight: 100
url: /ar/javascript-cpp/check-if-vba-code-is-signed/
description: تعرف على كيفية التحقق مما إذا كان مشروع رمز VBA موقّعًا باستخدام Aspose.Cells for JavaScript عبر C++. 
---

{{% alert color="primary" %}}

يتيح Aspose.Cells للمستخدم التحقق مما إذا كان مشروع كود VBA موقع بالتوقيع أم لا. يرجى استخدام خاصية [**VbaProject.isSigned()**](https://reference.aspose.com/cells/javascript-cpp/vbaproject/#isSigned--) للتحقق مما إذا كان مشروع كود VBA موقع بالتوقيع أم لا.

{{% /alert %}}

 يوضح الرمز التالي كيفية التحقق مما إذا كان رمز VBA موقعًا أم لا باستخدام خاصية [**VbaProject.isSigned()**](https://reference.aspose.com/cells/javascript-cpp/vbaproject/#isSigned--). يمكنك استخدام أي من ملفات Excel الخاصة بك لاختبار هذا الرمز. للاختبار، يمكنك استخدام [ملف Excel هذا المستخدم في الكود](5115032.xlsm).

## **التحقق مما إذا كان رمز VBA موقّعًا باستخدام JavaScript**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells VBA Signed Check Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.xlsm,.csv" />
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
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the VBA project and checking if it's signed
            const vbaProject = workbook.vbaProject;
            const isSigned = vbaProject.isSigned();

            resultDiv.innerHTML = `<p>Is VBA Code Project Signed: ${isSigned}</p>`;
        });
    </script>
</html>
```

## مخرج الكونسول

أدناه مخرج الكونسول للكود أعلاه باستخدام [ملف Excel عينة](5115032.xlsm) المقدم من خلال الرابط.

{{< highlight java >}}

Is VBA Code Project Signed: True

{{< /highlight >}}
