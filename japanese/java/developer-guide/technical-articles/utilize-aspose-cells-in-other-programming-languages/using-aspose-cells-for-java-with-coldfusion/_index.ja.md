---
title: ColdFusion で Aspose.Cells for Java を使用する
type: docs
weight: 40
url: /ja/java/using-aspose-cells-for-java-with-coldfusion/
---
{{% alert color="primary" %}}

この記事では、ColdFusion 開発者が ColdFusion アプリケーションで Aspose.Cells for Java を使用するために必要な基本情報とコード セグメントを提供します。

この記事では、ColdFusion を使用して単純な Web ページを作成し、Aspose.Cells for Java を使用して単純な Excel ファイルを生成する方法を示します。

{{% /alert %}}

## **Aspose.Cells: 本当の製品**

Aspose.Cells を使用すると、開発者はデータのエクスポート、あらゆる詳細およびあらゆるレベルでのスプレッドシートの書式設定、画像のインポート、グラフのインポート、グラフの作成、グラフの操作、Microsoft Excel データのストリーミング、XLS、CSV、SpreadsheetML、TabDelimited、TXT、XML などのさまざまな形式での保存を行うことができます([Aspose.Pdf](https://products.aspose.com/pdf/java/)統合) など。

製品情報、機能、およびプログラマー ガイドの詳細については、Aspose.Cells のドキュメントとオンラインの特集記事を参照してください。[デモ](https://github.com/aspose-cells/Aspose.Cells-for-Java).あなたはできる[ダウンロード](https://downloads.aspose.com/cells/java)無料で評価します。

### **前提条件**

ColdFusion アプリケーションで Aspose.Cells for Java を使用するには、Aspose.Cells.jar ファイルを {InstallationFolder\\}\wwwroot\WEB-INF\lib フォルダーにコピーします。

lib フォルダーに新しい JAR を配置した後、ColdFusion アプリケーション サーバーを再起動することを忘れないでください。

### **Aspose.Cells for Java と ColdFusion を使用して Excel ファイルを作成する**

以下では、空の Microsoft Excel ファイルを生成し、いくつかのコンテンツを挿入して XLS ファイルとして保存する簡単なアプリケーションを作成します。

以下は実際のコードです (ColdFusion & Aspose.Cells for Java)。コードを実行すると、Excel ファイル output.xls が生成されます。

**生成された output.xls**

![todo:画像_代替_文章](using-aspose-cells-for-java-with-coldfusion_1.png)

**Java**

{{< highlight "java" >}}

 <html>

<head><title>Hello World!</title></head>

<body>

    <b>This example shows how to create a simple MS Excel Workbook using Aspose.Cells</b>

    <cfset workbook=CreateObject("java", "com.aspose.cells.Workbook").init()>

    <cfset worksheets = workbook.getWorksheets()>

    <cfset sheet= worksheets.get("Sheet1")>

    <cfset cells= sheet.getCells()>

    <cfset cell= cells.getCell(0,0)>

    <cfset cell.setValue("Hello World!")>

    <cfset workbook.save("C:\output.xls")>

</body>

</html>

{{< /highlight >}}

## **概要**

{{% alert color="primary" %}}

この記事では、ColdFusion で Aspose.Cells for Java を使用する方法について説明します。

Aspose.Cells は優れた柔軟性を提供し、優れた速度、効率、および信頼性を提供します。 Aspose.Cells は、何年にもわたる研究、設計、慎重な調整の恩恵を受けてきました。

質問、コメント、提案を歓迎します。[Aspose.Cells フォーラム](https://forum.aspose.com/c/cells/9).

{{% /alert %}}
