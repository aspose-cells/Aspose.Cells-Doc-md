---
title: Filtering Data
type: docs
weight: 100
url: /net/aspose-cells-griddesktop/filtering-data/
keywords: GridDesktop,filter,filter data,AutoFilter,RowFilter
description: This article introduces how to filter data in the Worksheet in GridDesktop.
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}} 

**Aspose.Cells.GridDesktop** provides Auto-Filter and Custom Data Filter features for users. Using these features, you can select only those items from the worksheet that you want to display in a list. Moreover, you are allowed to filter items in a list according to a set of criteria. You can filter text, numbers, or dates with the Auto-Filter / Custom Data Filter features.

You can use the **EnableAutoFilter** Boolean attribute of the **RowFilterSettings** class to enable the Auto-Filter feature for the GridDesktop control. There are some other properties of the class that you can use, e.g., **HeaderRow**, **StartRow**, and **EndRow** to specify the header, start, and end row indexes. The **Criteria** property is used to set the custom filtering criteria. The class also has a method named **FilterRows** to get the filtered rows based on the given criteria.

The "contains" type search (case‑insensitive) attribute in RowFilter is also supported by GridDesktop. You may use the **IgnoreCase** property of the **GridColumn** class to specify the case sensitivity as needed. You can also use a property named **IsStartWithCriteria** of the **GridColumn** class to indicate whether the RowFilter uses the StartsWith criteria on a column; the default value of the property is false.

{{% /alert %}} 

## **Filtering Data**
We implement both Auto-Filter and Custom Data Filter features in this example. We fill a data list in the GridDesktop, enable the Auto-Filter feature, and then search filtered rows based on some criteria.

### **Auto-Filter**

{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-FilteringData-AutoFilter.cs" >}}

### **Custom Data Filter**

{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-FilteringData-CustomFilter.cs" >}}
