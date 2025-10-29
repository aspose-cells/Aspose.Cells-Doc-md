---
title: استخدام فئة ChartGlobalizationSettings لضبط لغة مختلفة لمكون المخطط باستخدام جافا سكريبت عبر C++
linktitle: استخدام فئة ChartGlobalizationSettings لتعيين لغة مختلفة لعنصر رسم بياني
description: تعلم كيفية استخدام فئة ChartGlobalizationSettings في Aspose.Cells for Javaسكريبت عبر C++ لضبط لغات مختلفة لمكونات المخطط. دليلنا سيساعدك على فهم كيفية توطين عناصر المخطط، التسميات، والأساطير.
keywords: Aspose.Cells for Javaسكريبت عبر C++، رسم بياني، عولمة المخطط، لغات، توطين، ChartGlobalizationSettings، العناصر، التسميات، الأساطير.
type: docs
weight: 2200
url: /ar/javascript-cpp/using-chartglobalizationsettings-class-to-set-different-language-for-chart-component/
---

## **سيناريوهات الاستخدام المحتملة**  

قامت APIs الخاصة بـ Aspose.Cells بالكشف عن فئة [**ChartGlobalizationSettings**](https://reference.aspose.com/cells/javascript-cpp/chartglobalizationsettings/) للتعامل مع السيناريوهات التي يرغب فيها المستخدم في تعيين مكونات المخطط إلى لغات مختلفة وتسميات مخصصة للمجاميع الفرعية في جدول البيانات.  

## **مقدمة في فئة ChartGlobalizationSettings**  

تقدم فئة [**ChartGlobalizationSettings**](https://reference.aspose.com/cells/javascript-cpp/chartglobalizationsettings/) حالياً الطرق الثمانية التالية والتي يمكن تجاوزها في فئة مخصصة لترجمة مثل اسم عنوان المحور، اسم وحدة المحور، اسم عنوان المخطط، وغيرها إلى لغات مختلفة.  
1. [**ChartGlobalizationSettings.axisTitleName**](https://reference.aspose.com/cells/javascript-cpp/chartglobalizationsettings/#axisTitleName--): يحصل على اسم العنوان للمحور.  
1. [**ChartGlobalizationSettings.axisUnitName(DisplayUnitType)**](https://reference.aspose.com/cells/javascript-cpp/chartglobalizationsettings/#axisUnitName-displayunittype-): يحصل على اسم وحدة المحور.  
1. [**ChartGlobalizationSettings.chartTitleName**](https://reference.aspose.com/cells/javascript-cpp/chartglobalizationsettings/#chartTitleName--): يحصل على اسم عنوان الرسم البياني.  
1. [**ChartGlobalizationSettings.legendDecreaseName**](https://reference.aspose.com/cells/javascript-cpp/chartglobalizationsettings/#legendDecreaseName--): يحصل على اسم الانخفاض لوحة التفسير.  
1. [**ChartGlobalizationSettings.legendIncreaseName**](https://reference.aspose.com/cells/javascript-cpp/chartglobalizationsettings/#legendIncreaseName--): يحصل على اسم زيادة للوسيلة التوضيحية.  
1. [**ChartGlobalizationSettings.legendTotalName**](https://reference.aspose.com/cells/javascript-cpp/chartglobalizationsettings/#legendTotalName--): يحصل على اسم الإجمالي لوحة التفسير.  
1. [**ChartGlobalizationSettings.otherName**](https://reference.aspose.com/cells/javascript-cpp/chartglobalizationsettings/#otherName--): يحصل على اسم تسميات "أخرى" للرسم البياني.  
1. [**ChartGlobalizationSettings.seriesName**](https://reference.aspose.com/cells/javascript-cpp/chartglobalizationsettings/#seriesName--): يحصل على اسم السلاسل في الرسم البياني.  

### **ترجمة لغة مخصصة**  
هنا، سنقوم بإنشاء رسم بياني شلالي استنادًا إلى البيانات التالية. سيتم عرض أسماء مكونات الرسم البياني باللغة الإنجليزية في الرسم البياني. سنستخدم مثال باللغة التركية لنريك كيفية عرض عنوان الرسم البياني وأسماء زيادة/انخفاض لوحة التفسير واسم الإجمالي وعنوان المحور باللغة التركية.  

![todo:image_alt_text](sample.png)  

## **الكود المثالي**  
يقوم الكود العيني التالي بتحميل [ملف Excel العيني](waterfall.xlsx).  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Chart Globalization Settings Example</title>
    </head>
    <body>
        <h1>Chart Globalization Settings Example (Turkey)</h1>
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

        // Define TurkeyChartGlobalizationSettings by converting getXxx methods to properties
        class TurkeyChartGlobalizationSettings extends AsposeCells.ChartGlobalizationSettings {
            constructor() {
                super();
                this.chartTitleName = "Grafik Başlığı"; // Chart Title
                this.legendIncreaseName = "Artış"; // Increase
                this.legendDecreaseName = "Düşüş"; // Decrease
                this.legendTotalName = "Toplam"; // Total
                this.axisTitleName = "Eksen Başlığı"; // Axis Title
            }
        }

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const resultDiv = document.getElementById('result');
            resultDiv.innerHTML = '';

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            // No try-catch: let errors propagate
            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate Workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Set custom chartGlobalizationSettings (Turkey)
            workbook.settings.globalizationSettings.chartSettings = new TurkeyChartGlobalizationSettings();

            // Access the first worksheet and its charts
            const worksheet = workbook.worksheets.get(0);
            const chartCollection = worksheet.charts;
            const chart = chartCollection.get(0);

            // Calculate the chart
            chart.calculate();

            // Get the chart title text
            const title = chart.title;
            const titleText = title ? title.text : "(No Title)";

            // Prepare output messages
            const messages = [];
            messages.push('<p style="color: green;">Operation completed successfully!</p>');
            messages.push(`<p>Workbook chart title: ${titleText}</p>`);

            // Get legend labels and output them
            const legendEntriesLabels = chart.legend.legendLabels;
            if (legendEntriesLabels && legendEntriesLabels.forEach) {
                const legendItems = [];
                legendEntriesLabels.forEach(label => {
                    legendItems.push(`<li>${label}</li>`);
                });
                if (legendItems.length) {
                    messages.push('<p>Workbook chart legend:</p>');
                    messages.push(`<ul>${legendItems.join('')}</ul>`);
                } else {
                    messages.push('<p>(No legend labels found)</p>');
                }
            } else {
                messages.push('<p>(No legend or legend labels available)</p>');
            }

            // Save modified workbook to allow download (optional)
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = messages.join('');
        });
    </script>
</html>
```  

## الإخراج الذي تم توليده بواسطة رمز العينة  

هذا هو إنتاج الكونسول للكود العيني أعلاه.  

{{< highlight javascript >}}  

Workbook chart title: Grafik Başlığı  

Workbook chart legend: Artış  

Workbook chart legend: Düşüş  

Workbook chart legend: Toplam  

Workbook category axis title: Eksen Başlığı  

{{< /highlight >}}
