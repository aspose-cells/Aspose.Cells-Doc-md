let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);

// Step 2: Populate sample data in row 1 (A1:E1)
worksheet.getCells().get("A1").putValue(5);
worksheet.getCells().get("B1").putValue(-3);
worksheet.getCells().get("C1").putValue(8);
worksheet.getCells().get("D1").putValue(-2);
worksheet.getCells().get("E1").putValue(6);

// Step 3: Add a Line sparkline group at F1
let lineArea = new AsposeCells.CellArea();
lineArea.setStartColumn(5);
lineArea.setEndColumn(5);
lineArea.setStartRow(0);
lineArea.setEndRow(0);
let lineIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Line, "A1:E1", false, lineArea);
let lineGroup = worksheet.getSparklineGroups().get(lineIdx);

// Customize the line sparkline color via CellsColor
let lineColor = workbook.createCellsColor();
lineColor.setColor(AsposeCells.Color.Blue);
lineGroup.setSeriesColor(lineColor);

// Step 4: Add a Column sparkline group at F2
let columnArea = new AsposeCells.CellArea();
columnArea.setStartColumn(5);
columnArea.setEndColumn(5);
columnArea.setStartRow(1);
columnArea.setEndRow(1);
let columnIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Column, "A1:E1", false, columnArea);
let columnGroup = worksheet.getSparklineGroups().get(columnIdx);

// Customize the column sparkline series color
let columnColor = workbook.createCellsColor();
columnColor.setColor(AsposeCells.Color.Green);
columnGroup.setSeriesColor(columnColor);

// Step 5: Add a Win/Loss (Stacked) sparkline group at F3
let stackedArea = new AsposeCells.CellArea();
stackedArea.setStartColumn(5);
stackedArea.setEndColumn(5);
stackedArea.setStartRow(2);
stackedArea.setEndRow(2);
let stackedIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Stacked, "A1:E1", false, stackedArea);
let stackedGroup = worksheet.getSparklineGroups().get(stackedIdx);

// Customize the win/loss sparkline series color
let stackedColor = workbook.createCellsColor();
stackedColor.setColor(AsposeCells.Color.DarkOrange);
stackedGroup.setSeriesColor(stackedColor);

// Step 6: Save the workbook
workbook.save("output_all.xlsx");