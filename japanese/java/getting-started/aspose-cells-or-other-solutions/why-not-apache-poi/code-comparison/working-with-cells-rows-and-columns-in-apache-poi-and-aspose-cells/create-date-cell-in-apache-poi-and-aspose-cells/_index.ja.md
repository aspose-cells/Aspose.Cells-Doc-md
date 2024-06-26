---
title: Apache POI と Aspose.Cells で日付セルを作成する
type: docs
weight: 90
url: /ja/java/create-date-cell-in-apache-poi-and-aspose-cells/
---

## **Aspose.Cells - 日付セルの作成**
**Java**

{{< highlight java >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Accessing the added worksheet in the Excel file

Worksheet worksheet = workbook.getWorksheets().get(0);

Cells cells = worksheet.getCells();

//Adding the current system date to "A1" cell

Cell cell = cells.get("A1");

cell.setValue(Calendar.getInstance());

//Setting the display format of the date to number 15 to show date as "d-mmm-yy"

Style style = cell.getStyle();

style.setCustom("d-mmm-yy");

cell.setStyle(style);

{{< /highlight >}}
## **Apache POI SS (HSSF + XSSF) - 日付セルの作成**
**Java**

{{< highlight java >}}

 Workbook wb = new HSSFWorkbook();

//Workbook wb = new XSSFWorkbook();

CreationHelper createHelper = wb.getCreationHelper();

Sheet sheet = wb.createSheet("new sheet");

// Create a row and put some cells in it. Rows are 0 based.

Row row = sheet.createRow(0);

// Create a cell and put a date value in it.  The first cell is not styled

// as a date.

Cell cell = row.createCell(0);

cell.setCellValue(new Date());

// we style the second cell as a date (and time).  It is important to

// create a new cell style from the workbook otherwise you can end up

// modifying the built in style and effecting not only this cell but other cells.

CellStyle cellStyle = wb.createCellStyle();

cellStyle.setDataFormat(

    createHelper.createDataFormat().getFormat("m/d/yy h:mm"));

cell = row.createCell(1);

cell.setCellValue(new Date());

cell.setCellStyle(cellStyle);

//you can also set date as java.util.Calendar

cell = row.createCell(2);

cell.setCellValue(Calendar.getInstance());

cell.setCellStyle(cellStyle);

{{< /highlight >}}
## **ランニングコードのダウンロード**
以下に示すソーシャルコーディングサイトから**Aspose.CellsおよびApache POIで日付セルを作成**するための実行例をダウンロードしてください:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells-Java-vs-POI-SS-v1.5)
## **ソースコードをダウンロード**
以下に示すソーシャルコーディングサイトから**Aspose.CellsおよびApache POIで日付セルを作成**のソースコードをダウンロードしてください:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java)

{{% alert color="primary" %}} 

詳細については、[セルへのデータの追加](/cells/ja/java/add-data-in-cells/)を参照してください。

{{% /alert %}}
