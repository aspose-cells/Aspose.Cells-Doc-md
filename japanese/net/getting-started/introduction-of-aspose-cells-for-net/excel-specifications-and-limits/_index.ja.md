---
title: Excelの仕様と制限
type: docs
weight: 40
url: /ja/net/excel-specifications-and-limits/
description: この記事では、すべてのワークブック、ワークシート、および機能の仕様と制限を見つけます。Excel 2010では、ワークシートの最大サイズは1,048,576行×16,384列です。
keywords: Excelの仕様と制限、計算仕様と制限、チャート作成仕様と制限、ピボットテーブルおよびピボットチャートレポートの仕様と制限
---

## **新しいバージョンのExcelの仕様と制限**
ワークシートおよびブック仕様と制限
|**機能**|**最大制限**|
| :- | :- |
|開いているブック|利用可能なメモリとシステムリソースによって制限されます
|ワークシート上の行と列の総数|1,048,576行×16,384列
|列の幅|255文字
|行の高さ|409ポイント
|改ページ|1,026水平および垂直
|セルに含めることができる全文字数|32,767文字
|ヘッダーまたはフッターの文字数|255
|セルごとの最大改行数|253
|ワークブック内のシート|利用可能なメモリによって制限されます（デフォルトは1シート）
|ブック内の色|1,600万色（24ビットカラースペクトラムの32ビットへの完全アクセス）
|ブック内の名前付きビュー|利用可能なメモリによって制限されます
|ユニークセル形式/セルスタイル|65,490
|塗りつぶしスタイル|256
|線の太さとスタイル|256
|ユニークフォントタイプ|使用可能なグローバルフォントが1,024；ワークブックごとに512
|ワークブック内の数値書式|言語バージョンによって200〜250の間
|ワークブック内の名前|利用可能なメモリによって制限されます
|ワークブック内のウィンドウ|利用可能なメモリによって制限されます
|ワークシート内のハイパーリンク|65,530
|ウィンドウ内の分割|4
|リンクされたシート|利用可能なメモリによって制限されます
|Scenarios|使用可能なメモリに制限されます。サマリーレポートは最初の251シナリオのみを表示します
|シナリオで変更可能なセル|32
|Solverで調整可能なセル|200
|カスタム関数|利用可能なメモリによって制限されます
|ズーム範囲|10%から400%
|レポート|利用可能なメモリによって制限されます
|参照をソートする|単一のソートで64個; 連続したソートを使用すると無制限
|元に戻すレベル|100
|データ形式内のフィールド|32
|ワークブックのパラメータ|ワークブックごとに255個のパラメータ
|フィルタのドロップダウンリストに表示される項目|10,000
|選択可能な非連続セル数|2,147,483,648個
|データモデルワークブックのメモリストレージとファイルサイズの最大制限|32ビット環境では仮想アドレススペースが2ギガバイト（GB）に制限され、Excel、ワークブック、および同じプロセスで実行されるアドインで共有される。データモデルのアドレススペースのシェアは500MB〜700MBになる場合がありますが、他のデータモデルやアドインがロードされているとさらに少なくなることがあります。64ビット環境ではファイルサイズに厳密な制限はありません。ワークブックのサイズは利用可能なメモリとシステムリソースによってのみ制限されます。Excel 2016以降、32ビットExcelは64ビットWindowsオペレーティングシステムで作業を行う際にメモリを2倍消費するようにするLarge Address Aware機能が利用できます。
|プロセッサコア|64
|ファイル名の長さ|218文字 - ファイルパスを含む。例：C:\ユーザー名\ドキュメント\ファイル名.xlsx。

## **Office 2010のExcel仕様と制限**
ワークシートおよびブック仕様と制限
|**機能**|**最大制限**|
| :- | :- |
|開いているブック|利用可能なメモリとシステムリソースによって制限されます
|ワークシート上の行と列の総数|1,048,576行×16,384列
|列の幅|255文字
|行の高さ|409ポイント
|改ページ|1,026水平および垂直
|セルに含めることができる全文字数|32,767文字
|ヘッダーまたはフッターの文字数|255
|セルごとの最大改行数|253
|ブック内のシート|利用可能なメモリによって制限されます（デフォルトは3シート）
|ブック内の色|1,600万色（24ビットカラースペクトラムの32ビットへの完全アクセス）
|ブック内の名前付きビュー|利用可能なメモリによって制限されます
|ユニークセル形式/セルスタイル|65,490
|塗りつぶしスタイル|256
|線の太さとスタイル|256
|ユニークフォントタイプ|使用可能なグローバルフォントが1,024；ワークブックごとに512
|ワークブック内の数値書式|言語バージョンによって200〜250の間
|ワークブック内の名前|利用可能なメモリによって制限されます
|ワークブック内のウィンドウ|利用可能なメモリによって制限されます
|ワークシート内のハイパーリンク|65,530個
|ウィンドウ内の分割|4
|リンクされたシート|利用可能なメモリによって制限されます
|Scenarios|使用可能なメモリに制限されます。サマリーレポートは最初の251シナリオのみを表示します
|シナリオで変更可能なセル|32
|Solverで調整可能なセル|200
|カスタム関数|利用可能なメモリによって制限されます
|ズーム範囲|10%から400%
|レポート|利用可能なメモリによって制限されます
|参照をソートする|単一のソートで64個; 連続したソートを使用すると無制限
|元に戻すレベル|100
|データ形式内のフィールド|32
|ワークブックのパラメータ|ワークブックごとに255個のパラメータ
|フィルタのドロップダウンリストに表示される項目|10,000
|選択可能な非連続セル数|2,147,483,648個
|プロセッサコア|64

## **Office 2007のExcel仕様と制限**
ワークシートおよびブック仕様と制限
|**機能**|**最大制限**|
| :- | :- |
|開いているブック|利用可能なメモリとシステムリソースによって制限されます
|ワークシート上の行と列の総数|1,048,576行×16,384列
|列の幅|255文字
|行の高さ|409ポイント
|改ページ|1,026水平および垂直
|セルに含めることができる全文字数|32,767文字
|ヘッダーまたはフッターの文字数|255
|セルごとの最大改行数|253
|ブック内のシート|利用可能なメモリによって制限されます（デフォルトは3シート）
|ブック内の色|1,600万色（24ビットカラースペクトラムの32ビットへの完全アクセス）
|ブック内の名前付きビュー|利用可能なメモリによって制限されます
|ユニークセル形式/セルスタイル|65,490
|塗りつぶしスタイル|256
|線の太さとスタイル|256
|ユニークフォントタイプ|使用可能なグローバルフォントが1,024；ワークブックごとに512
|ワークブック内の数値書式|言語バージョンによって200〜250の間
|ワークブック内の名前|利用可能なメモリによって制限されます
|ワークブック内のウィンドウ|利用可能なメモリによって制限されます
|ワークシート内のハイパーリンク|65,530個
|ウィンドウ内の分割|4
|リンクされたシート|利用可能なメモリによって制限されます
|Scenarios|使用可能なメモリに制限されます。サマリーレポートは最初の251シナリオのみを表示します
|シナリオで変更可能なセル|32
|Solverで調整可能なセル|200
|カスタム関数|利用可能なメモリによって制限されます
|ズーム範囲|10%から400%
|レポート|利用可能なメモリによって制限されます
|参照をソートする|単一のソートで64個; 連続したソートを使用すると無制限
|元に戻すレベル|100
|データ形式内のフィールド|32
|ワークブックのパラメータ|ワークブックごとに255個のパラメータ
|フィルタ ドロップダウン リスト|10,000

## **計算仕様と制限**
|**機能**|**最大制限**|
| :- | :- |
|数字の精度|15桁
|許容される最小の負の数|-2.2251E-308
|許容される最小の正の数|2.2251E-308
|許容される最大の正の数|9.99999999999999E+307
|許容される最大の負の数|-9.99999999999999E+307
|数式を使用した場合の許容される最大の正の数|1.7976931348623158e+308
|数式を使用した場合の許容される最大の負の数|-1.7976931348623158e+308
|数式内容の長さ|8,192 文字
|数式の内部長さ|16,384 バイト
|反復|32,767
|ワークシートの配列|利用可能なメモリによる制限
|選択された範囲|2,048
|関数内の引数|255
|関数のネストレベル|64
|ユーザー定義関数のカテゴリ|255
|使用可能なワークシート関数の数|341
|オペランド スタックのサイズ|1,024
|クロスワークシート依存性|他のシートを参照できるワークシート数 64,000
|クロスワークシート配列式の依存性|利用可能なメモリによる制限
|エリア依存性|利用可能なメモリによる制限
|ワークシートごとのエリア依存性|利用可能なメモリによる制限
|単一セルへの依存|単一のセルに依存できる数式の最大数 40億
|閉じたワークブックからのリンクされたセルの内容の長さ|32,767
|計算のために許可される最も古い日付|1900年1月1日（1904年1月1日は、1904年日付システムが使用されている場合）
|計算のために許可される最新の日付|9999年12月31日
|入力できる最大の時間|9999:59:59

## **チャート仕様と制限**
|**機能**|**最大制限**|
| :- | :- |
|ワークシートにリンクされたチャート|利用可能なメモリによって制限
|チャートで参照されるワークシート|255
|1つのチャート内のデータ系列|255
|2次元チャートのデータ系列ごとのデータポイント|32,000
|3次元チャートのデータ系列ごとのデータポイント|4,000
|1つのチャート内のすべてのデータ系列のデータポイント|256,000

## **ピボットテーブルおよびピボットチャートレポートの仕様と制限**
|**機能**|**最大制限**|
| :- | :- |
|シート上のピボットテーブルレポート|利用可能なメモリによって制限
|フィールドごとのユニークなアイテム|1,048,576
|ピボットテーブルレポート内の行または列フィールド|利用可能なメモリによって制限
|ピボットテーブルレポート内のレポートフィルター|256（利用可能なメモリによって制限される場合がある）
|ピボットテーブルレポート内の値フィールド|256
|ピボットテーブルレポート内の計算されたアイテムの式|利用可能なメモリによって制限
|ピボットチャートレポート内のレポートフィルター|256（利用可能なメモリによって制限される場合がある）
|ピボットチャートレポート内の値フィールド|256
|ピボットチャートレポート内の計算されたアイテムの式|利用可能なメモリによって制限
|PivotTableアイテムのMDX名の長さ|32,767
|リレーショナルPivotTable文字列の長さ|32,767

## **「複数のユーザーによる変更を許可...」設定が有効になっているブック**
ブックで「複数のユーザーによる変更を許可...」設定がオンになっている場合、以下の情報が適用されます。この設定は、共有ブックを使用する場合に有効になります。

|**機能**|**最大制限**|
| :- | :- |
|同時にブックを開いて共有できるユーザー|256
|ブック内のパーソナルビュー|利用可能なメモリによって制限
|変更履歴が維持される日数|32,767（デフォルトは30日）
|一度にマージできるワークブック|使用可能なメモリによって制限されます
|ハイライトできるセル|32,767
|変更のハイライトがオンになっているときに異なるユーザーによって行われた変更を識別するために使用される色|32 (各ユーザーは別々の色で識別されます；現在のユーザーによる変更はネイビーブルーでハイライト表示されます)
|ワークブック内のExcelテーブル|0 (ゼロ) 注：1つ以上のExcelテーブルを含むワークブックは、複数のユーザーによる変更を許可する...設定を有効にすることはできません。
{{< app/cells/assistant language="csharp" >}}
