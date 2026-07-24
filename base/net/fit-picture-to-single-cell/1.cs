// For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-.NET
using System;
using System.IO;
using Aspose.Cells;

string dataDir = "./";

// Create a new Workbook instance
Workbook workbook = new Workbook();

// Access the first worksheet
Aspose.Cells.Worksheet worksheet = workbook.Worksheets[0];

// Read the image file into a byte array
byte[] imageData = File.ReadAllBytes(dataDir + "sample.png");

// Access the target cell at row 5, column 2 (cell C6 in 1-based terms)
Cell cell = worksheet.Cells[5, 2];

// Embed the image directly inside the cell
cell.EmbeddedImage = imageData;

// Save the workbook to the output file
workbook.Save(dataDir + "embeddedimage.out.xlsx");