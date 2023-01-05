---
title: Créer un tableau croisé dynamique dans xlsx4j
type: docs
weight: 20
url: /fr/java/create-pivot-table-in-xlsx4j/
---
## **Aspose.Cells - Créer un tableau croisé dynamique**
Pour créer un tableau croisé dynamique à l'aide de Aspose.Cells :

1. Ajoutez des données aux cellules d'une feuille de calcul à l'aide de la méthode PutValue/setValue d'un objet Cell. Vous utilisez également un fichier modèle déjà rempli de données. Les données seront utilisées comme source de données du tableau croisé dynamique.
1. Ajoutez un tableau croisé dynamique à la feuille de calcul en appelant la méthode add de la collection PivotTables (encapsulée dans l'objet Worksheet).
1. Accédez au nouvel objet PivotTable à partir de la collection PivotTables en transmettant son index. # Utilisez n'importe lequel des objets de tableau croisé dynamique encapsulés dans l'objet PivotTable pour gérer le tableau.

**Java**

{{< highlight "java" >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Obtaining the reference of the newly added worksheet

Worksheet sheet = workbook.getWorksheets().get(0);

sheet.setName("PivotTable");

Cells cells = sheet.getCells();

//Setting the value to the cells

Cell cell = cells.get("A1");

cell.setValue("Sport");

cell = cells.get("B1");

cell.setValue("Quarter");

cell = cells.get("C1");

cell.setValue("Sales");

cell = cells.get("A2");

cell.setValue("Golf");

cell = cells.get("A3");

cell.setValue("Golf");

cell = cells.get("A4");

cell.setValue("Tennis");

cell = cells.get("A5");

cell.setValue("Tennis");

cell = cells.get("A6");

cell.setValue("Tennis");

cell = cells.get("A7");

cell.setValue("Tennis");

cell = cells.get("A8");

cell.setValue("Golf");

cell = cells.get("B2");

cell.setValue("Qtr3");

cell = cells.get("B3");

cell.setValue("Qtr4");

cell = cells.get("B4");

cell.setValue("Qtr3");

cell = cells.get("B5");

cell.setValue("Qtr4");

cell = cells.get("B6");

cell.setValue("Qtr3");

cell = cells.get("B7");

cell.setValue("Qtr4");

cell = cells.get("B8");

cell.setValue("Qtr3");

cell = cells.get("C2");

cell.setValue(1500);

cell = cells.get("C3");

cell.setValue(2000);

cell = cells.get("C4");

cell.setValue(600);

cell = cells.get("C5");

cell.setValue(1500);

cell = cells.get("C6");

cell.setValue(4070);

cell = cells.get("C7");

cell.setValue(5000);

cell = cells.get("C8");

cell.setValue(6430);

PivotTableCollection pivotTables = sheet.getPivotTables();

//Adding a PivotTable to the worksheet

int index = pivotTables.add("=A1:C8","E3","PivotTable1");

//Accessing the instance of the newly added PivotTable

PivotTable pivotTable = pivotTables.get(index);

//Unshowing grand totals for rows.

pivotTable.setRowGrand(false);

//Dragging the first field to the row area.

pivotTable.addFieldToArea(PivotFieldType.ROW,0);

//Dragging the second field to the column area.

pivotTable.addFieldToArea(PivotFieldType.COLUMN,1);

//Dragging the third field to the data area.

pivotTable.addFieldToArea(PivotFieldType.DATA,2);

//Saving the Excel file

workbook.save(dataDir + "AsposePivotTable.xls");


{{< /highlight >}}
## **Télécharger le code d'exécution**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **Télécharger l'exemple de code**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/tables/createpivottable/AsposeCreatePivotTable.java)

{{% alert color="primary" %}} 

 Pour plus de détails, visitez[Créer des tableaux croisés dynamiques et des graphiques croisés dynamiques](/cells/fr/java/create-pivot-tables-and-pivot-charts).

{{% /alert %}}
