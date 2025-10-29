---
title: عرض صفحة PDF واحدة لكل ورقة عمل Excel  تحويل Excel إلى PDF باستخدام JavaScript عبر C++
linktitle: عرض صفحة PDF واحدة لكل ورقة Excel  تحويل Excel إلى صيغة PDF
type: docs
weight: 100
url: /ar/javascript-cpp/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/
---

{{% alert color="primary" %}}

عند العمل مع ملفات Microsoft Excel الكبيرة (على سبيل المثال، مصنف يحتوي على العديد من الأوراق، كل ورقة بها 50 عمودًا و300 أو أكثر من الصفوف من البيانات)، قد ترغب في أن يُظهر إخراج PDF صفحة واحدة لكل ورقة عمل، بغض النظر عن حجم ورقة العمل. هذا يعني أن كل صفحة قد تكون ذات حجم صفحة مختلف بشكل جذري. يمكن تحقيق ذلك باستخدام Aspose.Cells for JavaScript عبر C++.

{{% /alert %}}

يرجى الاطلاع على الكود النموذجي التالي الذي يحول ملف Excel مع العديد من الأوراق إلى PDF.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Excel to PDF</title>
    </head>
    <body>
        <h1>Convert Excel to PDF (One Page Per Worksheet)</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
        <button id="runExample">Convert to PDF</button>
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

            // Initialize a new Workbook by opening the selected Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Implement one page per worksheet option
            const pdfSaveOptions = new PdfSaveOptions();
            pdfSaveOptions.onePagePerSheet = true;

            // Save the PDF file (returns binary data)
            const outputData = workbook.save(SaveFormat.Pdf, pdfSaveOptions);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'OutputFile.out.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">PDF generated successfully! Click the download link to get the PDF file.</p>';
        });
    </script>
</html>
```

{{% alert color="primary" %}}

إذا تم تعيين خيار [PdfSaveOptions.onePagePerSheet](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#onePagePerSheet--) إلى **true**، سيتم عرض محتوى جميع الأوراق على صفحة PDF واحدة.

{{% /alert %}} {{% alert color="primary" %}}

إذا كانت ورقة العمل تحتوي على معادلات، فمن الأفضل استدعاء [Workbook.calculateFormula()](https://reference.aspose.com/cells/javascript-cpp/workbook/#calculateFormula--) قبل تصدير ورقة العمل إلى PDF. يضمن ذلك إعادة حساب القيم المعتمدة على المعادلة، وظهور القيم الصحيحة في PDF.

{{% /alert %}}
