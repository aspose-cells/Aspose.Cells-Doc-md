---
title: xlsx4j のワークシートからデータをエクスポートする
type: docs
weight: 20
url: /ja/java/export-data-from-worksheets-in-xlsx4j/
---
## **Aspose.Cells - ワークシートからのデータのエクスポート**
Aspose.Cells では、ユーザーは外部データ ソースからワークシートにデータをインポートできるだけでなく、ワークシート データを配列にエクスポートすることもできます。

**Java**

{{< highlight "java" >}}

//開く Excel ファイルを含むファイル ストリームを作成する

FileInputStream fstream = new FileInputStream(dataDir + "workbook.xls");

// Workbook オブジェクトのインスタンス化

ワークブック ワークブック = 新しいワークブック(fstream);

//Excel ファイルの最初のワークシートにアクセスする

ワークシート ワークシート = workbook.getWorksheets().get(0);

//1セル目から7行2列の内容をArrayにエクスポート。

オブジェクト dataTable [][]= worksheet.getCells().exportArray(4,0,7,8);

 for (int i = 0 ; i< dataTable.length ; i++)

{

	System.out.println("["+ i +"]: "+ Arrays.toString(dataTable[i]));

}

{{< /highlight >}}
## **実行中のコードをダウンロード**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **サンプルコードをダウンロード**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/datahandling/exportdatafromworksheets/AsposeExportDataFromWorksheets.java)

{{% alert color="primary" %}} 

詳細については、次を参照してください。[ワークシートからのデータのエクスポート](/java/exporting-data-from-worksheets).

{{% /alert %}}
