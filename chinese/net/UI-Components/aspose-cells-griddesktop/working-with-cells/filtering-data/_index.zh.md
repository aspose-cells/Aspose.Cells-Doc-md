---
title: 筛选数据
type: docs
weight: 100
url: /zh/net/aspose-cells-griddesktop/filtering-data/
keywords: GridDesktop,筛选,筛选数据,自动筛选,行筛选
description: 本文介绍了如何在GridDesktop的工作表中筛选数据。
---

{{% alert color="primary" %}} 

**Aspose.Cells.GridDesktop**为用户提供了自动筛选和自定义数据筛选功能。 使用这些功能，您可以找到一种方法，只选择您要在列表中显示的工作表中的项目。 此外，您还可以根据设定的标准筛选列表中的项目。 您可以使用自动筛选/自定义数据筛选功能筛选文本、数字或日期。

您可以使用**RowFilterSettings**类的**EnableAutoFilter**布尔属性启用GridDesktop控件的自动筛选功能。 该类还具有其他属性，例如**HeaderRow**，**StartRow**和**EndRow**，用于指定标题、开始和结束行索引。 **Criteria**属性用于设置自定义筛选条件。 该类还有一个名为**FilterRows**的方法，用于根据给定条件获取经过筛选的行。

GridDesktop还支持RowFilter中的"包含"类型搜索(不区分大小写)属性。 您可以使用**GridColumn**类的**IgnoreCase**属性指定您的需求的大小写敏感属性。 您还可以使用**GridColumn**类的名为**IsStartWithCriteria**的属性指示RowFilter是否在列上使用StartWith标准；该属性的默认值设置为false。

{{% /alert %}} 
## **筛选数据**
在此示例中，我们实现了自动筛选和自定义数据筛选功能。 我们在GridDesktop中填充一些数据列表，启用自动筛选功能，然后根据一些条件搜索筛选的行。
### **自动筛选**


{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-FilteringData-AutoFilter.cs" >}}
### **自定义数据筛选**


{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-FilteringData-CustomFilter.cs" >}}
