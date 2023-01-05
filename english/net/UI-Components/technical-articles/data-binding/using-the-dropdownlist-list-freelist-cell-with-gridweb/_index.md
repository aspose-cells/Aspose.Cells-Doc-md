---
title: Using the DropDownList, List, FreeList Cell with GridWeb
type: docs
weight: 60
url: /net/using-the-dropdownlist-list-freelist-cell-with-gridweb/
---

{{% alert color="primary" %}} 

With Aspose.Cells, there are various ways to create a dropdown list: ValidationType.DropDownList, List and FreeList all offer this feature. The control supports a value/text pair in dropdown lists, lists and freelists. Use the Validation.ValueList.Add method to add a new value/text pair into the list.

In the code below, "1" is the value of the list item, and "1:test" is the list item's displayed text. 

**C#**

{{< highlight csharp >}}

 // Adds to a bindcolumn

GridWeb1.WebWorksheets[0].BindColumns["CategoryID"].Validation.ValueList.Add("1,1:test");

// Adds to a validation cell

GridWeb1.WebWorksheets[1].Cells["A1"].Validation.ValueList.Add("1,1:test");



{{< /highlight >}}

**VB**

{{< highlight csharp >}}

 ' Adds to a bindcolumn

GridWeb1.WebWorksheets(0).BindColumns("CategoryID").Validation.ValueList.Add("1,1:test")

' Adds to a validation cell

GridWeb1.WebWorksheets(1).Cells("A1").Validation.ValueList.Add("1,1:test")



{{< /highlight >}}

Use the LoadValueList method to load list items from a dataview object: 

**C#**

{{< highlight csharp >}}

 GridWeb1.WebWorksheets[0].BindColumns["CategoryID"].Validation.LoadValueList(dataSet31.Categories.DefaultView, "CategoryID", "CategoryName", true);



{{< /highlight >}}

**VB**

{{< highlight csharp >}}

 GridWeb1.WebWorksheets(0).BindColumns("CategoryID").Validation.LoadValueList(dataSet31.Categories.DefaultView, "CategoryID", "CategoryName", True)



{{< /highlight >}}

{{% /alert %}}
