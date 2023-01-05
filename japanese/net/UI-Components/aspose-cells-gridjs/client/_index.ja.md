---
title: GridJs クライアント側での作業
type: docs
weight: 250
url: /ja/net/aspose-cells-gridjs/client/
---
# GridJs クライアント側での作業
に基づいてGridJsクライアントを開発しました[x-スプレッドシート](https://github.com/myliang/x-spreadsheet).

## 主な手順は次のとおりです。

- x_spreadsheet インスタンスを作成する
```javascript
xs = x_spreadsheet(id, options)
```
- json データを読み込む
```javascript
xs.loadData(jsondata.data)
```
- アクティブシートを設定
```javascript
xs.setActiveSheetByName(jsondata.actname)
```
- アクティブセルを設定
```javascript
xs.setActiveCell(jsondata.actrow,jsondata.actcol);
```

たとえば、次のコードは x_spreadsheet オブジェクトを初期化します。
```javascript
 xs = x_spreadsheet('#gridjs-demo', {
			updateMode:'server',
			updateUrl:'/GridJs2/UpdateCell',
			mode: 'edit',
			showToolbar: true,
                        local: 'en',
            showContextmenu: true
        }).loadData(sheets)
```
 // オプションのパラメータ:
 updateMode: 現在、「サーバー」のみをサポートしています
updateUrl: json に基づいて更新アクションのサーバー側 URL を設定します
mode: read は readonly スプレッド シートを意味し、edit はスプレッド シートを編集できることを意味します。
 showToolbar: ツールバーを表示するかどうかを意味します
showFileName: ファイル名を表示するかどうか
ローカル: メニューの複数の言語をサポートします。ロケールは次のとおりです: en、cn、es、pt、de、ru、nl (英語、中国語、スペイン語、ポルトガル語、ドイツ、ロシア語、オランダ語)
 showContextmenu: セルを右クリックしたときにコンテキストメニューを表示するかどうかを意味します
## 

___
## その他の便利な API
- ビューをレンダリングする
```javascript
xs.reRender()
```
- 選択した画像/形状を取得します。何も選択しない場合、null が返されます
```javascript
xs.sheet.selector.getObj()
```

- セル オブジェクトを取得する
```javascript
xs.sheet.data.getCell(ri,ci)
    // the parameters are:
    ri:row index 
	ci:column index
```
- セル スタイルを取得する
```javascript
xs.sheet.data.getCellStyle(ri,ci)
    // the parameters are:
    ri:row index 
	ci:column index
```
- セル値を設定する
```javascript
xs.sheet.data.setCellText(ri,ci,value,state)
    // the parameters are:
    ri:row index 
	ci:column index
	value:the cell value
	state: input | finished
```

- 選択したセル範囲を取得/設定します
```javascript
xs.sheet.data.selector.range
```
- 選択したセルまたはセル領域のセル値を設定します
```javascript
xs.sheet.data.setSelectedCellText(value)
    // the parameters are:
	value:the  value for the cell
```
- 選択したセルまたはセル領域のスタイルを設定する
```javascript
xs.sheet.data.setSelectedCellAttr(attributename,value)
    // the parameters are:
    attributename:font-name | font-bold | font-italic | font-size  | format|border|merge|formula |strike|textwrap |underline |align |valign |color|bgcolor|pattern
	value:the  value for the attribute
```

- 選択したセル領域を結合
```javascript
xs.sheet.data.merge()
```

- 選択したセル領域の結合を解除
```javascript
xs.sheet.data.unmerge()
```
- 選択したセルを削除
```javascript
xs.sheet.data.deleteCell(what)
    // the parameters are:
    what:all|format  all: means delete the cell and clear the style ;format means delete the cell value and keep the cell style
```
- フリーズ ペインを設定する
```javascript
xs.sheet.data.setFreeze(ri,ci)
    // the parameters are:
    ri:row index 
	ci:column index
```

- 選択したセルに行または列を挿入する
```javascript
xs.sheet.data.insert(type, n)
    // the parameters are:
    type: row | column
	n:the row or column number
```
- 選択したセルの行または列を削除する
```javascript
xs.sheet.data.delete(type)
    // the parameters are:
    type: row | column
```

- 列の幅を設定します
```javascript
xs.sheet.data.setColWidth(ci,width)
    // the parameters are:
    ci:column index
	width:the width for the column
```
- 列の幅を取得します
```javascript
xs.sheet.data.cols.sumWidth(min,max)
    // the parameters are:
    min:the start column index
	max:the end column index,not include
```

- 行の高さを設定します
```javascript
xs.sheet.data.setRowHeight(ri,height)
    // the parameters are:
    ri:row index
	height:the height for the row
```
- 行の高さを取得します
```javascript
xs.sheet.data.rows.sumHeight(min,max)
    // the parameters are:
    min:the start row index
	max:the end row index,not include
```
- 表示方向を取得/設定します
```javascript
xs.sheet.data.displayRight2Left
```



詳細情報については、ここで例を確認できます
<https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Examples_GridJs>



 
 
