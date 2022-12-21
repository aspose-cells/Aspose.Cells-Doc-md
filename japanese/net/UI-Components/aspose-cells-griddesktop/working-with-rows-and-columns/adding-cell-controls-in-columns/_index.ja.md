---
title: 列に Cell コントロールを追加する
type: docs
weight: 90
url: /ja/net/adding-cell-controls-in-columns/
---
{{% alert color="primary" %}} 

後の説明では、ワークシートでのセル コントロールの追加と管理について説明しました。しかし、これらのアプローチを使用すると、セル コントロールを単一のセルに 1 つずつ追加できます。 1 つまたは複数の列のすべてのセルにセル コントロールを追加したい場合はどうすればよいでしょうか。そのような場合、開発者の労力を軽減するために、Aspose.Cells.GridDesktop は列ごとにセル コントロールを追加する機能を提供します。これは、開発者が目的の列のみを選択し、任意のセル コントロールを指定できることを意味します。指定したセル コントロールが、指定した列のすべてのセルに追加されます。この機能をどのように使用できるか見てみましょう。

{{% /alert %}} 
## **序章**
現在、Aspose.Cells.GridDesktop は、以下を含む 3 種類のセル コントロールの追加をサポートしています。

- **ボタン**
- **チェックボックス**
- **コンボボックス**

これらのコントロールはすべて、抽象クラスから派生しています。**セルコントロール**.

**重要：**列全体ではなく単一のセルにセル コントロールを追加する場合は、次を参照できます。[ワークシートに Cell コントロールを追加します。](/cells/ja/net/adding-cell-controls-in-worksheets/)
### **ボタンの追加**
Aspose.Cells.GridDesktop を使用して列にボタンを追加するには、次の手順に従ってください。

-  Aspose.Cells.GridDesktop コントロールを**形**
- 任意のアクセス**ワークシート**
- 追加**ボタン**指定された任意の**桁**の**ワークシート**

**ノート：**追加しながら**ボタン**、ボタンの幅、高さ、キャプションを指定できます。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-AddingCellControlsInColumns-AddingButton.cs" >}}


上記のコード スニペットは、指定された列のすべてのセルにボタンを追加します。その特定の列のセルが選択されるたびに、ボタンが表示されます。ボタンのイベント処理の詳細については、[ボタン コントロールのイベント処理。](/cells/ja/net/adding-cell-controls-in-worksheets/#event-handling-of-button)
### **チェックボックスの追加**
Aspose.Cells.GridDesktop を使用して列にチェックボックスを追加するには、次の手順に従ってください。

-  Aspose.Cells.GridDesktop コントロールを**形**
- 任意のアクセス**ワークシート**
- 追加**チェックボックス**指定された任意の**桁**の**ワークシート**

**ノート：**追加しながら**チェックボックス**、チェックボックスの状態を指定することもできます。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-AddingCellControlsInColumns-AddingCheckbox.cs" >}}


上記のコード スニペットは、指定された列のすべてのセルにチェックボックスを追加します。チェックボックスのイベント処理の詳細については、[CheckBox コントロールのイベント処理。](/cells/ja/net/adding-cell-controls-in-worksheets/#event-handling-of-checkbox)
### **コンボボックスの追加**
Aspose.Cells.GridDesktop を使用して列にコンボボックスを追加するには、次の手順に従ってください。

-  Aspose.Cells.GridDesktop コントロールを**形**
- 任意のアクセス**ワークシート**
- 追加される項目 (または値) の配列を作成します**コンボボックス**
- 追加**コンボボックス**(項目または値を含む) から指定された任意の**桁**の**ワークシート**



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-AddingCellControlsInColumns-AddingCombobox.cs" >}}


上記のコード スニペットは、指定された列のすべてのセルにコンボ ボックスを追加します。その特定の列のセルが選択されるたびに、コンボボックスが表示されます。コンボボックスのイベント処理の詳細については、[ComboBox コントロールのイベント処理。](/cells/ja/net/adding-cell-controls-in-worksheets/#event-handling-of-combobox)
