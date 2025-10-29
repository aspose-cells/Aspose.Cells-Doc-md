---
title: 智能导入变量数组到Excel
type: docs
weight: 30
url: /zh/net/how-to-import-variable-arrays-with-smart-markers/
---

## **为什么用变量数组进行智能标记**
Variable arrays (e.g., <<products[0].name>> or <<foreach item in cart>>) enable dynamic handling of repeated data structures in templates. They solve limitations of flat/nested objects when dealing with lists, tables, or collections.

1. 动态重复无需硬编码：静态标记对可变长度的数据（例如订单项、用户权限）不起作用。数组动态迭代。 
2. 简化聚合：直接计算总和、平均值或筛选。避免在模板中手动编写JavaScript/C#逻辑。
3. 表格/列表数据表示：自然匹配：表格、网格和列表本质上映射到数组。
4. 内存效率：数组降低模板复杂性和数据绑定开销。
5. 与API/数据源集成：符合以JSON/数组为中心的数据（例如REST API）。

## **如何使用智能标记导入变量数组**
以下示例代码展示了如何在智能标记中使用变量数组。我们将变量数组标记动态地放置到工作簿的第一个工作表的A1单元格中，其中包含我们为标记设置的值字符串，处理标记以将数据填充到标记的单元格中。最后，我们保存Excel文件。


{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-UsingVariableArray-1.cs" >}}

## **如何使用智能标记导入HTML属性**
The following sample code explains the use of HTML property of the Smart Markers. When it will be processed, it will show "World" in "Hello World" as bold because of HTML <b> tag.


{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-UsingHTMLProperty-1.cs" >}}

{{< app/cells/assistant language="csharp" >}}
