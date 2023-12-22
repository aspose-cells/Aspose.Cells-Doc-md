---
title: Itérer les lignes et les colonnes
type: docs
weight: 50
url: /fr/java/iterate-rows-and-columns/
description: Découvrez comment itérer des lignes et des colonnes via les API Aspose.Cells for Java.
keywords: How to Iterate Rows and Columns in Java, Iterate Rows using Java, Java Iterate Columns. 
---
##  **Comment itérer des lignes et des colonnes à l'aide de Aspose.Cells for Java**

Les lignes et les colonnes peuvent être itérées à l'aide de la collection de lignes et de colonnes.

**Java**

{{< highlight "java" >}}

 //Accès à la plage d'affichage maximale

Range range = worksheet.getCells().getMaxDisplayRange();

int tcols = range.getColumnCount();

int trows = range.getRowCount();

System.out.println("Total des lignes :" + trows);

System.out.println("Total Cols :" + tcols);

Lignes RowCollection = cellules.getRows();

 pour (int je = 0 ; je< rows.getCount() ; i++)

{

	for (int j = 0 ; j < tcols ; j++)

	{

		System.out.print(cells.get(i,j).getName() + " - " + cells.get(i,j).getValue() + "\t");

	}

	System.out.println("");

}

{{< /highlight >}}

##  **Apache POI SS - HSSF XSSF - Itérer les lignes et les colonnes**

Les lignes et Cells peuvent être itérées sur la feuille. Un exemple de code est mentionné ci-dessous :

**Java**

{{< highlight "java" >}}

 Workbook wb = WorkbookFactory.create(inStream);

Sheet sheet = wb.getSheetAt(0);

for (Row row : sheet)

{

  for (Cell cell : row)

  {

    System.out.println("Iteration.");

  }

}

{{< /highlight >}}

##  **Télécharger le code d'exécution**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)

##  **Télécharger un exemple de code**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/cellsrowscolumns/iterate)

