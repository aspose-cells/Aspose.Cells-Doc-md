---
title: حماية وإلغاء حماية بنية المصنف باستخدام JavaScript عبر C++
linktitle: حماية وإلغاء حماية هيكل دفتر العمل
type: docs
weight: 40
url: /ar/javascript-cpp/protect-and-unprotect-workbook-structure/
description: حماية وإلغاء حماية بنية المصنف لملفات Excel باستخدام JavaScript عبر C++.
---


{{% alert color="primary" %}}  
لمنع المستخدمين الآخرين من عرض أوراق عمل مخفية، أو إضافتها، أو نقلها، أو حذفها، أو إخفاءها، أو إعادة تسميتها، يمكنك حماية هيكل دفتر العمل الخاص بك بكلمة مرور.  
{{% /alert %}}  


## **حماية وإلغاء حماية هيكل دفتر العمل في MS Excel**  

**![حماية وإلغاء حماية هيكل دفتر العمل](protect-and-unprotect-workbook-structure.png)**  

1. انقر على **مراجعة > حماية الدفتر**.  
١. أدخل كلمة مرور في **مربع الكلمة السرية**.  
١. حدد **موافق**, أدخل كلمة المرور مرة أخرى لتأكيدها، ثم حدد **موافق** مجددًا.  


## **حماية بنية المصنف باستخدام Aspose.Cells for JavaScript عبر C++**  
متطلبات الترميز البسيطة التالية فقط لتنفيذ حماية هيكل دفتر العمل لملفات Excel.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Protect Workbook Structure Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ProtectionType, Utils } = AsposeCells;

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
            // Create a new workbook
            const workbook = new Workbook();

            // Protect workbook structure with a password
            workbook.protect(ProtectionType.Structure, "password");

            // Save the workbook to a downloadable file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Book1_protected.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Protected Workbook';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and protected successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```  

## **إلغاء حماية بنية المصنف باستخدام Aspose.Cells for JavaScript عبر C++**  
إلغاء حماية هيكل الدفتر بسيط مع واجهة برمجة تطبيقات Aspose.Cells.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
        <meta charset="utf-8" />
    </head>
    <body>
        <h1>Unprotect Workbook Structure Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Unprotect Workbook</button>
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
            const workbook = new Workbook(new Uint8Array(arrayBuffer));
            workbook.unprotect("password");
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            const baseName = file.name.replace(/(\.xlsx|\.xls|\.csv)$/i, '');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = baseName + '.unprotected.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Unprotected Excel File';
            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook structure unprotected successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

{{% alert color="primary" %}}  
ملاحظة: كلمة مرور صحيحة مطلوبة.  
{{% /alert %}}
