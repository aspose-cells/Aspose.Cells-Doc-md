public class CodeRunner {
    public static void main(String[] args) {
        try {
            // Step 1: Create a Workbook and get the first worksheet
            Workbook workbook = new Workbook();
            Worksheet worksheet = workbook.getWorksheets().get(0);
            Cells cells = worksheet.getCells();

            // Step 2: Write sample values 5, -3, 8, -2, 6 into cells A1:E1
            cells.get("A1").putValue(5);
            cells.get("B1").putValue(-3);
            cells.get("C1").putValue(8);
            cells.get("D1").putValue(-2);
            cells.get("E1").putValue(6);

            // Step 3: Build a CellArea pointing to destination cell F1
            CellArea dest = new CellArea();
            dest.StartColumn = 5;   // column F (0-indexed)
            dest.EndColumn = 5;
            dest.StartRow = 0;      // row 1 (0-indexed)
            dest.EndRow = 0;

            // Step 4: Add a Line sparkline from A1:E1 into F1
            // SparklineGroups.add returns the index of the newly added group
            int index = worksheet.getSparklineGroups().add(SparklineType.LINE, "A1:E1", false, dest);
            SparklineGroup group = worksheet.getSparklineGroups().get(index);

            // Step 5: Create a red CellsColor and assign it to the sparkline line color
            CellsColor red = workbook.createCellsColor();
            red.setColor(com.aspose.cells.Color.getRed());
            group.setSeriesColor(red);

            // Step 6: Enable high-point and low-point markers
            group.setShowHighPoint(true);
            group.setShowLowPoint(true);

            // Step 7: Save the workbook
            workbook.save("output_line.xlsx");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}