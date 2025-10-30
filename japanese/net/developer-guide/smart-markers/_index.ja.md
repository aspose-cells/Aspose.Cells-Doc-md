---
title: スマートマーカーでデータを賢くインポートおよび配置
linktitle: スマートマーカー
type: docs
weight: 190
url: /ja/net/using-smart-markers/
description: Aspose.Cellsライブラリを使用して、テンプレートExcelファイルに従ってデータをスマートにインポートおよび配置する。
---

## **なぜスマートマーカーでExcelにデータをインポートするのか**
スマートマーカーを使用してExcelにデータをインポートすることは、テンプレートベースの設計と動的なデータバインディングを組み合わせることで、データ統合を合理化します。このアプローチは、テンプレート内のマーカーがプレースホルダーとして機能し、多様なソースからデータを自動的に埋め込むAspose.Cellsのようなツールで特に価値があります。以下に主要な理由を示します。

1. 繰り返しレポートの効率化：テンプレートの再利用性、埋め込みマーカー（例：&=$VariableName、&=DataSource.Field）を持つExcelテンプレートは複数のデータセットに渡って再利用でき、手動の再フォーマットを排除します。例えば、財務レポートや在庫シートは、データソースを更新するだけでレイアウトの再構築は不要です。自動データバインディング、スマートマーカーは直接データソース（例：データベース、JavaBeans、配列）にリンクします。ソースデータの変更は処理後に自動的にExcel出力に反映され、コピーミスを減らします。

2. 複雑なデータ構造への対応：複数ソースの統合、単一テンプレートでさまざまなソース（例：変数、配列、ResultSet）をマージ可能です。階層化されたデータ処理、ネストされたデータ（例：グループ化されたレコード）は、 &=subtotal9:Person.id などのマーカーを使用して、Excel内で直接集計（合計、平均）を行えます。

3. Excelの機能保持：スマートマーカーは、Excelの計算式、条件付き書式、チャートなどと共存可能です。例えば：&==C{r}*D{r}を使用した動的計算は、行ごとの数式をデータ挿入時に適用します。テンプレートは、見出しやセルの色などの事前定義されたスタイルを維持し、インポート後の調整を不要にします。

4. 高度な自動化機能：カスタムデータソースの連携、開発者は.NETのICellsDataTableのようなインターフェースを実装して、独自のデータ構造とマーカーをマッピングできます。この柔軟性により、APIやセンサーからのリアルタイムデータの処理も可能です。バッチ処理、Aspose.CellsのWorkbookDesignerなどのツールは、大量の操作（例：1,000以上の請求書を一度に生成）をデータのループによって実行できます。

5. 開発・保守の負荷低減：ロジックとデザインの分離、デザイナーはExcelでテンプレートを管理（コーディング不要）、開発者はデータロジックを担当します。この分離により、反復作業が高速化されます。エラーの削減、データの自動マッピングは手動入力のリスクを最小化します。例えば、VC++で分析されたセンサーデータは、オブジェクトインターフェースを介してExcelテンプレートに自動入力でき、入力ミスを避けられます。

## **Smart Markersを使用したDataTableインポートのサンプルコード**
以下のサンプルコードには6件のレコードがあり、そのうち3件だけを1つのシートに表示し、残りは自動的に2番目のシートに移動します。2つのシートとも同じスマートマーカータグを持っている必要があり、両方のシートに[WorkbookDesigner.Process(sheetIndex, isPreserved)](https://reference.aspose.com/cells/net/aspose.cells.workbookdesigner/process/methods/2)メソッドを呼び出してください。サンプル出力のExcelファイル](SmartMarkerDataTableToExcel.xlsx)を参考にしてください。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "SmartMarkers-ImportDataTableToExcel.cs" >}}

## **スマートマーカーを使用したJSONデータのインポートサンプルコード**
Aspose.Cells for .NETはスマートマーカーにおいてJSONデータをサポートしています。サンプルコードはテーブルテンプレートを読み込み、インテリジェントにJSONデータをインポートしてテーブルデータを計算します。以下のコードで生成された出力Excelファイルの[テンプレートファイル](table.xlsx)、[JSONファイル](table.json)、およびスクリーンショットを確認してください。

|**table.xlsxファイルの最初のワークシートにスマートマーカーが表示されている例です。**|
| :- |
|![todo:image_alt_text](tabletemplate.png)|

|**出力Excelファイルのスクリーンショット**|
| :- |
|![todo:image_alt_text](tableresult.png)|

以下はJSONデータです：
```json data
{
	"Items" : [
		{
			"ItemName" : "A123",
			"Description" : "Peonies",
			"Qty" : "55",
			"UnitPrice" : "3.05"			
		},
		{
			"ItemName" : "B456",
			"Description" : "Tulips",
			"Qty" : "45",
			"UnitPrice" : "2.66",
		},
		{
			"ItemName" : "K789",
			"Description" : "Buttercup",
			"Qty" : "68",
			"UnitPrice" : "8.35",
		}
	]
}
```
以下の例は、これがどのように動作するかを示しています。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "SmartMarkers-ImportJsonToTable.cs" >}}

## **スマートマーカーを用いたネストされたオブジェクトのインポートサンプルコード**
Aspose.Cellsはスマートマーカーでネストされたオブジェクトをサポートし、ネストされたオブジェクトはシンプルである必要があります。単純なテンプレートファイルを使用します。一部のネストされたスマートマーカーを含むデザイナースプレッドシートを参照してください。

|**SM_NestedObjects.xlsxファイルの最初のワークシートには、ネストされたスマートマーカーが表示されています。**|
| :- |
|![todo:image_alt_text](using-smart-markers_7.png)|
以下の例は、これがどのように動作するかを示しています。


{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-UsingNestedObjects-1.cs" >}}


## **高度なトピック**
- [スマートマーカーのパラメーター](/cells/ja/net/smart-marker-parameters/)
- [データが大きすぎる場合は、他のワークシートにスマートマーカーデータを自動ポピュレートする](/cells/ja/net/adding-anonymous-or-custom-object-into-smartmarkers/)
- [データが大きすぎる場合、他のワークシートにスマートマーカーデータを自動的に埋め込む](/cells/ja/net/auto-populate-smart-marker-data-to-other-worksheets-if-data-is-too-large/)
- [スマートマーカーのフォーマット](/cells/ja/net/formatting-smart-markers/)
- [スマートマーカーを使用してデータをマージする際の通知の取得](/cells/ja/net/getting-notifications-while-merging-data-with-smart-markers/)
- [WorkbookDesignerにカスタムのDataSourceを設定](/cells/ja/net/set-custom-datasource-for-workbookdesigner/)
- [セル内の先頭アポストロフィを表示する](/cells/ja/net/show-leading-apostrophe-in-cells/)
- [Smart MarkerフィールドでFormulaパラメータを使用](/cells/ja/net/using-formula-parameter-in-smart-marker-field/)
- [スマートマーカーを使ったインデックスによる配列要素のExcelへのインポート例](/cells/ja/net/how-to-import-array-element-by-index-with-smart-markers/)
- [スマートマーカーを使ったスライサーによる配列要素のExcelへのインポート例](/cells/ja/net/how-to-import-array-element-by-slicer-with-smart-markers/)
- [スマートマーカーを使ったJSONのExcelへのインポート例](/cells/ja/net/how-to-import-json-into-excel-with-smart-markers/)
- [スマートマーカーを使ったネストされたオブジェクトのExcelへのインポート例](/cells/ja/net/how-to-import-nested-objects-with-smart-markers/)
- [スマートマーカーを使った変動する配列のExcelへのインポート例](/cells/ja/net/how-to-import-variable-arrays-with-smart-markers/)
- [Smart Markersを使用した画像マーカーの使い方](/cells/ja/net/how-to-use-image-markers-in-smart-markers/)
- [Smart Markersでデータをグループ化する方法](/cells/ja/net/how-to-group-data-in-smart-markers/)

{{< app/cells/assistant language="csharp" >}}
