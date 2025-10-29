---
title: إضافة خط توقيع إلى ورقة العمل باستخدام جافا سكريبت عبر C++
linktitle: إضافة خط التوقيع إلى ورقة العمل
type: docs
weight: 200
url: /ar/javascript-cpp/add-signature-line/
description: يصف هذا المقال كيفية إضافة خط توقيع إلى ورقة العمل باستخدام كود جافا سكريبت مع Aspose.Cells for JavaScript عبر C++.
keywords: إضافة خط توقيع إلى ورقة العمل جافا سكريبت عبر C++، كيفية إضافة خط توقيع إلى ورقة العمل جافا سكريبت عبر C++، كيفية إضافة خط التوقيع إلى ورقة العمل جافا سكريبت عبر C++.
---

## **مقدمة**

تقدم Aspose.Cells خاصية [**Picture.signatureLine**](https://reference.aspose.com/cells/javascript-cpp/picture/#signatureLine--) لإضافة خط التوقيع في ورقة العمل.

## **كيفية إضافة خط توقيع إلى الورقة**

يعرض رمز النموذج التالي كيفية استخدام خاصية [**Picture.signatureLine**](https://reference.aspose.com/cells/javascript-cpp/picture/#signatureLine--) لإضافة سطر توقيع لورقة العمل. تظهر لقطة الشاشة تأثير رمز النموذج على ملف Excel بعد التنفيذ.

![todo:image_alt_text](add-signature-line.png)

## **الكود المثالي**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Signature Line</title>
    </head>
    <body>
        <h1>Signature Line Example</h1>
        <p>Optional: select an existing Excel file to add the signature line to. Otherwise a new workbook will be created.</p>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <p>Select a PFX certificate file (required):</p>
        <input type="file" id="certInput" accept=".pfx" />
        <br/><br/>
        <button id="runExample">Add Signature Line and Sign Workbook</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Utils, SignatureLine, DigitalSignature, DigitalSignatureCollection } = AsposeCells;

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
            const resultDiv = document.getElementById('result');

            if (!certInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select a PFX certificate file.</p>';
                return;
            }

            const certFile = certInput.files[0];
            const certArrayBuffer = await certFile.arrayBuffer();
            const certBytes = new Uint8Array(certArrayBuffer);

            // Instantiate or load workbook
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Create and configure signature line
            const signatureLine = new SignatureLine();
            signatureLine.signer = "Aspose.Cells";
            signatureLine.title = "signed by Aspose.Cells";

            // Access first worksheet and add signature line
            const worksheet = workbook.worksheets.get(0);
            worksheet.shapes.addSignatureLine(1, 1, signatureLine);

            // Create digital signature from certificate bytes
            const signature = new DigitalSignature(certBytes, "aspose", "test Microsoft Office signature line", new Date());

            // Add signature to collection and assign to workbook
            const dsCollection = new DigitalSignatureCollection();
            dsCollection.add(signature);
            workbook.digitalSignature = dsCollection;

            // Save the workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'signatureLine.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Signed Workbook';

            resultDiv.innerHTML = '<p style="color: green;">Signature line added and workbook signed. Click the download link to get the file.</p>';
        });
    </script>
</html>
```
