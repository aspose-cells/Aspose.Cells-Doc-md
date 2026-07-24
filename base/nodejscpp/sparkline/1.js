let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);

// Step 2: Write sample values into A1:E1
let values = [5, -3, 8, -2, 6];
for (let i = 0; i < values.length; i++) {
    worksheet.getCells().get(0, i).putValue(values[i]);
}

// Step 3: Build a CellArea pointing to F1 (column index 5, row index 0)
let dest = new AsposeCells.CellArea();
dest.setStartColumn(5);
dest.setEndColumn(5);
dest.setStartRow(0);
dest.setEndRow(0);

// Step 4: Add a Column sparkline to the destination cell
let idx = worksheet.getSparklineGroups().add(
    AsposeCells.SparklineType.Column, "A1:E1", false, dest);
let group = worksheet.getSparklineGroups().get(idx);

// Step 5: Confirm the sparkline type by reading group.Type
console.log("Sparkline Type added: " + group.getType());

// Step 6: Save the workbook
workbook.save("output_column.xlsx");

console.log("Workbook saved as output_column.xlsx");