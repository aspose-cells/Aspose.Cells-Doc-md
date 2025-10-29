---
title: الوصول إلى مربع النص بواسطة الاسم باستخدام جافا سكريبت عبر C++
linktitle: الوصول إلى مربع النص من خلال الاسم
type: docs
weight: 230
url: /ar/javascript-cpp/access-the-text-box-by-the-name/
description: تعلم كيفية الوصول إلى مربع النص حسب الاسم من المجموعة باستخدام Aspose.Cells for JavaScript عبر C++. 
---

## الوصول إلى مربع النص بالاسم

في السابق، كان يتم الوصول إلى صناديق النص بالترتيب من مجموعة [**Worksheet.textBoxes**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#textBoxes--)، لكن الآن يمكنك الوصول أيضًا إلى صندوق النص بالاسم من هذه المجموعة. هذه طريقة مريحة وسريعة للوصول إلى صندوق النص إذا كنت تعرف اسمه بالفعل.

الكود المصدري التالي يقوم أولاً بإنشاء مربع نص وتعيين نص واسم له. ثم في الأسطر التالية، نقوم بالوصول إلى نفس مربع النص باستخدام اسمه وطباعة نصه.

### كود جافا سكريبت للوصول إلى مربع النص بالاسم

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

            const sheet = workbook.worksheets.get(0);

            const idx = sheet.textBoxes.add(10, 10, 10, 10);

            const tb1 = sheet.textBoxes.get(idx);
            tb1.name = "MyTextBox";
            tb1.text = "This is MyTextBox";

            const tb2 = sheet.textBoxes.get("MyTextBox");

            console.log(tb2.text);

            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'sample.modified.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = `<p style="color: green;">TextBox added. Text from named TextBox: ${tb2.text}</p>`;
        });
    </script>
</html>
```

### المخرجات في وحدة الطرفية التي تم إنشاؤها بواسطة الكود النموذجي



{{< highlight javascript >}}
This is MyTextBox
{{< /highlight >}}
