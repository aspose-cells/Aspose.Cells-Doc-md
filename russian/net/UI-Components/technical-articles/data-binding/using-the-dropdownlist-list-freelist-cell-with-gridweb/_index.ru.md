---
title: Используя DropDownList, List, FreeList ячейку с GridWeb
type: docs
weight: 60
url: /ru/net/aspose-cells-gridweb/using-the-dropdownlist-list-freelist-gridweb/
keywords: GridWeb,dropdownlist,freelist,list
description: Эта статья показывает, как использовать список в GridWeb.
---

{{% alert color="primary" %}} 

С помощью Aspose.Cells существует несколько способов создания выпадающего списка: ValidationType.DropDownList, List и FreeList предлагают эту функцию. Управление поддерживает пару значений/текста в выпадающих списках, списках и списке свободных значений. Используйте метод Validation.ValueList.Add для добавления новой пары значение/текст в список.

В приведенном ниже коде "1" - это значение элемента списка, а "1:test" - отображаемый текст элемента списка. 

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

Используйте метод LoadValueList для загрузки элементов списка из объекта DataView: 

**C#**

{{< highlight csharp >}}

 GridWeb1.WorkSheets[0].BindColumns["CategoryID"].Validation.LoadValueList(dataSet31.Categories.DefaultView, "CategoryID", "CategoryName", true);



{{< /highlight >}}

**VB**

{{< highlight csharp >}}

 GridWeb1.WorkSheets(0).BindColumns("CategoryID").Validation.LoadValueList(dataSet31.Categories.DefaultView, "CategoryID", "CategoryName", True)



{{< /highlight >}}

{{% /alert %}}
