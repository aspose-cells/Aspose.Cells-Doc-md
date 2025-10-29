---
title: تحديد ما إذا كانت الشكل هو شكل فن ذكي باستخدام JavaScript عبر C++
linktitle: تحديد ما إذا كانت الشكل شكل رسوم بيانية ذكية
type: docs
weight: 400
url: /ar/javascript-cpp/determine-if-shape-is-smart-art-shape/
description: تعلم كيفية تحديد ما إذا كان الشكل في إكسل هو شكل فن ذكي باستخدام Aspose.Cells for JavaScript عبر C++.
---

## **سيناريوهات الاستخدام المحتملة**  

أشكال الفن الذكي هي أشكال خاصة في مايكروسوفت إكسل تتيح لك إنشاء مخططات معقدة تلقائياً. يمكنك معرفة ما إذا كان الشكل هو شكل فن ذكي أو شكل عادي باستخدام خاصية [**Shape.isSmartArt()**](https://reference.aspose.com/cells/javascript-cpp/shape/#isSmartArt--).  

## **تحديد ما إذا كان الشكل هو شكل ذكاء ذكي**  

الرمز المساعد التالي يقوم بتحميل ملف إكسل (sample.xlsx) الذي يحتوي على شكل فن ذكي كما هو موضح في هذه الصورة. ثم يطبع قيمة خاصية [**Shape.isSmartArt()**](https://reference.aspose.com/cells/javascript-cpp/shape/#isSmartArt--) لأول شكل. يرجى الاطلاع على مخرجات وحدة التحكم للرمز المساعد المقدم أدناه.  

![todo:image_alt_text](determine-if-shape-is-smart-art-shape_1.png)  

## **الكود المثالي**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Example Title</h1>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Accessing the first shape
            const shape = worksheet.shapes.get(0);

            // Determine if shape is smart art (converted to property access)
            const isSmartArt = shape.isSmartArt;

            document.getElementById('result').innerHTML = `<p>Is Smart Art Shape: ${isSmartArt}</p>`;
        });
    </script>
</html>
```  

## **مخرجات الوحدة**  

{{< highlight java >}}  

Is Smart Art Shape: True  

{{< /highlight >}}
