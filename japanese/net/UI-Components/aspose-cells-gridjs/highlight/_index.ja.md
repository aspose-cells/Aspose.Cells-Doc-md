---
title: GridJs ハイライト機能の操作
type: docs
weight: 250
url: /ja/net/aspose-cells-gridjs/highlight/
description: この記事では、GridJs を使用してセルのテキスト、セル範囲、図形、画像を強調表示する方法について説明します。
keywords: highlight, highlight spreadsheet,redaction,remarks
---
#  GridJs ハイライト機能の操作
ハイライト機能では以下の JS API をサポートしています


- ハイライトを有効にし、ハイライト スタイルを設定します。すべてのハイライト API は、アクティブなワークシートでハイライト スタイルが設定された後にのみ有効になります。
```javascript
xs.sheet.showHighlights(style)
 // the parameter is:
 style: the style for highlight ,currently only support color
 for example: {'color':'rgba(85, 57, 47, 0.08)'}
```

- アクティブなワークシートに設定されているハイライト スタイルを更新します
```javascript
xs.sheet.updateHighlightStyle(style)
 // the parameter is:
 style: the style for highlight ,currently only support color
 for example: {'color':'rgba(85, 57, 47, 0.08)'}
```


- アクティブなワークシートのハイライトを無効にする
```javascript
xs.sheet.hideHighlights()
```
- アクティブなワークシートで強調表示するセル テキストを追加します。
```javascript
xs.sheet.addHighlightText(row,col,startpostion,endposition)
    // the parameters are:
	row:row index 
	col:column index
	startpostion: highlight start postion in cell text 
	endpostion: highlight end postion in cell text 
    //it support multiple range postion inside one cell
```

- アクティブなワークシートの配列内のセル テキストのハイライトを削除します
```javascript
xs.sheet.removeHighlightText(row,col,startpostion,endposition)
    // the parameters are:
	row:row index 
	col:column index
	startpostion: highlight start postion in cell text 
	endpostion: highlight end postion in cell text 
```

- アクティブなワークシートのセルテキストを強調表示するための配列を取得します
```javascript
xs.sheet.getHighlightTexts()
```

- アクティブなワークシートで強調表示するセル範囲を追加します
```javascript
xs.sheet.addHighlightRange(sri,sci,eri,eci)
    // the parameters are:
	sri:start row index of cell range
	sci:start column index of cell range
	eri:end row index of cell range
	eci:end column index of cell range
```

- アクティブなワークシートの配列内のセル範囲のハイライトを削除します
```javascript
xs.sheet.removeHighlightRange(sri,sci,eri,eci)
     // the parameters are:
	sri:start row index of cell range
	sci:start column index of cell range
	eri:end row index of cell range
	eci:end column index of cell range
```

- アクティブなワークシートのセル範囲を強調表示するための配列を取得します
```javascript
xs.sheet.getHighlightRanges()
```

- アクティブなワークシートでセル範囲を反転ハイライトに設定します
```javascript
xs.sheet.setHighlightInverseRange(sri,sci,eri,eci)
    // the parameters are:
	sri:start row index of cell range
	sci:start column index of cell range
	eri:end row index of cell range
	eci:end column index of cell range
```

- アクティブなワークシートの反転ハイライトのハイライトを削除します
```javascript
xs.sheet.removeHighlightInverseRange()
     
```

- アクティブなワークシートの反転ハイライトセル範囲を取得します
```javascript
xs.sheet.getHighlightInverseRange()
```


- アクティブなワークシート内の配列を強調表示する図形を追加します
```javascript
xs.sheet.addHighlightShape(shapeid)
    // the parameters are:
    shapeid: the id of shape, can be find in xs.sheet.data.shapes
```

- アクティブなワークシートの配列内のハイライト図形を削除します
```javascript
xs.sheet.removeHighlightShape(shapeid)
     // the parameters are:
    shapeid: the id of shape, can be find in xs.sheet.data.shapes
```

- アクティブなワークシートのハイライト形状の配列を取得します
```javascript
xs.sheet.getHighlightShaps()
```

- ハイライトするテキストボックスを追加します。テキストボックスは、アクティブなワークシートのタイププロパティが「TextBox」である特別な種類の図形です。
```javascript
xs.sheet.addHighlightTextBox(shapeid, startpostion, endposition)
    // the parameters are:
    shapeid: the id of shape, can be find in xs.sheet.data.shapes whose type is 'TextBox'
    startpostion: highlight start postion in the text of textbox
    endpostion: highlight end postion in the text of textbox
    //it support multiple range postion inside one textbox
```


- テキストボックスのハイライト範囲を削除します。テキストボックスは、アクティブなワークシートのタイププロパティが「TextBox」である特別な種類の図形です。
```javascript
xs.sheet.removeHighlightTextBox(shapeid, startpostion, endposition)
    // the parameters are:
    shapeid: the id of shape, can be find in xs.sheet.data.shapes whose type is 'TextBox'
    startpostion: highlight start postion in the text of textbox
    endpostion: highlight end postion in the text of textbox
    //it support multiple range postion inside one textbox
```

- アクティブなワークシートの配列を強調表示する画像を追加します
```javascript
xs.sheet.addHighlightImage(imageid)
    // the parameters are:
    imageid: the id of image, can be find in xs.sheet.data.images
```

- アクティブなワークシートの配列内のハイライト画像を削除します
```javascript
xs.sheet.removeHighlightImage(imageid)
     // the parameters are:
    imageid: the id of image, can be find in xs.sheet.data.images
```

- ハイライト画像の配列を取得
```javascript
xs.sheet.getHighlightImages()
```

- アクティブなワークシート内のすべてのオブジェクトを強調表示するかどうかを設定し、すべての図形と画像、およびすべてのワークシート領域を含めます
```javascript
xs.sheet.setHighlightAll(ishighlightall,isrerender=true)
   // the parameters are:
   ishighlightall: true or false,whether to highlight all
   isrerender: true or false,whether to reRender
```


- カスタム画像ハイライト機能を設定する
```javascript
xs.sheet.setCustomHighlightImgFunc(func)
   // the parameters are:
   func: the custom highlight image function, it shall take two parameters ,first is ishighlight,the second one is the fabric image object 
   //we use fabric js to manage image object, please refer to http://fabricjs.com/image-filters to check more info
   below is an example for the decleare function: 
   const customHighlightImage = (ishighlight, imgobj) => {
            imgobj.filters[0] = ishighlight ? new fabric.Image.filters.Sepia() : false;
            imgobj.applyFilters();
        }
    
```

- アクティブなワークシートのハイライト設定をクリア
```javascript
xs.sheet.clearHighlights()

```

### テキストボックスオブジェクトのハイライト
テキストボックスは、type プロパティが :"TextBox" である特別な種類の図形です。
例: 以下のコードは、どの図形がテキストボックスであるかを示します。

```javascript
for (let shape of xs.sheet.data.shapes) {
    if (shape.type === 'TextBox') {
        console.log(shape.id + ' is a textbox');
    }
}
```
- テキストボックスオブジェクトにハイライトを追加
```javascript
    addHighlight(startpostion,endposition)
    // the parameters are:
	startpostion: highlight start postion in textbox
	endpostion: highlight end postion in textbox

//for example,we assume shape 0 is a textbox object
const textbox=xs.sheet.data.shapes[0];
//first we shall add to highlight shape to enable the highlight for the textbox shape object,it support multiple range postion 
 xs.sheet.addHighlightShape(textbox.id);
 textbox.addHighlight(5,10);
 textbox.addHighlight(18,28);
```

- テキストボックスオブジェクトのハイライトを削除
```javascript
    removeHighlight(startpostion,endposition)
    // the parameters are:
	startpostion: highlight start postion in textbox
	endpostion: highlight end postion in textbox
    //for example,we assume shape 0 is a textbox object
     const textbox=xs.sheet.data.shapes[0];
     textbox.removeHighlight(5,10);
```

- テキストボックスオブジェクトのハイライトを取得する
```javascript
    getHighlight()
    //for example,we assume shape 0 is a textbox object
     const textbox=xs.sheet.data.shapes[0];
     textbox.getHighlight();
```

- テキストボックスオブジェクトの背景色を変更する
```javascript
    setBackgroundColor(color)
    // the parameters are:
        color: the html color value in hex string value
    //for example,we assume shape 0 is a textbox object,this will set the background color to Yellow 
     const textbox=xs.sheet.data.shapes[0];
     textbox.setBackgroundColor('#FFFF00');
```
- 背景色とテキストの色を自動的に変更して、視覚的にアクティブな効果を実現します
```javascript
    setActiveEffect(boolvalue)
    // the parameters are:
        boolvalue: if true,will change background color and the text color of the textbox object;if false,restore to original appearence
```

- テキストボックスオブジェクト内のテキストコンテンツを非表示/再表示します。
```javascript
    hideText(boolvalue)
    // the parameters are:
        boolvalue: if true,will not display the text in the textbox object;if false,restore to original appearence
```



詳細については、github のデモ ページ https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Examples_GridJs/wwwroot/xspread/index.html をご覧ください。
