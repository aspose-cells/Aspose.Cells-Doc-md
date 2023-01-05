---
title: 过滤数据
type: docs
weight: 100
url: /zh/net/filtering-data/
---
{{% alert color="primary" %}} 

**Aspose.Cells.GridDesktop**为用户提供自动过滤和自定义数据过滤功能。使用这些功能，您可能会找到一种方法来仅从工作表中选择您想要在列表中显示的那些项目。此外，您可以根据设定的标准过滤列表中的项目。您可以使用自动筛选/自定义数据筛选功能筛选文本、数字或日期。

您可以使用**启用自动过滤**的布尔属性**行过滤器设置**类以启用 GridDesktop 控件的自动筛选功能。您可以使用该类的其他一些属性，例如**表头行** , **起始行**和**结束行**指定标题、开始和结束行索引。这**标准**属性用于设置自定义过滤条件。该类还有一个名为**过滤行**根据给定条件获取过滤后的行。

 RowFilter 中的“包含”类型搜索（不区分大小写）属性也受 GridDesktop 支持。你可以使用**忽略大小写**的财产**网格列**类来指定您需要的区分大小写属性。您还可以使用名为**IsStartWithCriteria**的**网格列**指示 RowFilter 是否在列上使用 StartWith 条件的类；该属性的默认值设置为 false。

{{% /alert %}} 
## **过滤数据**
我们在此示例中实现了自动筛选和自定义数据筛选功能。我们在 GridDesktop 中填充一些数据列表，启用自动筛选功能，然后根据一些条件搜索筛选的行。
### **自动过滤**


{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-FilteringData-AutoFilter.cs" >}}
### **自定义数据过滤器**


{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-FilteringData-CustomFilter.cs" >}}
