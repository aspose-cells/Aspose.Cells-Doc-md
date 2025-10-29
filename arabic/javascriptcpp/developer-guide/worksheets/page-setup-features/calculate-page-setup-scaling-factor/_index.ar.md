---
title: حساب معامل تكبير إعداد صفحة الطباعة باستخدام جافا سكريبت عبر C++
linktitle: حساب عامل تحجيم إعداد الصفحة
type: docs
weight: 300
url: /ar/javascript-cpp/calculate-page-setup-scaling-factor/
description: توفر هذه المقالة رمزًا نمطيًا يوضح كيفية استخدام API جافا سكريبت عبر C++ لحساب معامل تكبير إعداد الصفحة باستخدام خيار الملائم لعرض n صفحة(ات) واسعة وm طويلة من ورقة عمل إكسل برمجيًا.
keywords: ملائمة لn صفحة بعرض و m طول، جافا سكريبت إكسل عبر C++، حساب معامل تكبير إعداد الصفحة جافا سكريبت عبر C++
---

{{% alert color="primary" %}}

عند تعيين مقياس إعداد الصفحة باستخدام خيار **الملاءمة إلى ن صفحة(ات) عرضية و م عالية**، يقوم Microsoft Excel بحساب عامل مقياس إعداد الصفحة. يمكنك حساب الشيء نفسه باستخدام الخاصية [**SheetRender.pageScale**](https://reference.aspose.com/cells/javascript-cpp/sheetrender/#pageScale--). تُرجع هذه الخاصية قيمة مزدوجة يمكن تحويلها إلى قيمة نسبة مئوية. على سبيل المثال، إذا كانت تُرجع 0.5 فهذا يعني أن عامل القياس هو 50%.

{{% /alert %}}

الرمز العيني التالي يوضح كيفية حساب عامل تحجيم إعداد الصفحة باستخدام الخاصية [**SheetRender.pageScale**](https://reference.aspose.com/cells/javascript-cpp/sheetrender/#pageScale--).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Page Scale</title>
    </head>
    <body>
        <h1>Page Scale Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, SheetRender, ImageOrPrintOptions, PaperSizeType, Utils } = AsposeCells;

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

            // Opening the Excel file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Put some data in these cells
            worksheet.cells.get("A4").putValue("Test");
            worksheet.cells.get("S4").putValue("Test");

            // Set paper size
            worksheet.pageSetup.paperSize = PaperSizeType.PaperA4;

            // Set fit to pages wide as 1
            worksheet.pageSetup.fitToPagesWide = 1;

            // Calculate page scale via sheet render
            const sr = new SheetRender(worksheet, new ImageOrPrintOptions());

            // Convert page scale double value to percentage
            const strPageScale = (sr.pageScale * 100).toFixed(0) + "%";

            // Write the page scale value
            document.getElementById('result').innerHTML = `<p>Page Scale: ${strPageScale}</p>`;
            console.log(strPageScale);
        });
    </script>
</html>
```
