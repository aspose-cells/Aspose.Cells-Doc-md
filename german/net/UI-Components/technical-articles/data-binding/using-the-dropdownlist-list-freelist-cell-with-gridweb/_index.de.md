---
title: Verwendung von DropDownList, List, FreeList Cell mit GridWeb
type: docs
weight: 60
url: /de/net/using-the-dropdownlist-list-freelist-cell-with-gridweb/
---
{{% alert color="primary" %}} 

Mit Aspose.Cells gibt es verschiedene Möglichkeiten, eine Dropdown-Liste zu erstellen: ValidationType.DropDownList, List und FreeList bieten alle diese Funktion. Das Steuerelement unterstützt ein Wert/Text-Paar in Dropdown-Listen, Listen und freien Listen. Verwenden Sie die Validation.ValueList.Add-Methode, um der Liste ein neues Wert/Text-Paar hinzuzufügen.

 Im folgenden Code ist „1“ der Wert des Listenelements und „1:test“ der angezeigte Text des Listenelements.

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

Verwenden Sie die LoadValueList-Methode, um Listenelemente aus einem DataView-Objekt zu laden:

**C#**

{{< highlight "csharp" >}}

 GridWeb1.WebWorksheets[0].BindColumns["CategoryID"].Validation.LoadValueList(dataSet31.Categories.DefaultView, "CategoryID", "CategoryName", true);



{{< /highlight >}}

**VB**

{{< highlight "csharp" >}}

 GridWeb1.WebWorksheets(0).BindColumns("CategoryID").Validation.LoadValueList(dataSet31.Categories.DefaultView, "CategoryID", "CategoryName", True)



{{< /highlight >}}

{{% /alert %}}
