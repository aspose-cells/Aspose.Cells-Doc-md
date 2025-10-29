---
title: طباعة التعليقات عند الحفظ إلى PDF باستخدام JavaScript عبر C++
linktitle: طباعة التعليقات أثناء الحفظ إلى صيغة PDF
type: docs
weight: 10
url: /ar/javascript-cpp/print-comments-while-saving-to-pdf/
description: تعلم كيفية طباعة التعليقات عند حفظ مستندات إكسل كملفات PDF باستخدام Aspose.Cells for JavaScript عبر C++.
---

{{% alert color="primary" %}}  

تسمح Microsoft Excel بطباعة التعليقات أثناء الطباعة أو الحفظ في صيغة PDF بالخيارات التالية  

- لا شيء  
- في نهاية الجدول  
- كما هو معروض على الجدول  

توفر Aspose.Cells تعدد القوائم [**PrintCommentsType**](https://reference.aspose.com/cells/javascript-cpp/printcommentstype) لدعم نفس الميزات. يحتوي تعدد القوائم [**PrintCommentsType**](https://reference.aspose.com/cells/javascript-cpp/printcommentstype) على الأعضاء التالية  

- PrintNoComments  
- PrintInPlace  
- PrintSheetEnd  

{{% /alert %}}  

## **طباعة التعليقات عند الحفظ إلى PDF**  

يوضح الكود التالي كيفية استخدام [**PrintCommentsType**](https://reference.aspose.com/cells/javascript-cpp/printcommentstype) لطباعة التعليقات عند الحفظ إلى PDF.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Print Comments to PDF</title>
    </head>
    <body>
        <h1>Print Comments While Saving to PDF Example</h1>
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

            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            const worksheet = workbook.worksheets.get(0);

            worksheet.pageSetup.printComments = AsposeCells.PrintCommentsType.PrintSheetEnd;

            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'PrintCommentWhileSavingToPdf_out.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook saved to PDF with comments printed at sheet end. Click the download link to get the file.</p>';
        });
    </script>
</html>
```
