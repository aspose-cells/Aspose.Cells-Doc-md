---
title: 筛选数据
type: docs
weight: 80
url: /zh/net/aspose-cells-gridweb/filter-data/
keywords: GridWeb，筛选，筛选数据，数据筛选
description: 本文介绍了如何在GridWeb中对数据进行筛选。
---

{{% alert color="primary" %}} 

Aspose.Cells.GridWeb提供自动筛选和自定义数据筛选功能。这些功能使您能够选择要在工作表中显示在列表中的项目。此外，您可以根据设定的条件筛选列表中的项目。使用筛选功能可以筛选文本、数字或日期。

{{% /alert %}} 
## **使用筛选功能**
使用工作表的AddAutoFilter方法启用工作表的自动筛选。该方法接受行号、开始和结束列索引。

要启用自定义筛选，使用工作表的AddCustomFilter方法，该方法接受要应用筛选的行索引和自定义筛选条件。

下面的示例实现了自动和自定义数据筛选。在示例中，启用了自动筛选功能，并根据一些条件搜索筛选行。

**输入：第一个工作表中的数据列表** 

![todo:image_alt_text](filter-data_1.jpg)

**输出：启用自动筛选功能** 

![todo:image_alt_text](filter-data_2.jpg)
### **自动筛选**
{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-SetAutoFilter.aspx-SetAutoFilter.cs" >}}
### **自定义数据筛选**
**根据条件自定义筛选数据** 

![todo:image_alt_text](filter-data_3.jpg)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-SetCustomFilter.aspx-SetCustomFilter.cs" >}}
