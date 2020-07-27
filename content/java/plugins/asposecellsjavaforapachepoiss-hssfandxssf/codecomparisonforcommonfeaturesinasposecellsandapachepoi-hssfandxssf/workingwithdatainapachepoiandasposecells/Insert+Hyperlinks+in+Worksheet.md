+++
title = "Insert Hyperlinks in Worksheet" 
description = "" 
weight = 20618 
+++

Aspose.Cells for Java : Insert Hyperlinks in Worksheet  

# Aspose.Cells for Java : Insert Hyperlinks in Worksheet


## Aspose.Cells - Insert Hyperlinks in Worksheet

**Adding a Link to a Cell in the Same File**

It is possible to add hyperlinks to cells in the same Excel file by calling the Hyperlink collection's Add method. The Add method works for both internal and external hyperlinks.

**Java**

{{< code lang="java" >}}
//Obtaining the reference of the first worksheet.
WorksheetCollection worksheets = workbook.getWorksheets();
Worksheet sheet = worksheets.get(0);
HyperlinkCollection hyperlinks = sheet.getHyperlinks();

//Adding a hyperlink to a URL at "A1" cell
hyperlinks.add("A1",1,1,"http://www.aspose.com");

//============ Link to Cell =================
//Setting a value to the "A1" cell
Cells cells = sheet.getCells();
Cell cell = cells.get("A2");
cell.setValue("Link to B9");

setFormatting(cell);

hyperlinks = sheet.getHyperlinks();

//Adding an internal hyperlink to the "B9" cell of the other worksheet "Sheet1" in
//the same Excel file

hyperlinks.add("A2",1 ,1, "Sheet1!B9");

{{< /code >}}

**Adding a Link to an External File**

It is possible to add hyperlinks to external Excel files by calling the Hyperlinks collection's Add method. The Add method takes the following parameters:

*   Cell name, the name of the cell the hyperlink will be added to.
*   Number of rows, the number of rows in this hyperlink range.
*   Number of columns, the number of columns in this hyperlink range.
*   URL, the address of the target, external Excel file.

**Java**

cell = cells.get("A3");cell.setValue("External Link");setFormatting(cell);hyperlinks = sheet.getHyperlinks();//Adding a link to the external filehyperlinks.add("A3", 1, 1, "book1.xls");

## Apache POI SS - HSSF XSSF - Insert Hyperlinks in Worksheet

**Java**

CellStyle hlink\_style = wb.createCellStyle();Font hlink\_font = wb.createFont();hlink\_font.setUnderline(Font.U\_SINGLE);hlink\_font.setColor(IndexedColors.BLUE.getIndex());hlink\_style.setFont(hlink\_font);Cell cell;Sheet sheet = wb.createSheet("Hyperlinks");//URLcell = sheet.createRow(0).createCell((short)0);cell.setCellValue("URL Link");Hyperlink link = createHelper.createHyperlink(Hyperlink.LINK\_URL);link.setAddress("http://poi.apache.org/");cell.setHyperlink(link);cell.setCellStyle(hlink\_style);//link to a file in the current directorycell = sheet.createRow(1).createCell((short)0);cell.setCellValue("File Link");link = createHelper.createHyperlink(Hyperlink.LINK\_FILE);link.setAddress("link1.xls");cell.setHyperlink(link);cell.setCellStyle(hlink\_style);//e-mail linkcell = sheet.createRow(2).createCell((short)0);cell.setCellValue("Email Link");link = createHelper.createHyperlink(Hyperlink.LINK\_EMAIL);//note, if subject contains white spaces, make sure they are url-encodedlink.setAddress("mailto:poi@apache.org?subject=Hyperlinks");cell.setHyperlink(link);cell.setCellStyle(hlink\_style);//link to a place in this workbook//create a target sheet and cellSheet sheet2 = wb.createSheet("Target Sheet");sheet2.createRow(0).createCell((short)0).setCellValue("Target Cell");cell = sheet.createRow(3).createCell((short)0);cell.setCellValue("Worksheet Link");Hyperlink link2 = createHelper.createHyperlink(Hyperlink.LINK\_DOCUMENT);link2.setAddress("'Target Sheet'!A1");cell.setHyperlink(link2);cell.setCellStyle(hlink\_style);

## Download Running Code

*   [CodePlex](https://asposecellsjavaapachepoi.codeplex.com/releases/view/618615)
*   [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)

## Download Sample Code

*   [CodePlex](https://asposecellsjavaapachepoi.codeplex.com/SourceControl/latest#src/main/java/com/aspose/cells/examples/featurescomparison/datahandling/hyperlink/)
*   [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/src/main/java/com/aspose/cells/examples/featurescomparison/datahandling/hyperlink)

For more details, visit [Adding Hyperlinks to Link Data](http://docs.aspose.com:8082/docs/display/cellsjava/Adding+Hyperlinks+to+Link+Data).

