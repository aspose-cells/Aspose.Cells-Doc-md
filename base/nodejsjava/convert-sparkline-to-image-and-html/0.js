let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);

// Populate sample data in cells A1:E1
worksheet.getCells().get("A1").putValue(5);
worksheet.getCells().get("B1").putValue(-3);
worksheet.getCells().get("C1").putValue(8);
worksheet.getCells().get("D1").putValue(-2);
worksheet.getCells().get("E1").putValue(6);

// Add a Line sparkline group anchored at F1 (column 5, row 0)
let lineArea = new AsposeCells.CellArea();
lineArea.setStartColumn(5);
lineArea.setEndColumn(5);
lineArea.setStartRow(0);
lineArea.setEndRow(0);
let lineIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Line, "A1:E1", false, lineArea);

// Add a Column sparkline group anchored at G1 (column 6, row 0)
let columnArea = new AsposeCells.CellArea();
columnArea.setStartColumn(6);
columnArea.setEndColumn(6);
columnArea.setStartRow(0);
columnArea.setEndRow(0);
let columnIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Column, "A1:E1", false, columnArea);

// Add a Win/Loss (Stacked) sparkline group anchored at H1 (column 7, row 0)
let stackedArea = new AsposeCells.CellArea();
stackedArea.setStartColumn(7);
stackedArea.setEndColumn(7);
stackedArea.setStartRow(0);
stackedArea.setEndRow(0);
let stackedIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Stacked, "A1:E1", false, stackedArea);

// Configure image options for PNG output
let imageOptions = new AsposeCells.ImageOrPrintOptions();
imageOptions.setImageType(AsposeCells.ImageType.Png);

// Convert the Line sparkline to image and embed it in cell F2
let lineSp = worksheet.getSparklineGroups().get(lineIdx).getSparklines().get(0);
let lineMs = new java.io.ByteArrayOutputStream();
lineSp.toImage(lineMs, imageOptions);
worksheet.getCells().get("F2").setEmbeddedImage(lineMs.toByteArray());

// Convert the Column sparkline to image and embed it in cell G2
let columnSp = worksheet.getSparklineGroups().get(columnIdx).getSparklines().get(0);
let columnMs = new java.io.ByteArrayOutputStream();
columnSp.toImage(columnMs, imageOptions);
worksheet.getCells().get("G2").setEmbeddedImage(columnMs.toByteArray());

// Convert the Win/Loss sparkline to image and embed it in cell H2
let stackedSp = worksheet.getSparklineGroups().get(stackedIdx).getSparklines().get(0);
let stackedMs = new java.io.ByteArrayOutputStream();
stackedSp.toImage(stackedMs, imageOptions);
worksheet.getCells().get("H2").setEmbeddedImage(stackedMs.toByteArray());

// Save the workbook to disk
workbook.save("output_with_sparklines.xlsx");