---
title: الحصول على قائمة الخطوط المستخدمة في جدول بيانات أو كتاب عمل
linktitle: الحصول على قائمة الخطوط المستخدمة في جدول بيانات أو كتاب عمل
description: تعلم كيفية الحصول على قائمة الخطوط المستخدمة في جدول بيانات أو دفتر عمل باستخدام Aspose.Cells for JavaScript عبر C++. ستوضح لك هذه المقالة كيفية استرداد معلومات الخط من المستند.
keywords: Aspose.Cells، جافا سكريبت عبر C++، جدول بيانات، دفتر عمل، خط، قائمة
type: docs
weight: 20
url: /ar/javascript-cpp/get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook/
---

## **سيناريوهات الاستخدام المحتملة**

غالبًا ما يكون من الضروري معرفة الخطوط المستخدمة في ملف العمل الخاص بك لأغراض العرض. عند تحويل ملف العمل إلى PDF أو صورة، فإن Aspose.Cells يتطلب تثبيت جميع الخطوط اللازمة على النظام الخاص بك أو وجودها في **مجلد الخطوط**. إذا كان Aspose.Cells غير قادر على العثور على الخط المطلوب، فإنه يحاول استبداله بخط مناسب آخر متوفر على نظامك أو في مجلد الخطوط الخاص بك ويمكن أن يحل محل الخط الفعلي الخاص بك. هذا لا يسفر فقط عن تصور غير مرغوب فيه لملف الـPDF أو الصور ولكنه يستغرق أيضًا وقت المعالجة للعثور على خطوط مناسبة.

للتعامل مع مثل هذه الحالات، يجب أن تعرف الخطوط المستخدمة في دفتر العمل الخاص بك، ثم إما تثبيت تلك الخطوط على نظامك في حالة بيئة Windows أو وضعها في دليل الخطوط في حالة بيئة Windows أو Linux.

يوفر Aspose.Cells for JavaScript عبر C++ طريقة [**Workbook.fonts**](https://reference.aspose.com/cells/javascript-cpp/workbook/#fonts--) التي تعيد قائمة بجميع الخطوط المستخدمة في دفتر العمل أو جدول البيانات الخاص بك.

## **الحصول على قائمة الخطوط المستخدمة في جدول بيانات أو كتاب عمل**

يحمل الشيفرة النموذجية التالية ملف إكسل المصدر ويسترجع قائمة الخطوط المستخدمة في داخله. يحتوي على ورقة عمل وهمية وقد تمت إضافة بعض الخطوط الوهمية لأغراض توضيحية. عندما تطبع الشيفرة جميع الخطوط داخل الدفتر، فإنها تطبع أيضًا تلك الخطوط الوهمية. تظهر اللقطة الشاشية التالية [ملف إكسل عيني](25395211.xlsx) وكيفية سرد الخطوط الوهمية.

![todo:image_alt_text](get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook_1.png)

## **الكود المثالي**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Get Fonts Example</title>
        <meta charset="utf-8" />
    </head>
    <body>
        <h1>Get Fonts from Workbook</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Get Fonts</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell, Utils } = AsposeCells;

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

            // Instantiate workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get all the fonts inside the workbook (converted from getFonts())
            const fonts = workbook.fonts;

            // Print all the fonts into the result div
            if (!fonts || fonts.length === 0) {
                document.getElementById('result').innerHTML = '<p>No fonts found in the workbook.</p>';
                return;
            }

            let html = '<h2>Fonts in Workbook</h2><ul>';
            for (let i = 0; i < fonts.length; i++) {
                html += `<li>${fonts[i].toString()}</li>`;
            }
            html += '</ul>';
            document.getElementById('result').innerHTML = html;
        });
    </script>
</html>
```


## **مخرجات الوحدة**



{{< highlight java >}}

Aspose.Cells.Font [ Calibri; 11; Regular; Color [Black] ]

Aspose.Cells.Font [ Arial; 10; Regular; Color [A=255, R=0, G=0, B=0] ]

Aspose.Cells.Font [ Calibri; 10; Bold; Color [Black] ]

Aspose.Cells.Font [ Calibri; 10; Regular; Color [A=255, R=128, G=128, B=128] ]

Aspose.Cells.Font [ Calibri; 10; Regular; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 16; Bold; Color [A=255, R=255, G=255, B=255] ]

Aspose.Cells.Font [ Calibri; 36; Regular; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 20; Bold; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 16; Regular; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 11; Regular; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 11; Bold; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 11; Bold; Color [A=255, R=255, G=255, B=255] ]

Aspose.Cells.Font [ Calibri; 11; Italic; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 16; Regular; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 16; Bold; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 16; Regular; Color [Black] ]

Aspose.Cells.Font [ Calibri; 16; Regular; Color [A=255, R=41, G=74, B=78] ]

Aspose.Cells.Font [ Calibri; 16; Regular; Color [A=255, R=41, G=74, B=78] ]

Aspose.Cells.Font [ Calibri; 12; Regular; Color [A=255, R=41, G=74, B=78] ]

Aspose.Cells.Font [ Calibri; 11; Regular; Color [A=255, R=41, G=74, B=78] ]

Aspose.Cells.Font [ Calibri; 11; Bold; Color [A=255, R=255, G=255, B=255] ]

Aspose.Cells.Font [ Dummy-Arial-X; 11; Regular; Color [Black] ]

Aspose.Cells.Font [ Dummy-Arial-Y; 11; Regular; Color [Black] ]

Aspose.Cells.Font [ Dummy-Arial-Z; 11; Regular; Color [Black] ]

Aspose.Cells.Font [ Dummy-Times-I; 11; Regular; Color [Black] ]

Aspose.Cells.Font [ Dummy-Times-II; 11; Regular; Color [Black] ]

Aspose.Cells.Font [ Dummy-Times-III; 11; Regular; Color [Black] ]

Aspose.Cells.Font [ Calibri; 10.5; Regular; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 20; Regular; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 11; Regular; Color [A=255, R=55, G=98, B=104] ]

{{< /highlight >}}
