---
title: Verwendung der Dropdown Liste, Liste, FreeList Zelle mit GridWeb
type: docs
weight: 60
url: /de/net/aspose-cells-gridweb/using-the-dropdownlist-list-freelist-gridweb/
keywords: GridWeb,dropdownlist,freelist,list
description: Dieser Artikel zeigt, wie Listen in GridWeb verwendet werden.
---

{{% alert color="primary" %}} 

Mit Aspose.Cells gibt es verschiedene Möglichkeiten, eine Dropdown-Liste zu erstellen: ValidationType. DropDownList, List und FreeList bieten alle diese Funktion. Die Steuerung unterstützt ein Wert/Text-Paar in Dropdown-Listen, Listen und Freilisten. Verwenden Sie die Validation.ValueList.Add-Methode, um ein neues Wert/Text-Paar in die Liste aufzunehmen.

Im folgenden Code ist "1" der Wert des Listenelements und "1:test" ist der angezeigte Text des Listenelements. 

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

Verwenden Sie die LoadValueList-Methode, um Listenelemente aus einem DataView-Objekt zu laden: 

**C#**

{{< highlight csharp >}}

 GridWeb1.WorkSheets[0].BindColumns["CategoryID"].Validation.LoadValueList(dataSet31.Categories.DefaultView, "CategoryID", "CategoryName", true);



{{< /highlight >}}

**VB**

{{< highlight csharp >}}

 GridWeb1.WorkSheets(0).BindColumns("CategoryID").Validation.LoadValueList(dataSet31.Categories.DefaultView, "CategoryID", "CategoryName", True)



{{< /highlight >}}

{{% /alert %}}
