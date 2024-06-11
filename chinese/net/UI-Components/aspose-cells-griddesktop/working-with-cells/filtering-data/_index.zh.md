---
title: 过滤数据
type: docs
weight: 100
url: /zh/net/aspose-cells-griddesktop/filtering-data/
keywords: GridDesktop,筛选,筛选数据,自动筛选,行筛选
description: 本文介绍了如何在 GridDesktop 的工作表中筛选数据。
---

{{% alert color="primary" %}} 

**Aspose.Cells.GridDesktop** 为用户提供了自动筛选和自定义数据筛选功能。使用这些功能，您可以从工作表中仅选择您想要在列表中显示的项目。此外，您还可以根据设定的条件筛选列表中的项目。您可以使用自动筛选/自定义数据筛选功能筛选文本、数字或日期。

您可以使用 **RowFilterSettings** 类的 **EnableAutoFilter** 布尔属性来为 GridDesktop 控件启用自动筛选功能。该类还有一些其他属性可供使用，例如 **HeaderRow**、**StartRow** 和 **EndRow** 用于指定标题行、开始行和结束行索引。**Criteria** 属性用于设置自定义过滤条件。该类还有一个名为 **FilterRows** 的方法，根据给定的条件获取筛选行。

GridDesktop 也支持 RowFilter 中的“包含”类型搜索（不区分大小写）。您可以使用 **GridColumn** 类的 **IgnoreCase** 属性来指定大小写敏感性属性。该类还可以使用名为 **IsStartWithCriteria** 的属性来指示 RowFilter 是否在列上使用 StartWith 标准；属性的默认值设置为 false。

{{% /alert %}} 
## **过滤数据**
在此示例中，我们实现了自动筛选和自定义数据筛选功能。我们在 GridDesktop 中填充一些数据列表，启用自动筛选功能，然后基于一些条件搜索筛选的行。
### **自动筛选**


{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-FilteringData-AutoFilter.cs" >}}
### **自定义数据筛选**


{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-FilteringData-CustomFilter.cs" >}}
