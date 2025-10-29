---
title: تحديث قيم الأشكال المرتبطة باستخدام جافا سكريبت عبر C++
linktitle: تحديث قيم الأشكال المرتبطة
type: docs
weight: 3200
url: /ar/javascript-cpp/refresh-values-of-linked-shapes/
description: تعلم كيف تقوم بتحديث قيم الأشكال المرتبطة في إكسل باستخدام Aspose.Cells for JavaScript عبر C++.
---

{{% alert color="primary" %}}

أحيانًا، لديك شكل مرتبط في ملف إكسل الخاص بك مرتبط بنتيجة خلية معينة. في ميكروسوفت إكسل، تغيير قيمة الخلية المرتبطة يغير أيضًا قيمة الشكل المرتبط. هذا يعمل أيضًا بشكل جيد مع Aspose.Cells for JavaScript عبر C++ إذا كنت ترغب في حفظ مصنفك بصيغة XLS أو XLSX. ومع ذلك، إذا كنت تريد حفظ المصنف بصيغة PDF أو HTML، فستحتاج إلى استدعاء طريقة [**ShapeCollection.updateSelectedValue()**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/#updateSelectedValue--) لتحديث قيمة الشكل المرتبط.

{{% /alert %}}

## مثال

يظهر لقطة الشاشة التالية ملف إكسل المصدر المستخدم في الشفرة أدناه. يحتوي على صورة مرتبطة مرتبطة بخلايا A1 إلى E4. سنغير قيمة الخلية B4 باستخدام Aspose.Cells ثم نستدعي طريقة [**ShapeCollection.updateSelectedValue()**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/#updateSelectedValue--) لتحديث قيمة الصورة وحفظها بتنسيق PDF.

![todo:image_alt_text](refresh-values-of-linked-shapes_1.jpg)

يمكنك تنزيل [ملف إكسل المصدر](95584291.xlsx) و [ملف PDF الناتج](95584292.pdf) من الروابط المعطاة.

### رمز جافا سكريبت لتحديث قيم الأشكال المرتبطة

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Refresh Value Of Linked Shapes Example</title>
    </head>
    <body>
        <h1>Refresh Value Of Linked Shapes Example</h1>
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

            // Create workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Change the value of cell B4
            const cell = worksheet.cells.get("B4");
            cell.value = 100;

            // Update the value of the Linked Picture which is linked to cell B4
            worksheet.shapes.updateSelectedValue();

            // Save the workbook in PDF format
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputRefreshValueOfLinkedShapes.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the PDF.</p>';
        });
    </script>
</html>
```
