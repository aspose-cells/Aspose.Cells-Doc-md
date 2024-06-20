---
title: Användning av DropDownList, List, FreeList Cell med GridWeb
type: docs
weight: 60
url: /sv/net/aspose-cells-gridweb/using-the-dropdownlist-list-freelist-gridweb/
keywords: GridWeb,dropdownlist,freelist,list
description: Den här artikeln introducerar hur man använder lista i GridWeb.
---

{{% alert color="primary" %}} 

Med Aspose.Cells finns det olika sätt att skapa en nedrullningsbar lista: ValidationType.DropDownList, List och FreeList erbjuder alla denna funktion. Kontrollen stödjer ett värde/textpar i nedrullningslistor, listor och freelistor. Använd metoden Validation.ValueList.Add för att lägga till ett nytt värde/textpar i listan.

I koden nedan är "1" värdet för listposten, och "1:test" är den visade texten för listposten. 

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

Använd LoadValueList-metoden för att ladda listposter från en dataview-objekt: 

**C#**

{{< highlight csharp >}}

 GridWeb1.WorkSheets[0].BindColumns["CategoryID"].Validation.LoadValueList(dataSet31.Categories.DefaultView, "CategoryID", "CategoryName", true);



{{< /highlight >}}

**VB**

{{< highlight csharp >}}

 GridWeb1.WorkSheets(0).BindColumns("CategoryID").Validation.LoadValueList(dataSet31.Categories.DefaultView, "CategoryID", "CategoryName", True)



{{< /highlight >}}

{{% /alert %}}
