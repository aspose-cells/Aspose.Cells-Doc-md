---
title: セルの非表示および表示
type: docs
weight: 30
url: /ja/java/hide-and-unhide-cells/
---

## **Aspose.Cells - 行および列の非表示および表示**
Aspose.CellsにはMicrosoft Excelファイルを表す[Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)クラスが提供されています。WorkbookクラスにはExcelファイル内の各ワークシートにアクセスできるWorksheetCollectionが含まれています。ワークシートは[Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)クラスによって表されます。Worksheetクラスにはワークシート内のすべてのセルを表すCellsコレクションが提供されます。Cellsコレクションには、ワークシート内の行または列を管理するためのいくつかのメソッドが用意されています。 

**Java**

{{< highlight java >}}

 Workbook workbook = new Workbook("workbook.xls");

//Accessing the first worksheet in the Excel file

Worksheet worksheet = workbook.getWorksheets().get(0);

Cells cells = worksheet.getCells();

cells.hideRow(2); //Hiding the 3rd row of the worksheet

cells.hideColumn(1); //Hiding the 2nd column of the worksheet

{{< /highlight >}}
## **Apache POI SS - HSSF XSSF - セルの非表示および表示**
行または列を非表示にするには、Apache POI SSにはRow.setZeroHeight(boolean)メソッドが提供されています。

**Java**

{{< highlight java >}}

 InputStream inStream = new FileInputStream("workbook.xls");

Workbook workbook = WorkbookFactory.create(inStream);

Sheet sheet = workbook.createSheet();

Row row = sheet.createRow(0);

row.setZeroHeight(true);

{{< /highlight >}}
## **ランニングコードのダウンロード**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **サンプルコードをダウンロード**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/cellsrowscolumns/hideunhidecells)

{{% alert color="primary" %}} 

詳細については、[行および列の非表示と表示](/java/hiding-and-showing-rows-and-columns)を参照してください。

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
