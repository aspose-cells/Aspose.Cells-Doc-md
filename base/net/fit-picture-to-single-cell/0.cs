using System;
using System.IO;
using Aspose.Cells;
using Aspose.Cells.Drawing;

string dataDir = "./";

// Create a new Workbook instance
Workbook workbook = new Workbook();

// Access the first worksheet
Worksheet worksheet = workbook.Worksheets[0];

// Open the image file and copy it into a MemoryStream
using (FileStream fs = new FileStream(dataDir + "sample.png", FileMode.Open, FileAccess.Read))
using (MemoryStream ms = new MemoryStream())
{
    fs.CopyTo(ms);
    ms.Position = 0;

    // Add picture anchored at row 5, column 2 (cell C6)
    int pictureIndex = worksheet.Pictures.Add(5, 2, ms);

    // Retrieve the newly added picture
    Picture picture = worksheet.Pictures[pictureIndex];

    // Move and resize with the cell
    picture.Placement = PlacementType.MoveAndSize;

    // Fit picture exactly to cell C6
    picture.UpperLeftRow = 5;
    picture.UpperLeftColumn = 2;
    picture.LowerRightRow = 6;
    picture.LowerRightColumn = 3;
}

// Save the workbook
workbook.Save(dataDir + "fitpicture.out.xlsx");