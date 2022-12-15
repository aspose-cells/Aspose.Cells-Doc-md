---
title: 过滤数据
type: docs
weight: 80
url: /zh/net/filter-data/
---
{{% alert color="primary" %}} 

Aspose.Cells.GridWeb 提供自动过滤和自定义数据过滤功能。这些功能使您可以只选择工作表中要显示在列表中的那些项目。此外，您可以根据设置的条件过滤列表中的项目。使用过滤功能过滤文本、数字或日期。

{{% /alert %}} 
## **使用过滤器**
使用工作表 AddAutoFilter 方法为工作表启用自动筛选。此方法接受行、开始和结束列索引。

要启用自定义过滤器，请使用工作表 AddCustomFilter 方法，该方法接受必须应用过滤器的行索引和自定义过滤条件。

下面的示例实现了自动和自定义数据过滤器。在该示例中，启用了自动筛选功能，并根据某些条件搜索筛选的行。

**输入：第一个工作表中的数据列表** 

![待办事项：图像_替代_文本](filter-data_1.jpg)

**输出：启用自动过滤功能** 

![待办事项：图像_替代_文本](filter-data_2.jpg)
### **自动过滤**
{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-SetAutoFilter.aspx-SetAutoFilter.cs" >}}
### **自定义数据过滤器**
**根据条件自定义过滤数据** 

![待办事项：图像_替代_文本](filter-data_3.jpg)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-SetCustomFilter.aspx-SetCustomFilter.cs" >}}
