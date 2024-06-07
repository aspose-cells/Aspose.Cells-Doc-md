---
title: 使用DropDownList、List、FreeList Cell与GridWeb
type: docs
weight: 60
url: /zh/net/aspose-cells-gridweb/using-the-dropdownlist-list-freelist-gridweb/
keywords: GridWeb支持使用GridWeb.CustomCalculationEngine属性计算自定义函数。该属性接受GridAbstractCalculationEngine接口的实例。请实现GridAbstractCalculationEngine接口，并使用自己的逻辑计算自定义函数。
description: 本文介绍了如何在GridWeb中使用列表。
---

{{% alert color="primary" %}} 

使用Aspose.Cells，有多种方法可以创建下拉列表：ValidationType.DropDownList、List和FreeList都提供了这个功能。该控件支持下拉列表、列表和自由列表中的值/文本对。使用Validation.ValueList.Add方法将新的值/文本对添加到列表中。

在下面的代码中，“1”是列表项的值，“1:test”是显示的文本。 

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

使用LoadValueList方法从dataview对象加载列表项： 

**C#**

{{< highlight csharp >}}

 GridWeb1.WorkSheets[0].BindColumns["CategoryID"].Validation.LoadValueList(dataSet31.Categories.DefaultView, "CategoryID", "CategoryName", true);



{{< /highlight >}}

**VB**

{{< highlight csharp >}}

 GridWeb1.WorkSheets(0).BindColumns("CategoryID").Validation.LoadValueList(dataSet31.Categories.DefaultView, "CategoryID", "CategoryName", True)



{{< /highlight >}}

{{% /alert %}}
