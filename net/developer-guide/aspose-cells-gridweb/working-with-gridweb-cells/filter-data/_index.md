---
title: Filter Data
type: docs
weight: 80
url: /net/filter-data/
---

{{% alert color="primary" %}} 

Aspose.Cells.GridWeb provides auto-filter and custom data filter features. These features give you a way to select only those items in a worksheet that you want to display in a list. Moreover, you can filter items in a list according to set criteria. Filter text, numbers or dates with the filtering features.

{{% /alert %}} 
## **Working with Filters**
Use the worksheet AddAutoFilter method to enable auto-filter for a worksheet. This method accepts the row, start and end column indexes.

To enable custom filter, use the worksheet AddCustomFilter method which accepts the row index to which filter has to be applied and the custom filtering criteria.

The example below implements both auto- and custom data filters. In the example, the auto-filter feature is enabled and filtered rows are searched based on some criteria.

**Input: the data list in the first worksheet** 

![todo:image_alt_text](filter-data_1.jpg)

**Output: enable auto-filter feature** 

![todo:image_alt_text](filter-data_2.jpg)
### **Auto-filter**
{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-SetAutoFilter.aspx-SetAutoFilter.cs" >}}
### **Custom Data Filter**
**Custom filtered data based on the criteria** 

![todo:image_alt_text](filter-data_3.jpg)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-SetCustomFilter.aspx-SetCustomFilter.cs" >}}
