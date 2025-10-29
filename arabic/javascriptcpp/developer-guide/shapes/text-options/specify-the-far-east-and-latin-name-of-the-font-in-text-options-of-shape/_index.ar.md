---
title: تحديد اسم اللغة الشرقية البعيدة واللاتينية للخط في خيارات النص للشكل باستخدام جافا سكريبت عبر C++
linktitle: تحديد اسم الشرق الأقصى واللاتيني للخط في خيارات النص للشكل
type: docs
weight: 1600
url: /ar/javascript-cpp/specify-the-far-east-and-latin-name-of-the-font-in-text-options-of-shape/
description: تعلم كيفية تحديد أسماء خطوط الشرق الأقصى واللاتينية في خيارات النص للأشكال باستخدام Script Aspose.Cells for Java عبر C++.
---

## **سيناريوهات الاستخدام المحتملة**  

في بعض الأحيان، تريد عرض النص بخط لغة الشرق الأقصى مثل اليابانية، الصينية، التايلاندية، إلخ. يوفر Script Aspose.Cells for Java عبر C++ خاصية [**TextOptions.farEastName**](https://reference.aspose.com/cells/javascript-cpp/textoptions/#farEastName--) التي يمكن استخدامها لتحديد اسم خط اللغة الشرقية البعيدة. بالإضافة إلى ذلك، يمكنك أيضًا تحديد اسم خط اللاتينية باستخدام الخاصية [**TextOptions.latinName**](https://reference.aspose.com/cells/javascript-cpp/textoptions/#latinName--).  

## **تحديد اسم الشرق الأقصى واللاتيني للخط في خيارات النص للشكل**  

يخلق الكود التالي مربع نص ويضيف فيه نصًا يابانيًا. ثم يحدد أسماء الخط اللاتيني وشرق آسيا للنص ويحفظ ملف العمل كملف إكسل الناتج. يظهر لقطة الشاشة أسماء الخطوط في مربع النص الناتج في إكسل.  

![todo:image_alt_text](specify-the-far-east-and-latin-name-of-the-font-in-text-options-of-shape_1.png)  

## **الكود المثالي**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Specify Far East and Latin Name of Font in TextOptions of Shape</h1>
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
            // Create empty workbook.
            const wb = new Workbook();

            // Access first worksheet.
            const ws = wb.worksheets.get(0);

            // Add textbox inside the worksheet.
            const idx = ws.textBoxes.add(5, 5, 50, 200);
            const tb = ws.textBoxes.get(idx);

            // Set the text of the textbox.
            tb.text = "こんにちは世界";

            // Specify the Far East and Latin name of the font.
            tb.textOptions.latinName = "Comic Sans MS";
            tb.textOptions.farEastName = "KaiTi";

            // Save the output Excel file.
            const outputData = wb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputSpecifyFarEastAndLatinNameOfFontInTextOptionsOfShape.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
