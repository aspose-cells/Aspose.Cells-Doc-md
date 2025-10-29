---
title: الحصول على جميع مفرقات الصفوف المخفية بعد تحديث تصفية السيارة. 
type: docs  
weight: 320  
url: /ar/javascript-cpp/get-all-hidden-rows-indices-after-refreshing-autofilter/  
description: تعلم كيفية الحصول على جميع فهارس الصفوف المخفية بعد تحديث الفلتر التلقائي باستخدام Aspose.Cells for JavaScript عبر C++.  
keywords: الحصول على جميع فهارس الصفوف المخفية بعد تحديث الفلتر التلقائي جافا سكريبت عبر C++، الحصول على جميع فهارس الصفوف المخفية بعد تحديث الفلتر التلقائي جافا سكريبت عبر C++، استرجاع جميع فهارس الصفوف المخفية بعد تحديث الفلتر التلقائي جافا سكريبت عبر C++  
---

## **سيناريوهات الاستخدام المحتملة**  

عند تطبيق الفلتر التلقائي على خلايا ورقة العمل، يتم إخفاء بعض الصفوف تلقائيًا. لكن قد تكون بعض الصفوف مخفية يدويًا بواسطة مستخدم إكسل ولا يتم إخفاؤها بواسطة الفلتر التلقائي. هذا يجعل من الصعب معرفة الصفوف المخفية بواسطة الفلتر التلقائي وتلك المخفية يدويًا بواسطة مستخدم إكسل. يتعامل Aspose.Cells for JavaScript عبر C++ مع هذه المشكلة باستخدام الخاصية [**AutoFilter.refresh(hideRows)**](https://reference.aspose.com/cells/javascript-cpp/autofilter/#refresh-boolean-). ترجع هذه الطريقة فهارس الصفوف لكل الصفوف التي يتم إخفاؤها بواسطة الفلتر التلقائي وليس يدويًا بواسطة مستخدم إكسل.  

## **الحصول على جميع فهرسات الصفوف المخفية بعد تحديث تصفية السيارة.**  

يرجى الاطلاع على رمز العينة التالي الذي يحمل [ملف إكسل نموذج](64716909.xlsx) الذي يحتوي على بعض الصفوف التي تم إخفاؤها يدويًا بواسطة مستخدم إكسل. يقوم الرمز بتطبيق الفلتر التلقائي ويحدثه باستخدام طريقة `Array` [**AutoFilter.refresh(hideRows)**](https://reference.aspose.com/cells/javascript-cpp/autofilter/#refresh-boolean-) التي ترجع مؤشرات الصفوف لجميع الصفوف المخفية بواسطة الفلتر التلقائي. ثم يعرض مؤشرات الصفوف المخفية على وحدة التحكم مع أسماء وقيَم الخلايا.  

## **الكود المثالي**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Get Hidden Rows After Refreshing AutoFilter</title>
    </head>
    <body>
        <h1>Get Hidden Rows After Refreshing AutoFilter</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
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
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from file input
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Apply autofilter
            worksheet.autoFilter.addFilter(0, "Orange");

            // True means it will refresh autofilter and return hidden rows.
            const rowIndices = worksheet.autoFilter.refresh(true);

            console.log("Printing Rows Indices, Cell Names and Values Hidden By AutoFilter.");
            console.log("--------------------------");

            let output = '<p>Printing Rows Indices, Cell Names and Values Hidden By AutoFilter.</p><pre>';
            rowIndices.forEach(r => {
                const cell = worksheet.cells.get(r, 0);
                console.log(`${r}\t${cell.name}\t${cell.stringValue}`);
                output += `${r}\t${cell.name}\t${cell.stringValue}\n`;
            });
            output += '</pre>';

            resultDiv.innerHTML = output;
        });
    </script>
</html>
```


## **مخرجات الوحدة**  

{{< highlight java >}}  

Printing Rows Indices, Cell Names and Values Hidden By AutoFilter.  

\--------------------------  

1       A2      Apple  

2       A3      Apple  

3       A4      Apple  

6       A7      Apple  

7       A8      Apple  

11      A12     Pear  

12      A13     Pear  

{{< /highlight >}}
