---
title: Aspose.Cells を使用して各ワークシートを異なる PDF に保存
type: docs
weight: 80
url: /ja/java/save-each-worksheet-to-different-pdf-using-aspose-cells/
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
## **サンプルコードをダウンロード**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/worksheets/SaveEachWorksheetToDifferentPDF.java)

{{% alert color="primary" %}} 

詳細については、[各ワークシートを別々のPDFファイルに保存](/cells/ja/java/save-each-worksheet-to-a-different-pdf-file)をご覧ください。

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
