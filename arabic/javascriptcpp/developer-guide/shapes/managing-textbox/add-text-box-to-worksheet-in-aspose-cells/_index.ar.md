---
title: كيفية إضافة/تضمين مربع نص إلى ورقة العمل باستخدام جافا سكريبت عبر C++
linktitle: إضافة مربع نص إلى ورقة العمل
type: docs
weight: 10
url: /ar/javascript-cpp/add-text-box-to-worksheet-in-aspose-cells/
description: كيفية إضافة/تضمين مربع نص إلى ورقة العمل في Aspose.Cells for JavaScript عبر C++.
keywords: إضافة/تضمين مربع النص إلى ورقة عمل Excel Aspose JavaScript عبر C++
---

## إضافة مربع نص إلى ورقة العمل في إكسل

في برنامج Excel (الإصدار 07 وما فوق)، هناك مكانان يمكن إدراج صناديق النص فيهما. واحد في "إدراج - أشكال"، الآخر على الجهة اليمنى من الشريط العلوي لخيار "إدراج".

### الطريقة الأولى:

![1](1.png)

### الطريقة الثانية:

![2](2.png)

## كيفية الإنشاء

يمكنك إنشاء مربعات نص بنص أفقي أو رأسي.

- حدد الخيار المقابل (أفقي أو عمودي)
- انقر بالزر الأيسر على الصفحة
- اضغط على الزر الأيسر واسحب مسافة على الصفحة
- أفلت الزر الأيسر

الآن حصلت على صندوق نص.

## إضافة مربع نص إلى ورقة العمل في Aspose.Cells for JavaScript عبر C++

عند الحاجة إلى إدراج العديد من صناديق النص في ورقة العمل دفعة واحدة، فإن طريقة الإدراج اليدوي تعتبر كارثة. إذا كان هذا يزعجك، أعتقد أن هذا المستند سيساعدك. يوفر لك [Aspose.Cells](https://products.aspose.com/cells/) واجهة برمجة تطبيقات لإجراء عمليات إدراج جماعية بسهولة في كودك.

الكود النموذجي التالي ينشئ مربع نص.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Add TextBox</title>
    </head>
    <body>
        <h1>Add TextBox to Workbook</h1>
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
            const fileInput = document.getElementById('fileInput');
            // If a file is provided, open it; otherwise create a new workbook
            let workbook;
            if (fileInput.files && fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Access first worksheet from the collection
            const sheet = workbook.worksheets.get(0);

            // Add the TextBox to the worksheet
            sheet.textBoxes.add(6, 10, 100, 200);

            // Save and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'result.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">TextBox added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

ستحصل على ملف مشابه لـ [نتيجة الملف](result.xlsx). في الملف، سترى ما يلي:

![](52449.png)
