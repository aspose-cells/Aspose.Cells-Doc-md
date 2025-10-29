---
title: قياس العرض والارتفاع لقيمة الخلية بوحدات البكسل
linktitle: قياس الحجم
type: docs
weight: 260
url: /ar/javascript-cpp/calculate-the-width-and-height-of-the-cell-value-in-unit-of-pixels/
description: تعلم كيفية قياس عرض وارتفاع قيمة الخلية بوحدة البيكسل عبر Aspose.Cells for JavaScript باستخدام C++.
keywords: قياس عرض قيمة الخلية بوحدة البيكسل باستخدام JavaScript عبر C++، قياس ارتفاع قيمة الخلية بوحدة البيكسل باستخدام JavaScript عبر C++، الحصول على عرض قيمة الخلية بوحدة البيكسل باستخدام JavaScript عبر C++، الحصول على ارتفاع قيمة الخلية بوحدة البيكسل باستخدام JavaScript عبر C++
---

{{% alert color="primary" %}}  

في بعض الأحيان تحتاج إلى حساب عرض وارتفاع قيمة الخلية لتناسب قيمة الخلية داخل الخلية. توفر Aspose.Cells الطرق [**Cell.widthOfValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#widthOfValue--) و [**Cell.heightOfValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#heightOfValue--) لهذا الغرض. من خلال استخدام هذه الأساليب يمكنك حساب عرض وارتفاع قيمة الخلية ثم تعيين عرض العمود وارتفاع الصف لتلك الخلية على التوالي وبعد ذلك سيتم ضبط أو تناسب قيمة الخلية داخل الخلية.  

بدلاً من ذلك، يمكنك أيضًا [مواءمة الصفوف والأعمدة في الخلية أو مجموعة خلاياك](/cells/ar/javascript-cpp/autofit-rows-and-columns/) باستخدام واجهات برمجة التطبيقات Aspose.Cells.  

{{% /alert %}}  

يفسر الكود التالي استخدام طرق [**Cell.widthOfValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#widthOfValue--) و [**Cell.heightOfValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#heightOfValue--).  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Get Cell Size Example</h1>
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

            // Create or load workbook
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access cell B2 and add some value inside it
            const cell = worksheet.cells.get("B2");
            cell.value = "Welcome to Aspose!";

            // Enlarge its font to size 16
            const style = cell.style;
            style.font.size = 16;
            cell.style = style;

            // Calculate the width and height of the cell value in unit of pixels
            const widthOfValue = cell.widthOfValue;
            const heightOfValue = cell.heightOfValue;

            // Print both values to the page
            document.getElementById('result').innerHTML = `<p>Width of Cell Value: ${widthOfValue}</p><p>Height of Cell Value: ${heightOfValue}</p>`;

            // Set the row height and column width to adjust/fit the cell value inside cell
            worksheet.cells.setColumnWidthPixel(1, widthOfValue);
            worksheet.cells.setRowHeightPixel(1, heightOfValue);

            // Save the output excel file and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';
        });
    </script>
</html>
```


## **مواضيع متقدمة**  
- [الحصول على عرض النص لقيمة الخلية](/cells/ar/javascript-cpp/get-text-width-of-cell-value/)
