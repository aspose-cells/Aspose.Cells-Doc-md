---
title: スマート マーカーを使用してデータをスマートにインポートおよび配置する
linktitle: スマートマーカー
type: docs
weight: 190
url: /ja/net/using-smart-markers/
description: Aspose.Cells ライブラリを使用してテンプレート Excel ファイルに合わせてデータをスマートにインポートおよび配置します。
---
## **序章**
**スマートマーカー**Aspose.Cells Excel デザイナー スプレッドシートに配置する情報を Aspose.Cells に知らせるために使用されます。スマート マーカーを使用すると、特定の情報と書式のみを含むテンプレートを作成できます。
## **デザイナー スプレッドシートとスマート マーカー**
Designer スプレッドシートは、視覚的な書式設定、数式、およびスマート マーカーを含む標準の Excel ファイルです。プロジェクトからの情報や関連する連絡先の情報など、1 つ以上のデータ ソースを参照するスマート マーカーを含めることができます。スマート マーカーは、情報が必要なセルに書き込まれます。

すべてのスマート マーカーは &= で始まります。データ マーカーの例は &=Party.FullName です。データ マーカーの結果が複数の項目 (たとえば、完全な行) になる場合、次の行は自動的に下に移動され、新しい情報のためのスペースが確保されます。したがって、小計と合計をデータ マーカーの直後の行に配置して、挿入されたデータに基づいて計算を行うことができます。挿入された行を計算するには、次を使用します。**動的数式**.

スマート マーカーは、**情報元**と**フィールド名**ほとんどの情報の部品。特別な情報は、変数と変数配列で渡すこともできます。変数は常に 1 つのセルのみを埋めますが、変数配列は複数のセルを埋めます。セルごとに 1 つのデータ マーカーのみを使用します。未使用のスマート マーカーは削除されます。

スマート マーカーには、パラメーターを含めることもできます。パラメータを使用すると、情報のレイアウト方法を変更できます。これらは、カンマ区切りのリストとして括弧内のスマート マーカーの末尾に追加されます。
### **スマート マーカーのオプション**
 &=データソース.フィールド名
&=[データソース].[フィールド名]&=$変数名
&=$変数配列
&==動的式
&=&=RepeatDynamicFormula
### **パラメーター**
次のパラメータが許可されています。

- **noadd** - データに合わせて余分な行を追加しないでください。
- **スキップ:n** - データの各行に対して n 行をスキップします。
- **昇順:n**また**降順:n** - スマート マーカーでデータを並べ替えます。 n が 1 の場合、列はソーターの最初のキーです。データ ソースの処理後に、データが並べ替えられます。例: &=Table1.Field3(昇順:1)。
- **水平** 上から下ではなく、左から右にデータを書き込みます。
- **数値** 可能であれば、テキストを数値に変換します。
- **シフト** 下または右にシフトし、データに合わせて余分な行または列を作成します。 shift パラメータは、Microsoft Excel と同じように機能します。たとえば、Microsoft Excel では、セルの範囲を選択するときに、右クリックして選択します。**入れる**と指定する**セルを下にシフト**, **セルを右にシフト**およびその他のオプション。要するに、**シフト**パラメータは、垂直/通常 (上から下) または水平 (左から右) のスマート マーカーに対して同じ機能を果たします。
- **コピースタイル** 基本セルのスタイルをその列のすべてのセルにコピーします。

パラメータ noadd と skip を組み合わせて、交互の行にデータを挿入できます。テンプレートは下から上に処理されるため、最初の行に noadd を追加して、別の行の前に余分な行が挿入されないようにする必要があります。

複数のパラメーターがある場合は、スペースを入れずにコンマで区切ります: parameterA、parameterB、parameterC

次のスクリーンショットは、1 行おきにデータを挿入する方法を示しています。

|**テンプレートファイル**|**出力ファイル**|
|:- |:- |
|![todo:画像_代替_文章](using-smart-markers_1.jpg)|![todo:画像_代替_文章](using-smart-markers_2.jpg)|
### **動的数式**
動的数式を使用すると、数式がエクスポート プロセス中に挿入される行を参照している場合でも、Excel 数式をセルに挿入できます。動的数式は、挿入された行ごとに繰り返すことも、データ マーカーが配置されているセルのみを使用することもできます。

動的数式では、次の追加オプションを使用できます。

- r - 現在の行番号。
- 2、-1 - 現在の行番号へのオフセット。

例えば：

{{< highlight "java" >}}

 &=&=B{-1}/C{-1}~(skip:1)

{{< /highlight >}}

動的数式マーカーでは、「-1」は除算演算用に設定される B 列と C 列のそれぞれの現在の行へのオフセットを示し、スキップ パラメーターは 1 行です。さらに、次の文字を指定する必要があります。

{{< highlight "java" >}}

 "~"

{{< /highlight >}}

動的数式でさらにパラメータを適用するための区切り文字として。

次のスクリーンショットは、動的数式の繰り返しと結果の Excel ワークシートを示しています。

|**テンプレートファイル**|**出力ファイル**|
|:- |:- |
|![todo:画像_代替_文章](using-smart-markers_3.jpg)|![todo:画像_代替_文章](using-smart-markers_4.jpg)|
Cell "C1" には数式が含まれています**A1*B1** 、セル「C2」が含まれています**A2*B2**セル「C3」には**A3*B3**.

スマートマーカーの処理は非常に簡単です。以下は 2 つのコード スニペットです。1 つは C# に、もう 1 つは VB にあり、その方法を示しています。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-DynamicFormulas-1.cs" >}}
## **変数配列の使用**
次のコード例は、スマート マーカーで変数配列を使用する方法を示しています。ワークブックの最初のワークシートの A1 セルに変数配列マーカーを動的に配置します。このセルには、マーカーに設定した値の文字列が含まれており、マーカーを処理して、マーカーに対してセルにデータを入力します。最後に、Excel ファイルを保存します。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-UsingVariableArray-1.cs" >}}
## **データのグループ化**
一部の Excel レポートでは、読みやすく分析しやすくするために、データをグループに分割する必要がある場合があります。データをグループに分割する主な目的の 1 つは、レコードの各グループに対して計算を実行する (集計操作を実行する) ことです。

Aspose.Cells スマート マーカーを使用すると、フィールドごとにデータをグループ化し、データ セットまたはデータ グループの間に集計行を配置できます。たとえば、Customers.CustomerID でデータをグループ化すると、グループが変更されるたびに集計レコードを追加できます。
### **パラメーター**
以下は、データのグループ化に使用されるスマート マーカー パラメーターの一部です。
#### **グループ:ノーマル/マージ/リピート**
選択できる 3 種類のグループをサポートしています。

- **正常** フィールド値によるグループ化は、列内の対応するレコードに対して繰り返されません。代わりに、データ グループごとに 1 回出力されます。
- **マージ** 通常のパラメータと同じ動作ですが、グループ セットごとにフィールドごとにグループ内のセルをマージします。
- **繰り返す** フィールド値によるグループ化は、対応するレコードに対して繰り返されます。

例: &=Customers.CustomerID(group:merge)
#### **スキップ**
各グループの後、指定された数の行をスキップします。

例: &=Employees.EmployeeID(group:normal,skip:1)
#### **小計N**
グループ化フィールドに関連する指定されたフィールド データの集計操作を実行します。 N は、データのリスト内の小計を計算するときに使用される関数を指定する 1 から 11 までの数値を表します。 (1=AVERAGE、2=COUNT、3=COUNTA、4=MAX、5=MIN、...9=SUM など) 詳細については、Microsoft Excel のヘルプの小計リファレンスを参照してください。

形式は実際には次のように述べています。
subtotalN:Ref Ref はグループごとの列を参照します。

例えば、

-  &=Products.Units(subtotal9:Products.ProductID) は集計関数を指定します**単位**に関するフィールド**製品番号**のフィールド**製品**テーブル。
-  &=Tabx.Col3(subtotal9:Tabx.Col1) は、**Col3**フィールドのグループ化**Col1**テーブルで**Tabx**.
-  &=Table1.ColumnD(subtotal9:Table1.ColumnA&Table1.ColumnB) で集計関数を指定**列 D**フィールドのグループ化**列A**と**列B**テーブルで**表1**.

この例は、実際のグループ化パラメーターの一部を示しています。 Northwind.mdb Microsoft Access データベースを使用し、"Order Details" という名前のテーブルからデータを抽出します。 Microsoft Excel で SmartMarker_Designer.xls というデザイナー ファイルを作成し、ワークシートのさまざまなセルにスマート マーカーを配置します。マーカーは、ワークシートを埋めるために処理されます。データは、グループ フィールドごとに配置および編成されます。

デザイナー ファイルには 2 つのワークシートがあります。最初に、下のスクリーンショットに示すように、グループ化パラメーターを使用してスマート マーカーを配置します。 3 つのスマート マーカー (グループ化パラメーター付き) が配置されます。
&=[注文内容].OrderID(group:merge,skip:1),
&=[注文明細].Quantity(subtotal9:注文明細.OrderID)、および
&=[Order Details].UnitPrice(subtotal9:Order Details.OrderID) はそれぞれ A5、B5、C5 に入ります。

|**SmartMarker_Designer.xls ファイルの最初のワークシートで、スマート マーカーが含まれています。**|
|:- |
|![todo:画像_代替_文章](using-smart-markers_5.png)|
デザイナー ファイルの 2 番目のワークシートには、下の図に示すように、さらにスマート マーカーを配置します。次のスマート マーカーを配置します。
&=[注文内容].OrderID(グループ:通常),
&=[注文内容].数量,
&=[注文内容].単価,
&=&=B(r)*C(r)、および
&=subtotal9:Order Details.OrderID をそれぞれ A5、B5、C5、D5、C6 に変換します。

|**混合スマート マーカーを示す SmartMarker_Designer.xls ファイルの 2 番目のワークシート。**|
|:- |
|![todo:画像_代替_文章](using-smart-markers_6.png)|
この例で使用されているソース コードは次のとおりです。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-GroupingData-1.cs" >}}

{{% alert color="primary" %}} 

サマリー行に独自のカスタム ラベルを追加する必要がある場合、またはフィールドの名前を「注文の小計」などのラベルと連結したい場合は、Aspose.Cells が Label および LabelPosition 属性を提供するので、スマート ラベルにカスタム ラベルを配置できます。グループ化データの小計行と連結する際のマーカー。参照用に、カスタム ラベルを追加してスマート マーカーの小計行と連結する方法に関するドキュメントを参照してください。

{{% /alert %}} 
## **匿名型またはカスタム オブジェクトの使用**
Aspose.Cells は、スマート マーカーで匿名型またはカスタム オブジェクトもサポートします。次の例は、これがどのように機能するかを示しています。スマート マーカーを使用して動的オブジェクトからデータをインポートするには、次の記事を参照してください。

[動的オブジェクトからデータ ソースとしてインポートする](/cells/ja/net/import-data-into-worksheet/#importdataintoworksheet-importingfromdynamicobjectasdatasource)



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-UsingAnonymousTypes-1.cs" >}}
## **画像マーカー**
Aspose.Cells スマートマーカーは画像マーカーもサポートしています。このセクションでは、スマート マーカーを使用して画像を挿入する方法について説明します。
### **画像パラメータ**
画像を管理するためのスマート マーカー パラメータ。

- **画像:FitToCell** - 画像をセルの行の高さと列の幅に自動調整します。
- **写真:ScaleN** - 高さと幅を N パーセントにスケーリングします。
- **写真:幅:忍&高さ:忍** 高さ N インチ、幅 N インチのイメージをレンダリングします。 Left と Top の位置をポイント単位で指定することもできます。

この例で使用されているソース コードは次のとおりです。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-ImageMarkers-1.cs" >}}
## **ネストされたオブジェクトの使用**
Aspose.Cells は、スマート マーカーでネストされたオブジェクトをサポートします。ネストされたオブジェクトは単純でなければなりません。シンプルなテンプレート ファイルを使用します。ネストされたスマート マーカーを含むデザイナー スプレッドシートを参照してください。

|**ネストされたスマート マーカーを示す SM_NestedObjects.xlsx ファイルの最初のワークシート。**|
|:- |
|![todo:画像_代替_文章](using-smart-markers_7.png)|
次の例は、これがどのように機能するかを示しています。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-UsingNestedObjects-1.cs" >}}
## **汎用リストをネストされたオブジェクトとして使用する**
Aspose.Cells は、ネストされたオブジェクトとしてジェネリック リストの使用もサポートするようになりました。次のコードで生成された出力 Excel ファイルのスクリーンショットを確認してください。スクリーンショットでわかるように、Teacher オブジェクトにはネストされた複数の Student オブジェクトが含まれています。

|![todo:画像_代替_文章](using-smart-markers_8.png)|
|:- |




{{< gist "aspose-com-gists" "24a8eac23c3325e20dababecf735a43b" "Examples-CSharp-SmartMarkers-UsingGenericList-1.cs" >}}
## **Smart Markers の HTML プロパティの使用**
次のサンプル コードでは、スマート マーカーの HTML プロパティの使用について説明します。処理されると、HTML のため、「Hello World」の「World」が太字で表示されます。<b>鬼ごっこ。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-UsingHTMLProperty-1.cs" >}}

## **行ごとではない**
現在のデフォルトの処理方法は、smartmaker を 1 行ずつ処理することです。しかし、場合によっては、同じデータ テーブルのスマート マーカーをまとめて処理する必要があります。
それらが同じ行にあるかどうか、名前付き範囲「_CellsSmartMarkers」を指定し、処理を呼び出す前に WorkbookDesigner.LineByLine を false として指定する必要があります。

|![todo:画像_代替_文章](using-smart-markers_11.png)|

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-LayerByLayer.cs" >}}

## **スマート マーカーを使用してデータを結合する際の通知の取得**
完了する前に、セル参照または処理中の特定のスマート マーカーに関する通知を取得する必要がある場合があります。これは、WorkbookDesigner.CallBack プロパティと ISmartMarkerCallBack を使用して実現できます。

## **先行トピック**
- [匿名またはカスタム オブジェクトを SmartMarker に追加する](/cells/ja/net/adding-anonymous-or-custom-object-into-smartmarkers/)
- [データが大きすぎる場合、スマート マーカー データを他のワークシートに自動入力](/cells/ja/net/auto-populate-smart-marker-data-to-other-worksheets-if-data-is-too-large/)
- [スマート マーカーの書式設定](/cells/ja/net/formatting-smart-markers/)
- [スマート マーカーを使用してデータを結合する際の通知の取得](/cells/ja/net/getting-notifications-while-merging-data-with-smart-markers/)
- [WorkbookDesigner のカスタム DataSource を設定する](/cells/ja/net/set-custom-datasource-for-workbookdesigner/)
- [セルの先頭のアポストロフィを表示する](/cells/ja/net/show-leading-apostrophe-in-cells/)
- [Smart Marker フィールドで Formula パラメータを使用する](/cells/ja/net/using-formula-parameter-in-smart-marker-field/)
- [スマート マーカーでデータをグループ化する際の画像マーカーの使用](/cells/ja/net/using-image-markers-while-grouping-data-in-smart-markers/)


