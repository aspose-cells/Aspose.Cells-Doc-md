---
title: تجميد أجزاء من جدول بيانات إكسل باستخدام جافا سكريبت عبر C++
linktitle: تجميد الأجزاء
type: docs
weight: 190
url: /ar/javascript-cpp/how-to-freeze-panes-of-excel-worksheet
description: في هذا المقال، ستتعلم كيفية تجميد أجزاء من جداول بيانات إكسل برمجياً باستخدام Aspose.Cells for JavaScript عبر C++.
keywords: تجميد الأجزاء، تجميد النافذة.
---

## **مقدمة**  

في هذه المقالة، سنتعلم كيف نجمّد الأجزاء. عندما يكون لديك كمية كبيرة من البيانات تحت عنوان مشترك، لا يمكنك رؤية العنوان عند التمرير لأسفل ورقة العمل. ويحتوي كل سجل على العديد من البيانات. يمكنك تجميد الأجزاء بحيث يمكنك رؤية الجزء المجمد حتى عند تمرير باقي البيانات. يمكنك بسهولة رؤية الرؤوس في الصفوف العليا أو الأعمدة الأولى. التجميد وفك التجميد للأجزاء يغير فقط عرض البيانات بدون تغيير البيانات نفسها.  

## **في إكسل**  

**![تجميد الأجزاء في إكسل](Freeze-panes.png)**  

1. إذا كنت تريد تجميد الأجزاء، وتجميد الصفوف والأعمدة، فحدد أولاً خلية (مثل B2).  
2. انقر على عرض > تجميد الأجزاء.  
3. في القائمة المنسدلة، انقر على تجميد الأجزاء.  
4. إذا قمت بالتمرير لأسفل أو لليمين، فإن الصف الأول والعمود يظل معلقًا.  

**![الأجزاء المجمدة](Frozen-Panes.png)**  

كما ترى، تم تجميد الصف الأول والعمود A، والصف الثاني هو 32 والعمود المرئي الثاني هو D.  

تمكنك ميزة تجميد الأجزاء من عرض بياناتك الكبيرة بدون الحاجة إلى تتبع علامات الصف أو العمود.  

## **تجميد الأجزاء مع Aspose.Cells for JavaScript عبر C++**  
من السهل تجميد الأجزاء باستخدام Aspose.Cells for JavaScript عبر C++. يرجى استخدام طريقة [**Worksheet.freezePanes(number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#freezePanes-number-number-number-number-) لتجميد الأجزاء عند الخلية المحددة.  
1. إنشاء دفتر العمل لفتح الملف أو إنشاء ملف فارغ.  
2. تجميد الأجزاء باستخدام طريقة Worksheet.freezePanes()  
3. حفظ الملف.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Freeze Panes Example</title>
    </head>
    <body>
        <h1>Freeze Panes Example</h1>
        <p>Select an Excel file (Freeze.xlsx) and click "Run Example" to freeze panes at B2.</p>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>

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
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Freezing panes at the cell B2
            worksheet.freezePanes("B2", 1, 1);

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'frozen.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Frozen Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Panes frozen successfully! Click the download link to get the modified file.</p>';
        });
    </script>
    </body>
</html>
```  

المرفق [ملف الإكسيل عينة](Freeze.xlsx).
