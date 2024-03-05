---
title: 最初の Aspose.Cells アプリケーション - Hello World
type: docs
weight: 30
url: /ja/python-java/your-first-aspose-cells-application-hello-world/
---
{{% alert color="primary" %}}

この初心者向けトピックでは、開発者が Aspose.Cells' simple API を使用して単純な最初のアプリケーション (Hello World) を作成する方法を示します。アプリケーションは、ワークシートの指定されたセルに Hello World という単語を含む Microsoft Excel ファイルを作成します。

{{% /alert %}}

### **Hello World アプリケーションの作成**

Aspose.Cells API を使用して Hello World アプリケーションを作成するには:

1. のインスタンスを作成します**[ワークブック](https://reference.aspose.com/cells/python-java/asposecells.api/ワークブック)**クラス。
1. ライセンスを適用します。
1. ライセンスを購入した場合は、アプリケーションでライセンスを使用して Aspose.Cells の全機能にアクセスします
1. コンポーネントの評価版を使用している場合 (ライセンスなしで Aspose.Cells を使用している場合)、この手順をスキップします。
1. 新しい Microsoft Excel ファイルを作成するか、テキストを追加/更新する既存のファイルを開きます。
1. Microsoft Excel ファイルのワークシートの任意のセルにアクセスします。
1. 単語を挿入する**Hello World!**アクセスされたセルに。
1. 変更された Microsoft Excel ファイルを生成します。

以下の例は、上記の手順を示しています。

#### **ワークブックの作成**

次の例では、新しいワークブックをゼロから作成し、"Hello World!" という単語を書き込みます。最初のワークシートのセル A1 に入力し、ファイルを保存します。

**生成されたスプレッドシート** 

![todo:画像_代替_文章](your-first-aspose-cells-application-hello-world_1.png)

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "CreatingHelloWorldFile.py" >}}

#### **既存のファイルを開く**

次の例では、既存の Microsoft Excel テンプレート ファイルを開きます。**book1.xls**、「Hello World！」という言葉を書きます。最初のワークシートのセル A1 で、ブックを新しいファイルとして保存します。

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "OpeningExistingFile.py" >}}
