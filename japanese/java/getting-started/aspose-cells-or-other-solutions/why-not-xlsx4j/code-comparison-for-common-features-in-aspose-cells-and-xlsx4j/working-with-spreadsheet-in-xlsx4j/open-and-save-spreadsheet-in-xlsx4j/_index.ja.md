---
title: スプレッドシートを xlsx4j で開いて保存する
type: docs
weight: 40
url: /ja/java/open-and-save-spreadsheet-in-xlsx4j/
---
## **Aspose.Cells - スプレッドシートを開いて保存する**
開発者は Aspose.Cells を使用して、さまざまな目的でファイルを開きます。たとえば、ファイルを開いてそこからデータを取得したり、定義済みのデザイナー スプレッドシート ファイルを使用して開発プロセスをスピードアップしたりできます。 Aspose.Cells を使用すると、開発者はさまざまな種類のソース ファイルを開くことができます。これらのソース ファイルは、Microsoft Excel レポート、SpreadsheetML、CSV、またはタブ区切りファイルです。

**Aspose.Cells**では、柔軟な API を使用して、開発者がゼロから Excel ファイルを作成できます。Excel ファイルを作成したら、ワークブック (ファイル) も保存する必要があります。 Aspose.Cells は、これらのファイルを保存するさまざまな方法を提供します。

**Java**

{{< highlight "java" >}}

 //Creating an Workbook object with an Excel file path

Workbook workbook = new Workbook(dataDir + "pivot.xlsm");

//Saving the Excel file

workbook.save(dataDir + "pivot-rtt-Aspose.xlsm");

{{< /highlight >}}
## **xlsx4j - スプレッドシートを開いて保存する**
以下の例は、xlsx4j を使用しているときにスプレッドシートを開いて保存する方法を示しています。

**Java**

{{< highlight "java" >}}

 String inputfilepath  = dataDir + "pivot.xlsm";

boolean save = true;

String outputfilepath = dataDir + "pivot-rtt-xlsx4j.xlsm";

// Open a document from the file system

// 1. Load the Package

OpcPackage pkg = OpcPackage.load(new java.io.File(inputfilepath));

// Save it

if (save) {

    SaveToZipFile saver = new SaveToZipFile(pkg);

    saver.save(outputfilepath);

}

{{< /highlight >}}
## **実行中のコードをダウンロード**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **サンプルコードをダウンロード**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/featurescomparison/workbook/opensavespreadsheet)
