---
title: Apache POI と Aspose.Cells の分割ペイン
type: docs
weight: 70
url: /ja/java/split-panes-in-apache-poi-and-aspose-cells/
---
## **Aspose.Cells - ペインの分割**
Aspose.Cells は、Microsoft Excel ファイルを表すクラス Workbook を提供します。 Workbook クラスは、Excel ファイルを管理するためのさまざまなプロパティとメソッドを提供します。分割ビューを実装するには、Worksheet クラスの split メソッドを使用します。分割ペインを削除するには、removeSplit メソッドを使用します。

**Java**

{{< highlight "java" >}}

 //Instantiate a new workbook / Open a template file

Workbook book = new Workbook(dataDir + "workbook.xls");

//Set the active cell

book.getWorksheets().get(0).setActiveCell("A20");

//Split the worksheet window

book.getWorksheets().get(0).split();

{{< /highlight >}}
## **Apache POI SS - HSSF & XSSF - 分割ペイン**
分割ペイン機能は、Apache POI SS (HSSF & XSSF) API の使用中に createSplitPane メソッドによって実現できます。

**Java**

{{< highlight "java" >}}

 Workbook wb = new XSSFWorkbook();

Sheet sheet = wb.createSheet("new sheet");

// Create a split with the lower left side being the active quadrant

sheet.createSplitPane(2000, 2000, 0, 0, Sheet.PANE_LOWER_LEFT);

{{< /highlight >}}
## **実行中のコードをダウンロード**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **サンプルコードをダウンロード**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/cellsrowscolumns/splitpanes)

{{% alert color="primary" %}} 

詳細については、次を参照してください。[ペインの分割](http://docs.aspose.com:8082/docs/display/cellsjava/Split+Panes).

{{% /alert %}}
