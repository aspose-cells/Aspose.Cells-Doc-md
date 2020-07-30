---
title : "Using the DropDownList List FreeList Cell with GridWeb" 
description : "" 
weight : 20352 
toc : false
type: docs
url: /net/developerguide/technicalarticles/gridcontrols/databinding/using+the+dropdownlist+list+freelist+cell+with+gridweb/
---

# Aspose.Cells for .NET : Using the DropDownList, List, FreeList Cell with GridWeb


With Aspose.Cells, there are various ways to create a dropdown list: `ValidationType.DropDownList`, `List` and `FreeList` all offer this feature. The control supports a value/text pair in dropdown lists, lists and freelists. Use the `Validation.ValueList.Add` method to add a new value/text pair into the list.

In the code below, "1" is the value of the list item, and "1:test" is the list item's displayed text.

**C#**

{{< code lang="c#" >}}
// Adds to a bindcolumn
GridWeb1.WebWorksheets[0].BindColumns["CategoryID"].Validation.ValueList.Add("1,1:test");

// Adds to a validation cell
GridWeb1.WebWorksheets[1].Cells["A1"].Validation.ValueList.Add("1,1:test");
 
{{< /code >}}

**VB**

{{< code lang="vb" >}}
' Adds to a bindcolumn
GridWeb1.WebWorksheets(0).BindColumns("CategoryID").Validation.ValueList.Add("1,1:test")

' Adds to a validation cell
GridWeb1.WebWorksheets(1).Cells("A1").Validation.ValueList.Add("1,1:test")
 
{{< /code >}}

Use the `LoadValueList` method to load list items from a `dataview` object:

**C#**

{{< code lang="c#" >}}
GridWeb1.WebWorksheets[0].BindColumns["CategoryID"].Validation.LoadValueList(dataSet31.Categories.DefaultView, "CategoryID", "CategoryName", true);
 
{{< /code >}}

**VB**

{{< code lang="vb" >}}
GridWeb1.WebWorksheets(0).BindColumns("CategoryID").Validation.LoadValueList(dataSet31.Categories.DefaultView, "CategoryID", "CategoryName", True)
 
{{< /code >}}

