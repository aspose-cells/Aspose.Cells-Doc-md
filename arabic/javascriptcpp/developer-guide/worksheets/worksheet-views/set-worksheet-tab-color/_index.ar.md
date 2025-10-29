---
title: تعيين لون علامة تبويب الورقة باستخدام جافا سكريبت عبر ++C
linktitle: تعيين لون علامة التبويب للورقة العمل
type: docs
weight: 120
url: /ar/javascript-cpp/set-worksheet-tab-color/
description: يعرض هذا المقال رمزًا يضبط لون علامة تبويب ورقة إكسل برمجياً باستخدام جافا سكريبت عبر ++C.
keywords: تعيين لون علامة تبويب إكسل جافا سكريبت عبر ++C، رمز لتعيين لون علامة تبويب إكسل جافا سكريبت عبر ++C
---

{{% alert color="primary" %}}

تسمح Aspose.Cells لك بتغيير لون علامات تبويب ورق العمل الفردية لتمييزها عن البقية. على سبيل المثال، يمكنك جعل تكاليف بلون أحمر، ومبيعات بلون أخضر، وأصول بلون أزرق، وما إلى ذلك.

{{% /alert %}}
## **ضبط لون علامة تبويب ورق العمل باستخدام Microsoft Excel**
1. انقر بزر الماوس الأيمن فوق علامة تبويب في ورقة العلامات في أسفل ورقة العمل الحالية.
1. حدد **لون العلامة التبويب**.
1. حدد لونًا من اللوحة.
1. انقر على **موافق**.
## **تعيين لون علامة تبويب الورقة العمل باستخدام Aspose.Cells**
الشيفرة المثالية أدناه تظهر كيفية تعيين لون علامة تبويب باستخدام Aspose.Cells.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Set Worksheet Tab Color Example</title>
    </head>
    <body>
        <h1>Set Worksheet Tab Color Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
        <button id="runExample">Run Example</button>
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
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();
            const workbook = new Workbook(new Uint8Array(arrayBuffer));
            const worksheet = workbook.worksheets.get(0);
            worksheet.tabColor = AsposeCells.Color.Red;
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'worksheettabcolor.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';
            document.getElementById('result').innerHTML = '<p style="color: green;">Worksheet tab color set successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
