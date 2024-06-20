---
title: Itérer les lignes et les colonnes
type: docs
weight: 50
url: /fr/java/iterate-rows-and-columns/
description: Apprenez comment itérer les lignes et les colonnes à travers les Aspose.Cells for Java API.
keywords: Comment itérer les lignes et les colonnes en Java, Itérer sur les lignes en utilisant Java, Itérer sur les colonnes en Java. 
---

## **Comment itérer sur les lignes et les colonnes en utilisant Aspose.Cells for Java**

Les lignes et les colonnes peuvent être itérées en utilisant la collection de lignes et de colonnes.

**Java**

{{< highlight java >}}

 //Access the Maximum Display Range

Range range = worksheet.getCells().getMaxDisplayRange();

int tcols = range.getColumnCount();

int trows = range.getRowCount();

System.out.println("Total Rows:" + trows);

System.out.println("Total Cols:" + tcols);

RowCollection rows = cells.getRows();

for (int i = 0 ; i < rows.getCount() ; i++)

{

	for (int j = 0 ; j < tcols ; j++)

	{

		System.out.print(cells.get(i,j).getName() + " - " + cells.get(i,j).getValue() + "\t");

	}

	System.out.println("");

}

{{< /highlight >}}

## **Apache POI SS - HSSF XSSF - Itérer sur les lignes et les colonnes**

Les lignes et les cellules peuvent être itérées sur la feuille. Le code d'exemple est mentionné ci-dessous :

**Java**

{{< highlight java >}}

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

## **Télécharger le code en cours d'exécution**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)

## **Télécharger le code source d'exemple**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/cellsrowscolumns/iterate)

