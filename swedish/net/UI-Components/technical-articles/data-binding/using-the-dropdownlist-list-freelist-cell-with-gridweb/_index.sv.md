---
title: Använda DropDownList, List, FreeList Cell med GridWeb
type: docs
weight: 60
url: /sv/net/using-the-dropdownlist-list-freelist-cell-with-gridweb/
---
{{% alert color="primary" %}} 

Med Aspose.Cells finns det olika sätt att skapa en rullgardinslista: ValidationType.DropDownList, List och FreeList erbjuder alla denna funktion. Kontrollen stöder ett värde/text-par i rullgardinslistor, listor och frilistor. Använd metoden Validation.ValueList.Add för att lägga till ett nytt värde/text-par i listan.

 I koden nedan är "1" värdet på listobjektet och "1:test" är listobjektets visade text.

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

Använd metoden LoadValueList för att ladda listobjekt från ett dataview-objekt:

**C#**

{{< highlight "csharp" >}}

 GridWeb1.WebWorksheets[0].BindColumns["CategoryID"].Validation.LoadValueList(dataSet31.Categories.DefaultView, "CategoryID", "CategoryName", true);



{{< /highlight >}}

**VB**

{{< highlight "csharp" >}}

 GridWeb1.WebWorksheets(0).BindColumns("CategoryID").Validation.LoadValueList(dataSet31.Categories.DefaultView, "CategoryID", "CategoryName", True)



{{< /highlight >}}

{{% /alert %}}
