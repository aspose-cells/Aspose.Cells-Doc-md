---
title: Insérer un tableau croisé dynamique
description: Créez et mettez en forme des tableaux croisés dynamiques de fichiers de feuilles de calcul Excel à l'aide d'Aspose.Cells pour Node.js via Java.
linktitle: Tableaux croisés dynamiques
url: /fr/nodejs-java/create-pivot-table/
type: docs
weight: 160
keywords: Créer un tableau croisé dynamique, Insérer un tableau croisé dynamique, Mettre en forme un tableau croisé dynamique, Aspose.Cells pour Node.js via Java.
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Créer un tableau croisé dynamique**
Il est possible d'utiliser Aspose.Cells pour ajouter des tableaux croisés dynamiques aux feuilles de calcul par programmation.

### **Modèle d'objet du tableau croisé dynamique**
Aspose.Cells fournit un ensemble de classes utilisées pour créer et contrôler des tableaux croisés dynamiques. Les éléments constitutifs sont:
- `PivotField` représente un champ dans un `PivotTable`.
- `PivotFieldCollection` représente une collection de tous les objets `PivotField` dans le `PivotTable`.
- `PivotTable` représente un tableau croisé dynamique sur une feuille de calcul.
- `PivotTableCollection` représente une collection de tous les objets `PivotTable` sur une feuille de calcul.

### **Créer un tableau croisé dynamique simple à l'aide d'Aspose.Cells**
1. Ajoutez des données à une feuille de calcul à l'aide de la méthode `putValue` de la cellule. Ces données serviront de source de données pour le tableau croisé dynamique.
2. Ajoutez un tableau croisé dynamique à la feuille de calcul en appelant la méthode `add` de la collection `PivotTables`, encapsulée dans l'objet feuille de calcul.
3. Accédez au nouvel objet `PivotTable` de la collection `PivotTables` en passant l'index du tableau croisé dynamique.
4. Utilisez n'importe lequel des objets `PivotTable` (expliqués ci-dessus) pour gérer le tableau croisé dynamique.

Après l'exécution du code d'exemple, un tableau croisé dynamique est ajouté à la feuille de calcul.

```javascript
var dataDir = "./";

// Instantiating a Workbook object
var workbook = new AsposeCells.Workbook();

// Obtaining the reference of the newly added worksheet
var sheet = workbook.getWorksheets().get(0);

var cells = sheet.getCells();

// Setting the value to the cells
var cell = cells.get("A1");
cell.putValue("Sport");
cell = cells.get("B1");
cell.putValue("Quarter");
cell = cells.get("C1");
cell.putValue("Sales");

cell = cells.get("A2");
cell.putValue("Golf");
cell = cells.get("A3");
cell.putValue("Golf");
cell = cells.get("A4");
cell.putValue("Tennis");
cell = cells.get("A5");
cell.putValue("Tennis");
cell = cells.get("A6");
cell.putValue("Tennis");
cell = cells.get("A7");
cell.putValue("Tennis");
cell = cells.get("A8");
cell.putValue("Golf");

cell = cells.get("B2");
cell.putValue("Qtr3");
cell = cells.get("B3");
cell.putValue("Qtr4");
cell = cells.get("B4");
cell.putValue("Qtr3");
cell = cells.get("B5");
cell.putValue("Qtr4");
cell = cells.get("B6");
cell.putValue("Qtr3");
cell = cells.get("B7");
cell.putValue("Qtr4");
cell = cells.get("B8");
cell.putValue("Qtr3");

cell = cells.get("C2");
cell.putValue(1500);
cell = cells.get("C3");
cell.putValue(2000);
cell = cells.get("C4");
cell.putValue(600);
cell = cells.get("C5");
cell.putValue(1500);
cell = cells.get("C6");
cell.putValue(4070);
cell = cells.get("C7");
cell.putValue(5000);
cell = cells.get("C8");
cell.putValue(6430);

var pivotTables = sheet.getPivotTables();

// Adding a PivotTable to the worksheet
var index = pivotTables.add("=A1:C8", "E3", "PivotTable2");

// Accessing the instance of the newly added PivotTable
var pivotTable = pivotTables.get(index);

// Unshowing grand totals for rows.
pivotTable.setRowGrand(false);

// Draging the first field to the row area.
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Row, 0);

// Draging the second field to the column area.
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Column, 1);

// Draging the third field to the data area.
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Data, 2);

// Saving the Excel file
workbook.save(dataDir + "pivotTable_test_out.xls");
```

{{% alert color="primary" %}}
Lors de l'affectation d'une plage de cellules comme source de données, la plage doit aller du coin supérieur gauche au coin inférieur droit. Par exemple, "A1:C3" est valide mais "C3:A1" ne l'est pas.
{{% /alert %}}

## Related Articles
- [Add Filter Fields to a Pivot Table in Aspose.Cells for Node.js via Java](/cells/fr/nodejs-java/add-page-field-in-pivot-table/)
- [Apply Styles to Pivot Tables in Aspose.Cells for Node.js via Java](/cells/fr/nodejs-java/apply-style-to-pivot-table/)
- [Modify Page Field Layout in Pivot Table](/cells/fr/nodejs-java/change-page-field-layout/)
- [Filtering Pivot Tables by Label or Value](/cells/fr/nodejs-java/filter-by-label-or-value-of-pivot-table/)
- [Manage Pivot Table Value Fields in Aspose.Cells for Node.js via Java](/cells/fr/nodejs-java/manage-value-fields/)

{{< app/cells/assistant language="nodejs-java" >}}