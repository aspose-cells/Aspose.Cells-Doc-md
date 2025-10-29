---
title: تصفية الأسماء المعرفة أثناء تحميل دفتر العمل باستخدام JavaScript عبر C++
linktitle: تصفية أسماء محددة أثناء تحميل المصنف
type: docs
weight: 50
url: /ar/javascript-cpp/filter-defined-names-while-loading-workbook/
---

## **سيناريوهات الاستخدام المحتملة**

يسمح Aspose.Cells لك بتصفية أو إزالة الأسماء المعرفة الموجودة داخل المصنف. يرجى استخدام [**LoadDataFilterOptions.DefinedNames**](https://reference.aspose.com/cells/javascript-cpp/loaddatafilteroptions/) لتحميل الأسماء المعرف عليها واستخدام [**LoadDataFilterOptions.DefinedNames**](https://reference.aspose.com/cells/javascript-cpp/loaddatafilteroptions/) لإزالتها أثناء تحميل المصنف. يرجى ملاحظة، إذا قمت بإزالة الأسماء المعرفة، قد تتعطل الصيغ داخل المصنف.

## **تصفية أسماء محددة أثناء تحميل المصنف**

يقوم الرمز النموذجي التالي بتحميل [ملف Excel النموذجي](61767860.xlsx) الذي يحتوي على صيغة في الخلية **C1** تحتوي على الأسماء المحددة i.e. * =SUM(MyName1, MyName2)*. نظرًا لأننا نستخدم [**LoadDataFilterOptions.DefinedNames**](https://reference.aspose.com/cells/javascript-cpp/loaddatafilteroptions/) لإزالة الأسماء المحددة أثناء تحميل دفتر العمل، تتعطل الصيغة في الخلية C1 في [ملف Excel الناتج](61767861.xlsx) وتظهر *#NAME?*. يرجى الاطلاع على الصورة التالية التي تُظهر تأثير الكود على ملف Excel النموذجي.

![todo:image_alt_text](filter-defined-names-while-loading-workbook_1.png)

## **الكود المثالي**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Filter Defined Names While Loading Workbook</title>
    </head>
    <body>
        <h1>Filter Defined Names While Loading Workbook</h1>
        <input type="file" id="fileInput" accept=".xlsx,.xls" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, LoadOptions, LoadFilter, LoadDataFilterOptions, Utils } = AsposeCells;

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

            // Specify the load options
            let opts = new LoadOptions();
            // We do not want to load defined names
            opts.loadFilter = new LoadFilter(~LoadDataFilterOptions.DefinedNames);

            // Load the workbook with load options
            const workbook = new Workbook(new Uint8Array(arrayBuffer), opts);

            // Save the output Excel file, it will break the formula in C1 if defined names were removed
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputFilterDefinedNamesWhileLoadingWorkbook.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">FilterDefinedNamesWhileLoadingWorkbook executed successfully. Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
