---
title: 智能导入与放置数据，配合智能标记
linktitle: 智能标记
type: docs
weight: 190
url: /zh/net/using-smart-markers/
description: 根据模板Excel文件使用Aspose.Cells库智能地导入并放置数据
---

## **为何使用智能标记导入数据到Excel**
利用智能标记导入数据到Excel实现数据集成的简化，通过模板设计和动态绑定结合。这种方法在如 Aspose.Cells 的工具中特别有价值，标记作为模板中的占位符，自动填充来自各源的数据。以下是采用此方法的主要原因：

1. 提高重复报告的效率：模板重复利用，预设计Excel模板内嵌标记（例如 &=$VariableName, &=DataSource.Field），可在多个数据集间重用，省去手动重新格式化。例如，财务报告或库存表只需更新数据源，无需重建布局。自动数据绑定，智能标记直接连接到数据源（如数据库、JavaBeans、数组），源数据变化后，处理完毕自动反映在Excel文件中，减少复制粘贴错误。

2. 支持复杂数据结构：多数据源整合，一个模板可合并来自不同来源（变量、数组、ResultSet）的数据。层次化数据处理，嵌套数据（如分组记录）可用标记如 &=subtotal9:Person.id 生成各组的总和（求和、平均）直接在Excel中。

3. 保留Excel功能：智能标记与Excel中的公式、条件格式和图表共存。例如：利用 &==C{r}*D{r} 在数据注入时动态计算行特定公式。模板保持预定义样式（如标题、单元格颜色），确保一致性，无需后期调整。

4. 高级自动化功能：自定义数据源集成，开发者可实现如 ICellsDataTable（在.NET中）接口，将专有数据结构映射到标记。这支持从API或传感器实时采集数据。批量处理，工具如 Aspose.Cells 的 WorkbookDesigner 支持批量操作（例如一次性生成 1000+ 发票），通过循环多个数据集实现。

5. 降低开发与维护成本：逻辑与设计分离，设计人员在Excel中管理模板（无需编码），开发者处理数据逻辑。此分工加快迭代速度。错误减少，自动数据映射降低手工录入风险。例如，VC++中的传感器数据分析可以通过对象接口自动填充到Excel模板，避免转录错误。

## **导入包含Smart Markers的DataTable的示例代码**
以下示例代码中，数据源有6条记录。我们只希望在一张工作表中显示3条记录，其余会自动转移到第二张工作表。请注意，第二张工作表也要有同样的智能标记标签，并调用 [WorkbookDesigner.Process(sheetIndex, isPreserved)](https://reference.aspose.com/cells/net/aspose.cells.workbookdesigner/process/methods/2) 方法处理两个表单。请查看由代码生成的[输出Excel文件](SmartMarkerDataTableToExcel.xlsx)作为参考。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "SmartMarkers-ImportDataTableToExcel.cs" >}}

## **导入带智能标记的JSON数据示例代码**
Aspose.Cells for .NET支持智能标记中的json数据。示例代码加载表格模板，智能导入JSON数据进行填充，然后计算表格数据。请查看[模板文件](table.xlsx)、[json文件](table.json)以及使用以下代码生成的输出Excel文件的截图。

|**显示smart markers的table.xlsx文件的第一个工作表。**|
| :- |
|![todo:image_alt_text](tabletemplate.png)|

|**输出Excel文件的截图。**|
| :- |
|![todo:image_alt_text](tableresult.png)|

如下所示的Json数据：
```json data
{
	"Items" : [
		{
			"ItemName" : "A123",
			"Description" : "Peonies",
			"Qty" : "55",
			"UnitPrice" : "3.05"			
		},
		{
			"ItemName" : "B456",
			"Description" : "Tulips",
			"Qty" : "45",
			"UnitPrice" : "2.66",
		},
		{
			"ItemName" : "K789",
			"Description" : "Buttercup",
			"Qty" : "68",
			"UnitPrice" : "8.35",
		}
	]
}
```
以下示例演示了其工作原理。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "SmartMarkers-ImportJsonToTable.cs" >}}

## **带智能标记的导入嵌套对象示例代码**
Aspose.Cells支持智能标记中的嵌套对象，这些嵌套对象应该是简单的。我们使用一个简单的模板文件。查看包含一些嵌套智能标记的设计电子表格。

|**SM_NestedObjects.xlsx文件的第一个工作表显示嵌套智能标记。**|
| :- |
|![todo:image_alt_text](using-smart-markers_7.png)|
以下示例演示了其工作原理。


{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-UsingNestedObjects-1.cs" >}}


## **高级主题**
- [智能标记参数](/cells/zh/net/smart-marker-parameters/)
- [格式化智能标记](/cells/zh/net/adding-anonymous-or-custom-object-into-smartmarkers/)
- [如果数据太大，可以将智能标记数据自动填充到其他工作表](/cells/zh/net/auto-populate-smart-marker-data-to-other-worksheets-if-data-is-too-large/)
- [为WorkbookDesigner设置自定义数据源](/cells/zh/net/formatting-smart-markers/)
- [在使用智能标记合并数据时获取通知](/cells/zh/net/getting-notifications-while-merging-data-with-smart-markers/)
- [为WorkbookDesigner设置自定义数据源](/cells/zh/net/set-custom-datasource-for-workbookdesigner/)
- [在单元格中显示前导撇号](/cells/zh/net/show-leading-apostrophe-in-cells/)
- [在智能标记变量名为Test及其数据源名称也为Test中嵌入公式的下面样本代码是这样子的 **&=$Test(formula)**，在执行代码后，[最终的输出Excel文件](47153156.xlsx)将在A1到A5单元格中具有公式。](/cells/zh/net/using-formula-parameter-in-smart-marker-field/)
- [智能导入数组元素到Excel（按索引）](/cells/zh/net/how-to-import-array-element-by-index-with-smart-markers/)
- [智能导入数组元素到Excel（按切片）](/cells/zh/net/how-to-import-array-element-by-slicer-with-smart-markers/)
- [智能导入JSON到Excel](/cells/zh/net/how-to-import-json-into-excel-with-smart-markers/)
- [智能导入嵌套对象到Excel](/cells/zh/net/how-to-import-nested-objects-with-smart-markers/)
- [智能导入变量数组到Excel](/cells/zh/net/how-to-import-variable-arrays-with-smart-markers/)
- [如何在智能标记中使用图片标记](/cells/zh/net/how-to-use-image-markers-in-smart-markers/)
- [如何在智能标记中进行数据分组](/cells/zh/net/how-to-group-data-in-smart-markers/)

{{< app/cells/assistant language="csharp" >}}
