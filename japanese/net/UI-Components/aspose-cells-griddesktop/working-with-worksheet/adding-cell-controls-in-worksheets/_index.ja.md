---
title: ワークシートに Cell コントロールを追加する
type: docs
weight: 120
url: /ja/net/adding-cell-controls-in-worksheets/
---
{{% alert color="primary" %}} 

Cell コントロールは、実際にはワークシートに追加できるコントロールです。私たちはそれらを呼びます**Cell コントロール**これらのコントロールはセルに表示されるためです。このトピックでは、これらのセル コントロールのイベントの追加と処理について説明します。

{{% /alert %}} 
## **序章**
現在、Aspose.Cells.GridDesktop は、以下を含む 3 種類のセル コントロールの追加をサポートしています。

- **ボタン**
- **チェックボックス**
- **コンボボックス**

これらのコントロールはすべて、抽象クラスから派生しています。**セルコントロール**.各ワークシートには、**コントロール**.これを使用して、新しいセル コントロールを追加したり、既存のセル コントロールにアクセスしたりできます。**コントロール**コレクションを簡単に。

**重要：**1 つずつ追加するのではなく、列のすべてのセルにセル コントロールを追加する場合は、次を参照できます。[Cell 列のコントロールの管理。](/cells/ja/net/adding-cell-controls-in-worksheets/)
### **ボタンの追加**
Aspose.Cells.GridDesktop を使用してワークシートにボタンを追加するには、次の手順に従ってください。

- Aspose.Cells.GridDesktop コントロールを**形**
- 任意のアクセス**ワークシート**
- 追加**ボタン**に**コントロール**のコレクション**ワークシート**



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddingCellControls-AddingButton.cs" >}}


追加しながら**ボタン**、セルの位置 (表示する場所)、幅と高さ、およびボタンのキャプションを指定できます。
#### **ボタンのイベント処理**
追加について話し合いました**ボタン**への制御**ワークシート**しかし、ボタンを使用できない場合、ワークシートにボタンを配置することの利点は何ですか。そこで、ボタンのイベント処理が必要になります。

を処理するには**クリック**のイベント**ボタン**コントロール、Aspose.Cells.GridDesktop が提供する**セルボタンクリック**必要に応じて開発者が実装する必要があるイベント。たとえば、以下に示すように、ボタンがクリックされたときにメッセージを表示しました。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddingCellControls-HandlingButton.cs" >}}
#### **ボタン コントロールの背景イメージの指定**
以下のコードに示すように、ラベル/テキストを使用してボタン コントロールの背景画像/画像を設定できます。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddingCellControls-SetBackground.cs" >}}


**重要：**セル コントロールのすべてのイベントには、**CellControlEventArgs**セル コントロール (イベントがトリガーされる) を含むセルの行番号と列番号を提供する引数。
### **チェックボックスの追加**
Aspose.Cells.GridDesktop を使用してワークシートにチェックボックスを追加するには、次の手順に従ってください。

- Aspose.Cells.GridDesktop コントロールを**形**
- 任意のアクセス**ワークシート**
- 追加**チェックボックス**に**コントロール**のコレクション**ワークシート**



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddingCellControls-AddingCheckbox.cs" >}}


追加しながら**チェックボックス**、セルの位置 (表示する場所) とチェックボックスの状態を指定できます。
#### **CheckBox のイベント処理**
Aspose.Cells.GridDesktop が提供する**CellCheckedChanged**のときにトリガーされるイベント**チェック済み**チェックボックスの状態が変わります。開発者は、要件に従ってこのイベントを処理できます。たとえば、メッセージを表示して、**チェック済み**以下のコードのチェックボックスの状態:



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddingCellControls-HandlingCheckbox.cs" >}}
### **コンボボックスの追加**
Aspose.Cells.GridDesktop を使用してコンボボックスをワークシートに追加するには、次の手順に従ってください。

- Aspose.Cells.GridDesktop コントロールを**形**
- 任意のアクセス**ワークシート**
- 追加される項目 (または値) の配列を作成します**コンボボックス**
- 追加**コンボボックス**に**コントロール**のコレクション**ワークシート**セルの位置 (コンボボックスが表示される場所) と、コンボボックスがクリックされたときに表示されるアイテム/値を指定することによって



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddingCellControls-AddingCombobox.cs" >}}
#### **ComboBox のイベント処理**
Aspose.Cells.GridDesktop が提供する**CellSelectedIndexChanged**のときにトリガーされるイベント**選択されたインデックス**コンボボックスの変更。開発者は、希望に応じてこのイベントを処理できます。たとえば、メッセージを表示して、**選択したアイテム**コンボボックスの:



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddingCellControls-HandlingCombobox.cs" >}}
