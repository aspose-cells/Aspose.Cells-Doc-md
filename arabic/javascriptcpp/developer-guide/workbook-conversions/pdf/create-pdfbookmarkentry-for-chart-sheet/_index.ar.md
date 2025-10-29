---
title: إنشاء مدخل إشارة مرجعية لورقة الرسوم البيانية باستخدام JavaScript عبر C++
linktitle: إنشاء إدخال PdfBookmarkEntry لورقة الرسم البياني
type: docs
weight: 50
url: /ar/javascript-cpp/create-pdfbookmarkentry-for-chart-sheet/
description: تعلم كيفية إنشاء PdfBookmarkEntry لأوراق المخططات باستخدام Aspose.Cells for JavaScript عبر C++.
---

## **سيناريوهات الاستخدام المحتملة**  

في السابق، كانت Aspose.Cells تنشئ [**PdfBookmarkEntry**](https://reference.aspose.com/cells/javascript-cpp/pdfbookmarkentry) للورقة العادية. لكن الآن، يمكن لـ Aspose.Cells أيضًا إنشاء [**PdfBookmarkEntry**](https://reference.aspose.com/cells/javascript-cpp/pdfbookmarkentry) لورقات الرسوم البيانية. نظرًا لعدم وجود خلايا أخرى في ورقة الرسم البياني غير الخلية A1، فستقوم بإنشاء [**PdfBookmarkEntry**](https://reference.aspose.com/cells/javascript-cpp/pdfbookmarkentry) فقط للخلية A1.  

## **إنشاء PdfBookmarkEntry لورقة الرسم البياني**  

يقوم الكود النموذجي التالي بتحميل [ملف Excel عينة](61767756.xlsx) الذي يحتوي على أربع صفحات. اثنتان منها عادية والأخرتان صفحات رسم بياني. ويقوم بإنشاء أربعة إدخالات للإشارة كما يلي  

- إشارة-I  
- إشارة-II-Chart1  
- إشارة-III  
- إشارة-IV-Chart2  

تظهر الصورة الملتقطة التالية [PDF المولد](61767757.pdf) بواسطة الكود النموذجي للإشارة.  

![todo:image_alt_text](create-pdfbookmarkentry-for-chart-sheet_1.png)  

## **الكود المثالي**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Create PDF Bookmark Entry for Chart Sheet Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PdfBookmarkEntry, PdfSaveOptions, Utils } = AsposeCells;

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

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access all four worksheets
            const sheet1 = workbook.worksheets.get(0);
            const sheet2 = workbook.worksheets.get(1);
            const sheet3 = workbook.worksheets.get(2);
            const sheet4 = workbook.worksheets.get(3);

            // Create Pdf Bookmark Entry for Sheet1
            const ent1 = new PdfBookmarkEntry();
            ent1.destination = sheet1.cells.get("A1");
            ent1.text = "Bookmark-I";

            // Create Pdf Bookmark Entry for Sheet2 - Chart
            const ent2 = new PdfBookmarkEntry();
            ent2.destination = sheet2.cells.get("A1");
            ent2.text = "Bookmark-II-Chart1";

            // Create Pdf Bookmark Entry for Sheet3
            const ent3 = new PdfBookmarkEntry();
            ent3.destination = sheet3.cells.get("A1");
            ent3.text = "Bookmark-III";

            // Create Pdf Bookmark Entry for Sheet4 - Chart
            const ent4 = new PdfBookmarkEntry();
            ent4.destination = sheet4.cells.get("A1");
            ent4.text = "Bookmark-IV-Chart2";

            // Arrange all Bookmark Entries
            const lst = [];
            lst.push(ent2);
            lst.push(ent3);
            lst.push(ent4);

            // Create Pdf Save Options with Bookmark Entries
            const opts = new PdfSaveOptions();
            opts.bookmark = ent1;

            // Save the output Pdf
            const outputData = workbook.save(SaveFormat.Pdf, opts);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputCreatePdfBookmarkEntryForChartSheet.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">PDF created successfully! Click the download link to get the PDF file.</p>';
        });
    </script>
</html>
```
