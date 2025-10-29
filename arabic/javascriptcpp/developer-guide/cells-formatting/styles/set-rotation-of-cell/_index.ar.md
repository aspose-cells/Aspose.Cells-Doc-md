---
title: كيفية دوران نص الخلية
linktitle: كيفية دوران نص الخلية  
type: docs  
weight: 80  
url: /ar/javascript-cpp/how-to-rotate-text-of-cell/  
description: تعلّم كيف تدور نصوص خلايا بشكل برمجي باستخدام Aspose.Cells for JavaScript عبر C++.  
keywords: جافا سكريبت عبر C++، تدوير نص الخلية، برمجة النصوص، تعيين زاوية التدوير برمجياً، جافا سكريبت، تدوير نص الخلية في إكسل  
---

## **تدوير نص الخلية في Aspose.Cells for JavaScript عبر C++**

Aspose.Cells هو مكون قوي لجافا سكريبت يمكّن المطورين من العمل مع جداول بيانات إكسل برمجياً. واحدة من الميزات التي يوفرها Aspose.Cells هي القدرة على تدوير الخلايا، مما يتيح تخصيص اتجاه النص وتحسين العرض البصري لبياناتك. في هذا المستند، سنستعرض كيفية تدوير الخلايا باستخدام Aspose.Cells.

## **كيفية تدوير نص الخلية في إكسل**
يمكنك تدوير خلية في إكسل باستخدام الخطوات التالية:
1. افتح برنامج إكسل وحدد الخلية أو مجموعة من الخلايا التي ترغب في تدويرها.
1. انقر بزر الماوس الأيمن على الخلية(الخلايا) المحددة واختر "تنسيق الخلايا" من قائمة السياق. بالإضافة إلى ذلك، يمكنك الانتقال إلى علامة التبويب "الرئيسية" في شريط أدوات إكسل، انقر على القائمة المنسدلة "تنسيق" في مجموعة "الخلايا"، واختر "تنسيق الخلايا".
1. في مربع حوار "تنسيق الخلايا"، انتقل إلى علامة التبويب "توجيه".
1. في قسم "التوجيه"، سترى خيارات لتدوير النص. يمكنك إدخال زاوية التدوير المرغوبة مباشرة في مربع "الدرجات". القيم الإيجابية تدور النص باتجاه عقارب الساعة، والقيم السالبة تدور به عكس اتجاه عقارب الساعة.
<br>
![todo:image_alt_text](alignment.png)
1. بمجرد اختيار الدورة المرغوبة، انقر على "موافق" لتطبيق التغييرات. ستتم إعادة تدوير الخلية(الخلايا) المحددة الآن استنادًا إلى زاوية التدوير أو التوجيه التي اخترتها.

## **كيفية تدوير نص الخلية باستخدام واجهة برمجة تطبيقات Aspose.Cells**

خاصية [**Style.rotationAngle(number)**](https://reference.aspose.com/cells/javascript-cpp/style/#rotationAngle-number-) تجعل من السهل تدوير الخلايا. لتدوير الخلايا في Aspose.Cells، تحتاج إلى اتباع الخطوات التالية:
1. تحميل دفتر العمل في إكسل  
<br>
أولاً، تحتاج إلى تحميل دفتر العمل في إكسل باستخدام Aspose.Cells. يمكنك استخدام فئة Workbook لفتح ملف إكسل موجود أو إنشاء ملف جديد. 

1. الوصول إلى ورقة البيانات  
<br>
بمجرد تحميل دفتر العمل، ستحتاج إلى الوصول إلى ورقة البيانات التي ترغب في تدوير الخلايا فيها. يمكنك الوصول إما إلى ورقة البيانات بمؤشرها أو اسمها. 

1. تدوير نص الخلية  
<br>
الآن بعد أن لديك وصول إلى ورقة البيانات، يمكنك تدوير الخلايا عن طريق تعديل كائن الأنماط (Style) للخلايا المرغوبة. كائن الأنماط يسمح لك بتعيين مجموعة متنوعة من خيارات التنسيق، بما في ذلك التدوير. 

1. حفظ دفتر العمل  
<br>
بعد تدوير الخلايا، يمكنك حفظ دفتر العمل المعدل مرة أخرى في ملف أو تيار باستخدام طريقة الحفظ.

## **رمز جافا سكريبت كنموذج**

 يرجى مراجعة الكود التالي، الذي ينشئ كائن مصنف ويحدد زوايا تدوير مختلفة لعدة خلايا. تُظهر الصورة الناتجة بعد تنفيذ المثال.
<br>
<img src="rotation.png" width=80% />

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Rotate Text in Cells Example</h1>
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
            // Creating a new Workbook (blank)
            const workbook = new Workbook();

            // Obtaining the reference of the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Row index of the cell
            let row = 0;
            // Column index of the cell
            let column = 0; 

            let a1 = worksheet.cells.get(row, column);
            a1.putValue("a1 rotate text");
            let a1Style = a1.style;

            // Set the rotation angle in degrees
            a1Style.rotationAngle = 45; 
            a1.style = a1Style;

            // set Column index of the cell
            column = 1;
            let b1 = worksheet.cells.get(row, column);
            b1.putValue("b1 rotate text");
            let b1Style = b1.style;

            // Set the rotation angle in degrees
            b1Style.rotationAngle = 255;
            b1.style = b1Style;

            // set Column index of the cell
            column = 2;
            let c1 = worksheet.cells.get(row, column);
            c1.putValue("c1 rotate text");
            let c1Style = c1.style;

            // Set the rotation angle in degrees
            c1Style.rotationAngle = -90;
            c1.style = c1Style;

            // set Column index of the cell
            column = 3;
            let d1 = worksheet.cells.get(row, column);
            d1.putValue("d1 rotate text");
            let d1Style = d1.style;

            // Set the rotation angle in degrees
            d1Style.rotationAngle = -90;
            d1.style = d1Style;

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
