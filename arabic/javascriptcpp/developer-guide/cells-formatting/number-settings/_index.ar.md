---
title: إعدادات الأرقام
linktitle: إعدادات الأرقام
description: Aspose.Cells مكتبة جافا سكريبت للعمل مع ملفات الجدول الإلكتروني تدعم العديد من إعدادات أرقام الخلايا. تقدم هذه المقالة كيفية استخدام مكتبة Aspose.Cells لإدارة إعدادات أرقام الخلايا لضبط تنسيقات الأرقام في جداول البيانات.
keywords: Aspose.Cells، مكتبة جافا سكريبت، جدول بيانات إلكتروني، إعدادات أرقام الخلايا، التنسيق، الإدارة، تنسيقات الأرقام والتواريخ
type: docs
weight: 10
url: /ar/javascript-cpp/cells-number-settings/
---

## **كيفية تعيين تنسيقات العرض للأرقام والتواريخ**  

واحدة من أقوى ميزات Microsoft Excel هي السماح للمستخدمين بضبط تنسيقات عرض القيم الرقمية والتواريخ. نعلم أن البيانات الرقمية يمكن استخدامها لتمثيل قيم مختلفة بما في ذلك العشري، العملة، النسبة المئوية، الكسر أو القيم المحاسبية، إلخ. تُعرض جميع هذه القيم الرقمية بتنسيقات مختلفة اعتمادًا على نوع المعلومات التي تمثلها. بالمثل، هناك العديد من التنسيقات التي يمكن عرض التاريخ أو الوقت فيها.  
تدعم أسبوس.خلايا هذه الوظيفة وتسمح للمطورين بتعيين أي تنسيق عرض لرقم أو تاريخ.  

### **كيفية تعيين تنسيقات العرض في مايكروسوفت إكسل**  

لتعيين تنسيقات العرض في مايكروسوفت إكسل:  

1. انقر بزر الماوس الأيمن على أي خلية.  
2. اختر **تنسيق الخلايا**. ستظهر نافذة حوار تُستخدم لضبط تنسيقات عرض أي نوع من القيم.  

على الجانب الأيسر من النافذة، توجد العديد من فئات القيم مثل **عام**، **رقم**، **عملة**، **محاسبة**، **تاريخ**، **وقت**، **نسبة مئوية**، وغيرها. يدعم Aspose.Cells جميع هذه التنسيقات العرضية.  

يقدم Aspose.Cells وحدة، [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) تمثل ملف Excel. تحتوي وحدة [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) على مجموعة [**Worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--) تتيح الوصول إلى كل ورقة عمل في ملف Excel. تمثل ورقة العمل بواسطة وحدة [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet). توفر وحدة [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) مجموعة [**Cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--). يمثل كل عنصر في مجموعة [**Cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--) كائنًا من وحدة [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell).  

 يوفر Aspose.Cells الخاصية [**style**](https://reference.aspose.com/cells/javascript-cpp/cell/#style--) لوحدة [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell). تستخدم هذه الخاصية للحصول على وتعيين تنسيق الخلية. توفر وحدة [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) بعض الخاصيات المفيدة للتعامل مع تنسيقات عرض الأرقام والتواريخ.  

### **كيفية استخدام التنسيقات الرقمية المدمجة**  

 يقدم Aspose.Cells بعض تنسيقات الأرقام المدمجة لضبط تنسيقات عرض الأرقام والتواريخ. يمكن تطبيق هذه التنسيقات المدمجة باستخدام خاصية [**number**](https://reference.aspose.com/cells/javascript-cpp/style/#number-number-) لكائن [**Style**](https://reference.aspose.com/cells/javascript-cpp/style). جميع تنسيقات الأرقام المدمجة معطاة بقيم رقمية فريدة. يمكن للمطورين تعيين أي قيمة رقمية مرغوبة للخاصية [**number**](https://reference.aspose.com/cells/javascript-cpp/style/#number-number-) الخاصة بكائن [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) لتطبيق تنسيق العرض. هذه الطريقة سريعة. تنسيقات الأرقام المدمجة التي يدعمها Aspose.Cells مدرجة أدناه.  

| **القيمة** | **النوع** | **سلسلة التنسيق** |  
| :- | :- | :- |  
|0|General|General|  
|1|Decimal|0|  
|2|Decimal|0.00|  
|3|Decimal|#,##0|  
|4|Decimal|#,##0.00|  
|5|Currency|$#,##0;$-#,##0|  
|6|Currency|$#,##0;[Red]$-#,##0|  
|7|Currency|$#,##0.00;$-#,##0.00|  
|8|Currency|$#,##0.00;[Red]$-#,##0.00|  
|9|Percentage|0%|  
|10|Percentage|0.00%|  
|11|Scientific|0.00E+00|  
|12|Fraction|# ?/?|  
|13|Fraction|# */*|  
|14|Date|m/d/yyyy|  
|15|Date|d-mmm-yy|  
|16|Date|d-mmm|  
|17|Date|mmm-yy|  
|18|Time|h:mm AM/PM|  
|19|Time|h:mm:ss AM/PM|  
|20|Time|h:mm|  
|21|Time|h:mm:ss|  
|22|Time|m/d/yy h:mm|  
|37|Currency|#,##0;-#,##0|  
|38|Currency|#,##0;[Red]-#,##0|  
|39|Currency|#,##0.00;-#,##0.00|  
|40|Currency|#,##0.00;[Red]-#,##0.00|  
|41|Accounting|_ * #,##0_ ;_ * "_ ;_ @_|  
|42|Accounting|_ $* #,##0_ ;_ $* "_ ;_ @_|  
|43|Accounting|_ * #,##0.00_ ;_ * "??_ ;_ @_|  
|44|Accounting|_ $* #,##0.00_ ;_ $* "??_ ;_ @_|  
|45|Time|mm:ss|  
|46|Time|h:mm:ss|  
|47|Time|mm:ss.0|  
|48|Scientific|##0.0E+00|  
|49|Text|@|  


```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Create/Modify Workbook</h1>
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

            // Adding the current system date to "A1" cell
            const cellA1 = worksheet.cells.get("A1");
            cellA1.value = new Date();

            // Getting the Style of the A1 Cell
            let style = cellA1.style;

            // Setting the display format to number 15 to show date as "d-mmm-yy"
            style.number = 15;

            // Applying the style to the A1 cell
            cellA1.style = style;

            // Adding a numeric value to "A2" cell
            const cellA2 = worksheet.cells.get("A2");
            cellA2.value = 20;

            // Getting the Style of the A2 Cell
            style = cellA2.style;

            // Setting the display format to number 9 to show value as percentage
            style.number = 9;

            // Applying the style to the A2 cell
            cellA2.style = style;

            // Adding a numeric value to "A3" cell
            const cellA3 = worksheet.cells.get("A3");
            cellA3.value = 2546;

            // Getting the Style of the A3 Cell
            style = cellA3.style;

            // Setting the display format to number 6 to show value as currency
            style.number = 6;

            // Applying the style to the A3 cell
            cellA3.style = style;

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook processed successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```  


### **كيفية استخدام التنسيقات الرقمية المخصصة**  

 لتحديد صيغة تنسيق مخصصة خاصة بك لضبط تنسيق العرض، استخدم خاصية [**custom**](https://reference.aspose.com/cells/javascript-cpp/style/#custom-string-) لكائن [**Style**](https://reference.aspose.com/cells/javascript-cpp/style). هذه الطريقة ليست بسرعة استخدام التنسيقات المسبقة ولكنها أكثر مرونة.  

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

            // Instantiate or open workbook depending on whether a file is provided
            let workbook;
            if (fileInput.files && fileInput.files.length > 0) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Obtaining the reference of the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Adding the current system date to "A1" cell
            const cellA1 = worksheet.cells.get("A1");
            cellA1.putValue(new Date());

            // Getting the Style of the A1 Cell
            let style = cellA1.style;

            // Setting the display format to number 15 to show date as "d-mmm-yy"
            style.number = 15;

            // Applying the style to the A1 cell
            cellA1.style = style;

            // Adding a numeric value to "A2" cell
            const cellA2 = worksheet.cells.get("A2");
            cellA2.putValue(20);

            // Getting the Style of the A2 Cell
            style = cellA2.style;

            // Setting the display format to number 9 to show value as percentage
            style.number = 9;

            // Applying the style to the A2 cell
            cellA2.style = style;

            // Adding a numeric value to "A3" cell
            const cellA3 = worksheet.cells.get("A3");
            cellA3.putValue(2546);

            // Getting the Style of the A3 Cell
            style = cellA3.style;

            // Setting the display format to number 6 to show value as currency
            style.number = 6;

            // Applying the style to the A3 cell
            cellA3.style = style;

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  


{{% alert color="primary" %}}  

 إذا استخدمت الخاصية [**custom**](https://reference.aspose.com/cells/javascript-cpp/style/#custom-string-) لضبط تنسيق الرقم، فسيتم تجاوز أي تنسيق سابق تم تعيينه باستخدام الخاصية [**number**](https://reference.aspose.com/cells/javascript-cpp/style/#number-number-) والعكس صحيح.  

{{% /alert %}}  

## **مواضيع متقدمة**  
- [تحقق من تنسيق الأرقام المخصص عند تعيين خاصية Style.Custom](/cells/ar/javascript-cpp/check-custom-number-format-when-setting-style-custom-property/)  
- [قائمة التنسيقات الرقمية المدعومة](/cells/ar/javascript-cpp/list-of-supported-number-formats/)  
- [عرض نمط التاريخ المخصص g وge mm dd](/cells/ar/javascript-cpp/render-custom-date-format-pattern-g-and-ge-mm-dd/)  
- [تحديد فواصل العدد العشري المخصصة وفواصل المجموعة لسجل العمل](/cells/ar/javascript-cpp/specify-custom-number-decimal-and-group-separators-for-workbook/)  
- [تحديد تنسيق نمط DBNum المخصص](/cells/ar/javascript-cpp/specifying-dbnum-custom-pattern-formatting/)
