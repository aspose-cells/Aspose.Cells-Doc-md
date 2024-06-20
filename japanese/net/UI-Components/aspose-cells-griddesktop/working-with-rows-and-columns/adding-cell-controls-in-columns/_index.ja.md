---
title: 列にセルコントロールを追加
type: docs
weight: 90
url: /ja/net/aspose-cells-griddesktop/add-cell-controls-in-columns/
keywords: GridDesktop,add,control,controls
description: この記事では、GridDesktopに列にコントロールを追加する方法について紹介します。
---

{{% alert color="primary" %}} 

後の議論では、ワークシートにセルコントロールを追加および管理する方法について説明しました。ただし、これらのアプローチを使用すると、1つずつ単一のセルにセルコントロールを追加できます。1つまたは複数の列のすべてのセルにセルコントロールを追加したい場合はどうすればよいでしょうか？ このような場合、開発者の手間を減らすために、Aspose.Cells.GridDesktopでは列ごとにセルコントロールを追加する機能が提供されます。これは、開発者が必要な列を選択し、任意のセルコントロールを指定するだけで、指定されたセルコントロールが指定された列のすべてのセルに追加されます。この機能の使用方法を見てみましょう。

{{% /alert %}} 
## **紹介**
現在、Aspose.Cells.GridDesktopは次の3つのタイプのセルコントロールをサポートしています。

- **ボタン**
- **チェックボックス**
- **ComboBox**

これらのコントロールはすべて、**CellControl**という抽象クラスから派生しています。

**重要:** セルの列全体ではなく単一のセルにセルコントロールを追加するには、[ワークシートへのセルコントロールの追加](/cells/ja/net/adding-cell-controls-in-worksheets/)を参照してください。
### **ボタンの追加**
Aspose.Cells.GridDesktopを使用して列にボタンを追加するには、以下の手順に従ってください:

- Aspose.Cells.GridDesktop コントロールを **Form** に追加します
- 任意の **Worksheet** にアクセスします
- **ワークシート**の任意の指定した**列**に**ボタン**を追加します

**注意:** **ボタン**を追加する際に、ボタンの幅、高さ、キャプションを指定することができます。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-AddingCellControlsInColumns-AddingButton.cs" >}}


上記のコードスニペットは、指定した列のすべてのセルにボタンを追加します。指定した列の任意のセルが選択されると、ボタンが表示されます。ボタンのイベント処理の詳細については、[ボタンコントロールのイベント処理](/cells/ja/net/adding-cell-controls-in-worksheets/#event-handling-of-button)を参照してください。
### **チェックボックスの追加**
Aspose.Cells.GridDesktopを使用して列にチェックボックスを追加するには、以下の手順に従ってください:

- Aspose.Cells.GridDesktop コントロールを **Form** に追加します
- 任意の **Worksheet** にアクセスします
- **ワークシート**の任意の指定した**列**に**チェックボックス**を追加します

**注意:** **チェックボックス**を追加する際に、チェックボックスの状態を指定することもできます。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-AddingCellControlsInColumns-AddingCheckbox.cs" >}}


上記のコードスニペットは、指定した列のすべてのセルにチェックボックスを追加します。チェックボックスのイベント処理の詳細については、[チェックボックスコントロールのイベント処理](/cells/ja/net/adding-cell-controls-in-worksheets/#event-handling-of-checkbox)を参照してください。
### **コンボボックスの追加**
Aspose.Cells.GridDesktopを使用して列にコンボボックスを追加するには、以下の手順に従ってください:

- Aspose.Cells.GridDesktop コントロールを **Form** に追加します
- 任意の **Worksheet** にアクセスします
- **コンボボックス**に追加する項目（または値）の配列を作成します
- **ワークシート**の任意の指定した**列**に、項目（または値）を含む**コンボボックス**を追加します



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-AddingCellControlsInColumns-AddingCombobox.cs" >}}


上記のコードスニペットは、指定した列のすべてのセルにコンボボックスを追加します。指定した列の任意のセルが選択されると、コンボボックスが表示されます。コンボボックスのイベント処理の詳細については、[コンボボックスコントロールのイベント処理](/cells/ja/net/adding-cell-controls-in-worksheets/#event-handling-of-combobox)を参照してください。
