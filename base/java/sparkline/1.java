import com.aspose.cells.*;

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);

// Write sample values into A1:E1
int[] values = new int[] { 5, -3, 8, -2, 6 };
for (int i = 0; i < values.length; i++) {
    worksheet.getCells().get(0, i).putValue(values[i]);
}

// Build a CellArea pointing to F1 (column index 5, row index 0)
CellArea dest = new CellArea();
dest.setStartColumn(5);
dest.setEndColumn(5);
dest.setStartRow(0);
dest.setEndRow(0);

// Add a Column sparkline to the destination cell
int idx = worksheet.getSparklineGroups().add(SparklineType.COLUMN, "A1:E1", false, dest);
SparklineGroup group = worksheet.getSparklineGroups().get(idx);

// Confirm the sparkline type by reading group.Type
System.out.println("Sparkline Type added: " + group.getType());

// Save the workbook
workbook.save("output_column.xlsx");

System.out.println("Workbook saved as output_column.xlsx");