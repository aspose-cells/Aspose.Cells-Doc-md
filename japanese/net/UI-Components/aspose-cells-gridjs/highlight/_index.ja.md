---
title: GridJs ハイライト機能の操作
type: docs
weight: 250
url: /ja/net/aspose-cells-gridjs/highlight/
description: この記事では、GridJ を使用してセル テキスト、セル範囲、形状、および画像を強調表示する方法について説明します。
keywords: highlight, highlight spreadsheet
---
# GridJs ハイライト機能の操作
ハイライト機能では、以下の JS API がサポートされています


- ハイライトを有効にし、ハイライト スタイルを設定します。すべてのハイライト API は、ハイライト スタイルが設定された後にのみ有効になります。
```javascript
xs.showHighlights(style)
 // the parameter is:
 style: the style for highlight ,currently only support color
 for example: {'color':'rgba(85, 57, 47, 0.08)'}
```

- ハイライトを無効にする
```javascript
xs.hideHighlights()
```
- 強調表示するセル テキストを追加する
```javascript
xs.sheet.addHighlightText(row,col,startpostion,endposition)
    // the parameters are:
    row:row index 
	col:column index
	startpostion: highlight start postion in cell text 
	endpostion: highlight end postion in cell text 
```

- 配列内のセル テキストのハイライトを削除
```javascript
xs.sheet.removeHighlightText(row,col)
    // the parameters are:
    row:row index 
	col:column index
```

- セル テキストのハイライトの配列を取得する
```javascript
xs.sheet.getHighlightTexts()
```

- ハイライトするセル範囲を追加
```javascript
xs.sheet.addHighlightRange(sri,sci,eri,eci)
    // the parameters are:
    sri:start row index of cell range
	sci:start column index of cell range
	 eri:end row index of cell range
	eci:end column index of cell range
```

- 配列内のセル範囲のハイライトを削除
```javascript
xs.sheet.removeHighlightRange(sri,sci,eri,eci)
     // the parameters are:
    sri:start row index of cell range
	sci:start column index of cell range
	 eri:end row index of cell range
	eci:end column index of cell range
```

- セル範囲のハイライトの配列を取得
```javascript
xs.sheet.getHighlightRanges()
```

- セル範囲を反転ハイライトに設定
```javascript
xs.sheet.setHighlightInverseRange(sri,sci,eri,eci)
    // the parameters are:
    sri:start row index of cell range
	sci:start column index of cell range
	 eri:end row index of cell range
	eci:end column index of cell range
```

- 反転ハイライトのハイライトを削除
```javascript
xs.sheet.removeHighlightInverseRange()
     
```

- 逆ハイライト セル範囲を取得する
```javascript
xs.sheet.getHighlightInverseRange()
```


- 形状を追加して配列を強調表示する
```javascript
xs.sheet.addHighlightShape(shapeid)
    // the parameters are:
    shapeid: the id of shape, can be find in xs.sheet.data.shapes
```

- 配列内のハイライト形状を削除
```javascript
xs.sheet.removeHighlightShape(shapeid)
     // the parameters are:
    shapeid: the id of shape, can be find in xs.sheet.data.shapes
```

- ハイライト形状の配列を取得
```javascript
xs.sheet.getHighlightShaps()
```


- ハイライト配列に画像を追加
```javascript
xs.sheet.addHighlightImage(imageid)
    // the parameters are:
    imageid: the id of image, can be find in xs.sheet.data.images
```

- 配列内のハイライト画像を削除
```javascript
xs.sheet.removeHighlightImage(imageid)
     // the parameters are:
    imageid: the id of image, can be find in xs.sheet.data.images
```

- ハイライト画像の配列を取得
```javascript
xs.sheet.getHighlightImages()
```

- すべてのワークシートを強調表示するかどうかを設定し、すべての図形と画像を含めます
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

詳細については、GitHub デモ ページ https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Examples_GridJs/wwwroot/xspread/index.html をご覧ください。
