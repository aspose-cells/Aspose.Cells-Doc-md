let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
worksheet.setName("WinLoss");

// Step 2: Populate sample data in row 1: A1=5, B1=-3, C1=8, D1=-2, E1=6
worksheet.getCells().get("A1").putValue(5);
worksheet.getCells().get("B1").putValue(-3);
worksheet.getCells().get("C1").putValue(8);
worksheet.getCells().get("D1").putValue(-2);
worksheet.getCells().get("E1").putValue(6);

// Step 3: Build a CellArea pointing to F1 (column 5, row 0)
let dest = new AsposeCells.CellArea();
dest.setStartColumn(5);   // F
dest.setEndColumn(5);
dest.setStartRow(0);      // row 1
dest.setEndRow(0);

// Step 4: Add a Win/Loss sparkline (SparklineType.Stacked)
let groupIndex = worksheet.getSparklineGroups().add(
    AsposeCells.SparklineType.Stacked,
    "A1:E1",
    false,
    dest
);
let group = worksheet.getSparklineGroups().get(groupIndex);

// Step 5: Customize the sparkline group
// Enable high-point and low-point markers
group.setShowHighPoint(true);
group.setShowLowPoint(true);
group.setShowNegativePoints(true);

// Set the high-point color to green
let highColor = workbook.createCellsColor();
highColor.setColor(AsposeCells.Color.getGreen());
group.setHighPointColor(highColor);

// Set the low-point color to red
let lowColor = workbook.createCellsColor();
lowColor.setColor(AsposeCells.Color.getRed());
group.setLowPointColor(lowColor);

// Set the negative-point color to orange
let negColor = workbook.createCellsColor();
negColor.setColor(AsposeCells.Color.getOrange());
group.setNegativePointsColor(negColor);

// Set the default series color (used for positive bars)
let seriesColor = workbook.createCellsColor();
seriesColor.setColor(AsposeCells.Color.getSteelBlue());
group.setSeriesColor(seriesColor);

// Step 6: Save the workbook
workbook.save("output_winloss.xlsx");

console.log("Workbook saved successfully: output_winloss.xlsx");