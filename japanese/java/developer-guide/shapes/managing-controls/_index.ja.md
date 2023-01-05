---
title: コントロールの管理
type: docs
weight: 120
url: /ja/java/managing-controls/
---
## **序章**

開発者は、テキスト ボックス、チェック ボックス、ラジオ ボタン、コンボ ボックス、ラベル、ボタン、線、長方形、弧、楕円、スピナー、スクロール バー、グループ ボックスなど、さまざまな描画オブジェクトを追加できます。すべての描画オブジェクト。ただし、まだサポートされていない描画オブジェクトまたは図形がいくつかあります。 Microsoft Excel を使用してデザイナー スプレッドシートでこれらの描画オブジェクトを作成し、デザイナー スプレッドシートを Aspose.Cells にインポートします。

## **TextBox コントロールをワークシートに追加する**

レポートで重要な情報を強調する 1 つの方法は、テキスト ボックスを使用することです。たとえば、テキストを追加して、会社名を強調したり、売上高が最も多い地域を示したりします。Aspose.Cells は、コレクションに新しいテキスト ボックスを追加するために使用される TextBoxes クラスを提供します。別のクラスがあり、[**テキストボックス**](https://reference.aspose.com/cells/java/com.aspose.cells/textbox)、すべてのタイプの設定を定義するために使用されるテキスト ボックスを表します。いくつかの重要なメンバーがあります。

- の[**getTextFrame**](https://reference.aspose.com/cells/java/com.aspose.cells/textbox#TextFrame)メソッドは[**MsoTextFrame**](https://reference.aspose.com/cells/java/com.aspose.cells/MsoTextFrame)テキスト ボックスの内容を調整するために使用されるオブジェクト。
- の[**setPlacement**](https://reference.aspose.com/cells/java/com.aspose.cells/textbox#Placement) method は配置タイプを指定します。
- の[**setFont**](https://reference.aspose.com/cells/java/com.aspose.cells/textbox#Font)メソッドは、フォント属性を指定します。
- の[**addハイパーリンク**](https://reference.aspose.com/cells/java/com.aspose.cells/textbox#addHyperlink(java.lang.String)メソッドは、テキスト ボックスのハイパーリンクを追加します。
- の[**FillFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/textbox#FillFormat)プロパティリターン[**MsoFillFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/MsoFillFormat)テキスト ボックスの塗りつぶし形式を設定するために使用されるオブジェクト。
- の[**LineFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/textbox#LineFormat)プロパティは[**MsoLineFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/MsoLineFormat)通常、テキスト ボックスの行のスタイルと太さに使用されるオブジェクト。
- の[**セットテキスト**](https://reference.aspose.com/cells/java/com.aspose.cells/textbox#Text)メソッドは、テキスト ボックスの入力テキストを指定します。

次の例では、ブックの最初のワークシートに 2 つのテキスト ボックスを作成します。最初のテキスト ボックスには、さまざまな書式設定が用意されています。 2 つ目は単純なものです。

コードを実行すると、次の出力が生成されます。

**ワークシートに 2 つのテキスト ボックスが作成されます** 

![todo:画像_代替_文章](managing-controls_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingTextBoxControl-1.java" >}}

## **Designer スプレッドシートでのテキスト ボックス コントロールの操作**

Aspose.Cells では、デザイナー ワークシートのテキスト ボックスにアクセスして操作することもできます。使用[**Worksheet.getTextBoxes**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#TextBoxes)シート内の textboxes コレクションを取得するプロパティ。

次の例では、上記の例で作成した Microsoft Excel ファイル (tsttextboxes.xls) を使用しています。 2 つのテキスト ボックスのテキスト文字列を取得し、2 番目のテキスト ボックスのテキストを変更してファイルを保存します。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-ManipulatingTextBoxControls-1.java" >}}

## **CheckBox コントロールをワークシートに追加する**

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

Aspose.Cells は[**CheckBoxコレクション**](https://reference.aspose.com/cells/java/com.aspose.cells/checkboxcollection)このクラスは、コレクションに新しいチェック ボックスを追加するために使用されます。別のクラスがあり、[**Aspose.Cells.Drawing.CheckBox**](https://reference.aspose.com/cells/java/com.aspose.cells/CheckBox)、チェック ボックスを表します。いくつかの重要なメンバーがあります。

- の[**setLinkedCell**](https://reference.aspose.com/cells/java/com.aspose.cells/checkbox#LinkedCell)メソッドは、チェック ボックスにリンクされているセルを指定します。
- の[**セットテキスト**](https://reference.aspose.com/cells/java/com.aspose.cells/checkbox#Text)メソッドは、チェック ボックスに関連付けられたテキスト文字列を指定します。チェックボックスのラベルです。
- の[**setValue**](https://reference.aspose.com/cells/java/com.aspose.cells/checkbox#Value)メソッドは、チェック ボックスをオンにするかどうかを指定します。

次の例は、ワークシートにチェックボックスを追加する方法を示しています。以下の出力は、コードの実行後に生成されます。

**ワークシートに CheckBox が追加されます** 

![todo:画像_代替_文章](managing-controls_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingCheckBoxControl-1.java" >}}

## **RadioButton コントロールをワークシートに追加する**

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

の[**シェイプコレクション**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection)クラスは、ワークシートにラジオ ボタン コントロールを追加するために使用できる addShape という名前のメソッドを提供します。このメソッドは、RadioButton オブジェクトを返す場合があります。クラス RadioButton は、オプション ボタンを表します。いくつかの重要なメンバーがあります。

- setLinkedCell メソッドは、ラジオ ボタンにリンクされるセルを指定します。
- setText メソッドは、ラジオ ボタンに関連付けられたテキスト文字列を指定します。ラジオボタンのラベルです。
- Checked プロパティは、ラジオ ボタンがチェックされているかどうかを指定します。
- setFillFormat メソッドは、ラジオ ボタンの塗りつぶし形式を指定します。
- setLineFormat メソッドは、オプション ボタンの線の書式スタイルを指定します。

次の例は、ラジオ ボタンをワークシートに追加する方法を示しています。この例では、年齢層を表す 3 つのラジオ ボタンを追加します。コードを実行すると、次の出力が生成されます。

**ワークシートにいくつかの RadioButtons が追加されます** 

![todo:画像_代替_文章](managing-controls_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingRadioButtonControl-1.java" >}}

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

の[**シェイプコレクション**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection)クラスには、ワークシートにコンボ ボックス コントロールを追加するために使用できる addShape という名前のメソッドが用意されています。このメソッドは ComboBox オブジェクトを返すことができます。クラス ComboBox は、コンボ ボックスを表します。いくつかの重要なメンバーがあります。

- setLinkedCell メソッドは、コンボ ボックスにリンクされるセルを指定します。
- setInputRange メソッドは、コンボ ボックスを埋めるために使用されるセルのワークシート範囲を指定します。
- setDropDownLines メソッドは、コンボ ボックスのドロップダウン部分に表示されるリストの行数を指定します。
- setShadow メソッドは、コンボ ボックスに 3D シェーディングがあるかどうかを示します。

次の例は、ワークシートにコンボ ボックスを追加する方法を示しています。コードを実行すると、次の出力が生成されます。

**ワークシートにコンボボックスが追加されました** 

![todo:画像_代替_文章](managing-controls_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingComboBoxControl-1.java" >}}

## **ワークシートへのラベル コントロールの追加**

ラベルは、スプレッドシートの内容に関する情報をユーザーに提供する手段です。 Aspose.Cells を使用すると、ワークシートでラベルを追加および操作できます。の[**シェイプコレクション**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection)クラスは、ワークシートにラベル コントロールを追加するために使用される addShape という名前のメソッドを提供します。このメソッドは Label オブジェクトを返します。クラス Label は、ワークシートのラベルを表します。いくつかの重要なメンバーがあります。

- setText メソッドは、ラベルのキャプション文字列を指定します。
- setPlacement メソッドは、ワークシートのセルにラベルを付ける方法である PlacementType を指定します。

次の例は、ワークシートにラベルを追加する方法を示しています。コードを実行すると、次の出力が生成されます。

**ワークシートにラベルが追加されます**

![todo:画像_代替_文章](managing-controls_5.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingLabelControl-1.java" >}}

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

の[**シェイプコレクション**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection)クラスには、ワークシートにリスト ボックス コントロールを追加するために使用される addShape という名前のメソッドが用意されています。メソッドは ListBox オブジェクトを返します。クラス ListBox は、リスト ボックスを表します。いくつかの重要なメンバーがあります。

- setLinkedCell メソッドは、リスト ボックスにリンクされているセルを指定します。
- setInputRange メソッドは、リスト ボックスを埋めるために使用されるセルのワークシート範囲を指定します。
- setSelectionType メソッドは、リスト ボックスの選択モードを指定します。
- setShadow メソッドは、リスト ボックスに 3D シェーディングがあるかどうかを示します。

次の例は、ワークシートにリスト ボックスを追加する方法を示しています。コードを実行すると、次の出力が生成されます。

**ワークシートにリスト ボックスが追加されます** 

![todo:画像_代替_文章](managing-controls_6.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingListBoxControl-1.java" >}}

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

の[**シェイプコレクション**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection)クラスは、ワークシートにボタン コントロールを追加するために使用される addShape という名前のメソッドを提供します。このメソッドは、Button オブジェクトを返す場合があります。クラス Button はボタンを表します。いくつかの重要なメンバーがあります。

- setText メソッドは、ボタンのキャプションを指定します。
- setPlacement メソッドは、ボタンがワークシートのセルに接続される方法である PlacementType を指定します。
- addHyperlink メソッドは、ボタン コントロールのハイパーリンクを追加します。ボタンをクリックすると、関連する URL に移動します。

次の例は、ワークシートにボタンを追加する方法を示しています。コードを実行すると、次の出力が生成されます

**ワークシートにボタンが追加されます**

![todo:画像_代替_文章](managing-controls_7.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingButtonControl-1.java" >}}

## **ワークシートへの行コントロールの追加**

Aspose.Cells を使用すると、ワークシートにオートシェイプを描画できます。簡単にラインを作ることができます。行をフォーマットすることもできます。たとえば、線の色を変更したり、必要に応じて線の太さとスタイルを指定したりできます。

### **Microsoft エクセルを使う**

1. 上で**描く**ツールバー、クリック**オートシェイプ**、 指し示す**ライン**をクリックして、必要な線のスタイルを選択します。
1. ドラッグして線を引きます。
1. 次のいずれかまたは両方を実行します。
 1. 開始点から 15 度の角度で描画するように線を制限するには、Shift キーを押しながらドラッグします。
 1. 最初の終点から反対方向に線を伸ばすには、CTRL キーを押しながらドラッグします。

### **Aspose.Cells を使用**

の[**シェイプコレクション**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection)クラスには、ワークシートに線の形状を追加するために使用される addShape という名前のメソッドが用意されています。このメソッドは、LineShape オブジェクトを返す場合があります。クラス LineShape は線を表します。いくつかの重要なメンバーがあります。

- setDashStyle メソッドは、線の形式を指定します。
- setPlacement メソッドは、ワークシート内のセルに線を接続する方法である PlacementType を指定します。

次の例は、ワークシートに行を追加する方法を示しています。スタイルの異なる 3 つのラインを作成します。コードを実行すると、次の出力が生成されます

**ワークシートにいくつかの行が追加されます** 

![todo:画像_代替_文章](managing-controls_8.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingLineControl-1.java" >}}

### **線に矢印を追加する**

Aspose.Cells では、矢印の線を描くこともできます。線に矢印を追加し、線をフォーマットすることができます。たとえば、線の色を変更したり、線の太さとスタイルを指定したりできます。

次の例は、線に矢印を追加する方法を示しています。コードを実行すると、次の出力が生成されます。

**ワークシートに矢印付きの線が追加されます** 

![todo:画像_代替_文章](managing-controls_9.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddinganArrowHead.java" >}}

## **ワークシートへの四角形コントロールの追加**

Aspose.Cells を使用すると、ワークシートに四角形を描画できます。長方形、正方形などを作成できます。また、コントロールの塗りつぶしの色と境界線の色をフォーマットすることもできます。たとえば、必要に応じて、長方形の色を変更したり、陰影の色を設定したり、長方形の太さとスタイルを指定したりできます。

### **Microsoft エクセルを使う**

1. 上で**描く**ツールバー、クリック**矩形**.
1. ドラッグして長方形を描きます。
1. 次のいずれかまたは両方を実行します。
 1. 開始点から四角形を描くように長方形を制限するには、Shift キーを押しながらドラッグします。
 1. 中心点から長方形を描くには、CTRL キーを押しながらドラッグします。

### **Aspose.Cells を使用**

の[**シェイプコレクション**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection)クラスは、ワークシートに四角形を追加するために使用される addShape という名前のメソッドを提供します。このメソッドは RectangleShape オブジェクトを返すことができます。クラス RectangleShape は長方形を表します。いくつかの重要なメンバーがあります。

- setLineFormat メソッドは、長方形の線フォーマット属性を指定します。
- setPlacement メソッドは PlacementType を指定します。これは、四角形がワークシートのセルに接続される方法です。
- FillFormat プロパティは、四角形の塗りつぶし形式のスタイルを指定します。

次の例は、ワークシートに四角形を追加する方法を示しています。コードを実行すると、次の出力が生成されます。

**ワークシートに四角形が追加されます** 

![todo:画像_代替_文章](managing-controls_10.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingRectangleControl-1.java" >}}

## **ワークシートへの円弧制御の追加**

Aspose.Cells を使用すると、ワークシートに円弧を描くことができます。シンプルで塗りつぶされた円弧を作成できます。コントロールの塗りつぶしの色と境界線の色をフォーマットできます。たとえば、円弧の色を指定/変更したり、シェーディングの色を設定したり、必要に応じて形状の重みとスタイルを指定したりできます。

### **Microsoft エクセルを使う**

1. 上で**描く**ツールバー、クリック**アーク**の中に**オートシェイプ**.
1. ドラッグして円弧を描きます。

### **Aspose.Cells を使用**

の[**シェイプコレクション**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection)クラスは addShape という名前のメソッドを提供します。これはワークシートに円弧形状を追加するために使用されます。このメソッドは、ArcShape オブジェクトを返すことができます。クラス ArcShape は円弧を表します。いくつかの重要なメンバーがあります。

- setLineFormat メソッドは、円弧形状の線フォーマット属性を指定します。
- setPlacement メソッドは、アークがワークシートのセルに接続される方法である PlacementType を指定します。
- FillFormat プロパティは、図形の塗りつぶし形式のスタイルを指定します。

次の例は、アーク形状をワークシートに追加する方法を示しています。この例では、2 つの円弧形状を作成します。1 つは塗りつぶされ、もう 1 つは単純です。コードを実行すると、次の出力が生成されます

**つの円弧形状がワークシートに追加されます** 

![todo:画像_代替_文章](managing-controls_11.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingArcControl-1.java" >}}

## **楕円形コントロールをワークシートに追加する**

Aspose.Cells では、ワークシートに楕円形を描くことができます。シンプルで塗りつぶされた楕円形を作成し、コントロールの塗りつぶしの色と境界線の色をフォーマットします。たとえば、楕円の色を指定/変更したり、シェーディングの色を設定したり、形状の太さとスタイルを指定したりできます。

### **Microsoft エクセルを使う**

1. 上で**描く**ツールバー、クリック**オーバル** .
1. ドラッグして楕円を描きます。
1. 次のいずれかまたは両方を実行します。
 1. 始点から円を描くように楕円を制限するには、Shift キーを押しながらドラッグします。
1. 中心点から楕円を描くには、CTRL キーを押しながらドラッグします。

### **Aspose.Cells を使用**

の[**シェイプコレクション**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection)クラスは、楕円形をワークシートに追加するために使用される addShape という名前のメソッドを提供します。このメソッドは、Oval オブジェクトを返す場合があります。 Oval クラスは、楕円形を表します。いくつかの重要なメンバーがあります。

- setLineFormat メソッドは、楕円形の線フォーマット属性を指定します。
-  setPlacement メソッドは、**配置タイプ**、楕円がワークシートのセルに接続される方法。
- FillFormat プロパティは、図形の塗りつぶし形式のスタイルを指定します。

次の例は、楕円形をワークシートに追加する方法を示しています。この例では、2 つの楕円形を作成します。1 つは塗りつぶされた楕円形で、もう 1 つは単純な円です。コードを実行すると、次の出力が生成されます。

**ワークシートに 2 つの楕円形が追加されます** 

![todo:画像_代替_文章](managing-controls_12.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddinganOvalControl-1.java" >}}

## **先行トピック**
- [Aspose.Cells を使用して ActiveX コントロールを追加します](/cells/ja/java/add-activex-controls-using-aspose-cells/)
- [ActiveX コントロールを削除する](/cells/ja/java/remove-activex-control/)
