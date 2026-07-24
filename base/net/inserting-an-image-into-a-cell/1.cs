var workbook = new Workbook();
var worksheet = workbook.Worksheets[0];

// Get the target cell C6
var cell = worksheet.Cells["C6"];

// Read the image file into a byte array
byte[] imageData = File.ReadAllBytes("logo.png");

// Embed the image directly into the cell
cell.EmbeddedImage = imageData;

// Optionally adjust row height and column width so the embedded image is more visible
worksheet.Cells.SetColumnWidth(2, 30);   // Column C (index 2)
worksheet.Cells.SetRowHeight(5, 100);     // Row 6 (index 5)

// Save the resulting workbook as an .xlsx file
workbook.Save("output.xlsx", SaveFormat.Xlsx);