---
title: JavaScript kullanarak C++ ile OData Bağlantısı Bilgisi nasıl alınır
linktitle: OData Bağlantı Bilgilerini Nasıl Alınır
type: docs
weight: 60
url: /tr/javascript-cpp/how-to-get-odata-connection-information/
description: C++ kullanarak Aspose.Cells for JavaScript ile Excel dosyasından OData bağlantı bilgisi nasıl çıkarılır öğrenin.
---

## **OData Bağlantı Bilgilerini Alın**

Geliştiricilerin bazen Excel dosyasından OData bilgisi çıkarması gerekebilir. Aspose.Cells for JavaScript C++ ile, Excel dosyasındaki DataMashup bilgilerinin döndürülmesini sağlayan [**Workbook.dataMashup**](https://reference.aspose.com/cells/javascript-cpp/workbook/#dataMashup--) özelliği sunar. Bu bilgiler [**DataMashup**](https://reference.aspose.com/cells/javascript-cpp/datamashup) sınıfı tarafından temsil edilir. [**DataMashup**](https://reference.aspose.com/cells/javascript-cpp/datamashup) sınıfı, [**DataMashup.powerQueryFormulas**](https://reference.aspose.com/cells/javascript-cpp/datamashup/#powerQueryFormulas--) özelliği ile [**PowerQueryFormulaCollection**](https://reference.aspose.com/cells/javascript-cpp/powerqueryformulacollection) koleksiyonunu döndürür. [**PowerQueryFormulaCollection**](https://reference.aspose.com/cells/javascript-cpp/powerqueryformulacollection) üzerinden [**PowerQueryFormula**](https://reference.aspose.com/cells/javascript-cpp/powerqueryformula) ve [**PowerQueryFormulaItem**](https://reference.aspose.com/cells/javascript-cpp/powerqueryformulaitem) erişebilirsiniz.

Aşağıdaki kod parçası, bu sınıfları kullanarak OData bilgisini almayı göstermektedir.

Aşağıdaki kod parçasında kullanılan Kaynak dosyası, referansınız için ekte bulunmaktadır.

[Kaynak Dosyası](96928098.xlsx)

### **Örnek Kod**

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

### **Konsol Çıktısı**

{{< highlight java >}}

Connection Name: Orders

Name: Source

Value: OData.Feed("https://services.odata.org/V3/Northwind/Northwind.svc/", null, [Implementation="2.0"])

Name: Orders_table

Value: Source{[Name="Orders",Signature="table"]}[Data]

{{< /highlight >}}
