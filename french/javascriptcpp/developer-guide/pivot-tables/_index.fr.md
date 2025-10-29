---
title: Insérer un tableau croisé dynamique
linktitle: Tableaux croisés dynamiques
type: docs
weight: 160
url: /fr/javascript-cpp/create-pivot-table/
description: Créer et formater des tableaux croisés dynamiques de fichiers de feuilles de calcul Excel.
---

## **Créer un tableau croisé dynamique**

Il est possible d'utiliser Aspose.Cells for JavaScript via C++ pour ajouter des tableaux croisés dynamiques aux feuilles de calcul de manière programmatique.

### **Modèle d'objet de tableau croisé dynamique**

Aspose.Cells for JavaScript via C++ fournit un ensemble spécial de classes utilisées pour créer et contrôler des tableaux croisés dynamiques. Ces classes servent à créer et à définir des objets [**PivotTable**](https://reference.aspose.com/cells/javascript-cpp/pivottable), les éléments de base d'un tableau croisé dynamique. Les objets sont :

- [**PivotField**](https://reference.aspose.com/cells/javascript-cpp/pivotfield) représente un champ dans un [**PivotTable**](https://reference.aspose.com/cells/javascript-cpp/pivottable).
- [**PivotFieldCollection**](https://reference.aspose.com/cells/javascript-cpp/pivotfieldcollection) représente une collection de tous les objets [**PivotField**](https://reference.aspose.com/cells/javascript-cpp/pivotfield) dans le [**PivotTable**](https://reference.aspose.com/cells/javascript-cpp/pivottable).
- [**PivotTable**](https://reference.aspose.com/cells/javascript-cpp/pivottable) représente un PivotTable dans une feuille de calcul.
- [**PivotTableCollection**](https://reference.aspose.com/cells/javascript-cpp/pivottablecollection) représente une collection de tous les objets [**PivotTable**](https://reference.aspose.com/cells/javascript-cpp/pivottable) sur une feuille de calcul.

### **Création d'un tableau croisé dynamique simple avec Aspose.Cells**

1. Ajoutez des données à une feuille de calcul en utilisant la méthode [**putValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#putValue-boolean-) de l'objet [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell).
   Ces données seront utilisées comme source de données du tableau croisé dynamique.
1. Ajoutez un tableau croisé dynamique à la feuille de calcul en appelant la méthode [**add**](https://reference.aspose.com/cells/javascript-cpp/pivottablecollection/#add-string-string-string-) de la collection [**PivotTables**](https://reference.aspose.com/cells/javascript-cpp/pivottablecollection), qui est encapsulée dans l'objet FeuilleDeCalcul.
1. Accédez au nouvel objet [**PivotTable**](https://reference.aspose.com/cells/javascript-cpp/pivottable) de la collection [**PivotTables**](https://reference.aspose.com/cells/javascript-cpp/pivottablecollection) en passant l'indice de PivotTable.
1. Utilisez l'un des objets [**PivotTable**](https://reference.aspose.com/cells/javascript-cpp/pivottable) (expliqués ci-dessus) pour gérer le tableau croisé dynamique.

Après l'exécution du code d'exemple, un tableau croisé dynamique est ajouté à la feuille de calcul.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Create Pivot Table Example</h1>
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

            document.getElementById('runExample').addEventListener('click', async () => {
                // Instantiate a new Workbook object
                const workbook = new Workbook();

                // Obtaining the reference of the newly added worksheet
                const sheetIndex = workbook.worksheets.add();
                const sheet = workbook.worksheets.get(sheetIndex);
                const cells = sheet.cells;

                // Setting the value to the cells
                let cell = cells.get("A1");
                cell.value = "Sport";
                cell = cells.get("B1");
                cell.value = "Quarter";
                cell = cells.get("C1");
                cell.value = "Sales";

                cell = cells.get("A2");
                cell.value = "Golf";
                cell = cells.get("A3");
                cell.value = "Golf";
                cell = cells.get("A4");
                cell.value = "Tennis";
                cell = cells.get("A5");
                cell.value = "Tennis";
                cell = cells.get("A6");
                cell.value = "Tennis";
                cell = cells.get("A7");
                cell.value = "Tennis";
                cell = cells.get("A8");
                cell.value = "Golf";

                cell = cells.get("B2");
                cell.value = "Qtr3";
                cell = cells.get("B3");
                cell.value = "Qtr4";
                cell = cells.get("B4");
                cell.value = "Qtr3";
                cell = cells.get("B5");
                cell.value = "Qtr4";
                cell = cells.get("B6");
                cell.value = "Qtr3";
                cell = cells.get("B7");
                cell.value = "Qtr4";
                cell = cells.get("B8");
                cell.value = "Qtr3";

                cell = cells.get("C2");
                cell.value = 1500;
                cell = cells.get("C3");
                cell.value = 2000;
                cell = cells.get("C4");
                cell.value = 600;
                cell = cells.get("C5");
                cell.value = 1500;
                cell = cells.get("C6");
                cell.value = 4070;
                cell = cells.get("C7");
                cell.value = 5000;
                cell = cells.get("C8");
                cell.value = 6430;

                const pivotTables = sheet.pivotTables;

                // Adding a PivotTable to the worksheet
                const index = pivotTables.add("=A1:C8", "E3", "PivotTable2");

                // Accessing the instance of the newly added PivotTable
                const pivotTable = pivotTables.get(index);

                // Unshowing grand totals for rows.
                pivotTable.rowGrand = false;

                // Dragging the first field to the row area.
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, 0);

                // Dragging the second field to the column area.
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, 1);

                // Dragging the third field to the data area.
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, 2);

                // Saving the Excel file
                const outputData = workbook.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById('downloadLink');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = 'CreatePivotTable_out.xlsx';
                downloadLink.style.display = 'block';
                downloadLink.textContent = 'Download Excel File';

                document.getElementById('result').innerHTML = '<p style="color: green;">Pivot table created successfully! Click the download link to get the file.</p>';
            });
        });
    </script>
</html>
```

{{% alert color="primary" %}}

Lors de l'attribution d'une plage de cellules en tant que source de données, la plage doit aller du coin supérieur gauche au coin inférieur droit. Par exemple, "A1:C3" est valide mais "C3:A1" ne l'est pas.

{{% /alert %}}
