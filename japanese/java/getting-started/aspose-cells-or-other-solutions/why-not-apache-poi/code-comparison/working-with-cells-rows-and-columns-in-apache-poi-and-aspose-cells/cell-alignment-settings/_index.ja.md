---
title: Cell アライメント設定
type: docs
weight: 20
url: /ja/java/cell-alignment-settings/
---
## **Aspose.Cells - Cell アライメント設定**
Aspose.Cells は、Excel ファイルを表すクラス Workbook を提供します。 Workbook クラスには、Excel ファイル内の各ワークシートへのアクセスを許可する WorksheetCollection が含まれています。ワークシートは Worksheet クラスによって表されます。

Worksheet クラスは Cells コレクションを提供します。 Cells コレクションの各アイテムは、Cell クラスのオブジェクトを表します。

Aspose.Cells は、セルの書式設定に使用される Cell クラスの setStyle メソッドを提供します。 Style クラスは、フォント設定を構成するための便利なプロパティを提供します。

TextAlignmentType 列挙体を使用して、任意のテキスト配置タイプを選択します。

**Java**

{{< highlight "java" >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Accessing the added worksheet in the Excel file

int sheetIndex = workbook.getWorksheets().add();

Worksheet worksheet = workbook.getWorksheets().get(sheetIndex);

Cells cells = worksheet.getCells();

//Adding the current system date to "A1" cell

Cell cell = cells.get("A1");

Style style = cell.getStyle();

//Adding some value to the "A1" cell

cell.setValue("Visit Aspose!");

//Setting the horizontal alignment of the text in the "A1" cell

style.setHorizontalAlignment(TextAlignmentType.CENTER);

//Saved style

cell.setStyle(style);

{{< /highlight >}}
## **Apache POI SS - HSSF & XSSF - Cell アライメント設定**
HSSFCellStyle は、Apache POI API を使用して、セル内の配置のスタイルを提供します。

**Java**

{{< highlight "java" >}}

 public static void main(String[]args) throws IOException

{

 // The path to the documents directory.

 String dataDir = Utils.getDataDir(ApacheCellAlignment.class);

 HSSFWorkbook wb = new HSSFWorkbook();

 HSSFSheet sheet = wb.createSheet("new sheet");

 HSSFRow row = sheet.createRow(2);

 createCell(wb, row, 0, HSSFCellStyle.ALIGN_CENTER);

 createCell(wb, row, 1, HSSFCellStyle.ALIGN_CENTER_SELECTION);

 createCell(wb, row, 2, HSSFCellStyle.ALIGN_FILL);

 createCell(wb, row, 3, HSSFCellStyle.ALIGN_GENERAL);

 createCell(wb, row, 4, HSSFCellStyle.ALIGN_JUSTIFY);

 createCell(wb, row, 5, HSSFCellStyle.ALIGN_LEFT);

 createCell(wb, row, 6, HSSFCellStyle.ALIGN_RIGHT);

 // Write the output to a file

 FileOutputStream fileOut = new FileOutputStream(dataDir + "ApahceAlignment.xls");

 wb.write(fileOut);

 fileOut.close();

 System.out.println("Done.");

}

/**

\* Creates a cell and aligns it a certain way.

\*

\* @param wb        the workbook

\* @param row       the row to create the cell in

\* @param column    the column number to create the cell in

\* @param align     the alignment for the cell.

*/

private static void createCell(HSSFWorkbook wb, HSSFRow row, int column, int align) {

 HSSFCell cell = row.createCell(column);

 cell.setCellValue("Align It");

 HSSFCellStyle cellStyle = wb.createCellStyle();

 cellStyle.setAlignment((short)align);

 cell.setCellStyle(cellStyle);

}

{{< /highlight >}}
## **実行中のコードをダウンロード**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **サンプルコードをダウンロード**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/cellsrowscolumns/cellalignment)

{{% alert color="primary" %}} 

詳細については、次を参照してください。[配置設定の構成](/cells/ja/java/data-formatting/).

{{% /alert %}}
