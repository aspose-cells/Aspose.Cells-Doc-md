---
title: Iterieren Sie Zeilen und Spalten
type: docs
weight: 50
url: /de/java/iterate-rows-and-columns/
description: Erfahren Sie, wie Sie Zeilen und Spalten über die APIs Aspose.Cells for Java iterieren.
keywords: How to Iterate Rows and Columns in Java, Iterate Rows using Java, Java Iterate Columns. 
---
##  **So iterieren Sie Zeilen und Spalten mit Aspose.Cells for Java**

Zeilen und Spalten können mithilfe der Zeilen- und Spaltensammlung iteriert werden.

**Java**

{{< highlight "java" >}}

 //Greifen Sie auf den maximalen Anzeigebereich zu

Bereichsbereich = worksheet.getCells().getMaxDisplayRange();

int tcols = range.getColumnCount();

int trows = range.getRowCount();

System.out.println("Total Rows:" + trows);

System.out.println("Total Cols:" + tcols);

RowCollection rows = cell.getRows();

 für (int i = 0 ; i< rows.getCount() ; i++)

{

	for (int j = 0 ; j < tcols ; j++)

	{

		System.out.print(cells.get(i,j).getName() + " - " + cells.get(i,j).getValue() + "\t");

	}

	System.out.println("");

}

{{< /highlight >}}

##  **Apache POI SS – HSSF XSSF – Zeilen und Spalten iterieren**

Zeilen und Cells können auf dem Blatt iteriert werden. Beispielcode ist unten aufgeführt:

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

##  **Laden Sie Running Code herunter**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)

##  **Beispielcode herunterladen**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/cellsrowscolumns/iterate)

