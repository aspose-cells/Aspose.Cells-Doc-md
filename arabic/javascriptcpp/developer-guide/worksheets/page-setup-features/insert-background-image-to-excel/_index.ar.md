---
title: إدراج صورة خلفية إلى إكسل باستخدام JavaScript عبر C++
linktitle: إدراج صورة خلفية إلى إكسل
type: docs
weight: 90
url: /ar/javascript-cpp/insert-background-image-to-excel/
description: "كيفية إدراج صورة خلفية إلى إكسل باستخدام Aspose.Cells for JavaScript عبر C++."
---

{{% alert color="primary" %}} 

يمكنك تحسين جاذبية ورقة العمل عن طريق إضافة صورة كخلفية. يمكن أن يكون هذا الميزة فعالًا إذا كان لديك صورة توضيحية خاصة للشركة تضيف لمسة من الخلفية دون حجب البيانات على الورقة. يمكنك تعيين صورة خلفية لورقة باستخدام واجهة برمجة التطبيقات Aspose.Cells.

{{% /alert %}} 

## **تعيين خلفية الورقة في Microsoft Excel**

لتعيين صورة خلفية لورقة في Microsoft Excel (على سبيل المثال، Microsoft Excel 2019):

1. من القائمة **تخطيط الصفحة**، ابحث عن خيار **إعداد الصفحة**، ثم انقر فوق خيار **الخلفية**.
1. حدد صورة لتعيين صورة خلفية للورقة.

   **تعيين خلفية لورقة**

![todo:image_alt_text](insert-background-to-excel.jpg)

## **ضبط خلفية الورقة باستخدام Aspose.Cells for JavaScript عبر C++**

يقوم الكود أدناه بتعيين صورة خلفية باستخدام صورة من مصدر بيانات.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Set Worksheet Background Image</title>
    </head>
    <body>
        <h1>Set Worksheet Background Image Example</h1>
        <p>
            Select a background image to apply to a new workbook's first worksheet,
            then click "Apply Background & Save" to generate XLSX and HTML files.
        </p>
        <input type="file" id="bgInput" accept="image/*" />
        <button id="runExample">Apply Background & Save</button>
        <a id="downloadXlsx" style="display: none; margin-left: 10px;"></a>
        <a id="downloadHtml" style="display: none; margin-left: 10px;"></a>
        <div id="result" style="margin-top: 1em;"></div>
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
            const bgInput = document.getElementById('bgInput');
            const resultDiv = document.getElementById('result');

            if (!bgInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select a background image file.</p>';
                return;
            }

            const bgFile = bgInput.files[0];
            const arrayBuffer = await bgFile.arrayBuffer();
            const imgBytes = new Uint8Array(arrayBuffer);

            // Create a new Workbook.
            const workbook = new Workbook();

            // Get the first worksheet.
            const sheet = workbook.worksheets.get(0);

            // Set the background image for the worksheet.
            sheet.backgroundImage = imgBytes;

            // Save the Excel file (XLSX)
            const xlsxData = workbook.save(SaveFormat.Xlsx);
            const blobXlsx = new Blob([xlsxData], { type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' });
            const downloadXlsx = document.getElementById('downloadXlsx');
            downloadXlsx.href = URL.createObjectURL(blobXlsx);
            downloadXlsx.download = 'outputBackImageSheet.xlsx';
            downloadXlsx.style.display = 'inline';
            downloadXlsx.textContent = 'Download Excel File';

            // Save the HTML file
            const htmlData = workbook.save(SaveFormat.Html);
            const blobHtml = new Blob([htmlData], { type: 'text/html' });
            const downloadHtml = document.getElementById('downloadHtml');
            downloadHtml.href = URL.createObjectURL(blobHtml);
            downloadHtml.download = 'outputBackImageSheet.html';
            downloadHtml.style.display = 'inline';
            downloadHtml.textContent = 'Download HTML File';

            resultDiv.innerHTML = '<p style="color: green;">Background image applied. Download links are ready.</p>';
        });
    </script>
</html>
```

## مقالات ذات صلة

- [العمل مع الخلفية في ملفات ODS](/cells/ar/javascript-cpp/working-with-background-in-ods-files/)
