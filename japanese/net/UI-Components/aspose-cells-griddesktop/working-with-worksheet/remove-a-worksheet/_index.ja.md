---
title: ワークシートを削除する
type: docs
weight: 30
url: /ja/net/remove-a-worksheet/
---
{{% alert color="primary" %}} 

このトピックでは、Aspose.Cells.GridDesktop コントロールを使用したワークシートの削除について説明します。この基本的なタスクを実行するには、いくつかの簡単な方法があります。

{{% /alert %}} 
## **ワークシートの削除**
Aspose.Cells.GridDesktop コントロールを使用してワークシートを削除するには、次の手順に従ってください。

1. Aspose.Cells.GridDesktop コントロールをフォームに追加します。
1. GridDesktop コントロールで Worksheets コレクションの Remove メソッドを呼び出します。
### **ワークシート インデックスの使用**
この方法では、削除するワークシートのワークシート インデックス (グリッドのワークシート コレクション内) を渡すだけです。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-RemoveWorksheet-RemoveUsingIndex.cs" >}}
### **ワークシート名の使用**
ワークシートの名前がわかっている場合は、その名前を指定して特定のワークシートを削除できます。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-RemoveWorksheet-RemoveUsingName.cs" >}}

{{% alert color="primary" %}} 

削除はメソッドです。ワークシート コレクション内のインデックスを使用してワークシートを削除するか、RemoveAt メソッドを使用してインデックス/名前を使用してワークシートを削除します。

{{% /alert %}}
