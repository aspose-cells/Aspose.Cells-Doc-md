---
title: حساب صيغة المصفوفة لجدول البيانات باستخدام JavaScript عبر C++
linktitle: حساب الصيغة الصفيفية لجداول البيانات
description: كيفية استخدام مكتبة Aspose.Cells لحساب صيغ المصفوفة لجدول البيانات في Microsoft Excel باستخدام JavaScript عبر C++. قم بتحميل أو إنشاء ملف Excel، حساب صيغة المصفوفة، وحفظ الملف المعدل.
keywords: Aspose.Cells، Excel، جداول البيانات، صيغ المصفوفة، الحسابات JavaScript عبر C++
type: docs
weight: 70
url: /ar/javascript-cpp/calculation-of-array-formula-of-data-tables/
---

{{% alert color="primary" %}}

يمكنك إنشاء جدول بيانات في Microsoft Excel باستخدام البيانات > تحليل ماذا-لو > جدول البيانات.... يتيح لك Aspose.Cells الآن حساب صيغة المصفوفة الخاصة بجدول البيانات. يرجى استخدام [**Workbook.calculateFormula()**](https://reference.aspose.com/cells/javascript-cpp/workbook/#calculateFormula--) كالمعتاد لحساب أي نوع من الصيغ.

{{% /alert %}}

في الكود النموذجي التالي، استخدمنا الملف المصدر (ملف Excel مصدر)5115535.xlsx. إذا قمت بتغيير قيمة الخلية B1 إلى 100، ستصبح قيم جدول البيانات المحددة باللون الأصفر 120 كما هو موضح في الصور التالية. يولد الكود النموذجي الملف [PDF الناتج](5115538.pdf).

![todo:image_alt_text](calculation-of-array-formula-of-data-tables_1.png)

![todo:image_alt_text](calculation-of-array-formula-of-data-tables_2.png)



```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>DataTable Calculation Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
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

            // Creating a Workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // When you will put 100 in B1, then all Data Table values formatted as Yellow will become 120
            const cell = worksheet.cells.get("B1");
            cell.putValue(100);

            // Calculate formula, now it also calculates Data Table array formula
            workbook.calculateFormula();

            // Save the workbook in pdf format
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: "application/pdf" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the PDF file.</p>';
        });
    </script>
</html>
```
