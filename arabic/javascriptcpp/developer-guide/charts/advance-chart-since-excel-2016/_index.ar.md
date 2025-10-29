---
title: قراء وتحكم في مخططات إكسل 2016 باستخدام جافا سكريبت عبر C++
linktitle: قراءة وتلاعب رسومات Excel 2016
description: تعلم كيفية قراءة والتحكم في مخططات إكسل 2016 باستخدام Aspose.Cells for JavaScript عبر C++. ستعرض لك هذه الدليل كيف تصل وتعدل خصائص المخططات المختلفة.
keywords: Aspose.Cells for JavaScript عبر C++، مخططات إكسل 2016، القراءة، التحكم، تسميات البيانات، ألوان السلسلة، التخطيط، التصنيف الهرمي، التصنيف الدائري.
type: docs
weight: 48
url: /ar/javascript-cpp/read-and-manipulate-excel-2016-charts/
---

## **سيناريوهات الاستخدام المحتملة**  
أصبحت Aspose.Cells الآن تدعم قراءة وتلاعب الرسومات Microsoft Excel 2016 التي لم تكن موجودة في Microsoft Excel 2013 أو الإصدارات السابقة.  
## **قراءة وتلاعب شكل بيانات Excel 2016**  
يعرض الكود النموذجي التالي تحميل ملف Excel المصدر ([source excel file](22774101.xlsx)) الذي يحتوي على مخططات Excel 2016 في أول ورقة عمل. يقوم بقراءة جميع المخططات واحدًا تلو الآخر ويغير عنوانه وفقًا لنوع المخطط. تظهر لقطة الشاشة التالية الملف المصدر قبل تنفيذ الكود. كما ترى، عنوان المخطط هو نفسه لجميع المخططات.

![todo:image_alt_text](read-and-manipulate-excel-2016-charts_1.png)

تظهر اللقطة الشاشية التالية [ملف Excel الناتج](22774104.xlsx) بعد تنفيذ الكود. كما تلاحظ، تم تغيير عنوان الرسم حسب نوعه.

![todo:image_alt_text](read-and-manipulate-excel-2016-charts_2.png)  
## **الكود المثالي**  
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Read and Update Chart Titles</h1>
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
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            // Read selected file
            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet which contains the charts
            const sheet = workbook.worksheets.get(0);

            // Access all charts one by one and read their types
            const chartsCount = sheet.charts.count;
            let logHtml = '<ul>';
            for (let i = 0; i < chartsCount; i++) {
                // Access the chart
                const ch = sheet.charts.get(i);

                // Read chart type
                const typeStr = ch.type.toString();
                console.log(typeStr);

                // Change the title of the chart
                ch.title.text = "Chart Type is " + typeStr;

                logHtml += `<li>Chart ${i}: ${typeStr}</li>`;
            }
            logHtml += '</ul>';

            // Save the workbook to a downloadable file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out_excel2016Charts.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Charts updated successfully! Click the download link to get the modified file.</p>' + logHtml;
        });
    </script>
</html>
```  
## **مخرجات الوحدة**  


{{< highlight javascript >}}  

 Waterfall  

Treemap  

Sunburst  

Histogram  

BoxWhisker  

{{< /highlight >}}  

## **مواضيع متقدمة**  
- [إنشاء رسم بياني Waterfall](/cells/ar/javascript-cpp/creating-waterfall-chart/)  
- [إنشاء رسم بياني TreeMap](/cells/ar/javascript-cpp/creating-treemap-chart/)  
- [إنشاء رسم بياني Sunburst](/cells/ar/javascript-cpp/creating-sunburst-chart/)
