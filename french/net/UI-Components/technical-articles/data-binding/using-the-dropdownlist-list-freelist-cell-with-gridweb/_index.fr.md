---
title: Utilisation de la cellule DropDownList, List, FreeList avec GridWeb
type: docs
weight: 60
url: /fr/net/aspose-cells-gridweb/using-the-dropdownlist-list-freelist-gridweb/
keywords: GridWeb,dropdownlist,freelist,list
description: Cet article présente comment utiliser la liste dans GridWeb.
---

{{% alert color="primary" %}} 

Avec Aspose.Cells, il existe différentes façons de créer une liste déroulante : ValidationType.DropDownList, List et FreeList offrent toutes cette fonctionnalité. Le contrôle prend en charge une paire valeur/texte dans les listes déroulantes, les listes et les freelists. Utilisez la méthode Validation.ValueList.Add pour ajouter une nouvelle paire valeur/texte dans la liste.

Dans le code ci-dessous, "1" est la valeur de l'élément de la liste, et "1:test" est le texte affiché de l'élément de la liste. 

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

Utilisez la méthode LoadValueList pour charger des éléments de liste à partir d'un objet dataview : 

**C#**

{{< highlight csharp >}}

 GridWeb1.WorkSheets[0].BindColumns["CategoryID"].Validation.LoadValueList(dataSet31.Categories.DefaultView, "CategoryID", "CategoryName", true);



{{< /highlight >}}

**VB**

{{< highlight csharp >}}

 GridWeb1.WorkSheets(0).BindColumns("CategoryID").Validation.LoadValueList(dataSet31.Categories.DefaultView, "CategoryID", "CategoryName", True)



{{< /highlight >}}

{{% /alert %}}
