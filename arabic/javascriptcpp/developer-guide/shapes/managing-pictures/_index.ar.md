---
title: إدارة الصور باستخدام جافا سكريبت عبر C++
linktitle: إدارة الصور
type: docs
weight: 10
url: /ar/javascript-cpp/managing-pictures/
description: تعلم كيفية إضافة وتحديد موضع الصور في جداول البيانات باستخدام Aspose.Cells for JavaScript عبر C++.
---

يسمح Aspose.Cells للمطورين بإضافة الصور إلى جداول البيانات في وقت التشغيل. علاوة على ذلك، يمكن التحكم في تحديد موضع هذه الصور في وقت التشغيل، والأمر الذي يتم مناقشته بتفصيل أكثر في الأقسام القادمة.

يشرح هذا المقال كيفية إضافة الصور وكيفية إدراج صورة تظهر محتوى خلايا معينة.

## **إضافة الصور**

إضافة الصور إلى جدول بيانات سهل للغاية. يستغرق الأمر سوى بضعة أسطر من الكود:  
ببساطة استدعِ طريقة [**Add**](https://reference.aspose.com/cells/javascript-cpp/picturecollection/#add-number-number-string-) من مجموعة [**Pictures**](https://reference.aspose.com/cells/javascript-cpp/picturecollection) (الم encapsulated في كائن [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)). تأخذ طريقة [**Add**](https://reference.aspose.com/cells/javascript-cpp/picturecollection/#add-number-number-string-) المعلمات التالية:

- **فهرس الصف الأعلى الأيسر**، فهرس الصف الأعلى.
- **فهرس العمود الأعلى الأيسر**، فهرس العمود الأعلى.
- **اسم ملف الصورة**، اسم ملف الصورة، مع المسار الكامل.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Add Picture to Workbook Example</h1>
        <p>Select an optional Excel file to update (or leave empty to create a new workbook), and select an image file to insert as a picture.</p>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <input type="file" id="imageInput" accept="image/*" />
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
            const imageInput = document.getElementById('imageInput');
            const resultDiv = document.getElementById('result');
            resultDiv.innerHTML = '';

            if (!imageInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an image file to insert.</p>';
                return;
            }

            // Load existing workbook if provided, otherwise create a new one
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Adding a new worksheet to the Workbook object
            const sheetIndex = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(sheetIndex);

            // Read image file bytes
            const imageFile = imageInput.files[0];
            const imageArrayBuffer = await imageFile.arrayBuffer();
            const imageBytes = new Uint8Array(imageArrayBuffer);

            // Adding a picture at the location of a cell whose row and column indices are 5 (F6)
            worksheet.pictures.add(5, 5, imageBytes);

            // Saving the Excel file (Excel 97-2003 .xls format)
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Picture added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **تحديد مواقع الصور**

هناك طريقتان ممكنتان للتحكم في تحديد موقع الصور باستخدام Aspose.Cells:

- تحديد موقع نسبي: تعريف موقع نسبي لارتفاع الصف والعرض.
- التمركز المطلق: تحديد الموقع الدقيق على الصفحة حيث سيتم إدراج الصورة، على سبيل المثال، 40 بكسل إلى اليسار و20 بكسل أسفل حافة الخلية.

### **التحديد النسبي**

يمكن للمطورين وضع الصور بنسبة متناسبة مع ارتفاع الصف وعرض العمود باستخدام خصائص [**upperDeltaX**](https://reference.aspose.com/cells/javascript-cpp/shape/#upperDeltaX--) و [**upperDeltaY**](https://reference.aspose.com/cells/javascript-cpp/shape/#upperDeltaY--) من كائن [**Picture**](https://reference.aspose.com/cells/javascript-cpp/picture/). يمكن الحصول على كائن [**Picture**](https://reference.aspose.com/cells/javascript-cpp/picture/) من مجموعة [**Pictures**](https://reference.aspose.com/cells/javascript-cpp/picturecollection) من خلال تمرير فهرس الصورة الخاص به. يُضع هذا المثال صورة في خلية F6.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells - Add Picture to New Workbook</h1>
        <p>Select an image to insert into a new Excel workbook. The picture will be placed at cell F6 (row 5, column 5).</p>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <br/><br/>
        <label for="imageInput">Select image to insert:</label>
        <input type="file" id="imageInput" accept="image/*" />
        <br/><br/>
        <button id="runExample">Create Workbook and Add Picture</button>
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
            const imageInput = document.getElementById('imageInput');
            if (!imageInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an image file to insert.</p>';
                return;
            }

            // Instantiate a new Workbook
            const workbook = new Workbook();

            // Add a new worksheet to the Workbook object
            const sheetIndex = workbook.worksheets.add();

            // Obtain the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(sheetIndex);

            // Read the selected image file as bytes
            const imageFile = imageInput.files[0];
            const arrayBuffer = await imageFile.arrayBuffer();
            const imageBytes = new Uint8Array(arrayBuffer);

            // Adding a picture at the location of a cell whose row and column indices are 5 (F6)
            const pictureIndex = worksheet.pictures.add(5, 5, imageBytes);

            // Accessing the newly added picture
            const picture = worksheet.pictures.get(pictureIndex);

            // Positioning the picture proportional to row height and column width (property assignments)
            picture.upperDeltaX = 200;
            picture.upperDeltaY = 200;

            // Saving the Excel file (Excel 97-2003 format)
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and picture added successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

### **التحديد المطلق**

يمكن للمطورين أيضًا وضع الصور بشكل مطلق باستخدام خصائص [**left**](https://reference.aspose.com/cells/javascript-cpp/shape/#left--) و [**top**](https://reference.aspose.com/cells/javascript-cpp/shape/#top--) من كائن [**Picture**](https://reference.aspose.com/cells/javascript-cpp/picture/). يضع هذا المثال صورة في الخلية F6، على بعد 60 بكسل من اليسار و 10 بكسل من أعلى الخلية.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Add Picture</title>
    </head>
    <body>
        <h1>Add Picture to Workbook Example</h1>
        <p>Select an image file to insert into a new Excel workbook:</p>
        <input type="file" id="fileInput" accept="image/*" />
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
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an image file.</p>';
                return;
            }

            // Read image file as bytes
            const imageFile = fileInput.files[0];
            const arrayBuffer = await imageFile.arrayBuffer();
            const imageBytes = new Uint8Array(arrayBuffer);

            // Instantiating a Workbook object
            const workbook = new Workbook();

            // Adding a new worksheet to the Workbook object
            const sheetIndex = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(sheetIndex);

            // Adding a picture at the location of a cell whose row and column indices are 5 in the worksheet ("F6")
            const pictureIndex = worksheet.pictures.add(5, 5, imageBytes);

            // Accessing the newly added picture
            const picture = worksheet.pictures.get(pictureIndex);

            // Absolute positioning of the picture in unit of pixels
            picture.left = 60;
            picture.top = 10;

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Picture added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **إدراج صورة بناءً على مرجع الخلية**

يتيح Aspose.Cells عرض محتويات خلية ورق العمل في شكل صورة. يمكنك ربط الصورة بالخلية التي تحتوي على البيانات التي ترغب في عرضها. نظرًا لأن الخلية، أو نطاق الخلية، مرتبط بالكائن الرسومي، فإن التغييرات التي تقوم بها في البيانات في تلك الخلية أو نطاق الخلية ستظهر تلقائيًا في الكائن الرسومي.

أضف صورة إلى ورقة العمل عن طريق استدعاء طريقة [**ShapeCollection.addPicture(number, number, number, number, Uint8Array)**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/#addPicture-number-number-number-number-uint8array-) من مجموعة [**ShapeCollection**](https://reference.aspose.com/cells/javascript-cpp/shapecollection) (الم encapsulated في كائن [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)). حدد نطاق الخلايا باستخدام سمة [**formula**](https://reference.aspose.com/cells/javascript-cpp/picture/#formula--) من كائن [**Picture**](https://reference.aspose.com/cells/javascript-cpp/picture/).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
        <meta charset="utf-8" />
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
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
            // This example creates a new workbook, modifies cells and pictures, and saves it.
            const workbook = new Workbook();

            // Get the first worksheet's cells collection
            const worksheet = workbook.worksheets.get(0);
            const cells = worksheet.cells;

            // Add string values to the cells
            cells.get("A1").value = "A1";
            cells.get("C10").value = "C10";

            // Get pictures collection and add a blank picture to the D1 cell
            const picts = worksheet.pictures;
            const picIndex = picts.add(0, 3, 10, 6, null);
            const pic = picts.get(picIndex);

            // Specify the formula that refers to the source range of cells
            pic.formula = "A1:C10";

            // Update the shapes selected value in the worksheet
            worksheet.shapes.updateSelectedValue();

            // Save the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **مواضيع متقدمة**
- [إضافة مجموعة رموز مشروطة مع نص الخلية](/cells/ar/javascript-cpp/add-conditional-icons-set-with-the-cell-text/)
- [إدراج صورة مرتبطة من عنوان ويب](/cells/ar/javascript-cpp/insert-a-linked-picture-from-web-address/)
- [إدراج صورة بناءً على مرجع الخلية](/cells/ar/javascript-cpp/insert-a-picture-based-on-cell-reference/)
- [تحميل صورة ويب من عنوان URL إلى ورقة عمل Excel](/cells/ar/javascript-cpp/load-a-web-image-from-a-url-into-an-excel-worksheet/)
