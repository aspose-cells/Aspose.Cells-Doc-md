+++
title = "Iterate Rows and Columns" 
description = "" 
weight = 20610 
+++

Aspose.Cells for Java : Iterate Rows and Columns  

# Aspose.Cells for Java : Iterate Rows and Columns


## Aspose.Cells - Iterate Rows and Columns

Rows and Columns can be iterated using rows and columns collection.

**Java**

{{< code lang="java" >}}
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
{{< /code >}}

## Apache POI SS - HSSF XSSF - Iterate Rows and Columns

Rows and Cells can be iterated on Sheet. Sample code is mentioned below:

**Java**

{{< code lang="java" >}}
Workbook wb = WorkbookFactory.create(inStream);
Sheet sheet = wb.getSheetAt(0);
for (Row row : sheet)
{
  for (Cell cell : row)
  {
    System.out.println("Iteration.");
  }
}
{{< /code >}}

## Download Running Code

*   [CodePlex](https://asposecellsjavaapachepoi.codeplex.com/releases/view/618615)
*   [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)

## Download Sample Code

*   [CodePlex](https://asposecellsjavaapachepoi.codeplex.com/SourceControl/latest#src/main/java/com/aspose/cells/examples/featurescomparison/cellsrowscolumns/iterate/)
*   [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/src/main/java/com/aspose/cells/examples/featurescomparison/cellsrowscolumns/iterate)

For more details, visit [Working with Data](http://docs.aspose.com:8082/docs/display/cellsjava/Working+with+Data).

