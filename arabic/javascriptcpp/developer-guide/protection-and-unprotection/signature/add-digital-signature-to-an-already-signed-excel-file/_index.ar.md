---
title: إضافة توقيع رقمي إلى ملف إكسل موقّع بالفعل باستخدام جافا سكريبت عبر C++
linktitle: إضافة توقيع رقمي إلى ملف إكسل تم توقيعه بالفعل
type: docs
weight: 20
url: /ar/javascript-cpp/add-digital-signature-to-an-already-signed-excel-file/
description: يصف هذا المقال كيفية إضافة توقيع رقمي إلى ملف إكسل موقّع بالفعل باستخدام جافا سكريبت مع Aspose.Cells for JavaScript عبر C++.
keywords: إضافة توقيع رقمي إلى ملف إكسل موقّع بالفعل، كيفية إضافة توقيع رقمي إلى مستند إكسل موقّع باستخدام جافا سكريبت عبر C++.
---

## **سيناريوهات الاستخدام المحتملة**

 يوفر Aspose.Cells for JavaScript عبر C++ طريقة [**Workbook.addDigitalSignature(digitalSignatureCollection)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#addDigitalSignature-digitalSignatureCollection-) التي يمكنك استخدامها لإضافة توقيع رقمي إلى ملف إكسل موقّع بالفعل.

{{% alert color="primary" %}}

يرجى ملاحظة أنه عند إضافة توقيع رقمي إلى مستند Excel موقّع بالفعل، إذا كان المستند الأصلي مستندًا تم إنشاؤه بواسطة Aspose.Cells، فإنه يعمل بشكل جيد. لكن إذا تم إنشاؤه بواسطة محركات أخرى (مثل Microsoft Excel، إلخ)، فإن Aspose.Cells لا يمكنه الاحتفاظ بنفس الملف بعد التحميل وإعادة الحفظ، مما يجعل التوقيع الأصلي غير صالح.

{{% /alert %}}

## **كيفية إضافة توقيع رقمي إلى ملف Excel تم توقيعه مسبقًا**

يعرض رمز النموذج التالي كيفية استخدام أسلوب [**Workbook.addDigitalSignature(digitalSignatureCollection)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#addDigitalSignature-digitalSignatureCollection-) لإضافة توقيع رقمي إلى ملف Excel موقّع مسبقًا. يرجى التحقق من [ملف Excel النموذجي](50528280.xlsx) المستخدم في هذا الكود. هذا الملف موقع رقميًا مسبقًا. يرجى التحقق من [ملف Excel الناتج](50528281.xlsx) الذي تم إنشاؤه بواسطة الكود. لقد استخدمنا شهادة عرضية باسم [AsposeDemo.pfx](50528279.pfx) بكلمة مرور **aspose** في هذا الكود، وتظهر لقطة الشاشة تأثير رمز النموذج على ملف Excel النموذجي بعد التنفيذ.

![todo:image_alt_text](add-digital-signature-to-an-already-signed-excel-file_1.png)

## **الكود المثالي**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Add Digital Signature Example</title>
    </head>
    <body>
        <h1>Add Digital Signature to Workbook</h1>
        <p>Select an Excel file and a PFX certificate, enter the certificate password, then click "Add Digital Signature".</p>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
        <br/><br/>
        <input type="file" id="certInput" accept=".pfx" />
        <br/><br/>
        <label for="certPassword">Certificate Password:</label>
        <input type="password" id="certPassword" value="aspose" />
        <br/><br/>
        <button id="runExample">Add Digital Signature</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, DigitalSignature, DigitalSignatureCollection, SaveFormat, Utils } = AsposeCells;

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
            const certInput = document.getElementById('certInput');
            const passwordInput = document.getElementById('certPassword');
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }
            if (!certInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select a .pfx certificate file.</p>';
                return;
            }

            // Read files as ArrayBuffer
            const excelFile = fileInput.files[0];
            const certFile = certInput.files[0];
            const certPassword = passwordInput.value;

            const excelArrayBuffer = await excelFile.arrayBuffer();
            const certArrayBuffer = await certFile.arrayBuffer();

            // Instantiate Workbook from uploaded Excel file
            const workbook = new Workbook(new Uint8Array(excelArrayBuffer));

            // Create the digital signature collection
            const dsCollection = new DigitalSignatureCollection();

            // Create new digital signature and add it in digital signature collection
            // Using certificate bytes (Uint8Array), password, comment and signing date
            const signature = new DigitalSignature(new Uint8Array(certArrayBuffer), certPassword, "Aspose.Cells added new digital signature in existing digitally signed workbook.", new Date());
            dsCollection.add(signature);

            // Add digital signature collection inside the workbook
            workbook.addDigitalSignature(dsCollection);

            // Save the workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputDigitallySignedByCells.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Digitally Signed Excel File';

            // Dispose the workbook
            workbook.dispose();

            resultDiv.innerHTML = '<p style="color: green;">Digital signature added successfully! Click the download link to get the signed file.</p>';
        });
    </script>
</html>
```
