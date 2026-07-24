var workbook = new AsposeCells.Workbook();
var worksheet = workbook.getWorksheets().get(0);

// Get the target cell C6
var cell = worksheet.getCells().get("C6");

// Read the image file into a byte array
var imageData = fs.readFileSync("logo.png");

// Embed the image directly into the cell
cell.setEmbeddedImage(imageData);

// Optionally adjust row height and column width so the embedded image is more visible
worksheet.getCells().setColumnWidth(2, 30);   // Column C (index 2)
worksheet.getCells().setRowHeight(5, 100);     // Row 6 (index 5)

// Save the resulting workbook as an .xlsx file
workbook.save("output.xlsx", AsposeCells.SaveFormat.Xlsx);