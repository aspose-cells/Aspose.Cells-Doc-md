---
title: إدراج الصور والأشكال في ملفات إكسل باستخدام JavaScript عبر C++  
linktitle: الأشكال  
type: docs  
weight: 140  
url: /ar/javascript-cpp/insert-shapes/  
description: إدارة الصور، كائنات OLE، والأشكال في ملفات إكسل باستخدام Aspose.Cells for JavaScript عبر C++.  
---  

{{% alert color="primary" %}}  
أحيانًا تحتاج إلى إدراج بعض الأشكال الضرورية في ورقة العمل. قد تحتاج إلى إدراج نفس الشكل في مواقع مختلفة من ورقة العمل. أو تحتاج إلى إدراج العديد من الأشكال دفعة واحدة في ورقة العمل.  
لا تقلق! [Aspose.Cells](https://products.aspose.com/cells/) تدعم جميع هذه العمليات.  
{{% /alert %}}  

الأشكال في Excel مقسمة بشكل رئيسي إلى الأنواع التالية:  
- **الصور**  
- **الكائنات OLE**  
- **الخطوط**  
- **المستطيلات**  
- **الأشكال الأساسية**  
- **السهام البلوكية**  
- **أشكال المعادلة**  
- **رسوم بيانية لسير العمل**  
- **النجوم والرايات**  
- **التلويحات**  

سيختار هذا المستند التعليمي شكلين أو شكل واحد من كل نوع لإنشاء عينات. من خلال هذه الأمثلة، ستتعلم كيفية استخدام [Aspose.Cells](https://products.aspose.com/cells/) لإدراج الشكل المحدد في ورقة العمل.  

## ** إضافة الصور إلى ورقة عمل إكسل باستخدام JavaScript**  

إضافة الصور إلى جدول بيانات سهل للغاية. يستغرق الأمر سوى بضعة أسطر من الكود:  
ببساطة استدعِ طريقة [**PictureCollection.add(number, number, number, number, Uint8Array)**](https://reference.aspose.com/cells/javascript-cpp/picturecollection/#add-number-number-number-number-uint8array-) من مجموعة [**Pictures**](https://reference.aspose.com/cells/javascript-cpp/picturecollection) (الم encapsulated في كائن [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)). تأخذ طريقة [**PictureCollection.add(number, number, number, number, Uint8Array)**](https://reference.aspose.com/cells/javascript-cpp/picturecollection/#add-number-number-number-number-uint8array-) المعلمات التالية:  

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
        <p>
            Optional: select an existing Excel file to modify, or leave empty to create a new workbook.
        </p>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <p>
            Select an image to insert into the worksheet (required):
        </p>
        <input type="file" id="imageInput" accept="image/*" />
        <br/><br/>
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;"></a>
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

            if (!imageInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an image file to insert.</p>';
                return;
            }

            // If an Excel file is provided, open it; otherwise create a new workbook
            let workbook;
            if (fileInput.files.length) {
                const excelFile = fileInput.files[0];
                const arrayBuffer = await excelFile.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Add a new worksheet to the Workbook object
            const sheetIndex = workbook.worksheets.add();

            // Obtain the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(sheetIndex);

            // Read the selected image file as Uint8Array
            const imageFile = imageInput.files[0];
            const imageArrayBuffer = await imageFile.arrayBuffer();
            const imageBytes = new Uint8Array(imageArrayBuffer);

            // Adding a picture at the location of a cell whose row and column indices are 5 (F6)
            worksheet.pictures.add(5, 5, imageBytes);

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Resulting Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Picture inserted successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

## ** إدراج كائنات OLE في ورقة عمل إكسل باستخدام JavaScript**  

يدعم Aspose.Cells إضافة واستخراج والتعامل مع كائنات OLE في أوراق العمل. لهذا السبب، يحتوي Aspose.Cells على فئة [**OleObjectCollection**](https://reference.aspose.com/cells/javascript-cpp/oleobjectcollection)، المستخدمة لإضافة كائن OLE جديد إلى قائمة التجميع. فئة أخرى، [**OleObject**](https://reference.aspose.com/cells/javascript-cpp/oleobject)، تمثل كائن OLE. لديها بعض الأعضاء المهمة:  

- تحدد الخاصية [**OleObject.imageData**](https://reference.aspose.com/cells/javascript-cpp/oleobject/#imageData--) بيانات الصورة (الأيقونة) من نوع مصفوفة البايت. سيتم عرض الصورة لعرض كائن OLE في ورقة العمل.  
- تحدد الخاصية [**OleObject.objectData**](https://reference.aspose.com/cells/javascript-cpp/oleobject/#objectData--) بيانات الكائن على شكل مصفوفة البايت. سيتم عرض هذه البيانات في البرنامج المعني عند النقر المزدوج على أيقونة كائن OLE.  

المثال التالي يوضح كيفية إضافة كائنات OLE إلى ورقة العمل.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Insert OLE Object Example</h1>
        <p>
            Select an image to display as the OLE object's icon and an Excel file to embed as the OLE object.
        </p>
        <input type="file" id="imageInput" accept="image/*" />
        <input type="file" id="excelInput" accept=".xls,.xlsx" />
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
            const imageInput = document.getElementById('imageInput');
            const excelInput = document.getElementById('excelInput');
            const resultDiv = document.getElementById('result');

            if (!imageInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an image file for the OLE icon.</p>';
                return;
            }
            if (!excelInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file to embed.</p>';
                return;
            }

            const imageFile = imageInput.files[0];
            const excelFile = excelInput.files[0];

            // Read files as ArrayBuffers
            const imageArrayBuffer = await imageFile.arrayBuffer();
            const excelArrayBuffer = await excelFile.arrayBuffer();

            // Convert to Uint8Array for Aspose.Cells
            const imageData = new Uint8Array(imageArrayBuffer);
            const objectData = new Uint8Array(excelArrayBuffer);

            // Instantiate a new Workbook.
            const workbook = new Workbook();

            // Get the first worksheet.
            const sheet = workbook.worksheets.get(0);

            // Add an Ole object into the worksheet with the image shown in MS Excel.
            sheet.oleObjects.add(14, 3, 200, 220, imageData);

            // Set embedded ole object data.
            sheet.oleObjects.get(0).objectData = objectData;

            // Save the excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData], { type: 'application/vnd.ms-excel' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">OLE object embedded successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

## ** إدراج خط إلى ورقة عمل إكسل باستخدام JavaScript**  

ينتمي شكل الخط إلى فئة **الخطوط**.  

*  

- حدد الخلية التي تريد إدراج الخط فيها  
- انقر فوق القائمة إدراج وانقر فوق الأشكال.  
- ثم، اختر الخط من 'الأشكال المستخدمة مؤخرًا' أو 'الخطوط'  

![](line.png)  

***استخدام Aspose.Cells***  

يمكنك استخدام الطريقة التالية لإدراج خط في ورقة العمل.  

{{% alert color="primary" %}}  
[**ShapeCollection.addLine(number, number, number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/#addLine-number-number-number-number-number-number-)  
 ترجع الطريقة كائن [LineShape](https://reference.aspose.com/cells/javascript-cpp/lineshape).  
{{% /alert %}}  

يوضح المثال التالي كيفية إدراج خط في ورقة العمل.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Add Line Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell } = AsposeCells;

        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");
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

                // Access first worksheet from the collection
                const sheet = workbook.worksheets.get(0);

                // Add the line to the worksheet
                sheet.shapes.addLine(2, 0, 2, 0, 100, 300);

                // Save workbook to XLSX format and create download link
                const outputData = workbook.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById('downloadLink');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = 'sample.xlsx';
                downloadLink.style.display = 'block';
                downloadLink.textContent = 'Download Excel File';

                document.getElementById('result').innerHTML = '<p style="color: green;">Line added successfully! Click the download link to get the modified file.</p>';
            });
        });
    </script>
</html>
```  

قم بتنفيذ الكود أعلاه، ستحصل على النتائج التالية:  

![](line2.png)  

## ** إدراج سهم خطي إلى ورقة عمل إكسل باستخدام JavaScript**  

شكل سهم السطر ينتمي إلى فئة **الخطوط**. وهو حالة خاصة من الخط.  

*  

- حدد الخلية التي تريد إدراج سهم الخط فيها  
- انقر فوق القائمة إدراج وانقر فوق الأشكال.  
- ثم، اختر سهم السطر من 'الأشكال المُستخدمة مؤخرًا' أو 'الخطوط'  

![](line_arrow1.png)  

***استخدام Aspose.Cells***  

يمكنك استخدام الطريقة التالية لإدراج سهم خط في ورقة العمل.  

{{% alert color="primary" %}}  
[**ShapeCollection.addLine(number, number, number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/#addLine-number-number-number-number-number-number-)  
 ترجع الطريقة كائن [LineShape](https://reference.aspose.com/cells/javascript-cpp/lineshape).  
{{% /alert %}}  

يوضح المثال التالي كيفية إدراج سهم خطي في ورقة عمل.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Add Line Arrow Example</h1>
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

            // Loads the workbook which contains shapes
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet from the collection
            const sheet = workbook.worksheets.get(0);

            // Add the line arrow to the worksheet
            let s = sheet.shapes.addLine(2, 0, 2, 0, 100, 300); // method 1
            // let s = sheet.shapes.addAutoShape(AsposeCells.AutoShapeType.Line, 2, 0, 2, 0, 100, 300); // method 2
            // let s = sheet.shapes.addShape(AsposeCells.MsoDrawingType.Line, 2, 0, 2, 0, 100, 300); // method 3

            // add a arrow at the line begin
            s.line.beginArrowheadStyle = AsposeCells.MsoArrowheadStyle.Arrow; // arrow type
            s.line.beginArrowheadWidth = AsposeCells.MsoArrowheadWidth.Wide; // arrow width
            s.line.beginArrowheadLength = AsposeCells.MsoArrowheadLength.Short; // arrow length

            // add a arrow at the line end
            s.line.endArrowheadStyle = AsposeCells.MsoArrowheadStyle.ArrowOpen; // arrow type
            s.line.endArrowheadWidth = AsposeCells.MsoArrowheadWidth.Narrow; // arrow width
            s.line.endArrowheadLength = AsposeCells.MsoArrowheadLength.Long; // arrow length

            // Save and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'sample.with_arrow.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File with Arrow';

            document.getElementById('result').innerHTML = '<p style="color: green;">Arrow added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

قم بتنفيذ الكود أعلاه، ستحصل على النتائج التالية:  

![](line_arrow2.png)  

## ** إدراج مستطيل إلى ورقة عمل إكسل باستخدام JavaScript**  

ينتمي شكل المستطيل إلى فئة **المستطيلات**.  

*  

- حدد الخلية التي تريد إدراج المستطيل فيها  
- انقر فوق القائمة إدراج وانقر فوق الأشكال.  
- ثم، اختر المستطيل من 'الأشكال المُستخدمة مؤخرًا' أو 'المستطيلات'  

![](rectangle.png)  

***استخدام Aspose.Cells***  

يمكنك استخدام الطريقة التالية لإدراج مستطيل في ورقة العمل.  

{{% alert color="primary" %}}  
[**ShapeCollection.addRectangle(number, number, number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/#addRectangle-number-number-number-number-number-number-)  
 ترجع الطريقة كائن [RectangleShape](https://reference.aspose.com/cells/javascript-cpp/rectangleshape).  
{{% /alert %}}  

يوضح المثال التالي كيفية إدراج مستطيل في ورقة عمل.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Add Rectangle</title>
    </head>
    <body>
        <h1>Add Rectangle to Worksheet</h1>
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
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Create workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet from the collection
            const sheet = workbook.worksheets.get(0);

            // Add the rectangle to the worksheet
            sheet.shapes.addRectangle(2, 0, 2, 0, 100, 300);

            // Save and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'sample.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Rectangle added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

قم بتنفيذ الكود أعلاه، ستحصل على النتائج التالية:  

![](rectangle2.png)  

## ** إدراج مكعب إلى ورقة عمل إكسل باستخدام JavaScript**  

ينتمي شكل المكعب إلى فئة **الأشكال الأساسية**.  

*  

- حدد الخلية التي تريد إدراج المكعب فيها  
- انقر فوق القائمة إدراج وانقر فوق الأشكال.  
- ثم، اختر المكعب من **الأشكال الأساسية**  

![](cube.png)  

***استخدام Aspose.Cells***  

يمكنك استخدام الطريقة التالية لإدراج مكعب في الورقة العمل.  

{{% alert color="primary" %}}  
[**ShapeCollection.addAutoShape(AutoShapeType, number, number, number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/#addAutoShape-autoshapetype-number-number-number-number-number-number-)  
 ترجع الطريقة كائن [Shape](https://reference.aspose.com/cells/javascript-cpp/shape).  
{{% /alert %}}  

يوضح المثال التالي كيفية إدراج مكعب في ورقة عمل.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Add Cube</title>
    </head>
    <body>
        <h1>Add Cube to Worksheet</h1>
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
            const result = document.getElementById('result');
            if (!fileInput.files.length) {
                result.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet from the collection
            const sheet = workbook.worksheets.get(0);

            // Add the cube to the worksheet
            sheet.shapes.addAutoShape(AsposeCells.AutoShapeType.Cube, 2, 0, 2, 0, 100, 300);

            // Save and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'sample.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            result.innerHTML = '<p style="color: green;">Cube added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

قم بتنفيذ الكود أعلاه، ستحصل على النتائج التالية:  

![](cube2.png)  

## ** إدراج سهم رباعي من نوع Callout إلى ورقة عمل إكسل باستخدام JavaScript**  

ينتمي شكل سهم ناتئ رباعي إلى فئة **السهم الكتلي**.  

*  

- حدد الخلية التي تريد إدراج سهم المربعي الدعوة فيها  
- انقر فوق القائمة إدراج وانقر فوق الأشكال.  
- ثم، اختر سهم ناتئ رباعي من **السهم الكتلي**  

![](callout_quad_arrow.png)  

***استخدام Aspose.Cells***  

يمكنك استخدام الطريقة التالية لإدراج سهم رباعي الاتصال في ورقة العمل.  

{{% alert color="primary" %}}  
[**ShapeCollection.addAutoShape(AutoShapeType, number, number, number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/#addAutoShape-autoshapetype-number-number-number-number-number-number-)  
تُرجع الطريقة كائن [شكل](https://reference.aspose.com/cells/javascript-cpp/shape).  
{{% /alert %}}  

يوضح المثال التالي كيفية إدراج سهم ناتئ رباعي في ورقة عمل.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Add Callout Quad Arrow</title>
    </head>
    <body>
        <h1>Add Callout Quad Arrow Shape</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, AutoShapeType } = AsposeCells;

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

            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            const sheet = workbook.worksheets.get(0);

            sheet.shapes.addAutoShape(AutoShapeType.QuadArrowCallout, 2, 0, 2, 0, 100, 100);

            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'sample.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Shape added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

قم بتنفيذ الكود أعلاه، ستحصل على النتائج التالية:  

![](callout_quad_arrow2.png)  

## **إدراج علامة ضرب في ورقة عمل إكسل باستخدام جافا سكريبت**  

ينتمي شكل علامة الضرب إلى فئة **أشكال المعادلة**.  

*  

- حدد الخلية التي ترغب في إدراج علامة الضرب فيها  
- انقر فوق القائمة إدراج وانقر فوق الأشكال.  
- ثم، اختر علامة الضرب من **أشكال المعادلة**  

![](multiplication_sign.png)  

***استخدام Aspose.Cells***  

يمكنك استخدام الطريقة التالية لإدراج علامة الضرب في ورقة العمل.  

{{% alert color="primary" %}}  
[**ShapeCollection.addAutoShape(AutoShapeType, number, number, number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/#addAutoShape-autoshapetype-number-number-number-number-number-number-)  
تُرجع الطريقة كائن [شكل](https://reference.aspose.com/cells/javascript-cpp/shape).  
{{% /alert %}}  

يوضح المثال التالي كيفية إدراج علامة ضرب في ورقة عمل.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Add Multiply Sign</title>
    </head>
    <body>
        <h1>Add Multiplication Sign to Worksheet</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, AutoShapeType } = AsposeCells;

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

            // Instantiating a Workbook object by opening the Excel file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet from the collection
            const sheet = workbook.worksheets.get(0);

            // Add the multiplication sign to the worksheet
            sheet.shapes.addAutoShape(AsposeCells.AutoShapeType.MathMultiply, 2, 0, 2, 0, 100, 100);

            // Save and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'sample.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Multiplication sign added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

قم بتنفيذ الكود أعلاه، ستحصل على النتائج التالية:  

![](multiplication_sign2.png)  

## **إدراج مستند متعدد في ورقة عمل إكسل باستخدام جافا سكريبت**  

ينتمي شكل المستند المتعدد إلى فئة **مخططات التدفق**.  

*  

- حدد الخلية التي ترغب في إدراج مستند متعدد الوثائق فيها  
- انقر فوق القائمة إدراج وانقر فوق الأشكال.  
- ثم، اختر المستند متعدد من **مخططات التدفق**  

![](multidocument.png)  

***استخدام Aspose.Cells***  

يمكنك استخدام الطريقة التالية لإدراج مستند متعدد الوثائق في ورقة العمل.  

{{% alert color="primary" %}}  
[**ShapeCollection.addAutoShape(AutoShapeType, number, number, number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/#addAutoShape-autoshapetype-number-number-number-number-number-number-)  
تُرجع الطريقة كائن [شكل](https://reference.aspose.com/cells/javascript-cpp/shape).  
{{% /alert %}}  

يوضح المثال التالي كيفية إدراج مستند متعدد في ورقة عمل.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
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
        const { Workbook, SaveFormat, AutoShapeType } = AsposeCells;

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

            // Access first worksheet from the collection
            const sheet = workbook.worksheets.get(0);

            // Add the multidocument to the worksheet
            sheet.shapes.addAutoShape(AutoShapeType.FlowChartMultidocument, 2, 0, 2, 0, 100, 100);

            // Save and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], { type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'sample.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

قم بتنفيذ الكود أعلاه، ستحصل على النتائج التالية:  

![](multidocument2.png)  

## **إدراج نجمة ذات خمسة أضلاع في ورقة عمل إكسل باستخدام جافا سكريبت**  

شكل النجمة ذات الخمس نقاط ينتمي إلى فئة **النجوم والرايات**.  

*  

- حدد الخلية التي ترغب في إدراج النجمة المؤلفة من خمس نقاط فيها  
- انقر فوق القائمة إدراج وانقر فوق الأشكال.  
- ثم، اختر النجمة ذات الخمس نقاط من **النجوم والرايات**  

![](star_5_points.png)  

***استخدام Aspose.Cells***  

يمكنك استخدام الأسلوب التالي لإدراج نجمة ذات خمس نقاط في ورقة العمل.  

{{% alert color="primary" %}}  
[**ShapeCollection.addAutoShape(AutoShapeType, number, number, number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/#addAutoShape-autoshapetype-number-number-number-number-number-number-)  
تُرجع الطريقة كائن [شكل](https://reference.aspose.com/cells/javascript-cpp/shape).  
{{% /alert %}}  

يوضح المثال التالي كيفية إدراج نجمة ذات خمس نقاط في ورقة العمل.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Add Star Shape</title>
    </head>
    <body>
        <h1>Add Five-Pointed Star to Worksheet</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, AutoShapeType } = AsposeCells;

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

            // Instantiate workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const sheet = workbook.worksheets.get(0);

            // Add the Five-pointed star to the worksheet
            sheet.shapes.addAutoShape(AutoShapeType.Star5, 2, 0, 2, 0, 100, 100);

            // Save and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'sample.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Star shape added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

قم بتنفيذ الكود أعلاه، ستحصل على النتائج التالية:  

![](star_5_points2.png)  

## **إدراج فقاعة فكرية سحابية في ورقة عمل إكسل باستخدام جافا سكريبت**  

شكل سحابة فقاعة الفكر ينتمي إلى فئة **التعليقات**.  

*  

- حدد الخلية التي تريد إدراج سحابة الفكر فيها  
- انقر فوق القائمة إدراج وانقر فوق الأشكال.  
- ثم، اختر سحابة فقاعة الفكر من **التعليقات**  

![](thought_bubble_cloud.png)  

***استخدام Aspose.Cells***  

يمكنك استخدام الأسلوب التالي لإدراج سحابة فكرية في ورقة العمل.  

{{% alert color="primary" %}}  
[**ShapeCollection.addAutoShape(AutoShapeType, number, number, number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/#addAutoShape-autoshapetype-number-number-number-number-number-number-)  
تُرجع الطريقة كائن [شكل](https://reference.aspose.com/cells/javascript-cpp/shape).  
{{% /alert %}}  

يوضح المثال التالي كيفية إدراج سحابة فقاعة الفكر في ورقة العمل.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Add Cloud Callout Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, AutoShapeType } = AsposeCells;

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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet from the collection
            const sheet = workbook.worksheets.get(0);

            // Add the thought bubble cloud to the worksheet
            sheet.shapes.addAutoShape(AutoShapeType.CloudCallout, 2, 0, 2, 0, 100, 100);

            // Save and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'sample.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Cloud callout added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

قم بتنفيذ الكود أعلاه، ستحصل على النتائج التالية:  

![](thought_bubble_cloud2.png)  

## **مواضيع متقدمة**  
- [تغيير قيم التعديل للشكل](/cells/ar/javascript-cpp/change-adjustment-values-of-the-shape/)  
- [نسخ الأشكال بين أوراق العمل](/cells/ar/javascript-cpp/copy-shapes-between-worksheets/)  
- [البيانات في شكل غير مبدل](/cells/ar/javascript-cpp/data-in-non-primitive-shape/)  
- [العثور على الموضع المطلق للشكل داخل الورقة العمل](/cells/ar/javascript-cpp/finding-absolute-position-of-shape-inside-the-worksheet/)  
- [الحصول على نقاط الاتصال من الشكل](/cells/ar/javascript-cpp/get-connection-points-from-shape/)  
- [إدارة الضوابط](/cells/ar/javascript-cpp/managing-controls/)  
- [إضافة رموز إلى ورقة العمل](/cells/ar/javascript-cpp/insert-svg-to-excel/)  
- [إدارة كائنات OLE](/cells/ar/javascript-cpp/managing-ole-objects/)  
- [إدارة الصور](/cells/ar/javascript-cpp/managing-pictures/)  
- [إدارة الذكاء الفني](/cells/ar/javascript-cpp/managing-smartart/)  
- [إدارة مربع النص](/cells/ar/javascript-cpp/managing-textbox-of-excel/)  
- [إضافة كلمة WaterArt كعلامة مائية إلى ورقة العمل](/cells/ar/javascript-cpp/add-wordart-watermark-to-worksheet/)  
- [تحديث القيم للأشكال المرتبطة](/cells/ar/javascript-cpp/refresh-values-of-linked-shapes/)  
- [إرسال الشكل إلى الأمام أو الوراء داخل ورقة العمل](/cells/ar/javascript-cpp/send-shape-front-or-back-inside-the-worksheet/)  
- [إدارة خيارات الشكل](/cells/ar/javascript-cpp/managing-shape-options/)  
- [إدارة خيارات نص الشكل](/cells/ar/javascript-cpp/managing-shape-text-options/)  
- [ملحقات الويب - إضافات الأوفيس](/cells/ar/javascript-cpp/web-extensions-office-add-ins/)
