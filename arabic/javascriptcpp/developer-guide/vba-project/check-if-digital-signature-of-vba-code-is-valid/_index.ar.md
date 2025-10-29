---
title: التحقق مما إذا كانت التوقيع الرقمي لرمز VBA صالحًا باستخدام جافا سكريبت عبر C++
linktitle: تحقق ما إذا كان التوقيع الرقمي لشيفر آلي VBA صالحًا
type: docs
weight: 120
url: /ar/javascript-cpp/check-if-digital-signature-of-vba-code-is-valid/
description: تعلم كيفية التحقق من صحة التوقيع الرقمي لرمز VBA باستخدام Aspose.Cells for JavaScript عبر C++.
--- 

{{% alert color="primary" %}}

تسمح Aspose.Cells لك بالتحقق مما إذا كان التوقيع الرقمي لشيفر آلي VBA صالحًا باستخدام الخاصية [**Workbook.isValidSigned()**](https://reference.aspose.com/cells/javascript-cpp/vbaproject/#isValidSigned--). سيعيد **true** إذا كان التوقيع صالحًا وإلا سيعيد **false**. يصبح التوقيع الرقمي لشيفر آلي VBA غير صالح عند تغيير شيفر آلي VBA.

{{% /alert %}}

## ** التحقق مما إذا كانت التوقيع الرقمي لرمز VBA صالحًا في جافا سكريبت**

الكود التالي يوضح استخدام هذه الخاصية باستخدام [ملف الإكسل العيني](5115030.xlsm) الذي يمكنك تنزيله من الرابط المُقدم. يحتوي نفس ملف Excel على توقيع صالح ولكن عند تعديل شيفر آلي VBA وحفظ سجل العمل ثم إعادة التحقق ، نجد أن توقيعه أصبح غير صالح.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells VBA Signature Example</title>
    </head>
    <body>
        <h1>VBA Signature Example</h1>
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
            const resultEl = document.getElementById('result');
            if (!fileInput.files.length) {
                resultEl.innerHTML = '<p style="color: red;">Please select an Excel file (preferably .xlsm).</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Loads the workbook which contains the VBA project
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Signature status before modification
            const isSignedBefore = workbook.vbaProject.isValidSigned();
            console.log("Is VBA Code Project Valid Signed: " + isSignedBefore);

            // Modify the VBA Code, save the workbook then reload
            // VBA Code Signature will now be invalid
            let code = workbook.vbaProject.modules.get(1).codes;
            code = code.replace("Welcome to Aspose", "Welcome to Aspose.Cells");
            workbook.vbaProject.modules.get(1).codes = code;

            // Save the modified workbook to a downloadable blob
            const outputData = workbook.save(SaveFormat.Xlsm);
            const blob = new Blob([outputData], { type: 'application/vnd.ms-excel.sheet.macroEnabled.12' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsm';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            // Reload from the saved output data to verify signature status
            const reloadedWorkbook = new Workbook(new Uint8Array(outputData));
            const isSignedAfter = reloadedWorkbook.vbaProject.isValidSigned();
            console.log("Is VBA Code Project Valid Signed: " + isSignedAfter);

            // Update result UI
            resultEl.innerHTML = `
                <p style="color: green;">Operation completed successfully!</p>
                <p>Signature valid before modification: <strong>${isSignedBefore}</strong></p>
                <p>Signature valid after modification: <strong>${isSignedAfter}</strong></p>
                <p>Click the download link to get the modified file.</p>
            `;
        });
    </script>
</html>
```
