---
title: تحويل ملف XLS مع الصور أو الرسوم البيانية إلى PDF باستخدام JavaScript عبر C++
linktitle: تحويل ملف XLS الذي يحتوي على صور أو رسومات إلى PDF
type: docs
weight: 50
url: /ar/javascript-cpp/convert-xls-file-with-images-or-charts-to-pdf/
---

{{% alert color="primary" %}} 

يدعم Aspose.Cells تحويل ملفات XLS التي تحتوي على صور ورسوم بيانية إلى مستندات PDF. يمكن لسكربت Aspose.Cells for Java عبر C++ العمل بشكل مستقل لتحويل جدول البيانات إلى PDF: لا يلزم استخدام Aspose.PDF للJavaScript عبر C++ في عملية التحويل. يمكن إتمام العملية في الذاكرة لأنها لا تعتمد على ملفات XML مؤقتة أو وسيطة. هذا يعني أن ملفات Excel الكبيرة، مثل التي تحتوي على صور ورسوم بيانية وأشياء أخرى، يمكن تحويلها بسرعة وفعالية.

{{% /alert %}} 
## **الكود المثالي**


```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Convert Excel to PDF Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Convert to PDF</button>
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

            // Instantiating a Workbook object by opening the Excel file from the file input
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Save the workbook as PDF
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Output.out.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">PDF generated successfully! Click the download link to get the PDF file.</p>';
        });
    </script>
</html>
```

{{% alert color="primary" %}} 

إذا كان جدول البيانات يحتوي على صيغ، فمن الأفضل استدعاء طريقة [Workbook.calculateFormula()](https://reference.aspose.com/cells/javascript-cpp/workbook/#calculateFormula--) قبل تحويله إلى PDF. يضمن ذلك إعادة حساب القيم المعتمدة على الصيغ، وعرض القيم الصحيحة في ملف PDF.

{{% /alert %}}
