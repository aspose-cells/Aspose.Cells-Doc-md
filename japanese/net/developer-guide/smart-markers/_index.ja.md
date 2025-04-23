---
title: スマートマーカーを使用してデータをスマートにインポートおよび配置する
linktitle: スマートマーカー
type: docs
weight: 190
url: /ja/net/using-smart-markers/
description: Aspose.Cellsライブラリを使用して、テンプレートExcelファイルに従ってデータをスマートにインポートおよび配置する。
---


## **紹介**
**スマートマーカー**は、Aspose.Cellsにどの情報をMicrosoft Excelのデザイナースプレッドシートに配置するかを知らせるために使用されます。スマートマーカーを使用すると、特定の情報と書式を含むテンプレートを作成できます。
## **デザイナースプレッドシートとスマートマーカー**
デザイナースプレッドシートは、視覚的な書式、数式、スマートマーカーを含む標準のExcelファイルです。プロジェクトからの情報や関連連絡先の情報など、1つ以上のデータソースを参照するスマートマーカーを含めることができます。スマートマーカーは、情報を配置したいセルに書き込まれます。

すべてのスマートマーカーは、&=で始まります。データマーカーの例として、&=Party.FullNameがあります。データマーカーが1つ以上のアイテム（例：完全な行）の結果を得る場合、新しい情報に対応するために自動的に次の行が移動されます。したがって、サブトータルや合計は、挿入されたデータに基づいて計算を行うために、データマーカーの直後の行に配置することができます。挿入された行で計算を行うには、**動的な数式**を使用します。

スマートマーカーには、ほとんどの情報の**データソース**と**フィールド名**から成るものがあります。特別な情報は変数や変数配列を伴ったスマートマーカーにも渡される場合があります。変数は常に1つのセルのみに入り、変数配列は複数のセルに入ることがあります。セルごとに1つのデータマーカーしか使用しないでください。未使用のスマートマーカーは削除されます。

スマートマーカーにはパラメータも含めることができます。パラメータを使用すると、情報のレイアウト方法を変更することができます。パラメータは、カンマで区切られたリストとしてスマートマーカーの末尾に追加されます。
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
- **ascending:n**または**descending:n** - スマートマーカーのデータをソートします。nが1の場合、列はソーターの最初のキーです。データはデータソースの処理後に並べ替えられます。例えば：&=Table1.Field3(ascending:1)。
- **horizontal** - 上下ではなく左から右にデータを書き込みます。
- **numeric** - 可能であればテキストを数値に変換します。
- **shift** - 下方向または右方向にシフトし、データに合わせて余分な行または列を作成します。シフトパラメーターはMicrosoft Excelと同じ方法で機能します。たとえば、Microsoft Excelではセルの範囲を選択して、右クリックして**挿入**を選択し、**セルを下にシフト**、**セルを右にシフト**などを指定します。 簡単に言うと、**shift**パラメーターは垂直／通常（上から下へ）または水平（左から右へ）のスマートマーカーのために同じ機能を果たします。
- **copystyle** - ベースセルのスタイルをその列のすべてのセルにコピーします。

パラメーターnoaddとskipを組み合わせることで、交互に行にデータを挿入できます。テンプレートは上から下に処理されるため、交互の行の前に余分な行が挿入されるのを避けるために、最初の行にnoaddを追加するべきです。

複数のパラメータを持つ場合は、コンマで区切りますが、スペースは入れません：parameterA,parameterB,parameterC。

次のスクリーンショットは、交互の行にデータを挿入する方法を示しています。

|**テンプレートファイル**|**出力ファイル**|
| :- | :- |
|![todo:image_alt_text](using-smart-markers_1.jpg)|![todo:image_alt_text](using-smart-markers_2.jpg)|
### **動的な式**
動的な式を使用すると、エクスポートプロセス中に挿入される行を参照する式をセルに挿入できます。 動的な式は、挿入された行ごとに繰り返すことができるか、データマーカーが配置されたセルのみを使用できます。

動的な式には、次の追加のオプションがあります:

- r - 現在の行番号。
- 2, -1 - 現在の行番号へのオフセット。

例:

{{< highlight java >}}

 &=&=B{-1}/C{-1}~(skip:1)

{{< /highlight >}}

動的な数式のマーカーでは、「-1」は、除算操作に設定されるB列とC列への現在の行へのオフセットを示し、スキップパラメーターは1行です。さらに、以下の文字を指定する必要があります:

{{< highlight java >}}

 "~"

{{< /highlight >}}

動的な数式で追加のパラメーターを適用するための区切り文字。

次のスクリーンショットは、繰り返しの動的な数式とその結果のExcelワークシートを示しています。

|**テンプレートファイル**|**出力ファイル**|
| :- | :- |
|![todo:image_alt_text](using-smart-markers_3.jpg)|![todo:image_alt_text](using-smart-markers_4.jpg)|
セル"C1"には、式**= A1*B1**が含まれ、セル"C2"には**= A2*B2**、セル"C3"には**= A3*B3**が含まれています。

スマートマーカーの処理は非常に簡単です。 次の例コードは、スマートマーカーで動的式を使用する方法を示しています。 [テンプレートファイル](templateDynamicFormulas.xlsx)を読み込んでテストデータを作成し、マーカーを処理してセルにデータを埋めます。 

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-DynamicFormulas-1.cs" >}}

## **変数配列を使用する**
次の例のコードは、スマートマーカーで可変配列を使用する方法を示しています。ワークブックの最初のワークシートのA1セルに可変配列マーカーを配置し、そのマーカーの値を設定し、マーカーに対してデータを埋めるように処理します。最後にExcelファイルを保存します。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-UsingVariableArray-1.cs" >}}
## **データのグループ化**
Excelの報告書では、データをグループ化して読みやすくし、分析しやすくする必要があることがあります。データをグループに分割する主な目的の1つは、各レコードのグループごとに計算（集計演算）を実行することです。

Aspose.Cellsのスマートマーカーを使用すると、フィールドごとにデータをグループ化し、データセットまたはデータグループの間にサマリーレコードを配置することができます。たとえば、Customers.CustomerIDでデータをグループ化する場合、グループが変わるたびにサマリーレコードを追加できます。
### **パラメータ**
次に、データのグループ化に使用されるスマートマーカーパラメータをいくつか紹介します。
#### **group:normal/merge/repeat**
選択できる3種類のグループをサポートしています。

- **normal** - グループ化フィールドの値が対応する列のレコードで繰り返されず、代わりに各データグループごとに一度だけ印刷されます。
- **merge** - normalパラメータと同様の動作ですが、グループ化フィールドのセルを各グループセットごとにマージします。
- **repeat** - グループ化フィールドの値が対応するレコードで繰り返されます。

例: &=Customers.CustomerID(group:merge)
#### **skip**
指定した数の行を各グループの後にスキップします。

例えば、&=Employees.EmployeeID(group:normal,skip:1)
#### **subtotalN**
グループ化フィールドに関連する指定されたフィールドデータの集計操作を実行します。Nは、データリスト内の小計を計算する際に使用される関数を1から11までの数字で指定します（1=AVERAGE, 2=COUNT, 3=COUNTA, 4=MAX, 5=MIN, ... 9=SUM など）。詳細については、Microsoft Excelのヘルプの小計リファレンスを参照してください。

実際のフォーマットは次のようになります:
subtotalN:Ref ここで、Refはグループ化する列を意味します。

例:

- &=Products.Units(subtotal9:Products.ProductID) は**Units**フィールドに対して**Products**テーブルの**ProductID**フィールドに関連して要約関数を指定します。
- &=Tabx.Col3(subtotal9:Tabx.Col1) は**Col3**フィールドを**Col1**でグループ化する際に要約関数を指定します。
- &=Table1.ColumnD(subtotal9:Table1.ColumnA&Table1.ColumnB) は、**Table1** テーブル内の **ColumnA** および **ColumnB** でグループ化した **ColumnD** フィールドに対する集計関数を指定します。

この例では、グルーピングパラメータのいくつかを実演しています。Microsoft AccessデータベースのNorthwind.mdbを使用し、「Order Details」という名前のテーブルからデータを抽出します。Microsoft ExcelでSmartMarker_Designer.xlsという名前の設計ファイルを作成し、ワークシートのさまざまなセルにスマートマーカーを配置します。マーカーはワークシートを埋めるように処理されます。データはグループフィールドによって配置および整理されます。

設計ファイルには2つのワークシートがあります。1番目のワークシートには、以下のスクリーンショットに示すように、グルーピングパラメータを持つスマートマーカーを配置します。3つのスマートマーカー（グルーピングパラメータを持つ）が配置されます：
&=[Order Details].OrderID(group:merge,skip:1),
&=[Order Details].Quantity(subtotal9:Order Details.OrderID)、および
&=[Order Details].UnitPrice(subtotal9:Order Details.OrderID) がそれぞれ A5、B5、C5 に入ります。

|**SmartMarker_Designer.xlsファイル内の1つ目のワークシート、すべてのスマートマーカーを備えたワークシート**|
| :- |
|![todo:image_alt_text](using-smart-markers_5.png)|
デザイナーファイルの2番目のワークシートでは、以下の図に示すように、さらなるスマートマーカーが配置されます。次のスマートマーカーを配置します:
&=[Order Details].OrderID(group:normal),
&=[Order Details].Quantity,
&=[Order Details].UnitPrice,
&=&=B(r)*C(r)、および
&=subtotal9:Order Details.OrderID それぞれ A5、B5、C5、D5、C6 に入ります。

|**スマートマーカー設計者.xlsファイルの2番目のワークシート、混在したスマートマーカー**|
| :- |
|![todo:image_alt_text](using-smart-markers_6.png)|
こちらが例で使用されたソースコードです。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-GroupingData-1.cs" >}}

{{% alert color="primary" %}} 

合計行に独自のカスタムラベルを追加したり、フィールド名をラベルと結合したい場合は、"Subtotal of Orders"のように、Aspose.CellsではLabelおよびLabelPosition属性を提供しているため、グループ化されたデータ内のSubtotal行にカスタムラベルを配置することができます。詳細については、Smart MarkersのSubtotal行と連結するためのカスタムラベルの追加方法に関するドキュメントを参照してください。

{{% /alert %}} 
## **匿名型またはカスタムオブジェクトの使用**
Aspose.Cellsでは、スマートマーカー内で匿名型またはカスタムオブジェクトもサポートしています。以下の例では、これがどのように機能するかを示しています。スマートマーカーを使用して動的オブジェクトからデータをインポートする場合は、次の記事を参照してください：

[動的オブジェクトをデータソースとしてインポートする](/cells/ja/net/import-data-into-worksheet/#importdataintoworksheet-importingfromdynamicobjectasdatasource)



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-UsingAnonymousTypes-1.cs" >}}
## **イメージマーカー**
Aspose.Cellsのスマートマーカーでは画像マーカーもサポートされています。このセクションでは、スマートマーカーを使用して画像を挿入する方法を示します。
### **画像パラメータ**
画像を操作するためのスマートマーカーのパラメータ。

- **Picture:FitToCell** - 画像をセルの行の高さと列の幅に自動調整します。
- **Picture:ScaleN** - 高さと幅をNパーセントにスケーリングします。
- **Picture:Width:Nin&Height:Nin** - 画像を高さNインチ、幅Nインチでレンダリングします。LeftとTopの位置（ポイント単位）も指定できます。

こちらが例で使用されたソースコードです。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-ImageMarkers-1.cs" >}}
## **ネストされたオブジェクトの使用**
Aspose.Cellsはスマートマーカーでネストされたオブジェクトをサポートし、ネストされたオブジェクトはシンプルである必要があります。単純なテンプレートファイルを使用します。一部のネストされたスマートマーカーを含むデザイナースプレッドシートを参照してください。

|**SM_NestedObjects.xlsxファイルの最初のワークシートには、ネストされたスマートマーカーが表示されています。**|
| :- |
|![todo:image_alt_text](using-smart-markers_7.png)|
以下の例は、これがどのように動作するかを示しています。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-UsingNestedObjects-1.cs" >}}

## **JSONデータの使用**
Aspose.CellsはスマートマーカーでJSONデータをサポートします。JSONデータは階層的にネスト可能です。[テンプレートファイル](smartmarker.xlsx)、[JSONファイル](smartmarker.json)、および以下のコードで生成された出力Excelファイルのスクリーンショットを確認してください。

|**smartmarker.xlsxファイルの最初のワークシートにスマートマーカーを表示**|
| :- |
|![todo:image_alt_text](jsontemplate.png)|

|**出力Excelファイルのスクリーンショット**|
| :- |
|![todo:image_alt_text](jsonresult.png)|

以下はJSONデータです：
```json data
{
    "EntityCin" : "EntityCin Test",
    "EntityName" : "EntityName Test",
    "FirstName" : "FirstName Test",
    "MiddleName" : "MiddleName Test",
    "LastName" : "LastName Test",
    "DOB" : "2025-02-08",
    "SSN" : "11111111",
    "Directors" : [
        {
            "id" : "director id 1",
            "FirstName" : "director first 1",
            "MiddleName" : "director middle 1",
            "LastName" : "director last 1",
            "Reportees" : [
                {
                    "id" : "aaa",
                    "FirstName" : "first aaa",
                    "MiddleName" : "middle aaa",
                    "LastName" : "last aaa",
                    "Department" : "aaa department",
                    "City" : "aaa city",
                    "GST" : "Yes",
                    "ITR" : "No"
                },
                {
                    "id" : "bbb",
                    "FirstName" : "first bbb",
                    "MiddleName" : "middle bbb",
                    "LastName" : "last bbb",
                    "Department" : "bbb department",
                    "City" : "bbb city",
                    "GST" : "Yes",
                    "ITR" : "Yes"
                },
                {
                    "id" : "ccc",
                    "FirstName" : "first ccc",
                    "MiddleName" : "middle ccc",
                    "LastName" : "last ccc",
                    "Department" : "ccc department",
                    "City" : "ccc city",
                    "GST" : "No",
                    "ITR" : "No"
                }
            ]
        },
        {
            "id" : "director id 2",
            "FirstName" : "director first 2",
            "MiddleName" : "director middle 2",
            "LastName" : "director last 2",
            "Reportees" : [
                {
                    "id" : "eee",
                    "FirstName" : "first eee",
                    "MiddleName" : "middle eee",
                    "LastName" : "last eee",
                    "Department" : "eee department",
                    "City" : "eee city",
                    "GST" : "Yes",
                    "ITR" : "No"
                },
                {
                    "id" : "fff",
                    "FirstName" : "first fff",
                    "MiddleName" : "middle fff",
                    "LastName" : "last fff",
                    "Department" : "fff department",
                    "City" : "fff city",
                    "GST" : "No",
                    "ITR" : "No"
                }
            ]
        }
    ]
}
```
以下の例は、これがどのように動作するかを示しています。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "SmartMarkers-Using-JSON-Data.cs" >}}

## **ネストされたオブジェクトとしてのジェネリックリストの使用**
Aspose.Cellsは今やネストオブジェクトとして一般的なリストの使用もサポートしています。以下のコードで生成された出力エクセルファイルのスクリーンショットをご確認ください。スクリーンショットでは、Teacherオブジェクトが複数のネストされたStudentオブジェクトを含んでいるのが確認できます。

|![todo:image_alt_text](using-smart-markers_8.png)|
| :- |

{{< gist  "aspose-com-gists" "24a8eac23c3325e20dababecf735a43b" "Examples-CSharp-SmartMarkers-UsingGenericList-1.cs" >}}
## **スマートマーカーのHTMLプロパティの使用**
The following sample code explains the use of HTML property of the Smart Markers. When it will be processed, it will show "World" in "Hello World" as bold because of HTML <b> tag.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-UsingHTMLProperty-1.cs" >}}

## **一行ごとではなく**
現在のデフォルトの処理方法は、スマートマーカーを行ごとに処理することです。しかし、データテーブルの同じスマートマーカーを、行が同じであるかどうかに関係なく一緒に処理する必要がある場合は、処理を呼び出す前に名前付き範囲"_CellsSmartMarkers"を指定し、WorkbookDesigner.LineByLineをfalseに指定する必要があります。 
スマートマーカーと一緒にデータをマージする際の通知の取得

|![todo:image_alt_text](using-smart-markers_11.png)|

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-LayerByLayer.cs" >}}

## **スマートマーカーを使用してデータをマージする際の通知の取得**
スマートマーカーに匿名またはカスタムオブジェクトを追加する

## **高度なトピック**
- [データが大きすぎる場合は、他のワークシートにスマートマーカーデータを自動ポピュレートする](/cells/ja/net/adding-anonymous-or-custom-object-into-smartmarkers/)
- [データが大きすぎる場合、他のワークシートにスマートマーカーデータを自動的に埋め込む](/cells/ja/net/auto-populate-smart-marker-data-to-other-worksheets-if-data-is-too-large/)
- [スマートマーカーのフォーマット](/cells/ja/net/formatting-smart-markers/)
- [スマートマーカーを使用してデータをマージする際の通知の取得](/cells/ja/net/getting-notifications-while-merging-data-with-smart-markers/)
- [WorkbookDesignerにカスタムのDataSourceを設定](/cells/ja/net/set-custom-datasource-for-workbookdesigner/)
- [セル内の先頭アポストロフィを表示する](/cells/ja/net/show-leading-apostrophe-in-cells/)
- [Smart MarkerフィールドでFormulaパラメータを使用](/cells/ja/net/using-formula-parameter-in-smart-marker-field/)
- [Smart Markersでデータをグループ化する際に画像マーカーを使用する](/cells/ja/net/using-image-markers-while-grouping-data-in-smart-markers/)


{{< app/cells/assistant language="csharp" >}}
