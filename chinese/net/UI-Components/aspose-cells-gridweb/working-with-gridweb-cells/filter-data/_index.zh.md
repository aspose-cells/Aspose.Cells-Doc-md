---
title: 筛选数据
type: docs
weight: 80
url: /zh/net/aspose-cells-gridweb/filter-data/
keywords: 本文介绍了如何在GridWeb中筛选数据。
description: Aspose.Cells.GridWeb提供了自动筛选和自定义数据筛选功能。这些功能为您提供了一种选择要在工作表中显示的项的方法。此外，您还可以根据设置的条件筛选列表中的项目。使用筛选功能对文本、数字或日期进行筛选。
---

{{% alert color="primary" %}} 

Aspose.Cells.GridWeb 提供自动筛选和自定义数据筛选功能。这些功能让你可以选择工作表中想要显示的项目，而且你还可以按照一定的标准筛选列表中的项目。使用这些筛选功能，可以按照设定的条件筛选文本、数字或日期。

{{% /alert %}} 
## **处理筛选**
使用工作表的AddAutoFilter方法启用工作表的自动筛选。此方法接受行、起始和结束列索引。

要启用自定义筛选，使用工作表的AddCustomFilter方法，该方法接受要应用筛选的行索引和自定义筛选条件。

下面的示例实现了自动和自定义数据筛选。在示例中，启用了自动筛选功能，并基于一些条件搜索筛选行。

输入：第一个工作表中的数据列表 

![todo:image_alt_text](filter-data_1.jpg)

输出：启用自动筛选功能 

![todo:image_alt_text](filter-data_2.jpg)
### **自动筛选**
{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-SetAutoFilter.aspx-SetAutoFilter.cs" >}}
### **自定义数据筛选**
基于条件的自定义筛选数据 

![todo:image_alt_text](filter-data_3.jpg)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-SetCustomFilter.aspx-SetCustomFilter.cs" >}}
