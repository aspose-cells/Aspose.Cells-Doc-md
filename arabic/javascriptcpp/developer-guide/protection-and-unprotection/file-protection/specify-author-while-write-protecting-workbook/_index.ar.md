---
title: تحديد المؤلف أثناء حماية محتوى الكتاب باستخدام جافا سكريبت عبر C++
linktitle: تحديد المؤلف أثناء حماية كتاب العمل
type: docs
weight: 40
url: /ar/javascript-cpp/specify-author-while-write-protecting-workbook/
description: تحديد اسم مؤلف أثناء حماية كتاب باستخدام Aspose.Cells for JavaScript عبر C++.
---

## **سيناريوهات الاستخدام المحتملة**

 يمكنك تحديد اسم مؤلف أثناء حماية حقوق الطباعة لمصنف باستخدام Aspose.Cells API. يرجى استخدام خاصية [**Workbook.author**](https://reference.aspose.com/cells/javascript-cpp/writeprotection/#author--) لهذا الغرض.

## **تحديد المؤلف أثناء حماية كتاب العمل**

يوضح رمز النموذج التالي استخدام خاصية [**Workbook.author**](https://reference.aspose.com/cells/javascript-cpp/writeprotection/#author--). ينشئ الكود مصنف فارغ، ويحميه بكلمة مرور، ويحدد اسم المؤلف، ويحفظه باسم [ملف Excel الناتج](67338582.xlsx). توضح لقطة الشاشة التالية تأثير رمز النموذج على ملف Excel الناتج لمعاينتك.

![todo:image_alt_text](specify-author-while-write-protecting-workbook_1.png)

## **الكود المثالي**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Specify Author While Write Protecting Workbook</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
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
            // Create empty workbook.
            const workbook = new Workbook();

            // Write protect workbook with password.
            workbook.settings.writeProtection.password = "1234";

            // Specify author while write protecting workbook.
            workbook.settings.writeProtection.author = "SimonAspose";

            // Save the workbook in XLSX format.
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputSpecifyAuthorWhileWriteProtectingWorkbook.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and write-protected successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
