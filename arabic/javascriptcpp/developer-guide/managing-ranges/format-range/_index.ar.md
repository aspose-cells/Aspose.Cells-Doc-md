---
title: تنسيق النطاقات باستخدام JavaScript عبر C++
linktitle: تنسيق النطاقات
type: docs
weight: 105
url: /ar/javascript-cpp/how-to-format-a-range/
description: تعلم كيفية تنسيق نطاق من الخلايا في Excel باستخدام Aspose.Cells for JavaScript عبر C++.
---

## **سيناريوهات الاستخدام المحتملة**  
عندما تحتاج إلى تطبيق نمط على النطاق، يمكنك استخدام تنسيق النطاق.  

## **كيفية تنسيق نطاق في إكسل**  

لتنسيق مجموعة من الخلايا في إكسل، يمكنك استخدام الخيارات المدمجة للتنسيق المقدمة من إكسل. إليك كيف يمكنك تنسيق مجموعة من الخلايا مباشرة في إكسل:  

1. افتح إكسل وافتح المصنف الذي يحتوي على النطاق الذي تريد تنسيقه.  

2. حدد النطاق من الخلايا التي تريد تنسيقها. يمكنك النقر وسحب لتحديد النطاق، أو يمكنك استخدام اختصارات لوحة المفاتيح مثل Shift + مفاتيح الأسهم لتوسيع التحديد.  

3. بمجرد تحديد النطاق، انقر بزر الماوس الأيمن على النطاق المحدد واختر "تنسيق الخلايا" من القائمة المنسدلة. بالإضافة إلى ذلك، يمكنك الانتقال إلى علامة التبويب الرئيسية في الشريط في إكسل، انقر فوق القائمة المنسدلة "تنسيق" في مجموعة "الخلايا"، واختر "تنسيق الخلايا".  

4. ستظهر نافذة "تنسيق الخلايا". هنا، يمكنك اختيار خيارات التنسيق المختلفة لتطبيقها على النطاق المحدد. على سبيل المثال، يمكنك تغيير نمط الخط، حجم الخط، لون الخط، تنسيق الأرقام، الحدود، لون الخلفية، إلخ. استكشاف علامات التبويب المختلفة في نافذة الحوار للوصول إلى خيارات التنسيق المختلفة.  

5. بعد إجراء التغييرات في التنسيق المطلوب، انقر على زر "موافق" لتطبيق التنسيق على النطاق المحدد.  

## **كيفية تنسيق نطاق باستخدام JavaScript**  

لتنسيق نطاق باستخدام Aspose.Cells for JavaScript عبر C++، يمكنك استخدام الطرق التالية:  
1. [Range.applyStyle(style, flag)](https://reference.aspose.com/cells/javascript-cpp/range/#applyStyle-style-styleflag-)  
2. [Range.style](https://reference.aspose.com/cells/javascript-cpp/range/#style-style-)  
3. [Range.style](https://reference.aspose.com/cells/javascript-cpp/range/#style-style-)  

## **الكود المثالي**  
في هذا المثال، نقوم بإنشاء دفتر عمل Excel، إضافة بعض البيانات العينية، الوصول إلى ورقة العمل الأولى، وتعريف نطاقين ("A1:C3" و "A4:C5"). ثم نقوم بإنشاء أنماط جديدة، وضبط خيارات التنسيق المختلفة (مثل لون الخط، والنص العريض)، وتطبيق النمط على النطاق. وأخيرًا، نحفظ دفتر العمل في ملف جديد.  
<br>  
![todo:image_alt_text](format-range.png)  

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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Create the workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the first worksheet
            const ws = workbook.worksheets.get(0);

            const cells = ws.cells;

            // Setting the value to the cells (converted putValue -> value)
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

            // Access the worksheet (already have ws, but keep variable for clarity)
            const worksheet = workbook.worksheets.get(0);

            // Define the range
            const range = worksheet.cells.createRange("A1:C3");

            // Apply formatting to the range
            const style = workbook.createStyle();
            style.font.color = AsposeCells.Color.Red;
            style.font.isBold = true;

            const flag = new AsposeCells.StyleFlag();
            flag.font = true;
            range.applyStyle(style, flag);

            // Define the range
            const range2 = worksheet.cells.createRange("A4:C5");

            // Apply formatting to the range
            const style2 = workbook.createStyle();
            style2.font.color = AsposeCells.Color.Blue;
            style2.font.isItalic = true;
            range2.setStyle(style2);

            // Save the modified workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook modified successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
