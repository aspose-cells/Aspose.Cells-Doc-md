---
title: Hur man får OData anslutningsinformation med JavaScript via C++
linktitle: Hur man får OData anslutningsinformation
type: docs
weight: 60
url: /sv/javascript-cpp/how-to-get-odata-connection-information/
description: Lär dig hur du hämtar OData anslutningsinformation från en Excel fil med Aspose.Cells for JavaScript via C++.
---

## **Få OData-anslutningsinformation**

Det kan finnas fall där utvecklare behöver extrahera OData-information från Excel-filen. Aspose.Cells for JavaScript via C++ ger egenskapen [**Workbook.dataMashup**](https://reference.aspose.com/cells/javascript-cpp/workbook/#dataMashup--) som returnerar DataMashup-informationen som finns i Excel-filen. Denna information representeras av klassen [**DataMashup**](https://reference.aspose.com/cells/javascript-cpp/datamashup). Klassen [**DataMashup**](https://reference.aspose.com/cells/javascript-cpp/datamashup) tillhandahåller egenskapen [**DataMashup.powerQueryFormulas**](https://reference.aspose.com/cells/javascript-cpp/datamashup/#powerQueryFormulas--) som returnerar [**PowerQueryFormulaCollection**](https://reference.aspose.com/cells/javascript-cpp/powerqueryformulacollection)-samlingen. Från [**PowerQueryFormulaCollection**](https://reference.aspose.com/cells/javascript-cpp/powerqueryformulacollection) kan du få tillgång till [**PowerQueryFormula**](https://reference.aspose.com/cells/javascript-cpp/powerqueryformula) och [**PowerQueryFormulaItem**](https://reference.aspose.com/cells/javascript-cpp/powerqueryformulaitem).

Följande kodsnutt visar användningen av dessa klasser för att hämta OData-informationen.

Källfilen som används i den följande kodsnutten bifogas för din referens.

[Källfil](96928098.xlsx)

### **Exempelkod**

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

### **Konsoloutput**

{{< highlight java >}}

Connection Name: Orders

Name: Source

Value: OData.Feed("https://services.odata.org/V3/Northwind/Northwind.svc/", null, [Implementation="2.0"])

Name: Orders_table

Value: Source{[Name="Orders",Signature="table"]}[Data]

{{< /highlight >}}
