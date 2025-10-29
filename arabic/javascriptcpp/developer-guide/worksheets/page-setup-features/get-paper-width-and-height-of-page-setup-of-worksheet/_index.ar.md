---
title: الحصول على عرض وارتفاع ورقة إعداد الصفحة لورقة العمل باستخدام جافا سكريبت عبر C++
linktitle: الحصول على عرض وارتفاع الورق لإعداد الصفحة لورقة العمل
type: docs
weight: 50
url: /ar/javascript-cpp/get-paper-width-and-height-of-page-setup-of-worksheet/
description: اكتشف كيفية الحصول على عرض وارتفاع ورقة إعداد صفحة العمل في إكسل باستخدام جافا سكريبت عبر C++ برمجيًا.
keywords: إعداد حجم الورق لصفحة الإعداد في إكسل، إعداد ارتفاع الورق جافا سكريبت عبر C++، إعداد عرض الورق جافا سكريبت عبر C++
---

## **سيناريوهات الاستخدام المحتملة**

أحيانًا، تحتاج إلى معرفة عرض وارتفاع حجم الورق كما تم تعيينه في إعداد الصفحة لورقة العمل. يرجى استخدام الخاصيتين [**PageSetup.paperWidth**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#paperWidth--) و [**PageSetup.paperHeight**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#paperHeight--) لهذا الغرض.

## **الحصول على عرض وارتفاع الورق لإعداد الصفحة لورقة العمل**

يفسر الكود النموذجي التالي استخدام الخاصتين [**PageSetup.paperWidth**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#paperWidth--) و [**PageSetup.paperHeight**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#paperHeight--). يغير أولاً حجم الورق إلى *A2* ثم يحدد عرض وارتفاع الورق، ثم يغير إلى *A3*, *A4*, و *Letter* ويحدد عرض وارتفاع الورق على التوالي.

### **الكود المثالي**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Paper Size Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell, Utils } = AsposeCells;

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

            // If a file is selected, open it; otherwise create a new workbook
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Access first worksheet
            const sheet = workbook.worksheets.get(0);

            // Set paper size to A2 and print paper width and height in inches
            sheet.pageSetup.paperSize = AsposeCells.PaperSizeType.PaperA2;
            console.log("PaperA2: " + sheet.pageSetup.paperWidth + "x" + sheet.pageSetup.paperHeight);

            // Set paper size to A3 and print paper width and height in inches
            sheet.pageSetup.paperSize = AsposeCells.PaperSizeType.PaperA3;
            console.log("PaperA3: " + sheet.pageSetup.paperWidth + "x" + sheet.pageSetup.paperHeight);

            // Set paper size to A4 and print paper width and height in inches
            sheet.pageSetup.paperSize = AsposeCells.PaperSizeType.PaperA4;
            console.log("PaperA4: " + sheet.pageSetup.paperWidth + "x" + sheet.pageSetup.paperHeight);

            // Set paper size to Letter and print paper width and height in inches
            sheet.pageSetup.paperSize = AsposeCells.PaperSizeType.PaperLetter;
            console.log("PaperLetter: " + sheet.pageSetup.paperWidth + "x" + sheet.pageSetup.paperHeight);

            const outputLines = [
                "PaperA2: " + sheet.pageSetup.paperWidth + "x" + sheet.pageSetup.paperHeight,
                "PaperA3: " + sheet.pageSetup.paperWidth + "x" + sheet.pageSetup.paperHeight,
                "PaperA4: " + sheet.pageSetup.paperWidth + "x" + sheet.pageSetup.paperHeight,
                "PaperLetter: " + sheet.pageSetup.paperWidth + "x" + sheet.pageSetup.paperHeight
            ];

            document.getElementById('result').innerHTML = '<pre>' + outputLines.join('\n') + '</pre>';
        });
    </script>
</html>
```

### **مخرجات الوحدة**



{{< highlight java >}}

PaperA2: 16.54x23.39

PaperA3: 11.69x16.54

PaperA4: 8.27x11.69

PaperLetter: 8.5x11

{{< /highlight >}}
