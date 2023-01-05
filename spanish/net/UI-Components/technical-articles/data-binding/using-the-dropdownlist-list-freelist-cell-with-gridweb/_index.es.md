---
title: Uso de DropDownList, List, FreeList Cell con GridWeb
type: docs
weight: 60
url: /es/net/using-the-dropdownlist-list-freelist-cell-with-gridweb/
---
{{% alert color="primary" %}} 

Con Aspose.Cells, hay varias formas de crear una lista desplegable: ValidationType.DropDownList, List y FreeList ofrecen esta función. El control admite un par de valor/texto en listas desplegables, listas y listas libres. Utilice el método Validation.ValueList.Add para agregar un nuevo par de valor/texto a la lista.

 En el siguiente código, "1" es el valor del elemento de la lista y "1:prueba" es el texto que se muestra en el elemento de la lista.

**C#**

{{< highlight "csharp" >}}

 // Adds to a bindcolumn

GridWeb1.WebWorksheets[0].BindColumns["CategoryID"].Validation.ValueList.Add("1,1:test");

// Adds to a validation cell

GridWeb1.WebWorksheets[1].Cells["A1"].Validation.ValueList.Add("1,1:test");



{{< /highlight >}}

**VB**

{{< highlight "csharp" >}}

 ' Adds to a bindcolumn

GridWeb1.WebWorksheets(0).BindColumns("CategoryID").Validation.ValueList.Add("1,1:test")

' Adds to a validation cell

GridWeb1.WebWorksheets(1).Cells("A1").Validation.ValueList.Add("1,1:test")



{{< /highlight >}}

Use el método LoadValueList para cargar elementos de lista desde un objeto de vista de datos:

**C#**

{{< highlight "csharp" >}}

 GridWeb1.WebWorksheets[0].BindColumns["CategoryID"].Validation.LoadValueList(dataSet31.Categories.DefaultView, "CategoryID", "CategoryName", true);



{{< /highlight >}}

**VB**

{{< highlight "csharp" >}}

 GridWeb1.WebWorksheets(0).BindColumns("CategoryID").Validation.LoadValueList(dataSet31.Categories.DefaultView, "CategoryID", "CategoryName", True)



{{< /highlight >}}

{{% /alert %}}
