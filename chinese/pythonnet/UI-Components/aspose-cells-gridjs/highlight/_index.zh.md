---
title: 使用 GridJs 高亮功能
type: docs
weight: 250
url: /zh/python-net/aspose-cells-gridjs/highlight/
description: 本文描述了如何在单元格文本、单元格范围、形状和图片上使用 GridJs 进行高亮显示。
keywords: 高亮,表格,编辑,备注,Excel,评论	
---

# 使用 GridJs 高亮功能 
我们支持以下用于高亮功能的 JS API 


- 启用高亮并设置高亮样式，所有高亮 API 仅在活动工作表中设置高亮样式后才生效 
```javascript
xs.sheet.showHighlights(style)
 // the parameter is:
 style: the style for highlight ,currently only support color
 for example: {'color':'rgba(85, 57, 47, 0.08)'}
```

- 更新活动工作表中设置的高亮样式 
```javascript
xs.sheet.updateHighlightStyle(style)
 // the parameter is:
 style: the style for highlight ,currently only support color
 for example: {'color':'rgba(85, 57, 47, 0.08)'}
```


- 在活动工作表中禁用高亮    
```javascript
xs.sheet.hideHighlights()
```
- 将单元格文本添加到活动工作表中的高亮 
```javascript
xs.sheet.addHighlightText(row,col,startpostion,endposition)
    // the parameters are:
	row:row index 
	col:column index
	startpostion: highlight start postion in cell text 
	endpostion: highlight end postion in cell text 
    //it support multiple range postion inside one cell
```

- 从活动工作表中的数组中删除单元格文本的高亮 
```javascript
xs.sheet.removeHighlightText(row,col,startpostion,endposition)
    // the parameters are:
	row:row index 
	col:column index
	startpostion: highlight start postion in cell text 
	endpostion: highlight end postion in cell text 
```

- 获取活动工作表中单元格文本的高亮数组   
```javascript
xs.sheet.getHighlightTexts()
```

- 将单元格范围添加到活动工作表中进行高亮显示 
```javascript
xs.sheet.addHighlightRange(sri,sci,eri,eci)
    // the parameters are:
	sri:start row index of cell range
	sci:start column index of cell range
	eri:end row index of cell range
	eci:end column index of cell range
```

- 在活动工作表中的数组中移除单元格范围的高亮显示 
```javascript
xs.sheet.removeHighlightRange(sri,sci,eri,eci)
     // the parameters are:
	sri:start row index of cell range
	sci:start column index of cell range
	eri:end row index of cell range
	eci:end column index of cell range
```

- 获取活动工作表中单元格范围的高亮显示数组   
```javascript
xs.sheet.getHighlightRanges()
```

- 在活动工作表中设置单元格范围以进行反向高亮显示 
```javascript
xs.sheet.setHighlightInverseRange(sri,sci,eri,eci)
    // the parameters are:
	sri:start row index of cell range
	sci:start column index of cell range
	eri:end row index of cell range
	eci:end column index of cell range
```

- 在活动工作表中移除反向高亮显示的高亮显示 
```javascript
xs.sheet.removeHighlightInverseRange()

```

- 获取活动工作表中高亮单元格范围的逆向高亮 
```javascript
xs.sheet.getHighlightInverseRange()
```


- 在活动工作表中的高亮数组中添加形状 
```javascript
xs.sheet.addHighlightShape(shapeid)
    // the parameters are:
    shapeid: the id of shape, can be find in xs.sheet.data.shapes
```

- 从活动工作表中的高亮数组中移除高亮形状 
```javascript
xs.sheet.removeHighlightShape(shapeid)
     // the parameters are:
    shapeid: the id of shape, can be find in xs.sheet.data.shapes
```

- 获取活动工作表中高亮形状的数组  
```javascript
xs.sheet.getHighlightShaps()
```

- 在活动工作表中添加文本框到高亮区域，文本框是一种特殊类型的形状，其类型属性为:"TextBox" 
```javascript
xs.sheet.addHighlightTextBox(shapeid, startpostion, endposition)
    // the parameters are:
    shapeid: the id of shape, can be find in xs.sheet.data.shapes whose type is 'TextBox'
    startpostion: highlight start postion in the text of textbox
    endpostion: highlight end postion in the text of textbox
    //it support multiple range postion inside one textbox
```


- 从文本框中移除高亮范围，文本框是一种特殊类型的形状，其类型属性为:"TextBox" 
```javascript
xs.sheet.removeHighlightTextBox(shapeid, startpostion, endposition)
    // the parameters are:
    shapeid: the id of shape, can be find in xs.sheet.data.shapes whose type is 'TextBox'
    startpostion: highlight start postion in the text of textbox
    endpostion: highlight end postion in the text of textbox
    //it support multiple range postion inside one textbox
```

-将图像添加到活动工作表中的突出显示数组中 
```javascript
xs.sheet.addHighlightImage(imageid)
    // the parameters are:
    imageid: the id of image, can be find in xs.sheet.data.images
```

-在活动工作表中的突出显示数组中删除突出显示的图像 
```javascript
xs.sheet.removeHighlightImage(imageid)
     // the parameters are:
    imageid: the id of image, can be find in xs.sheet.data.images
```

-获取突出显示图像的数组  
```javascript
xs.sheet.getHighlightImages()
```

-设置是否突出显示活动工作表中的所有对象，包括所有形状和图像以及所有工作表区域
```javascript
xs.sheet.setHighlightAll(ishighlightall,isrerender=true)
   // the parameters are:
   ishighlightall: true or false,whether to highlight all
   isrerender: true or false,whether to reRender
```


-设置自定义图像突出显示函数
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

-  清除活动工作表的突出显示设置
```javascript
xs.sheet.clearHighlights()

```

### 文本框对象的突出显示
文本框是一种特殊的形状，其类型属性为:"TextBox",
例如：下面的代码将显示哪种形状是文本框

```javascript
for (let shape of xs.sheet.data.shapes) {
    if (shape.type === 'TextBox') {
        console.log(shape.id + ' is a textbox');
    }
}
```
-  为文本框对象添加突出显示
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

-  移除文本框对象的突出显示 
```javascript
    removeHighlight(startpostion,endposition)
    // the parameters are:
	startpostion: highlight start postion in textbox
	endpostion: highlight end postion in textbox
    //for example,we assume shape 0 is a textbox object
     const textbox=xs.sheet.data.shapes[0];
     textbox.removeHighlight(5,10);
```

-  获取文本框对象的高亮显示 
```javascript
    getHighlight()
    //for example,we assume shape 0 is a textbox object
     const textbox=xs.sheet.data.shapes[0];
     textbox.getHighlight();
```

-  更改文本框对象的背景颜色
```javascript
    setBackgroundColor(color)
    // the parameters are:
        color: the html color value in hex string value
    //for example,we assume shape 0 is a textbox object,this will set the background color to Yellow 
     const textbox=xs.sheet.data.shapes[0];
     textbox.setBackgroundColor('#FFFF00');
```
-  自动更改背景颜色和文本颜色以获得视觉活动效果
```javascript
    setActiveEffect(boolvalue)
    // the parameters are:
        boolvalue: if true,will change background color and the text color of the textbox object;if false,restore to original appearence
```

-  隐藏/显示文本框对象中的文本内容
```javascript
    hideText(boolvalue)
    // the parameters are:
        boolvalue: if true,will not display the text in the textbox object;if false,restore to original appearence
```



您可以在我们的 GitHub 演示页面 https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Examples_GridJs/wwwroot/xspread/index.html 找到更多信息
