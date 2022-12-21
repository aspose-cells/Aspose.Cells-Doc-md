---
title: 最初の Aspose.Cells アプリケーション - Hello World
type: docs
weight: 30
url: /ja/net/your-first-aspose-cells-application-hello-world/
---
{{% alert color="primary" %}}

このチュートリアルでは、Aspose.Cells' シンプル API を使用して最初のアプリケーション (Hello World) を作成する方法を示します。

{{% /alert %}}

## **Hello World アプリケーションの作成**

以下の手順では、Aspose.Cells API を使用して Hello World アプリケーションを作成します。

1. のインスタンスを作成します[ワークブック](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラス。
1. 免許をお持ちの方は、[それを適用する](/cells/ja/net/licensing/).
評価版を使用している場合は、ライセンス関連のコード行をスキップしてください。
1. 新しい Excel ファイルを作成するか、既存の Excel ファイルを開きます。
1. Excel ファイル内のワークシートの目的のセルにアクセスします。
1. 単語を挿入する**Hello World!**アクセスされたセルに。
1. 変更された Microsoft Excel ファイルを生成します。

上記の手順の実装は、以下の例で示されています。

### **コード サンプル: 新しいワークブックの作成**

次の例では、ゼロから新しいワークブックを作成し、Hello World を書き込みます。最初のワークシートのセル A1 に入力し、Excel ファイルを保存します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Introduction-FirstApplication-1.cs" >}}

### **コード サンプル: 既存のファイルを開く**

次の例では、「Sample.xlsx」という名前の既存の Microsoft Excel テンプレート ファイルを開き、「Hello World!」と入力します。最初のワークシートの A1 セルにテキストを入力し、ブックを保存します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Introduction-OpenExistingFile-1.cs" >}}
