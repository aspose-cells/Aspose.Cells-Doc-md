---
title: Apache POIおよびAspose.Cellsでパネをフリーズする
type: docs
weight: 80
url: /ja/java/freeze-panes-in-apache-poi-and-aspose-cells/
---

## **Aspose.Cells - ペインを固定する**
Aspose.CellsにはMicrosoft Excelファイルを表す[Workbook](http://docs.aspose.com:8082/docs/display/cellsjava/Workbook)クラスが提供されています。Workbookクラスには各ワークシートにアクセスできるWorksheetCollectionが含まれています。

ワークシートは[Worksheet](http://docs.aspose.com:8082/docs/display/cellsjava/Worksheet)クラスによって表されます。Worksheetクラスにはワークシートの管理に幅広いプロパティとメソッドが用意されています。フリーズペインを設定するには、WorksheetクラスのfreezePanesメソッドを呼び出します。freezePanesメソッドには以下のパラメータが必要です:

- **行**、枠が開始するセルの行インデックス。
- **列**、枠が開始するセルの列インデックス。
- **固定行**、上部枠内に表示される行数。
- **固定列**、左部枠内に表示される列数。

**Java**

{{< highlight java >}}

 worksheet1.freezePanes(0,2,0,2); // Freezing Columns

worksheet2.freezePanes(2,0,2,0); // Freezing Rows

{{< /highlight >}}
## **Apache POI SS - HSSF XSSF - フリーズペイン**
Apache POI SS - HSSFおよびXSSFを使用してフリーズペイン機能を実現するためには、sheet.createFreezePaneが利用可能です

**Java**

{{< highlight java >}}

 // Freeze just one row

sheet1.createFreezePane( 0, 2, 0, 2 );

// Freeze just one column

sheet2.createFreezePane( 2, 0, 2, 0 );

// Freeze the columns and rows (forget about scrolling position of the lower right quadrant).

sheet3.createFreezePane( 2, 2 );

{{< /highlight >}}
## **ランニングコードのダウンロード**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **サンプルコードをダウンロード**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/cellsrowscolumns/freezepanes)

{{% alert color="primary" %}} 

詳細については、[フリーズペイン](http://docs.aspose.com:8082/docs/display/cellsjava/Freeze+Panes)を参照してください。

{{% /alert %}}
