---
title: Créer des tableaux croisés dynamiques en utilisant Apache POI et Aspose.Cells
type: docs
weight: 40
url: /fr/java/create-pivot-tables-using-apache-poi-and-aspose-cells/
---

## **Aspose.Cells - Créer un tableau croisé dynamique**
Pour créer un tableau croisé dynamique en utilisant Aspose.Cells:

1. Ajoutez des données à des cellules de feuille de calcul en utilisant la méthode setValue d'un objet Cell. Vous pouvez également utiliser un fichier modèle déjà rempli de données. Les données seront utilisées comme source de données du tableau croisé dynamique.
2. Ajoutez un tableau croisé dynamique à la feuille de calcul en appelant la méthode add de PivotTableCollection (encapsulée dans l'objet {{Feuille de calcul}}).
3. Accédez au nouvel objet PivotTable de la collection PivotTableCollection en passant son index.

**Java**

{{< highlight java >}}

 // Instantiating a Workbook object

Workbook workbook = new Workbook();

// Obtaining the reference of the newly added worksheet

Worksheet sheet = workbook.getWorksheets().get(0);

sheet.setName("PivotTable");

Cells cells = sheet.getCells();

// Setting the value to the cells

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

// Adding a PivotTable to the worksheet

int index = pivotTables.add("=A1:C8", "E3", "PivotTable1");

// Accessing the instance of the newly added PivotTable

PivotTable pivotTable = pivotTables.get(index);

// Unshowing grand totals for rows.

pivotTable.setRowGrand(false);

// Dragging the first field to the row area.

pivotTable.addFieldToArea(PivotFieldType.ROW, 0);

// Dragging the second field to the column area.

pivotTable.addFieldToArea(PivotFieldType.COLUMN, 1);

// Dragging the third field to the data area.

pivotTable.addFieldToArea(PivotFieldType.DATA, 2);

{{< /highlight >}}
## **Apache POI SS (HSSF + XSSF) - Créer des tableaux croisés dynamiques**
**Java**

{{< highlight java >}}

 XSSFWorkbook wb = new XSSFWorkbook();

XSSFSheet sheet = wb.createSheet();

//Create some data to build the pivot table on

setCellData(sheet);

XSSFPivotTable pivotTable = sheet.createPivotTable(new AreaReference("A1:D4"), new CellReference("H5"));

//Configure the pivot table

//Use first column as row label

pivotTable.addRowLabel(0);

//Sum up the second column

pivotTable.addColumnLabel(DataConsolidateFunction.SUM, 1);

//Set the third column as filter

pivotTable.addColumnLabel(DataConsolidateFunction.AVERAGE, 2);

//Add filter on forth column

pivotTable.addReportFilter(3);

{{< /highlight >}}
## **Télécharger le code en cours d'exécution**
Télécharger des exemples en cours d'exécution pour **Créer des tableaux croisés dynamiques en utilisant Apache POI et Aspose.Cells** à partir de l'un des sites de codage social mentionnés ci-dessous:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells-Java-vs-POI-SS-v1.5)
## **Télécharger le code source**
Téléchargez le code source pour **Créer des tableaux croisés dynamiques en utilisant Apache POI et Aspose.Cells** à partir de l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java)

{{% alert color="primary" %}} 

Pour plus de détails, visitez [Créer des tableaux croisés dynamiques et des graphiques croisés dynamiques](/cells/fr/java/create-pivot-tables-and-pivot-charts/).

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
