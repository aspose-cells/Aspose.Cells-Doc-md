---
title: 使用 GridJs 客户端
type: docs
weight: 250
url: /zh/net/aspose-cells-gridjs/client/
---
# 使用 GridJs 客户端
我们开发了基于GridJs的客户端[x-电子表格](https://github.com/myliang/x-spreadsheet).

## 主要步骤是：

- 创建 x_spreadsheet 实例
```javascript
xs = x_spreadsheet(id, options)
```
- 加载json数据
```javascript
xs.loadData(jsondata.data)
```
- 设置活动表
```javascript
xs.setActiveSheetByName(jsondata.actname)
```
- 设置活动单元格
```javascript
xs.setActiveCell(jsondata.actrow,jsondata.actcol);
```

例如下面的代码初始化一个 x_spreadsheet 对象。
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
 // 选项的参数：
 updateMode：目前我们只支持'server'
 updateUrl：根据json设置更新动作的服务端url
模式：读取表示只读电子表格/编辑表示我们可以编辑电子表格
showToolbar：表示是否显示工具栏
showFileName：是否显示文件名
local: 支持多语言菜单，locale 可以是：en, cn, es, pt, de, ru, nl for english,chinese,Spanish,Portuguese,germany,Russian,Dutch
 showContextmenu：表示是否在右键单击单元格时显示上下文菜单
## 

___
## 其他有用的api
- 渲染视图
```javascript
xs.reRender()
```
- 获取选定的图像/形状...如果没有选择将返回 null
```javascript
xs.sheet.selector.getObj()
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
	state: input | finished
```

- 获取/设置选中的单元格范围
```javascript
xs.sheet.data.selector.range
```
- 为选中的单元格或单元格区域设置单元格值
```javascript
xs.sheet.data.setSelectedCellText(value)
    // the parameters are:
	value:the  value for the cell
```
- 设置所选单元格或单元格区域的样式
```javascript
xs.sheet.data.setSelectedCellAttr(attributename,value)
    // the parameters are:
    attributename:font-name | font-bold | font-italic | font-size  | format|border|merge|formula |strike|textwrap |underline |align |valign |color|bgcolor|pattern
	value:the  value for the attribute
```

- 合并选中的单元格区域
```javascript
xs.sheet.data.merge()
```

- 取消合并选定的单元格区域
```javascript
xs.sheet.data.unmerge()
```
- 删除选定的单元格
```javascript
xs.sheet.data.deleteCell(what)
    // the parameters are:
    what:all|format  all: means delete the cell and clear the style ;format means delete the cell value and keep the cell style
```
- 设置冻结窗格
```javascript
xs.sheet.data.setFreeze(ri,ci)
    // the parameters are:
    ri:row index 
	ci:column index
```

- 在所选单元格中插入行或列
```javascript
xs.sheet.data.insert(type, n)
    // the parameters are:
    type: row | column
	n:the row or column number
```
- 删除所选单元格中的行或列
```javascript
xs.sheet.data.delete(type)
    // the parameters are:
    type: row | column
```

- 设置列的宽度
```javascript
xs.sheet.data.setColWidth(ci,width)
    // the parameters are:
    ci:column index
	width:the width for the column
```
- 获取列的宽度
```javascript
xs.sheet.data.cols.sumWidth(min,max)
    // the parameters are:
    min:the start column index
	max:the end column index,not include
```

- 设置行的高度
```javascript
xs.sheet.data.setRowHeight(ri,height)
    // the parameters are:
    ri:row index
	height:the height for the row
```
- 获取行的高度
```javascript
xs.sheet.data.rows.sumHeight(min,max)
    // the parameters are:
    min:the start row index
	max:the end row index,not include
```
- 获取/设置显示方向
```javascript
xs.sheet.data.displayRight2Left
```



有关详细信息，您可以在此处查看示例
<https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Examples_GridJs>



 
 
