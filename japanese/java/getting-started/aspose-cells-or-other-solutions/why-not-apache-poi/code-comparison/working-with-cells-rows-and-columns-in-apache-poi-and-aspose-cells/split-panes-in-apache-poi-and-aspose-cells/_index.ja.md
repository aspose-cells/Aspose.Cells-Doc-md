---
title: Apache POIおよびAspose.Cellsで分割されたペインを作成する
type: docs
weight: 70
url: /ja/java/split-panes-in-apache-poi-and-aspose-cells/
---

## **Aspose.Cells - 分割ウィンドウ**
Aspose.Cellsは、Microsoft Excelファイルを表すWorkbookクラスを提供します。Workbookクラスは、Excelファイルを管理するための幅広いプロパティとメソッドを提供します。分割ビューを実装するには、Worksheetクラスのsplitメソッドを使用します。スプリットペインを削除するには、removeSplitメソッドを使用します。

**Java**

{{< highlight java >}}

 //Instantiate a new workbook / Open a template file

Workbook book = new Workbook(dataDir + "workbook.xls");

//Set the active cell

book.getWorksheets().get(0).setActiveCell("A20");

//Split the worksheet window

book.getWorksheets().get(0).split();

{{< /highlight >}}
## **Apache POI SS - HSSF＆XSSF - 分割されたペイン**
Apache POI SS（HSSF＆XSSF）APIを使用する際にcreateSplitPaneメソッドを使用してスプリットペインの機能を実現できます。

**Java**

{{< highlight java >}}

 Workbook wb = new XSSFWorkbook();

Sheet sheet = wb.createSheet("new sheet");

// Create a split with the lower left side being the active quadrant

sheet.createSplitPane(2000, 2000, 0, 0, Sheet.PANE_LOWER_LEFT);

{{< /highlight >}}
## **ランニングコードのダウンロード**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **サンプルコードをダウンロード**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/cellsrowscolumns/splitpanes)

{{% alert color="primary" %}} 

詳細については、[Split Panes](http://docs.aspose.com:8082/docs/display/cellsjava/Split+Panes)を参照してください。

{{% /alert %}}
