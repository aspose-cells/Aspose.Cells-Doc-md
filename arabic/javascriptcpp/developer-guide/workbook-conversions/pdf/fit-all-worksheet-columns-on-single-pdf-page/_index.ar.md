---
title: تناسب جميع أعمدة ورقة العمل على صفحة PDF واحدة باستخدام JavaScript عبر C++
linktitle: ملائمة جميع أعمدة الصفحة العملية على صفحة PDF واحدة
type: docs
weight: 160
url: /ar/javascript-cpp/fit-all-worksheet-columns-on-single-pdf-page/
---

{{% alert color="primary" %}}

أحيانًا تحتاج إلى إنشاء ملف PDF يلائم جميع أعمدة صفحة العملية على صفحة واحدة. توفر الخاصية [**PdfSaveOptions.allColumnsInOnePagePerSheet**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#allColumnsInOnePagePerSheet--) هذه الميزة بطريقة سهلة الاستخدام جدًا. يتم التعامل مع الحسابات المعقدة مثل ارتفاع وعرض PDF الناتج داخليًا ويستند إلى البيانات في صفحة العملية.

{{% /alert %}}

## **ملائمة أعمدة صفحة العملية على صفحة PDF واحدة**

[**PdfSaveOptions.allColumnsInOnePagePerSheet**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#allColumnsInOnePagePerSheet--) يضمن أن يتم عرض جميع أعمدة ورقة العمل على صفحة PDF واحدة، على الرغم من أن الصفوف قد تتوسع إلى عدة صفحات اعتمادًا على البيانات في ورقة العمل.

الكود النموذجي أدناه يوضح كيفية استخدام [**PdfSaveOptions.allColumnsInOnePagePerSheet**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#allColumnsInOnePagePerSheet--) لعرض صفحة عمل كبيرة تحتوي على 100 عمود.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Save Workbook to PDF Example</title>
    </head>
    <body>
        <h1>Save Workbook to PDF Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, PdfSaveOptions, SaveFormat, Utils } = AsposeCells;

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

            // Create and initialize an instance of Workbook
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Create and initialize an instance of PdfSaveOptions
            const saveOptions = new PdfSaveOptions();
            // Set AllColumnsInOnePagePerSheet to true (converted from setter to property)
            saveOptions.allColumnsInOnePagePerSheet = true;

            // Save Workbook to PDF format by passing the object of PdfSaveOptions
            const outputData = workbook.save(SaveFormat.Pdf, saveOptions);
            const blob = new Blob([outputData], { type: "application/pdf" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            resultDiv.innerHTML = '<p style="color: green;">PDF created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

{{% alert color="primary" %}}

عندما يحتوي ورق العمل المعطى على العديد من الأعمدة، قد يظهر ملف PDF المقرن بحجم صغير جدًا. لا يزال قابلاً للقراءة عند تكبيره في تطبيق العرض مثل Acrobat Reader.

{{% /alert %}} {{% alert color="primary" %}}

إذا كانت جداول البيانات الخاصة بك تحتوي على صيغ، من الأفضل استدعاء [**Workbook.calculateFormula()**](https://reference.aspose.com/cells/javascript-cpp/workbook/#calculateFormula--) قبل تحويل جدول البيانات إلى تنسيق PDF. وذلك سيضمن إعادة حساب قيم الصيغ الخاصة وتقديم القيم الصحيحة في الملف الناتج PDF.

{{% /alert %}}
