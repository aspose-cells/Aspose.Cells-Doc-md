---
title: 設定パラメータ
type: docs
weight: 10
url: /ja/jasperreports/configuration-parameters/
---

{{% alert color="primary" %}} 

次の表には、設定パラメータが一覧されています。 

{{% /alert %}} 

|**パラメータ名**|**説明**|
| :- | :- |
|FORMAT_TYPE |「EXCEL97TO2003」または「EXCEL2007」に設定して、Microsoft Excel 79 0 2003またはExcel 2007形式のファイルを生成できます。
|IS_ONE_PAGE_PER_SHEET |各レポートページを別のXLSワークシートに書き込むかどうかを指定するブール値。
|IS_REMOVE_EMPTY_SPACE_BETWEEN_ROWS |行間に現れる空白を削除するかどうかを指定するブール値。
|IS_REMOVE_EMPTY_SPACE_BETWEEN_COLUMNS |列間に現れる空白を削除するかどうかを指定するブール値。
|IS_WHITE_PAGE_BACKGROUND |ページの背景色を白またはデフォルトのXLS背景色に設定するかどうかを指定するブール値。XLSの背景色は、XLSビューアのプロパティやオペレーティングシステムの色のスキームによって異なる場合があります。
|IS_DETECT_CELL_TYPE |エクスポータが元のテキストフィールド式のタイプを考慮してセルの型と値を設定するかどうかを示すフラグ。
|SHEET_NAMES |カスタムシート名を表す文字列の配列。IS_ONE_PAGE_PER_SHEETパラメータと併用すると便利です。
|IS_FONT_SIZE_FIX_ENABLED |指定したセルの高さにテキストが収まるようにフォントサイズを縮小するフラグ。
|MAXIMUM_ROWS_PER_SHEET |シートに表示できる最大行数を指定する整数値。設定された場合、残りの行を表示するために新しいシートが作成されます。負の値またはゼロの場合、制限が設定されていないことを意味します。
|IS_IGNORE_GRAPHICS |グラフィカル要素を無視し、テキスト要素のみをエクスポートするためのフラグ。
|IS_COLLAPSE_ROW_SPAN |行の結合を折りたたんでセルを行間で結合しないフラグ。
|IS_IGNORE_CELL_BORDER |セルの境界線を無視するフラグ。
|IS_USE_EXCEL_CHART |静的な画像ではなく、Microsoft Excel形式の編集可能なチャートを使用するフラグ。デフォルト値はtrueです。

