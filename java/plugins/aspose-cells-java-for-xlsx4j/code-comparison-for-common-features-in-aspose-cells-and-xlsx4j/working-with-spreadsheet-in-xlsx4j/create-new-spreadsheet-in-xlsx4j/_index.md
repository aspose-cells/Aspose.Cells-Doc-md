---
title: Create New Spreadsheet in xlsx4j
type: docs
weight: 30
url: /java/create-new-spreadsheet-in-xlsx4j/
---

## **Aspose.Cells - Create New Spreadsheet**
Workbook class is available for simple use.

**Java**

{{< highlight java >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Adding a new worksheet to the Workbook object

WorksheetCollection worksheets = workbook.getWorksheets();

Worksheet worksheet = worksheets.add("My Worksheet");

Cells cells = worksheet.getCells();

//Adding some value to cell

Cell cell = cells.get("A1");

cell.setValue("This is Aspose test of fonts!");

//Saving the Excel file

workbook.save(dataDir + "newWorksheet_Aspose.xls");

{{< /highlight >}}
## **xlsx4j - Create New Spreadsheet**
Below sample shows how new spreadsheet can be created while using xlsx4j.

**Java**

{{< highlight java >}}

 public static void main(String[] args) throws Exception {

    String outputfilepath = dataDir + "newWorksheet_Xlsx4j.xlsx";

    SpreadsheetMLPackage pkg = SpreadsheetMLPackage.createPackage();

    WorksheetPart sheet = pkg.createWorksheetPart(new PartName("/xl/worksheets/sheet1.xml"), "Sheet1", 1);

    addContent(sheet);

    SaveToZipFile saver = new SaveToZipFile(pkg);

    saver.save(outputfilepath);

    System.out.println("\n\n done .. " + outputfilepath);

}

private static void addContent(WorksheetPart sheet) {

    // Minimal content already present

    SheetData sheetData = sheet.getJaxbElement().getSheetData();

    // Now add

    Row row = Context.getsmlObjectFactory().createRow();

    Cell cell = Context.getsmlObjectFactory().createCell();

    cell.setV("1234");

    row.getC().add(cell);

    row.getC().add(createCell("hello world!"));

    sheetData.getRow().add(row);

}

/**

    // Note: if you are trying to add characters, not a number,

    // the easiest approach is to use inline strings (as opposed to the shared string table).

    // See http://openxmldeveloper.org/blog/b/openxmldeveloper/archive/2011/11/22/screen-cast-write-simpler-spreadsheetml-when-generating-spreadsheets.aspx

    // and http://www.docx4java.org/forums/xlsx-java-f15/cells-with-character-values-t874.html

 */

private static Cell createCell(String content) {

    Cell cell = Context.getsmlObjectFactory().createCell();

    CTXstringWhitespace ctx = Context.getsmlObjectFactory().createCTXstringWhitespace();

    ctx.setValue(content);

    CTRst ctrst = new CTRst();

    ctrst.setT(ctx);

    cell.setT(STCellType.INLINE_STR);

    cell.setIs(ctrst); // add ctrst as inline string

    return cell;

}

{{< /highlight >}}
## **Download Running Code**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **Download Sample Code**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/featurescomparison/workbook/createnewspreadsheet)

{{% alert color="primary" %}} 

For more details, visit [File Handling Features](/java/file-handling-features).

{{% /alert %}}
