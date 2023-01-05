---
title: ワークブック内でシートをコピー
type: docs
weight: 40
url: /ja/java/copy-sheet-within-workbook/
---
## **Microsoft Excel - ワークブック内のシートの移動またはコピー**
以下は、ワークブック内またはワークブック間でワークシートをコピーおよび移動するための手順です。

1. ブック内またはブック間でシートを移動またはコピーするには、シートを受け取るブックを開きます。
1. 移動またはコピーするシートを含むブックに切り替えてから、シートを選択します。
1. 上で**編集**メニュー、クリック**シートの移動またはコピー**.
1. [To book] ボックスで、ワークブックをクリックしてシートを受け取ります。
1. 選択したシートを新しいワークブックに移動またはコピーするには、**新しい本**.
1. の中に**シート前**ボックスで、移動またはコピーしたシートを挿入する前のシートをクリックします。
1. シートを移動する代わりにコピーするには、**コピーを作成する**チェックボックス。
## **Aspose.Cells - ワークブック内のシートのコピー**
{{% alert color="primary" %}} 

Aspose.Cells は、オーバーロードされたメソッド WorksheetCollection.addCopy() を提供します。これは、ワークシートをコレクションに追加し、既存のワークシートからデータをコピーするために使用されます。メソッドの 1 つのバージョンは、ソース ワークシートのインデックスをパラメーターとして受け取ります。もう一方のバージョンは、ソース ワークシートの名前を取ります。

次の例は、ブック内の既存のワークシートをコピーする方法を示しています。

{{% /alert %}} 

Aspose.Cells を使用してシートをコピーする

**Java**

{{< highlight "java" >}}

 //Create a new Workbook by excel file path

Workbook wb = new Workbook(dataDir + "workbook.xls");

//Create a Worksheets object with reference to the sheets of the Workbook.

WorksheetCollection sheets = wb.getWorksheets();

//Copy data to a new sheet from an existing sheet within the Workbook.

sheets.addCopy("Sheet1");

{{< /highlight >}}
## **Apache POI SS - ワークブック内のシートのコピー**
{{% alert color="primary" %}} 

Workbook.cloneSheet() は、ワークブックでシートをコピーするために使用されます。

{{% /alert %}} 

Apache POI SS を使用してシートをコピーする

**Java**

{{< highlight "java" >}}

 Workbook wb = new HSSFWorkbook();

wb.createSheet("new sheet");

wb.createSheet("second sheet");

Sheet cloneSheet = wb.cloneSheet(0);

{{< /highlight >}}
## **実行中のコードをダウンロード**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **サンプルコードをダウンロード**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/worksheets/copysheetwithinworkbook)

{{% alert color="primary" %}} 

詳細については、次を参照してください。[ワークシートのコピーと移動](/cells/ja/java/copying-and-moving-worksheets).

{{% /alert %}}
