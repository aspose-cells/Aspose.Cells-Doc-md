---
title: 配置参数
type: docs
weight: 10
url: /zh/jasperreports/configuration-parameters/
---

{{% alert color="primary" %}} 

以下表列出了配置参数。 

{{% /alert %}} 

|**参数名称** |**描述** |
| :- | :- |
|FORMAT_TYPE |可以设置为"EXCEL97TO2003"或"EXCEL2007"，以生成Microsoft Excel 79 0 2003或Excel 2007格式的文件。|
|IS_ONE_PAGE_PER_SHEET |一个布尔值，指定是否每个报表页面都应写入不同的XLS工作表。|
|IS_REMOVE_EMPTY_SPACE_BETWEEN_ROWS |一个布尔值，指定是否应该删除可能出现在行之间的空白或不删除。|
|IS_REMOVE_EMPTY_SPACE_BETWEEN_COLUMNS |一个布尔值，指定是否应该删除可能出现在列之间的空白或不删除。|
|IS_WHITE_PAGE_BACKGROUND |一个布尔值，指定页面背景应该是白色还是默认的XLS背景颜色。XLS背景颜色可能根据XLS查看器属性或操作系统颜色方案而有所不同。|
|IS_DETECT_CELL_TYPE |用于指示导出器是否应考虑原始文本字段表达式的类型，并相应地设置单元格类型和值的标志。|
|SHEET_NAMES |表示自定义工作表名称的字符串数组。在与IS_ONE_PAGE_PER_SHEET参数一起使用时很有用。|
|IS_FONT_SIZE_FIX_ENABLED |用于减小字体大小以使文本适合指定的单元高度的标志。|
|MAXIMUM_ROWS_PER_SHEET |一个整数值，指定允许在工作表中显示的最大行数。当设置时，将为剩余的行创建一个新工作表以显示。负值或零表示未设置限制。|
|IS_IGNORE_GRAPHICS |用于忽略图形元素并仅导出文本元素的标志。|
|IS_COLLAPSE_ROW_SPAN |用于折叠行跨度并避免跨行合并单元格的标志。|
|IS_IGNORE_CELL_BORDER |用于忽略单元格边框的标志。|
|IS_USE_EXCEL_CHART |用于在Microsoft Excel格式中使用可编辑的图表而不是静态图片的标志。默认值为true。|

