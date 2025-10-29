---
title: تغيير تنسيق الخلية
linktitle: تغيير تنسيق الخلية
description: كيفية استخدام مكتبة Aspose.Cells في جافاسكريبت عبر C++ لتغيير تنسيق الخلايا، بما في ذلك الخط، اللون، الحد، إلخ. من خلال تعديل هذه الخصائص، لديك مزيد من التحكم في مظهر الخلايا.
keywords: Aspose.Cells، تنسيق الخلايا، جافاسكريبت عبر C++، الخط، اللون، الحد
type: docs
weight: 20
url: /ar/javascript-cpp/how-to-change-format-of-cell/
---

## **سيناريوهات الاستخدام المحتملة**
عندما ترغب في تسليط الضوء على بعض البيانات، يمكنك تغيير نمط الخلايا.

## **كيفية تغيير تنسيق الخلية في إكسل**

لتغيير تنسيق خلية واحدة في إكسل، اتبع هذه الخطوات:

1. افتح إكسل وافتح الدفتر الذي يحتوي على الخلية التي ترغب في تنسيقها.

2. اعثر على الخلية التي ترغب في تنسيقها.

3. انقر بزر الماوس الأيمن على الخلية وحدد "تنسيق الخلايا" من قائمة السياق. كبديل، يمكنك تحديد الخلية والانتقال إلى علامة التبويب الرئيسية في شريط أدوات إكسل، انقر فوق قائمة "تنسيق" في مجموعة "الخلايا" وحدد "تنسيق الخلايا".

4. سيظهر مربع حوار "تنسيق الخلايا". هنا، يمكنك اختيار خيارات التنسيق المختلفة لتطبيقها على الخلية المحددة. على سبيل المثال، يمكنك تغيير نمط الخط، حجم الخط، لون الخط، تنسيق الأرقام، الحدود، لون الخلفية، إلخ. استكشف الألسنة المختلفة في مربع الحوار للوصول إلى خيارات التنسيق المختلفة.

5. بعد إجراء التغييرات في التنسيق المطلوب، انقر على زر "موافق" لتطبيق التنسيق على الخلية المحددة.


## **كيفية تغيير تنسيق خلية باستخدام جافاسكريبت**

لتغيير تنسيق خلية باستخدام Aspose.Cells، يمكنك استخدام الطرق التالية:
1. [نمط_الخلية(نمط)](https://reference.aspose.com/cells/javascript-cpp/cell/#style-style-)
2. [نمط_الخلية(نمط، علم صريح)](https://reference.aspose.com/cells/javascript-cpp/cell/#style-style-boolean-)
3. [نمط_الخلية(نمط، علم نمط)](https://reference.aspose.com/cells/javascript-cpp/cell/#style-style-styleflag-)


## **الكود المثالي**
في هذا المثال، نقوم بإنشاء ملف عمل إكسل، نضيف بعض البيانات النموذجية، نصل إلى الورقة الأولى، والحصول على خليتين ("A2" و"B3"). ثم، نحصل على نمط الخلية، ونضبط خيارات التنسيق المختلفة (مثل لون الخط، عريض)، ونغير التنسيق للخلية. أخيرًا، نحفظ ملف العمل إلى ملف جديد.
![todo:image_alt_text](change-format.png)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell } = AsposeCells;

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

            // Instantiating a Workbook object by opening the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the first worksheet
            const ws = workbook.worksheets.get(0);
            const cells = ws.cells;

            // Setting the value to the cells
            let cell = cells.get("A1");
            cell.value = "Fruit";
            cell = cells.get("B1");
            cell.value = "Count";
            cell = cells.get("C1");
            cell.value = "Price";

            cell = cells.get("A2");
            cell.value = "Apple";
            cell = cells.get("A3");
            cell.value = "Mango";
            cell = cells.get("A4");
            cell.value = "Blackberry";
            cell = cells.get("A5");
            cell.value = "Cherry";

            cell = cells.get("B2");
            cell.value = 5;
            cell = cells.get("B3");
            cell.value = 3;
            cell = cells.get("B4");
            cell.value = 6;
            cell = cells.get("B5");
            cell.value = 4;

            cell = cells.get("C2");
            cell.value = 5;
            cell = cells.get("C3");
            cell.value = 20;
            cell = cells.get("C4");
            cell.value = 30;
            cell = cells.get("C5");
            cell.value = 60;

            // Access the worksheet
            const worksheet = workbook.worksheets.get(0);

            const a2 = worksheet.cells.get("A2");

            // Get style of A2
            const style = a2.style;

            // Change the format
            style.font.color = AsposeCells.Color.Red;
            style.font.isBold = true;

            const flag = new AsposeCells.StyleFlag();
            flag.fontColor = true;
            // Apply style (assignment per conversion rules)
            a2.style = style;

            const b3 = worksheet.cells.get("B3");
            // Get style of B3
            const style2 = b3.style;

            // Change the format
            style2.font.color = AsposeCells.Color.Blue;
            style2.font.isItalic = true;
            b3.style = style2;

            // Saving the modified workbook and offering it for download
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
