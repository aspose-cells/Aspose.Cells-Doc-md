---
title: إدراج صورة مرتبطة من عنوان ويب باستخدام JavaScript عبر C++
linktitle: إدراج صورة ربط من عنوان الويب
type: docs
weight: 450
url: /ar/javascript-cpp/insert-a-linked-picture-from-web-address/
description: تعلم كيفية إدراج صورة مرتبطة من عنوان ويب في ورقة العمل باستخدام Aspose.Cells for JavaScript عبر C++.
---

{{% alert color="primary" %}}
 في بعض الأحيان تحتاج إلى إدراج صورة من الويب (http://) في ورقة عمل. للقيام بذلك، حدد عنوان URL للصورة، وسيتم تنزيل الصورة في كل مرة يتم فيها فتح جدول البيانات في إكسل. الصورة غير مضمنة فعليًا في مستند إكسل، ولكنها تشير إلى مصدر ويب.
{{% /alert %}}

## **استخدام Microsoft Excel**

في Microsoft Excel (على سبيل المثال 2007):

1. انقر فوق قائمة **إدراج** وحدد **صورة**.  
1. حدد عنوان الويب للصورة في مربع حوار إدراج صورة.

## ** باستخدام Aspose.Cells for JavaScript عبر C++**

 يدعم Aspose.Cells for JavaScript عبر C++ إضافة صورة مرتبطة باستخدام [**ShapeCollection.addLinkedPicture(upperLeftRow, upperLeftColumn, heightPixels, widthPixels, sourceFullName)**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/#addLinkedPicture-number-number-number-number-string-). ترجع الطريقة كائن [**Picture**](https://reference.aspose.com/cells/javascript-cpp/picture).

يظهر المثال التالي كيفية إضافة صورة مرتبطة من عنوان ويب إلى ورقة عمل.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells - Insert Linked Picture Example</h1>
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
            const fileInput = document.getElementById('fileInput');

            if (fileInput.files.length) {
                // If file provided, use it as the base workbook
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                var workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                // Otherwise create a new workbook
                var workbook = new Workbook();
            }

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Insert a linked picture (from Web Address) to B2 Cell.
            const pic = worksheet.shapes.addLinkedPicture(1, 1, 100, 100, "http://www.aspose.com/Images/aspose-logo.jpg");

            // Set the height and width of the inserted image.
            pic.heightInch = 1.04;
            pic.widthInch = 2.6;

            // Save the Excel file and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outLinkedPicture.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Linked picture inserted successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
