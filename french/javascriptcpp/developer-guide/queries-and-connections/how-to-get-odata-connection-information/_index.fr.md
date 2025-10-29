---
title: Comment obtenir les informations de connexion OData avec JavaScript via C++
linktitle: Comment obtenir les informations de connexion OData
type: docs
weight: 60
url: /fr/javascript-cpp/how-to-get-odata-connection-information/
description: Apprenez comment extraire les informations de connexion OData à partir d un fichier Excel en utilisant Aspose.Cells for JavaScript via C++.
---

## **Obtenir les informations de connexion OData**

Il peut arriver que les développeurs aient besoin d'extraire des informations OData du fichier Excel. Aspose.Cells for JavaScript via C++ fournit la propriété [**Workbook.dataMashup**](https://reference.aspose.com/cells/javascript-cpp/workbook/#dataMashup--) qui retourne les informations DataMashup présentes dans le fichier Excel. Ces informations sont représentées par la classe [**DataMashup**](https://reference.aspose.com/cells/javascript-cpp/datamashup). La classe [**DataMashup**](https://reference.aspose.com/cells/javascript-cpp/datamashup) fournit la propriété [**DataMashup.powerQueryFormulas**](https://reference.aspose.com/cells/javascript-cpp/datamashup/#powerQueryFormulas--) qui retourne la collection [**PowerQueryFormulaCollection**](https://reference.aspose.com/cells/javascript-cpp/powerqueryformulacollection). À partir de [**PowerQueryFormulaCollection**](https://reference.aspose.com/cells/javascript-cpp/powerqueryformulacollection), vous pouvez accéder à [**PowerQueryFormula**](https://reference.aspose.com/cells/javascript-cpp/powerqueryformula) et [**PowerQueryFormulaItem**](https://reference.aspose.com/cells/javascript-cpp/powerqueryformulaitem).

Le code suivant illustre l'utilisation de ces classes pour récupérer les informations OData.

Le fichier source utilisé dans l'extrait de code suivant est joint à titre de référence.

[Fichier source](96928098.xlsx)

### **Code d'exemple**

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

### **Sortie console**

{{< highlight java >}}

Connection Name: Orders

Name: Source

Value: OData.Feed("https://services.odata.org/V3/Northwind/Northwind.svc/", null, [Implementation="2.0"])

Name: Orders_table

Value: Source{[Name="Orders",Signature="table"]}[Data]

{{< /highlight >}}
