---
title: コントロールの管理
type: docs
weight: 150
url: /ja/python-net/managing-controls/
---

## **紹介**

開発者は、テキストボックス、チェックボックス、ラジオボタン、コンボボックス、ラベル、ボタン、線、長方形、弧、楕円、スピナー、スクロールバー、グループボックスなどのさまざまな描画オブジェクトを追加できます。Aspose.Cells for Python via .NET は、すべての描画オブジェクトを含む Aspose.Cells.Drawing 名前空間を提供します。ただし、一部の描画オブジェクトや図形はまだサポートされていません。Microsoft Excel を使用してこれらの描画オブジェクトをデザイナーのスプレッドシートで作成し、その後、そのデザイナーのスプレッドシートを Aspose.Cells にインポートしてください。Aspose.Cells for Python via .NET は、これらの描画オブジェクトをデザイナーのスプレッドシートからロードし、生成されたファイルに書き込むことを可能にします。

## **ワークシートにテキストボックスコントロールを追加**

レポート内の重要な情報を強調する一つの方法は、テキストボックスを使用することです。例えば、会社名をハイライトするためや、売上高が最も高い地域を示すためなどです。Aspose.Cells for Python via .NET は、コレクションに新しいテキストボックスを追加するために [**TextBoxCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/textboxcollection) クラスを提供します。もう一つのクラス [**TextBox**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/textbox) は、すべての設定タイプを定義するためのテキストボックスを表します。重要なメンバーがいくつかあります：

- [**text_frame**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/text_frame)プロパティは、テキストボックスの内容を調整するために使用される[**MsoTextFrame**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/msotextframe)オブジェクトを返します。
- [**placement**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/placement)プロパティは配置タイプを指定します。
- [**font**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/font)プロパティはフォント属性を指定します。
- [**add_hyperlink**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/add_hyperlink)メソッドは、テキストボックスにハイパーリンクを追加します。
- [**fill_format**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/fill_format)プロパティは、テキストボックスの塗りつぶし形式を設定するために使用される[**MsoFillFormat**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/msofillformat)オブジェクトを返します。
- [**line_format**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/line_format)プロパティは、テキストボックスのラインのスタイルと太さを通常設定するために使用される[**MsoLineFormat**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/msolineformat)オブジェクトを返します。
- [**text**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/text)プロパティは、テキストボックスの入力テキストを指定します。

次の例では、ブックの最初のワークシートに2つのテキストボックスを作成します。最初のテキストボックスはさまざまなフォーマット設定で整備されています。2番目はシンプルなものです。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Controls-AddingTextBoxControl-1.py" >}}

## **デザイナースプレッドシート内のテキストボックスコントロールの操作**

Aspose.Cells for Python via .NET は、デザイナーのワークシート内のテキストボックスにアクセスし、それらを操作することも可能です。[**Worksheet.TextBoxes**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/text_boxes) プロパティを使用して、シート内のテキストボックスのコレクションを取得します。

次の例では、上記の例で作成したMicrosoft Excelファイルを使用しています。2つのテキストボックスのテキストを取得し、2番目のテキストボックスのテキストを変更してファイルを保存します。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Controls-ManipulatingTextBoxControls-1.py" >}}

## **ワークシートにチェックボックスコントロールを追加する**

チェックボックスは、true または false、はい または いいえなどの二つの選択肢の中からユーザーに選ばせる方法を提供したい場合に便利です。Aspose.Cells for Python via .NET では、ワークシート内にチェックボックスを使用できます。例えば、特定の買収について考慮するかどうかを示す財務予測ワークシートを作成した場合、ワークシートの上部にチェックボックスを配置したいことがあります。その後、そのチェックボックスの状態を別のセルにリンクさせ、チェックボックスが選択されている場合はセルの値が True に、選択されていない場合は False になるように設定できます。

### **Microsoft Excel の使用**

ワークシートにチェックボックスコントロールを配置するには、次の手順に従います。

1. フォームツールバーが表示されていることを確認します。
1. フォームツールバーの**チェックボックス**ツールをクリックします。
1. ワークシートエリアで、チェックボックスとチェックボックスの横に表示されるラベルを定義するためにクリックしてドラッグします。
1. チェックボックスが配置されたら、マウスカーソルをラベル領域に移動してラベルを変更します。
1. **セルリンク**フィールドで、このチェックボックスをリンクするセルのアドレスを指定します。
1. **OK** をクリックします。

### **Aspose.Cells for Python via .NETを使用して**

Aspose.Cells for Python via .NET は、新しいチェックボックスをコレクションに追加するために [**CheckBoxCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/checkboxcollection) クラスを提供します。もう一つのクラス [**Aspose.Cells.Drawing.CheckBox**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/checkbox) はチェックボックスを表します。重要なメンバーがいくつかあります：

- [**linked_cell**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/linked_cell)プロパティは、チェックボックスにリンクされるセルを指定します。
- [**text**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/text)プロパティは、チェックボックスに関連付けられたテキスト文字列を指定します。これはチェックボックスのラベルです。
- [**value**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/checkbox/value)プロパティは、チェックボックスが選択されているかどうかを指定します。

次の例では、ワークシートにチェックボックスを追加する方法を示しています。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Controls-AddingCheckBoxControl-1.py" >}}

## **ワークシートにラジオボタンコントロールを追加する**

ラジオボタン、またはオプションボタンは、円形のボックスからなるコントロールです。ユーザーはラウンドボックスを選択することで決定を行います。ラジオボタンは通常、他のラジオボタンに伴って表示され、グループとして振る舞います。ユーザーは1つのボタンのみを選択することで、どのボタンが有効か決定します。ユーザーが1つのボタンをクリックすると、それは選択されます。グループ内の1つのボタンが選択されると、同じグループのボタンは空になります。

### **Microsoft Excel の使用**

ワークシートにラジオボタンコントロールを配置するには、次の手順に従います。

1. **フォーム** ツールバーが表示されていることを確認します。
1. **オプションボタン**ツールをクリックします。
1. ワークシートで、オプションボタンとオプションボタンの横に表示されるラベルを定義するためにクリックしてドラッグします。
1. ワークシートにラジオボタンを配置したら、マウスカーソルをラベル領域に移動してラベルを変更します。
1. **セルリンク**フィールドで、このラジオボタンがリンクされるセルのアドレスを指定します。
1. **OK** をクリックします。

### **Aspose.Cells for Python via .NETを使用して**

[**Aspose.Cells.Drawing.ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection)クラスには、ワークシートにラジオボタンコントロールを追加するために使用される[**add_radio_button**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_radio_button)というメソッドがあります。このメソッドは[**Aspose.Cells.Drawing.RadioButton**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/radiobutton)オブジェクトを返します。また、[**Aspose.Cells.Drawing.RadioButton**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/radiobutton)クラスもあります。

- [**linked_cell**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/linked_cell)プロパティは、ラジオボタンにリンクされるセルを指定します。
- [**text**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/text)プロパティは、ラジオボタンに関連付けられたテキスト文字列を指定します。これはラジオボタンのラベルです。
- [**is_checked**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/radiobutton/is_checked)プロパティは、ラジオボタンが選択されているかどうかを指定します。
- [**fill_format**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/fill_format)プロパティは、ラジオボタンの塗りつぶし形式を指定します。
- [**line_format**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/line_format)プロパティは、オプションボタンの線の形式スタイルを指定します。

次の例では、ワークシートにラジオボタンを追加する方法を示しています。例では、3つの年齢グループを表すラジオボタンが追加されています。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Controls-AddingRadioButtonControl-1.py" >}}

## **ワークシートにコンボボックスコントロールを追加する**

データの入力を容易にするか、定義した項目にエントリを制限するためには、ワークシートの他のセルからコンパイルされる有効なエントリのコンボボックス、またはドロップダウンリストを作成できます。セルのドロップダウンリストを作成すると、そのセルの隣に矢印が表示されます。そのセルに情報を入力するには、矢印をクリックし、その後、欲しいエントリをクリックします。

### **Microsoft Excel の使用**

ワークシートにコンボボックスコントロールを配置するには、次の手順に従います：

1. **フォーム** ツールバーが表示されていることを確認します。
1. **コンボボックス** ツールをクリックします。
1. ワークシートエリアで、コンボボックスを保持する四角形を定義するためにクリックしてドラッグします。
1. コンボボックスがワークシートに配置されたら、コントロールを右クリックして **コントロールの書式設定** をクリックし、入力範囲を指定します。
1. **セルリンク** フィールドで、このコンボボックスをリンクするセルのアドレスを指定します。
1. **OK** をクリックします。

### **Aspose.Cells for Python via .NETを使用して**

クラス [**Aspose.Cells.Drawing.ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection) は [**add_combo_box**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_combo_box) という名前のメソッドを提供し、これはワークシートにコンボボックスコントロールを追加するために使用されます。このメソッドは [**Aspose.Cells.Drawing.ComboBox**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/combobox) オブジェクトを返します。[**Aspose.Cells.Drawing.ComboBox**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/combobox) クラスはコンボボックスを表します。いくつかの重要なメンバを持っています：

- [**linked_cell**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/linked_cell) プロパティはコンボボックスにリンクされたセルを指定します。
- [**input_range**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/input_range) プロパティはコンボボックスを埋めるために使用されるワークシートのセル範囲を指定します。
- [**drop_down_lines**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/combobox/drop_down_lines) プロパティはドロップダウン部分に表示されるリスト行の数を指定します。
- [**shadow**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/combobox/shadow) プロパティはコンボボックスが 3D シェーディングを持っているかどうかを示します。

次の例は、ワークシートにコンボボックスを追加する方法を示しています。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Controls-AddingComboBoxControl-1.py" >}}

## **ワークシートにラベルコントロールを追加する**

ラベルは、スプレッドシートの内容についてユーザーに情報を提供する手段です。Aspose.Cells for Python via .NET では、ワークシート内のラベルを追加・操作することが可能です。[**ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection) クラスは、[**add_label**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_label) というメソッド提供し、これを使用してラベルコントロールをワークシートに追加します。このメソッドは [**Label**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/label) オブジェクトを返します。[**Label**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/label) クラスは、ワークシート内のラベルを表します。重要なメンバーがいくつかあります。

- [**text**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/text) メソッドはラベルのキャプション文字列を指定します。
- [**placement**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/placement) メソッドは、ラベルがワークシート内のセルにどのようにアタッチされるかを指定します。

次の例は、ワークシートにラベルを追加する方法を示しています。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Controls-AddingLabelControl-1.py" >}}

## **ワークシートにリストボックスコントロールを追加する**

リストボックスコントロールは、単一または複数のアイテム選択を可能にするリストコントロールを作成します。

### **Microsoft Excel の使用**

ワークシートにリストボックスコントロールを配置するには：

1. **フォーム** ツールバーが表示されていることを確認します。
1. **リストボックス** ツールをクリックします。
1. ワークシートエリアで、リストボックスを保持する四角形を定義するためにクリックしてドラッグします。
1. リストボックスがワークシートに配置されたら、コントロールを右クリックして **コントロールの書式設定** をクリックし、入力範囲を指定します。
1. **セルリンク** フィールドで、このリストボックスをリンクするセルのアドレスを指定し、選択タイプ（単一、複数、拡張）属性を設定します。
1. **OK** をクリックします。

### **Aspose.Cells for Python via .NETを使用して**

クラス [**ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection) は、ワークシートにリストボックスコントロールを追加するために使用される [**add_list_box**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_list_box) という名前のメソッドを提供します。このメソッドは [**Aspose.Cells.Drawing.ListBox**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/listbox) オブジェクトを返します。[**ListBox**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/listbox) クラスはリストボックスを表します。いくつかの重要なメンバを持っています：

- [**linked_cell**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/linked_cell) メソッドはリストボックスにリンクされたセルを指定します。
- [**input_range**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/input_range) メソッドはリストボックスを埋めるために使用されるワークシートのセル範囲を指定します。
- [**selection_type**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/listbox/selection_type) メソッドはリストボックスの選択モードを指定します。
- [**shadow**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/listbox/shadow) メソッドはリストボックスに3Dシェーディングがあるかどうかを示します。

次の例は、ワークシートにリストボックスを追加する方法を示しています。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Controls-AddingListBoxControl-1.py" >}}

## **ボタンコントロールをワークシートに追加する**

ボタンは何かアクションを行うために便利です。時には、ボタンにVBAマクロを割り当てたり、Webページを開くためのハイパーリンクを割り当てることも有用です。

### **Microsoft Excel の使用**

ボタンコントロールをワークシートに配置するには:

1. **フォーム** ツールバーが表示されていることを確認します。
1. **ボタン** ツールをクリックします。
1. ワークシート領域でクリックしてドラッグして、ボタンを配置する矩形を定義します。
1. リストボックスがワークシートに配置されたら、コントロールを右クリックして **フォーマットコントロール** を選択し、VBAマクロを指定し、フォント、配置、サイズ、余白などに関連する属性を設定します。
1. **OK** をクリックします。

### **Aspose.Cells for Python via .NETを使用して**

 [**ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection) クラスは、ボタンコントロールをワークシートに追加するための [**add_button**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_button) という名前のメソッドを提供します。このメソッドは [**Aspose.Cells.Drawing.Button**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/button) オブジェクトを返します。クラス [**Aspose.Cells.Drawing.Button**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/button) はボタンを表します。いくつかの重要なメンバーがあります:

- [**text**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/text) プロパティはボタンのキャプションを指定します。
- [**font**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/font) プロパティはボタンコントロールのラベルのフォント属性を指定します。
- [**placement**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/placement) プロパティはボタンがワークシートのセルにアタッチされる方法を指定します。
- [**add_hyperlink**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/add_hyperlink) プロパティはボタンコントロールにハイパーリンクを追加します。ボタンをクリックすると関連するURLに移動します。

次の例は、ワークシートにボタンを追加する方法を示しています。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Controls-AddingButtonControl-1.py" >}}

## **ワークシートにラインコントロールを追加する**

### **Microsoft Excel の使用**

1. **描画** ツールバーで **オートシェイプ** をクリックし、**ライン** を指して、希望のラインスタイルを選択します。
1. ドラッグしてラインを描きます。
1. 次のいずれかを行います。
   1. ラインを開始点から15度の角度で制限するには、ドラッグしながら **SHIFT** キーを押します。
   1. 最初の端点から異なる方向にラインを長くするには、ドラッグしながら **CTRL** キーを押します。

### **Aspose.Cells for Python via .NETを使用して**

[**ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection) クラスは、ワークシートにラインシェイプを追加するために使用される [**add_line**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_line) という名前のメソッドを提供します。このメソッドは [**LineShape**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/lineshape) オブジェクトを返します。クラス [**LineShape**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/lineshape) はラインを表します。いくつかの重要なメンバーがあります:

- [**line_format**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/line_format) メソッドはラインのフォーマットを指定します。
- [**placement**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/placement) メソッドはラインがワークシートのセルにアタッチされる方法を指定します。

次の例は、ワークシートにラインを追加する方法を示しています。異なるスタイルで3つのラインが作成されます。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Controls-AddingLineControl-1.py" >}}

### **ラインに矢印を追加する**

Aspose.Cells for Python via .NET は、矢印線を描画することも可能です。線に矢じりを追加したり、線の書式を設定したりすることができます。例えば、線の色を変更したり、線の太さやスタイルを指定したりできます。

次の例は、ラインに矢印を追加する方法を示しています。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Controls-AddinganArrowHead-1.py" >}}

## **ワークシートに長方形コントロールを追加する**

Aspose.Cells for Python via .NET は、ワークシートに長方形の図形を描画することを可能にします。長方形、正方形などを作成でき、塗りつぶし色や境界線の色のフォーマットも可能です。例えば、長方形の色を変更したり、シェーディング色を設定したり、必要に応じて太さやスタイルを指定できます。

### **Microsoft Excel の使用**

1. **描画**ツールバーで、**長方形**をクリックします。
1. 長方形を描画するには、ドラッグします。
1. 次のいずれかを行います。
   1. 長方形を開始点から正方形に描画するには、ドラッグしながらSHIFTキーを押し続けます。
   1. 長方形を中心点から描画するには、ドラッグしながらCTRLキーを押し続けます。

### **Aspose.Cells for Python via .NETを使用して**

クラス[**ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection)には、ワークシートに長方形を追加するための[**add_rectangle**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_rectangle)という名前のメソッドがあります。このメソッドは[**Aspose.Cells.Drawing.RectangleShape**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/rectangleshape)オブジェクトを返します。クラス[**Aspose.Cells.Drawing.RectangleShape**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/rectangleshape)は長方形を表します。いくつか重要なメンバーがあります。

- [**line_format**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/line_format)プロパティは長方形の線の書式属性を指定します。
- [**placement**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/placement)プロパティは[**PlacementType**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/placementtype)を指定し、長方形がワークシートのセルにアタッチされる方法を示します。
- [**fill_format**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/fill_format)プロパティは長方形の塗りつぶしの書式スタイルを指定します。

次の例は、ワークシートに長方形を追加する方法を示しています。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Controls-AddingRectangleControl-1.py" >}}

## **ワークシートに円弧コントロールを追加する**

Aspose.Cells for Python via .NET は、楕円の図形を描画することもできます。シンプルな楕円や塗りつぶし楕円を作成し、塗りつぶし色や境界線の色をフォーマットすることができます。

### **Microsoft Excel の使用**

1. **図形の自動スタイル**で、**円弧**をクリックします。
1. 円弧を描画するには、ドラッグします。

### **Aspose.Cells for Python via .NETを使用して**

クラス[**ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection)には、ワークシートに円弧形状を追加するための[**add_arc**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_arc)という名前のメソッドがあります。このメソッドは[**Aspose.Cells.Drawing.ArcShape**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/arcshape)オブジェクトを返します。クラス[**Aspose.Cells.Drawing.ArcShape**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/arcshape)は円弧を表します。いくつか重要なメンバーがあります。

- [**line_format**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/line_format)プロパティは円弧形状の線の書式属性を指定します。
- [**placement**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/placement)プロパティは[**PlacementType**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/placementtype)を指定し、円弧がワークシートのセルにアタッチされる方法を示します。
- [**fill_format**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/fill_format)プロパティは形状の塗りつぶし形式スタイルを指定します。
- [**lower_right_row**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/lower_right_row)プロパティは右下の行インデックスを指定します。
- [**lower_right_column**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/lower_right_column)プロパティは右下の列インデックスを指定します。

次の例は、ワークシートに円弧形状を追加する方法を示しています。この例では、塗りつぶしの円弧形状とシンプルな円弧形状の2つを作成します。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Controls-AddingArcControl-1.py" >}}

## **ワークシートに楕円コントロールを追加する**

Aspose.Cells for Python via .NET は、ワークシートに楕円形を描くことも可能です。シンプルまたは塗りつぶしの楕円を作成し、塗りつぶし色や境界線の色を設定できます。

### **Microsoft Excel の使用**

- *図形*ツールバーで、*楕円*をクリックします。
- 楕円を描画するには、ドラッグします。
- 以下のいずれか、または両方を行います。
- 楕円を開始点から円として描画するには、ドラッグしながらSHIFTキーを押し続けます。
- 楕円を中心点から描画するには、ドラッグしながらCTRLキーを押し続けます。

### **Aspose.Cells for Python via .NETを使用して**

クラス[**ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection)は、ワークシートに楕円形を追加するために使用される[**add_oval**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_oval)というメソッドを提供します。このメソッドは[**Aspose.Cells.Drawing.Oval**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/oval)オブジェクトを返します。クラス[**Aspose.Cells.Drawing.Oval**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/oval)は楕円形を表し、いくつかの重要なメンバーがあります。

- [**line_format**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/line_format)プロパティは楕円形の線形式属性を指定します。
- [**placement**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/placement)プロパティはワークシート内のセルに楕円形を接続する方法を指定します。
- [**fill_format**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/fill_format)プロパティは形状の塗りつぶし形式スタイルを指定します。
- [**lower_right_row**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/lower_right_row)プロパティは右下の行インデックスを指定します。
- [**lower_right_column**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/lower_right_column)プロパティは右下の列インデックスを指定します。

次の例は、ワークシートに楕円形を追加する方法を示しています。この例では、塗りつぶしの楕円形と単純な円形の2つの楕円形を作成します。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Controls-AddingOvalControl-1.py" >}}

## **ワークシートにスピンボックスコントロールを追加**

スピンボックスは、上矢印と下矢印のついたボタン（スピンボタン）に付属したテキストボックスです。クリックすることで値を段階的に増減させることができます。スピンボックスを使用すると、財務モデルに入力された値の変化が、モデルの出力にどのように影響するかを見ることができます。特定の入力セルにスピンボタンを結びつけることが可能です。スピンボタンの上矢印または下矢印をクリックすると、対象の入力セルの整数値が増加または減少します。*Aspose.Cells for Python via .NET* では、ワークシートにスピナーを作成できます。

### **Microsoft Excel の使用**

ワークシートにスピンボックスコントロールを配置するには:

- *フォーム*ツールバーが表示されていることを確認します。
- *スピンボックス*ツールをクリックします。
- ワークシート領域で、スピンボックスを保持する矩形を定義するためにクリックしてドラッグします。
- スピンボックスをワークシートに配置したら、コントロールを右クリックして *フォーマットコントロール* をクリックし、最大値、最小値、増分値を指定します。
- *セルリンク* フィールドに、このスピンボックスをリンクするセルのアドレスを指定します。
- *OK* をクリックします。

### **Aspose.Cells for Python via .NETを使用して**

クラス[**ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection)は、ワークシートにスピンボックスコントロールを追加するために使用される[**add_spinner**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_spinner)というメソッドを提供します。このメソッドは[**Aspose.Cells.Drawing.Spinner**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/spinner)オブジェクトを返します。クラス[**Aspose.Cells.Drawing.Spinner**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/spinner)はスピンボックスを表し、いくつかの重要なメンバーがあります。

- [**linked_cell**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/linked_cell)プロパティは、スピンボックスにリンクされたセルを指定します。
- [**max**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/spinner/max)プロパティは、スピンボックス範囲の最大値を指定します。
- [**min**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/spinner/min)プロパティは、スピンボックス範囲の最小値を指定します。
- [**incremental_change**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/spinner/incremental_change)プロパティは、スピンボックスが1行スクロールされる値の量を指定します。
- [**shadow**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/spinner/shadow)プロパティは、スピンボックスに3Dシェーディングがあるかどうかを示します。
- [**current_value**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/spinner/current_value)プロパティは、スピンボックスの現在の値を指定します。

次の例は、ワークシートにスピンボックスを追加する方法を示しています。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Controls-AddingSpinnerControl-1.py" >}}

## **ワークシートにスクロールバーコントロールを追加する**

スクロールバーコントロールは、ワークシート上のデータを選択するのを支援するために使用され、スピンボックスコントロールと同様の方法でワークシートに追加できます。ワークシートにコントロールを追加し、セルにリンクすることで、コントロールの現在の位置の数値を返すことができます。

### **Microsoft Excel の使用**

- Excel 2003およびそれ以前のバージョンでは、*フォーム*ツールバーの *スクロールバー* ボタンをクリックし、高さでセルB2:B6をカバーし、列の1/4程度の幅でスクロールバーを作成します。
- Excel 2007では、*開発*タブをクリックし、*挿入*をクリックし、フォームコントロールセクションで*スクロールバー*をクリックします。
- スクロールバーを右クリックし、*フォーマットコントロール*をクリックします。
- 次の情報を入力し、*OK*をクリックします。
  - *現在の値*ボックスに1と入力します。
  - *最小値*ボックスに1と入力します。この値は、スクロールバーの上部をリスト内の最初のアイテムに制限します。
  - *最大値*ボックスに20と入力します。この数はリスト内のエントリの最大数を指定します。
  - *増分変更*ボックスに1と入力します。この値は、スクロールバーが現在の値を増分変更する数を制御します。
  - *ページ変更*ボックスに5と入力します。このエントリは、スクロールバー内のスクロールボックスのいずれかの側をクリックした場合に、現在の値が増分変更される量を制御します。
  - リストで選択されたアイテムに応じてセルG1に数値を入力する場合、*セルリンク*ボックスにG1と入力します。
- スクロールバーが選択されていないことを確認するために、どこかのセルをクリックします。

スクロールバーの上または下のコントロールをクリックすると、セルG1はスクロールバーの現在の値に増分変更を足したり引いたりした数値に更新されます。

### **Aspose.Cells for Python via .NETを使用して**

[**ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection)クラスは、ワークシートにスクロールバーコントロールを追加するために使用される[**add_scroll_bar**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_scroll_bar)というメソッドを提供します。このメソッドは[**Aspose.Cells.Drawing.ScrollBar**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/scrollbar)オブジェクトを返します。[**Aspose.Cells.Drawing.ScrollBar**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/scrollbar)クラスはスクロールバーを表します。いくつかの重要なメンバーがあります:

- [**linked_cell**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/linked_cell)プロパティは、スクロールバーにリンクされたセルを指定します。
- [**max**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/scrollbar/max)プロパティは、スクロールバー範囲の最大値を指定します。
- [**min**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/scrollbar/min)プロパティは、スクロールバー範囲の最小値を指定します。
- [**incremental_change**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/scrollbar/incremental_change)プロパティは、スクロールバーが1行スクロールされたときの値の量を指定します。
- [**shadow**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/scrollbar/shadow)プロパティは、スクロールバーに3Dの影があるかどうかを示します。
- [**current_value**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/scrollbar/current_value)プロパティは、スクロールバーの現在の値を指定します。
- [**page_change**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/scrollbar/page_change)プロパティは、スクロールバー内のスクロールボックスのいずれかの側をクリックした場合に、現在の値が増分変更される量を指定します。

以下の例は、ワークシートにスクロールバーを追加する方法を示しています。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Controls-AddingScrollBarControl-1.py" >}}

## **ワークシートでグループコントロールにグループボックスコントロールを追加する**

特定のグループに所属するラジオボタンやその他のコントロールを実装する必要がある場合は、グループボックスまたは長方形コントロールを含めることによって実装できます。これらの2つのオブジェクトのいずれかがグループのデリミタとして機能します。これらの形を追加した後は、2つ以上のラジオボタンやその他のグループオブジェクトを追加できます。

### **Microsoft Excel の使用**

ワークシートにグループボックスコントロールを配置し、その中にコントロールを配置するには:

- フォームを開始するには、メインメニューで*表示*をクリックし、*ツールバー*と*フォーム*をクリックします。
- *フォーム*ツールバーで、*グループボックス*をクリックし、ワークシート上に長方形を描きます。
- ボックスのキャプション文字列を入力します。
- *フォーム*ツールバーで、*オプションボタン*をクリックし、*グループボックス*内のキャプション文字列の真下をクリックします。
- 再度*フォーム*ツールバーで、*オプションボタン*をクリックし、前のラジオボタンの下に*グループボックス*内をクリックします。
- もう一度*フォーム*ツールバーで、*オプションボタン*をクリックし、前のラジオボタンの下に*グループボックス*内をクリックします。

### **Aspose.Cells for Python via .NETを使用して**

[**ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection)クラスは、ワークシートにグループボックスを追加し、コントロールをグループ化するための[**add_group_box**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_group_box)というメソッドを提供します。このメソッドは[**Aspose.Cells.Drawing.GroupBox**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/groupbox)オブジェクトを返します。また、[**group**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/group)クラスの[**ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection)メソッドは、形をグループ化し、[**Shape**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape)配列をパラメータとして取り、[**GroupShape**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/groupshape)オブジェクトを返します。[**Aspose.Cells.Drawing.GroupBox**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/groupbox)クラスはグループボックスを表します。いくつかの重要なメンバーがあります:

- [**text**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/text)プロパティは、グループボックスのキャプション文字列を指定します。
- [**shadow**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/groupbox/shadow)プロパティは、グループボックスに3Dの影があるかどうかを示します。

以下の例は、ワークシートにグループボックスを追加し、コントロールをグループ化する方法を示しています。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Controls-AddingGroupBoxControl-1.py" >}}

## **高度なトピック**
- [ActiveX コントロールを追加](/cells/ja/python-net/add-activex-controls-using-aspose-cells/)
- [ActiveXコントロールを削除](/cells/ja/python-net/remove-activex-control/)
- [ActiveX ComboBoxコントロールを更新](/cells/ja/python-net/update-activex-combobox-control/)
