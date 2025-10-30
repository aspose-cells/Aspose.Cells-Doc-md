---
title: スマートマーカーを使ったマスターと詳細データのインポートをスマートに行う
type: docs
weight: 30
url: /ja/net/how-to-use-master-and-details-with-smart-markers/
---

## **可能な使用シナリオ**
時折、ダイナミックなExcelレポートを生成したい場合があります。これには、総合的なメインダッシュボードと複数の詳細ワークシートが含まれています。その中で、単一のメインテーブルは概要を表示し、さまざまな製品バリアントを示すことがあります。一つの対応する詳細ワークシートは、特定のバリアントの詳細で深堀りしたデータを提供します。Aspose.Cellsは、マスターと詳細をスマートマーカーで完璧にサポートします。


## **マスターと詳細のためのスマートマーカーのパラメータ**
Excelにマスターと詳細データをインポートするには、次のスマートマーカーのパラメータを使用する必要があります。

| パラメータ | 説明 | 許容値（構文） | 制約 | オプション性 | デフォルトの動作 | Excelの制約 |
| --- | --- | --- | --- | --- | --- | --- |
| `DetailSheet` | テンプレートファイル内の詳細ワークシートの名前を指定します。 | 文字列値 | 値はnullかワークシート名でなければなりません。nullの場合、これは詳細シートです。単純な文字列値であるべきです。変数はサポートされません。 | 省略された場合、マスターまたは詳細シートではありません。 | 通常のワークシート、マスターまたは詳細ではありません。 | |
| `DetailTable` | テンプレートファイル内の詳細ワークシートのテーブル名を指定します。 | 文字列値 | | 省略された場合、詳細シートのスマートマーカーはマスターシートに類似している必要があり、そうでなければデータソースが見つかりません。 | 省略された場合、詳細シートのスマートマーカーはマスターシートに類似している必要があります。さもなければデータソースを見つけられません。 | |
| `DetailSheetNewName` | 新しく作成される詳細ワークシートの名前を指定します。 | Excelの式のような表現 | 変数（({a.bc})）を簡単な値に置き換える場合、有効なExcelの式でなければなりません。 | 省略された場合、新しいシートはSheet1、Sheet2...になります。 | 省略された場合、新しいシートはSheet1、Sheet2...になります。 | 名前は有効なワークシート名でなければなりません。 |
| `DetailLink` | インポートされたデータの位置へのハイパーリンクを追加するかどうかを示します。 | | | 省略された場合、インポートされたデータの位置へのハイパーリンクは追加されません。 | 省略された場合、ハイパーリンクは追加されません。 | |

## **マスターと詳細が1つのワークシート内にある場合のマスターと詳細の使用方法**
時折、SmartMarkersでマスターと詳細データをExcelにインポートする必要があります。Aspose.Cellsは、スマートマーカーでマスターと詳細のパラメータを使用できるようにします。 [テンプレートファイル](MasterDetailInOneSheet.xlsx)、[JSONファイル](MasterDetailData.json)、および以下のコードで生成された出力Excelファイルのスクリーンショットを確認してください。

|**テンプレート.xlsxの最初のワークシート。**|
| :- |
|![todo:image_alt_text](1.png)|

|**出力Excelファイルの最初のワークシート。**|
| :- |
|![todo:image_alt_text](2.png)|

|**出力Excelファイルの2番目のワークシート。**|
| :- |
|![todo:image_alt_text](3.png)|

以下はJSONデータです：
```json data
{
	"node": {
		"Styles1": [
			{
				"StyleID": "1style001",
				"StyleName": "StyleName1",
				"Quantity": 6,
				"UnitPrice": 18.45,
				"MaterialType":"Cotton"
			}
		],
		"Styles2": [
			{
				"StyleID": "2style001",
				"StyleName": "Cotton StyleName2",
				"Quantity": 6,
				"UnitPrice": 18.45,
				"MaterialType":"Cotton"
			},
			{
				"StyleID": "2style002",
				"StyleName": "Denim StyleName2",
				"Quantity": 8,
				"UnitPrice": 58.8,
				"MaterialType":"Denim"
			}
		]
	}
}
```
以下の例は、これがどのように動作するかを示しています。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "SmartMarkers-Using-Master-Details-InOneSheet.cs" >}}

## **マスターと詳細が異なるワークシートにある場合のマスターと詳細の使用方法**
時折、SmartMarkersでマスターと詳細データをExcelにインポートする必要があります。Aspose.Cellsは、スマートマーカーでマスターと詳細のパラメータを使用できるようにします。 [テンプレートファイル](MasterDetailInTwoSheets.xlsx)、[JSONファイル](MasterDetailData.json)、および以下のコードで生成された出力Excelファイルのスクリーンショットを確認してください。

|**テンプレート.xlsxの最初のマスターワークシート。**|
| :- |
|![todo:image_alt_text](4.png)|

|**テンプレート.xlsxの二番目のマスターワークシート。**|
| :- |
|![todo:image_alt_text](5.png)|

|**テンプレート.xlsxの詳細ワークシート。**|
| :- |
|![todo:image_alt_text](6.png)|

|**出力Excelファイルの最初のマスターワークシート。**|
| :- |
|![todo:image_alt_text](7.png)|

|**出力Excelファイルの二番目のマスターワークシート。**|
| :- |
|![todo:image_alt_text](8.png)|

|**出力Excelファイルの最初のマスターワークシートの詳細ワークシート。**|
| :- |
|![todo:image_alt_text](9.png)|

|**出力Excelファイルの二番目のマスターワークシートの最初の詳細ワークシート。**|
| :- |
|![todo:image_alt_text](10.png)|

|**出力Excelファイルの二番目のマスターワークシートの二番目の詳細ワークシート。**|
| :- |
|![todo:image_alt_text](11.png)|

以下はJSONデータです：
```json data
{
	"node": {
		"Styles1": [
			{
				"StyleID": "1style001",
				"StyleName": "StyleName1",
				"Quantity": 6,
				"UnitPrice": 18.45,
				"MaterialType":"Cotton"
			}
		],
		"Styles2": [
			{
				"StyleID": "2style001",
				"StyleName": "Cotton StyleName2",
				"Quantity": 6,
				"UnitPrice": 18.45,
				"MaterialType":"Cotton"
			},
			{
				"StyleID": "2style002",
				"StyleName": "Denim StyleName2",
				"Quantity": 8,
				"UnitPrice": 58.8,
				"MaterialType":"Denim"
			}
		]
	}
}
```
以下の例は、これがどのように動作するかを示しています。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "SmartMarkers-Using-Master-Details-InDifferentSheets.cs" >}}
