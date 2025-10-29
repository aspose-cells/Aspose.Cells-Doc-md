---
title: استخدام فئة GlobalizationSettings لعلامات الإجمالي الفرعي المخصصة وعلامات أخرى للمخطط الدائري باستخدام JavaScript عبر C++
linktitle: استخدام فئة GlobalizationSettings لتخصيص علامات مجموع جزئي مخصصة وعلامة أخرى لمخطط البيت
type: docs
weight: 70
url: /ar/javascript-cpp/using-globalizationsettings-class-for-custom-subtotal-labels-and-other-label-of-pie-chart/
description: تعلم كيفية تخصيص علامات الإجمالي الفرعي والعلامات الأخرى للمخططات الدائرية باستخدام فئة GlobalizationSettings في Aspose.Cells for JavaScript عبر C++.
---

## **سيناريوهات الاستخدام المحتملة**

 قدمت واجهات برمجة التطبيقات Aspose.Cells فئة [**GlobalizationSettings**](https://reference.aspose.com/cells/javascript-cpp/globalizationsettings) للتعامل مع السيناريوهات التي يرغب فيها المستخدم في استخدام تسميات مخصصة للمجاميع الفرعية في جدول البيانات. علاوة على ذلك، يمكن أيضًا استخدام فئة [**GlobalizationSettings**](https://reference.aspose.com/cells/javascript-cpp/globalizationsettings) لتعديل تسمية **Other** لرسوم بيانية الفطيرة عند عرض الورقة أو الرسم.

## **مقدمة في فئة GlobalizationSettings**

 تقدم فئة [**GlobalizationSettings**](https://reference.aspose.com/cells/javascript-cpp/globalizationsettings) حاليًا الطرق الثلاثة التالية التي يمكن تجاوزها في فئة مخصصة للحصول على التسميات المطلوبة للمجاميع الفرعية أو لعرض نص مخصص لتسمية **Other** في رسم فطيرة.

1. [**GlobalizationSettings.totalName(ConsolidationFunction)**](https://reference.aspose.com/cells/javascript-cpp/globalizationsettings/#totalName-consolidationfunction-): يحصل على الاسم الكامل للوظيفة.
1. [**GlobalizationSettings.grandTotalName(ConsolidationFunction)**](https://reference.aspose.com/cells/javascript-cpp/globalizationsettings/#grandTotalName-consolidationfunction-): يستلم اسم المجموع الكلي للوظيفة.


### **علامات مخصصة للمجاميع الجزئية**

 يمكن استخدام فئة [**GlobalizationSettings**](https://reference.aspose.com/cells/javascript-cpp/globalizationsettings) لتخصيص تسميات المجموع الفرعي من خلال تجاوز الطرق [**GlobalizationSettings.totalName(ConsolidationFunction)**](https://reference.aspose.com/cells/javascript-cpp/globalizationsettings/#totalName-consolidationfunction-) و [**GlobalizationSettings.grandTotalName(ConsolidationFunction)**](https://reference.aspose.com/cells/javascript-cpp/globalizationsettings/#grandTotalName-consolidationfunction-) كما هو موضح أدناه.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Custom GlobalizationSettings Example</title>
    </head>
    <body>
        <h1>Custom GlobalizationSettings Example</h1>
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

        // Defines a custom class derived from GlobalizationSettings class
        class CustomSettings extends AsposeCells.GlobalizationSettings {
            // Overrides the totalName method (converted from getTotalName)
            totalName(functionType) {
                switch (functionType) {
                    case AsposeCells.ConsolidationFunction.Average:
                        return "AVG";
                    default:
                        return super.totalName(functionType);
                }
            }

            // Overrides the grandTotalName method (converted from getGrandTotalName)
            grandTotalName(functionType) {
                switch (functionType) {
                    case AsposeCells.ConsolidationFunction.Average:
                        return "GRD AVG";
                    default:
                        return super.grandTotalName(functionType);
                }
            }
        }

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            // Read the selected file and process with Aspose.Cells
            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate a Workbook object from the file bytes
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Create and assign the custom globalization settings to the workbook
            const customSettings = new CustomSettings();
            workbook.globalizationSettings = customSettings;

            // Save the workbook and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Custom globalization settings applied. Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

 من أجل إدخال تسميات مخصصة، من الضروري تعيين الخاصية [**WorkbookSettings.globalizationSettings**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#globalizationSettings--) إلى مثيل من فئة **CustomSettings** المعرفة أعلاه قبل إضافة المجاميع الفرعية إلى الورقة.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Subtotal with Custom Globalization Settings</h1>
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

        // Defines a custom class derived from GlobalizationSettings class
        class CustomSettings extends AsposeCells.GlobalizationSettings {
            // Overrides the TotalName method (converted from getTotalName)
            totalName(functionType) {
                // Checks the function type used to add the subtotals
                switch (functionType) {
                    // Returns custom value based on the function type used to add the subtotals
                    case AsposeCells.ConsolidationFunction.Average:
                        return "AVG";
                    // Handle other cases as per requirement
                    default:
                        return super.totalName(functionType);
                }
            }

            // Overrides the GrandTotalName method (converted from getGrandTotalName)
            grandTotalName(functionType) {
                // Checks the function type used to add the subtotals
                switch (functionType) {
                    // Returns custom value based on the function type used to add the subtotals
                    case AsposeCells.ConsolidationFunction.Average:
                        return "GRD AVG";
                    // Handle other cases as per requirement
                    default:
                        return super.grandTotalName(functionType);
                }
            }
        }

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

            // Assigns the GlobalizationSettings property of the WorkbookSettings class to a custom class created
            workbook.settings.globalizationSettings = new CustomSettings();

            // Accesses the 1st worksheet from the collection which contains data that resides in the cell range A2:B9
            const sheet = workbook.worksheets.get(0);

            // Adds Subtotal of type Average to the worksheet
            sheet.cells.subtotal(AsposeCells.CellArea.createCellArea("A2", "B9"), 0, AsposeCells.ConsolidationFunction.Average, [1]);

            // Calculates Formulas
            workbook.calculateFormula();

            // Auto fits all columns
            sheet.autoFitColumns();

            // Saving the workbook and preparing download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

{{% alert color="primary" %}}

 تعمل فئة [**GlobalizationSettings**](https://reference.aspose.com/cells/javascript-cpp/globalizationsettings) فقط على إضافة مجاميع فرعية جديدة. إذا كانت ورقة البيانات تحتوي على مجاميع فرعية بالفعل، فلا يمكن تعديل تسمياتها.

{{% /alert %}}
