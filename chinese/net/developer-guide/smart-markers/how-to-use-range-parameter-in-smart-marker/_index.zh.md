---
title: 如何在智能标记中使用范围参数
type: docs
weight: 10
url: /zh/net/how-to-use-range-parameter-in-smart-markers/
---

## **在智能标记中使用范围参数的原因**
智能标记中的范围参数用于在用数据源（如JSON、数据库）填充Excel模板时，精确控制数据的放置位置和方式。它有助于管理动态数据输出，特别是在处理可变长度数组或复杂分组时。

1. 控制数据位置并避免重叠：当数据源包含动态数组（例如每条记录的元素数量不同）时，范围参数确保数据在定义的Excel范围内填充，防止溢出到相邻单元格或区域。

2. 处理动态数组公式：对于如转置动态数组（如 &=TRANSPOSE(DataArray)）的操作，范围参数确保输出根据实际数据大小进行调整，不会留下残留值（例如空字段中的零）来自以前的操作。

3. 支持分组和层级数据：当数据需要分组（如嵌套JSON结构）时，范围参数帮助定义层级输出区域。例如，将记录分组在父类别下，无需手动调整行。没有定义范围时，智能标记可能无法准确表示嵌套关系，特别是在数据源没有明确层级时。

4. 改善模板设计和一致性：通过指定范围，确保格式、公式和边框在输出区域内应用一致，避免生成的报告中单元格样式不一致或公式断裂的问题。

5. 优化性能和数据排序：范围参数允许工具在填充模板前预先排序数据源，确保分组数据按正确顺序出现。

## **在智能标记中使用范围参数的方法**
有时候，您需要对智能标记中的范围进行排序或执行其他操作。Aspose.Cells 允许在智能标记中使用范围参数。请查看[模板文件](range.xlsx)、[json文件](range.json)以及以下代码生成的输出Excel文件的截图。

|**显示smart标记的range.xlsx文件的第一个工作表。**|
| :- |
|![todo:image_alt_text](range_template.png)|

|**输出Excel文件的截图。**|
| :- |
|![todo:image_alt_text](range_result.png)|

如下所示的Json数据：
```json data
{
  "Groups": [
    {
      "Materials": [
        { 
	        "Name": "BBB", 
	        "DSSection": { "Name": "Item B" } 
	      },
        {
          "Name": "CCC",
          "DSSection": { "Name": "Item C" }
        },
        {
          "Name": "AAA",
          "DSSection": { "Name": "Item A" }
        },        
        {
          "Name": "BBB",
          "DSSection": { "Name": "Item A" }
        },
        {
          "Name": "CCC",
          "DSSection": { "Name": "Item A" }
        },
        {
          "Name": "BBB",
          "DSSection": { "Name": "Item A" }
        },
        { 
	        "Name": "AAA", 
	        "DSSection": { "Name": "Item C" } 
        }
      ]
    }
  ]
}
```
以下示例演示了其工作原理。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "SmartMarkers-Using-Range-Parameter.cs" >}}
{{< app/cells/assistant language="csharp" >}}
