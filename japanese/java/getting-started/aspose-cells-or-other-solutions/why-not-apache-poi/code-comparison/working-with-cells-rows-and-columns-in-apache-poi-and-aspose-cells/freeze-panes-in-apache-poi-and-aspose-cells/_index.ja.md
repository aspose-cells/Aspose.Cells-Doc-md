---
title: Apache POI および Aspose.Cells でペインをフリーズする
type: docs
weight: 80
url: /ja/java/freeze-panes-in-apache-poi-and-aspose-cells/
---
## **Aspose.Cells - フリーズペイン**
Aspose.Cells はクラスを提供し、[ワークブック](http://docs.aspose.com:8082/docs/display/cellsjava/Workbook)Microsoft Excel ファイルを表します。 Workbook クラスには、Excel ファイル内の各ワークシートへのアクセスを可能にする WorksheetCollection が含まれています。

ワークシートは、[ワークシート](http://docs.aspose.com:8082/docs/display/cellsjava/Worksheet)クラス。 Worksheet クラスは、ワークシートを管理するための幅広いプロパティとメソッドを提供します。フリーズ ペインを構成するには、Worksheet クラスの freezePanes メソッドを呼び出します。 FreezePanes メソッドは、次のパラメーターを取ります。

- **行**、フリーズが開始されるセルの行インデックス。
- **桁**、フリーズが開始されるセルの列インデックス。
- **凍結された行**、上部ペインに表示される行の数。
- **冷凍列**、左ペインに表示される列の数

**Java**

{{< highlight "java" >}}

 worksheet1.freezePanes(0,2,0,2); // Freezing Columns

worksheet2.freezePanes(2,0,2,0); // Freezing Rows

{{< /highlight >}}
## **Apache POI SS - HSSF XSSF - フリーズ ペイン**
sheet.createFreezePane は、Apache POI SS - HSSF および XSSF の使用中に FreezePane 機能を実現するために使用できます。

**Java**

{{< highlight "java" >}}

 // Freeze just one row

sheet1.createFreezePane( 0, 2, 0, 2 );

// Freeze just one column

sheet2.createFreezePane( 2, 0, 2, 0 );

// Freeze the columns and rows (forget about scrolling position of the lower right quadrant).

sheet3.createFreezePane( 2, 2 );

{{< /highlight >}}
## **実行中のコードをダウンロード**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **サンプルコードをダウンロード**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/cellsrowscolumns/freezepanes)

{{% alert color="primary" %}} 

詳細については、次を参照してください。[フリーズペイン](http://docs.aspose.com:8082/docs/display/cellsjava/Freeze+Panes).

{{% /alert %}}
