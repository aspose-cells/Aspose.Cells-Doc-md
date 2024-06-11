---
title: 使用 GridWeb 中的 DropDownList、List、FreeList 单元格
type: docs
weight: 60
url: /zh/net/aspose-cells-gridweb/using-the-dropdownlist-list-freelist-gridweb/
keywords: GridWeb、dropdownlist、freelist、list
description: 本文介绍如何在 GridWeb 中使用 list。
---

{{% alert color="primary" %}} 

使用 Aspose.Cells，有多种方式可以创建下拉列表：ValidationType.DropDownList、List 和 FreeList 都提供了这个功能。该控件支持下拉列表、列表和自由列表中的值/文本对。使用 Validation.ValueList.Add 方法将新的值/文本对添加到列表中。

在下面的代码中，“1”是列表项的值，“1:test”是列表项显示的文本。 

**C#**

{{< highlight csharp >}}

 // Adds to a bindcolumn

GridWeb1.WorkSheets[0].BindColumns["CategoryID"].Validation.ValueList.Add("1,1:test");

// Adds to a validation cell

GridWeb1.WorkSheets[1].Cells["A1"].Validation.ValueList.Add("1,1:test");



{{< /highlight >}}

**VB**

{{< highlight csharp >}}

 ' Adds to a bindcolumn

GridWeb1.WorkSheets(0).BindColumns("CategoryID").Validation.ValueList.Add("1,1:test")

' Adds to a validation cell

GridWeb1.WorkSheets(1).Cells("A1").Validation.ValueList.Add("1,1:test")



{{< /highlight >}}

使用 LoadValueList 方法从 dataview 对象加载列表项： 

**C#**

{{< highlight csharp >}}

 GridWeb1.WorkSheets[0].BindColumns["CategoryID"].Validation.LoadValueList(dataSet31.Categories.DefaultView, "CategoryID", "CategoryName", true);



{{< /highlight >}}

**VB**

{{< highlight csharp >}}

 GridWeb1.WorkSheets(0).BindColumns("CategoryID").Validation.LoadValueList(dataSet31.Categories.DefaultView, "CategoryID", "CategoryName", True)



{{< /highlight >}}

{{% /alert %}}
