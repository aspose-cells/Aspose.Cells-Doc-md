---
title: GridJsハイライト機能の操作
type: docs
weight: 250
url: /ja/net/aspose-cells-gridjs/highlight/
description: この記事では、GridJsでセルテキスト、セル範囲、図形、および画像のハイライトの使い方について説明します。
keywords: GridJs、ハイライト、スプレッドシートのハイライト、マスキング、備考
---

# GridJsのハイライト機能の操作 
以下のJS APIをサポートしています 


- ハイライトを有効にし、ハイライトスタイルを設定する。 ハイライトAPIは、アクティブなワークシートでハイライトスタイルが設定されてからのみ有効になります 
```javascript
xs.sheet.showHighlights(style)
 // the parameter is:
 style: the style for highlight ,currently only support color
 for example: {'color':'rgba(85, 57, 47, 0.08)'}
```

- アクティブなワークシートに設定されているハイライトスタイルを更新する 
```javascript
xs.sheet.updateHighlightStyle(style)
 // the parameter is:
 style: the style for highlight ,currently only support color
 for example: {'color':'rgba(85, 57, 47, 0.08)'}
```


- アクティブなワークシートでハイライトを無効にする    
```javascript
xs.sheet.hideHighlights()
```
- アクティブなワークシートでハイライトするためのセルテキストを追加する 
```javascript
xs.sheet.addHighlightText(row,col,startpostion,endposition)
    // the parameters are:
	row:row index 
	col:column index
	startpostion: highlight start postion in cell text 
	endpostion: highlight end postion in cell text 
    //it support multiple range postion inside one cell
```

- アクティブなワークシートの配列内のセルテキストのハイライトを削除する 
```javascript
xs.sheet.removeHighlightText(row,col,startpostion,endposition)
    // the parameters are:
	row:row index 
	col:column index
	startpostion: highlight start postion in cell text 
	endpostion: highlight end postion in cell text 
```

- アクティブなワークシートでセルテキストのハイライトの配列を取得する   
```javascript
xs.sheet.getHighlightTexts()
```

- アクティブなワークシートでセル範囲をハイライトする 
```javascript
xs.sheet.addHighlightRange(sri,sci,eri,eci)
    // the parameters are:
	sri:start row index of cell range
	sci:start column index of cell range
	eri:end row index of cell range
	eci:end column index of cell range
```

- アクティブなワークシート内の配列からセル範囲のハイライトを削除する 
```javascript
xs.sheet.removeHighlightRange(sri,sci,eri,eci)
     // the parameters are:
	sri:start row index of cell range
	sci:start column index of cell range
	eri:end row index of cell range
	eci:end column index of cell range
```

- アクティブなワークシートでセル範囲のハイライトの配列を取得する   
```javascript
xs.sheet.getHighlightRanges()
```

- アクティブなワークシートで逆ハイライトするためのセル範囲を設定する 
```javascript
xs.sheet.setHighlightInverseRange(sri,sci,eri,eci)
    // the parameters are:
	sri:start row index of cell range
	sci:start column index of cell range
	eri:end row index of cell range
	eci:end column index of cell range
```

- アクティブなワークシート内の逆ハイライトを削除する 
```javascript
xs.sheet.removeHighlightInverseRange()

```

- アクティブなワークシートで逆ハイライトのセル範囲を取得する 
```javascript
xs.sheet.getHighlightInverseRange()
```


- アクティブなワークシートで図形をハイライト配列に追加する 
```javascript
xs.sheet.addHighlightShape(shapeid)
    // the parameters are:
    shapeid: the id of shape, can be find in xs.sheet.data.shapes
```

- アクティブワークシートの配列内のハイライト形状を削除する 
```javascript
xs.sheet.removeHighlightShape(shapeid)
     // the parameters are:
    shapeid: the id of shape, can be find in xs.sheet.data.shapes
```

- アクティブワークシート内のハイライト形状の配列を取得する  
```javascript
xs.sheet.getHighlightShaps()
```

- アクティブワークシートにテキストボックスを追加する、テキストボックスは"TextBox"型の特別な形状で、種類プロパティがあります 
```javascript
xs.sheet.addHighlightTextBox(shapeid, startpostion, endposition)
    // the parameters are:
    shapeid: the id of shape, can be find in xs.sheet.data.shapes whose type is 'TextBox'
    startpostion: highlight start postion in the text of textbox
    endpostion: highlight end postion in the text of textbox
    //it support multiple range postion inside one textbox
```


- テキストボックス内のハイライト範囲を削除する、テキストボックスは"TextBox"型の特別な形状で、アクティブワークシート内です 
```javascript
xs.sheet.removeHighlightTextBox(shapeid, startpostion, endposition)
    // the parameters are:
    shapeid: the id of shape, can be find in xs.sheet.data.shapes whose type is 'TextBox'
    startpostion: highlight start postion in the text of textbox
    endpostion: highlight end postion in the text of textbox
    //it support multiple range postion inside one textbox
```

- アクティブワークシート内の配列に画像を追加する 
```javascript
xs.sheet.addHighlightImage(imageid)
    // the parameters are:
    imageid: the id of image, can be find in xs.sheet.data.images
```

- アクティブワークシート内の配列内のハイライト画像を削除する 
```javascript
xs.sheet.removeHighlightImage(imageid)
     // the parameters are:
    imageid: the id of image, can be find in xs.sheet.data.images
```

- ハイライト画像の配列を取得する  
```javascript
xs.sheet.getHighlightImages()
```

アクティブワークシートで全てのオブジェクトをハイライトするかどうかを設定します。全てのシェイプとイメージ、そして全てのワークシート領域を含む
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

アクティブワークシートのハイライト設定をクリアする
```javascript
xs.sheet.clearHighlights()

```

### テキストボックスオブジェクトのハイライト
テキストボックスは"TextBox"型の特別な形状です
たとえば: 以下のコードは、どの形状がテキストボックスであるかを示します

```javascript
for (let shape of xs.sheet.data.shapes) {
    if (shape.type === 'TextBox') {
        console.log(shape.id + ' is a textbox');
    }
}
```
- テキストボックスオブジェクトのハイライトを追加する
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

- テキストボックスオブジェクトのハイライトを削除する 
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




GitHubのデモページで詳細をご覧いただけます：https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Examples_GridJs/wwwroot/xspread/index.html
