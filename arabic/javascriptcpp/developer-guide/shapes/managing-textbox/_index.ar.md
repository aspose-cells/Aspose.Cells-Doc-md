---
title: إدارة مربع النص باستخدام جافا سكريبت عبر C++
linktitle: إدارة مربع النص
type: docs
weight: 50
url: /ar/javascript-cpp/managing-textbox-of-excel/
description: تعلم كيفية إدارة مربع النص في إكسل باستخدام Aspose.Cells for JavaScript عبر C++. 
keywords: إدارة مربع النص في إكسل عبر جافا سكريبت باستخدام C++
---

## **سيناريوهات الاستخدام المحتملة**
هناك سيناريوهات قد تحتاج فيها إلى إضافة أو تحديث أو التعامل مع عناصر مربع النص داخل ورقة عمل إكسل. يمكن أن يكون ذلك مفيدًا لإضافة تعليقات، نصوص إرشادية، أو أي معلومات إضافية تساعد في عرض البيانات. يوفر Aspose.Cells for JavaScript عبر C++ وظائف قوية لإدارة مربع النص في مستندات إكسل. 

## ** إدارة مربع النص باستخدام Aspose.Cells for JavaScript عبر C++**
يوضح هذا المثال كيف:

1. إنشاء ورقة عمل جديدة.
2. أضف شكل WordArt.
3. عدِّل خصائص مربع النص حسب الحاجة.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells TextBox Example</title>
    </head>
    <body>
        <h1>TextBox Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Color } = AsposeCells;

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
            let workbook;

            if (fileInput.files && fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Adding a TextBox shape
            const textBox = worksheet.shapes.addTextBox(2, 2, 100, 100);

            // Set TextBox properties (converted getters/setters to properties)
            textBox.text = "This is a TextBox.";
            textBox.fontSize = 12;
            textBox.fillColor = Color.fromArgb(255, 255, 255); // White background

            // Save the workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'TextBoxExample.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created/modified successfully. Click the download link to get the file.</p>';
        });
    </script>
</html>
```

توضح هذه الرموز كيفية إنشاء وتكوين مربع النص داخل ورقة عمل Excel، مع إظهار كيفية تعديل حجمه وموقعه وتنسيقه وفقًا لمتطلباتك.

 ضع في اعتبارك أن التفاعلات مع مربعات النص قد تختلف بناءً على الحالات الخاصة، لذا استشر توثيق Aspose.Cells for JavaScript عبر C++ للحصول على طرق وخصائص إضافية.
