---
title: ワークシートでの検証の操作
type: docs
weight: 70
url: /ja/net/working-with-validations-in-worksheets/
---
{{% alert color="primary" %}} 

Aspose.Cells.GridDesktop は、ワークシートのセルへの検証 (または検証ルール) の追加もサポートしています。検証ルールをセルに適用することにより、開発者はユーザーが特定の形式でグリッドにデータを入力することを制限できます。 Aspose.Cells.GridDesktop では、さまざまな検証モードがサポートされています。このトピックでは、これらの検証モードについて説明するだけでなく、これらの検証の操作についても説明します。

{{% /alert %}} 
## **検証モード**
Aspose.Cells.GridDesktop では、次の 3 つの検証モードがサポートされています。

- 検証モードが必要です
- 正規表現検証モード
- カスタム検証モード
### **検証モードが必要です**
この検証モードでは、ユーザーは指定されたセルに値を入力することが制限されます。一度**検証が必要です**がワークシート セルに適用されると、ユーザーはそのセルに値を入力する必要があります。
### **正規表現検証モード**
このモードでは、ユーザーが特定の形式でデータをセルに送信できるように、ワークシートのセルに制限が適用されます。データ形式のパターンは、**正規表現**.
### **カスタム検証モード**
使用するには**カスタム検証**、開発者は Aspose.Cells.GridDesktop.ICustomValidation インターフェイスを実装する必要があります。インターフェイスは、**検証**方法。データが有効な場合、このメソッドは true を返し、それ以外の場合は false を返します。
## **Aspose.Cells.GridDesktop での検証の操作**
### **検証の追加**
ワークシート セルに任意の種類の検証を追加するには、次の手順に従ってください。

-  Aspose.Cells.GridDesktop コントロールを**形**
- 任意のアクセス**ワークシート**
- 必要な検証を**検証**のコレクション**ワークシート**どの検証をどのセルに適用するかを指定します。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ValidationInWorksheets-AddingValidation.cs" >}}

{{% alert color="primary" %}} 

上の図では、これらの検証ルールが適用されるセルの前に検証ルールについても言及しています。無効な値 (そのセルに定義された検証規則に従って無効な値) が入力された場合、**メッセージボックス**無効なエントリについてユーザーに通知するように見えます。

{{% /alert %}} 
### **ICustomValidation の実装**
上記のコード スニペットでは、カスタム検証を追加しています。**A8**cell ですが、そのカスタム検証はまだ実装していません。このトピックの冒頭で説明したように、カスタム検証を適用するには、実装する必要があります**ICustomValidation**インターフェース。それでは、実装するクラスを作成してみましょう**ICustomValidation**インターフェース。

以下のコード スニペットでは、次のチェックを実行するカスタム検証を実装しています。

- 検証が追加されたセルのアドレスが正確かどうかを確認します
- セルの値のデータ型が double かどうかを確認します
- セルの値が 100 より大きいかどうかを確認します



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ValidationInWorksheets-ImplementingICustomInterface.cs" >}}
### **検証へのアクセス**
検証が特定のワークシート セルに追加されると、開発者は実行時に特定の検証の属性にアクセスして変更する必要がある場合があります。したがって、Aspose.Cells.GridDesktop により、開発者はこのタスクを簡単に実行できるようになりました。

特定の検証にアクセスするには、次の手順に従ってください。

- 希望のアクセス**ワークシート**
- 特定の**検証**検証が適用されたセル名を指定して、ワークシートで
- 編集**検証**必要に応じて属性



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ValidationInWorksheets-AccessingValidation.cs" >}}

{{% alert color="primary" %}} 

**検証**コレクションには 2 つのインデクサーがあります。 1 つのインデクサー (以下の例で使用) は、**検証**別のインデクサーは 2 つのパラメーター (行番号と列番号) を使用して同じタスクを実行します。

{{% /alert %}} 
### **検証の削除**
ワークシートから特定の検証を削除するには、次の手順に従ってください。

- 希望のアクセス**ワークシート**
- 特定の**検証**から**ワークシート**検証が適用されたセル名を指定することによって



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ValidationInWorksheets-RemoveValidation.cs" >}}
