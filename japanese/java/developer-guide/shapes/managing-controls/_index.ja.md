---
title: コントロールの管理
type: docs
weight: 120
url: /ja/java/managing-controls/
---

## **紹介**

開発者はテキストボックス、チェックボックス、ラジオボタン、コンボボックス、ラベル、ボタン、ライン、四角形、円弧、楕円、スピンボタン、スクロールバー、グループボックスなどの異なる図形オブジェクトを追加できます。Aspose.Cellsには、すべての図形オブジェクトを含むAspose.Cells.Drawing名前空間が提供されています。ただし、まだサポートされていないいくつかの図形オブジェクトや形状があります。これらの図形オブジェクトはMicrosoft Excelでデザインされたスプレッドシートに作成し、その後Aspose.Cellsに読み込むことができます。Aspose.Cellsは、デザイナースプレッドシートからこれらの図形オブジェクトを読み込み、生成されたファイルに書き込むことができます。

## **ワークシートにテキストボックスコントロールを追加する**

報告書で重要な情報を強調する1つの方法は、テキストボックスを使用することです。たとえば、企業名を強調するためのテキストを追加したり、売上高が最も高い地域を示すためにテキストを追加することができます。Aspose.Cells にはテキストボックスコントロールを追加するための TextBoxes クラスが用意されています。また、その他の設定を定義するために使用するテキストボックスを表すクラス [**TextBox**](https://reference.aspose.com/cells/java/com.aspose.cells/textbox) もあります。いくつか重要なメンバーを持っています:

- [**getTextFrame**](https://reference.aspose.com/cells/java/com.aspose.cells/textbox#TextFrame) メソッドは [**MsoTextFrame**](https://reference.aspose.com/cells/java/com.aspose.cells/MsoTextFrame) オブジェクトを返し、テキストボックスの内容を調整するのに使用されます。
- [**setPlacement**](https://reference.aspose.com/cells/java/com.aspose.cells/textbox#Placement) メソッドは配置のタイプを指定します。
- [**setFont**](https://reference.aspose.com/cells/java/com.aspose.cells/textbox#Font) メソッドはフォント属性を指定します。
- [**addHyperlink**](https://reference.aspose.com/cells/java/com.aspose.cells/textbox#addHyperlink(java.lang.String))メソッドは、テキストボックスにハイパーリンクを追加します。
- [**FillFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/textbox#FillFormat) プロパティはテキストボックスの塗りつぶし形式を設定するために使用する [**MsoFillFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/MsoFillFormat) オブジェクトを返します。
- [**LineFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/textbox#LineFormat)プロパティは、テキストボックスのラインのスタイルと太さを通常設定するために使用される[**MsoLineFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/MsoLineFormat)オブジェクトを返します。
- [**setText**](https://reference.aspose.com/cells/java/com.aspose.cells/textbox#Text) メソッドはテキストボックスの入力テキストを指定します。

次の例では、ブックの最初のワークシートに2つのテキストボックスを作成します。最初のテキストボックスはさまざまなフォーマット設定で整備されています。2番目はシンプルなものです。

上記のコードを実行した結果は次のとおりです:

**ワークシートに2つのテキストボックスが作成されます** 

![todo:image_alt_text](managing-controls_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingTextBoxControl-1.java" >}}

## **デザイナースプレッドシート内のテキストボックスコントロールを操作する**

Aspose.Cellsでは、デザイナースプレッドシート内のテキストボックスにアクセスして操作することもできます。[**Worksheet.getTextBoxes**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#TextBoxes)プロパティを使用して、シート内のテキストボックスのコレクションを取得します。

以下の例は、上記の例で作成した Microsoft Excel ファイル - tsttextboxes.xls - を使用します。2つのテキストボックスのテキスト文字列を取得し、2番目のテキストボックスのテキストを変更してファイルを保存します。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-ManipulatingTextBoxControls-1.java" >}}

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

Aspose.Cellsには新しいチェックボックスをコレクションに追加するために使用される[**CheckBoxCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/checkboxcollection)クラスが提供されています。重要なメンバーを持つ他のクラス[**Aspose.Cells.Drawing.CheckBox**](https://reference.aspose.com/cells/java/com.aspose.cells/CheckBox)もあります。

- [**setLinkedCell**](https://reference.aspose.com/cells/java/com.aspose.cells/checkbox#LinkedCell)メソッドは、チェックボックスにリンクされたセルを指定します。
- [**setText**](https://reference.aspose.com/cells/java/com.aspose.cells/checkbox#Text)メソッドは、チェックボックスに関連付けられるテキスト文字列を指定します。これはチェックボックスのラベルです。
- [**setValue**](https://reference.aspose.com/cells/java/com.aspose.cells/checkbox#Value)メソッドは、チェックボックスがチェックされているかどうかを指定します。

以下の例は、ワークシートにチェックボックスを追加する方法を示しています。以下の出力は、コードの実行後に生成されます。

**ワークシートにCheckBoxが追加されました** 

![todo:image_alt_text](managing-controls_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingCheckBoxControl-1.java" >}}

## **ワークシートにRadioButtonコントロールを追加する**

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

[**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection)クラスは、ワークシートにラジオボタンコントロールを追加するために使用できるaddShapeというメソッドを提供します。このメソッドはRadioButtonオブジェクトを返すことがあります。RadioButtonクラスは、オプションボタンを表します。いくつかの重要なメンバーがあります:

- setLinkedCellメソッドは、ラジオボタンにリンクされたセルを指定します。
- setTextメソッドは、ラジオボタンに関連するテキスト文字列を指定します。これはラジオボタンのラベルです。
- Checkedプロパティは、ラジオボタンがチェックされているかどうかを指定します。
- setFillFormatメソッドは、ラジオボタンの塗りつぶし形式を指定します。
- setLineFormatメソッドは、オプションボタンのライン形式スタイルを指定します。

以下の例は、ワークシートにラジオボタンを追加する方法を示しています。この例では、年齢層を表す3つのラジオボタンが追加されます。下記の出力は、コードの実行後に生成されます。

**ワークシートにいくつかのラジオボタンが追加されました** 

![todo:image_alt_text](managing-controls_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingRadioButtonControl-1.java" >}}

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

[**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection) クラスは、ワークシートにコンボボックスコントロールを追加するための addShape メソッドを提供します。メソッドは ComboBox オブジェクトを返すことができます。ComboBox クラスはコンボボックスを表します。いくつかの重要なメンバーがあります:

- setLinkedCell メソッドは、コンボボックスにリンクされるセルを指定します。
- setInputRange メソッドは、コンボボックスを埋めるために使用されるワークシート範囲のセルを指定します。
- setDropDownLines メソッドは、コンボボックスのドロップダウン部分に表示されるリスト行の数を指定します。
- setShadow メソッドは、コンボボックスに 3D シェーディングがあるかどうかを示します。

次の例は、ワークシートにコンボボックスを追加する方法を示しています。コードを実行すると、次の出力が生成されます。

**ワークシートにコンボボックスが追加されています** 

![todo:image_alt_text](managing-controls_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingComboBoxControl-1.java" >}}

## **ワークシートにラベルコントロールを追加する**

ラベルは、スプレッドシートの内容に関するユーザーに情報を提供する手段です。Aspose.Cells では、ワークシートにラベルを追加および操作することができます。[**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection) クラスは、ワークシートにラベルコントロールを追加するための addShape というメソッドを提供します。メソッドは Label オブジェクトを返します。Label クラスは、ワークシート内のラベルを表します。いくつかの重要なメンバーがあります:

- setText メソッドは、ラベルのキャプション文字列を指定します。
- setPlacement メソッドは、ラベルがワークシートのセルに取り付けられる方法である PlacementType を指定します。

次の例は、ワークシートにラベルを追加する方法を示しています。コードを実行すると、次の出力が生成されます。

**ワークシートにラベルが追加されています**

![todo:image_alt_text](managing-controls_5.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingLabelControl-1.java" >}}

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

[**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection) クラスは、ワークシートにリストボックスコントロールを追加するための addShape というメソッドを提供します。メソッドは ListBox オブジェクトを返します。ListBox クラスはリストボックスを表します。いくつかの重要なメンバーがあります:

- setLinkedCell メソッドは、リストボックスにリンクされるセルを指定します。
- setInputRangeメソッドは、リストボックスを埋めるために使用されるワークシート範囲を指定します。
- setSelectionTypeメソッドは、リストボックスの選択モードを指定します。
- setShadowメソッドは、リストボックスに3Dの影があるかどうかを示します。

次の例では、ワークシートにリストボックスを追加する方法を示しています。コードを実行すると、次の出力が生成されます。

ワークシートにリストボックスが追加されます 

![todo:image_alt_text](managing-controls_6.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingListBoxControl-1.java" >}}

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

[**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection) クラスには、ボタンコントロールをワークシートに追加するためのaddShapeというメソッドが用意されています。このメソッドは、ボタンオブジェクトを返すことがあります。Buttonクラスはボタンを表します。いくつか重要なメンバがあります:

- setTextメソッドはボタンのキャプションを指定します。
- setPlacementメソッドは、ボタンがワークシートのセルに接続される方法を指定します。
- addHyperlinkメソッドは、ボタンコントロールにハイパーリンクを追加します。ボタンをクリックすると、関連する URL に移動します。

次の例では、ワークシートにボタンを追加する方法を示しています。コードを実行すると、次の出力が生成されます

ワークシートにボタンが追加されます

![todo:image_alt_text](managing-controls_7.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingButtonControl-1.java" >}}

## **ワークシートにラインコントロールを追加する**

Aspose.Cellsを使用すると、ワークシートに自動形状を描画することができます。線を簡単に作成できます。また、線の書式を指定することもできます。例えば、線の色を変更したり、線の太さやスタイルを指定することができます。

### **Microsoft Excel の使用**

1. **描画** ツールバーで **オートシェイプ** をクリックし、**ライン** を指して、希望のラインスタイルを選択します。
1. ドラッグしてラインを描きます。
1. 次のいずれかを行います。
   1. ラインを開始点から15度の角度で制限するには、ドラッグしながら **SHIFT** キーを押します。
   1. 最初の端点から異なる方向にラインを長くするには、ドラッグしながら **CTRL** キーを押します。

### **Aspose.Cellsの使用**

[**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection) クラスには、ワークシートにライン形状を追加するために使用されるaddShapeというメソッドが用意されています。このメソッドは、LineShapeオブジェクトを返すことがあります。LineShapeクラスはラインを表します。いくつか重要なメンバがあります:

- setDashStyleメソッドは、ラインの形式を指定します。
- setPlacementメソッドは、ラインがワークシートのセルに接続される方法を指定します。

次の例では、ワークシートにラインを追加する方法を示しています。異なるスタイルの3本のラインを作成します。コードを実行すると、次の出力が生成されます。

**ワークシートに数行が追加されます** 

![todo:image_alt_text](managing-controls_8.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingLineControl-1.java" >}}

### **直線に矢印を追加**

Aspose.Cellsでは、矢印付きの直線を描画することもできます。直線に矢印を追加したり、直線のフォーマットを行ったりすることができます。例えば、直線の色を変更したり、直線の太さやスタイルを指定したりすることができます。

次の例では、直線に矢印を追加する方法が示されています。コードを実行すると、次の出力が生成されます。

**ワークシートに矢印付きの直線が追加されます** 

![todo:image_alt_text](managing-controls_9.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddinganArrowHead.java" >}}

## **ワークシートに長方形コントロールを追加する**

Aspose.Cellsを使用すると、ワークシートに長方形の図形を描画できます。長方形や正方形などを作成できます。また、コントロールの塗りつぶしの色や境界線の色を書式設定することができます。たとえば、長方形の色を変更したり、シェーディングの色を設定したり、必要に応じて長方形の太さやスタイルを指定することができます。

### **Microsoft Excel の使用**

1. **描画**ツールバーで、**長方形**をクリックします。
1. 長方形を描画するには、ドラッグします。
1. 次のいずれかを行います。
   1. 長方形を開始点から正方形に描画するには、ドラッグしながらSHIFTキーを押し続けます。
   1. 長方形を中心点から描画するには、ドラッグしながらCTRLキーを押し続けます。

### **Aspose.Cellsの使用**

[**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection)クラスは、長方形形状をワークシートに追加するために使用されるaddShapeというメソッドを提供します。このメソッドはRectangleShapeオブジェクトを返すことができます。RectangleShapeクラスは長方形を表します。重要なメンバーを持っており、次のようなものがあります。

- setLineFormatメソッドは、長方形の線のフォーマット属性を指定します。
- setPlacementメソッドは、長方形がワークシートのセルにどのようにアタッチされるかを指定するPlacementTypeを指定します。
- FillFormatプロパティは、長方形の塗りつぶしのフォーマットスタイルを指定します。

次の例では、ワークシートに長方形を追加する方法が示されています。コードを実行すると、次の出力が生成されます。

**ワークシートに長方形が追加されます** 

![todo:image_alt_text](managing-controls_10.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingRectangleControl-1.java" >}}

## **ワークシートに円弧コントロールを追加する**

Aspose.Cellsを使用すると、ワークシートに円弧の図形を描画できます。シンプルな円弧や塗りつぶした円弧を作成できます。また、コントロールの塗りつぶしの色や境界線の色を書式設定することができます。たとえば、円弧の色を指定/変更したり、シェーディングの色を設定したり、必要に応じて図形の太さやスタイルを指定することができます。

### **Microsoft Excel の使用**

1. **図形の自動スタイル**で、**円弧**をクリックします。
1. 円弧を描画するには、ドラッグします。

### **Aspose.Cellsの使用**

[**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection)クラスは、ワークシートに円弧形状を追加するために使用されるaddShapeというメソッドを提供します。このメソッドはArcShapeオブジェクトを返すことができます。ArcShapeクラスは円弧を表します。重要なメンバーを持っており、次のようなものがあります。

- setLineFormatメソッドは、円弧形状の線のフォーマット属性を指定します。
- setPlacementメソッドは、円弧がワークシートのセルにどのようにアタッチされるかを指定するPlacementTypeを指定します。
- FillFormat プロパティは、形状の塗りつぶし形式スタイルを指定します。

次の例では、ワークシートに円弧形状を追加する方法が示されています。例では、塗りつぶされた円弧と単純な円弧の2つを作成します。コードを実行すると、次の出力が生成されます。

**ワークシートに2つの円弧形状が追加されます** 

![todo:image_alt_text](managing-controls_11.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingArcControl-1.java" >}}

## **ワークシートに楕円コントロールを追加する**

Aspose.Cellsを使用すると、ワークシートに楕円の図形を描画できます。単純な楕円や塗りつぶした楕円形状を作成し、コントロールの塗りつぶしの色や境界線の色を書式設定できます。たとえば、楕円の色を指定/変更したり、シェーディングの色を設定したり、必要に応じて図形の太さやスタイルを指定することができます。

### **Microsoft Excel の使用**

1. **描画** ツールバーで **楕円** をクリックします。
1. 楕円を描画するにはドラッグします。
1. 次のいずれかを行います。
   1. 楕円を開始点から円に制約するには、ドラッグしながら SHIFT キーを押します。
   1. 中心点から楕円を描くには、ドラッグしながら CTRL キーを押します。

### **Aspose.Cellsの使用**

[**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection) クラスは、ワークシートに楕円形を追加するために使用される addShape というメソッドを提供しています。このメソッドは、Oval オブジェクトを返す可能性があります。Oval クラスは楕円形を表します。いくつか重要なメンバーがあります。

- setLineFormat メソッドは、楕円形のライン形式の属性を指定します。
- setPlacement メソッドは、楕円形がワークシートの中のセルにアタッチされる方法である **PlacementType** を指定します。
- FillFormat プロパティは、形状の塗りつぶし形式スタイルを指定します。

次の例は、ワークシートに楕円形を追加する方法を示しています。この例では、塗りつぶしのある楕円形と単純な円形の2つの楕円形が作成されます。 コードを実行すると、次の出力が生成されます。

**ワークシートに2つの楕円形が追加されました** 

![todo:image_alt_text](managing-controls_12.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddinganOvalControl-1.java" >}}

## **高度なトピック**
- [Aspose.Cells を使用して ActiveX コントロールを追加する](/cells/ja/java/add-activex-controls-using-aspose-cells/)
- [ActiveXコントロールを削除](/cells/ja/java/remove-activex-control/)
