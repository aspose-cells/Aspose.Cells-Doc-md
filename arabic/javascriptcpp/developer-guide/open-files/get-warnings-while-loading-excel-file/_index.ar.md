---
title: الحصول على تحذيرات أثناء تحميل ملف إكسل باستخدام JavaScript عبر C++
linktitle: الحصول على تحذيرات أثناء تحميل ملف إكسل
type: docs
weight: 110
url: /ar/javascript-cpp/get-warnings-while-loading-excel-file/
description: تعلّم كيفية التقاط التحذيرات أثناء تحميل ملف إكسل باستخدام Aspose.Cells for JavaScript عبر C++. التعامل مع دفاتر العمل الفاسدة ولكن القابلة للتحميل بفعالية.
---

## **سيناريوهات الاستخدام المحتملة**

أحيانًا، يحاول المستخدم تحميل دفتر عمل يكون معطوبًا بعض الشيء ولكنه قابل للتحميل. في مثل هذه الحالات، يرمي Aspose.Cells تحذيرات أثناء تحميل دفتر العمل. يمكنك التقاط هذه التحذيرات من خلال تنفيذ واجهة [**IWarningCallback**](https://reference.aspose.com/cells/javascript-cpp/iwarningcallback) وتعيين الخاصية [**LoadOptions.warningCallback**](https://reference.aspose.com/cells/javascript-cpp/loadoptions/#warningCallback--).

## **الحصول على تحذيرات أثناء تحميل ملف إكسل**

يشرح الكود النموذجي التالي كيفية الحصول على التحذيرات أثناء تحميل ملف Excel. يقوم الكود بتحميل [ملف Excel النموذجي](sampleDuplicateDefinedName.xlsx) الذي يرمي تحذير [**DuplicateDefinedName**](https://reference.aspose.com/cells/javascript-cpp/warningtype) عند التحميل. ثم يتم التقاط هذا التحذير بواسطة طريقة [**IWarningCallback.warning(WarningInfo)**](https://reference.aspose.com/cells/javascript-cpp/iwarningcallback/#warning-warninginfo-) التي تطبع رسائل التحذير على وحدة التحكم. ثم يحفظ الكود دفتر العمل كـ [ملف Excel الناتج](outputDuplicateDefinedName.xlsx). إذا فتحت ملف Excel النموذجي في Microsoft Excel، فستعرض أيضًا هذا التحذير كما هو موضح في الصورة. يرجى أيضًا التحقق من إخراج وحدة التحكم للرمز أدناه لمزيد من الفهم.

![todo:image_alt_text](get-warnings-while-loading-excel-file_1.png)

## **الكود المثالي**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Warning Callback Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Warning Callback Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, LoadOptions, WarningType } = AsposeCells;

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

        // Implement IWarningCallback interface to catch warnings while loading workbook
        class WarningCallback extends AsposeCells.IWarningCallback {
            warning(warningInfo) {
                if (warningInfo.type === AsposeCells.WarningType.DuplicateDefinedName) {
                    console.log("Duplicate Defined Name Warning: " + warningInfo.description);
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

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Create load options and set the WarningCallback property 
            // to catch warnings while loading workbook
            const options = new LoadOptions();
            options.warningCallback = new WarningCallback();

            // Load the source excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer), options);

            // Save the workbook and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputDuplicateDefinedName.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Resulting Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Workbook processed successfully. Check console for warnings.</p>';
        });
    </script>
</html>
```

## **مخرجات الوحدة**



{{< highlight java >}}

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:Introduction!$D$16:$D$17

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:Panel!$B$228

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:'Queries '!$D$14:$D$16

{{< /highlight >}}
