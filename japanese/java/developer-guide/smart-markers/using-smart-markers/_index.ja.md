---
title: スマート マーカーの使用
type: docs
weight: 40
url: /ja/java/using-smart-markers/
---
## **序章**

{{% alert color="primary" %}}

**スマートマーカー**Aspose.Cells に、Microsoft Excel に配置する情報を知らせるために使用されます。[デザイナースプレッドシート](/cells/ja/java/what-is-a-designer-spreadsheet/).スマート マーカーを使用すると、関連する情報と書式のみを含むテンプレートを作成できます。

{{% /alert %}}

## **デザイナー スプレッドシートとスマート マーカー**

Designer スプレッドシートは、視覚的な書式設定、数式、およびスマート マーカーを含む標準の Excel ファイルです。プロジェクトからの情報や関連する連絡先の情報など、1 つ以上のデータ ソースを参照するスマート マーカーを含めることができます。スマート マーカーは、情報が必要なセルに書き込まれます。

すべてのスマート マーカーは &= で始まります。データ マーカーの例は &=Party.FullName です。データ マーカーの結果が複数の項目 (たとえば、完全な行) になる場合、次の行は自動的に下に移動され、新しい情報のためのスペースが確保されます。したがって、小計と合計をデータ マーカーの直後の行に配置して、挿入されたデータに基づいて計算を行うことができます。挿入された行を計算するには、次を使用します。[動的数式](/cells/ja/java/using-smart-markers/#dynamic-formulas).

スマート マーカーは、**情報元**と**フィールド名**ほとんどの情報の部品。特別な情報は、変数と変数配列で渡すこともできます。変数は常に 1 つのセルのみを埋めますが、変数配列は複数のセルを埋めます。セルごとに 1 つのデータ マーカーのみを使用します。未使用のスマート マーカーは削除されます。

スマート マーカーには、パラメーターを含めることもできます。パラメータを使用すると、情報のレイアウト方法を変更できます。それらは、カンマ区切りのリストとして括弧内のスマート マーカーの末尾に追加されます。

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
- *ascending:n または descending:n - スマート マーカーでデータを並べ替えます。 n が 1 の場合、列はソーターの最初のキーです。データ ソースの処理後に、データが並べ替えられます。例: &=Table1.Field3(昇順:1)。
- **水平** 上から下ではなく、左から右にデータを書き込みます。
- **数値** 可能であれば、テキストを数値に変換します。
- **シフト** 下または右にシフトし、データに合わせて余分な行または列を作成します。 shift パラメータは、Microsoft Excel と同じように機能します。たとえば、Microsoft Excel では、セルの範囲を選択するときに、右クリックして選択します。**入れる**と指定する**セルを下にシフト**, **セルを右にシフト**およびその他のオプション。つまり、シフト パラメータは、垂直/通常 (上から下) または水平 (左から右) のスマート マーカーに対して同じ機能を果たします。
- **豆** データ ソースが単純な POJO であることを示します。 Java API でのみサポートされています。

パラメータ noadd と skip を組み合わせて、交互の行にデータを挿入できます。テンプレートは下から上に処理されるため、余分な行が別の行の前に挿入されないように、最初の行に noadd を追加する必要があります。

複数のパラメーターがある場合は、スペースを入れずにコンマで区切ります: parameterA、parameterB、parameterC

次のスクリーンショットは、1 行おきにデータを挿入する方法を示しています。

![todo:画像_代替_文章](using-smart-markers_1.png)

**なる...**

![todo:画像_代替_文章](using-smart-markers_2.png)

### **動的数式**

動的数式を使用すると、数式がエクスポート プロセス中に挿入される行を参照している場合でも、Excel 数式をセルに挿入できます。動的数式は、挿入された行ごとに繰り返すことも、データ マーカーが配置されているセルのみを使用することもできます。

動的数式では、次の追加オプションを使用できます。

- r - 現在の行番号。
- 2、-1 - 現在の行番号へのオフセット。

次の図は、繰り返し動的数式と結果の Excel ワークシートを示しています。

![todo:画像_代替_文章](using-smart-markers_3.png)

**…になる**

![todo:画像_代替_文章](using-smart-markers_4.png)

Cell C1 には式 =A1 が含まれています*B1、C2 を含む = A2*B2 と C3 = A3*B3。

スマートマーカーの処理は非常に簡単です。次のコード スニペットは、その方法を示しています。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-DynamicFormulas-DynamicFormulas.java" >}}

## **変数配列の使用**

次のコード例は、スマート マーカーで変数配列を使用する方法を示しています。ワークブックの最初のワークシートの A1 セルに可変配列マーカーを動的に配置します。このセルには、マーカーに設定した値の文字列が含まれており、マーカーを処理して、マーカーに対してセルにデータを入力します。最後に、Excel ファイルを保存します。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-UsingVariableArray-UsingVariableArray.java" >}}

## **データのグループ化**

一部の Excel レポートでは、読みやすく分析しやすくするために、データをグループに分割する必要がある場合があります。データをグループに分割する主な目的の 1 つは、レコードの各グループに対して計算を実行する (集計操作を実行する) ことです。

Aspose.Cells スマート マーカーを使用すると、フィールド セットごとにデータをグループ化し、データ セットまたはデータ グループの間に集計行を配置できます。たとえば、Customers.CustomerID でデータをグループ化すると、グループが変更されるたびに集計レコードを追加できます。

### **パラメーター**

以下は、データのグループ化に使用されるスマート マーカー パラメーターの一部です。

#### **グループ:ノーマル/マージ/リピート**

選択できる 3 種類のグループをサポートしています。

- **正常** フィールド値によるグループ化は、列内の対応するレコードに対して繰り返されません。代わりに、データ グループごとに 1 回出力されます。
- **マージ** 通常のパラメータと同じ動作ですが、グループ セットごとにフィールドごとにグループ内のセルをマージします。
- **繰り返す** フィールド値によるグループ化は、対応するレコードに対して繰り返されます。

例: &=Customers.CustomerID(group:merge)

#### **スキップ**

各グループの後、特定の数の行をスキップします。

例 &=Employees.EmployeeID(group:normal,skip:1)

#### **小計N**

グループ化フィールドに関連する指定されたフィールド データの集計操作を実行します。 N は、データのリスト内の小計を計算するときに使用される関数を指定する 1 から 11 までの数値を表します。 (1=AVERAGE、2=COUNT、3=COUNTA、4=MAX、5=MIN、...9=SUM など) 詳細については、Microsoft Excel のヘルプの小計リファレンスを参照してください。

形式は実際には次のように述べています。
subtotalN:Ref Ref はグループごとの列を参照します。

例えば、

-  &=Products.Units(subtotal9:Products.ProductID) は集計関数を指定します**単位**に関するフィールド**製品番号**のフィールド**製品**テーブル。
-  &=Tabx.Col3(subtotal9:Tabx.Col1) は、**Col3**フィールドのグループ化**Col1**テーブルで**Tabx**.
-  &=Table1.ColumnD(subtotal9:Table1.ColumnA&Table1.ColumnB) で集計関数を指定**列 D**フィールドのグループ化**列A**と**列B**表に**表1**.

## **ネストされたオブジェクトの使用**

Aspose.Cells は、スマート マーカーでネストされたオブジェクトをサポートします。ネストされたオブジェクトは単純でなければなりません。

シンプルなテンプレート ファイルを使用します。ネストされたスマート マーカーを含むデザイナー スプレッドシートを参照してください。

**ネストされたスマート マーカーを示すデザイナー ファイルの最初のワークシート。**

![todo:画像_代替_文章](using-smart-markers_5.png)

次の例は、これがどのように機能するかを示しています。以下のコードを実行すると、以下の出力が得られます。

**結果データを示す出力ファイルの最初のワークシート。**

![todo:画像_代替_文章](using-smart-markers_6.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-UsingNestedObjects-UsingNestedObjects.java" >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-Individual-Individual.java" >}}

## **汎用リストをネストされたオブジェクトとして使用する**

Aspose.Cells は、一般的なリストをネストされたオブジェクトとして使用することもサポートするようになりました。次のコードで生成された出力 Excel ファイルのスクリーンショットを確認してください。スクリーンショットでわかるように、教師オブジェクトには複数のネストされた生徒オブジェクトが含まれています。

![todo:画像_代替_文章](using-smart-markers_7.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-UsingGenericList-UsingGenericList.java" >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-Teacher-Teacher.java" >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-Person-Person.java" >}}

## **Smart Markers の HTML プロパティの使用**

次のサンプル コードでは、スマート マーカーの HTML プロパティの使用について説明します。処理されると、HTML のため、「Hello World」の「World」が太字で表示されます\<b>鬼ごっこ。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-UsingHTMLProperty-UsingHTMLProperty.java" >}}

## **スマート マーカーを使用してデータを結合する際の通知の取得**

完了する前に、セル参照または処理中の特定のスマート マーカーに関する通知を取得する必要がある場合があります。これは、[**WorkbookDesigner.CallBack**](https://reference.aspose.com/cells/java/com.aspose.cells/workbookdesigner#CallBack)プロパティと[**ISmartMarkerCallBack**](https://reference.aspose.com/cells/java/com.aspose.cells/ISmartMarkerCallBack)

サンプルコードと詳しい説明はこちらの記事をご覧ください。

- [スマート マーカーを使用してデータを結合する際の通知の取得](/cells/ja/java/getting-notifications-while-merging-data-with-smart-markers/)
