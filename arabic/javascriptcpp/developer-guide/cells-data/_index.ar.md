---
title: إدارة بيانات ملفات إكسل
linktitle: بيانات الخلايا
type: docs
weight: 110
url: /ar/javascript-cpp/view-and-edit-excel-data/
description: تصف هذه المقالة كيف يمكن عرض وتعديل بيانات ملفات Excel باستخدام مكتبة Aspose.Cells لـ JavaScript عبر C++.
keywords: إدارة بيانات ملف Excel باستخدام Aspose.Cells JavaScript عبر C++، إضافة بيانات إلى ملف Excel، الحصول على بيانات من ملف Excel، كيفية تحسين كفاءة إضافة البيانات، إدارة بيانات الخلايا، تحديث بيانات الخلايا، الحصول على بيانات الخلايا، إدراج بيانات الخلايا
---

{{% alert color="primary" %}}

في [الوصول إلى خلايا ورقة العمل](/cells/ar/javascript-cpp/accessing-cells-of-a-worksheet/)، ناقشنا الطرق الأساسية للوصول إلى خلايا في ورقة العمل. تستخدم هذه المقالة واحدة من تلك الطرق لإضافة أنواع مختلفة من البيانات إلى الخلايا.

{{% /alert %}}

## **كيفية إضافة بيانات إلى الخلايا**

Aspose.Cells for Java ينفذ عبر C++ يوفر فئة، [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)، تمثل ملف Microsoft Excel. تحتوي فئة [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) على مجموعة [**worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--) تتيح الوصول إلى كل ورقة عمل في ملف Excel. تمثل ورقة العمل بواسطة فئة [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet). تقدم فئة [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) مجموعة [**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--). كل عنصر في مجموعة [**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--) يمثل كائنًا من فئة [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell). 

يسمح Aspose.Cells للمطورين بإضافة البيانات إلى خلايا ورقة العمل من خلال استدعاء طريقة [**putValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#putValue-boolean-) من فئة [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell). توفر Aspose.Cells نسخ تحميل متراكبة من طريقة [**putValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#putValue-boolean-) التي تتيح للمطورين إضافة أنواع مختلفة من البيانات إلى الخلايا. باستخدام هذه النسخ التحميلية من طريقة [**putValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#putValue-boolean-)، من الممكن إضافة قيمة Boolean، سلسلة، Double، عدد صحيح، أو تاريخ/وقت، وغيرها إلى الخلية.

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
            // If a file is provided, open it; otherwise create a new workbook
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Obtaining the reference of the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Adding values to cells
            const cells = worksheet.cells;
            const cellA1 = cells.get("A1");
            cellA1.value = "Hello World";

            const cellA2 = cells.get("A2");
            cellA2.value = 20.5;

            const cellA3 = cells.get("A3");
            cellA3.value = 15;

            const cellA4 = cells.get("A4");
            cellA4.value = true;

            const cellA5 = cells.get("A5");
            cellA5.value = new Date();

            // Setting the display format of the date
            let style = cellA5.style;
            style.number = 15;
            cellA5.style = style;

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created/modified successfully. Click the download link to get the file.</p>';
        });
    </script>
</html>
```


## **كيفية تحسين الكفاءة**

إذا كنت تستخدم طريقة [**putValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#putValue-boolean-) لوضع كمية كبيرة من البيانات في ورقة العمل، فعليك إضافة القيم إلى الخلايا، أولاً عن طريق الصف ثم العمود. هذا النهج يحسن بشكل كبير من كفاءة تطبيقاتك.

## **كيفية استرداد البيانات من الخلايا**

8667720447سكربت عبر C++ يوفر فئة، [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) التي تمثل ملف إكسل من مايكروسوفت. تحتوي فئة [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) على مجموعة [**worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--) التي تتيح الوصول إلى أوراق العمل في الملف. يتم تمثيل ورقة العمل بواسطة فئة [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet). توفر فئة [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) مجموعة [**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--). كل عنصر في مجموعة [**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--) يمثل كائن من فئة [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell).

توفر فئة [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell) العديد من الخصائص التي تسمح للمطورين باسترجاع القيم من الخلايا وفقًا لأنواع بياناتها. تشمل هذه الخصائص:

- [**stringValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#stringValue--): يُرجع القيمة النصية للخلية.
- [**doubleValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#doubleValue--): يُرجع القيمة المزدوجة للخلية.
- [**boolValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#boolValue--): يُرجع القيمة المنطقية للخلية.
- [**dateTimeValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#dateTimeValue--): يُرجع قيمة التاريخ/الوقت للخلية.
- [**floatValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#floatValue--): يُرجع القيمة العائمة للخلية.
- [**intValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#intValue--): يُرجع القيمة الصحيحة للخلية.

عندما لا يتم ملء حقل، ترمي الخلايا التي تحتوي على [**doubleValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#doubleValue--) أو [**floatValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#floatValue--) استثناء.

يمكن أيضًا فحص نوع البيانات المحتواة في الخلية باستخدام طريقة [**type**](https://reference.aspose.com/cells/javascript-cpp/cell/#type--) من فئة [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell). في الواقع، تعتمد طريقة [**type**](https://reference.aspose.com/cells/javascript-cpp/cell/#type--) من فئة [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell) على تعداد [**CellValueType**](https://reference.aspose.com/cells/javascript-cpp/cellvaluetype) الذي يتم سرد القيم المعرفة مسبقًا أدناه:

|**أنواع قيم الخلية**|**الوصف**|
| :- | :- |
|IsBool| يحدد أن قيمة الخلية هي بولية.
|IsDateTime| يحدد أن قيمة الخلية هي تاريخ/وقت.
|IsNull| تمثل خلية فارغة.
|IsNumeric| يحدد أن قيمة الخلية هي رقمية.
|IsString| يحدد أن قيمة الخلية هي نصية.
|IsUnknown| يحدد أن قيمة الخلية غير معروفة.

يمكنك أيضًا استخدام أنواع القيم الخلوية المعرفة مسبقًا المذكورة أعلاه للمقارنة مع نوع البيانات الموجودة في كل خلية.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Read Cell Values Example</h1>
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
        });

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Opening an existing workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing first worksheet
            const worksheet = workbook.worksheets.get(0);

            var cells = worksheet.cells;
            var maxRow = cells.maxRow;
            var maxColumn = cells.maxColumn;
            let logs = [];
            for (let i = 0; i <= maxRow; i++) {
                for (let j = 0; j <= maxColumn; j++) 
                {
                    const cell1 = cells.get(i, j);
                    if (!cell1) {
                        continue;
                    }
                    // Variables to store values of different data types
                    let stringValue;
                    let doubleValue;
                    let boolValue;
                    let dateTimeValue;

                    // Passing the type of the data contained in the cell for evaluation
                    switch (cell1.type) {
                        // Evaluating the data type of the cell data for string value
                        case AsposeCells.CellValueType.IsString:
                            stringValue = cell1.stringValue;
                            console.log("String Value: " + stringValue);
                            logs.push("String Value: " + stringValue);
                            break;

                        // Evaluating the data type of the cell data for double value
                        case AsposeCells.CellValueType.IsNumeric:
                            doubleValue = cell1.doubleValue;
                            console.log("Double Value: " + doubleValue);
                            logs.push("Double Value: " + doubleValue);
                            break;

                        // Evaluating the data type of the cell data for boolean value
                        case AsposeCells.CellValueType.IsBool:
                            boolValue = cell1.boolValue;
                            console.log("Bool Value: " + boolValue);
                            logs.push("Bool Value: " + boolValue);
                            break;

                        // Evaluating the data type of the cell data for date/time value
                        case AsposeCells.CellValueType.IsDateTime:
                            dateTimeValue = cell1.dateTimeValue;
                            console.log("DateTime Value: " + dateTimeValue);
                            logs.push("DateTime Value: " + dateTimeValue);
                            break;

                        // Evaluating the unknown data type of the cell data
                        case AsposeCells.CellValueType.IsUnknown:
                            stringValue = cell1.stringValue;
                            console.log("Unknown Value: " + stringValue);
                            logs.push("Unknown Value: " + stringValue);
                            break;

                        // Terminating the type checking of type of the cell data is null
                        case AsposeCells.CellValueType.IsNull:
                            break;
                    }
                }
            }

            document.getElementById('result').innerHTML = `<p style="color: green;">Operation completed successfully! See console for detailed cell values.</p><pre>${logs.join("\n")}</pre>`;
        });
    </script>
</html>
```


{{% alert color="primary" %}}

أثناء العمل على ورقة العمل، قد يضيف المستخدمون أنواعًا مختلفة من البيانات في الخلايا. قد تتضمن هذه البيانات Boolean، عدد صحيح، نقطة عائمة، نص، أو قيم تاريخ/وقت. مع Aspose.Cells، يمكنك الحصول على القيم المناسبة من الخلايا وفقًا لأنواع البيانات.

{{% /alert %}}

## **مواضيع متقدمة**
- [الوصول إلى الخلايا في ورقة العمل](/cells/ar/javascript-cpp/accessing-cells-of-a-worksheet/)
- [تحويل بيانات النص الرقمية إلى رقم](/cells/ar/javascript-cpp/convert-text-numeric-data-to-number/)
- [إنشاء المجاميع الفرعية](/cells/ar/javascript-cpp/creating-subtotals/)
- [تصفية البيانات](/cells/ar/javascript-cpp/data-filtering/)
- [فرز البيانات](/cells/ar/javascript-cpp/sort-data-of-excel/)
- [التحقق من البيانات](/cells/ar/javascript-cpp/data-validation/)
- [العثور على البيانات أو البحث](/cells/ar/javascript-cpp/find-or-search-data/)
- [الحصول على قيمة سلسلة الخلية بتنسيق وبدون تنسيق](/cells/ar/javascript-cpp/get-cell-string-value-with-and-without-formatting/)
- [إضافة نص فائق النص الغني HTML داخل الخلية](/cells/ar/javascript-cpp/adding-html-rich-text-inside-the-cell/)
- [إدراج الروابط التشعبية في إكسل أو أوبن أوفيس](/cells/ar/javascript-cpp/insert-hyperlinks-to-excel/)
- [كيفية استخدام العدادات وأين استخدامها](/cells/ar/javascript-cpp/how-and-where-to-use-enumerators/)
- [قياس عرض وارتفاع قيمة الخلية بوحدة البكسل](/cells/ar/javascript-cpp/calculate-the-width-and-height-of-the-cell-value-in-unit-of-pixels/)
- [قراءة قيم الخلية في مواضيع متعددة بشكل متزامن](/cells/ar/javascript-cpp/reading-cell-values-in-multiple-threads-simultaneously/)
- [التحويل بين اسم الخلية وفهرس الصف/العمود](/cells/ar/javascript-cpp/names-and-indices/)
- [ملء البيانات أولاً حسب الصف ثم حسب العمود](/cells/ar/javascript-cpp/populate-data-first-by-row-then-by-column/)
- [الحفاظ على بادئة اقتباس واحدة لقيمة الخلية أو النطاق](/cells/ar/javascript-cpp/preserve-single-quote-prefix-of-cell-value-or-range/)
- [الوصول إلى وتحديث أجزاء النص الغني للخلية](/cells/ar/javascript-cpp/access-and-update-the-portions-of-rich-text-of-cell/)
