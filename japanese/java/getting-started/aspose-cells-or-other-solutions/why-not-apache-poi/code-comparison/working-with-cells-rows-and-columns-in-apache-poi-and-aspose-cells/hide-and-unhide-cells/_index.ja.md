---
title: 非表示と再表示 Cells
type: docs
weight: 30
url: /ja/java/hide-and-unhide-cells/
---
## **Aspose.Cells - 行と列の非表示と再表示**
Aspose.Cells はクラスを提供し、[ワークブック](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)、Microsoft Excel ファイルを表します。 Workbook クラスには、Excel ファイル内の各ワークシートへのアクセスを許可する WorksheetCollection が含まれています。ワークシートは、[ワークシート](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)クラス。 Worksheet クラスは、ワークシート内のすべてのセルを表す Cells コレクションを提供します。 Cells コレクションは、ワークシートの行または列を管理するためのいくつかのメソッドを提供します。

**Java**

{{< highlight "java" >}}

 Workbook workbook = new Workbook("workbook.xls");

//Accessing the first worksheet in the Excel file

Worksheet worksheet = workbook.getWorksheets().get(0);

Cells cells = worksheet.getCells();

cells.hideRow(2); //Hiding the 3rd row of the worksheet

cells.hideColumn(1); //Hiding the 2nd column of the worksheet

{{< /highlight >}}
## **Apache POI SS - HSSF XSSF - 表示/非表示 Cells**
行または列を非表示にするために、Apache POI SS は Row.setZeroHeight(boolean) メソッドを提供します。

**Java**

{{< highlight "java" >}}

 InputStream inStream = new FileInputStream("workbook.xls");

Workbook workbook = WorkbookFactory.create(inStream);

Sheet sheet = workbook.createSheet();

Row row = sheet.createRow(0);

row.setZeroHeight(true);

{{< /highlight >}}
## **実行中のコードをダウンロード**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **サンプルコードをダウンロード**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/cellsrowscolumns/hideunhidecells)

{{% alert color="primary" %}} 

詳細については、次を参照してください。[行と列の表示と非表示](/java/hiding-and-showing-rows-and-columns).

{{% /alert %}}
