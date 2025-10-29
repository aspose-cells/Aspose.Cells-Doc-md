---
title: تشفير وفك تشفير ملفات ODS باستخدام جافا سكريبت عبر C++
linktitle: تشفير وفك تشفير ملفات ODS
type: docs
weight: 10
url: /ar/javascript-cpp/encrypt-and-decrypt-ods-files/
description: حماية كلمة المرور وتشفير ملفات ODS باستخدام Aspose.Cells for JavaScript عبر C++. 
---

{{% alert color="primary" %}}
يدعم OpenOffice.org مجموعة مكتملة من الميزات، ويتيح حماية بكلمة مرور وتشفير الملفات. ومع ذلك، يمكن فتح ملف ODS المشفر فقط بواسطة OpenOffice بعد إدخال كلمة المرور. لا يمكن لـ Excel فتح ملف ODS المشفر، وقد يعرض رسائل تحذيرية. خيارات التشفير غير قابلة للتطبيق على ملفات ODS، على عكس أنواع الملفات الأخرى. 
يسمح Aspose.Cells لك بتشفير وفك تشفير ملفات ODS. يمكن فتح ملفات ODS المفككة في كل من Excel وOpenOffice.
{{% /alert %}}

## **التشفير باستخدام OpenOffice Calc**
1. اختر **حفظ باسم** وانقر على مربع **الحفظ بكلمة مرور**.
1. انقر على زر **حفظ**.
1. اكتب كلمة المرور المطلوبة في حقلي **أدخل كلمة المرور للفتح** و **تأكيد كلمة المرور** في نافذة تعيين كلمة المرور التي تفتح. 
1. انقر على زر **موافق** لحفظ الملف.

## **تشفير ملف ODS باستخدام Aspose.Cells for JavaScript عبر C++**
لتشفير ملف ODS، قم بتحميل الملف واضبط قيمة [**WorkbookSettings.password**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#password--) على كلمة المرور الفعلية قبل الحفظ. يمكن فتح ملف ODS المشفر الناتج في OpenOffice فقط.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Protect ODS File</title>
    </head>
    <body>
        <h1>Protect ODS File Example</h1>
        <input type="file" id="fileInput" accept=".ods" />
        <button id="runExample">Protect and Download ODS</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;

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
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an ODS file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by opening the uploaded ODS file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Password protect the file (converted from getSettings().setPassword -> settings.password)
            workbook.settings.password = "1234";

            // Saving the ODS file
            const outputData = workbook.save(SaveFormat.Ods);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputEncryptedODSFile.ods';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Encrypted ODS File';

            document.getElementById('result').innerHTML = '<p style="color: green;">File protected successfully! Click the download link to get the encrypted file.</p>';
        });
    </script>
</html>
```

## **فك تشفير ملف ODS باستخدام Aspose.Cells for JavaScript عبر C++**
لفك تشفير ملف ODS، قم بتحميل الملف من خلال إدخال كلمة المرور في [**LoadOptions.password**](https://reference.aspose.com/cells/javascript-cpp/loadoptions/#password--). بمجرد تحميل الملف، اضبط سلسلة [**WorkbookSettings.password**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#password--) على null.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Decrypt ODS Example</title>
    </head>
    <body>
        <h1>Decrypt ODS Example</h1>
        <input type="file" id="fileInput" accept=".ods" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, LoadOptions, LoadFormat, Utils } = AsposeCells;

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
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an ODS file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Open an encrypted ODS file with load options
            const loadOptions = new LoadOptions(LoadFormat.Ods);

            // Set original password
            loadOptions.password = "1234";

            // Load the encrypted ODS file with the appropriate load options
            const workbook = new Workbook(new Uint8Array(arrayBuffer), loadOptions);

            // Set the password to null (remove password from settings)
            workbook.settings.password = null;

            // Save the decrypted ODS file and provide download link
            const outputData = workbook.save(SaveFormat.Ods);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputDecryptedODSFile.ods';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Decrypted ODS File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Decryption completed successfully! Click the download link to get the decrypted file.</p>';
        });
    </script>
</html>
```
