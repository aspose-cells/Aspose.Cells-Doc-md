---
title: Vérifiez que la valeur de la cellule satisfait aux règles de validation des données
type: docs
weight: 210
url: /fr/javascript-cpp/verify-that-cell-value-satisfies-data-validation-rules/
description: Apprenez à vérifier si la valeur d une cellule satisfait les règles de validation de données via l API Aspose.Cells for JavaScript via C++.
keywords: Obtenez la valeur de validation de la cellule avec JavaScript via C++, Obtenez la valeur de validation de la cellule avec JavaScript via C++, Vérifiez si une valeur satisfait les règles de validation de données appliquées à la cellule avec JavaScript via C++
---

{{% alert color="primary" %}} 

Microsoft Excel permet aux utilisateurs d'ajouter des règles de validation des données aux cellules. Par exemple, une validation décimale précise que seuls des nombres compris entre 10 et 20 peuvent être saisis. Si un utilisateur entre un autre nombre, Excel affiche un message d'erreur et lui demande d'entrer un nombre dans la plage correcte. Si vous copiez et collez un nombre, disons 3, dans la cellule, Excel ne lance pas de vérification de validation ni n'affiche de message d'erreur.

Parfois, il est nécessaire de vérifier si une valeur satisfait les règles de validation des données appliquées à la cellule de manière programmée. Dans le cas ci-dessus, par exemple, l'entrée devrait échouer.

{{% /alert %}} 
## **Introduction**
Aspose.Cells for JavaScript via C++ fournit la propriété [Cell.validationValue](https://reference.aspose.com/cells/javascript-cpp/cell/#validationValue--) pour valider les valeurs des cellules de manière programmatique. Si la valeur dans une cellule ne satisfait pas la règle de validation de données appliquée à cette cellule, elle renvoie **false**, sinon **true**.

Le code d'exemple suivant illustre le fonctionnement de la propriété [Cell.validationValue](https://reference.aspose.com/cells/javascript-cpp/cell/#validationValue--). Tout d'abord, il entre la valeur 3 dans C1. Comme cela ne satisfait pas la règle de validation de données, la propriété [Cell.validationValue](https://reference.aspose.com/cells/javascript-cpp/cell/#validationValue--) renvoie **false**. Ensuite, il entre la valeur 15 dans C1. Comme cette valeur satisfait la règle de validation de données, la propriété [Cell.validationValue](https://reference.aspose.com/cells/javascript-cpp/cell/#validationValue--) renvoie **true**. De même, elle renvoie **false** pour la valeur 30.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Validation Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Validation Example</h1>
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
            const resultDiv = document.getElementById('result');
            resultDiv.innerHTML = '';

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access Cell C1
            // Cell C1 has the Decimal Validation applied on it.
            // It can take only the values Between 10 and 20
            const cell = worksheet.cells.get("C1");

            // Enter 3 inside this cell (not between 10 and 20)
            cell.value = 3;

            // Check if number 3 satisfies the Data Validation rule applied on this cell
            const valid3 = cell.validationValue;
            console.log("Is 3 a Valid Value for this Cell: " + valid3);
            resultDiv.innerHTML += `<p>Is 3 a Valid Value for this Cell: ${valid3}</p>`;

            // Enter 15 inside this cell (between 10 and 20)
            cell.value = 15;

            // Check if number 15 satisfies the Data Validation rule applied on this cell
            const valid15 = cell.validationValue;
            console.log("Is 15 a Valid Value for this Cell: " + valid15);
            resultDiv.innerHTML += `<p>Is 15 a Valid Value for this Cell: ${valid15}</p>`;

            // Enter 30 inside this cell (not between 10 and 20)
            cell.value = 30;

            // Check if number 30 satisfies the Data Validation rule applied on this cell
            const valid30 = cell.validationValue;
            console.log("Is 30 a Valid Value for this Cell: " + valid30);
            resultDiv.innerHTML += `<p>Is 30 a Valid Value for this Cell: ${valid30}</p>`;
        });
    </script>
</html>
```


### **Sortie**
{{< highlight javascript >}}

 Is 3 a Valid Value for this Cell: false

Is 15 a Valid Value for this Cell: true

Is 30 a Valid Value for this Cell: false

{{< /highlight >}}
