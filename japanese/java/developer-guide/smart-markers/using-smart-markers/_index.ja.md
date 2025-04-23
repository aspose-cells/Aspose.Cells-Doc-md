---
title: スマートマーカーを使用する
type: docs
weight: 40
url: /ja/java/using-smart-markers/
---

## **紹介**

{{% alert color="primary" %}}

**スマートマーカー**は、Aspose.CellsにMicrosoft Excelの[デザイナースプレッドシート](/cells/ja/java/what-is-a-designer-spreadsheet/)に配置する情報やフォーマットを指示するために使用されます。スマートマーカーを使用することで、関連する情報や連絡先の情報など、重要な情報とフォーマットだけを含むテンプレートを作成できます。

{{% /alert %}}

## **デザイナースプレッドシートとスマートマーカー**

デザイナースプレッドシートは、視覚的なフォーマットや数式、スマートマーカーを含む標準のExcelファイルです。1つ以上のデータソース、プロジェクトからの情報や関連する連絡先の情報などが参照されるスマートマーカーを含めることができます。スマートマーカーは、情報を必要とするセルに書き込まれます。

すべてのスマートマーカーは&=で始まります。データマーカーの例として、&=Party.FullNameがあります。データマーカーの結果が1つ以上ある場合、例えば完全な行の場合、その後の行は自動的に下に移動して、新しい情報のためのスペースを作ります。そのため、挿入されたデータに基づいてサブトータルや合計を入れるために、挿入された行のすぐ後ろの行にサブトータルや合計を入れることができます。挿入された行の計算をするには、[動的な数式](/cells/ja/java/using-smart-markers/#dynamic-formulas)を使用します。

スマートマーカーには、ほとんどの情報の**データソース**と**フィールド名**から成るものがあります。特別な情報は変数や変数配列を伴ったスマートマーカーにも渡される場合があります。変数は常に1つのセルのみに入り、変数配列は複数のセルに入ることがあります。セルごとに1つのデータマーカーしか使用しないでください。未使用のスマートマーカーは削除されます。

スマートマーカーにはパラメータも含まれる場合があります。パラメータを使用することで、情報のレイアウトの修正が可能です。それらはセルのスマートマーカーの末尾に、カンマで区切られたリストとして括弧に追加されます。

### **スマートマーカーオプション**

&=DataSource.FieldName
&=[Data Source].[Field Name]
&=$VariableName
&=$VariableArray
&==DynamicFormula
&=&=RepeatDynamicFormula

### **パラメータ**

以下のパラメータが許可されています:

- **noadd** - データに合わせて追加の行を追加しません。
- **skip:n** - 各データ行ごとにn行をスキップします。
- **horizontal** - データを左から右に書き込みます。上から下へではなく。
- **horizontal** - 上下ではなく左から右にデータを書き込みます。
- **numeric** - 可能であればテキストを数値に変換します。
- **shift** - データに合わせて追加の行または列を作成し、下または右にシフトします。シフトパラメータは、マイクロソフトエクセルの場合と同じように機能します。 たとえば、セルの範囲を選択して、右クリックして**挿入**を選択し、**セルを下にシフト**、**セルを右にシフト**などを指定します。 要するに、シフトパラメータは、垂直/通常（上から下）または水平（左から右）スマートマーカーのために同じ機能を果たします。
- **bean** - データソースがシンプルなPOJOであることを示します。 Java APIでのみサポートされています。

noaddとskipパラメータは、交互の行にデータを挿入するために組み合わせることができます。 テンプレートは上から下に処理されるため、交互の行の前に余分な行が挿入されないように最初の行にnoaddを追加する必要があります。

複数のパラメータがある場合は、それらをカンマで区切りますが、スペースはありません: パラメータA、パラメータB、パラメータC

次のスクリーンショットは、交互の行にデータを挿入する方法を示しています。

![todo:image_alt_text](using-smart-markers_1.png)

**になります...**

![todo:image_alt_text](using-smart-markers_2.png)

### **動的な式**

動的な式を使用すると、エクスポートプロセス中に挿入される行を参照する式をセルに挿入できます。 動的な式は、挿入された行ごとに繰り返すことができるか、データマーカーが配置されたセルのみを使用できます。

動的な式には、次の追加のオプションがあります:

- r - 現在の行番号。
- 2, -1 - 現在の行番号へのオフセット。

次の図は、繰り返しダイナミック式とその結果のExcelワークシートを示しています。

![todo:image_alt_text](using-smart-markers_3.png)

**になります...**

![todo:image_alt_text](using-smart-markers_4.png)

セルC1には式として=A1*B1、C2には= A2*B2、C3にはA3*B3が含まれています。

スマートマーカーの処理は非常に簡単です。 次の例コードは、スマートマーカーで動的式を使用する方法を示しています。 [テンプレートファイル](templateDynamicFormulas.xlsx)を読み込んでテストデータを作成し、マーカーを処理してセルにデータを埋めます。 

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-DynamicFormulas-DynamicFormulas.java" >}}

## **変数配列を使用する**

次の例コードは、スマートマーカーで変数配列を使用する方法を示しています。 ワークブックの最初のワークシートのA1セルに動的に変数配列マーカーを配置し、マーカーに設定された値の文字列を含めます。 マーカーに対してセルにデータを入れるためにマーカーを処理します。 最後に、Excelファイルを保存します。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-UsingVariableArray-UsingVariableArray.java" >}}

## **データのグループ化**

Excelの報告書では、データをグループ化して読みやすくし、分析しやすくする必要があることがあります。データをグループに分割する主な目的の1つは、各レコードのグループごとに計算（集計演算）を実行することです。

Aspose.Cellsのスマートマーカーを使用すると、フィールドを設定してデータをグループ化し、データセットまたはデータグループの間に集計行を配置することができます。たとえば、Customers.CustomerIDでデータをグループ化する場合、グループが変更されるたびに集計レコードを追加できます。

### **パラメータ**

次に、データのグループ化に使用されるいくつかのスマートマーカーパラメータを示します。

#### **group:normal/merge/repeat**

選択できる3種類のグループをサポートしています。

- **normal** - グループ化フィールドの値が対応する列のレコードで繰り返されず、代わりに各データグループごとに一度だけ印刷されます。
- **merge** - normalパラメータと同様の動作ですが、グループ化フィールドのセルを各グループセットごとにマージします。
- **repeat** - グループ化フィールドの値が対応するレコードで繰り返されます。

例: &=Customers.CustomerID(group:merge)

#### **skip**

各グループの後に特定の行数をスキップします。

例: &=Employees.EmployeeID(group:normal,skip:1)

#### **subtotalN**

グループ化フィールドに関連する指定されたフィールドデータの集計操作を実行します。Nは、データリスト内の小計を計算する際に使用される関数を1から11までの数字で指定します（1=AVERAGE, 2=COUNT, 3=COUNTA, 4=MAX, 5=MIN, ... 9=SUM など）。詳細については、Microsoft Excelのヘルプの小計リファレンスを参照してください。

実際のフォーマットは次のようになります:
subtotalN:Ref ここで、Refはグループ化する列を意味します。

例:

- &=Products.Units(subtotal9:Products.ProductID) は**Units**フィールドに対して**Products**テーブルの**ProductID**フィールドに関連して要約関数を指定します。
- &=Tabx.Col3(subtotal9:Tabx.Col1) は**Col3**フィールドを**Col1**でグループ化する際に要約関数を指定します。
- &=Table1.ColumnD(subtotal9:Table1.ColumnA&Table1.ColumnB) は**ColumnA**および**ColumnB**でグループ化する**ColumnD**フィールドに対して要約関数を指定します。

## **ネストされたオブジェクトの使用**

Aspose.Cellsはスマートマーカー内でネストされたオブジェクトをサポートしており、ネストされたオブジェクトは簡単である必要があります。

簡単なテンプレートファイルを使用します。いくつかのネストされたスマートマーカーを含むデザイナースプレッドシートを参照してください。

**デザイナーファイルの最初のワークシートには、ネストされたスマートマーカーが表示されます。**

![todo:image_alt_text](using-smart-markers_5.png)

次の例は、この機能の動作方法を示しています。以下のコードを実行すると、以下の出力が得られます。

**出力ファイルの最初のワークシートには、生成されたデータが表示されます。**

![todo:image_alt_text](using-smart-markers_6.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-UsingNestedObjects-UsingNestedObjects.java" >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-Individual-Individual.java" >}}

## **ネストされたオブジェクトとしてのジェネリックリストの使用**

Aspose.Cellsは今やジェネリックリストをネストされたオブジェクトとして使用することをサポートしています。次のコードで生成された出力エクセルファイルのスクリーンショットをご確認ください。スクリーンショットには、Teacherオブジェクトが複数のネストされたstudentオブジェクトを含むことが示されています。

![todo:image_alt_text](using-smart-markers_7.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-UsingGenericList-UsingGenericList.java" >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-Teacher-Teacher.java" >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-Person-Person.java" >}}

## **スマートマーカーのHTMLプロパティの使用**

The following sample code explains the use of the HTML property of the Smart Markers. When it will be processed, it will show "World" in "Hello World" as bold because of HTML \<b> tag.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-UsingHTMLProperty-UsingHTMLProperty.java" >}}

## **スマートマーカーを使用してデータをマージする際の通知の取得**

完了前に処理されるセル参照または特定のスマートマーカーに関する通知を取得する必要がある場合があります。これは[**WorkbookDesigner.CallBack**](https://reference.aspose.com/cells/java/com.aspose.cells/workbookdesigner#CallBack)プロパティおよび[**ISmartMarkerCallBack**](https://reference.aspose.com/cells/java/com.aspose.cells/ISmartMarkerCallBack)プロパティを使用して実現できます。

サンプルコードと詳細な説明については、この記事を参照してください。

- [スマートマーカーを使用してデータをマージする際の通知の取得](/cells/ja/java/getting-notifications-while-merging-data-with-smart-markers/)
{{< app/cells/assistant language="java" >}}
