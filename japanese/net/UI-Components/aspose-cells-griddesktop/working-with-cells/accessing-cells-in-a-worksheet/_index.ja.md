---
title: ワークシートで Cells にアクセスする
type: docs
weight: 10
url: /ja/net/accessing-cells-in-a-worksheet/
---
{{% alert color="primary" %}} 

これまでワークシート、行、列の操作について説明してきましたが、今度はさらに深くセルについて説明します。したがって、このトピックでは、セルにアクセスする基本的な機能からセルについての議論を開始します。

{{% /alert %}} 
## **ワークシートで Cells にアクセスする**
Aspose.Cells.GridDesktop の API を使用して、ワークシートの任意のセルにアクセスできます。セルにアクセスするには、次の 3 つの方法が考えられます。

- **Cell名を使用**
- **Cell の行と列のインデックスを使用する**
- **集中する Cell**

上記の 3 つのアプローチを 1 つずつ説明しましょう。
### **Cell名を使用**
ワークシート内のすべてのセルには、一意の名前があります。たとえば、A1、A2、B1、B2 などです。Aspose.Cells.GridDesktop を使用すると、開発者はセル名を使用して目的のセルにアクセスできます。セル名を (インデックスとして) に渡すだけです。**Cells**のコレクション**ワークシート**.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-AccessingCells-AccessByName.cs" >}}
### **Cell の行インデックスと列インデックスの使用**
ワークシート内のセルは、行インデックスと列インデックスの位置を使用して認識することもできます。セルの行インデックスと列インデックスを**Cells**のコレクション**ワークシート**.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-AccessingCells-AccessByIndices.cs" >}}
### **集中する Cell**
アクセスするセルが正確にわからない場合。次に、Aspose.Cells.GridDesktop を使用すると、現在ユーザーがフォーカスしているセルにアクセスすることもできます。この機能を使用すると、ユーザーが任意のセルを選択できるようになり、バックエンドでそのセルにアクセスできるようになります。を使用することで簡単に実現できます。**GetFocusedCell**の方法**ワークシート**.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-AccessingCells-AccessFocusedCell.cs" >}}
