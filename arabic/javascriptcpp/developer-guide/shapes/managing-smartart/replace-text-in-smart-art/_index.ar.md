---
title: استبدال النص في الشكل الذكي باستخدام جافا سكريبت عبر C++
linktitle: استبدال النص في شكل ذكاء ذكي
type: docs
weight: 1200
url: /ar/javascript-cpp/replace-text-in-smart-art/
description: تعلم كيفية استبدال النص في الشكل الذكي باستخدام Aspose.Cells for JavaScript عبر C++.
---

## **سيناريوهات الاستخدام المحتملة**  

الاشكال الذكية هي واحدة من الكائنات الرئيسية في مصنف العمل. في كثير من الأحيان، يكون هناك حاجة لتحديث النص في الأشكال الذكية. توفر Aspose.Cells for JavaScript عبر C++ هذه الميزة عن طريق تعيين الخاصية [**Shape.text**](https://reference.aspose.com/cells/javascript-cpp/shape/#text--).  

يمكن تنزيل ملف المصدر من الرابط التالي:  

[SmartArt.xlsx](77496338.xlsx)  

## **الكود المثالي**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells SmartArt Example</title>
    </head>
    <body>
        <h1>SmartArt Replacement Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, OoxmlSaveOptions } = AsposeCells;

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

            // Access worksheets collection
            const worksheets = workbook.worksheets;
            for (let i = 0; i < worksheets.count; i++) {
                const worksheet = worksheets.get(i);
                const shapes = worksheet.shapes;
                for (let j = 0; j < shapes.count; j++) {
                    const shape = shapes.get(j);
                    // Set alternative text using property assignment
                    shape.alternativeText = "ReplacedAlternativeText";
                    if (shape.isSmartArt()) {
                        // Access smart art grouped shapes via properties
                        const smartArtShapes = shape.resultOfSmartArt.groupedShapes;
                        for (let k = 0; k < smartArtShapes.length; k++) {
                            const smartart = smartArtShapes[k];
                            // Set text using property assignment
                            smartart.text = "ReplacedText";
                        }
                    }
                }
            }

            // Configure save options and enable SmartArt update
            const options = new OoxmlSaveOptions();
            options.updateSmartArt = true;

            // Save workbook to XLSX format with options and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx, options);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputSmartArt.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">SmartArt updated successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
