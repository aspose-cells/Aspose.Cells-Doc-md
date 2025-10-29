---
title: قراءة عنوان الشارت من ملف ODS باستخدام JavaScript عبر C++
linktitle: قراءة عنوان المخطط من ملف ODS
description: تعلم كيفية استخدام Aspose.Cells for JavaScript عبر C++ لقراءة عنوان الشارت من ملف جدول بيانات مستند مفتوح (ODS). ستعرض أدلتنا كيفية استخراج والوصول إلى عنوان الشارت لمزيد من التحليل أو العرض.
keywords: Aspose.Cells for JavaScript عبر C++، قراءة عنوان الشارت، ملف جدول بيانات مستند مفتوح، ملف ODS، استخراج الشارت، تحليل البيانات.
type: docs
weight: 160
url: /ar/javascript-cpp/read-chart-subtitle-from-ods-file/
---

## **قراءة عنوان الرسم البياني من ملف ODS**

توفر لك Aspose.Cells القدرة على قراءة عناوين المخططات النصية الفرعية في ملفات ODS عن طريق استخدام الخاصية [**Chart.subTitle**](https://reference.aspose.com/cells/javascript-cpp/chart/#subTitle--). يحمّل نموذج الكود التالي ملف ODS النموذجي [ملف ODS النموذجي](89620481.ods) ويقرأ عنوان المخطط النصي الفرعي باستخدام الخاصية [**Chart.subTitle**](https://reference.aspose.com/cells/javascript-cpp/chart/#subTitle--) ويطبعه في نافذة وحدة التحكم. يرجى الاطلاع على مخرجات وحدة التحكم للكود المقدم أدناه للرجوع إليه.

## **الكود المثالي**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Get Chart Subtitle</title>
    </head>
    <body>
        <h1>Get Chart Subtitle Example</h1>
        <input type="file" id="fileInput" accept=".ods,.xls,.xlsx,.csv" />
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
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel or ODS file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the workbook
            const worksheet = workbook.worksheets.get(0);

            // Accessing the first chart inside the worksheet
            const chart = worksheet.charts.get(0);

            // Accessing chart subtitle text (converted from getSubTitle().getText())
            const subtitleText = chart.subTitle.text;

            console.log("Chart Subtitle: " + subtitleText);
            document.getElementById('result').innerHTML = '<p>Chart Subtitle: ' + (subtitleText ?? '') + '</p>';
        });
    </script>
</html>
```

## **مخرجات الوحدة**

{{< highlight javascript >}}

Chart Subtitle: Sample Chart Subtitle

{{< /highlight >}}
