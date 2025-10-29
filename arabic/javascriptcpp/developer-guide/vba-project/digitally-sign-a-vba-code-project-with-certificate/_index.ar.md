---
title: توقيع مشروع رمز VBA رقميًا باستخدام شهادة باستخدام JavaScript عبر C++
linktitle: التوقيع الرقمي لمشروع كود VBA بشهادة
type: docs
weight: 110
url: /ar/javascript-cpp/digitally-sign-a-vba-code-project-with-certificate/
description: تعلم كيفية توقيع مشروع رمز VBA رقميًا باستخدام شهادة باستخدام Aspose.Cells for JavaScript عبر C++.
---

{{% alert color="primary" %}}

يمكنك توقيع مشروع كود VBA رقميًا باستخدام Aspose.Cells مع طريقتها [**VbaProject.sign(DigitalSignature)**](https://reference.aspose.com/cells/javascript-cpp/vbaproject/#sign-digitalsignature-). يرجى اتباع هذه الخطوات للتحقق مما إذا كان ملف إكسل الخاص بك موقعًا رقمياً بشهادة.

- انقر فوق **Basic Visual** من علامة التبويب **المطور** لفتح **البيئة المتقدمة لتطبيقات Basic Visual**
- انقر فوق **أدوات** > **التوقيعات الرقمية...** من **بيئة Visual Basic للتطبيقات**

وسيظهر النموذج التوقيع **الرقمي** يظهر إذا كان المستند موقعًا رقميًا بشهادة أم لا.

{{% /alert %}} 

## **توقيع مشروع رمز VBA رقميًا باستخدام الشهادة في JavaScript**

 يوضح رمز العينة التالي كيفية استخدام [**VbaProject.sign(DigitalSignature)**](https://reference.aspose.com/cells/javascript-cpp/vbaproject/#sign-digitalsignature-) الطريقتين. إليك ملفات الإدخال والإخراج للرمز التجريبي. يمكنك استخدام أي ملف Excel وأي شهادة لاختبار هذا الرمز.

- [ملف Excel المصدر](5115028.xlsm) المستخدم في الكود العيني.
- [ملف pfx العيني](5115039.pfx) لإنشاء توقيع رقمي. يرجى تثبيته على جهاز الكمبيوتر الخاص بك لتشغيل هذا الكود. كلمة المرور الخاصة به هي 1234.
- [ملف Excel الناتج](5115029.xlsm) الذي تم إنشاؤه بواسطة الكود العيني.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Sign VBA Project with Digital Signature</h1>
        <div>
            <label for="fileInput">Select Excel Workbook (.xlsm): </label>
            <input type="file" id="fileInput" accept=".xlsm,.xls,.xlsx" />
        </div>
        <div>
            <label for="pfxInput">Select PFX Certificate (.pfx): </label>
            <input type="file" id="pfxInput" accept=".pfx" />
        </div>
        <button id="runExample">Sign VBA Project</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, DigitalSignature } = AsposeCells;

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
            const pfxInput = document.getElementById('pfxInput');
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length || !pfxInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select both the Excel workbook and the PFX certificate files.</p>';
                return;
            }

            const workbookFile = fileInput.files[0];
            const pfxFile = pfxInput.files[0];

            // Read files as ArrayBuffer
            const [wbArrayBuffer, pfxArrayBuffer] = await Promise.all([
                workbookFile.arrayBuffer(),
                pfxFile.arrayBuffer()
            ]);

            // Prepare bytes
            const wbBytes = new Uint8Array(wbArrayBuffer);
            const pfxBytes = new Uint8Array(pfxArrayBuffer);

            // Set Digital Signature parameters
            const password = "1234";
            const comment = "Signing Digital Signature using Aspose.Cells";
            const digitalSignature = new DigitalSignature(pfxBytes, password, comment, new Date());

            // Create workbook object from excel file
            const workbook = new Workbook(wbBytes);

            // Sign VBA Code Project with Digital Signature
            workbook.vbaProject.sign(digitalSignature);

            // Save the workbook as XLSM
            const outputData = workbook.save(SaveFormat.Xlsm);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputDigitallySignVbaProjectWithCertificate.xlsm';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Signed Workbook';

            resultDiv.innerHTML = '<p style="color: green;">Workbook signed successfully! Click the download link to download the signed workbook.</p>';
        });
    </script>
</html>
```
