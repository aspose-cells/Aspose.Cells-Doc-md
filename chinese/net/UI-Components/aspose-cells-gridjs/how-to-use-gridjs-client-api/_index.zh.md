---
title: 与GridJs客户端端协同工作
type: docs
weight: 250
url: /zh/net/aspose-cells-gridjs/how-to-use-gridjs-client-api/
keywords: GridJs,自定义,logo,设置,api,js API,客户端API
description: 本文介绍了GridJs中的客户端JavaScript API或函数。
aliases:
  - /net/aspose-cells-gridjs/client/
  - /net/aspose-cells-gridjs/work-with-client-api/
  - /net/aspose-cells-gridjs/use-js-api/
  - /net/aspose-cells-gridjs/gridjs-spreadsheet-api/
  - /net/aspose-cells-gridjs/client-api/
  - /net/aspose-cells-gridjs/js-api/
  - /net/aspose-cells-gridjs/javascript-api/
---

# 与GridJs客户端端协同工作
我们基于[x-spreadsheet](https://github.com/myliang/x-spreadsheet)开发了GridJs客户端。

## 主要步骤如下：

- 创建x_spreadsheet实例
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
加载选项的参数：

| 参数 | 描述 | 默认值 | 可选 |
| --- | --- | --- | --- |
| `allowSelectTextInTextBoxInReadMode` | 在只读模式下是否允许在 TextBox 控件中选择文本。<br>默认值为 false。 | `false` | 是 |
| `checkSyntax` | 是否对用户输入的文本内容进行语法检查和拼写纠错。<br>与 setSyntaxCheckUrl 配合使用。<br>默认值为 false。 | `false` | 是 |
| `loadingGif` | 加载图 images / shapes 时的 GIF 动图 URL。<br>默认值为 content/img/updating.gif。 | `content/img/updating.gif` | 是 |
| `local` | 设置菜单和工具栏的本地化信息，支持多种语言。<br>可能的值包括：<br>- `en, zh, es, pt, de, ru, nl`（英语、中文、西班牙语、葡萄牙语、德语、俄语、荷兰语）<br>- `ar, fr, id, it, ja`（阿拉伯语、法语、印尼语、意大利语、日语）<br>- `ko, th, tr, vi, cht`（韩语、泰语、土耳其语、越南语、繁体中文字幕） | `en` | 是 |
| `mode` | 可以是 `read` 或 `edit`；`read` 表示只读电子表格；`edit` 表示可以编辑电子表格。 | 无 | 否 |
| `isCollaborative` | 是否支持协作模式。 | `false` | 是 |
| `searchHighlightColor` | 搜索关键词的高亮背景色。<br>颜色必须包括透明度通道。 | `#dbe71338` | 是 |
| `showCheckSyntaxButton` | 是否在工具栏显示语法检查和拼写纠错按钮。<br>默认值为 false。 | `false` | 是 |
| `showContextmenu` | 是否在单元格右键点击时显示右键菜单。<br>默认值为 true。 | `true` | 是 |
| `showFileName` | 是否显示文件名。 | `true` | 是 |
| `showFormulaExplain` | 鼠标悬停时是否显示应用于此单元格的公式说明。<br>与 setFormulaExplainUrl 配合使用。<br>默认值为 false。 | `false` | 是 |
| `showFormulaTip` | 鼠标悬停时是否显示应用于此单元格的现有公式。<br>默认值为 false。 | `false` | 是 |
| `showNonEditableSymbolInCell` | 是否在单元格显示客户端不可编辑符号。<br>设置为 true 后，点击右键菜单“禁用编辑”后，禁用编辑的区域会显示符号。<br>默认值为 false。 | `false` | 是 |
| `showToolbar` | 是否显示工具栏。 | `true` | 是 |
| `updateMode` | 目前仅支持 `server`。 | `server` | 否 |
| `updateUrl` | 根据 JSON 设置服务器端的更新操作 URL。 | 无 | 否 |
| `view` | 设置表格视图大小，例如 `{width: () => 1000, height: ()=> 500}`。 | `{width: () => document.documentElement.clientWidth, height: () => document.documentElement.clientHeight }` | 是 |
| `token` | 设置认证令牌。当令牌不为空时，`Authorization: Bearer {token}` 头部会自动添加到请求中。你可以使用 `xs.refreshToken(token)` 设置新令牌。 | 无 | 是 |    
| `showBottombarStats` | 是否显示底部栏统计信息。<br>默认值为true。 | `true` | 是 |   
| `showRowAppenderToolbar` | 是否显示批量添加行工具栏。<br>默认值为true。 | `true` | 是 |   

- 用json数据加载
```javascript
xs.loadData(data)
// the parameters is:
	data: the json data which describ the data structure for the worksheets
```
- 通过sheetname设置活动表格
```javascript
xs.setActiveSheetByName(sheetname)
// the parameters is:
	sheetname: the sheet name 
```
- 通过id设置活动表格
```javascript
xs.setActiveSheet(id)
// the parameters is:
	sheetname: the sheet id 
```

- 设置活动单元
```javascript
xs.setActiveCell(row,col);
// the parameters are:
	row: the cell row
	col: the cell column
```

-  设置多个实例的激活状态 
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
- 设置自定义提示
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

- 为服务器端操作的形状/图像操作设置信息
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

- 为服务器端操作设置下载操作的信息
```javascript
xs.setFileDownloadInfo(downloadActionUrl);
// the parameters are:
	downloadActionUrl: the get download file action URL in the server side controller

    for example: 
            const fileDownloadUrl = "/GridJs2/Download";
            xs.setFileDownloadInfo(fileDownloadUrl);
```

- 为服务器端操作设置OLE对象操作的信息
```javascript
xs.setOleDownloadInfo(oleActionUrl);
// the parameters are:
	oleActionUrl: the ole object file action URL in the server side controller
    for example: 
            const oleDownloadUrl = "/GridJs2/Ole";
            xs.setOleDownloadInfo(oleDownloadUrl);
```
-  设置语法检查和拼写更正操作的服务器端信息
```javascript
xs.setSyntaxCheckUrl(checkUrl);
// the parameters are:
	checkUrl: the  syntax checking & spell correction operation action URL in the server side controller
    for example: 
            const checkurl = "/GridJs2/CheckSyntax";
            xs.setSyntaxCheckUrl(checkurl);
```

-  设置公式说明的服务器端信息
```javascript
xs.setFormulaExplainUrl(formulaExplainUrl);
// the parameters are:
	formulaExplainUrl: the  formula explanation  action URL in the server side controller
    for example: 
            const formulaExplainUrl = "/GridJs2/FormulaExplain";
            xs.setFormulaExplainUrl(formulaExplainUrl);
```


___
## 其他有用的API
- 渲染视图
```javascript
xs.reRender()
```

- 获取活动工作表ID
```javascript
xs.getActiveSheet()
```

- 添加新工作表
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
- 修改工作表名称
```javascript
xs.modifySheetName(oldName,newName)
// the parameters are:
	oldName:the sheet name
	newName:the new desired name
   for example:
     xs.modifySheetName('Sheet1','student');
```
- 删除工作表
```javascript
xs.deleteSheet(name)
// the parameters is:
	name:the sheet name
   for example:
        xs.deleteSheet('Sheet1');

```

- 设置缩放级别
```javascript
xs.setZoomLevel(zoom)
// the parameters is:
	zoom:the zoom level ,can be number ,for example 0.5 for zoom out, or 2 for zoom in
```

- 设置文件名 
```javascript
xs.setFileName(name)
// the parameters is:
	name:the file name with extension ,for example trip.xlsx
```
- 在保存前设置函数调用 
```javascript
xs.setBeforeSaveFunction(func)
// the parameters is:
	func:This function is called before the save action. If it returns true, the save will proceed; otherwise, the save will not proceed.
   for example:
	xs.setBeforeSaveFunction(()=>{console.log('hello before save');return true;});
```

-  用于发送邮件功能的回调函数
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

- 是否启用GridJs的窗口按键事件
```javascript
xs.enableKeyEvent(isenable)
// the parameters is:
	isenable:whether the window key event is active for GridJs
//when has other controls in the same page, you may want to ignore the key event in GridJs 
```

- 取消所有已绑定到GridJs的事件，包括窗口按键事件和窗口调整大小事件
```javascript
xs.destroy()
```

- 在协作模式下设置协作参数，确保在设置唯一ID之前调用setCollaborativeSetting  
```javascript
xs.setCollaborativeSetting(url,wsendpoint,wsapp,wsuser,wstopic)
    //the parameters are:
         url: the basic action URL in the server side controller to get history messages ,the default is '/GridJs2/msg'
	 wsendpoint: the websocket endpoint in the server side , the default is '/ws'
	 wsapp: the websocket destinations prefixed with "/app", the default is '/app/opr'
	 wsuser: the websocket for user-specific queues prefixed with "/usr", the default is '/user/queue'
	 wstopic: the websocket destinations prefixed with "/topic", the default is '/topic/opr'


```

- 为图像/形状设置可见过滤器
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

- 获取选定的图像/形状，如果没有选定则返回空
```javascript
xs.sheet.selector.getObj()
```
-  在指定单元格位置显示或隐藏 HTML 节点
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

-  设置图片/形状的可选状态 
```javascript
const shape=xs.sheet.selector.getObj();
shape.setControlable(isenable)
     // the parameter is:
      isenable: when set to true,the image or shape can be selectable and movable/resizeable
```


- 插入行
```javascript
xs.sheet.insertRows(start, n)
    // the parameters are:
	start: start row id 
	n:how many rows will be inserted
```
- 插入列 
```javascript
xs.sheet.insertColumns(start, n)
    // the parameters are:
	start: start column id
	n:how many columns will be inserted
```
- 删除行 
```javascript
xs.sheet.deleteRows(start, n)
    // the parameters are:
	start: start row id 
	n:how many rows will be deleted
```
- 删除列 
```javascript
xs.sheet.deleteColumns(start, n)
    // the parameters are:
	start: start column id 
	n:how many columns will be deleted
```
-  设置冻结窗格
```javascript
xs.sheet.freeze(ri,ci)
    // the parameters are:
	ri:row index 
	ci:column index
```
- 取消冻结窗格
```javascript
xs.sheet.freeze(0,0)
```

- 设置可编辑/只读区域
```javascript
xs.sheet.setEditableRange(range,isenable)
    // the parameters are:
	range:the cell range ,etc. {sri:0,sci:0,eri:2,eci:2} reprensents range start from cell A1 to C3
	isenable:when set to true,the range is editable.other wise,the range is readonly.
```

- 隐藏行 
```javascript
xs.sheet.hideRows(sri,eri)
    // the parameters are:
	sri:the start row index 
	eri:the end row index
```

- 取消隐藏行
```javascript
xs.sheet.unhideRows(sri,eri)
    // the parameters are:
	sri:the start row index 
	eri:the end row index
```

- 隐藏列 
```javascript
xs.sheet.hideColumns(sci,eci)
    // the parameters are:
	sci:the start column index 
	eci:the end column index
```

- 取消隐藏列
```javascript
xs.sheet.unhideColumns(sci,eci)
    // the parameters are:
	sci:the start column index 
	eci:the end column index
```


-  设置行的高度
```javascript
xs.sheet.setRowHeight(ri,height)
    // the parameters are:
	ri:row index
	height:the height for the row
```
-  设置行的高度
```javascript
xs.sheet.setRowsHeight(sri,eri,height)
    // the parameters are:
	sri:start row index
	eri:end row index
	height:the height for the rows
```

-  设置所有行的高度
```javascript
xs.sheet.setAllRowsHeight(height)
    // the parameters are:
	height:the height for the rows
```

-  设置列的宽度
```javascript
xs.sheet.setColWidth(ci,width)
    // the parameters are:
	ci:column index
	width:the width for the column
```
-  设置列的宽度
```javascript
xs.sheet.setColsWidth(sci,eci,width)
    // the parameters are:
	sci:the start column index
	eci:the end column index
	width:the width for the column
```

-  设置所有列的宽度
```javascript
xs.sheet.setAllColsWidth(width)
    // the parameters are:
	width:the width for the columns
```

- 设置单元格的批注
```javascript
xs.sheet.setComment(ri,ci,author,note)
    // the parameters are:
	ri:row index of the cell
	ci:column index of the cell
	author:the author for the comment
	note:the content for the comment
```

- 移除单元格的批注
```javascript
xs.sheet.removeComment(ri,ci)
    // the parameters are:
	ri:row index of the cell
	ci:column index of the cell
```


- 获取单元格对象
```javascript
xs.sheet.data.getCell(ri,ci)
    // the parameters are:
	ri:row index 
	ci:column index
```

- 获取单元格样式
```javascript
xs.sheet.data.getCellStyle(ri,ci)
    // the parameters are:
	ri:row index 
	ci:column index
```
- 设置单元格值
```javascript
xs.sheet.data.setCellText(ri,ci,value,state)
    // the parameters are:
	ri:row index 
	ci:column index
	value:the cell value
	state: input | finished ,if finished ,it will do update action to servside
```

- 获取/设置选定的单元格范围
```javascript
xs.sheet.data.selector.range
```
- 为选定的单元格或单元格区域设置单元格值
```javascript
xs.sheet.data.setSelectedCellText(value)
    // the parameters are:
	value:the  value for the cell
```
- 为选定的单元格或单元格区域设置样式
```javascript
xs.sheet.data.setSelectedCellAttr(attributename,value)
    // the parameters are:
	attributename:font-name | font-bold | font-italic | font-size  | format|border|merge|formula |strike|textwrap |underline |align |valign |color|bgcolor|pattern
	value:the  value for the attribute
```

- 设置所选单元格区域的样式
```javascript
xs.sheet.data.setRangeAttr(range,attributename,value)
    // the parameters are:
        range:the cell range ,etc. {sri:0,sci:0,eri:2,eci:2} reprensents range start from cell A1 to C3
	attributename:font-name | font-bold | font-italic | font-size  | format|border|merge|formula |strike|textwrap |underline |align |valign |color|bgcolor|pattern
	value:the  value for the attribute
   for example:
        xs.sheet.data.setRangeAttr({sri:0,sci:0,eri:2,eci:2},'bgcolor','#11ee2a');
```


- 合并选定的单元格区域
```javascript
xs.sheet.data.merge()
```

- 取消合并选定的单元格区域
```javascript
xs.sheet.data.unmerge()
```
- 删除所选单元格内容或清除样式  
```javascript
xs.sheet.data.deleteCell(type)
    // the parameters are:
	type:all|format  all: means delete the cell and clear the style ;format means delete the cell value and keep the cell style
```

- 删除目标单元格区域的单元格内容或清除样式
```javascript
xs.sheet.data.deleteRange(range,type)
    // the parameters are:
        range:the cell range ,etc. {sri:0,sci:0,eri:2,eci:2} reprensents range start from cell A1 to C3
	type:all|format  all: means delete the cell and clear the style ;format means delete the cell value and keep the cell style
```



-  获取列的宽度 
```javascript
xs.sheet.data.cols.sumWidth(min,max)
    // the parameters are:
	min:the start column index
	max:the end column index,not include
```



-  获取行的高度 
```javascript
xs.sheet.data.rows.sumHeight(min,max)
    // the parameters are:
	min:the start row index
	max:the end row index,not include
```

-  获取/设置显示方向
```javascript
xs.sheet.data.displayRight2Left
```

## 事件回调
- 我们可以追踪以下事件
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
- 预检事件
  如果返回 false，插入/删除操作将不会继续。
```javascript
  xs.checkRowInsert = (ri, size) => { if (ri % 2 == 1) return true; else return false; };
  xs.checkColumnInsert = (ci, size) => { if (ci % 2 == 1) return true; else return false; };
  xs.checkRowDelete = (ri, size) => { if (ri % 2 == 1) return true; else return false; };
  xs.checkColumnDelete = (ci, size) => { if (ci % 2 == 1) return true; else return false; };
```

## 自定义

- 设置主页图标和链接
```javascript
xs.sheet.menubar.icon.setHomeIcon(iconUrl,targetUrl)
    // the parameters are:
	iconUrl:the home icon URL
	targetUrl:the target link URL
	for example ,the below code will set the new logo and with link to google.com
	xs.sheet.menubar.icon.setHomeIcon('https://forum.aspose.com/letter_avatar_proxy/v4/letter/y/3e96dc/45.png','https://www.google.com')
```
- 显示菜单栏
```javascript
xs.sheet.menubar.show()
```

- 隐藏菜单栏
```javascript
xs.sheet.menubar.hide()
```
## 形状对象的API
- 更改形状对象的背景颜色
```javascript
    setBackgroundColor(color)
    // the parameters are:
        color: the html color value in hex string value
    //for example,we assume shape 0 existed,this will set the background color to Yellow 
     const ashape=xs.sheet.data.shapes[0];
     ashape.setBackgroundColor('#FFFF00');
```

## 用于TextBox对象的API
TextBox是一种特殊类型的形状，其类型属性为:"TextBox"
例如：以下代码将显示哪种形状是文本框

```javascript
for (let shape of xs.sheet.data.shapes) {
    if (shape.type === 'TextBox') {
        console.log(shape.id + ' is a textbox');
    }
}
```

- 为文本框对象应用字体设置
```javascript
    setFont(fontsettings)
    // the parameter is:
        fontsettings:   {'name':'Arial', 'size':12, 'bold':true, 'color':'#FFFF00', 'italic':true} ,the properties are 'name', 'size', 'bold', 'color', 'italic',they are all optional.
    //for example,we assume shape 0 is a textbox object,this will set the font color to Yellow ,and font size to 12pt,and bold the font. 
     const textbox=xs.sheet.data.shapes[0];
     const fontsettings= {'name':'Arial', 'size':12, 'bold':true, 'color':'#FFFF00'}; 
     textbox.setFont(fontsettings);
```
- 自动更改背景颜色和文本颜色以实现视觉效果
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

有关详细信息，您可以在此处查看示例
<https://github.com/aspose-cells/Aspose.Cells.Grid-for-.NET/tree/master/Examples_GridJs>





