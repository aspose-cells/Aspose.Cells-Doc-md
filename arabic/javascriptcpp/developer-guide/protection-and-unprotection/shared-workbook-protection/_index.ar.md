---
title: حماية أو إلغاء حماية الملف المشترك باستخدام JavaScript عبر C++
linktitle: حماية كلمة المرور أو إلغاء حمايتها لكتاب العمل المشترك
type: docs
weight: 10
url: /ar/javascript-cpp/password-protect-or-unprotect-the-shared-workbook/
---

## **سيناريوهات الاستخدام المحتملة**

 يمكنك حماية الملف المشترك أو إلغاء حمايته باستخدام Microsoft Excel كما هو موضح في لقطة الشاشة التالية. يدعم Aspose.Cells for JavaScript عبر C++ أيضًا هذه الميزة باستخدام الطريقتين [**Workbook.protectSharedWorkbook(string)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#protectSharedWorkbook-string-) و [**Workbook.unprotectSharedWorkbook(string)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#unprotectSharedWorkbook-string-).

![todo:image_alt_text](password-protect-or-unprotect-the-shared-workbook_1.png)

## **حماية كلمة المرور أو إلغاء حمايتها لكتاب العمل المشترك**

الرمز البريدي العيني التالي ينشئ كتاب عمل ويحميه أثناء تمكين العمل المشترك ويحفظه كملف Excel الناتج. تبين لقطة الشاشة أنه عند محاولة إلغاء حمايته ، يطلب منك Microsoft Excel إدخال كلمة المرور لإلغاء حمايته.

![todo:image_alt_text](password-protect-or-unprotect-the-shared-workbook_2.png)

## **الكود المثالي**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Protect Shared Workbook Example</h1>
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
            // Creating an empty Workbook
            const workbook = new Workbook();

            // Protect the Shared Workbook with Password
            workbook.protectSharedWorkbook("1234");

            // Uncomment this line to Unprotect the Shared Workbook
            // workbook.unprotectSharedWorkbook("1234");

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputProtectSharedWorkbook.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook protected successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
