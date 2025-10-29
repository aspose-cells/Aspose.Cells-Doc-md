---
title: تجنب الصفحة الفارغة في ملف PDF الناتج عندما لا يوجد شيء للطباعة باستخدام JavaScript عبر C++
linktitle: تجنب الصفحة الفارغة في ملف PDF الناتج عندما لا يوجد شيء للطباعة
type: docs
weight: 30
url: /ar/javascript-cpp/avoid-blank-page-in-output-pdf-when-there-is-nothing-to-print/
description: تعلم كيفية تجنب الصفحات الفارغة في ملف PDF الناتج عندما لا يوجد شيء للطباعة باستخدام Aspose.Cells for Java سكربت عبر C++.
---

## **سيناريوهات الاستخدام المحتملة**

عندما يكون ملف Excel فارغًا ويحفظه المستخدم إلى PDF باستخدام Aspose.Cells for Java سكربت عبر C++، فإنه يعرض صفحة فارغة في ملف PDF الناتج. أحيانًا، يكون هذا السلوك الافتراضي غير مرغوب فيه. يوفر Aspose.Cells الخاصية [**PdfSaveOptions.outputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#outputBlankPageWhenNothingToPrint--) لمعالجة هذه المشكلة. إذا قمت بضبطها على **false**، فسيحدث استثناء كلما لم توجد شيء للطباعة في ملف PDF الناتج.

## **تجنب الصفحة الفارغة في ملف PDF الناتج عندما لا يوجد شيء للطباعة**

 ينشئ المثال التالي كودًا نموذجيًا لمصنف فارغ ثم يحفظه كملف PDF بعد ضبط الخاصية [**PdfSaveOptions.outputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#outputBlankPageWhenNothingToPrint--) على **false**. بما أنه لا يوجد شيء للطباعة في ملف PDF الناتج، يحدث استثناء كما هو موضح أدناه.

## **الكود المثالي**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Save Workbook to PDF Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PdfSaveOptions, Utils } = AsposeCells;

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
                // No file selected - will create an empty workbook (to mirror original JavaScript behavior)
                document.getElementById('result').innerHTML = '<p>No file selected. Creating an empty workbook and attempting to save to PDF.</p>';
            } else {
                document.getElementById('result').innerHTML = '<p>Loading selected workbook...</p>';
            }

            // Instantiate workbook from file if provided, otherwise create an empty workbook
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Create Pdf save options.
            const opts = new PdfSaveOptions();

            // Default value of OutputBlankPageWhenNothingToPrint is true.
            // Setting false means - Do not output blank page when there is nothing to print.
            opts.outputBlankPageWhenNothingToPrint = false;

            // Save workbook to Pdf format.
            // Note: If workbook has nothing to print and outputBlankPageWhenNothingToPrint is false,
            // this operation may throw an exception which will propagate (no try-catch per requirements).
            const outputData = workbook.save(SaveFormat.Pdf, opts);

            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">PDF generated successfully. Click the download link to get the file.</p>';
        });
    </script>
</html>
```

## **استثناء**

{{< highlight javascript >}}

 exception was unhandled

  HResult=-2146232832

  Message=There is nothing to output/print.

  Source=Aspose.Cells

  StackTrace:

       at Aspose.Cells.Workbook.Save(String fileName, SaveOptions saveOptions)

{{< /highlight >}}
