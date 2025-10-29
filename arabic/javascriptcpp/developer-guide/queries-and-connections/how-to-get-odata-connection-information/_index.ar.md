---
title: كيفية الحصول على معلومات اتصال OData باستخدام JavaScript عبر C++
linktitle: كيفية الحصول على معلومات اتصال OData
type: docs
weight: 60
url: /ar/javascript-cpp/how-to-get-odata-connection-information/
description: تعلّم كيف تستخرج معلومات اتصال OData من ملف Excel باستخدام Aspose.Cells for JavaScript عبر C++.
---

## **الحصول على معلومات اتصال OData**

قد يحتاج المطورون إلى استخراج معلومات OData من ملف Excel في بعض الحالات. يوفر Aspose.Cells for JavaScript عبر C++ الخاصية [**Workbook.dataMashup**](https://reference.aspose.com/cells/javascript-cpp/workbook/#dataMashup--) التي تُرجع معلومات DataMashup الموجودة في ملف Excel. تمثل هذه المعلومات من خلال فئة [**DataMashup**](https://reference.aspose.com/cells/javascript-cpp/datamashup). توفر الفئة [**DataMashup**](https://reference.aspose.com/cells/javascript-cpp/datamashup) الخاصية [**DataMashup.powerQueryFormulas**](https://reference.aspose.com/cells/javascript-cpp/datamashup/#powerQueryFormulas--) التي تُرجع مجموعة [**PowerQueryFormulaCollection**](https://reference.aspose.com/cells/javascript-cpp/powerqueryformulacollection). من [**PowerQueryFormulaCollection**](https://reference.aspose.com/cells/javascript-cpp/powerqueryformulacollection)، يمكنك الوصول إلى [**PowerQueryFormula**](https://reference.aspose.com/cells/javascript-cpp/powerqueryformula) و [**PowerQueryFormulaItem**](https://reference.aspose.com/cells/javascript-cpp/powerqueryformulaitem).

توضح مقتطفات الشفرة التالية استخدام هذه الفئات لاسترداد معلومات OData.

الملف المصدر المستخدم في مقطع الكود التالي مرفق للرجوع إليه.

[الملف المصدر](96928098.xlsx)

### **الكود المثالي**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Read Power Query Formulas</title>
    </head>
    <body>
        <h1>Read Power Query Formulas Example</h1>
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
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by loading the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access DataMashup and its PowerQueryFormulas collection
            const PQFcoll = workbook.dataMashup.powerQueryFormulas;

            let html = '<h2>Power Query Formulas</h2>';
            if (!PQFcoll || PQFcoll.count === 0) {
                html += '<p>No Power Query formulas found.</p>';
            } else {
                for (let i = 0; i < PQFcoll.count; i++) {
                    const PQF = PQFcoll.get(i);
                    html += `<h3>Connection Name: ${PQF.name}</h3>`;
                    const PQFIcoll = PQF.powerQueryFormulaItems;
                    if (!PQFIcoll || PQFIcoll.count === 0) {
                        html += '<p>No items found for this connection.</p>';
                    } else {
                        html += '<ul>';
                        for (let j = 0; j < PQFIcoll.count; j++) {
                            const PQFI = PQFIcoll.get(j);
                            html += `<li><strong>Name:</strong> ${PQFI.name} <br/><strong>Value:</strong> ${PQFI.value}</li>`;
                        }
                        html += '</ul>';
                    }
                }
            }

            document.getElementById('result').innerHTML = html;
        });
    </script>
</html>
```

### **مخرجات الوحدة**

{{< highlight java >}}

Connection Name: Orders

Name: Source

Value: OData.Feed("https://services.odata.org/V3/Northwind/Northwind.svc/", null, [Implementation="2.0"])

Name: Orders_table

Value: Source{[Name="Orders",Signature="table"]}[Data]

{{< /highlight >}}
