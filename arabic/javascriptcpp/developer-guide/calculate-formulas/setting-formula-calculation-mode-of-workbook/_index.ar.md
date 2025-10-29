---
title: إعداد وضع حساب الصيغة للمصنف باستخدام JavaScript عبر C++
linktitle: ضبط وضع حساب الصيغ لسجل العمل
description: تقدم هذه المقالة كيفية ضبط وضع حساب الصيغة للمصنف في Microsoft Excel باستخدام Aspose.Cells for JavaScript عبر C++. من خلال تحميل ملف إكسل موجود أو إنشاء ملف جديد، يمكننا استخدام الخاصية التي توفرها Aspose.Cells لضبط وضع حساب الصيغة والحصول على النتيجة. وأخيرًا، نحفظ ملف إكسل المعدل على القرص.
keywords: Aspose.Cells, إكسل، دفتر العمل، وضع حساب الصيغة، الإعدادات، جافا سكريبت عبر C++
type: docs
weight: 110
url: /ar/javascript-cpp/setting-formula-calculation-mode-of-workbook/
---

{{% alert color="primary" %}}  
يتيح Microsoft Excel لك تعيين وضع حساب الصيغة، أي الطريقة التي يتم بها حساب الصيغ. هناك ثلاثة قيم ممكنة:  

- تلقائي - إعادة الحساب كلما تم تغيير شيء ما، وفي كل مرة يتم فيها فتح دفتر العمل.  
- تلقائي ما عدا الجداول البيانية - إعادة الحساب كلما تم تغيير شيء ما، ولكن دون الجداول البيانية.  
- يدوي - إعادة الحساب فقط عندما يطلب المستخدم ذلك صراحة عن طريق الضغط على F9 أو CTRL+ALT+F9، أو عند حفظ دفتر العمل.  
{{% /alert %}}  

لتعيين وضع حساب الصيغ في Microsoft Excel:  

1. حدد **الصيغ** ثم **خيارات الحساب**.  
1. حدد أحد الخيارات.  

Aspose.Cells for JavaScript عبر C++ يتيح أيضًا تعيين **وضع حساب الصيغة** باستخدام خاصية الوضع [**FormulaSettings.calculationMode**](https://reference.aspose.com/cells/javascript-cpp/formulasettings/#calculationMode--). يمكنك تعيينه إلى التعداد [**CalcModeType**](https://reference.aspose.com/cells/javascript-cpp/calcmodetype) الذي يحتوي على إحدى القيم التالية:  

- CalcModeType.Automatic  
- CalcModeType.AutomaticExceptTable  
- CalcModeType.Manual  

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
            // Creating a workbook
            const workbook = new Workbook();

            // Set the Formula Calculation Mode to Manual
            workbook.settings.formulaSettings.calculationMode = AsposeCells.CalcModeType.Manual;

            // Save the workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and saved successfully. Click the download link to get the file.</p>';
        });
    </script>
</html>
```
