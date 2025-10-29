---
title: إنشاء، تعديل أو إزالة سيناريوهات من أوراق العمل باستخدام جافا سكريبت عبر C++
linktitle: إدارة السيناريوهات
type: docs
weight: 190
url: /ar/javascript-cpp/create-manipulate-or-remove-scenarios-from-worksheets/
description: تعلم كيفية إنشاء، تعديل، أو إزالة سيناريوهات من أوراق عمل إكسل برمجياً باستخدام واجهة برمجة تطبيقات جافا سكريبت عبر C++.
keywords: إنشاء سيناريو لورقة العمل جافا سكريبت عبر C++، إزالة سيناريو من ورقة عمل إكسل جافا سكريبت عبر C++، تعديل سيناريو لورقة العمل جافا سكريبت عبر C++
---

{{% alert color="primary" %}}

في بعض الأحيان، قد تحتاج إلى إنشاء، التلاعب أو حذف السيناريوهات في جداول البيانات. السيناريو هو نموذج 'ماذا لو؟' يتضمن خلايا إدخال متغيرة مرتبطة بواحد أو أكثر من الصيغ. قبل إنشاء سيناريو، صمم الورقة العمل بحيث تحتوي على صيغة واحدة على الأقل تعتمد على الخلايا التي يمكن إدراج قيم مختلفة فيها. يظهر المثال التالي كيفية إنشاء وإزالة السيناريوهات من ورقة عمل في مصنف باستخدام واجهات Aspose.Cells.

{{% /alert %}}

توفر Aspose.Cells بعض الفئات المفيدة، على سبيل المثال، الفئات [**ScenarioCollection**](https://reference.aspose.com/cells/javascript-cpp/scenariocollection)، [**Scenario**](https://reference.aspose.com/cells/javascript-cpp/scenario)، [**ScenarioInputCellCollection**](https://reference.aspose.com/cells/javascript-cpp/scenarioinputcellcollection)، و [**ScenarioInputCell**](https://reference.aspose.com/cells/javascript-cpp/scenarioinputcell). كما تقدم الخاصية [**Worksheet.scenarios**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#scenarios--). يفتح كود المثال أدناه ملف إكسل XLSX يحتوي على بعض السيناريوهات ويزيل سيناريو موجود، بالإضافة إلى إضافة سيناريو جديد إلى ورقة العمل قبل حفظ ملف الإكسل. يستخدم المثال ملف قالب بسيط جدًا يحتوي على سيناريو.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Scenarios Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Scenarios Example</h1>
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

            // Instantiate the Workbook by loading the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            if (worksheet.scenarios.count > 0) {
                // Remove the existing first scenario from the sheet
                worksheet.scenarios.removeAt(0);
            }

            // Create a scenario
            const i = worksheet.scenarios.add("MyScenario");
            // Get the scenario
            const scenario = worksheet.scenarios.get(i);
            // Add comment to it
            scenario.comment = "Test scenario is created.";
            // Get the input cells for the scenario
            const sic = scenario.inputCells;
            // Add the scenario on B4 (as changing cell) with default value
            sic.add(3, 1, "1100000");

            // Save the Excel file and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outBk_scenarios1.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Process completed successfully. File ready for download.</p>';
        });
    </script>
</html>
```
