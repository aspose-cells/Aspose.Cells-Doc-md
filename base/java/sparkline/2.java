import com.aspose.cells.*;
import com.aspose.cells.charts.*;
import com.aspose.cells.drawing.*;
import java.awt.Color;

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
worksheet.setName("WinLoss");

// Populate sample data
worksheet.getCells().get("A1").putValue(5);
worksheet.getCells().get("B1").putValue(-3);
worksheet.getCells().get("C1").putValue(8);
worksheet.getCells().get("D1").putValue(-2);
worksheet.getCells().get("E1").putValue(6);

// Build a CellArea pointing to F1 (column 5, row 0)
CellArea dest = new CellArea();
dest.setStartColumn(5);
dest.setEndColumn(5);
dest.setStartRow(0);
dest.setEndRow(0);

// Add a Win/Loss sparkline (SparklineType.Stacked)
int groupIndex = worksheet.getSparklineGroups().add(SparklineType.STACKED, "A1:E1", false, dest);
SparklineGroup group = worksheet.getSparklineGroups().get(groupIndex);

// Customize the sparkline group
group.setShowHighPoint(true);
group.setShowLowPoint(true);
group.setShowNegativePoints(true);

// Set the high-point color to green
CellsColor highColor = workbook.createCellsColor();
highColor.setColor(Color.GREEN);
group.setHighPointColor(highColor);

// Set the low-point color to red
CellsColor lowColor = workbook.createCellsColor();
lowColor.setColor(Color.RED);
group.setLowPointColor(lowColor);

// Set the negative-point color to orange
CellsColor negColor = workbook.createCellsColor();
negColor.setColor(Color.ORANGE);
group.setNegativePointsColor(negColor);

// Set the default series color (used for positive bars)
CellsColor seriesColor = workbook.createCellsColor();
seriesColor.setColor(new Color(70, 130, 180)); // SteelBlue approximation
group.setSeriesColor(seriesColor);

// Save the workbook
workbook.save("output_winloss.xlsx");

System.out.println("Workbook saved successfully: output_winloss.xlsx");