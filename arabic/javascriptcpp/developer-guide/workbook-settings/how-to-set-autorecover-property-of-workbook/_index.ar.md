---
title: كيفية تعيين خاصية الاسترداد التلقائي للمصنف باستخدام جافا سكريبت عبر C++
linktitle: كيفية تعيين خاصية AutoRecover للفصل
type: docs
weight: 220
url: /ar/javascript-cpp/how-to-set-autorecover-property-of-workbook/
description: تعلم كيفية تعيين خاصية الاسترداد التلقائي لمصنف باستخدام Aspose.Cells for JavaScript عبر C++.
---

{{% alert color="primary" %}}  
يمكنك استخدام Aspose.Cells لتعيين خاصية AutoRecover للمصنف. القيمة الافتراضية لهذه الخاصية هي **true**. عند تعيينها على **false** في مصنف، يقوم Microsoft Excel بتعطيل AutoRecover (النسخ التلقائي) على ذلك الملف.  

يوفر Aspose.Cells خاصية [**Workbook.autoRecover**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#autoRecover--) لتمكين أو تعطيل هذا الخيار.  
{{% /alert %}}  

يوضح الكود التالي كيفية استخدام خاصية [**Workbook.autoRecover**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#autoRecover--) للمصنف. يقرأ أولاً القيمة الافتراضية لهذه الخاصية وهي **true**، ثم يعينها إلى **false** ويحفظ المصنف. ثم يفتح المصنف مرة أخرى ويقرأ قيمة الخاصية التي تكون **false** الآن.  

## كود جافا سكريبت لتعيين خاصية الاسترداد التلقائي للمصنف  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - AutoRecover</title>
    </head>
    <body>
        <h1>AutoRecover Property Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
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
            const resultDiv = document.getElementById('result');
            resultDiv.innerHTML = '';

            // Create workbook object
            const workbook = new Workbook();

            // Read AutoRecover property
            const autoRecoverBefore = workbook.settings.autoRecover;
            resultDiv.innerHTML += `<p>AutoRecover before: ${autoRecoverBefore}</p>`;

            // Set AutoRecover property to false
            workbook.settings.autoRecover = false;

            // Save the workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download output_out.xlsx';

            // Read the saved workbook again from the saved data
            const workbook2 = new Workbook(new Uint8Array(outputData));

            // Read AutoRecover property
            const autoRecoverAfter = workbook2.settings.autoRecover;
            resultDiv.innerHTML += `<p>AutoRecover after reload: ${autoRecoverAfter}</p>`;
        });
    </script>
</html>
```  

## **الناتج**  



{{< highlight java >}}  
AutoRecover: True  
AutoRecover: False  
{{< /highlight >}}
