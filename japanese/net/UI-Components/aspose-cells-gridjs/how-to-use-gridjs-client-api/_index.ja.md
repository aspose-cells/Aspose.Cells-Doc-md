---
title: GridJsクライアントサイドでの作業
type: docs
weight: 250
url: /ja/net/aspose-cells-gridjs/how-to-use-gridjs-client-api/
keywords: GridJs、カスタム、ロゴ、設定、API、JS API、クライアントAPI
description: この記事では、GridJsのクライアント側のJavaScript APIまたは機能を紹介しています。
aliases:
  - /net/aspose-cells-gridjs/client/
  - /net/aspose-cells-gridjs/work-with-client-api/
  - /net/aspose-cells-gridjs/use-js-api/
  - /net/aspose-cells-gridjs/gridjs-spreadsheet-api/
  - /net/aspose-cells-gridjs/client-api/
  - /net/aspose-cells-gridjs/js-api/
  - /net/aspose-cells-gridjs/javascript-api/
---

# GridJsクライアントサイドでの作業
[x-spreadsheet](https://github.com/myliang/x-spreadsheet)をベースにしたGridJsクライアントを開発しました。

## 主な手順は次のとおりです：

- x_spreadsheetインスタンスの作成
```javascript
xs = x_spreadsheet(id, options)
    // the parameters are:
    id: the html node id ,for example :'#gridjs-demo' for the html  <div id="gridjs-demo"></div>
    options: the load options


for example the below code init a gridjs_spreadsheet object.
	xs = x_spreadsheet('#gridjs-demo', {
			updateMode:'server',
			updateUrl:'/GridJs2/UpdateCell',
			mode: 'edit',
			showToolbar: true,
                        local: 'en',
			showContextmenu: true
			})
```
ロードオプションのパラメータ：

| パラメータ | 説明 | デフォルト値 | 任意 |
| --- | --- | --- | --- |
| `allowSelectTextInTextBoxInReadMode` | 読み取りモード中にテキストボックスでテキスト選択を許可するかどうか。<br>デフォルト値はfalse。 | `false` | はい |
| `checkSyntax` | ユーザー入力の文法チェックとスペル訂正を行うかどうか。<br>setSyntaxCheckUrlとの連携。<br>デフォルト値はfalse。 | `false` | はい |
| `loadingGif` | 画像や図形を読み込むときのローディングGIFのURL。<br>デフォルトはcontent/img/updating.gif。 | `content/img/updating.gif` | はい |
| `local` | メニューやツールバーのローカリゼーション情報を設定し、多言語対応。<br>可能な値は：<br>- `en, zh, es, pt, de, ru, nl`（英語、中国語、スペイン語、ポルトガル語、ドイツ語、ロシア語、オランダ語）<br>- `ar, fr, id, it, ja`（アラビア語、フランス語、インドネシア語、イタリア語、日本語）<br>- `ko, th, tr, vi, cht`（韓国語、タイ語、トルコ語、ベトナム語、繁体字中国語） | `en` | はい |
| `mode` | `read`または`edit`が設定可能です。`read`は読み取り専用のスプレッドシートを意味し、`edit`は編集可能。 | なし | いいえ |
| `isCollaborative` | コラボレーティブモードをサポートするかどうか。 | `false` | はい |
| `searchHighlightColor` | 検索語のハイライト背景色。<br>色はアルファチャネルを含む必要があります。 | `#dbe71338` | はい |
| `showCheckSyntaxButton` | 文法チェック＆スペル訂正ボタンをツールバーに表示するかどうか。<br>デフォルトはfalse。 | `false` | はい |
| `showContextmenu` | セルの右クリック時にコンテキストメニューを表示するかどうか。<br>デフォルトはtrue。 | `true` | はい |
| `showFileName` | ファイル名を表示するかどうか。 | `true` | はい |
| `showFormulaExplain` | マウスがセル上にあるときに、そのセルに適用された式の説明を表示するかどうか。<br>setFormulaExplainUrlと連携。<br>デフォルトはfalse。 | `false` | はい |
| `showFormulaTip` | マウスがセル上にあるときに、そのセルに適用された既存の式を表示するかどうか。<br>デフォルトはfalse。 | `false` | はい |
| `showNonEditableSymbolInCell` | セルにクライアント側の編集不可記号を表示するかどうか。<br>trueに設定すると、「編集無効化」コンテキストメニューのクリック後に選択範囲に記号が表示されます。<br>デフォルト値はfalseです。 | `false` | Yes |
| `showToolbar` | ツールバーを表示するかどうか。 | `true` | Yes |
| `updateMode` | 現在、`server` のみサポートされています。 | `server` | No |
| `updateUrl` | JSONに基づいたサーバーサイドの更新アクション用URLを設定します。 | なし | No |
| `view` | シートのビュサイズを設定します。例：`{width: () => 1000, height: ()=> 500}`。 | `{width: () => document.documentElement.clientWidth, height: () => document.documentElement.clientHeight }` | Yes |
| `token` | 認証トークンを設定します。トークンがnullでない場合、リクエストヘッダーに `Authorization: Bearer {token}`が自動的に追加されます。`xs.refreshToken(token)`を使用して新しいトークンを設定できます。 | なし | はい |    
| `showBottombarStats` | 下部バーの統計情報を表示するかどうか。<br>デフォルトはtrue。 | `true` | はい |   
| `showRowAppenderToolbar` | バッチ行追加ツールバーを表示するかどうか。<br>デフォルトはtrue。 | `true` | はい |   

- JSONデータでロード
```javascript
xs.loadData(data)
// the parameters is:
	data: the json data which describ the data structure for the worksheets
```
- シート名でアクティブシートを設定
```javascript
xs.setActiveSheetByName(sheetname)
// the parameters is:
	sheetname: the sheet name 
```
- IDでアクティブシートを設定
```javascript
xs.setActiveSheet(id)
// the parameters is:
	sheetname: the sheet id 
```

- アクティブセルを設定
```javascript
xs.setActiveCell(row,col);
// the parameters are:
	row: the cell row
	col: the cell column
```

- 複数インスタンスのアクティブ設定 
```javascript
xs.setActiveForMultipleInstance(isacitve);
// the parameters are:
	isacitve: whether need to do edit operation at this xs instanse 
// when there are more than one GridJs instances in one page, we need to call this method.
// we only support do edit operation for one instances at a page.
// for example,if we have two instances: xs1 and xs2 in one html page.
// if we need to keep edit operation in xs1,
// we shall call:
xs1.setActiveForMultipleInstance(true);
xs2.setActiveForMultipleInstance(false);

// if we need not do any edit operation for both,
// we shall call:
xs1.setActiveForMultipleInstance(false);
xs2.setActiveForMultipleInstance(false);

```
- カスタムトーストを設定
```javascript
xs.customToast(customToastFunction);
// the parameter is:
	customToastFunction: user defined function to toast message,it shall have three parameters :title, content,callback
	if set to null,it will use the default build-in toast.

    for example: 
            function myCustomToast(title, content, callback) {
	    //.....
	    }
            xs.customToast(myCustomToast);
```

- サーバーサイドアクションのための形状/画像操作の情報を設定
```javascript
xs.setImageInfo(imageGetActionUrl, imageAddByUploadActionUrl, imageAddByUrlActionUrl, imageCopyActionUrl, zindex, loadingGif);
// the parameters are:
	imageGetActionUrl: the get image action URL in the server side controller
	imageAddByUploadActionUrl: the upload image action  URL in the server side controller
	imageAddByUrlActionUrl: the add image from URL action  URL in the server side controller
	imageCopyActionUrl: the copy image action  URL in the server side controller
	zindex: the minimum zindex of the image in the canvas
	loadingGif (optional): the loading gif url when loading the image/shape .it is optional,the default value is:content/img/updating.gif
    for example: 
            const imageurl = "/GridJs2/imageurl";
            const imageuploadurl1 = "/GridJs2/AddImage";
            const imageuploadurl2 = "/GridJs2/AddImageByURL";
            const imagecopyurl = "/GridJs2/CopyImage";  
            const basiczorder = 5678;
    xs.setImageInfo(imageurl, imageuploadurl1, imageuploadurl2, imagecopyurl, basiczorder);
```

- サーバーサイドアクションのためのダウンロード操作の情報を設定
```javascript
xs.setFileDownloadInfo(downloadActionUrl);
// the parameters are:
	downloadActionUrl: the get download file action URL in the server side controller

    for example: 
            const fileDownloadUrl = "/GridJs2/Download";
            xs.setFileDownloadInfo(fileDownloadUrl);
```

- サーバーサイドアクションのためのOLEオブジェクト操作の情報を設定
```javascript
xs.setOleDownloadInfo(oleActionUrl);
// the parameters are:
	oleActionUrl: the ole object file action URL in the server side controller
    for example: 
            const oleDownloadUrl = "/GridJs2/Ole";
            xs.setOleDownloadInfo(oleDownloadUrl);
```
- サーバーサイドの構文チェック＆スペル修正操作の情報設定
```javascript
xs.setSyntaxCheckUrl(checkUrl);
// the parameters are:
	checkUrl: the  syntax checking & spell correction operation action URL in the server side controller
    for example: 
            const checkurl = "/GridJs2/CheckSyntax";
            xs.setSyntaxCheckUrl(checkurl);
```

- サーバーサイドの数式説明の情報設定
```javascript
xs.setFormulaExplainUrl(formulaExplainUrl);
// the parameters are:
	formulaExplainUrl: the  formula explanation  action URL in the server side controller
    for example: 
            const formulaExplainUrl = "/GridJs2/FormulaExplain";
            xs.setFormulaExplainUrl(formulaExplainUrl);
```


___
## その他の便利なAPI
- ビューをレンダリング
```javascript
xs.reRender()
```

- アクティブシートのIDを取得
```javascript
xs.getActiveSheet()
```

- 新しいワークシートを追加
```javascript
xs.addSheet(name,isactive,tabcolor,fontcolor)
// the parameters are:
	name:the sheet name
	isactive:whether set this sheet as active sheet
	tabcolor:the background color for the sheet in the tab bottom menu
	fontcolor:the font color for the sheet name in the tab bottom menu
   for example:
    xs.addSheet('hello',true,'#12ee5b','#2c5d3b')
```
- シート名を変更
```javascript
xs.modifySheetName(oldName,newName)
// the parameters are:
	oldName:the sheet name
	newName:the new desired name
   for example:
     xs.modifySheetName('Sheet1','student');
```
- シートを削除する
```javascript
xs.deleteSheet(name)
// the parameters is:
	name:the sheet name
   for example:
        xs.deleteSheet('Sheet1');

```

- ズームレベルを設定
```javascript
xs.setZoomLevel(zoom)
// the parameters is:
	zoom:the zoom level ,can be number ,for example 0.5 for zoom out, or 2 for zoom in
```

- ファイル名を設定 
```javascript
xs.setFileName(name)
// the parameters is:
	name:the file name with extension ,for example trip.xlsx
```
- 保存前に関数呼び出しを設定する 
```javascript
xs.setBeforeSaveFunction(func)
// the parameters is:
	func:This function is called before the save action. If it returns true, the save will proceed; otherwise, the save will not proceed.
   for example:
	xs.setBeforeSaveFunction(()=>{console.log('hello before save');return true;});
```

- メール送信機能のためのコールバック関数
```javascript
xs.setEmailSendCallFunction(callback)
// the parameters is:
	callback: the callback function to handle email sending, receives a mailObj parameter
		callback: function(mailObj) {
			// mailObj properties:
			// mailObj.receiver: the email address of the receiver, e.g., 'example@gmail.com'
			// mailObj.type: the format of the file to be sent, can be 'html', 'xlsx', or 'pdf'
		}
```

- GridJsのウィンドウキーイベントを有効にするかどうか
```javascript
xs.enableKeyEvent(isenable)
// the parameters is:
	isenable:whether the window key event is active for GridJs
//when has other controls in the same page, you may want to ignore the key event in GridJs 
```

- ウィンドウリサイズイベントやウィンドウキーイベントなど、GridJsにアタッチされたすべてのイベントを解除します。
```javascript
xs.destroy()
```

- コラボレーションモードでの設定を行う。setUniqueIdの前にsetCollaborativeSettingを設定してください  
```javascript
xs.setCollaborativeSetting(url,wsendpoint,wsapp,wsuser,wstopic)
    //the parameters are:
         url: the basic action URL in the server side controller to get history messages ,the default is '/GridJs2/msg'
	 wsendpoint: the websocket endpoint in the server side , the default is '/ws'
	 wsapp: the websocket destinations prefixed with "/app", the default is '/app/opr'
	 wsuser: the websocket for user-specific queues prefixed with "/usr", the default is '/user/queue'
	 wstopic: the websocket destinations prefixed with "/topic", the default is '/topic/opr'


```

- 画像/形状の可視フィルタを設定
```javascript
xs.setVisibleFilter((sheet,s) =>{})
    //  to set a function which return true(for visible) or false(for invisible) for the visible filter with the below parameters :
	sheet:the sheet instance
	s:the image or shape instance
    for example: 
	//this will make visible for image/shape in sheet with name 'Sheet3' and 'Sheet1' except for the 'Rectangle' type
		xs.setVisibleFilter((sheet,s) => { if (sheet.data.name==='Sheet3'||sheet.data.name==='Sheet1') return s.type!=='Rectangle';  return false; })
	//this will make visible for image/shape in sheet with name  'Sheet1' 
		xs.setVisibleFilter((sheet,s) => { if (sheet.data.name==='Sheet1') return true;  return false; })
	//this will make invisible for image/shape in all sheets 
		xs.setVisibleFilter((sheet,s) => {  return false; })
	//if all the image/shape is already loaded and you want to change the visible filter at runtime,you can call the below code to trigger a reload for image/shape
		xs.reRender()
```

- 選択された画像/形状を取得し、何も選択されていない場合はnullを返します
```javascript
xs.sheet.selector.getObj()
```
- 指定セル位置にHTMLノードを表示または非表示
```javascript
xs.sheet.showHtmlAtCell(isShow, html, ri, ci, deltaX, deltaY)

    //the parameters are:
      isShow: Boolean value indicating whether to show or hide the HTML content.
      html: The HTML string to be displayed.
      ri: Row index of the target cell.
      ci: Column index of the target cell.
      deltaX: (Optional) Relative X-position adjustment from the top-left corner of the cell.
      deltaY: (Optional) Relative Y-position adjustment from the top-left corner of the cell.

    for example: 
    // Show HTML at cell A1
    xs.sheet.showHtmlAtCell(true, "<span>html span</span><input length='30' id='myinput'>test</input>", 0, 0);

    // Hide the HTML node
    xs.sheet.showHtmlAtCell(false);

    // Note: When an HTML node is shown, the default GridJS event handling is disabled to allow interaction with the HTML content.
    // This means you cannot select any cells or perform edit operations until the HTML node is hidden.
```

- 画像/シェイプの選択可能状態設定 
```javascript
const shape=xs.sheet.selector.getObj();
shape.setControlable(isenable)
     // the parameter is:
      isenable: when set to true,the image or shape can be selectable and movable/resizeable
```


- 行を挿入する
```javascript
xs.sheet.insertRows(start, n)
    // the parameters are:
	start: start row id 
	n:how many rows will be inserted
```
- 列を挿入する 
```javascript
xs.sheet.insertColumns(start, n)
    // the parameters are:
	start: start column id
	n:how many columns will be inserted
```
- 行を削除する 
```javascript
xs.sheet.deleteRows(start, n)
    // the parameters are:
	start: start row id 
	n:how many rows will be deleted
```
- 列を削除する 
```javascript
xs.sheet.deleteColumns(start, n)
    // the parameters are:
	start: start column id 
	n:how many columns will be deleted
```
- 固定ペインを設定します
```javascript
xs.sheet.freeze(ri,ci)
    // the parameters are:
	ri:row index 
	ci:column index
```
- ペインの固定を解除する
```javascript
xs.sheet.freeze(0,0)
```

- 編集可能／読み取り専用範囲を設定する
```javascript
xs.sheet.setEditableRange(range,isenable)
    // the parameters are:
	range:the cell range ,etc. {sri:0,sci:0,eri:2,eci:2} reprensents range start from cell A1 to C3
	isenable:when set to true,the range is editable.other wise,the range is readonly.
```

- 行を非表示にする 
```javascript
xs.sheet.hideRows(sri,eri)
    // the parameters are:
	sri:the start row index 
	eri:the end row index
```

- 行の表示を解除する
```javascript
xs.sheet.unhideRows(sri,eri)
    // the parameters are:
	sri:the start row index 
	eri:the end row index
```

- 列を非表示にする 
```javascript
xs.sheet.hideColumns(sci,eci)
    // the parameters are:
	sci:the start column index 
	eci:the end column index
```

- 列の表示を解除する
```javascript
xs.sheet.unhideColumns(sci,eci)
    // the parameters are:
	sci:the start column index 
	eci:the end column index
```


- 行の高さを設定します
```javascript
xs.sheet.setRowHeight(ri,height)
    // the parameters are:
	ri:row index
	height:the height for the row
```
- 行の高さを設定します
```javascript
xs.sheet.setRowsHeight(sri,eri,height)
    // the parameters are:
	sri:start row index
	eri:end row index
	height:the height for the rows
```

- すべての行の高さを設定します
```javascript
xs.sheet.setAllRowsHeight(height)
    // the parameters are:
	height:the height for the rows
```

- 列の幅を設定します
```javascript
xs.sheet.setColWidth(ci,width)
    // the parameters are:
	ci:column index
	width:the width for the column
```
- 列の幅を設定します
```javascript
xs.sheet.setColsWidth(sci,eci,width)
    // the parameters are:
	sci:the start column index
	eci:the end column index
	width:the width for the column
```

- すべての列の幅を設定します
```javascript
xs.sheet.setAllColsWidth(width)
    // the parameters are:
	width:the width for the columns
```

- セルにコメントを設定する
```javascript
xs.sheet.setComment(ri,ci,author,note)
    // the parameters are:
	ri:row index of the cell
	ci:column index of the cell
	author:the author for the comment
	note:the content for the comment
```

- セルのコメントを削除する
```javascript
xs.sheet.removeComment(ri,ci)
    // the parameters are:
	ri:row index of the cell
	ci:column index of the cell
```


- セルオブジェクトを取得
```javascript
xs.sheet.data.getCell(ri,ci)
    // the parameters are:
	ri:row index 
	ci:column index
```

- セルスタイルを取得
```javascript
xs.sheet.data.getCellStyle(ri,ci)
    // the parameters are:
	ri:row index 
	ci:column index
```
- セル値を設定
```javascript
xs.sheet.data.setCellText(ri,ci,value,state)
    // the parameters are:
	ri:row index 
	ci:column index
	value:the cell value
	state: input | finished ,if finished ,it will do update action to servside
```

- 選択されたセル範囲の取得/設定
```javascript
xs.sheet.data.selector.range
```
- 選択されたセルまたはセル領域のセル値を設定します
```javascript
xs.sheet.data.setSelectedCellText(value)
    // the parameters are:
	value:the  value for the cell
```
- 選択されたセルまたはセル領域のスタイルを設定します
```javascript
xs.sheet.data.setSelectedCellAttr(attributename,value)
    // the parameters are:
	attributename:font-name | font-bold | font-italic | font-size  | format|border|merge|formula |strike|textwrap |underline |align |valign |color|bgcolor|pattern
	value:the  value for the attribute
```

- 表示範囲のスタイルを設定する
```javascript
xs.sheet.data.setRangeAttr(range,attributename,value)
    // the parameters are:
        range:the cell range ,etc. {sri:0,sci:0,eri:2,eci:2} reprensents range start from cell A1 to C3
	attributename:font-name | font-bold | font-italic | font-size  | format|border|merge|formula |strike|textwrap |underline |align |valign |color|bgcolor|pattern
	value:the  value for the attribute
   for example:
        xs.sheet.data.setRangeAttr({sri:0,sci:0,eri:2,eci:2},'bgcolor','#11ee2a');
```


- 選択されたセル領域を結合します
```javascript
xs.sheet.data.merge()
```

- 選択されたセル領域の結合を解除します
```javascript
xs.sheet.data.unmerge()
```
- 選択したセルの内容を削除またはスタイルをクリアする  
```javascript
xs.sheet.data.deleteCell(type)
    // the parameters are:
	type:all|format  all: means delete the cell and clear the style ;format means delete the cell value and keep the cell style
```

- 目的のセル範囲の内容を削除またはスタイルをクリアする
```javascript
xs.sheet.data.deleteRange(range,type)
    // the parameters are:
        range:the cell range ,etc. {sri:0,sci:0,eri:2,eci:2} reprensents range start from cell A1 to C3
	type:all|format  all: means delete the cell and clear the style ;format means delete the cell value and keep the cell style
```



- 列の幅を取得します 
```javascript
xs.sheet.data.cols.sumWidth(min,max)
    // the parameters are:
	min:the start column index
	max:the end column index,not include
```



- 行の高さを取得します 
```javascript
xs.sheet.data.rows.sumHeight(min,max)
    // the parameters are:
	min:the start row index
	max:the end row index,not include
```

- 表示方向の取得/設定をします
```javascript
xs.sheet.data.displayRight2Left
```

## イベントコールバック
- 以下のイベントを追跡できます
```javascript
 xs.on('cell-selected', (cell, ri, ci) => {
                console.log('cell selected:', cell, ', ri:', ri, ', ci:', ci);
                if (ci === -1) {
                    console.log('ci === -1 means a row selected ',ri);
                }
                if (ri === -1) {
                    console.log('ri === -1 means a column selected',ci);
                }
            }).on('cells-selected', (cell, range) => {
                console.log('range   selected:', cell, ', rang:', range);
            }).on('object-selected', (shapeOrImageObj) => {
                console.log('shape or image selected id:', shapeOrImageObj.id, ', type: ', shapeOrImageObj.type);
            }).on('sheet-selected', (id,name) => {
                console.log('sheet selected id:', id, ', name: ',name);
            }).on('sheet-loaded', (id,name) => {
                console.log('sheet load finished:', id, ', name: ',name);
            }).on('cell-edited', (text, ri, ci) => {
	        //just edit the cell
                console.log('text:', text, ', ri: ', ri, ', ci:', ci);
            }).on('cells-updated', (name, cells) => {
	       //cell value got updated
                console.log('cells updated for sheet name:', name);
                cells.forEach((acell, index, array) => {
                console.log('acell got updated:', acell);
            })
            }).on('cells-deleted', (range) => {
                console.log('cells deleted :', range);
            }).on('rows-deleted', (ri, n) => {
                console.log('rows-deleted :', ri, ",size", n);

            }).on('columns-deleted', (ci, n) => {
                console.log('columns-deleted :', ci, ",size", n);

            }).on('rows-inserted', (ri, n) => {
                console.log('rows-inserted :', ri, ",size", n);

            }).on('columns-inserted', (ci, n) => {
                console.log('columns-inserted :', ci, ",size", n);

            });
```
- 事前チェックイベント
  falseを返すと、挿入/削除操作は実行されません。
```javascript
  xs.checkRowInsert = (ri, size) => { if (ri % 2 == 1) return true; else return false; };
  xs.checkColumnInsert = (ci, size) => { if (ci % 2 == 1) return true; else return false; };
  xs.checkRowDelete = (ri, size) => { if (ri % 2 == 1) return true; else return false; };
  xs.checkColumnDelete = (ci, size) => { if (ci % 2 == 1) return true; else return false; };
```

## カスタマイズ

- ホームアイコンとリンクを設定します
```javascript
xs.sheet.menubar.icon.setHomeIcon(iconUrl,targetUrl)
    // the parameters are:
	iconUrl:the home icon URL
	targetUrl:the target link URL
	for example ,the below code will set the new logo and with link to google.com
	xs.sheet.menubar.icon.setHomeIcon('https://forum.aspose.com/letter_avatar_proxy/v4/letter/y/3e96dc/45.png','https://www.google.com')
```
- メニューバーを表示します
```javascript
xs.sheet.menubar.show()
```

- メニューバーを非表示にします
```javascript
xs.sheet.menubar.hide()
```
## 形状オブジェクト用API
- 形状オブジェクトの背景色を変更する
```javascript
    setBackgroundColor(color)
    // the parameters are:
        color: the html color value in hex string value
    //for example,we assume shape 0 existed,this will set the background color to Yellow 
     const ashape=xs.sheet.data.shapes[0];
     ashape.setBackgroundColor('#FFFF00');
```

## テキストボックスオブジェクト用のAPI
TextBoxはTypeプロパティが"TextBox"である特別な種類のシェイプです
たとえば: 以下のコードは、どの形状がテキストボックスであるかを示します

```javascript
for (let shape of xs.sheet.data.shapes) {
    if (shape.type === 'TextBox') {
        console.log(shape.id + ' is a textbox');
    }
}
```

- テキストボックスオブジェクトのフォント設定を適用
```javascript
    setFont(fontsettings)
    // the parameter is:
        fontsettings:   {'name':'Arial', 'size':12, 'bold':true, 'color':'#FFFF00', 'italic':true} ,the properties are 'name', 'size', 'bold', 'color', 'italic',they are all optional.
    //for example,we assume shape 0 is a textbox object,this will set the font color to Yellow ,and font size to 12pt,and bold the font. 
     const textbox=xs.sheet.data.shapes[0];
     const fontsettings= {'name':'Arial', 'size':12, 'bold':true, 'color':'#FFFF00'}; 
     textbox.setFont(fontsettings);
```
- 視覚的なアクティブ効果を得るために、自動で背景色とテキスト色を変更する
```javascript
    setActiveEffect(boolvalue)
    // the parameters are:
        boolvalue: if true,will change background color and the text color of the textbox object;if false,restore to original appearence
```

- テキストボックスオブジェクトのテキストコンテンツを非表示/表示します
```javascript
    hideText(boolvalue)
    // the parameters are:
        boolvalue: if true,will not display the text in the textbox object;if false,restore to original appearence
```

詳細情報については、こちらの例を確認してください
<https://github.com/aspose-cells/Aspose.Cells.Grid-for-.NET/tree/master/Examples_GridJs>





