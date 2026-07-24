using System;
using Aspose.Cells;
using Aspose.Cells.Charts;

// Step 1: Create a Workbook and get the first worksheet
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];

// Step 2: Populate sample data in row 1 (A1:E1)
worksheet.Cells["A1"].PutValue(5);
worksheet.Cells["B1"].PutValue(-3);
worksheet.Cells["C1"].PutValue(8);
worksheet.Cells["D1"].PutValue(-2);
worksheet.Cells["E1"].PutValue(6);

// Step 3: Add a Line sparkline group at F1
CellArea lineArea = new CellArea();
lineArea.StartColumn = 5;
lineArea.EndColumn = 5;
lineArea.StartRow = 0;
lineArea.EndRow = 0;
int lineIdx = worksheet.SparklineGroups.Add(SparklineType.Line, "A1:E1", false, lineArea);
SparklineGroup lineGroup = worksheet.SparklineGroups[lineIdx];

// Customize the line sparkline color via CellsColor
CellsColor lineColor = workbook.CreateCellsColor();
lineColor.Color = System.Drawing.Color.Blue;
lineGroup.SeriesColor = lineColor;

// Step 4: Add a Column sparkline group at F2
CellArea columnArea = new CellArea();
columnArea.StartColumn = 5;
columnArea.EndColumn = 5;
columnArea.StartRow = 1;
columnArea.EndRow = 1;
int columnIdx = worksheet.SparklineGroups.Add(SparklineType.Column, "A1:E1", false, columnArea);
SparklineGroup columnGroup = worksheet.SparklineGroups[columnIdx];

// Customize the column sparkline series color
CellsColor columnColor = workbook.CreateCellsColor();
columnColor.Color = System.Drawing.Color.Green;
columnGroup.SeriesColor = columnColor;

// Step 5: Add a Win/Loss (Stacked) sparkline group at F3
CellArea stackedArea = new CellArea();
stackedArea.StartColumn = 5;
stackedArea.EndColumn = 5;
stackedArea.StartRow = 2;
stackedArea.EndRow = 2;
int stackedIdx = worksheet.SparklineGroups.Add(SparklineType.Stacked, "A1:E1", false, stackedArea);
SparklineGroup stackedGroup = worksheet.SparklineGroups[stackedIdx];

// Customize the win/loss sparkline series color
CellsColor stackedColor = workbook.CreateCellsColor();
stackedColor.Color = System.Drawing.Color.DarkOrange;
stackedGroup.SeriesColor = stackedColor;

// Step 6: Save the workbook
workbook.Save("output_all.xlsx");