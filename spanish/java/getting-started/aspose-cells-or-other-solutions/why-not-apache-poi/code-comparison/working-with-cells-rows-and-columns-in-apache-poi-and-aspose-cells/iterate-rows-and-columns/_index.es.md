---
title: Iterar filas y columnas
type: docs
weight: 50
url: /es/java/iterate-rows-and-columns/
---
## **Aspose.Cells - Iterar filas y columnas**

Las filas y las columnas se pueden iterar utilizando la colección de filas y columnas.

**Java**

{{< highlight "java" >}}

 //Acceda al rango máximo de visualización

Rango rango = hoja de trabajo.getCells().getMaxDisplayRange();

int tcols = range.getColumnCount();

int trows = range.getRowCount();

System.out.println("Total de filas:" + trows);

System.out.println("Total de columnas:" + tcols);

RowCollection filas = celdas.getRows();

 para (int i = 0 ; i< rows.getCount() ; i++)

{

	for (int j = 0 ; j < tcols ; j++)

	{

		System.out.print(cells.get(i,j).getName() + " - " + cells.get(i,j).getValue() + "\t");

	}

	System.out.println("");

}

{{< /highlight >}}

## **Apache POI SS - HSSF XSSF - Iterar filas y columnas**

Las filas y Cells se pueden iterar en la hoja. El código de ejemplo se menciona a continuación:

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

## **Descargar código de ejecución**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)

## **Descargar código de muestra**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/cellsrowcolumns/iterate)

