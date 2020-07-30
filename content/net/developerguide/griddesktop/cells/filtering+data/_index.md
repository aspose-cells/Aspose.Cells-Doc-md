---
title : "Filtering Data" 
description : "" 
weight : 16646 
toc : false
type: docs
url: /net/developerguide/griddesktop/cells/filtering+data/
---

# Aspose.Cells for .NET : Filtering Data


**Aspose.Cells.GridDesktop** provides Auto-Filter and Custom Data Filter features for the users. Using these features, you may find a way to select only those items from the worksheet that you want to display in a list. Moreover, you are allowed to filter items in a list according to a set criteria. You can filter text, numbers or dates with Auto-Filter / Custom Data Filter feature.

You can use **EnableAutoFilter** Boolean attribute of **RowFilterSettings** class to enable the Auto-Filter feature for the GridDesktop control. There are some other properties of the class that you can use, e.g **HeaderRow** , **StartRow** and **EndRow** to specify the header, start and end row indexes. The **Criteria** property is used to set the custom filtering criteria. The class has also a method named **FilterRows** to get the filtered rows based on the given criteria.

The "contains" type search (case-insensitive) attribute in RowFilter is also supported by GridDesktop. You may use **IgnoreCase** property of **GridColumn** class to specify the case sensivity attribute for your need. You can also use a property named **IsStartWithCriteria** of **GridColumn** class to indicate whether the RowFilter uses the StartWith criteria on a column; the default value of the property is set to false.

{{< panel title="Contents Summary" style="primary" >}}
*   1 [Filtering Data](#filtering-data)
    *   1.1 [Auto-Filter](#auto-filter)
    *   1.2 [Custom Data Filter](#custom-data-filter)
{{< /panel >}}
 

 

## Filtering Data

We implement both Auto-Filter and Custom Data Filter features in this example. We fill some data list in the GridDesktop, enable Auto-Filter feature and then search filtered rows based on some criteria.

### Auto-Filter

### Custom Data Filter

## Attachments:

![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Filtering Data-001.png](https://docs2.aspose.com/cells/net/attachments/5017949/5113885.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Filtering Data-002.png](https://docs2.aspose.com/cells/net/attachments/5017949/5115162.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Filtering Data-003.png](https://docs2.aspose.com/cells/net/attachments/5017949/5115164.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Filtering Data-003.png](https://docs2.aspose.com/cells/net/attachments/5017949/5113741.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Filtering Data-002.png](https://docs2.aspose.com/cells/net/attachments/5017949/5113886.png) (image/png)  

