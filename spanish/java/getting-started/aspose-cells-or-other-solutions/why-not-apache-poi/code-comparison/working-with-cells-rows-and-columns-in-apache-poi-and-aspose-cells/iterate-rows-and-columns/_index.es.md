---
title: Iterar Filas y Columnas
type: docs
weight: 50
url: /es/java/iterate-rows-and-columns/
description: Aprende cómo iterar Filas y Columnas a través de las Aspose.Cells for Java API.
keywords: Cómo Iterar Filas y Columnas en Java, Iterar Filas usando Java, Java Iterar Columnas. 
---

## **Cómo Iterar Filas y Columnas Usando Aspose.Cells for Java**

Las Filas y Columnas se pueden iterar usando la colección de filas y columnas.

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

## **Apache POI SS - HSSF XSSF -Iterar Filas y Columnas**

Se pueden iterar Filas y Celdas en la Hoja. El código de muestra se menciona a continuación:

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

## **Descargar Código en Ejecución**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)

## **Descargar Código de Ejemplo**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/cellsrowscolumns/iterate)

