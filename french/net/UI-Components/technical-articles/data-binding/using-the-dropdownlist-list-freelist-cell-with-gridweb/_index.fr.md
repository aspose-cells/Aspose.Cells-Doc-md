---
title: Utilisation de DropDownList, List, FreeList Cell avec GridWeb
type: docs
weight: 60
url: /fr/net/using-the-dropdownlist-list-freelist-cell-with-gridweb/
---
{{% alert color="primary" %}} 

Avec Aspose.Cells, il existe différentes manières de créer une liste déroulante : ValidationType.DropDownList, List et FreeList proposent toutes cette fonctionnalité. Le contrôle prend en charge une paire valeur/texte dans les listes déroulantes, les listes et les listes libres. Utilisez la méthode Validation.ValueList.Add pour ajouter une nouvelle paire valeur/texte dans la liste.

 Dans le code ci-dessous, "1" est la valeur de l'élément de liste et "1: test" est le texte affiché de l'élément de liste.

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

Utilisez la méthode LoadValueList pour charger des éléments de liste à partir d'un objet dataview :

**C#**

{{< highlight "csharp" >}}

 GridWeb1.WebWorksheets[0].BindColumns["CategoryID"].Validation.LoadValueList(dataSet31.Categories.DefaultView, "CategoryID", "CategoryName", true);



{{< /highlight >}}

**VB**

{{< highlight "csharp" >}}

 GridWeb1.WebWorksheets(0).BindColumns("CategoryID").Validation.LoadValueList(dataSet31.Categories.DefaultView, "CategoryID", "CategoryName", True)



{{< /highlight >}}

{{% /alert %}}
