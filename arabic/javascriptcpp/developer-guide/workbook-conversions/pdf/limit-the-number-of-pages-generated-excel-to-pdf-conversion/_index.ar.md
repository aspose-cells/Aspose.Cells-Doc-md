---
title: تحديد عدد الصفحات الناتجة  تحويل إكسل إلى PDF باستخدام JavaScript عبر C++
linktitle: تحديد عدد الصفحات المولدة  تحويل Excel إلى PDF
type: docs
weight: 180
url: /ar/javascript-cpp/limit-the-number-of-pages-generated-excel-to-pdf-conversion/
description: تعلم كيفية تحديد عدد الصفحات التي يتم إنشاؤها عند تحويل جدول إكسل إلى PDF باستخدام Aspose.Cells for JavaScript عبر C++. 
---

{{% alert color="primary" %}}

 أحيانًا، تريد طباعة نطاق من الصفحات إلى ملف PDF إخراج. يمتلك Aspose.Cells for JavaScript عبر C++ القدرة على تحديد حد لعدد الصفحات التي يتم إنشاؤها عند تحويل جدول إكسل إلى تنسيق ملف PDF.

{{% /alert %}}

## **تحديد الحد الأقصى لعدد الصفحات المولدة**

المثال التالي يظهر كيفية عرض مجموعة من الصفحات (3 و 4) في ملف Microsoft Excel إلى صيغة PDF.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells PDF Export Example</title>
    </head>
    <body>
        <h1>Export Specific Pages to PDF</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PdfSaveOptions } = AsposeCells;

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

            // Open an Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Instantiate the PdfSaveOption
            const options = new PdfSaveOptions();

            // Print only Page 3 and Page 4 in the output PDF
            // Starting page index (0-based index)
            options.pageIndex = 3;
            // Number of pages to be printed
            options.pageCount = 2;

            // Save the PDF file
            const outputData = workbook.save(SaveFormat.Pdf, options);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outPDF1.out.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">PDF generated successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

{{% alert color="primary" %}}

إذا كانت الورقة تحتوي على صيغ، فمن الأفضل استدعاء [**Workbook.calculateFormula()**](https://reference.aspose.com/cells/javascript-cpp/workbook/#calculateFormula--) قبل عرضها كملف PDF. يضمن ذلك إعادة حساب القيم المعتمدة على الصيغة، وعرض القيم الصحيحة في الملف الناتج.

{{% /alert %}}
