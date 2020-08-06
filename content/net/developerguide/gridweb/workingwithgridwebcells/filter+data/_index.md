---
title : "Filter Data" 
description : "" 
weight : 16717 
toc : false
type: docs
url: /net/developerguide/gridweb/workingwithgridwebcells/filter+data/
---

# Aspose.Cells for .NET : Filter Data


Aspose.Cells.GridWeb provides auto-filter and custom data filter features. These features give you a way to select only those items in a worksheet that you want to display in a list. Moreover, you can filter items in a list according to set criteria. Filter text, numbers or dates with the filtering features.

{{< panel title="Contents Summary" style="primary" >}}
*   1 [Working with Filters](#working-with-filters)
    *   1.1 [Auto-filter](#auto-filter)
    *   1.2 [Custom Data Filter](#custom-data-filter)
{{< /panel >}}
 

## Working with Filters

Use the worksheet `AddAutoFilter` method to enable auto-filter for a worksheet. This method accepts the row, start and end column indexes.

To enable custom filter, use the worksheet `AddCustomFilter` method which accepts the row index to which filter has to be applied and the custom filtering criteria.

The example below implements both auto- and custom data filters. In the example, the auto-filter feature is enabled and filtered rows are searched based on some criteria.

**Input: the data list in the first worksheet**  
![image](5115380.jpg)

**Output: enable auto-filter feature**  
![image](5115379.jpg)

### Auto-filter

### Custom Data Filter

**Custom filtered data based on the criteria**  
![image](5115378.jpg)

