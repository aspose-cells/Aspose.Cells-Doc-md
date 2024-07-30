---
title: 使用GridJs的高亮功能
type: docs
weight: 250
url: /zh/net/aspose-cells-gridjs/how-to-use-highlight-api/
description: 本文介绍如何在GridJs中对单元格文本、单元格范围、形状和图片进行突出显示。
keywords: GridJs,突出显示, 电子表格突出显示, 删除、备注
aliases:
  - /net/aspose-cells-gridjs/highlight/
  - /net/aspose-cells-gridjs/how-to-highlight/
  - /net/aspose-cells-gridjs/work-with-highlight-api/
  - /net/aspose-cells-gridjs/work-with-highlight-apis/
---

# 使用 GridJs 突出显示功能 
我们支持以下 JS API 用于突出显示功能 


- 启用突出显示并设置突出显示样式,所有突出显示 API 只有在设置了活动工作表的突出显示样式后才会生效 
```javascript
xs.sheet.showHighlights(style)
 // the parameter is:
 style: the style for highlight ,currently only support color
 for example: {'color':'rgba(85, 57, 47, 0.08)'}
```

- 更新活动工作表中设置的突出显示样式 
```javascript
xs.sheet.updateHighlightStyle(style)
 // the parameter is:
 style: the style for highlight ,currently only support color
 for example: {'color':'rgba(85, 57, 47, 0.08)'}
```


- 在活动工作表中禁用突出显示    
```javascript
xs.sheet.hideHighlights()
```
- 将单元格文本添加到活动工作表中的突出显示 
```javascript
xs.sheet.addHighlightText(row,col,startpostion,endposition)
    // the parameters are:
	row:row index 
	col:column index
	startpostion: highlight start postion in cell text 
	endpostion: highlight end postion in cell text 
    //it support multiple range postion inside one cell
```

- 在活动工作表中为单元格文本数组删除突出显示 
```javascript
xs.sheet.removeHighlightText(row,col,startpostion,endposition)
    // the parameters are:
	row:row index 
	col:column index
	startpostion: highlight start postion in cell text 
	endpostion: highlight end postion in cell text 
```

- 获取活动工作表中单元格文本的突出显示数组   
```javascript
xs.sheet.getHighlightTexts()
```

- 将单元格范围添加到活动工作表中的突出显示 
```javascript
xs.sheet.addHighlightRange(sri,sci,eri,eci)
    // the parameters are:
	sri:start row index of cell range
	sci:start column index of cell range
	eri:end row index of cell range
	eci:end column index of cell range
```

- 从活动工作表中的单元格范围数组中移除突出显示 
```javascript
xs.sheet.removeHighlightRange(sri,sci,eri,eci)
     // the parameters are:
	sri:start row index of cell range
	sci:start column index of cell range
	eri:end row index of cell range
	eci:end column index of cell range
```

- 获取活动工作表中单元格范围的突出显示数组   
```javascript
xs.sheet.getHighlightRanges()
```

- 设置活动工作表中的单元格范围为反向突出显示 
```javascript
xs.sheet.setHighlightInverseRange(sri,sci,eri,eci)
    // the parameters are:
	sri:start row index of cell range
	sci:start column index of cell range
	eri:end row index of cell range
	eci:end column index of cell range
```

- 在活动工作表中移除反向突出显示 
```javascript
xs.sheet.removeHighlightInverseRange()

```

- 获取活动工作表中反向突出显示的单元格范围 
```javascript
xs.sheet.getHighlightInverseRange()
```


- 将形状添加到活动工作表中的突出显示数组 
```javascript
xs.sheet.addHighlightShape(shapeid)
    // the parameters are:
    shapeid: the id of shape, can be find in xs.sheet.data.shapes
```

- 从活动工作表中的形状数组中移除突出显示形状 
```javascript
xs.sheet.removeHighlightShape(shapeid)
     // the parameters are:
    shapeid: the id of shape, can be find in xs.sheet.data.shapes
```

- 获取活动工作表中形状的突出显示数组  
```javascript
xs.sheet.getHighlightShaps()
```

- 将文本框添加到突出显示文本框数组中，文本框是 type 属性为"TextBox"的特殊形状，在活动工作表中 
```javascript
xs.sheet.addHighlightTextBox(shapeid, startpostion, endposition)
    // the parameters are:
    shapeid: the id of shape, can be find in xs.sheet.data.shapes whose type is 'TextBox'
    startpostion: highlight start postion in the text of textbox
    endpostion: highlight end postion in the text of textbox
    //it support multiple range postion inside one textbox
```


- 从文本框中的突出显示范围中删除，文本框是 type 属性为"TextBox"的特殊形状，在活动工作表中 
```javascript
xs.sheet.removeHighlightTextBox(shapeid, startpostion, endposition)
    // the parameters are:
    shapeid: the id of shape, can be find in xs.sheet.data.shapes whose type is 'TextBox'
    startpostion: highlight start postion in the text of textbox
    endpostion: highlight end postion in the text of textbox
    //it support multiple range postion inside one textbox
```

- 在活动工作表中的高亮数组中添加图像 
```javascript
xs.sheet.addHighlightImage(imageid)
    // the parameters are:
    imageid: the id of image, can be find in xs.sheet.data.images
```

- 在活动工作表中的数组中删除高亮图像 
```javascript
xs.sheet.removeHighlightImage(imageid)
     // the parameters are:
    imageid: the id of image, can be find in xs.sheet.data.images
```

- 获取用于高亮图像的数组  
```javascript
xs.sheet.getHighlightImages()
```

设置是否要对活动工作表中的所有对象进行高亮显示，包括所有形状、图像和所有工作表区域
```javascript
xs.sheet.setHighlightAll(ishighlightall,isrerender=true)
   // the parameters are:
   ishighlightall: true or false,whether to highlight all
   isrerender: true or false,whether to reRender
```


- 设置自定义图像高亮功能
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

清除活动工作表的高亮设置
```javascript
xs.sheet.clearHighlights()

```

### 用于文本框对象的高亮
文本框是一种特殊类型的形状，其类型属性为:"文本框"
例如：以下代码将显示哪种形状是文本框

```javascript
for (let shape of xs.sheet.data.shapes) {
    if (shape.type === 'TextBox') {
        console.log(shape.id + ' is a textbox');
    }
}
```
- 为文本框对象添加高亮显示
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

- 删除文本框对象的高亮显示 
```javascript
    removeHighlight(startpostion,endposition)
    // the parameters are:
	startpostion: highlight start postion in textbox
	endpostion: highlight end postion in textbox
    //for example,we assume shape 0 is a textbox object
     const textbox=xs.sheet.data.shapes[0];
     textbox.removeHighlight(5,10);
```

- 获取文本框对象的高亮 
```javascript
    getHighlight()
    //for example,we assume shape 0 is a textbox object
     const textbox=xs.sheet.data.shapes[0];
     textbox.getHighlight();
```




您可以在我们的 GitHub 演示页面找到更多 https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Examples_GridJs/wwwroot/xspread/index.html
