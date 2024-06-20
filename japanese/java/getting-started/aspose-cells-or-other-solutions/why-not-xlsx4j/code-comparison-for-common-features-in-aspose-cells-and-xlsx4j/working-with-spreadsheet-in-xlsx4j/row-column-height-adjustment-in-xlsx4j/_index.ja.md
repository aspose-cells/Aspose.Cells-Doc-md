---
title: xlsx4j で行列の高さを調整する
type: docs
weight: 50
url: /ja/java/row-column-height-adjustment-in-xlsx4j/
---

## **Aspose.Cells - 行列の高さを調整する**
Cells 集合の setRowHeight メソッドを呼び出すことで、単一の行の高さを設定することが可能です。 setRowHeight メソッドは、以下のパラメータを取ります。

- **行インデックス**：高さを変更する行のインデックス。
- **行の高さ**：行に適用する行の高さ。

Cells 集合の setColumnWidth メソッドを呼び出すことで、列の幅を設定することが可能です。 setColumnWidth メソッドは、以下のパラメータを取ります。

- **列インデックス**：幅を変更する列のインデックス。
- **列の幅**：設定したい列の幅。

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
## **xlsx4j - 行列の高さを調整する**
Row.setHt を使用して、xlsx4j を使用して行のカスタム高さを設定します。 setCustomHeight は TRUE に設定する必要があります。

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
## **ランニングコードのダウンロード**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **サンプルコードをダウンロード**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/featurescomparison/worksheet/adjustheight)

{{% alert color="primary" %}} 

詳細については、[行の高さと列の幅を調整](/java/adjusting-row-height-and-volumn-width) をご覧ください。

{{% /alert %}}
