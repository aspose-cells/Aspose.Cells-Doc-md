using System;
using System.IO;
using Aspose.Cells;
using Aspose.Cells.Drawing;

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];

using (FileStream fs = new FileStream("logo.png", FileMode.Open, FileAccess.Read))
{
    int picIndex = worksheet.Pictures.Add(5, 2, fs);
    Picture picture = worksheet.Pictures[picIndex];
    picture.UpperLeftRow = 5;
    picture.UpperLeftColumn = 2;
    picture.LowerRightRow = 6;
    picture.LowerRightColumn = 3;
    picture.Placement = PlacementType.MoveAndSize;
}

workbook.Save("output.xlsx", SaveFormat.Xlsx);