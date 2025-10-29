---
title: إعدادات الحدود
linktitle: إعدادات الحدود
description: كيفية استخدام مكتبة Aspose.Cells في JavaScript عبر C++ لضبط نمط ولون حدود الخلايا. عن طريق ضبط عرض النمط واللون، تحصل على مزيد من التحكم في مظهر الخلايا وظهورها.
keywords: Aspose.Cells، إعدادات حدود الخلية، جافاسكريبت عبر C++، عرض الحد، نمط الحد، لون الحد
type: docs
weight: 40
url: /ar/javascript-cpp/cells-border-settings/
---

## **إضافة حدود إلى الخلايا**

يسمح Microsoft Excel للمستخدمين بتنسيق الخلايا عن طريق إضافة حدود. يعتمد نوع الحد على مكان إضافته. على سبيل المثال، الحد العلوي هو الحد المضاف إلى أعلى موضع من الخلية. يمكن للمستخدمين أيضًا تعديل نمط وخطوط الألوان للحدود.

مع Aspose.Cells for JavaScript عبر C++، يمكن للمطورين إضافة حدود وتخصيص مظهرها بنفس الطريقة المرنة كما في Microsoft Excel.

### **إضافة حدود إلى الخلايا**

توفر مكتبة Aspose.Cells فئة [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) التي تمثل ملف Excel من Microsoft. تحتوي فئة [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) على مجموعة [**worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--) تتيح الوصول إلى كل ورقة عمل في ملف Excel. تمثل ورقة العمل بواسطة فئة [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet). توفر فئة [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) مجموعة [**cells**](https://reference.aspose.com/cells/javascript-cpp/cells). كل عنصر في مجموعة [**cells**](https://reference.aspose.com/cells/javascript-cpp/cells) يمثل كائن من الفئة [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell).

يقدم Aspose.Cells الخاصية [**style**](https://reference.aspose.com/cells/javascript-cpp/cell/#style--) في فئة [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell). يُستخدم [**style**](https://reference.aspose.com/cells/javascript-cpp/cell/#style-style-) لتعيين نمط تنسيق الخلية. توفر فئة [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) خصائص لإضافة حدود للخلايا.

#### **إضافة حدود إلى خلية**

يمكن للمطورين إضافة حدود إلى خلية باستخدام مجموعة [**borders**](https://reference.aspose.com/cells/javascript-cpp/style/#borders--) من كائن [**Style**](https://reference.aspose.com/cells/javascript-cpp/style). يُمرر نوع الحد كفهرس إلى مجموعة [**borders**](https://reference.aspose.com/cells/javascript-cpp/style/#borders--). جميع أنواع الحدود معرفَة مسبقًا في تعداد [**BorderType**](https://reference.aspose.com/cells/javascript-cpp/bordertype).

**تعداد الحدود**

|**أنواع الحدود**|**الوصف**|
| :- | :- |
خط حد فسفلي |BottomBorder||
خط قطري من أعلى اليسار إلى أسفل اليمين |DiagonalDown||
خط قطري من أسفل اليسار إلى أعلى اليمين |DiagonalUp||
خط حد أيسر |LeftBorder||
خط حد أيمن |RightBorder||
خط حد علوي |TopBorder||

تخزن مجموعة [**borders**](https://reference.aspose.com/cells/javascript-cpp/style/#borders--) جميع الحدود. يُمثل كل حد في مجموعة [**borders**](https://reference.aspose.com/cells/javascript-cpp/style/#borders--) بواسطة كائن [**Border**](https://reference.aspose.com/cells/javascript-cpp/border) يوفر خصيتين، [**color**](https://reference.aspose.com/cells/javascript-cpp/border/#color-color-) و[**lineStyle**](https://reference.aspose.com/cells/javascript-cpp/border/#lineStyle-cellbordertype-) لضبط لون الخط ونمط الحد على التوالي.

لتعيين لون خط الحد، اختر لونًا باستخدام تعداد اللون (جزء من جافاسكريبت) وقم بتعيينه لخاصية لون كائن الحد.

يتم ضبط نمط خط الحد عن طريق اختيار نمط خط من تعداد [**CellBorderType**](https://reference.aspose.com/cells/javascript-cpp/cellbordertype).

**تعداد CellBorderType**

|**أنماط الخطوط**|**الوصف**|
| :- | :- |
|DashDot| خط متقطع رفيع
|DashDotDot| خط نقطة متقطعة رفيع
خط متقطع |Dashed||
خط منقط |Dotted||
|Double|خط مزدوج|
|Hair|خط رفيع|
|MediumDashDot|خط متقطع متوسط المتنقل|
|MediumDashDotDot|خط متوسط متقطع بالنقاط|
|MediumDashed|خط متوسط متقطع|
|None|لا يوجد خط|
|Medium|خط متوسط|
|SlantedDashDot|خط مائل متوسط متقطع بالنقاط|
|Thick|خط سميك|
|Thin|خط رفيع|
اختر أحد أنماط الخط ثم قم بتعيينه إلى خاصية [**lineStyle**](https://reference.aspose.com/cells/javascript-cpp/border/#lineStyle-cellbordertype-) لكائن [**Border**](https://reference.aspose.com/cells/javascript-cpp/border).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Add Borders to A1 Cell Example</h1>
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
            // This example creates a new workbook and adds borders to cell A1.
            // No try/catch is used so errors propagate for testing.

            // Instantiating a Workbook object
            const workbook = new Workbook();

            // Obtaining the reference of the first (default) worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(0);

            // Accessing the "A1" cell from the worksheet
            const cell = worksheet.cells.get("A1");

            // Adding some value to the "A1" cell
            cell.value = "Visit Aspose!";

            // Create a style object
            const style = cell.style;

            // Setting the line style and color of the top border
            style.borders.get(AsposeCells.BorderType.TopBorder).lineStyle = AsposeCells.CellBorderType.Thick;
            style.borders.get(AsposeCells.BorderType.TopBorder).color = AsposeCells.Color.Black;

            // Setting the line style and color of the bottom border
            style.borders.get(AsposeCells.BorderType.BottomBorder).lineStyle = AsposeCells.CellBorderType.Thick;
            style.borders.get(AsposeCells.BorderType.BottomBorder).color = AsposeCells.Color.Black;

            // Setting the line style and color of the left border
            style.borders.get(AsposeCells.BorderType.LeftBorder).lineStyle = AsposeCells.CellBorderType.Thick;
            style.borders.get(AsposeCells.BorderType.LeftBorder).color = AsposeCells.Color.Black;

            // Setting the line style and color of the right border
            style.borders.get(AsposeCells.BorderType.RightBorder).lineStyle = AsposeCells.CellBorderType.Thick;
            style.borders.get(AsposeCells.BorderType.RightBorder).color = AsposeCells.Color.Black;

            // Apply the border styles to the cell
            cell.style = style;

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and styled successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

{{% alert color="primary" %}}
يجب تعيين كل من نمط الخط ولونه في نفس الوقت. يجب أن يكون لنظامي الخطوط القطرية نفس النمط واللون.
{{% /alert %}}

#### **إضافة حدود لمجموعة من الخلايا**

من الممكن أيضًا إضافة حدود لنطاق من الخلايا بدلاً من خلية واحدة فقط. للقيام بذلك، أولاً، أنشئ نطاق خلايا عبر استدعاء طريقة [**createRange**](https://reference.aspose.com/cells/javascript-cpp/cells/#createRange-string-string-) لمجموعة [**cells**](https://reference.aspose.com/cells/javascript-cpp/cells). تأخذ المعلمات التالية:

- الصف الأول، الصف الأول من المجموعة.
- العمود الأول، يمثل العمود الأول من المجموعة.
- عدد الصفوف، عدد الصفوف في المجموعة.
- عدد الأعمدة، عدد الأعمدة في المجموعة.

تعيد طريقة [**createRange**](https://reference.aspose.com/cells/javascript-cpp/cells/#createRange-string-string-) كائن [**Range**](https://reference.aspose.com/cells/javascript-cpp/range)، الذي يحتوي على النطاق المحدد من الخلايا. يوفر كائن [**Range**](https://reference.aspose.com/cells/javascript-cpp/range) طريقة [**outlineBorder**](https://reference.aspose.com/cells/javascript-cpp/range/#outlineBorder-bordertype-cellbordertype-cellscolor-) التي تأخذ المعلمات التالية لإضافة حد إلى نطاق الخلايا:

- **نوع الحد**، نوع الحد، مختار من تعداد [**BorderType**](https://reference.aspose.com/cells/javascript-cpp/bordertype).
- **نمط الخط**، نمط خط الحد، مختار من تعداد [**CellBorderType**](https://reference.aspose.com/cells/javascript-cpp/cellbordertype).
- **اللون**، لون الخط، المحدد من تعداد الألوان.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Create Workbook and Apply Borders</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, BorderType, CellBorderType, Color } = AsposeCells;

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
            // This example creates a new workbook, writes to A1, creates a range and applies borders, then offers the file for download.
            const workbook = new Workbook();

            const worksheet = workbook.worksheets.get(0);

            const cell = worksheet.cells.get("A1");

            cell.putValue("Hello World From Aspose");

            const range = worksheet.cells.createRange(0, 0, 1, 3);

            // Applying borders using property assignment conversions for setter methods
            range.outlineBorder = [BorderType.TopBorder, CellBorderType.Thick, Color.Blue];
            range.outlineBorder = [BorderType.BottomBorder, CellBorderType.Thick, Color.Blue];
            range.outlineBorder = [BorderType.LeftBorder, CellBorderType.Thick, Color.Blue];
            range.outlineBorder = [BorderType.RightBorder, CellBorderType.Thick, Color.Blue];

            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and borders applied successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
