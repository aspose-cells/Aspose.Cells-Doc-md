---
title: Usando los controles DropDownList, List, y FreeList con GridWeb
type: docs
weight: 60
url: /es/net/aspose-cells-gridweb/using-the-dropdownlist-list-freelist-gridweb/
keywords: GridWeb,dropdownlist,freelist,list
description: Este artículo muestra cómo utilizar una lista en GridWeb.
---

{{% alert color="primary" %}} 

Con Aspose.Cells, hay varias formas de crear una lista desplegable: ValidationType.DropDownList, List y FreeList ofrecen esta función. El control admite pares valor/texto en las listas desplegables, listas y listas libres. Utiliza el método Validation.ValueList.Add para agregar un nuevo par de valor/texto a la lista.

En el código a continuación, "1" es el valor del elemento de la lista, y "1:test" es el texto mostrado del elemento de la lista. 

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

Utiliza el método LoadValueList para cargar elementos de lista desde un objeto dataview: 

**C#**

{{< highlight csharp >}}

 GridWeb1.WorkSheets[0].BindColumns["CategoryID"].Validation.LoadValueList(dataSet31.Categories.DefaultView, "CategoryID", "CategoryName", true);



{{< /highlight >}}

**VB**

{{< highlight csharp >}}

 GridWeb1.WorkSheets(0).BindColumns("CategoryID").Validation.LoadValueList(dataSet31.Categories.DefaultView, "CategoryID", "CategoryName", True)



{{< /highlight >}}

{{% /alert %}}
