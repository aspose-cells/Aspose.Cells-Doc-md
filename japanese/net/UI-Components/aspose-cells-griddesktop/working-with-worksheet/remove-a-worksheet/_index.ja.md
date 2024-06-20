---
title: ワークシートの削除
type: docs
weight: 30
url: /ja/net/aspose-cells-griddesktop/remove-a-worksheet/
keywords: GridDesktop, ワークシートの削除
description: この記事では、GridDesktopでワークシートを削除する方法について紹介します。
---

{{% alert color="primary" %}} 

このトピックでは、Aspose.Cells.GridDesktopコントロールを使用したワークシートの削除について説明します。この基本的なタスクを達成するためのいくつかのシンプルなアプローチがあります。

{{% /alert %}} 
## **ワークシートの削除**
Aspose.Cells.GridDesktopコントロールを使用してワークシートを削除するには、以下の手順に従ってください：

1. Aspose.Cells.GridDesktopコントロールをフォームに追加します。
1. GridDesktopコントロールのワークシートコレクションのRemoveメソッドを呼び出します。
### **ワークシートのインデックスを使用する**
この方法では、グリッドのワークシートコレクション内のワークシートのインデックスを単に渡します。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-RemoveWorksheet-RemoveUsingIndex.cs" >}}
### **ワークシートの名前を使用する**
ワークシートの名前がわかっている場合、その名前を指定して特定のワークシートを削除することができます。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-RemoveWorksheet-RemoveUsingName.cs" >}}

{{% alert color="primary" %}} 

削除はメソッドです。ワークシートのインデックス（ワークシートコレクション内）を使用してワークシートを削除するにはこれを使用するか、インデックス/名前を使用してワークシートを削除するには RemoveAt メソッドを使用します。

{{% /alert %}}
