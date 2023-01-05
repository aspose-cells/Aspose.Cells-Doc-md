---
title: Использование DropDownList, List, FreeList Cell с GridWeb
type: docs
weight: 60
url: /ru/net/using-the-dropdownlist-list-freelist-cell-with-gridweb/
---
{{% alert color="primary" %}} 

С Aspose.Cells существуют различные способы создания раскрывающегося списка: ValidationType.DropDownList, List и FreeList предлагают эту функцию. Элемент управления поддерживает пару значение/текст в раскрывающихся списках, списках и свободных списках. Используйте метод Validation.ValueList.Add, чтобы добавить в список новую пару значение/текст.

 В приведенном ниже коде «1» — это значение элемента списка, а «1:test» — отображаемый текст элемента списка.

**C#**

{{< highlight "csharp" >}}

 // Adds to a bindcolumn

GridWeb1.WebWorksheets[0].BindColumns["CategoryID"].Validation.ValueList.Add("1,1:test");

// Adds to a validation cell

GridWeb1.WebWorksheets[1].Cells["A1"].Validation.ValueList.Add("1,1:test");



{{< /highlight >}}

**ВБ**

{{< highlight "csharp" >}}

 ' Adds to a bindcolumn

GridWeb1.WebWorksheets(0).BindColumns("CategoryID").Validation.ValueList.Add("1,1:test")

' Adds to a validation cell

GridWeb1.WebWorksheets(1).Cells("A1").Validation.ValueList.Add("1,1:test")



{{< /highlight >}}

Используйте метод LoadValueList для загрузки элементов списка из объекта представления данных:

**C#**

{{< highlight "csharp" >}}

 GridWeb1.WebWorksheets[0].BindColumns["CategoryID"].Validation.LoadValueList(dataSet31.Categories.DefaultView, "CategoryID", "CategoryName", true);



{{< /highlight >}}

**ВБ**

{{< highlight "csharp" >}}

 GridWeb1.WebWorksheets(0).BindColumns("CategoryID").Validation.LoadValueList(dataSet31.Categories.DefaultView, "CategoryID", "CategoryName", True)



{{< /highlight >}}

{{% /alert %}}
