---
title: Aspose.Cellsアプリケーションの最初の例  Hello World
type: docs
weight: 30
url: /ja/python-net/your-first-aspose-cells-application-hello-world/
---

{{% alert color="primary" %}}

この初心者向けのトピックでは、開発者がAspose.Cellsの単純なAPIを使用して最初のアプリケーション（Hello World）を作成する方法を示しています。このアプリケーションは、ワークシートの特定のセルにHello Worldという言葉が記載されたMicrosoft Excelファイルを作成します。

{{% /alert %}}

### **Hello Worldアプリケーションの作成**

Aspose.Cells APIを使用してHello Worldアプリケーションを作成するには：

1. Workbook クラスのインスタンスを作成します。
1. ライセンスを適用します：
   1. ライセンスを購入している場合は、ライセンスを使用してアプリケーションにAspose.Cellsの完全機能にアクセスします。
   1. コンポーネントの評価版を使用している場合（ライセンスなしでAspose.Cellsを使用している場合）は、このステップをスキップします。
1. 新しいMicrosoft Excelファイルを作成するか、追加/更新したい既存のファイルを開きます。
1. Microsoft Excelファイルのワークシートの任意のセルにアクセスします。
1. アクセスしたセルに**Hello World!**の単語を挿入します。
1. 変更されたMicrosoft Excelファイルを生成します。

以下の例は上記の手順を示しています。

#### **ワークブックの作成**

以下の例では、新しいワークブックをゼロから作成し、最初のワークシートのセルA1に"Hello World!"という単語を書き込み、ファイルを保存します。

**生成されたスプレッドシート** 

![todo:image_alt_text](your-first-aspose-cells-application-hello-world_1.png)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "CreatingHelloWorldFile.py" >}}

#### **既存のファイルを開く**

以下の例では、"book1.xls"という既存のMicrosoft Excelテンプレートファイルを開き、最初のワークシートのセルA1に"Hello World!"という単語を書き込んで、ワークブックを新しいファイルとして保存します。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "OpeningExistingFile.py" >}}
{{< app/cells/assistant language="python-net" >}}
