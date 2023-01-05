---
title: 元に戻す機能とやり直し機能の使用
type: docs
weight: 120
url: /ja/net/using-undo-and-redo-feature/
---
{{% alert color="primary" %}} 

GridDesktop の Undo/Redo 機能は非常に便利です。名前はその機能自体を説明しており、ワークシートで最近のアクションを元に戻したりやり直したりできます。たとえば、数式が誤って削除された場合や、実際には不要なセルのデータを編集した場合、これらのアクションは、コントロールによって提供される元に戻す操作とやり直し操作を使用して修正できます。

{{% /alert %}} 
## **元に戻す操作とやり直し操作を実行する**
このタスクでは、次の API を使用できます。 APIごとに記載しておりますので、そちらをご確認ください。

- **GridDesktop.EnableUndo** - 属性: 元に戻す機能が有効かどうかを示します。デフォルト値は「false」です。
- **元に戻すマネージャー**– クラス: 元に戻す/やり直し操作を管理するために使用されます。
- **GridDesktop.UndoManager** – 属性: のインスタンスを取得します**元に戻すマネージャー**物体。
- **UndoManager.元に戻す**– メソッド: 元に戻す操作を実行します。
- **UndoManager.Redo -**メソッド: やり直し操作を実行します。
- **UndoManager.ClearStack** – メソッド: 元に戻す/やり直しスタックをクリアします。
- **UndoManager.UndoStepsCount** – 属性: 現在使用可能な元に戻すステップの数を取得します。
- **UndoManager.RedoStepsCount** – 属性: 現在使用可能なやり直しステップの数を取得します。
- **UndoManager.UndoStackSize** – 属性: アンドゥ スタック サイズを取得/設定します。
### **元に戻す**
次のサンプル コードは、GridDesktop API を使用して元に戻す操作を実装する方法を示しています。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-UndoRedoFeature-Undo.cs" >}}
### **やり直し**
次のサンプル コードは、GridDesktop API を使用してやり直し操作を実装する方法を示しています。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-UndoRedoFeature-Redo.cs" >}}

{{% alert color="primary" %}} 

現在、元に戻す/やり直し操作は、セル値の変更を指します。

{{% /alert %}}
