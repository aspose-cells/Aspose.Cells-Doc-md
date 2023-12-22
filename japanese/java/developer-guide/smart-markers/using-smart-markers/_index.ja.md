---
title: スマートマーカーの使用
type: docs
weight: 40
url: /ja/java/using-smart-markers/
---
##  **導入**

{{% alert color="primary" %}}

**スマートマーカー**Aspose.Cells Excel に配置する情報を Aspose.Cells に知らせるために使用されます。[デザイナースプレッドシート](/cells/ja/java/what-is-a-designer-spreadsheet/)。スマート マーカーを使用すると、関連する情報と書式設定のみを含むテンプレートを作成できます。

{{% /alert %}}

##  **デザイナーのスプレッドシートとスマート マーカー**

デザイナー スプレッドシートは、視覚的な書式設定、数式、スマート マーカーを含む標準の Excel ファイルです。これらには、プロジェクトからの情報や関連する連絡先の情報など、1 つ以上のデータ ソースを参照するスマート マーカーを含めることができます。スマート マーカーは、情報が必要なセルに書き込まれます。

すべてのスマート マーカーは &= で始まります。データ マーカーの例は &=Party.FullName です。データ マーカーの結果が複数の項目 (完全な行など) になる場合、新しい情報を入れるスペースを確保するために、後続の行が自動的に下に移動されます。したがって、小計と合計をデータ マーカーの直後の行に配置して、挿入されたデータに基づいて計算を行うことができます。挿入された行に対して計算を行うには、次を使用します。[動的数式](/cells/ja/java/using-smart-markers/#dynamic-formulas).

スマート マーカーは次のもので構成されます。**情報元**そして**フィールド名**ほとんどの情報については、この部分を参照してください。特別な情報は、変数および変数配列とともに渡すこともできます。変数は常に 1 つのセルのみを入力しますが、変数配列は複数のセルを入力する場合があります。セルごとに 1 つのデータ マーカーのみを使用します。使用されていないスマート マーカーは削除されます。

スマート マーカーにはパラメータが含まれる場合もあります。パラメータを使用すると、情報のレイアウト方法を変更できます。これらは、スマート マーカーの末尾に、カンマ区切りのリストとして括弧内に追加されます。

###  **スマートマーカーオプション**

&=データソース.フィールド名
&=[データソース].[フィールド名]
&=$変数名
&=$変数配列
&==ダイナミックフォーミュラ
&=&=RepeatDynamicFormula

###  **パラメーター**

次のパラメータが許可されます。

- **ノアド** データを合わせるために余分な行を追加しないでください。
- **スキップ:n** - データの各行について n 行スキップします。
- *ascending:n またはdecending:n - スマート マーカー内のデータを並べ替えます。 n が 1 の場合、その列はソーターの最初のキーになります。データは、データ ソースの処理後に並べ替えられます。例: &=Table1.Field3(ascending:1)。
- **水平** データを上から下ではなく左から右に書き込みます。
- **数値** 可能であればテキストを数値に変換します。
- **シフト** 下または右にシフトして、データに合わせて追加の行または列を作成します。シフトパラメータは、Microsoft Excel と同じように機能します。たとえば、Microsoft Excel では、セル範囲を選択するときに右クリックして選択します。**入れる**そして指定します**セルを下にシフト**、**セルを右にシフト**およびその他のオプション。つまり、shift パラメーターは、垂直/標準 (上から下) または水平 (左から右) のスマート マーカーに対して同じ機能を果たします。
- **豆** データ ソースが単純な POJO であることを示します。 Java API でのみサポートされます。

パラメーター noadd と Skip を組み合わせて、交互の行にデータを挿入できます。テンプレートは下から上に処理されるため、代替行の前に余分な行が挿入されないように、最初の行に noadd を追加する必要があります。

複数のパラメータがある場合は、parameterA、parameterB、parameterC のようにスペースを入れずにカンマで区切ります。

次のスクリーンショットは、1 行おきにデータを挿入する方法を示しています。

![todo:image_alt_text](using-smart-markers_1.png)

**になる...**

![todo:image_alt_text](using-smart-markers_2.png)

###  **動的な数式**

動的数式を使用すると、エクスポート プロセス中に挿入される行を数式が参照している場合でも、Excel 数式をセルに挿入できます。動的数式は、挿入された行ごとに繰り返すことも、データ マーカーが配置されているセルのみを使用することもできます。

動的数式では、次の追加オプションが可能です。

- r - 現在の行番号。
- 2、-1 - 現在の行番号へのオフセット。

以下に、繰り返しの動的数式とその結果の Excel ワークシートを示します。

![todo:image_alt_text](using-smart-markers_3.png)

**になる…**

![todo:image_alt_text](using-smart-markers_4.png)

Cell C1 には式 =A1*B1 が含まれ、C2 には = A2*B2 および C3 = A3*B3 が含まれます。

スマートマーカーの処理は非常に簡単です。次のコード例は、スマート マーカーで動的数式を使用する方法を示しています。ロードします[テンプレートファイル](templateDynamicFormulas.xlsx)テスト データを作成し、マーカーを処理してマーカーに対してセルにデータを入力します。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-DynamicFormulas-DynamicFormulas.java" >}}

##  **変数配列の使用**

次のコード例は、スマート マーカーで変数配列を使用する方法を示しています。変数配列マーカーを、マーカーに設定した値の文字列を含むワークブックの最初のワークシートの A1 セルに動的に配置し、マーカーを処理して、マーカーに対してセルにデータを入力します。最後に、Excel ファイルを保存します。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-UsingVariableArray-UsingVariableArray.java" >}}

##  **データのグループ化**

一部の Excel レポートでは、読みやすく分析しやすいようにデータをグループに分割する必要がある場合があります。データをグループに分割する主な目的の 1 つは、レコードの各グループに対して計算を実行する (集計演算を実行する) ことです。

Aspose.Cells スマート マーカーを使用すると、フィールド セットごとにデータをグループ化し、データ セットまたはデータ グループの間に集計行を配置できます。たとえば、Customers.CustomerID でデータをグループ化する場合、グループが変更されるたびに概要レコードを追加できます。

###  **パラメーター**

以下は、データのグループ化に使用されるいくつかのスマート マーカー パラメーターです。

####  **グループ:ノーマル/マージ/リピート**

選択できる 3 種類のグループをサポートしています。

- **普通** フィールドごとのグループ値は、列内の対応するレコードに対して繰り返されません。代わりに、データ グループごとに 1 回印刷されます。
- **マージ** 通常のパラメーターと同じ動作ですが、各グループ セットのフィールドごとにグループ内のセルを結合します。
- **繰り返す** フィールドごとのグループ値は、対応するレコードに対して繰り返されます。

例: &=Customers.CustomerID(group:merge)

####  **スキップ**

各グループの後の特定の行数をスキップします。

例: &=Employees.EmployeeID(group:normal,skip:1)

####  **小計N**

グループ化フィールドに関連する指定されたフィールド データの集計操作を実行します。 N は、データのリスト内で小計を計算するときに使用される関数を指定する 1 ～ 11 の数値を表します。 (1=AVERAGE、2=COUNT、3=COUNTA、4=MAX、5=MIN、...9=SUM など) 詳細については、Excel のヘルプ Microsoft の小計リファレンスを参照してください。

実際の形式は次のようになります。
subtotalN:Ref ここで、Ref は列ごとのグループを指します。

例えば、

-  &=Products.Units(subtotal9:Products.ProductID) は集計関数を指定します**単位**に関するフィールド**製品番号**のフィールド**製品**テーブル。
-  &=Tabx.Col3(subtotal9:Tabx.Col1) は、集計関数を指定します。**列3**フィールドのグループ化基準**列1**テーブル *Tabx** 内。
-  &=Table1.ColumnD(subtotal9:Table1.ColumnA&Table1.ColumnB) は集計関数を指定します**列D**フィールドのグループ化基準**列A**そして**列B**テーブル *Table1** 内。

##  **ネストされたオブジェクトの使用**

Aspose.Cells はスマート マーカーでネストされたオブジェクトをサポートします。ネストされたオブジェクトは単純である必要があります。

単純なテンプレート ファイルを使用します。いくつかのネストされたスマート マーカーを含むデザイナー スプレッドシートを参照してください。

**ネストされたスマート マーカーを示すデザイナー ファイルの最初のワークシート。**

![todo:image_alt_text](using-smart-markers_5.png)

次の例は、これがどのように機能するかを示しています。以下のコードを実行すると、以下の出力が得られます。

**結果のデータを示す出力ファイルの最初のワークシート。**

![todo:image_alt_text](using-smart-markers_6.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-UsingNestedObjects-UsingNestedObjects.java" >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-Individual-Individual.java" >}}

##  **ジェネリックリストをネストされたオブジェクトとして使用する**

Aspose.Cells では、ネストされたオブジェクトとして汎用リストの使用もサポートされるようになりました。次のコードで生成された出力 Excel ファイルのスクリーンショットを確認してください。スクリーンショットでわかるように、Teacher オブジェクトには複数のネストされた生徒オブジェクトが含まれています。

![todo:image_alt_text](using-smart-markers_7.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-UsingGenericList-UsingGenericList.java" >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-Teacher-Teacher.java" >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-Person-Person.java" >}}

##  **スマート マーカーの HTML プロパティの使用**

次のサンプル コードでは、スマート マーカーの HTML プロパティの使用方法を説明します。処理されると、HTML \ のため、「Hello World」の「World」が太字で表示されます。<b>鬼ごっこ。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-UsingHTMLProperty-UsingHTMLProperty.java" >}}

##  **スマート マーカーとデータを結合する際の通知の取得**

場合によっては、完了前に処理中のセル参照または特定のスマート マーカーに関する通知を取得することが必要な場合があります。これは、[**WorkbookDesigner.CallBack**](https://reference.aspose.com/cells/java/com.aspose.cells/workbookdesigner#CallBack)財産と[**ISmartMarkerCallBack**](https://reference.aspose.com/cells/java/com.aspose.cells/ISmartMarkerCallBack)

サンプルコードと詳しい説明はこちらの記事をご覧ください。

- [スマート マーカーとデータを結合する際の通知の取得](/cells/ja/java/getting-notifications-while-merging-data-with-smart-markers/)
