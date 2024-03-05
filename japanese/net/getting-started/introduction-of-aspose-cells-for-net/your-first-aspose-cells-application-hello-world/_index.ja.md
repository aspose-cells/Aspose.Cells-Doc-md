---
title: 初めての Aspose.Cells アプリケーション - Hello World
type: docs
weight: 30
url: /ja/net/your-first-aspose-cells-application-hello-world/
description: Aspose.Cells for .NET を使用して、サポートされている形式で最初の Excel ファイルを作成、編集、保存し、C# のシンプルさと強力さを体験してください。
keywords: C# Hello World, Aspose.Cells for .NET Hello World, The first application using Aspose.Cells for .NET, The first program via Aspose.Cells for .NET.
---
{{% alert color="primary" %}}

このチュートリアルでは、Aspose.Cells' simple API を使用して最初のアプリケーション (Hello World) を作成する方法を示します。この単純なアプリケーションは、指定されたワークシート セルにテキスト 'Hello World' を含む Microsoft Excel ファイルを作成します。

{{% /alert %}}

##  **Hello World アプリケーションの作成方法**

以下の手順では、Aspose.Cells API を使用して Hello World アプリケーションを作成します。

1. のインスタンスを作成します。[ワークブック](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラス。
1. 免許をお持ちであれば、[それを適用してください](/cells/ja/net/licensing/).
評価版を使用している場合は、ライセンス関連のコード行をスキップしてください。
1. 新しい Excel ファイルを作成するか、既存の Excel ファイルを開きます。
1. Excel ファイル内のワークシートの任意のセルにアクセスします。
1. 言葉を挿入する**Hello World!**アクセスされたセルに。
1. 変更した Microsoft Excel ファイルを生成します。

上記のステップの実装を以下の例で示します。

###  **新しいワークブックを作成する方法**

次の例では、新しいワークブックを最初から作成し、Hello World! と書き込みます。を最初のワークシートのセル A1 に入力し、Excel ファイルを保存します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Introduction-FirstApplication-1.cs" >}}

###  **既存のファイルを開く方法**

次の例では、「Sample.xlsx」という名前の既存の Microsoft Excel テンプレート ファイルを開き、「Hello World!」と入力します。最初のワークシートの A1 セルにテキストを入力し、ワークブックを保存します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Introduction-OpenExistingFile-1.cs" >}}
