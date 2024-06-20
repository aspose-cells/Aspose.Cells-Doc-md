---
title: 元に戻すおよびやり直しの機能を使用する
type: docs
weight: 120
url: /ja/net/aspose-cells-griddesktop/use-undo-and-redo-feature/
keywords: GridDesktop、元に戻す、やり直す
description: この記事では、GridDesktop での元に戻すおよびやり直しの機能について紹介しています。
---

{{% alert color="primary" %}} 

GridDesktop の元に戻す/やり直し機能は非常に便利です。その名前がその機能を説明しています。ワークシートで最近行われた操作を元に戻したりやり直したりすることができます。たとえば、誤って数式を削除したり、実際には行いたくないセルのデータを編集したりした場合は、このコントロールが提供する元に戻しややり直し操作を使用してそれらの操作を修正することができます。

{{% /alert %}} 
## **元に戻しとやり直しの操作の実行**
次の API がそのために利用できます。各 API についての説明が付いていますので、それぞれを確認してください。

- **GridDesktop.EnableUndo** - 属性: 元に戻し機能が有効かどうかを示します。デフォルト値は "false" です。
- **UndoManager** – クラス: 元に戻し/やり直し操作を管理するために使用されます。
- **GridDesktop.UndoManager** – 属性: **UndoManager** オブジェクトのインスタンスを取得します。
- **UndoManager.Undo** – メソッド: 元に戻し操作を実行します。
- **UndoManager.Redo -** メソッド: やり直し操作を実行します。
- **UndoManager.ClearStack** – メソッド: 元に戻し/やり直しスタックをクリアします。
- **UndoManager.UndoStepsCount** – 属性: 現在の利用可能な元に戻しステップの数を取得します。
- **UndoManager.RedoStepsCount** – 属性: 現在の利用可能なやり直しステップの数を取得します。
- **UndoManager.UndoStackSize** – 属性: 元に戻しスタックのサイズを取得 / 設定します。
### **元に戻す**
以下のサンプルコードは、GridDesktop API を使用して元に戻す操作を実装する方法を示しています。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-UndoRedoFeature-Undo.cs" >}}
### **やり直す**
以下のサンプルコードは、GridDesktop API を使用してやり直し操作を実装する方法を示しています。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-UndoRedoFeature-Redo.cs" >}}

{{% alert color="primary" %}} 

現在、元に戻し/やり直し操作はセルの値の変更を指します。

{{% /alert %}}
