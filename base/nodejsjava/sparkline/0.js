let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
let cells = worksheet.getCells();

// Step 2: Write sample values 5, -3, 8, -2, 6 into cells A1:E1
cells.get("A1").putValue(5);
cells.get("B1").putValue(-3);
cells.get("C1").putValue(8);
cells.get("D1").putValue(-2);
cells.get("E1").putValue(6);

// Step 3: Build a CellArea pointing to destination cell F1
let dest = new AsposeCells.CellArea();
dest.setStartColumn(5);   // column F (0-indexed)
dest.setEndColumn(5);
dest.setStartRow(0);      // row 1 (0-indexed)
dest.setEndRow(0);

// Step 4: Add a Line sparkline from A1:E1 into F1
// SparklineGroups.Add returns the index of the newly added group
let index = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Line, "A1:E1", false, dest);
let group = worksheet.getSparklineGroups().get(index);

// Step 5: Create a red CellsColor and assign it to the sparkline line color
let red = workbook.createCellsColor();
red.setColor(AsposeCells.Color.fromArgb(255, 0, 0));
group.setSeriesColor(red);

// Step 6: Enable high-point and low-point markers
group.setShowHighPoint(true);
group.setShowLowPoint(true);

// Step 7: Save the workbook
workbook.save("output_line.xlsx");