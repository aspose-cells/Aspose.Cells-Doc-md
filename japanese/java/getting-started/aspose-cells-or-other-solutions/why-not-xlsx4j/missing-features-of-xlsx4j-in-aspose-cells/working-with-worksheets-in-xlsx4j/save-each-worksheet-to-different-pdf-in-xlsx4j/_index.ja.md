---
title: xlsx4jでのワークシートごとに異なるPDFへの保存
type: docs
weight: 50
url: /ja/java/save-each-worksheet-to-different-pdf-in-xlsx4j/
---

## **Aspose.Cells - 各ワークシートを異なる PDF に保存**
Aspose.Cellsでは、画像、チャートなどが含まれるXLSファイルをPDFドキュメントに変換する機能がサポートされています。Aspose.Cells for JavaでスプレッドシートをPDFドキュメントに変換することができ、この変換にはAspose.Pdf for Javaを使用する必要はありません。変換には一時ファイルの作成/使用も必要ありません。全プロセスはメモリ内で行うことができます。

**Java**

{{< highlight java >}}

 //Get the Excel file path

String filePath = dataDir + "workbook.xlsx";

//Instantiate a new workbook and open the Excel

//File from its location

Workbook workbook = new Workbook(filePath);

//Get the count of the worksheets in the workbook

int sheetCount = workbook.getWorksheets().getCount();

//Make all sheets invisible except first worksheet

for (int i = 1; i < workbook.getWorksheets().getCount(); i++)

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
## **ランニングコードのダウンロード**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **サンプルコードをダウンロード**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/worksheets/saveeachworksheettopdf/AsposeSaveEachWorksheetToDifferentPDF.java)

{{% alert color="primary" %}} 

詳細については、[各ワークシートを別々のPDFファイルに保存](/cells/ja/java/save-each-worksheet-to-a-different-pdf-file)をご覧ください。

{{% /alert %}}
