---
title: コントロールの管理
type: docs
weight: 150
url: /ja/net/managing-controls/
---
## **序章**

開発者は、テキスト ボックス、チェック ボックス、ラジオ ボタン、コンボ ボックス、ラベル、ボタン、線、長方形、弧、楕円、スピナー、スクロール バー、グループ ボックスなど、さまざまな描画オブジェクトを追加できます。すべての描画オブジェクト。ただし、まだサポートされていない描画オブジェクトまたは図形がいくつかあります。 Microsoft Excel を使用してデザイナー スプレッドシートでこれらの描画オブジェクトを作成し、デザイナー スプレッドシートを Aspose.Cells にインポートします。

## **テキスト ボックス コントロールをワークシートに追加する**

レポートで重要な情報を強調する 1 つの方法は、テキスト ボックスを使用することです。たとえば、テキストを追加して、会社名を強調したり、売上高が最も多い地域を示したりします。Aspose.Cells は、[**TextBoxCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/textboxcollection)コレクションに新しいテキスト ボックスを追加するために使用されるクラス。別のクラスがあり、[**テキストボックス**](https://reference.aspose.com/cells/net/aspose.cells.drawing/textbox)、すべてのタイプの設定を定義するために使用されるテキスト ボックスを表します。いくつかの重要なメンバーがあります。

- の[**テキストフレーム**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/textframe)プロパティは[**MsoTextFrame**](https://reference.aspose.com/cells/net/aspose.cells.drawing/msotextframe)テキスト ボックスの内容を調整するために使用されるオブジェクト。
- の[**配置**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/placement)プロパティは配置タイプを指定します。
- の[**フォント**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/font)プロパティは、フォント属性を指定します。
- の[**ハイパーリンクを追加**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/methods/addhyperlink)メソッドは、テキスト ボックスのハイパーリンクを追加します。
- の[**FillFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/fillformat)プロパティは[**MsoFillFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/msofillformat)テキスト ボックスの塗りつぶし形式を設定するために使用されるオブジェクト。
- の[**LineFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lineformat)プロパティは[**MsoLineFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/msolineformat)通常、テキスト ボックスの行のスタイルと太さに使用されるオブジェクト。
- の[**文章**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/text)プロパティは、テキスト ボックスの入力テキストを指定します。

次の例では、ブックの最初のワークシートに 2 つのテキスト ボックスを作成します。最初のテキスト ボックスには、さまざまな書式設定が用意されています。 2 つ目は単純なものです。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingTextBoxControl-1.cs" >}}

## **Designer スプレッドシートでのテキスト ボックス コントロールの操作**

Aspose.Cells では、デザイナー ワークシートのテキスト ボックスにアクセスして操作することもできます。使用[**Worksheet.TextBoxes**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/textboxes)シート内の textboxes コレクションを取得するプロパティ。

次の例では、上記の例で作成した Microsoft Excel ファイルを使用しています。 2 つのテキスト ボックスのテキスト文字列を取得し、2 番目のテキスト ボックスのテキストを変更してファイルを保存します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-ManipulatingTextBoxControls-1.cs" >}}

## **ワークシートへのチェック ボックス コントロールの追加**

チェック ボックスは、ユーザーが true または false などの 2 つのオプションから選択できるようにする場合に便利です。はい、もしくは、いいえ。 Aspose.Cells では、ワークシートでチェック ボックスを使用できます。たとえば、特定の買収を説明できるかどうかを説明できる財務予測ワークシートを作成したとします。この場合、ワークシートの上部にチェック ボックスを配置することができます。次に、このチェック ボックスのステータスを別のセルにリンクして、チェック ボックスがオンの場合にセルの値が True になるようにします。選択されていない場合、セルの値は False です。

### **Microsoft エクセルを使う**

ワークシートにチェック ボックス コントロールを配置するには、次の手順を実行します。

1. フォーム ツールバーが表示されていることを確認します。
1. クリック**チェックボックス**フォーム ツールバーのツール。
1. ワークシート領域で、クリック アンド ドラッグして、チェック ボックスとチェック ボックスの横のラベルを保持する四角形を定義します。
1. チェック ボックスを配置したら、マウス カーソルをラベル領域に移動し、ラベルを変更します。
1. の中に**Cell リンク**フィールドで、このチェック ボックスをリンクするセルのアドレスを指定します。
1. クリック**わかった**.

### **Aspose.Cells を使用**

Aspose.Cells は[**CheckBoxコレクション**](https://reference.aspose.com/cells/net/aspose.cells.drawing/checkboxcollection)このクラスは、コレクションに新しいチェック ボックスを追加するために使用されます。別のクラスがあり、[**Aspose.Cells.Drawing.CheckBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/checkbox)、チェック ボックスを表します。いくつかの重要なメンバーがあります。

- の[**リンクされたセル**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/linkedcell)プロパティは、チェック ボックスにリンクされているセルを指定します。
- の[**文章**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/text)プロパティは、チェック ボックスに関連付けられたテキスト文字列を指定します。チェックボックスのラベルです。
- の[**価値**](https://reference.aspose.com/cells/net/aspose.cells.drawing/checkbox/properties/value)プロパティは、チェック ボックスをオンにするかどうかを指定します。

次の例は、ワークシートにチェックボックスを追加する方法を示しています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingCheckBoxControl-1.cs" >}}

## **ワークシートへのラジオ ボタン コントロールの追加**

ラジオ ボタンまたはオプション ボタンは、丸いボックスで構成されるコントロールです。ユーザーは、丸いボックスを選択して決定を下します。ラジオ ボタンには通常、常にではありませんが、他のボタンが付随しています。このようなラジオ ボタンは、グループとして表示され、動作します。ユーザーは、そのうちの 1 つだけを選択することによって、どのボタンが有効であるかを決定します。ユーザーが 1 つのボタンをクリックすると、それが満たされます。グループ内の 1 つのボタンを選択すると、同じグループのボタンは空になります。

### **Microsoft エクセルを使う**

ワークシートにラジオ ボタン コントロールを配置するには、次の手順に従います。

1. を確認してください**フォーム**ツールバーが表示されます。
1. クリック**オプションボタン**道具。
1. ワークシートで、クリック アンド ドラッグして、オプション ボタンとオプション ボタンの横のラベルを保持する四角形を定義します。
1. ラジオ ボタンがワークシートに配置されたら、マウス カーソルをラベル領域に移動し、ラベルを変更します。
1. の中に**Cell リンク**フィールドで、このラジオ ボタンをリンクするセルのアドレスを指定します。
1. クリック**わかった**.

### **Aspose.Cells を使用**

[**Aspose.Cells.Drawing.ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection)クラスは、という名前のメソッドを提供します[**追加ラジオボタン**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addradiobutton)、ワークシートにラジオ ボタン コントロールを追加するために使用されます。メソッドは[**Aspose.Cells.Drawing.RadioButton**](https://reference.aspose.com/cells/net/aspose.cells.drawing/radiobutton)物体。クラス[**Aspose.Cells.Drawing.RadioButton**](https://reference.aspose.com/cells/net/aspose.cells.drawing/radiobutton)オプションボタンを表します。いくつかの重要なメンバーがあります。

- の[**リンクされたセル**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/linkedcell)プロパティは、ラジオ ボタンにリンクされているセルを指定します。
- の[**文章**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/text)プロパティは、ラジオ ボタンに関連付けられたテキスト文字列を指定します。ラジオボタンのラベルです。
- の[**チェック済み**](https://reference.aspose.com/cells/net/aspose.cells.drawing/radiobutton/properties/ischecked)プロパティは、ラジオ ボタンをオンにするかどうかを指定します。
- の[**FillFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/fillformat)プロパティは、ラジオ ボタンの塗りつぶし形式を指定します。
- の[**LineFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lineformat)プロパティは、オプション ボタンの線の書式スタイルを指定します。

次の例は、ラジオ ボタンをワークシートに追加する方法を示しています。この例では、年齢層を表す 3 つのラジオ ボタンを追加します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingRadioButtonControl-1.cs" >}}

## **コンボ ボックス コントロールをワークシートに追加する**

データ入力を容易にするため、または定義した特定の項目にエントリを制限するために、コンボ ボックス、またはワークシートの他の場所のセルからコンパイルされた有効なエントリのドロップダウン リストを作成できます。セルのドロップダウン リストを作成すると、そのセルの横に矢印が表示されます。そのセルに情報を入力するには、矢印をクリックし、目的のエントリをクリックします。

### **Microsoft エクセルを使う**

ワークシートにコンボ ボックス コントロールを配置するには、次の手順を実行します。

1. を確認してください**フォーム**ツールバーが表示されます。
1. クリックしてください**コンボボックス**道具。
1. ワークシート領域で、クリック アンド ドラッグして、コンボ ボックスを保持する四角形を定義します。
1. コンボ ボックスがワークシートに配置されたら、コントロールを右クリックしてクリックします。**フォーマット制御**入力範囲を指定します。
1. の中に**Cell リンク**フィールドで、このコンボ ボックスをリンクするセルのアドレスを指定します。
1. クリック**わかった**.

### **Aspose.Cells を使用**

の[**Aspose.Cells.Drawing.ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection)クラスは、という名前のメソッドを提供します[**AddComboBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addcombobox) 、コンボ ボックス コントロールをワークシートに追加するために使用されます。メソッドは[**Aspose.Cells.Drawing.ComboBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/combobox)物体。クラス[**Aspose.Cells.Drawing.ComboBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/combobox)コンボボックスを表します。いくつかの重要なメンバーがあります。

- の[**リンクされたセル**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/linkedcell)プロパティは、コンボ ボックスにリンクされているセルを指定します。
- の[**入力範囲**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/inputrange)プロパティは、コンボ ボックスを埋めるために使用されるセルのワークシート範囲を指定します。
- の[**ドロップダウンライン**](https://reference.aspose.com/cells/net/aspose.cells.drawing/combobox/properties/dropdownlines)プロパティは、コンボ ボックスのドロップダウン部分に表示されるリストの行数を指定します。
- の[**影**](https://reference.aspose.com/cells/net/aspose.cells.drawing/combobox/properties/shadow)プロパティは、コンボ ボックスに 3D シェーディングがあるかどうかを示します。

次の例は、ワークシートにコンボ ボックスを追加する方法を示しています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingComboBoxControl-1.cs" >}}

## **ワークシートへのラベル コントロールの追加**

ラベルは、スプレッドシートの内容に関する情報をユーザーに提供する手段です。 Aspose.Cells を使用すると、ワークシートでラベルを追加および操作できます。の[**シェイプコレクション**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection)クラスは、という名前のメソッドを提供します[**ラベルを追加**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addlabel)、ワークシートにラベル コントロールを追加するために使用されます。メソッドは[**ラベル**](https://reference.aspose.com/cells/net/aspose.cells.drawing/label)物体。クラス[**ラベル**](https://reference.aspose.com/cells/net/aspose.cells.drawing/label)ワークシートのラベルを表します。いくつかの重要なメンバーがあります。

- の[**文章**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/text)メソッドは、ラベルのキャプション文字列を指定します。
- の[**配置**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/placement)メソッドは[**配置タイプ**](https://reference.aspose.com/cells/net/aspose.cells.drawing/placementtype)、ワークシートのセルにラベルを付ける方法。

次の例は、ワークシートにラベルを追加する方法を示しています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingLabelControl-1.cs" >}}

## **ワークシートへのリスト ボックス コントロールの追加**

リスト ボックス コントロールは、1 つまたは複数の項目を選択できるリスト コントロールを作成します。

### **Microsoft エクセルを使う**

ワークシートにリスト ボックス コントロールを配置するには:

1. を確認してください**フォーム**ツールバーが表示されます。
1. クリックしてください**リストボックス**道具。
1. ワークシート領域で、クリック アンド ドラッグして、リスト ボックスを保持する四角形を定義します。
1. リスト ボックスがワークシートに配置されたら、コントロールを右クリックしてクリックします。**フォーマット制御**入力範囲を指定します。
1. の中に**Cell リンク**フィールドで、このリスト ボックスをリンクするセルのアドレスを指定し、選択タイプ (Single、Multi、Extend) 属性を設定します。
1. クリック**わかった**.

### **Aspose.Cells を使用**

の[**シェイプコレクション**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection)クラスは、という名前のメソッドを提供します[**AddListBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addlistbox) 、リスト ボックス コントロールをワークシートに追加するために使用されます。メソッドは[**Aspose.Cells.Drawing.ListBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/listbox)物体。クラス[**リストボックス**](https://reference.aspose.com/cells/net/aspose.cells.drawing/listbox)リストボックスを表します。いくつかの重要なメンバーがあります。

- の[**リンクされたセル**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/linkedcell)メソッドは、リスト ボックスにリンクされているセルを指定します。
- の[**入力範囲**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/inputrange)メソッドは、リスト ボックスを埋めるために使用されるセルのワークシート範囲を指定します。
- の[**選択タイプ**](https://reference.aspose.com/cells/net/aspose.cells.drawing/listbox/properties/selectiontype)メソッドは、リスト ボックスの選択モードを指定します。
- の[**影**](https://reference.aspose.com/cells/net/aspose.cells.drawing/listbox/properties/shadow)メソッドは、リスト ボックスに 3D シェーディングがあるかどうかを示します。

次の例は、ワークシートにリスト ボックスを追加する方法を示しています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingListBoxControl-1.cs" >}}

## **ボタン コントロールをワークシートに追加する**

ボタンは、いくつかのアクションを実行するのに役立ちます。場合によっては、VBA マクロをボタンに割り当てたり、ハイパーリンクを割り当てて Web ページを開くと便利です。

### **Microsoft エクセルを使う**

ワークシートにボタン コントロールを配置するには:

1. を確認してください**フォーム**ツールバーが表示されます。
1. クリックしてください**ボタン**道具。
1. ワークシート領域で、クリック アンド ドラッグして、ボタンを保持する四角形を定義します。
1. リスト ボックスがワークシートに配置されたら、コントロールを右クリックし、**フォーマット制御**、次に VBA マクロと属性に関連するフォント、配置、サイズ、余白などを指定します。
1. クリック**わかった**.

### **Aspose.Cells を使用**

の[**シェイプコレクション**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection)クラスは、という名前のメソッドを提供します[**追加ボタン**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addbutton)ボタン コントロールをワークシートに追加するために使用します。メソッドは[**Aspose.Cells.Drawing.Button**](https://reference.aspose.com/cells/net/aspose.cells.drawing/button)物体。クラス[**Aspose.Cells.Drawing.Button**](https://reference.aspose.com/cells/net/aspose.cells.drawing/button)ボタンを表します。いくつかの重要なメンバーがあります。

- の[**文章**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/text)プロパティは、ボタンのキャプションを指定します。
- の[**フォント**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/font)プロパティは、ボタン コントロールのラベルのフォント属性を指定します。
- の[**配置**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/placement)プロパティは、[**配置タイプ**](https://reference.aspose.com/cells/net/aspose.cells.drawing/placementtype)、ボタンがワークシートのセルに接続される方法。
- の[**ハイパーリンクを追加**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/methods/addhyperlink)プロパティは、ボタン コントロールのハイパーリンクを追加します。ボタンをクリックすると、関連する URL に移動します。

次の例は、ワークシートにボタンを追加する方法を示しています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingButtonControl-1.cs" >}}

## **ワークシートへの行コントロールの追加**

### **Microsoft エクセルを使う**

1. 上で**描く**ツールバー、クリック**オートシェイプ**、 指し示す**ライン**をクリックして、必要な線のスタイルを選択します。
1. ドラッグして線を引きます。
1. 次のいずれかまたは両方を実行します。
 1. 開始点から 15 度の角度で描画するように線を制限するには、Shift キーを押しながらドラッグします。
 1. 最初の終点から反対方向に線を伸ばすには、CTRL キーを押しながらドラッグします。

### **Aspose.Cells を使用**

の[**シェイプコレクション**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection)クラスは、という名前のメソッドを提供します[**行を追加**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addline)、ワークシートに線の形状を追加するために使用されます。メソッドは[**線の形状**](https://reference.aspose.com/cells/net/aspose.cells.drawing/lineshape)物体。クラス[**線の形状**](https://reference.aspose.com/cells/net/aspose.cells.drawing/lineshape)線を表します。いくつかの重要なメンバーがあります。

- の[**LineFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lineformat)メソッドは、行の形式を指定します。
- の[**配置**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/placement)メソッドは[**配置タイプ**](https://reference.aspose.com/cells/net/aspose.cells.drawing/placementtype)、ワークシート内のセルに線が接続される方法。

次の例は、ワークシートに行を追加する方法を示しています。スタイルの異なる 3 つのラインを作成します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingLineControl-1.cs" >}}

### **線に矢じりを追加する**

Aspose.Cells では、矢印の線を描くこともできます。線に矢印を追加し、線をフォーマットすることができます。たとえば、線の色を変更したり、線の太さとスタイルを指定したりできます。

次の例は、線に矢印を追加する方法を示しています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddinganArrowHead-1.cs" >}}

## **ワークシートへの四角形コントロールの追加**

Aspose.Cells を使用すると、ワークシートに四角形を描画できます。長方形、正方形などを作成できます。また、コントロールの塗りつぶしの色と境界線の色をフォーマットすることもできます。たとえば、必要に応じて、長方形の色を変更したり、陰影の色を設定したり、長方形の太さとスタイルを指定したりできます。

### **Microsoft エクセルを使う**

1. 上で**描く**ツールバー、クリック**矩形**.
1. ドラッグして長方形を描きます。
1. 次のいずれかまたは両方を実行します。
 1. 開始点から四角形を描くように長方形を制限するには、Shift キーを押しながらドラッグします。
 1. 中心点から長方形を描くには、CTRL キーを押しながらドラッグします。

### **Aspose.Cells を使用**

の[**シェイプコレクション**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection)クラスは、という名前のメソッドを提供します[**長方形を追加**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addrectangle)、ワークシートに四角形を追加するために使用されます。メソッドは戻ります[**Aspose.Cells.Drawing.RectangleShape**](https://reference.aspose.com/cells/net/aspose.cells.drawing/rectangleshape)物体。クラス[**Aspose.Cells.Drawing.RectangleShape**](https://reference.aspose.com/cells/net/aspose.cells.drawing/rectangleshape)長方形を表します。いくつかの重要なメンバーがあります。

- の[**LineFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lineformat)プロパティは、四角形の線の書式属性を指定します。
- の[**配置**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/placement)プロパティは、[**配置タイプ**](https://reference.aspose.com/cells/net/aspose.cells.drawing/placementtype)、四角形がワークシートのセルに接続される方法。
- の[**FillFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/fillformat)プロパティは、四角形の塗りつぶし形式のスタイルを指定します。

次の例は、ワークシートに四角形を追加する方法を示しています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingRectangleControl-1.cs" >}}

## **ワークシートへの円弧制御の追加**

Aspose.Cells を使用すると、ワークシートに円弧を描くことができます。シンプルで塗りつぶされた円弧を作成できます。コントロールの塗りつぶしの色と境界線の色をフォーマットできます。たとえば、円弧の色を指定/変更したり、シェーディングの色を設定したり、必要に応じて形状の重みとスタイルを指定したりできます。

### **Microsoft エクセルを使う**

1. 上で**描く**ツールバー、クリック**アーク**の中に**オートシェイプ**.
1. ドラッグして円弧を描きます。

### **Aspose.Cells を使用**

の[**シェイプコレクション**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection)クラスは、という名前のメソッドを提供します[**追加円弧**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addarc)、円弧形状をワークシートに追加するために使用されます。メソッドは[**Aspose.Cells.Drawing.ArcShape**](https://reference.aspose.com/cells/net/aspose.cells.drawing/arcshape)物体。クラス[**Aspose.Cells.Drawing.ArcShape**](https://reference.aspose.com/cells/net/aspose.cells.drawing/arcshape)円弧を表します。いくつかの重要なメンバーがあります。

- の[**LineFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lineformat)プロパティは、円弧形状の線形式属性を指定します。
- の[**配置**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/placement)プロパティは、[**配置タイプ**](https://reference.aspose.com/cells/net/aspose.cells.drawing/placementtype)、アークがワークシートのセルに接続される方法。
- の[**FillFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/fillformat)プロパティは、形状の塗りつぶし形式のスタイルを指定します。
- の[**右下の行**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lowerrightrow)プロパティは、右下隅の行インデックスを指定します。
- の[**右下の列**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lowerrightcolumn)プロパティは、右下隅の列インデックスを指定します。

次の例は、アーク形状をワークシートに追加する方法を示しています。この例では、2 つの円弧形状を作成します。1 つは塗りつぶされ、もう 1 つは単純です。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingArcControl-1.cs" >}}

## **楕円形コントロールをワークシートに追加する**

Aspose.Cells では、ワークシートに楕円形を描くことができます。シンプルで塗りつぶされた楕円形を作成し、コントロールの塗りつぶしの色と境界線の色をフォーマットします。たとえば、楕円の色を指定/変更したり、シェーディングの色を設定したり、形状の太さとスタイルを指定したりできます。

### **Microsoft エクセルを使う**

- 上で*描く*ツールバー、クリック*オーバル*.
- ドラッグして楕円を描きます。
- 次のいずれかまたは両方を実行します。
- 楕円が始点から円を描くように制限するには、Shift キーを押しながらドラッグします。
- 中心点から楕円を描くには、CTRL キーを押しながらドラッグします。

### **Aspose.Cells を使用**

の[**シェイプコレクション**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection)クラスは、という名前のメソッドを提供します[**AddOval**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addoval) 、ワークシートに楕円形を追加するために使用されます。メソッドは[**Aspose.Cells.Drawing.Oval**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oval)物体。クラス[**Aspose.Cells.Drawing.Oval**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oval)楕円形を表します。いくつかの重要なメンバーがあります。

- の[**LineFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lineformat)プロパティは、楕円形のライン フォーマット属性を指定します。
- の[**配置**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/placement)プロパティは、[**配置タイプ**](https://reference.aspose.com/cells/net/aspose.cells.drawing/placementtype)、楕円がワークシートのセルに接続される方法。
- の[**FillFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/fillformat)プロパティは、形状の塗りつぶし形式のスタイルを指定します。
- の[**右下の行**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lowerrightrow)プロパティは、右下隅の行インデックスを指定します。
- の[**右下の列**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lowerrightcolumn)プロパティは、右下隅の列インデックスを指定します。

次の例は、楕円形をワークシートに追加する方法を示しています。この例では、2 つの楕円形を作成します。1 つは塗りつぶされた楕円形で、もう 1 つは単純な円です。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingOvalControl-1.cs" >}}

## **スピナー コントロールをワークシートに追加する**

スピン ボックスは、上向き矢印と下向き矢印で構成されるボタン (スピン ボタンと呼ばれる) に接続されたテキスト ボックスで、クリックするとテキスト ボックスの値が段階的に変更されます。スピン ボックスを使用すると、財務モデルへの入力の変更がモデルの出力をどのように変更するかを確認できます。特定の入力セルにスピン ボタンをアタッチできます。スピン ボタンの上矢印または下矢印をクリックすると、対象の入力セルの整数値が増減します。*Aspose.Cells*ワークシートにスピナーを作成できます。

### **Microsoft エクセルを使う**

ワークシートにスピン ボックス コントロールを配置するには:

- を確認してください*フォーム*ツールバーが表示されます。
- クリック*スピナー*道具。
- ワークシート領域で、クリック アンド ドラッグして、スピナーを保持する長方形を定義します。
- スピナーがワークシートに配置されたら、コントロールを右クリックして*フォーマット制御*最大値、最小値、増分値を指定します。
- の中に*Cell リンク*フィールドで、このスピン ボックスをリンクするセルのアドレスを指定します。
- クリック*わかった*.

### **Aspose.Cells を使用**

の[**シェイプコレクション**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection)クラスは、という名前のメソッドを提供します[**AddSpinner**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addspinner)、スピン ボックス コントロールをワークシートに追加するために使用されます。メソッドは[**Aspose.Cells.Drawing.Spinner**](https://reference.aspose.com/cells/net/aspose.cells.drawing/spinner)物体。クラス[**Aspose.Cells.Drawing.Spinner**](https://reference.aspose.com/cells/net/aspose.cells.drawing/spinner)スピンボックスを表します。いくつかの重要なメンバーがあります。

- の[**リンクされたセル**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/linkedcell)プロパティは、スピン ボックスにリンクされているセルを指定します。
- の[**マックス**](https://reference.aspose.com/cells/net/aspose.cells.drawing/spinner/properties/max)プロパティは、スピン ボックスの範囲の最大値を指定します。
- の[**分**](https://reference.aspose.com/cells/net/aspose.cells.drawing/spinner/properties/min)プロパティは、スピン ボックスの範囲の最小値を指定します。
- の[**増分変更**](https://reference.aspose.com/cells/net/aspose.cells.drawing/spinner/properties/incrementalchange)プロパティは、ライン スクロールによってスピナーがインクリメントされる値の量を指定します。
- の[**影**](https://reference.aspose.com/cells/net/aspose.cells.drawing/spinner/properties/shadow)プロパティは、スピン ボックスに 3D シェーディングがあるかどうかを示します。
- の[**現在の価値**](https://reference.aspose.com/cells/net/aspose.cells.drawing/spinner/properties/currentvalue)プロパティは、スピン ボックスの現在の値を指定します。

次の例は、ワークシートにスピン ボックスを追加する方法を示しています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingSpinnerControl-1.cs" >}}

## **ワークシートへのスクロール バー コントロールの追加**

スクロール バー コントロールは、スピン ボックス コントロールと同様の方法でワークシート上のデータを選択するために使用されます。コントロールをワークシートに追加してセルにリンクすることにより、コントロールの現在位置の数値を返すことができます。

### **Microsoft エクセルを使う**

- Excel 2003 以前のバージョンでスクロール バーを追加するには、*スクロール・バー*ボタン*フォーム*ツールバーをクリックし、高さがセル B2:B6 をカバーし、列の幅の約 4 分の 1 のスクロール バーを作成します。
-  Excel 2007 でスクロール バーを追加するには、*デベロッパー*タブ、クリック*入れる*をクリックし、*スクロール・バー*フォーム コントロール セクションにあります。
- スクロール バーを右クリックし、*フォーマット制御*.
- 次の情報を入力して、*わかった*:
 - の中に*現在の価値*ボックス、タイプ 1。
 - の中に*最小値*ボックスに 1 を入力します。この値は、スクロール バーの上部をリストの最初の項目に制限します。
 - の中に*最大値*ボックスに 20 と入力します。この数は、リスト内のエントリの最大数を指定します。
 - の中に*増分変更*ボックスに 1 を入力します。この値は、スクロール バー コントロールが現在の値をインクリメントする数を制御します。
 - の中に*ページ変更*ボックスに 5 と入力します。このエントリは、スクロール ボックスのいずれかの側のスクロール バー内をクリックした場合に、現在の値がどれだけ増加するかを制御します。
 セル G1 に数値を入力するには (リストで選択されている項目によって異なります)、*Cell リンク*箱。
- スクロール バーが選択されないように任意のセルをクリックします。

スクロール バーのアップまたはダウン コントロールをクリックすると、セル G1 は、スクロール バーの現在の値にスクロール バーの増分変化を加えた値または引いた値を示す数値に更新されます。

### **Aspose.Cells を使用**

の[**シェイプコレクション**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection)クラスは、という名前のメソッドを提供します[**AddScrollBar**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addscrollbar) 、スクロール バー コントロールをワークシートに追加するために使用されます。メソッドは[**Aspose.Cells.Drawing.ScrollBar**](https://reference.aspose.com/cells/net/aspose.cells.drawing/scrollbar)物体。クラス[**Aspose.Cells.Drawing.ScrollBar**](https://reference.aspose.com/cells/net/aspose.cells.drawing/scrollbar)スクロールバーを表します。いくつかの重要なメンバーがあります。

- の[**リンクされたセル**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/linkedcell)プロパティは、スクロール バーにリンクされているセルを指定します。
- の[**マックス**](https://reference.aspose.com/cells/net/aspose.cells.drawing/scrollbar/properties/max)プロパティは、スクロール バーの範囲の最大値を指定します。
- の[**分**](https://reference.aspose.com/cells/net/aspose.cells.drawing/scrollbar/properties/min)プロパティは、スクロール バーの範囲の最小値を指定します。
- の[**増分変更**](https://reference.aspose.com/cells/net/aspose.cells.drawing/scrollbar/properties/incrementalchange)プロパティは、行スクロールでスクロール バーがインクリメントされる値の量を指定します。
- の[**影**](https://reference.aspose.com/cells/net/aspose.cells.drawing/scrollbar/properties/shadow)プロパティは、スクロール バーに 3D シェーディングがあるかどうかを示します。
- の[**現在の価値**](https://reference.aspose.com/cells/net/aspose.cells.drawing/scrollbar/properties/currentvalue)プロパティは、スクロール バーの現在の値を指定します。
- の[**ページ変更**](https://reference.aspose.com/cells/net/aspose.cells.drawing/scrollbar/properties/pagechange)プロパティは、スクロール ボックスのいずれかの側にあるスクロール バーの内側をクリックした場合に、現在の値が増加する量を指定します。

次の例は、ワークシートにスクロール バーを追加する方法を示しています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingScrollBarControl-1.cs" >}}

## **ワークシートのグループ コントロールへの GroupBox コントロールの追加**

特定のグループに属するラジオ ボタンやその他のコントロールを実装する必要がある場合があります。グループ ボックスまたは四角形のコントロールを含めることで実装できます。これら 2 つのオブジェクトのいずれかが、グループの区切り文字として機能します。これらの図形の 1 つを追加した後、2 つ以上のラジオ ボタンまたは他のグループ オブジェクトを追加できます。

### **Microsoft エクセルを使う**

ワークシートにグループ ボックス コントロールを配置し、その中にコントロールを配置するには:

- フォームを開始するには、メイン メニューで*意見*、 に続く*ツールバー*と*フォーム*.
- 上で*フォーム*ツールバーで、*グループボックス*そしてワークシートに長方形を描きます。
- ボックスのキャプション文字列を入力します。
- 上で*フォーム*ツールバー、クリック*オプションボタン*をクリックし、*グループボックス*キャプション文字列のすぐ下。
- から*フォーム*ツールバーを再度クリックし、*オプションボタン*をクリックし、*グループボックス*最初のラジオボタンの下。
- もう一度*フォーム*ツールバー、クリック*オプションボタン*をクリックし、*グループボックス*前のラジオボタンの下。

### **Aspose.Cells を使用**

の[**シェイプコレクション**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection)クラスは、という名前のメソッドを提供します[**グループボックスを追加**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addgroupbox)、グループ ボックス コントロールをワークシートに追加するために使用されます。メソッドは[**Aspose.Cells.Drawing.GroupBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/groupbox)物体。さらに、[**グループ**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/group)の方法[**シェイプコレクション**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection)クラスは形状をグループ化します。[**形**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape)配列をパラメータとして返し、[**グループシェイプ**](https://reference.aspose.com/cells/net/aspose.cells.drawing/groupshape)物体。クラス[**Aspose.Cells.Drawing.GroupBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/groupbox)グループボックスを表します。いくつかの重要なメンバーがあります。

- の[**文章**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/text)プロパティは、グループ ボックスのキャプション文字列を指定します。
- の[**影**](https://reference.aspose.com/cells/net/aspose.cells.drawing/groupbox/properties/shadow)プロパティは、グループ ボックスに 3D シェーディングがあるかどうかを示します。

次の例は、グループ ボックスを追加し、ワークシート内のコントロールをグループ化する方法を示しています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingGroupBoxControl-1.cs" >}}

## **先行トピック**
- [Aspose.Cells を使用して ActiveX コントロールを追加します](/cells/ja/net/add-activex-controls-using-aspose-cells/)
- [ActiveX コントロールを削除する](/cells/ja/net/remove-activex-control/)
- [ActiveX ComboBox コントロールの更新](/cells/ja/net/update-activex-combobox-control/)
