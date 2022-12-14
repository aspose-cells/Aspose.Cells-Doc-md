---
title: 使用 GridJs 突出显示功能
type: docs
weight: 250
url: /zh/net/aspose-cells-gridjs/highlight/
description: 本文介绍如何使用 GridJs 来突出显示单元格文本、单元格范围、形状和图片。
keywords: highlight, highlight spreadsheet
---
# 使用 GridJs 突出显示功能
我们支持以下 JS API 以实现突出显示功能


- 启用高亮和设置高亮样式，所有高亮API只有在设置高亮样式后才会生效
```javascript
xs.showHighlights(style)
 // the parameter is:
 style: the style for highlight ,currently only support color
 for example: {'color':'rgba(85, 57, 47, 0.08)'}
```

- 禁用突出显示
```javascript
xs.hideHighlights()
```
- 添加要突出显示的单元格文本
```javascript
xs.sheet.addHighlightText(row,col,startpostion,endposition)
    // the parameters are:
    row:row index 
	col:column index
	startpostion: highlight start postion in cell text 
	endpostion: highlight end postion in cell text 
```

- 删除数组中单元格文本的突出显示
```javascript
xs.sheet.removeHighlightText(row,col)
    // the parameters are:
    row:row index 
	col:column index
```

- 获取单元格文本突出显示的数组
```javascript
xs.sheet.getHighlightTexts()
```

- 添加要突出显示的单元格范围
```javascript
xs.sheet.addHighlightRange(sri,sci,eri,eci)
    // the parameters are:
    sri:start row index of cell range
	sci:start column index of cell range
	 eri:end row index of cell range
	eci:end column index of cell range
```

- 删除数组中单元格区域的突出显示
```javascript
xs.sheet.removeHighlightRange(sri,sci,eri,eci)
     // the parameters are:
    sri:start row index of cell range
	sci:start column index of cell range
	 eri:end row index of cell range
	eci:end column index of cell range
```

- 获取单元格范围突出显示的数组
```javascript
xs.sheet.getHighlightRanges()
```

- 将单元格范围设置为反转突出显示
```javascript
xs.sheet.setHighlightInverseRange(sri,sci,eri,eci)
    // the parameters are:
    sri:start row index of cell range
	sci:start column index of cell range
	 eri:end row index of cell range
	eci:end column index of cell range
```

- 删除高亮显示为反转高亮显示
```javascript
xs.sheet.removeHighlightInverseRange()
     
```

- 获取反高亮单元格范围
```javascript
xs.sheet.getHighlightInverseRange()
```


- 添加形状以突出显示数组
```javascript
xs.sheet.addHighlightShape(shapeid)
    // the parameters are:
    shapeid: the id of shape, can be find in xs.sheet.data.shapes
```

- 删除数组中的高亮形状
```javascript
xs.sheet.removeHighlightShape(shapeid)
     // the parameters are:
    shapeid: the id of shape, can be find in xs.sheet.data.shapes
```

- 获取突出显示形状的数组
```javascript
xs.sheet.getHighlightShaps()
```


- 添加图像以突出显示数组
```javascript
xs.sheet.addHighlightImage(imageid)
    // the parameters are:
    imageid: the id of image, can be find in xs.sheet.data.images
```

- 删除数组中的高亮图像
```javascript
xs.sheet.removeHighlightImage(imageid)
     // the parameters are:
    imageid: the id of image, can be find in xs.sheet.data.images
```

- 获取突出显示图像的数组
```javascript
xs.sheet.getHighlightImages()
```

- 设置是否高亮所有工作表，包括所有形状和图像
```javascript
xs.sheet.setHighlightAll(ishighlightall,isrerender=true)
   // the parameters are:
   ishighlightall: true or false,whether to highlight all
   isrerender: true or false,whether to reRender
```


- 设置自定义图片高亮功能
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

您可以在我们的 github 演示页面中找到更多信息 https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Examples_GridJs/wwwroot/xspread/index.html
