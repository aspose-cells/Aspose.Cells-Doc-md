---
title: إدارة كائنات OLE باستخدام جافا سكريبت عبر C++
linktitle: إدارة كائنات OLE
type: docs
weight: 50
url: /ar/javascript-cpp/managing-ole-objects/
description: تعرف على كيفية إدارة كائنات OLE في Aspose.Cells for JavaScript عبر C++. إضافة، استخراج، والتعامل مع كائنات OLE داخل أوراق العمل.
---

## **مقدمة**  

OLE (الربط والدمج بالكائنات) هو إطار عمل لتقنية المستندات المركبة. باختصار، المستند المركب هو شيء مثل سطح مكتبي يمكن أن يحتوي على الكائنات المرئية والمعلوماتية من جميع الأنواع: النصوص، التقاويم، الرسوم المتحركة، الصوت، الفيديو الحركي، 3D، الأخبار المحدثة باستمرار، عناصر التحكم، وهكذا. كل كائن سطح مكتبي هو كيان برنامج مستقل يمكنه التفاعل مع المستخدم والتواصل مع الكيانات الأخرى على سطح المكتب.  

يدعم الكثير من البرامج نظام OLE ويستخدم لجعل المحتوى الذي تم إنشاؤه في برنامج واحد متاحًا في آخر. على سبيل المثال، يمكنك إدراج مستند Microsoft Word في Microsoft Excel. لمعرفة أنواع المحتوى التي يمكنك إدراجها، انقر على **الكائن** في قائمة **إدراج**. تظهر البرامج المثبتة على الكمبيوتر والتي تدعم كائنات OLE في مربع **نوع الكائن**.  

### **إدراج كائنات OLE في ورقة العمل**  

يدعم Aspose.Cells for JavaScript عبر C++ إضافة، استخراج، والتعامل مع كائنات OLE في أوراق العمل. لهذا السبب، تحتوي فئة [**OleObjectCollection**](https://reference.aspose.com/cells/javascript-cpp/oleobjectcollection) على Aspose.Cells، والتي تُستخدم لإضافة كائن OLE جديد إلى المجموعة. فئة أخرى، [**OleObject**](https://reference.aspose.com/cells/javascript-cpp/oleobject)، تمثل كائن OLE. لديها بعض الأعضاء المهمة:  

- تحدد الخاصية [**imageData**](https://reference.aspose.com/cells/javascript-cpp/oleobject/#imageData--) بيانات الصورة (الأيقونة) من نوع مصفوفة البايت. سيتم عرض الصورة لعرض كائن OLE في ورقة العمل.  
- تحدد الخاصية [**objectData**](https://reference.aspose.com/cells/javascript-cpp/oleobject/#objectData--) بيانات الكائن على شكل مصفوفة البايت. سيتم عرض هذه البيانات في البرنامج المعني عند النقر المزدوج على أيقونة كائن OLE.  

المثال التالي يوضح كيفية إضافة كائنات OLE إلى ورقة العمل.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Add OLE Object Example</title>
    </head>
    <body>
        <h1>Add OLE Object Example</h1>
        <p>
            Select an image to display for the OLE object (e.g., logo.jpg) and a file to embed into the OLE object (e.g., book1.xls).
        </p>
        <label>Image (for OLE display): <input type="file" id="imageInput" accept="image/*" /></label>
        <br/>
        <label>Object to embed (e.g., .xls): <input type="file" id="objectInput" accept=".xls,.xlsx,.doc,.docx,.pdf" /></label>
        <br/>
        <button id="runExample">Add OLE Object and Save</button>
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
            const imageInput = document.getElementById('imageInput');
            const objectInput = document.getElementById('objectInput');
            const resultDiv = document.getElementById('result');

            if (!imageInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an image file for the OLE display.</p>';
                return;
            }
            if (!objectInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select a file to embed into the OLE object.</p>';
                return;
            }

            // Read files
            const imageFile = imageInput.files[0];
            const objectFile = objectInput.files[0];

            const imageBuffer = await imageFile.arrayBuffer();
            const objectBuffer = await objectFile.arrayBuffer();

            // Instantiate a new Workbook.
            const workbook = new Workbook();

            // Get the first worksheet.
            const sheet = workbook.worksheets.get(0);

            // Add an Ole object into the worksheet with the image shown in MS Excel.
            // Position: row 14, column 3, width 200, height 220 (same as JavaScript example)
            sheet.oleObjects.add(14, 3, 200, 220, new Uint8Array(imageBuffer));

            // Set embedded ole object data (converted setter to property assignment)
            sheet.oleObjects.get(0).objectData = new Uint8Array(objectBuffer);

            // Save the excel file (Excel97To2003 format to match .xls)
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">OLE object added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

### **استخراج كائنات OLE في الدفتر**  

المثال التالي يوضح كيفية استخراج كائنات OLE في كتاب العمل. يقوم المثال بالحصول على كائنات OLE مختلفة من ملف XLS موجود ويحفظ ملفات مختلفة (DOC، XLS، PPT، PDF، إلخ) استنادًا إلى نوع تنسيق ملف كائن OLE.  

بعد تشغيل الكود، يمكننا حفظ ملفات مختلفة استنادًا إلى أنواع تنسيق كائنات OLE الخاصة بها.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Extract OLE Objects</title>
    </head>
    <body>
        <h1>Extract OLE Objects from Excel</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.xlsb" />
        <button id="runExample">Extract OLE Objects</button>
        <div id="downloadContainer"></div>
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
            const downloadContainer = document.getElementById('downloadContainer');
            const result = document.getElementById('result');
            downloadContainer.innerHTML = '';
            result.innerHTML = '';

            if (!fileInput.files.length) {
                result.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the OleObject Collection in the first worksheet.
            const worksheet = workbook.worksheets.get(0);
            const oles = worksheet.oleObjects;

            // Loop through all the oleobjects and extract each object.
            for (let i = 0; i < oles.count; i++) {
                const ole = oles.get(i);

                // Specify the output filename.
                let ext = 'jpg';

                // Specify each file format based on the oleobject format type.
                switch (ole.fileFormatType) {
                    case AsposeCells.FileFormatType.Doc:
                        ext = "doc";
                        break;
                    case AsposeCells.FileFormatType.Xlsx:
                        ext = "xlsx";
                        break;
                    case AsposeCells.FileFormatType.Ppt:
                        ext = "ppt";
                        break;
                    case AsposeCells.FileFormatType.Pdf:
                        ext = "pdf";
                        break;
                    case AsposeCells.FileFormatType.Unknown:
                        ext = "jpg";
                        break;
                    default:
                        ext = "bin";
                        break;
                }

                const fileName = `ole_${i}.${ext}`;

                // Save the oleobject as a new excel file if the object type is xlsx.
                if (ole.fileFormatType === AsposeCells.FileFormatType.Xlsx) {
                    const ms = new Uint8Array(ole.objectData);
                    const oleBook = new Workbook(ms);
                    oleBook.settings.isHidden = false;
                    const outputData = oleBook.save(SaveFormat.Xlsx);
                    const blob = new Blob([outputData]);
                    const link = document.createElement('a');
                    link.href = URL.createObjectURL(blob);
                    link.download = `Excel_File${i}.out.xlsx`;
                    link.textContent = `Download Excel_File${i}.out.xlsx`;
                    link.style.display = 'block';
                    downloadContainer.appendChild(link);
                } else {
                    // Create the files based on the oleobject format types.
                    const data = ole.objectData;
                    const blob = new Blob([data]);
                    const link = document.createElement('a');
                    link.href = URL.createObjectURL(blob);
                    link.download = fileName;
                    link.textContent = `Download ${fileName}`;
                    link.style.display = 'block';
                    downloadContainer.appendChild(link);
                }
            }

            result.innerHTML = '<p style="color: green;">OLE object extraction completed. Use the links above to download the files.</p>';
        });
    </script>
</html>
```  

### **استخراج ملف MOL المضمن**  

 يدعم Aspose.Cells for JavaScript عبر C++ استخراج كائنات من أنواع غير مألوفة مثل MOL (ملف بيانات جزيئية يحتوي على معلومات عن الذرات والروابط). يوضح مقتطف الشفرة التالي كيفية استخراج ملف MOL مدمج وحفظه على القرص باستخدام هذا [ملف إكسل نموذجي](94896196.xlsx).  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Extract OLE Objects Example</title>
    </head>
    <body>
        <h1>Extract OLE Objects Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));
            let index = 1;

            const worksheets = workbook.worksheets;
            const sheetCount = worksheets.count;
            const resultDiv = document.getElementById('result');
            resultDiv.innerHTML = '';

            for (let i = 0; i < sheetCount; i++) {
                const sheet = worksheets.get(i);
                const oles = sheet.oleObjects;
                const oleCount = oles.count;
                for (let j = 0; j < oleCount; j++) {
                    const ole = oles.get(j);
                    const data = ole.objectData;
                    const blob = new Blob([data], { type: 'application/octet-stream' });
                    const url = URL.createObjectURL(blob);
                    const fileName = `OleObject${index}.mol`;
                    const link = document.createElement('a');
                    link.href = url;
                    link.download = fileName;
                    link.textContent = `Download ${fileName}`;
                    link.style.display = 'block';
                    resultDiv.appendChild(link);
                    index++;
                }
            }

            if (!resultDiv.hasChildNodes()) {
                resultDiv.innerHTML = '<p>No OLE objects found in the workbook.</p>';
            } else {
                const info = document.createElement('p');
                info.style.color = 'green';
                info.textContent = 'OLE objects extracted. Click the links to download the extracted .mol files.';
                resultDiv.insertBefore(info, resultDiv.firstChild);
            }
        });
    </script>
</html>
```  

## **مواضيع متقدمة**  
- [الوصول إلى وتعديل التسمية العرضية لكائن Ole المرتبط](/cells/ar/javascript-cpp/access-and-modify-the-display-label-of-the-linked-ole-object/)  
- [تحديث كائن Ole تلقائيًا عبر Microsoft Excel باستخدام Aspose.Cells](/cells/ar/javascript-cpp/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/)  
- [استخراج كائنات OLE من كتاب العمل](/cells/ar/javascript-cpp/extract-ole-objects-from-workbook/)  
- [الحصول على معرف الفئة الخاص بكائن OLE المضمّن أو تعيينه](/cells/ar/javascript-cpp/get-or-set-the-class-identifier-of-the-embedded-ole-object/)  
- [إدراج ملف WAV ككائن Ole](/cells/ar/javascript-cpp/inserting-a-wav-file-as-an-ole-object/)
