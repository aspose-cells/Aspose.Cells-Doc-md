---
title: إدراج صورة بناءً على إشارة الخلية باستخدام JavaScript عبر C++
linktitle: إدراج صورة بناءً على مرجع الخلية
type: docs
weight: 150
url: /ar/javascript-cpp/insert-a-picture-based-on-cell-reference/
description: تعلم كيفية إدراج صورة في ورقة عمل بناءً على إشارة خلية باستخدام Aspose.Cells for JavaScript عبر C++. عرض بيانات الخلية في صورة.
---

{{% alert color="primary" %}}
أحيانًا يكون لديك صورة فارغة وتحتاج إلى عرض البيانات أو المحتويات في الصورة عن طريق تحديد إشارة للخلية في شريط الصيغة. تدعم Aspose.Cells هذه الميزة (Microsoft Excel 2010).
{{% /alert %}}

## إدراج صورة بناءً على إشارة الخلية

 يدعم Aspose.Cells for JavaScript عبر C++ عرض محتويات خلية ورقة العمل في شكل صورة. يمكنك ربط الصورة بالخلية التي تحتوي على البيانات التي تريد عرضها. بما أن الخلية أو نطاق الخلايا مرتبط بالكائن الرسومي، تظهر التغييرات التي تجريها على البيانات في تلك الخلية أو النطاق تلقائيًا في الكائن الرسومي. أضف صورة إلى ورقة العمل باستدعاء طريقة [**ShapeCollection.addPicture(number, number, number, number, Uint8Array)**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/#addPicture-number-number-number-number-uint8array-) من مجموعة [**ShapeCollection**](https://reference.aspose.com/cells/javascript-cpp/shapecollection) (الملفوفة في كائن [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)). حدد نطاق الخلايا باستخدام سمة [**Picture.formula**](https://reference.aspose.com/cells/javascript-cpp/picture/#formula--) من الكائن [**Picture**](https://reference.aspose.com/cells/javascript-cpp/picture).

### مثال على الكود

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Referenced Picture Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
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
            // Instantiate a new Workbook
            const workbook = new Workbook();
            // Get the first worksheet's cells collection
            const cells = workbook.worksheets.get(0).cells;

            // Add string values to the cells
            cells.get("A1").value = "A1";
            cells.get("C10").value = "C10";

            // Get the conditional icon's image data
            const imagedata = AsposeCells.ConditionalFormattingIcon.iconImageData(AsposeCells.IconSetType.TrafficLights31, 0);
            // Create a stream based on the image data
            const stream = Uint8Array.from(imagedata);

            // Add a blank picture to the D1 cell
            const pic = workbook.worksheets.get(0).shapes.addPicture(0, 3, stream, 10, 10);
            // Specify the formula that refers to the source range of cells
            pic.formula = "A1:C10";
            // Update the shapes selected value in the worksheet
            workbook.worksheets.get(0).shapes.updateSelectedValue();

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'referencedpicture.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
