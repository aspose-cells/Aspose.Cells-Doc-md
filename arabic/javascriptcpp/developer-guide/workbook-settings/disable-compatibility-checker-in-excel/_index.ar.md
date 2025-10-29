---
title: تعطيل مدقق التوافق في إكسل باستخدام جافا سكريبت عبر C++
linktitle: تعطيل فاحص التوافق في الإكسيل
type: docs
weight: 170
url: /ar/javascript-cpp/disable-compatibility-checker-in-excel/
description: تعلم كيفية تعطيل مدقق التوافق من خلال Aspose.Cells for JavaScript عبر API C++.
keywords: تعطيل مدقق التوافق جافا سكريبت، تعطيل مدقق التوافق في إكسل عبر جافا سكريبت باستخدام C++، تعطيل مدقق التوافق في المصنف.
---

## تعطيل مدقق التوافق في أوراق عمل إكسل في جافا سكريبت  

{{% alert color="primary" %}}  
يُعلق مُدقق التوافق في Microsoft Excel علامة عند حفظ ملف في تنسيق ملف أقدم قد يتسبب في مشكلات الوظائف أو فقدان الصِدق. مُدقق التوافق هو ميزة في Microsoft Office Excel 2007 و Microsoft Excel 2010.  

عند حفظ دفتر عمل في إصدار سابق، Excel 97 من خلال Excel 2003، من Excel 2007 أو Excel 2010، يقوم مُدقق التوافق بفحص الدفتر لمعرفة ما إذا كان يحتوي على ميزات لا تدعمها الإصدار السابق. لمساعدتك في اتخاذ قرارات حول كيفية التعامل مع مشكلات التوافق، يعرض مُدقق التوافق صناديق حوار مع خيارات. يمكن أيضًا استخدامه لإنشاء تقرير عن أي مشكلات في الدفتر، أو تعطيل الميزة.  

أحيانًا، تحتاج إلى تعطيل مدقق التوافق لمصنف معين. مع واجهات برمجة التطبيقات Aspose.Cells، يمكنك فعل ذلك برمجياً بحيث لا يُشعر المستخدمون بالإحباط أو الارتباك عند ظهور مربع حوار مدقق التوافق عند إعادة حفظ الملف في Microsoft Excel يدويًا.  
{{% /alert %}}  

## **كيفية تعطيل مُدقق التوافق باستخدام Microsoft Excel**  

- (Excel 2007) على زر الأوفيس، انقر على **إعداد**, ثم **تشغيل مُدقق التوافق**, ثم قم بمسح خيار **التحقق من التوافق عند حفظ هذا الدفتر**.  

- (Excel 2010) على علامة التبويب الملف، انقر فوق **معلومات**, ثم **البحث عن مشكلات**, انقر على **التحقق من التوافق**, وبصورة نهائية، قم بمسح خيار **التحقق من التوافق عند حفظ هذا الدفتر**.  
كيفية تعطيل مُدقق التوافق باستخدام واجهات برمجة التطبيقات لـ Aspose.Cells  

## **قم بتعيين الخاصية {0} إلى **False** لتعطيل مُدقق التوافق في Microsoft Excel.**  

قم بضبط خاصية [**Workbook.checkCompatibility**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#checkCompatibility--) على **false** لتعطيل مدقق التوافق في Microsoft Excel.  

### **أمثلة على الشفرة**  

 تظهر الأمثلة البرمجية التالية كيفية تعطيل مدقق التوافق باستخدام Aspose.Cells for JavaScript عبر C++.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Disable Compatibility Checker Example</h1>
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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Disable the compatibility checker
            workbook.settings.checkCompatibility = false;

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Output_BK_CompCheck.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Compatibility check disabled. Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
