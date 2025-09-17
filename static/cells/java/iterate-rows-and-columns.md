##Iterate Rows and Columns
Learn how to Iterate Rows and Columns through the Aspose.Cells for Java APIs.
## **How to Iterate Rows and Columns Using Aspose.Cells for Java**
Rows and Columns can be iterated using rows and columns collection.
**Java**
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
## **Apache POI SS - HSSF XSSF - Iterate Rows and Columns**
Rows and Cells can be iterated on Sheet. Sample code is mentioned below:
**Java**
Workbook wb = WorkbookFactory.create(inStream);
Sheet sheet = wb.getSheetAt(0);
for (Row row : sheet)
{
for (Cell cell : row)
{
System.out.println("Iteration.");
}
}
## **Download Running Code**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Download Sample Code**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/cellsrowscolumns/iterate)
