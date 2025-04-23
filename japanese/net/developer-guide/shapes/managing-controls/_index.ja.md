---
title: コントロールの管理
type: docs
weight: 150
url: /ja/net/managing-controls/
---

## **紹介**

開発者はテキストボックス、チェックボックス、ラジオボタン、コンボボックス、ラベル、ボタン、ライン、四角形、円弧、楕円、スピンボタン、スクロールバー、グループボックスなどの異なる図形オブジェクトを追加できます。Aspose.Cellsには、すべての図形オブジェクトを含むAspose.Cells.Drawing名前空間が提供されています。ただし、まだサポートされていないいくつかの図形オブジェクトや形状があります。これらの図形オブジェクトはMicrosoft Excelでデザインされたスプレッドシートに作成し、その後Aspose.Cellsに読み込むことができます。Aspose.Cellsは、デザイナースプレッドシートからこれらの図形オブジェクトを読み込み、生成されたファイルに書き込むことができます。

## **ワークシートにテキストボックスコントロールを追加**

レポートで重要な情報を強調する一つの方法は、テキストボックスを使用することです。たとえば、企業名を強調するためにテキストを追加したり、最も売り上げの高い地理的地域を示すために使用したりします。Aspose.Cellsは、新しいテキストボックスをコレクションに追加するために使用される[**TextBoxCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/textboxcollection)クラスを提供しています。別の[**TextBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/textbox)クラスもあり、すべての種類の設定を定義するために使用されるテキストボックスを表しています。いくつか重要なメンバーがあります:

- [**TextFrame**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/textframe)プロパティは、テキストボックスの内容を調整するために使用される[**MsoTextFrame**](https://reference.aspose.com/cells/net/aspose.cells.drawing/msotextframe)オブジェクトを返します。
- [**Placement**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/placement)プロパティは配置タイプを指定します。
- [**Font**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/font)プロパティはフォント属性を指定します。
- [**AddHyperlink**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/methods/addhyperlink)メソッドは、テキストボックスにハイパーリンクを追加します。
- [**FillFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/fillformat)プロパティは、テキストボックスの塗りつぶし形式を設定するために使用される[**MsoFillFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/msofillformat)オブジェクトを返します。
- [**LineFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lineformat)プロパティは、テキストボックスのラインのスタイルと太さを通常設定するために使用される[**MsoLineFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/msolineformat)オブジェクトを返します。
- [**Text**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/text)プロパティは、テキストボックスの入力テキストを指定します。

次の例では、ブックの最初のワークシートに2つのテキストボックスを作成します。最初のテキストボックスはさまざまなフォーマット設定で整備されています。2番目はシンプルなものです。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingTextBoxControl-1.cs" >}}

## **デザイナースプレッドシート内のテキストボックスコントロールの操作**

Aspose.Cellsでは、デザイナースプレッドシート内のテキストボックスにアクセスして操作することもできます。[**Worksheet.TextBoxes**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/textboxes)プロパティを使用して、シート内のテキストボックスのコレクションを取得します。

次の例では、上記の例で作成したMicrosoft Excelファイルを使用しています。2つのテキストボックスのテキストを取得し、2番目のテキストボックスのテキストを変更してファイルを保存します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-ManipulatingTextBoxControls-1.cs" >}}

## **ワークシートにチェックボックスコントロールを追加する**

チェックボックスは、ユーザーが真偽またははい・いいえなどの2つのオプションから選択する方法を提供したい場合に便利です。Aspose.Cellsを使用すると、ワークシートでチェックボックスを使用できます。たとえば、特定の取得を考慮するかどうかを伴う財務予測ワークシートを作成した場合、そのワークシートの上部にチェックボックスを配置したいと思うかもしれません。その後、このチェックボックスの状態を他のセルにリンクすることができます。つまり、チェックボックスが選択されている場合、セルの値はTrueになり、選択されていない場合、セルの値はFalseになります。

### **Microsoft Excel の使用**

ワークシートにチェックボックスコントロールを配置するには、次の手順に従います。

1. フォームツールバーが表示されていることを確認します。
1. フォームツールバーの**チェックボックス**ツールをクリックします。
1. ワークシートエリアで、チェックボックスとチェックボックスの横に表示されるラベルを定義するためにクリックしてドラッグします。
1. チェックボックスが配置されたら、マウスカーソルをラベル領域に移動してラベルを変更します。
1. **セルリンク**フィールドで、このチェックボックスをリンクするセルのアドレスを指定します。
1. **OK** をクリックします。

### **Aspose.Cellsの使用**

Aspose.Cellsには新しいチェックボックスをコレクションに追加するために使用される[**CheckBoxCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/checkboxcollection)クラスが提供されています。重要なメンバーを持つ他のクラス[**Aspose.Cells.Drawing.CheckBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/checkbox)もあります。

- [**LinkedCell**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/linkedcell)プロパティは、チェックボックスにリンクされるセルを指定します。
- [**Text**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/text)プロパティは、チェックボックスに関連付けられたテキスト文字列を指定します。これはチェックボックスのラベルです。
- [**Value**](https://reference.aspose.com/cells/net/aspose.cells.drawing/checkbox/properties/value)プロパティは、チェックボックスが選択されているかどうかを指定します。

次の例では、ワークシートにチェックボックスを追加する方法を示しています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingCheckBoxControl-1.cs" >}}

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

### **Aspose.Cellsの使用**

[**Aspose.Cells.Drawing.ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection)クラスには、ワークシートにラジオボタンコントロールを追加するために使用される[**AddRadioButton**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addradiobutton)というメソッドがあります。このメソッドは[**Aspose.Cells.Drawing.RadioButton**](https://reference.aspose.com/cells/net/aspose.cells.drawing/radiobutton)オブジェクトを返します。また、[**Aspose.Cells.Drawing.RadioButton**](https://reference.aspose.com/cells/net/aspose.cells.drawing/radiobutton)クラスもあります。

- [**LinkedCell**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/linkedcell)プロパティは、ラジオボタンにリンクされるセルを指定します。
- [**Text**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/text)プロパティは、ラジオボタンに関連付けられたテキスト文字列を指定します。これはラジオボタンのラベルです。
- [**IsChecked**](https://reference.aspose.com/cells/net/aspose.cells.drawing/radiobutton/properties/ischecked)プロパティは、ラジオボタンが選択されているかどうかを指定します。
- [**FillFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/fillformat)プロパティは、ラジオボタンの塗りつぶし形式を指定します。
- [**LineFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lineformat)プロパティは、オプションボタンの線の形式スタイルを指定します。

次の例では、ワークシートにラジオボタンを追加する方法を示しています。例では、3つの年齢グループを表すラジオボタンが追加されています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingRadioButtonControl-1.cs" >}}

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

### **Aspose.Cellsの使用**

クラス [**Aspose.Cells.Drawing.ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) は [**AddComboBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addcombobox) という名前のメソッドを提供し、これはワークシートにコンボボックスコントロールを追加するために使用されます。このメソッドは [**Aspose.Cells.Drawing.ComboBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/combobox) オブジェクトを返します。[**Aspose.Cells.Drawing.ComboBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/combobox) クラスはコンボボックスを表します。いくつかの重要なメンバを持っています：

- [**LinkedCell**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/linkedcell) プロパティはコンボボックスにリンクされたセルを指定します。
- [**InputRange**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/inputrange) プロパティはコンボボックスを埋めるために使用されるワークシートのセル範囲を指定します。
- [**DropDownLines**](https://reference.aspose.com/cells/net/aspose.cells.drawing/combobox/properties/dropdownlines) プロパティはドロップダウン部分に表示されるリスト行の数を指定します。
- [**Shadow**](https://reference.aspose.com/cells/net/aspose.cells.drawing/combobox/properties/shadow) プロパティはコンボボックスが 3D シェーディングを持っているかどうかを示します。

次の例は、ワークシートにコンボボックスを追加する方法を示しています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingComboBoxControl-1.cs" >}}

## **ワークシートにラベルコントロールを追加する**

ラベルはスプレッドシートの内容に関するユーザーへの情報提供手段です。Aspose.Cells を使用すると、ワークシートにラベルを追加および操作することができます。クラス [**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) は、ワークシートにラベルコントロールを追加するために使用する [**AddLabel**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addlabel) という名前のメソッドを提供します。このメソッドは [**Label**](https://reference.aspose.com/cells/net/aspose.cells.drawing/label) オブジェクトを返します。[**Label**](https://reference.aspose.com/cells/net/aspose.cells.drawing/label) クラスはワークシート内のラベルを表します。いくつかの重要なメンバを持っています：

- [**Text**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/text) メソッドはラベルのキャプション文字列を指定します。
- [**Placement**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/placement) メソッドは、ラベルがワークシート内のセルにどのようにアタッチされるかを指定します。

次の例は、ワークシートにラベルを追加する方法を示しています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingLabelControl-1.cs" >}}

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

### **Aspose.Cellsの使用**

クラス [**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) は、ワークシートにリストボックスコントロールを追加するために使用される [**AddListBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addlistbox) という名前のメソッドを提供します。このメソッドは [**Aspose.Cells.Drawing.ListBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/listbox) オブジェクトを返します。[**ListBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/listbox) クラスはリストボックスを表します。いくつかの重要なメンバを持っています：

- [**LinkedCell**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/linkedcell) メソッドはリストボックスにリンクされたセルを指定します。
- [**InputRange**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/inputrange) メソッドはリストボックスを埋めるために使用されるワークシートのセル範囲を指定します。
- [**SelectionType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/listbox/properties/selectiontype) メソッドはリストボックスの選択モードを指定します。
- [**Shadow**](https://reference.aspose.com/cells/net/aspose.cells.drawing/listbox/properties/shadow) メソッドはリストボックスに3Dシェーディングがあるかどうかを示します。

次の例は、ワークシートにリストボックスを追加する方法を示しています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingListBoxControl-1.cs" >}}

## **ボタンコントロールをワークシートに追加する**

ボタンは何かアクションを行うために便利です。時には、ボタンにVBAマクロを割り当てたり、Webページを開くためのハイパーリンクを割り当てることも有用です。

### **Microsoft Excel の使用**

ボタンコントロールをワークシートに配置するには:

1. **フォーム** ツールバーが表示されていることを確認します。
1. **ボタン** ツールをクリックします。
1. ワークシート領域でクリックしてドラッグして、ボタンを配置する矩形を定義します。
1. リストボックスがワークシートに配置されたら、コントロールを右クリックして **フォーマットコントロール** を選択し、VBAマクロを指定し、フォント、配置、サイズ、余白などに関連する属性を設定します。
1. **OK** をクリックします。

### **Aspose.Cellsの使用**

 [**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) クラスは、ボタンコントロールをワークシートに追加するための [**AddButton**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addbutton) という名前のメソッドを提供します。このメソッドは [**Aspose.Cells.Drawing.Button**](https://reference.aspose.com/cells/net/aspose.cells.drawing/button) オブジェクトを返します。クラス [**Aspose.Cells.Drawing.Button**](https://reference.aspose.com/cells/net/aspose.cells.drawing/button) はボタンを表します。いくつかの重要なメンバーがあります:

- [**Text**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/text) プロパティはボタンのキャプションを指定します。
- [**Font**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/font) プロパティはボタンコントロールのラベルのフォント属性を指定します。
- [**Placement**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/placement) プロパティはボタンがワークシートのセルにアタッチされる方法を指定します。
- [**AddHyperlink**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/methods/addhyperlink) プロパティはボタンコントロールにハイパーリンクを追加します。ボタンをクリックすると関連するURLに移動します。

次の例は、ワークシートにボタンを追加する方法を示しています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingButtonControl-1.cs" >}}

## **ワークシートにラインコントロールを追加する**

### **Microsoft Excel の使用**

1. **描画** ツールバーで **オートシェイプ** をクリックし、**ライン** を指して、希望のラインスタイルを選択します。
1. ドラッグしてラインを描きます。
1. 次のいずれかを行います。
   1. ラインを開始点から15度の角度で制限するには、ドラッグしながら **SHIFT** キーを押します。
   1. 最初の端点から異なる方向にラインを長くするには、ドラッグしながら **CTRL** キーを押します。

### **Aspose.Cellsの使用**

[**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) クラスは、ワークシートにラインシェイプを追加するために使用される [**AddLine**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addline) という名前のメソッドを提供します。このメソッドは [**LineShape**](https://reference.aspose.com/cells/net/aspose.cells.drawing/lineshape) オブジェクトを返します。クラス [**LineShape**](https://reference.aspose.com/cells/net/aspose.cells.drawing/lineshape) はラインを表します。いくつかの重要なメンバーがあります:

- [**LineFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lineformat) メソッドはラインのフォーマットを指定します。
- [**Placement**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/placement) メソッドはラインがワークシートのセルにアタッチされる方法を指定します。

次の例は、ワークシートにラインを追加する方法を示しています。異なるスタイルで3つのラインが作成されます。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingLineControl-1.cs" >}}

### **ラインに矢印を追加する**

Aspose.Cellsでは、矢印付きの直線を描画することもできます。直線に矢印を追加したり、直線のフォーマットを行ったりすることができます。例えば、直線の色を変更したり、直線の太さやスタイルを指定したりすることができます。

次の例は、ラインに矢印を追加する方法を示しています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddinganArrowHead-1.cs" >}}

## **ワークシートに長方形コントロールを追加する**

Aspose.Cellsを使用すると、ワークシートに長方形の図形を描画できます。長方形や正方形などを作成できます。また、コントロールの塗りつぶしの色や境界線の色を書式設定することができます。たとえば、長方形の色を変更したり、シェーディングの色を設定したり、必要に応じて長方形の太さやスタイルを指定することができます。

### **Microsoft Excel の使用**

1. **描画**ツールバーで、**長方形**をクリックします。
1. 長方形を描画するには、ドラッグします。
1. 次のいずれかを行います。
   1. 長方形を開始点から正方形に描画するには、ドラッグしながらSHIFTキーを押し続けます。
   1. 長方形を中心点から描画するには、ドラッグしながらCTRLキーを押し続けます。

### **Aspose.Cellsの使用**

クラス[**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection)には、ワークシートに長方形を追加するための[**AddRectangle**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addrectangle)という名前のメソッドがあります。このメソッドは[**Aspose.Cells.Drawing.RectangleShape**](https://reference.aspose.com/cells/net/aspose.cells.drawing/rectangleshape)オブジェクトを返します。クラス[**Aspose.Cells.Drawing.RectangleShape**](https://reference.aspose.com/cells/net/aspose.cells.drawing/rectangleshape)は長方形を表します。いくつか重要なメンバーがあります。

- [**LineFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lineformat)プロパティは長方形の線の書式属性を指定します。
- [**Placement**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/placement)プロパティは[**PlacementType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/placementtype)を指定し、長方形がワークシートのセルにアタッチされる方法を示します。
- [**FillFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/fillformat)プロパティは長方形の塗りつぶしの書式スタイルを指定します。

次の例は、ワークシートに長方形を追加する方法を示しています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingRectangleControl-1.cs" >}}

## **ワークシートに円弧コントロールを追加する**

Aspose.Cellsを使用すると、ワークシートに円弧の図形を描画できます。シンプルな円弧や塗りつぶした円弧を作成できます。また、コントロールの塗りつぶしの色や境界線の色を書式設定することができます。たとえば、円弧の色を指定/変更したり、シェーディングの色を設定したり、必要に応じて図形の太さやスタイルを指定することができます。

### **Microsoft Excel の使用**

1. **図形の自動スタイル**で、**円弧**をクリックします。
1. 円弧を描画するには、ドラッグします。

### **Aspose.Cellsの使用**

クラス[**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection)には、ワークシートに円弧形状を追加するための[**AddArc**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addarc)という名前のメソッドがあります。このメソッドは[**Aspose.Cells.Drawing.ArcShape**](https://reference.aspose.com/cells/net/aspose.cells.drawing/arcshape)オブジェクトを返します。クラス[**Aspose.Cells.Drawing.ArcShape**](https://reference.aspose.com/cells/net/aspose.cells.drawing/arcshape)は円弧を表します。いくつか重要なメンバーがあります。

- [**LineFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lineformat)プロパティは円弧形状の線の書式属性を指定します。
- [**Placement**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/placement)プロパティは[**PlacementType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/placementtype)を指定し、円弧がワークシートのセルにアタッチされる方法を示します。
- [**FillFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/fillformat)プロパティは形状の塗りつぶし形式スタイルを指定します。
- [**LowerRightRow**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lowerrightrow)プロパティは右下の行インデックスを指定します。
- [**LowerRightColumn**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lowerrightcolumn)プロパティは右下の列インデックスを指定します。

次の例は、ワークシートに円弧形状を追加する方法を示しています。この例では、塗りつぶしの円弧形状とシンプルな円弧形状の2つを作成します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingArcControl-1.cs" >}}

## **ワークシートに楕円コントロールを追加する**

Aspose.Cellsを使用すると、ワークシートに楕円の図形を描画できます。単純な楕円や塗りつぶした楕円形状を作成し、コントロールの塗りつぶしの色や境界線の色を書式設定できます。たとえば、楕円の色を指定/変更したり、シェーディングの色を設定したり、必要に応じて図形の太さやスタイルを指定することができます。

### **Microsoft Excel の使用**

- *図形*ツールバーで、*楕円*をクリックします。
- 楕円を描画するには、ドラッグします。
- 以下のいずれか、または両方を行います。
- 楕円を開始点から円として描画するには、ドラッグしながらSHIFTキーを押し続けます。
- 楕円を中心点から描画するには、ドラッグしながらCTRLキーを押し続けます。

### **Aspose.Cellsの使用**

クラス[**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection)は、ワークシートに楕円形を追加するために使用される[**AddOval**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addoval)というメソッドを提供します。このメソッドは[**Aspose.Cells.Drawing.Oval**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oval)オブジェクトを返します。クラス[**Aspose.Cells.Drawing.Oval**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oval)は楕円形を表し、いくつかの重要なメンバーがあります。

- [**LineFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lineformat)プロパティは楕円形の線形式属性を指定します。
- [**Placement**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/placement)プロパティはワークシート内のセルに楕円形を接続する方法を指定します。
- [**FillFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/fillformat)プロパティは形状の塗りつぶし形式スタイルを指定します。
- [**LowerRightRow**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lowerrightrow)プロパティは右下の行インデックスを指定します。
- [**LowerRightColumn**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lowerrightcolumn)プロパティは右下の列インデックスを指定します。

次の例は、ワークシートに楕円形を追加する方法を示しています。この例では、塗りつぶしの楕円形と単純な円形の2つの楕円形を作成します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingOvalControl-1.cs" >}}

## **ワークシートにスピンボックスコントロールを追加**

スピンボックスは、ボタン（スピンボタンと呼ばれる）に取り付けられたテキストボックスで、テキストボックスの値を逐次的に変更するためにクリックする上向き矢印と下向き矢印で構成されます。スピンボックスを使用することで、財務モデルの入力がモデルの出力にどのように影響するかを確認できます。スピンボタンを特定の入力セルに取り付けることができます。スピンボタンの上向き矢印または下向き矢印をクリックすると、対象の入力セル内の整数値が増減します。*Aspose.Cells*を使用すると、ワークシートにスピンボックスを作成できます。

### **Microsoft Excel の使用**

ワークシートにスピンボックスコントロールを配置するには:

- *フォーム*ツールバーが表示されていることを確認します。
- *スピンボックス*ツールをクリックします。
- ワークシート領域で、スピンボックスを保持する矩形を定義するためにクリックしてドラッグします。
- スピンボックスをワークシートに配置したら、コントロールを右クリックして *フォーマットコントロール* をクリックし、最大値、最小値、増分値を指定します。
- *セルリンク* フィールドに、このスピンボックスをリンクするセルのアドレスを指定します。
- *OK* をクリックします。

### **Aspose.Cellsの使用**

クラス[**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection)は、ワークシートにスピンボックスコントロールを追加するために使用される[**AddSpinner**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addspinner)というメソッドを提供します。このメソッドは[**Aspose.Cells.Drawing.Spinner**](https://reference.aspose.com/cells/net/aspose.cells.drawing/spinner)オブジェクトを返します。クラス[**Aspose.Cells.Drawing.Spinner**](https://reference.aspose.com/cells/net/aspose.cells.drawing/spinner)はスピンボックスを表し、いくつかの重要なメンバーがあります。

- [**LinkedCell**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/linkedcell)プロパティは、スピンボックスにリンクされたセルを指定します。
- [**Max**](https://reference.aspose.com/cells/net/aspose.cells.drawing/spinner/properties/max)プロパティは、スピンボックス範囲の最大値を指定します。
- [**Min**](https://reference.aspose.com/cells/net/aspose.cells.drawing/spinner/properties/min)プロパティは、スピンボックス範囲の最小値を指定します。
- [**IncrementalChange**](https://reference.aspose.com/cells/net/aspose.cells.drawing/spinner/properties/incrementalchange)プロパティは、スピンボックスが1行スクロールされる値の量を指定します。
- [**Shadow**](https://reference.aspose.com/cells/net/aspose.cells.drawing/spinner/properties/shadow)プロパティは、スピンボックスに3Dシェーディングがあるかどうかを示します。
- [**CurrentValue**](https://reference.aspose.com/cells/net/aspose.cells.drawing/spinner/properties/currentvalue)プロパティは、スピンボックスの現在の値を指定します。

次の例は、ワークシートにスピンボックスを追加する方法を示しています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingSpinnerControl-1.cs" >}}

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

### **Aspose.Cellsの使用**

[**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection)クラスは、ワークシートにスクロールバーコントロールを追加するために使用される[**AddScrollBar**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addscrollbar)というメソッドを提供します。このメソッドは[**Aspose.Cells.Drawing.ScrollBar**](https://reference.aspose.com/cells/net/aspose.cells.drawing/scrollbar)オブジェクトを返します。[**Aspose.Cells.Drawing.ScrollBar**](https://reference.aspose.com/cells/net/aspose.cells.drawing/scrollbar)クラスはスクロールバーを表します。いくつかの重要なメンバーがあります:

- [**LinkedCell**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/linkedcell)プロパティは、スクロールバーにリンクされたセルを指定します。
- [**Max**](https://reference.aspose.com/cells/net/aspose.cells.drawing/scrollbar/properties/max)プロパティは、スクロールバー範囲の最大値を指定します。
- [**Min**](https://reference.aspose.com/cells/net/aspose.cells.drawing/scrollbar/properties/min)プロパティは、スクロールバー範囲の最小値を指定します。
- [**IncrementalChange**](https://reference.aspose.com/cells/net/aspose.cells.drawing/scrollbar/properties/incrementalchange)プロパティは、スクロールバーが1行スクロールされたときの値の量を指定します。
- [**Shadow**](https://reference.aspose.com/cells/net/aspose.cells.drawing/scrollbar/properties/shadow)プロパティは、スクロールバーに3Dの影があるかどうかを示します。
- [**CurrentValue**](https://reference.aspose.com/cells/net/aspose.cells.drawing/scrollbar/properties/currentvalue)プロパティは、スクロールバーの現在の値を指定します。
- [**PageChange**](https://reference.aspose.com/cells/net/aspose.cells.drawing/scrollbar/properties/pagechange)プロパティは、スクロールバー内のスクロールボックスのいずれかの側をクリックした場合に、現在の値が増分変更される量を指定します。

以下の例は、ワークシートにスクロールバーを追加する方法を示しています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingScrollBarControl-1.cs" >}}

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

### **Aspose.Cellsの使用**

[**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection)クラスは、ワークシートにグループボックスを追加し、コントロールをグループ化するための[**AddGroupBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addgroupbox)というメソッドを提供します。このメソッドは[**Aspose.Cells.Drawing.GroupBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/groupbox)オブジェクトを返します。また、[**Group**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/group)クラスの[**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection)メソッドは、形をグループ化し、[**Shape**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape)配列をパラメータとして取り、[**GroupShape**](https://reference.aspose.com/cells/net/aspose.cells.drawing/groupshape)オブジェクトを返します。[**Aspose.Cells.Drawing.GroupBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/groupbox)クラスはグループボックスを表します。いくつかの重要なメンバーがあります:

- [**Text**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/text)プロパティは、グループボックスのキャプション文字列を指定します。
- [**Shadow**](https://reference.aspose.com/cells/net/aspose.cells.drawing/groupbox/properties/shadow)プロパティは、グループボックスに3Dの影があるかどうかを示します。

以下の例は、ワークシートにグループボックスを追加し、コントロールをグループ化する方法を示しています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingGroupBoxControl-1.cs" >}}

## **高度なトピック**
- [Aspose.Cells を使用して ActiveX コントロールを追加する](/cells/ja/net/add-activex-controls-using-aspose-cells/)
- [ActiveXコントロールを削除](/cells/ja/net/remove-activex-control/)
- [ActiveX ComboBoxコントロールを更新](/cells/ja/net/update-activex-combobox-control/)
{{< app/cells/assistant language="csharp" >}}
