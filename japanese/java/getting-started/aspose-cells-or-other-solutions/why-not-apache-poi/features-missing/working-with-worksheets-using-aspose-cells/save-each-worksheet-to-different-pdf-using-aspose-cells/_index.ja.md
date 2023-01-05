---
title: Aspose.Cells を使用して、各ワークシートを別の PDF に保存します
type: docs
weight: 80
url: /ja/java/save-each-worksheet-to-different-pdf-using-aspose-cells/
---
## **Aspose.Cells - 各ワークシートを別の PDF に保存**
Aspose.Cells は、XLS ファイル (画像、チャートなどを含む) を PDF ドキュメントに変換することをサポートします。 Aspose.Cells for Java は独立してスプレッドシートを Pdf ドキュメントに変換することができ、変換に Aspose.Pdf for Java を使用する必要がなくなりました。プロセス全体をメモリ内で実行できるため、変換では一時ファイルを作成/使用する必要はありません。

**Java**

{{< highlight "java" >}}

 //Excelファイルのパスを取得

文字列 filePath = dataDir + "workbook.xlsx";

//新しいワークブックをインスタンス化し、Excel を開く

//その場所からのファイル

ワークブック ワークブック = 新しいワークブック(ファイルパス);

//ブック内のワークシートの数を取得します

int sheetCount = workbook.getWorksheets().getCount();

//最初のワークシートを除くすべてのシートを非表示にします

for (int i = 1; i< workbook.getWorksheets().getCount(); i++)

{

     workbook.getWorksheets().get(i).setVisible(false);

}

//Take Pdfs of each sheet

for (int j = 0; j < workbook.getWorksheets().getCount(); j++)

{

    Worksheet ws = workbook.getWorksheets().get(j);

    workbook.save(dataPath + ws.getName() + ".pdf");

    if (j < workbook.getWorksheets().getCount() - 1)

    {

       workbook.getWorksheets().get(j + 1).setVisible(true);

       workbook.getWorksheets().get(j).setVisible(false);

    }

}

{{< /highlight >}}
## **実行中のコードをダウンロード**
## **サンプルコードをダウンロード**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/worksheets/SaveEachWorksheetToDifferentPDF.java)

{{% alert color="primary" %}} 

詳細については、次を参照してください。[各ワークシートを別の PDF ファイルに保存する](/cells/ja/java/save-each-worksheet-to-a-different-pdf-file).

{{% /alert %}}
