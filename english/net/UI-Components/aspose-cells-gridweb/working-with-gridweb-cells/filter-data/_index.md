---
title: Filter Data
type: docs
weight: 80
url: /net/aspose-cells-gridweb/filter-data/
keywords: GridWeb,filter,filter data,data filtering
description: This article introduces how to filter data in GridWeb.
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}} 

Aspose.Cells.GridWeb provides AutoFilter and custom data filter features. These features allow you to select only those items in a worksheet that you want to display in a list. Moreover, you can filter items in a list according to set criteria. Filter text, numbers, or dates with the filtering features.

{{% /alert %}} 
## **Working with Filters**
Use the `Worksheet.AddAutoFilter` method to enable AutoFilter for a worksheet. This method accepts the row index, start column index, and end column index.

To enable a custom filter, use the `Worksheet.AddCustomFilter` method, which accepts the row index to which the filter has to be applied and the custom filtering criteria.

The example below implements both AutoFilter and custom data filters. In the example, the AutoFilter feature is enabled, and filtered rows are retrieved based on some criteria.

**Input: The data list in the first worksheet** 

![todo:image_alt_text](filter-data_1.jpg)

**Output: AutoFilter feature enabled** 

![todo:image_alt_text](filter-data_2.jpg)
### **Auto-filter**
{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-SetAutoFilter.aspx-SetAutoFilter.cs" >}}
### **Custom Data Filter**
**Custom‑filtered data based on the criteria** 

![todo:image_alt_text](filter-data_3.jpg)

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-SetCustomFilter.aspx-SetCustomFilter.cs" >}}
