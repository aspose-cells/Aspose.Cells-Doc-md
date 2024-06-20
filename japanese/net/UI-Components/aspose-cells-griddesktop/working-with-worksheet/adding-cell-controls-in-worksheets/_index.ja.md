---
title: ワークシートにセルコントロールを追加する
type: docs
weight: 120
url: /ja/net/aspose-cells-griddesktop/add-cell-controls-in-worksheets/
keywords: GridDesktop,add,control,button,checkbox,combobox
description: この記事では、GridDesktopのワークシートにコントロールを追加する方法について紹介します。
---

{{% alert color="primary" %}} 

セルコントロールは実際にはワークシートに追加できるコントロールです。これらのコントロールを**セルコントロール**と呼びます。このトピックでは、これらのセルコントロールの追加およびイベントの処理について説明します。

{{% /alert %}} 
## **紹介**
現在、Aspose.Cells.GridDesktopは次の3つのタイプのセルコントロールをサポートしています。

- **ボタン**
- **チェックボックス**
- **ComboBox**

これらのコントロールはすべて、抽象クラス**CellControl**から派生しています。 各ワークシートには**Controls**のコレクションが含まれています。 新しいセルコントロールを追加し、既存のものに簡単にアクセスするためには、この**Controls**コレクションを使用できます。

**重要:** 1つずつ追加する代わりに、列のすべてのセルにセルコントロールを追加したい場合は、[列の中のセルコントロールの管理](/cells/ja/net/aspose-cells-griddesktop/adding-cell-controls-in-worksheets/)を参照してください。
### **ボタンの追加**
Aspose.Cells.GridDesktopを使用してワークシートにボタンを追加するには、以下の手順に従ってください：

- あなたの**フォーム**にAspose.Cells.GridDesktopコントロールを追加
- 好きな**ワークシート**にアクセス
- **ワークシート**の**Controls**コレクションに**ボタン**を追加



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddingCellControls-AddingButton.cs" >}}


**ボタン**を追加する際には、セルの場所（表示する位置）、幅と高さ、およびボタンのキャプションを指定できます。
#### **ボタンのイベント処理**
私たちは**ワークシート**に**ボタン**コントロールを追加したところで、ボタンがクリックされても使用しない場合の利点は何でしょうか。 ですから、ここでボタンのイベント処理の必要性が出てきます。

**ボタン**コントロールの**Click**イベントを処理するには、Aspose.Cells.GridDesktopは**CellButtonClick**イベントを提供しており、開発者はそれを自分の必要に応じて実装する必要があります。 たとえば、以下にボタンがクリックされたときにメッセージを表示しただけの例があります：



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddingCellControls-HandlingButton.cs" >}}
#### **ボタンコントロールの背景画像の指定**
ボタンコントロールのラベル/テキストとともに背景画像/写真を設定することができます。 以下のコードに示すように。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddingCellControls-SetBackground.cs" >}}


**重要:** セルコントロールのすべてのイベントには、そのイベントがトリガーされたセルコントロールを含むセルの行番号と列番号を提供する**CellControlEventArgs**引数が含まれています。
### **チェックボックスの追加**
Aspose.Cells.GridDesktopを使用してワークシートにチェックボックスを追加する場合は、以下の手順に従ってください。

- あなたの**フォーム**にAspose.Cells.GridDesktopコントロールを追加
- 好きな**ワークシート**にアクセス
- **ワークシート**の**Controls**コレクションに**チェックボックス**を追加



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddingCellControls-AddingCheckbox.cs" >}}


**チェックボックス**を追加する際には、セルの場所（表示する位置）とチェックボックスの状態を指定できます。
#### **チェックボックスのイベント処理**
Aspose.Cells.GridDesktopは、**チェックボックス**の**Checked**状態が変更されたときにトリガーされる**CellCheckedChanged**イベントを提供しています。 開発者は必要に応じてこのイベントを処理できます。 たとえば、以下にチェックボックスの**Checked**状態を表示するためのメッセージを表示しただけの例があります：



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddingCellControls-HandlingCheckbox.cs" >}}
### **コンボボックスの追加**
Aspose.Cells.GridDesktopを使用してワークシートにコンボボックスを追加するには、以下の手順に従ってください。

- あなたの**フォーム**にAspose.Cells.GridDesktopコントロールを追加
- 好きな**ワークシート**にアクセス
- **ComboBox**がクリックされたときに表示されるアイテム（または値）の配列を作成
- セルの場所（コンボボックスが表示される場所）と、コンボボックスがクリックされたときに表示されるアイテム/値を指定して**ワークシート**の**Controls**コレクションに**ComboBox**を追加



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddingCellControls-AddingCombobox.cs" >}}
#### **コンボボックスのイベント処理**
Aspose.Cells.GridDesktopは、**CellSelectedIndexChanged** イベントを提供しています。このイベントは、コンボボックスの**選択されたインデックス**が変更されたときにトリガーされます。開発者はこのイベントを自分の望むように処理できます。たとえば、コンボボックスの**選択されたアイテム**を表示するためのメッセージを表示するだけであるとします。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddingCellControls-HandlingCombobox.cs" >}}
