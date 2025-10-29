---
title: 智能导入主表和明细数据到Excel与智能标记
type: docs
weight: 30
url: /zh/net/how-to-use-master-and-details-with-smart-markers/
---

## **可能的使用场景**
有时，你希望生成动态Excel报告，包括一个全面的主控面板和多个细粒度的明细工作表。其中，一个主表显示概览，可能展示各种产品变体，而每个对应的详细工作表提供单一变体的具体和深入数据。Aspose.Cells可以通过主表和明细表与智能标记完美满足你的需求。


## **主表和明细表的智能标记参数**
要将主表和明细表数据导入Excel，你需要使用以下智能标记参数：

| 参数 | 描述 | 允许的值（语法） | 限制 | 可选 | 默认行为 | Excel约束 |
| --- | --- | --- | --- | --- | --- | --- |
| `DetailSheet` | 指定存储在模板文件中的明细工作表名称。 | 字符串值 | 值必须为空或工作表名称。如果为空，为明细工作表。它应该是一个简单字符串值。不支持变量。 | 如果省略，则不是主或明细工作表。 | 普通工作表，不是主或明细工作表。 | |
| `DetailTable` | 指定模板文件中明细工作表的表名。 | 字符串值 | | 如果省略，明细工作表中的智能标记应该与主表类似，否则无法找到数据源。 | 如果省略，明细工作表中的智能标记应该与主表类似，否则无法找到数据源。 | |
| `DetailSheetNewName` | 指定新创建的明细工作表的名称。 | 类似Excel公式的表达式 | 如果用简单值替换变量（{a.bc}）应是有效的Excel公式。 | 如果省略，新工作表将是Sheet1、Sheet2... | 如果省略，新工作表将是Sheet1、Sheet2... | 名称必须是有效的工作表名称。 |
| `DetailLink` | 指示是否在导入数据的位置添加超链接。 | | |如果省略，不添加超链接到导入数据的位置。 | 如果省略，不添加超链接到导入数据的位置。 | |

## **如何在主表和明细都在一张工作表时使用主表和明细**
有时，你需要在SmartMarkers中将主表和明细数据导入Excel。Aspose.Cells支持在SmartMarkers中使用主表和明细参数。请检查[模板文件](MasterDetailInOneSheet.xlsx)、[json文件](MasterDetailData.json)以及用以下代码生成的输出Excel文件截图。

|**template.xlsx的第一个工作表**|
| :- |
|![todo:image_alt_text](1.png)|

|**输出Excel文件的第一个工作表**|
| :- |
|![todo:image_alt_text](2.png)|

|**输出Excel文件的第二个工作表**|
| :- |
|![todo:image_alt_text](3.png)|

如下所示的Json数据：
```json data
{
	"node": {
		"Styles1": [
			{
				"StyleID": "1style001",
				"StyleName": "StyleName1",
				"Quantity": 6,
				"UnitPrice": 18.45,
				"MaterialType":"Cotton"
			}
		],
		"Styles2": [
			{
				"StyleID": "2style001",
				"StyleName": "Cotton StyleName2",
				"Quantity": 6,
				"UnitPrice": 18.45,
				"MaterialType":"Cotton"
			},
			{
				"StyleID": "2style002",
				"StyleName": "Denim StyleName2",
				"Quantity": 8,
				"UnitPrice": 58.8,
				"MaterialType":"Denim"
			}
		]
	}
}
```
以下示例演示了其工作原理。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "SmartMarkers-Using-Master-Details-InOneSheet.cs" >}}

## **在不同工作表中使用主表和明细的操作方法**
有时，你需要在SmartMarkers中将主表和明细数据导入Excel。Aspose.Cells支持在SmartMarkers中使用主表和明细参数。请检查[模板文件](MasterDetailInTwoSheets.xlsx)、[json文件](MasterDetailData.json)以及用以下代码生成的输出Excel文件截图。

|**模板.xlsx的第一主工作表。**|
| :- |
|![todo:image_alt_text](4.png)|

|**模板.xlsx的第二主工作表。**|
| :- |
|![todo:image_alt_text](5.png)|

|**模板.xlsx的详细工作表。**|
| :- |
|![todo:image_alt_text](6.png)|

|**输出Excel文件的第一主工作表。**|
| :- |
|![todo:image_alt_text](7.png)|

|**输出Excel文件的第二主工作表。**|
| :- |
|![todo:image_alt_text](8.png)|

|**输出Excel文件中第一个主工作表的详细工作表。**|
| :- |
|![todo:image_alt_text](9.png)|

|**输出Excel文件中第二个主工作表的第一个详细工作表。**|
| :- |
|![todo:image_alt_text](10.png)|

|**输出Excel文件中第二个主工作表的第二个详细工作表。**|
| :- |
|![todo:image_alt_text](11.png)|

如下所示的Json数据：
```json data
{
	"node": {
		"Styles1": [
			{
				"StyleID": "1style001",
				"StyleName": "StyleName1",
				"Quantity": 6,
				"UnitPrice": 18.45,
				"MaterialType":"Cotton"
			}
		],
		"Styles2": [
			{
				"StyleID": "2style001",
				"StyleName": "Cotton StyleName2",
				"Quantity": 6,
				"UnitPrice": 18.45,
				"MaterialType":"Cotton"
			},
			{
				"StyleID": "2style002",
				"StyleName": "Denim StyleName2",
				"Quantity": 8,
				"UnitPrice": 58.8,
				"MaterialType":"Denim"
			}
		]
	}
}
```
以下示例演示了其工作原理。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "SmartMarkers-Using-Master-Details-InDifferentSheets.cs" >}}
