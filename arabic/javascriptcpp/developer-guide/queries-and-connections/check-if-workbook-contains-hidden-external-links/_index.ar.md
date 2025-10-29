---
title: التحقق مما إذا كان المصنف يحتوي على روابط خارجية مخفية باستخدام JavaScript عبر C++
linktitle: التحقق مما إذا كانت مصفوفة العمل تحتوي على روابط خارجية مخفية
type: docs
weight: 230
url: /ar/javascript-cpp/check-if-workbook-contains-hidden-external-links/
description: تعلّم كيفية التحقق مما إذا كان المصنف يحتوي على روابط خارجية مخفية باستخدام Aspose.Cells for JavaScript عبر C++.
---

## **سيناريوهات الاستخدام المحتملة**  
أحيانًا، يحتوي المصنف على روابط خارجية مخفية ولا يمكن رؤيتها في Microsoft Excel. تسترجع Aspose.Cells جميع الروابط الخارجية سواء كانت مرئية أم مخفية. ومع ذلك، يمكنك التحقق من خاصية [ExternalLink.isVisible()](https://reference.aspose.com/cells/javascript-cpp/externallink/#isVisible--) للتحقق مما إذا كان الرابط الخارجي مرئيًا أم لا.

## **التحقق مما إذا كانت مصفوفة العمل تحتوي على روابط خارجية مخفية**  
يحمّل الكود النموذجي التالي ملف Excel المصدر الذي يحتوي على روابط خارجية مخفية. لا يمكن عرض هذه الروابط في Microsoft Excel، لكنها موجودة داخل المصنف. بعد طباعة الخاصيتين [ExternalLink.dataSource](https://reference.aspose.com/cells/javascript-cpp/externallink/#dataSource--) و [ExternalLink.isReferred()](https://reference.aspose.com/cells/javascript-cpp/externallink/#isReferred--)، يتم طباعة خاصية [ExternalLink.isVisible()](https://reference.aspose.com/cells/javascript-cpp/externallink/#isVisible--). في المخرجات أدناه، ترى أن جميع الروابط الخارجية غير مرئية.

### **الكود المثالي**  
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - External Links</title>
    </head>
    <body>
        <h1>External Links Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result" style="white-space: pre-wrap; margin-top: 1em;"></div>
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

            // Instantiating a Workbook object by loading the selected file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the external link collection of the workbook
            const links = workbook.worksheets.externalLinks;

            // Print all the external links and check their IsVisible property
            let output = '';
            for (let i = 0; i < links.count; i++) {
                const link = links.get(i);
                output += "Data Source: " + link.dataSource + "\n";
                output += "Is Referred: " + link.isReferred + "\n";
                output += "Is Visible: " + link.isVisible + "\n\n";

                console.log("Data Source: " + link.dataSource);
                console.log("Is Referred: " + link.isReferred);
                console.log("Is Visible: " + link.isVisible);
                console.log();
            }

            document.getElementById('result').textContent = output || 'No external links found.';
        });
    </script>
</html>
```  

### **مخرجات الوحدة**  


{{< highlight java >}}  
 Data Source: C:\International\DDB\FAS 133\Swap Rates\GS_1M_3M_1_2_5_¥$_(B)IRSwaps_0400.xls  

Is Referred: True  

Is Visible: False  

Data Source: C:\DIST DAY\MAY TEMPLATES\030601t.xls  

Is Referred: True  

Is Visible: False  

Data Source: C:\AREVIEW\2002 Controllable\Autobrct.xls  

Is Referred: True  

Is Visible: False  

Data Source: C:\CARDSFO\Main Files\Rate Forecast\FY 11\IFR 11 01 (New Model REPORTS 11.08.07).xls  

Is Referred: True  

Is Visible: False  
{{< /highlight >}}
