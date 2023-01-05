---
title: Obtenir le contenu Cell
type: docs
weight: 10
url: /fr/java/getting-cell-contents/
---
## **Aspose.Cells - Obtenir Cell Contenu**
La méthode Cells.get() est disponible pour accéder aux cellules.

**Java**

{{< highlight "java" >}}

 //Accéder à la première feuille de calcul du fichier Excel

feuille de calcul feuille de calcul = workbook.getWorksheets().get(0);

Cells cellules = feuille de calcul.getCells();

// Accéder à la plage d'affichage maximale

Plage plage = worksheet.getCells().getMaxDisplayRange();

int tcols = range.getColumnCount();

int trows = range.getRowCount();

System.out.println("Nombre total de lignes :" + lignes );

System.out.println("Total Cols :" + tcols);

// Valeur d'accès de Cell B4

//=====================================================

System.out.println(cells.get("B4").getValue());

Cell cellule = cellules.get(3,1); //Valeur d'accès de Cell B4

System.out.println(cell.getValue());

//=====================================================

RowCollection rows = cells.getRows();

 pour (int je = 0 ; je< rows.getCount() ; i++)

{

	for (int j = 0 ; j < tcols ; j++)

	{

		if (cells.get(i,j).getType() != CellValueType.IS_NULL)

		{

			System.out.println(cells.get(i,j).getName() + " - " + cells.get(i,j).getValue());

		}

	}

}

{{< /highlight >}}
## **Apache POI SS - HSSF XSSF - Obtenir le contenu Cell**
Apache POI fournit la classe Cell pour accéder à diverses propriétés des cellules.

**Java**

{{< highlight "java" >}}

 Sheet sheet1 = wb.getSheetAt(0);

for (Row row : sheet1) {

    for (Cell cell : row) {

        CellReference cellRef = new CellReference(row.getRowNum(), cell.getColumnIndex());

        System.out.print(cellRef.formatAsString());

        System.out.print(" - ");

        switch (cell.getCellType()) {

            case Cell.CELL_TYPE_STRING:

                System.out.println(cell.getRichStringCellValue().getString());

                break;

            case Cell.CELL_TYPE_NUMERIC:

                if (DateUtil.isCellDateFormatted(cell)) {

                    System.out.println(cell.getDateCellValue());

                } else {

                    System.out.println(cell.getNumericCellValue());

                }

                break;

            case Cell.CELL_TYPE_BOOLEAN:

                System.out.println(cell.getBooleanCellValue());

                break;

            case Cell.CELL_TYPE_FORMULA:

                System.out.println(cell.getCellFormula());

                break;

            default:

                System.out.println();

        }

    }

}

{{< /highlight >}}
## **Télécharger le code d'exécution**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Télécharger l'exemple de code**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/datahandling/gettingcellcontent)

{{% alert color="primary" %}} 

 Pour plus de détails, visitez[Fonctionnalités de traitement des données utilisant Aspose.Cells](/cells/fr/java/data-handling-features-using-aspose-cells/)

{{% /alert %}}
