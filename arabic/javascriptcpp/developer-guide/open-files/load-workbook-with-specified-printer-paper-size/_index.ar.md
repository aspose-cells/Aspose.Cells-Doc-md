---
title: تحميل دفتر العمل بحجم ورق طابعة محدد via JavaScript و C++
linktitle: تحميل الدفتر بحجم ورقة الطابعة المحدد
type: docs
weight: 430
url: /ar/javascript-cpp/load-workbook-with-specified-printer-paper-size/
description: تعلّم كيفية تعيين حجم ورق الطابعة أثناء تحميل دفتر العمل باستخدام Aspose.Cells for JavaScript عبر C++.
---

{{% alert color="primary" %}}
يمكنك تحديد حجم ورق الطابعة الذي تختاره أثناء تحميل دفتر العمل باستخدام خاصية [**LoadOptions.paperSize(PaperSizeType)**](https://reference.aspose.com/cells/javascript-cpp/loadoptions/#paperSize-papersizetype-). يرجى ملاحظة، إذا قمت بإنشاء ملف جديد في MS Excel، ستجد أن حجم الورق هو نفس إعداد الطابعة الافتراضية في جهازك.
{{% /alert %}}

يوضح الرمز التالي استخدام خاصية [**LoadOptions.paperSize(PaperSizeType)**](https://reference.aspose.com/cells/javascript-cpp/loadoptions/#paperSize-papersizetype-). يبدأ بإنشاء دفتر عمل، ثم يحفظه في تدفق ذاكرة بصيغة XLSX. ثم يقوم بتحميله بحجم ورق A5 ويحفظه بصيغة PDF. ثم يعيده بتحميله بحجم ورق A3 ويحفظه مرة أخرى بصيغة PDF. إذا فتحت ملفات الـ PDF الناتجة وتحققت من حجم الورق، سترى أنها مختلفة. واحدة بحجم A5 والأخرى بحجم A3. يرجى تنزيل ملف PDF الناتج بحجم A5 ([5115234.pdf](5115234.pdf)) وملف PDF بحجم A3 ([5115233.pdf](5115233.pdf)) الذي أنشأه الشيفرة للمراجعة.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Load Workbook With Printer Size Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLinkA5" style="display: none; margin-right: 10px;">Download A5 PDF</a>
        <a id="downloadLinkA3" style="display: none;">Download A3 PDF</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, LoadOptions, LoadFormat, PaperSizeType, SaveFormat, Utils } = AsposeCells;

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
            // This example does not require a file input; file input is present per template.
            const resultDiv = document.getElementById('result');

            // Create a sample workbook and add some data inside the first worksheet
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            const cell = worksheet.cells.get("P30");
            cell.value = "This is sample data.";

            // Save the workbook into a byte array (in-memory)
            const msData = workbook.save(SaveFormat.Xlsx);

            // Load the workbook from memory with A5 paper size
            const opts = new LoadOptions(LoadFormat.Xlsx);
            opts.paperSize = PaperSizeType.PaperA5;
            const workbookA5 = new Workbook(msData, opts);

            // Save the workbook in PDF format (A5)
            const outputDataA5 = workbookA5.save(SaveFormat.Pdf);
            const blobA5 = new Blob([outputDataA5], { type: 'application/pdf' });
            const downloadLinkA5 = document.getElementById('downloadLinkA5');
            downloadLinkA5.href = URL.createObjectURL(blobA5);
            downloadLinkA5.download = 'LoadWorkbookWithPrinterSize-a5_out.pdf';
            downloadLinkA5.style.display = 'inline-block';
            downloadLinkA5.textContent = 'Download A5 PDF';

            // Load the workbook again from the same memory data with A3 paper size
            opts.paperSize = PaperSizeType.PaperA3;
            const workbookA3 = new Workbook(msData, opts);

            // Save the workbook in PDF format (A3)
            const outputDataA3 = workbookA3.save(SaveFormat.Pdf);
            const blobA3 = new Blob([outputDataA3], { type: 'application/pdf' });
            const downloadLinkA3 = document.getElementById('downloadLinkA3');
            downloadLinkA3.href = URL.createObjectURL(blobA3);
            downloadLinkA3.download = 'LoadWorkbookWithPrinterSize-a3_out.pdf';
            downloadLinkA3.style.display = 'inline-block';
            downloadLinkA3.textContent = 'Download A3 PDF';

            resultDiv.innerHTML = '<p style="color: green;">PDF files generated successfully. Use the links above to download the A5 and A3 PDFs.</p>';
        });
    </script>
</html>
```
