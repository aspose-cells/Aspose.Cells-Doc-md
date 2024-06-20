---
title: Aspose.Cellsアプリケーションの最初の例  Hello World
type: docs
weight: 30
url: /ja/net/your-first-aspose-cells-application-hello-world/
description: サポートされている形式で最初のExcelファイルを作成、編集、保存することで、Aspose.Cells for .NETのシンプリシティとパワーを体験するためのC#を使用してください。
keywords: C＃のHello World、Aspose.Cells for .NETのHello World、Aspose.Cells for .NETを使用した最初のアプリケーション、Aspose.Cells for .NETを通じた最初のプログラム。
---

{{% alert color="primary" %}}

このチュートリアルでは、Aspose.CellsのシンプルなAPIを使用して、非常に基本的なアプリケーション（Hello World）を作成する方法を示しています。このシンプルなアプリケーションでは、指定されたワークシートのセルに 'Hello World' というテキストが含まれるMicrosoft Excelファイルが作成されます。

{{% /alert %}}

## **Hello Worldアプリケーションの作成方法**

以下の手順により、Aspose.Cells APIを使用してHello Worldアプリケーションを作成できます:

1. [Workbook](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラスのインスタンスを作成します。
1. ライセンスがある場合は、[適用します](/cells/ja/net/licensing/)。
   評価版を使用している場合は、ライセンスに関連するコード行をスキップします。
1.新しいExcelファイルを作成するか、既存のExcelファイルを開きます。
1. Excelファイルのワークシートの任意のセルにアクセスします。
1. アクセスしたセルに**Hello World!**の単語を挿入します。
1. 変更されたMicrosoft Excelファイルを生成します。

上記の手順の実装は、以下の例で示されています。

### **新しいワークブックの作成方法**

次の例は、ゼロから新しいワークブックを作成し、最初のワークシートのセルA1にHello World！を書き込み、Excelファイルを保存します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Introduction-FirstApplication-1.cs" >}}

### **既存のファイルを開く方法**

次の例は、存在するMicrosoft Excelテンプレートファイル「Sample.xlsx」を開き、最初のワークシートのA1セルに「Hello World！」というテキストを入力し、ワークブックを保存します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Introduction-OpenExistingFile-1.cs" >}}
