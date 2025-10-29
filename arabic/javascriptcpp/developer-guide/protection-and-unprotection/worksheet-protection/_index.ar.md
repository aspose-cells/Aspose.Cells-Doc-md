---
title: حماية وإلغاء حماية ورقة العمل باستخدام JavaScript عبر C++
linktitle: حماية وإلغاء الحماية لورق العمل
type: docs
weight: 40
url: /ar/javascript-cpp/protect-and-unprotect-worksheets/
description: حماية وإلغاء حماية ورقة العمل لملفات Excel باستخدام Aspose.Cells for JavaScript عبر C++.
---

{{% alert color="primary" %}}  
لمنع مستخدمين آخرين من تغيير البيانات في ورقة العمل عن طريق الخطأ أو بشكل متعمد، يمكنك قفل الخلايا في ورقة العمل الخاصة بك ثم حماية الورقة بكلمة مرور.  
{{% /alert %}}  

## **حماية وإلغاء حماية ورقة العمل في MS Excel**  

**![حماية وإلغاء حماية ورقة العمل](protect-and-unprotect-worksheet.png)**  

١. انقر فوق **مراجعة > حماية ورقة عمل**.  
١. أدخل كلمة مرور في **مربع الكلمة السرية**.  
١. حدد خيارات **السماح**.  
١. حدد **موافق**, أدخل كلمة المرور مرة أخرى لتأكيدها، ثم حدد **موافق** مجددًا.  

## **حماية ورقة العمل باستخدام Aspose.Cells for JavaScript عبر C++**  
متطلبات الترميز البسيطة التالية فقط لتنفيذ حماية هيكل دفتر العمل لملفات Excel.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Protect Worksheet Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ProtectionType } = AsposeCells;

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
            // Create a new file (workbook)
            const workbook = new Workbook();

            // Gets the first worksheet.
            const sheet = workbook.worksheets.get(0);

            // Protect contents of the worksheet.
            sheet.protect(ProtectionType.Contents);

            // Protect worksheet with password.
            sheet.protection.password = "test";

            // Save as Excel file and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Book1.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Worksheet protected and file is ready. Click the download link to get the file.</p>';
        });
    </script>
</html>
```  

## **إلغاء حماية ورقة العمل باستخدام Aspose.Cells for JavaScript عبر C++**  
سهولة إلغاء حماية ورقة العمل باستخدام API Aspose.Cells. إذا كانت ورقة العمل محمية بكلمة مرور، يتطلب الأمر كلمة مرور صحيحة.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Unprotect Worksheet Example</title>
    </head>
    <body>
        <h1>Unprotect Worksheet Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Unprotect Worksheet</button>
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

            // Instantiate Workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet
            const sheet = workbook.worksheets.get(0);

            // Unprotect contents of the worksheet using password
            sheet.unprotect("password");

            // Save the modified workbook to XLSX format and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Book1.unprotected.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Unprotected Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Worksheet unprotected successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

## **مواضيع متقدمة**  
- [إعدادات الحماية المتقدمة منذ Excel XP](/cells/ar/javascript-cpp/advanced-protection-settings-since-excel-xp/)  
- [الكشف عما إذا كانت ورقة العمل محمية بكلمة مرور](/cells/ar/javascript-cpp/detect-if-worksheet-is-password-protected/)  
- [حماية ورق العمل](/cells/ar/javascript-cpp/protecting-worksheets/)  
- [إلغاء حماية ورقة العمل](/cells/ar/javascript-cpp/unprotect-a-worksheet/)  
- [التحقق من الكلمة المستخدمة لحماية ورقة العمل](/cells/ar/javascript-cpp/verify-password-used-to-protect-the-worksheet/)
