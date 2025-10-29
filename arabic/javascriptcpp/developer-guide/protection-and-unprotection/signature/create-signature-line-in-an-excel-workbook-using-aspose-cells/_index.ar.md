---
title: إنشاء خط توقيع في مصنف إكسل باستخدام Aspose.Cells for JavaScript عبر C++
linktitle: إنشاء سطر توقيع في سجل Excel باستخدام Aspose.Cells
type: docs
weight: 150
url: /ar/javascript-cpp/create-signature-line-in-an-excel-workbook-using-aspose-cells/
description: يصف هذا المقال كيفية إنشاء خط توقيع في مصنف إكسل باستخدام كود جافا سكريبت مع Aspose.Cells for JavaScript عبر C++.
keywords: إنشاء خط توقيع في مصنف إكسل جافا سكريبت عبر C++، كيفية إنشاء خط توقيع في مصنف إكسل، كيفية إضافة خط توقيع، كيفية إضافة خط توقيع إلى ملف إكسل.
---

## **مقدمة**  

توفر Microsoft Excel ميزة إضافة **سطر توقيع** في سجل Excel. يمكنك إضافة سطر توقيع عن طريق النقر فوق علامة **إدراج** ثم تحديد **سطر توقيع** من مجموعة **نص**.  

## **كيفية إنشاء خط توقيع لإكسل**  

 يوفر Aspose.Cells for JavaScript عبر C++ أيضًا هذه الميزة وقدم الخاصية [**Picture.signatureLine**](https://reference.aspose.com/cells/javascript-cpp/picture/#signatureLine--) لهذا الغرض. سيوضح هذا المقال كيفية استخدام هذه الخاصية لإضافة خط توقيع باستخدام Aspose.Cells.  

يضيف رمز النموذج التالي سطر توقيع باستخدام خاصية [**Picture.signatureLine**](https://reference.aspose.com/cells/javascript-cpp/picture/#signatureLine--) ويحفظ المصنف.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Add Signature Line Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, SignatureLine, Utils } = AsposeCells;

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

            // Create or load workbook
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Create signature line object
            const signatureLine = new SignatureLine();
            signatureLine.signer = "John Doe";
            signatureLine.title = "Development Lead";
            signatureLine.email = "john.doe@aspose.com";

            // Adds a Signature Line to the first worksheet.
            workbook.worksheets.get(0).shapes.addSignatureLine(1, 1, signatureLine);

            // Save the workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Signature line added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
