---
title: إنشاء المجاميع الفرعية
type: docs
weight: 800
url: /ar/javascript-cpp/creating-subtotals/
description: تعلم كيفية إنشاء مجاميع فرعية لأي قيم مكررة في جدول بيانات باستخدام واجهة برمجة تطبيقات Aspose.Cells for Javaسكريبت عبر C++.
keywords: تطبيق المجاميع الفرعية، تعيين المجاميع الفرعية، إضافة المجاميع الفرعية، إنشاء المجاميع الفرعية، كيفية إضافة مجاميع فرعية لجدول بيانات 
---

{{% alert color="primary" %}}

يمكنك تلقائيًا إنشاء مجاميع فرعية لأي قيم مكررة في جدول بيانات. يوفر Aspose.Cells for Javaسكريبت عبر C++ ميزات واجهة برمجة التطبيقات التي تساعدك على إضافة المجاميع الفرعية إلى جداول البيانات برمجياً.

{{% /alert %}}

## **استخدام Microsoft Excel**

لإضافة المجاميع الفرعية في Microsoft Excel:

1. إنشاء قائمة بيانات بسيطة في الورقة العمل الأولى من المفكرة (كما هو مبين في الشكل أدناه) وحفظ الملف كـ Book1.xls.
1. حدد أي خلية ضمن قائمتك.
1. من قائمة **البيانات**, حدد **المجاميع الفرعية**. سيتم عرض مربع حوار المجاميع الفرعية. حدد الوظيفة المطلوب استخدامها ومكان وضع المجاميع الفرعية.

## **باستخدام واجهة برمجة تطبيقات Aspose.Cells for Javaسكريبت عبر C++**

يقدم Aspose.Cells for Javaسكريبت عبر C++ فئة، [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)، تمثل ملف إكسل من مايكروسوفت. تحتوي فئة [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) على مجموعة [**worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--) التي تتيح الوصول إلى كل ورقة عمل في ملف إكسل.

تمثل ورقة العمل بالفئة [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet). توفر الفئة مجموعة واسعة من الخصائص والطرق لإدارة الأوراق والأشياء الأخرى. تتكون كل ورقة عمل من مجموعة [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells). لإضافة مجاميع فرعية إلى ورقة عمل، استخدم طريقة [**subtotal**](https://reference.aspose.com/cells/javascript-cpp/cells/#subtotal-cellarea-number-consolidationfunction-numberarray-) لفئة [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells). قدم قيم المعاملات للطريقة لتحديد كيفية حساب المجاميع ومكانها.

في الأمثلة أدناه، أضفنا المجاميع الفرعية للورقة الأولى في [ملف النموذج](book1.xlsx) باستخدام واجهة برمجة تطبيقات Aspose.Cells for Javaسكريبت عبر C++. عند تنفيذ الشفرة، يتم إنشاء ورقة عمل بها مجاميع فرعية.

توضح مقتطفات الشفرة التالية كيفية إضافة مجاميع فرعية إلى ورقة عمل باستخدام Aspose.Cells for Javaسكريبت عبر C++.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Apply Subtotal Example</h1>
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

            // Instantiate a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the Cells collection in the first worksheet
            const worksheet = workbook.worksheets.get(0);
            const cells = worksheet.cells;

            // Create a cellarea i.e., B3:C19
            const ca = new AsposeCells.CellArea();
            ca.startRow = 2;
            ca.startColumn = 1;
            ca.endRow = 18;
            ca.endColumn = 2;

            // Apply subtotal, the consolidation function is Sum and it will be applied to
            // Second column (C) in the list
            cells.subtotal(ca, 0, AsposeCells.ConsolidationFunction.Sum, [1]);

            // Save the excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Subtotal applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
