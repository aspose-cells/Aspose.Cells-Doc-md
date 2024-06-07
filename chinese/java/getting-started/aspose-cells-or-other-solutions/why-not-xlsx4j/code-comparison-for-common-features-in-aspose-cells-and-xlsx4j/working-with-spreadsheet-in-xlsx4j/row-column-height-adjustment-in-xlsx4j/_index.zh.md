---
title: xlsx4j中的行列高度调整
type: docs
weight: 50
url: /zh/java/row-column-height-adjustment-in-xlsx4j/
---

## **Aspose.Cells - 行列高度调整**
可以通过调用Cells集合的setRowHeight方法来设置单行的高度。setRowHeight方法接受以下参数：

- **行索引**，要更改其高度的行的索引。
- **行高**，要应用于该行的行高。

通过调用Cells集合的setColumnWidth方法来设置列的宽度。setColumnWidth方法接受以下参数：

- **列索引**，要更改其宽度的列的索引。
- **列宽**，所需的列宽。

**Java**

{{< highlight java >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Accessing the first worksheet in the Excel file

Worksheet worksheet = workbook.getWorksheets().get(0);

Cells cells = worksheet.getCells();

//Setting the height of all rows in the worksheet to 8

worksheet.getCells().setStandardHeight(8f);

//Setting the height of the second row to 40

cells.setRowHeight(1, 40);



//Setting the width of the second column to 17.5

cells.setColumnWidth(1, 17.5);

{{< /highlight >}}
## **xlsx4j - 行列高度调整**
Row.setHt用于使用xlsx4j设置行的自定义高度。应该将setCustomHeight设置为TRUE。

**Java**

{{< highlight java >}}

 SpreadsheetMLPackage pkg = SpreadsheetMLPackage.createPackage();

WorksheetPart sheet = pkg.createWorksheetPart(new PartName("/sheet1.xml"), "Sheet1", 1);

CTSheetFormatPr format = Context.getsmlObjectFactory().createCTSheetFormatPr();

format.setDefaultRowHeight(5);

format.setCustomHeight(Boolean.TRUE);

sheet.getJaxbElement().setSheetFormatPr(format);

SheetData sheetData = sheet.getJaxbElement().getSheetData();

Row row = Context.getsmlObjectFactory().createRow();

row.setHt(66.0);

row.setCustomHeight(Boolean.TRUE);

row.setR(1L);

Cell cell1 = Context.getsmlObjectFactory().createCell();

cell1.setV("1234");

row.getC().add(cell1);

Cell cell2 = Context.getsmlObjectFactory().createCell();

cell2.setV("56");

row.getC().add(cell2);

sheetData.getRow().add(row);

{{< /highlight >}}
## **下载运行代码**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **下载示例代码**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/featurescomparison/worksheet/adjustheight)

{{% alert color="primary" %}} 

更多详细信息，请访问[调整行高和列宽](/java/adjusting-row-height-and-volumn-width)。

{{% /alert %}}
