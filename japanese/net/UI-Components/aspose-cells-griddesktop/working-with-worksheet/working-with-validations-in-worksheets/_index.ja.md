---
title: ワークシートでの検証と操作
type: docs
weight: 70
url: /ja/net/aspose-cells-griddesktop/work-with-validations-in-worksheets/
keywords: GridDesktop,validations,validation
description: この記事では、GridDesktopで検証を行う方法について紹介します。
---

{{% alert color="primary" %}} 

Aspose.Cells.GridDesktopは、ワークシートのセルに検証（もしくは検証ルール）を追加することもサポートしています。セルに検証ルールを適用することで、開発者は特定の形式でデータをGridに入力するようユーザーを制限することができます。Aspose.Cells.GridDesktopでは異なるモードの検証もサポートされています。このトピックでは、それらの検証モードについてだけでなく、これらの検証の操作方法についても説明します。

{{% /alert %}} 
## **検証モード**
Aspose.Cells.GridDesktopでサポートされている3つの検証モードは次のとおりです:

- 必須検証モード
- 正規表現検証モード
- カスタム検証モード
### **必須検証モード**
この検証モードでは、指定されたセルに値を入力することが制限されます。**必須検証**をワークシートセルに適用すると、そのセルに値を入力することが必須となります。
### **正規表現検証モード**
このモードでは、ワークシートセルに対して特定の形式でデータを入力するための制限が適用されます。データの形式のパターンは、**正規表現**形式で提供されます。
### **カスタム検証モード**
**カスタム検証**を使用するには、Aspose.Cells.GridDesktop.ICustomValidation インターフェースを実装する必要があります。このインターフェースは**Validate**メソッドを提供します。このメソッドはデータが有効な場合にはtrueを返し、そうでない場合にはfalseを返します。
## **Aspose.Cells.GridDesktopでの検証の操作**
### **検証の追加**
ワークシートセルに任意の検証を追加するには、以下の手順に従ってください:

- Aspose.Cells.GridDesktop コントロールを **Form** に追加します
- 任意の **Worksheet** にアクセスします
- **Worksheet**の**Validations**コレクションに任意の検証を追加して、どの検証をどのセルに適用するかを指定します



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ValidationInWorksheets-AddingValidation.cs" >}}

{{% alert color="primary" %}} 

上記の図では、検証ルールが適用されたセルに対して検証ルールが記載されています。不正な値（そのセルの検証ルールに合致しない有効な値）が入力された場合、**MessageBox**が表示されてユーザーに無効な入力を通知します。

{{% /alert %}} 
### **ICustomValidationの実装**
上記のコードスニペットでは、**A8** セルにカスタム検証を追加しましたが、まだそのカスタム検証を実装していません。このトピックの冒頭で説明したように、カスタム検証を適用するには、**ICustomValidation** インターフェイスを実装する必要があります。それでは、**ICustomValidation** インターフェイスを実装するクラスを作成してみましょう。

以下のコードスニペットでは、カスタム検証を実装して、以下のチェックを実行します:

- 検証が追加されたセルのアドレスが正確かどうかをチェックする
- セルの値のデータ型が倍精度浮動小数点数かどうかをチェックする
- セルの値が100より大きいかどうかをチェックする



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ValidationInWorksheets-ImplementingICustomInterface.cs" >}}
### **検証へのアクセス**
特定のワークシートセルに検証が追加された後、開発者が実行時に特定の検証の属性にアクセスして変更する必要がある場合があります。そのような場合、Aspose.Cells.GridDesktop は開発者がこのタスクを簡単に達成できるようにしました。

特定の検証にアクセスするには、以下の手順に従ってください:

- 希望の **Worksheet** にアクセス
- 検証が適用されたセル名を指定してワークシート内の特定の **Validation** にアクセス
- 必要に応じて **Validation** 属性を編集



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ValidationInWorksheets-AccessingValidation.cs" >}}

{{% alert color="primary" %}} 

**Validations** コレクションには2つのインデクサがあります。以下の例で使用される1つのインデクサは、セル名をそのインデックスとして受け取り、**Validation** オブジェクトにアクセスできます。もう1つのインデクサは（行番号と列番号）を2つのパラメータとして受け取り、同じタスクを実行します。

{{% /alert %}} 
### **検証の削除**
ワークシートから特定の検証を削除するには、以下の手順に従ってください:

- 希望の **Worksheet** にアクセス
- 検証が適用されたセル名を指定してワークシートから特定の **Validation** を削除



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ValidationInWorksheets-RemoveValidation.cs" >}}
