---
title: تحديد ما إذا كان حجم الورق في ورقة العمل تلقائيًا باستخدام جافا سكريبت عبر C++
linktitle: تحديد ما إذا كان حجم الورق للورقة التفاعلي
type: docs
weight: 90
url: /ar/javascript-cpp/determine-if-paper-size-of-worksheet-is-automatic/
description: تشرح هذه المقالة كيفية استخدام API جافا سكريبت مع إضافات C++ لتحديد ما إذا كان حجم الورق في ورقة عمل معين مضبوطًا على وضع تلقائي برمجيًا.
keywords: تحديد ما إذا كان حجم الورق في ورقة العمل تلقائيًا باستخدام جافا سكريبت عبر C++
---

## **سيناريوهات الاستخدام المحتملة**

غالبًا ما يكون حجم الورق لورقة العمل تلقائيًا. عندما يكون تلقائيًا، غالبًا يكون مضبوطًا على *Letter*. أحيانًا يحدد المستخدم حجم الورق لورقة العمل حسب متطلباته. في هذه الحالة، فإن حجم الورق ليس تلقائيًا. يمكنك معرفة ما إذا كان حجم الورق لورقة العمل تلقائيًا أو لا باستخدام الخاصية [**Worksheet.isAutomaticPaperSize()**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#isAutomaticPaperSize--).

## **تحديد ما إذا كان حجم الورق للورقة تلقائي**

الشيفرة العينية المعطاة أدناه تحمل الملفات الإكسل التاليتين

- [samplePageSetupIsAutomaticPaperSize-False.xlsx](48496681.xlsx)
- [samplePageSetupIsAutomaticPaperSize-True.xlsx](48496682.xlsx)

ثم ابحث عما إذا كان حجم الورق لأول ورقة فيهما تلقائيًا أم لا. في Microsoft Excel، يمكنك التحقق ما إذا كان حجم الورق تلقائيًا أو لا من خلال نافذة إعداد الصفحة كما هو موضح في هذه لقطة الشاشة.

![todo:image_alt_text](determine-if-paper-size-of-worksheet-is-automatic_1.png)

## **الكود المثالي**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - PageSetup IsAutomaticPaperSize</title>
    </head>
    <body>
        <h1>PageSetup IsAutomaticPaperSize Example</h1>
        <p>Select two Excel files to compare the PageSetup.isAutomaticPaperSize property:</p>
        <input type="file" id="fileInput1" accept=".xls,.xlsx,.csv" />
        <input type="file" id="fileInput2" accept=".xls,.xlsx,.csv" />
        <br/><br/>
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
            const fileInput1 = document.getElementById('fileInput1');
            const fileInput2 = document.getElementById('fileInput2');
            const resultDiv = document.getElementById('result');

            if (!fileInput1.files.length || !fileInput2.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select both Excel files.</p>';
                return;
            }

            const file1 = fileInput1.files[0];
            const file2 = fileInput2.files[0];

            const arrayBuffer1 = await file1.arrayBuffer();
            const arrayBuffer2 = await file2.arrayBuffer();

            // Instantiating Workbook objects from uploaded files
            const wb1 = new Workbook(new Uint8Array(arrayBuffer1));
            const wb2 = new Workbook(new Uint8Array(arrayBuffer2));

            // Access first worksheet of both workbooks
            const ws11 = wb1.worksheets.get(0);
            const ws12 = wb2.worksheets.get(0);

            // Read the PageSetup.isAutomaticPaperSize property of both worksheets
            const isAuto1 = ws11.pageSetup.isAutomaticPaperSize;
            const isAuto2 = ws12.pageSetup.isAutomaticPaperSize;

            // Display results
            resultDiv.innerHTML = `
                <p>First Worksheet of First Workbook - IsAutomaticPaperSize: ${isAuto1}</p>
                <p>First Worksheet of Second Workbook - IsAutomaticPaperSize: ${isAuto2}</p>
            `;
        });
    </script>
</html>
```

## **مخرجات الوحدة**



{{< highlight java >}}

First Worksheet of First Workbook - IsAutomaticPaperSize: False

First Worksheet of Second Workbook - IsAutomaticPaperSize: True

{{< /highlight >}}
