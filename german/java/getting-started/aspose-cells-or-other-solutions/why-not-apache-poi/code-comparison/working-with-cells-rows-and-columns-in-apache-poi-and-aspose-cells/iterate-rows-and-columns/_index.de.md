---
title: Zeilen und Spalten durchlaufen
type: docs
weight: 50
url: /de/java/iterate-rows-and-columns/
description: Erfahren Sie, wie man Zeilen und Spalten durch die Aspose.Cells for Java APIs durchläuft.
keywords: Wie man in Java Zeilen und Spalten durchläuft, Zeilen in Java durchläuft, Spalten in Java durchläuft. 
---

## **Wie man Zeilen und Spalten unter Verwendung von Aspose.Cells for Java durchläuft**

Zeilen und Spalten können unter Verwendung der Zeilen- und Spaltensammlung durchlaufen werden.

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

## **Apache POI SS - HSSF XSSF - Zeilen und Spalten durchlaufen**

Auf dem Arbeitsblatt können Zeilen und Zellen durchlaufen werden. Der Beispielcode ist unten aufgeführt:

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

## **Laufenden Code herunterladen**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)

## **Beispielcode herunterladen**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/cellsrowscolumns/iterate)

{{< app/cells/assistant language="java" >}}
