---
title: تجميد العمود(أعمدة) الأولى من ورقة عمل إكسل باستخدام جافا سكريبت عبر C++
linktitle: تجميد الأعمدة
type: docs
weight: 190
url: /ar/javascript-cpp/how-to-freeze-columns-of-excel-worksheet
description: تعلم كيفية تجميد الأعمدة اليسرى لورقات عمل إكسل برمجياً باستخدام Aspose.Cells for JavaScript عبر C++.
keywords: تجميد الأعمدة اليسرى، تجميد الأعمدة الأولى، قفل العمود/الأعمدة
---

## **مقدمة**  

في هذه المقالة، سنتعلم كيف نجمّد العمود(الأعمدة) اليسرى. عندما يكون لديك كمية هائلة من البيانات في صف، قد لا تتمكن من رؤية الأعمدة اليسرى عند التمرير الأفقي لورقة العمل. يمكنك تجميد وقفل العمود(الأعمدة) الأولى بحيث يمكنك رؤية الجزء المجمد حتى عند تمرير باقي البيانات. يمكنك بسهولة رؤية رؤوس الأعمدة في الأعمدة اليسرى.  

## **تجميد الأعمدة في Excel**  

**![تجميد الأعمدة اليسرى في Excel](freeze-columns.png)**  

1. إذا أردت تجميد العمود/الأعمدة اليسرى، فابدأ بتحديد العمود تحت العمود الذي يحتاج إلى تجميده.
2. انقر على عرض > تجميد الأجزاء.
3. في القائمة المنسدلة، انقر فوق تجميد العمود الأول.
4. إذا قمت بالتمرير لأسفل، سيكون العمود الأول دائماً في العرض الأيسر.

**![عمود مجمد](frozen-columns.png)**  

كما ترى، العمود الأول مجمد، والعمود الأول دائمًا ثابت في الأعلى عند التمرير أفقيًا.

تتيح لك ميزة تجميد الأعمدة عرض بياناتك الطويلة بدون عناء تتبع العمود الأول.

## **تجميد الأعمدة باستخدام Aspose.Cells for JavaScript عبر C++**  
من السهل تجميد العمود / الأعمدة الأولى باستخدام Aspose.Cells for JavaScript عبر C++.  
يرجى استخدام طريقة [**Worksheet.freezePanes(number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#freezePanes-number-number-number-number-) لتجميد الأعمدة عند العمود المحدد.  
1. إنشاء دفتر العمل لفتح الملف أو إنشاء ملف فارغ.
2. تجميد العمود الأول باستخدام طريقة Worksheet.freezePanes()
3. حفظ الملف.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Freeze Panes Example</title>
    </head>
    <body>
        <h1>Freeze Panes Example</h1>
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

            // Instantiate a new Workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Freezing panes at the second column on the first worksheet
            const worksheet = workbook.worksheets.get(0);
            worksheet.freezePanes("B1", 0, 1);

            // Saving the file and preparing download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], { type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'frozen.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Frozen Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Freeze panes applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

المرفق [ملف الإكسيل عينة](Freeze.xlsx).
