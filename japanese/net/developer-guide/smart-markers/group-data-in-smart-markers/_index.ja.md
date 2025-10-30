---
title: Smart Markersでデータをグループ化する方法
type: docs
weight: 30
url: /ja/net/how-to-group-data-in-smart-markers/
---

## **可能な使用シナリオ**
Excelの報告書では、データをグループ化して読みやすくし、分析しやすくする必要があることがあります。データをグループに分割する主な目的の1つは、各レコードのグループごとに計算（集計演算）を実行することです。

Aspose.Cellsのスマートマーカーを使用すると、フィールドごとにデータをグループ化し、データセットまたはデータグループの間にサマリーレコードを配置することができます。たとえば、Customers.CustomerIDでデータをグループ化する場合、グループが変わるたびにサマリーレコードを追加できます。

## **Smart Markersにおけるグループ化パラメータ**
次に、データのグループ化に使用されるスマートマーカーパラメータをいくつか紹介します。
### **group:normal/merge/repeat**
選択できる3種類のグループをサポートしています。

- **normal** - グループ化フィールドの値が対応する列のレコードで繰り返されず、代わりに各データグループごとに一度だけ印刷されます。
- **merge** - normalパラメータと同様の動作ですが、グループ化フィールドのセルを各グループセットごとにマージします。
- **repeat** - グループ化フィールドの値が対応するレコードで繰り返されます。

例: &=Customers.CustomerID(group:merge)
### **skip**
指定した数の行を各グループの後にスキップします。

例えば、&=Employees.EmployeeID(group:normal,skip:1)
### **subtotalN**
グループ化フィールドに関連する指定されたフィールドデータの集計操作を実行します。Nは、データリスト内の小計を計算する際に使用される関数を1から11までの数字で指定します（1=AVERAGE, 2=COUNT, 3=COUNTA, 4=MAX, 5=MIN, ... 9=SUM など）。詳細については、Microsoft Excelのヘルプの小計リファレンスを参照してください。

実際のフォーマットは次のようになります:
subtotalN:Ref ここで、Refはグループ化する列を意味します。

例:

- &=Products.Units(subtotal9:Products.ProductID) は**Units**フィールドに対して**Products**テーブルの**ProductID**フィールドに関連して要約関数を指定します。
- &=Tabx.Col3(subtotal9:Tabx.Col1) は**Col3**フィールドを**Col1**でグループ化する際に要約関数を指定します。
- &=Table1.ColumnD(subtotal9:Table1.ColumnA&Table1.ColumnB) は、**Table1** テーブル内の **ColumnA** および **ColumnB** でグループ化した **ColumnD** フィールドに対する集計関数を指定します。

## **Smart Markersでデータをグループ化する方法**

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
