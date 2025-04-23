---
title: ワークブック内でシートをコピー
type: docs
weight: 40
url: /ja/java/copy-sheet-within-workbook/
---

## **Microsoft Excel - ワークブック内でシートを移動またはコピー**
ブック内またはブック間でのワークシートのコピーおよび移動の手順は次のとおりです。

1. ワークブック内またはワークブック間でシートを移動またはコピーするには、シートを受け取るワークブックを開きます。
1. 移動またはコピーしたいシートを含むワークブックに切り替え、そのシートを選択します。
1. **編集**メニューで**シートの移動またはコピー**をクリックします。
1. 別のブックのボックスで、シートを受け取るブックをクリックしてください。
1. 選択したシートを新しいブックに移動またはコピーするには、**新しいブック**をクリックしてください。
1. **前のシート**ボックスで、移動またはコピーされたシートが挿入される前のシートをクリックします。
1. 移動ではなくシートをコピーする場合、**コピーを作成** チェックボックスを選択します。
## **Aspose.Cells - ワークブック内のシートをコピー**
{{% alert color="primary" %}} 

Aspose.Cells には、既存のワークシートからデータをコピーし、ワークシートをコレクションに追加するオーバーロードされたメソッド、 WorksheetCollection.addCopy() が提供されています。このメソッドのバージョンの1つは、ソースワークシートのインデックスをパラメータとして取ります。もう一つのバージョンは、ソースワークシートの名前を取ります。

次の例は、ブック内で既存のワークシートをコピーする方法を示しています。

{{% /alert %}} 

Aspose.Cells を使用してシートをコピーする

**Java**

{{< highlight java >}}

 //Create a new Workbook by excel file path

Workbook wb = new Workbook(dataDir + "workbook.xls");

//Create a Worksheets object with reference to the sheets of the Workbook.

WorksheetCollection sheets = wb.getWorksheets();

//Copy data to a new sheet from an existing sheet within the Workbook.

sheets.addCopy("Sheet1");

{{< /highlight >}}
## **Apache POI SS - ワークブック内のシートをコピー**
{{% alert color="primary" %}} 

Workbook.cloneSheet() は、ワークブック内のシートをコピーするために使用されます。

{{% /alert %}} 

Apache POI SS を使用してシートをコピーする

**Java**

{{< highlight java >}}

 Workbook wb = new HSSFWorkbook();

wb.createSheet("new sheet");

wb.createSheet("second sheet");

Sheet cloneSheet = wb.cloneSheet(0);

{{< /highlight >}}
## **ランニングコードのダウンロード**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **サンプルコードをダウンロード**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/worksheets/copysheetwithinworkbook)

{{% alert color="primary" %}} 

詳細については、[ワークシートのコピーと移動](/cells/ja/java/copying-and-moving-worksheets)をご覧ください。

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
