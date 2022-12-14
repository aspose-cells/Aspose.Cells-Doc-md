---
title: Utilizzo di DropDownList, List, FreeList Cell con GridWeb
type: docs
weight: 60
url: /it/net/using-the-dropdownlist-list-freelist-cell-with-gridweb/
---
{{% alert color="primary" %}} 

Con Aspose.Cells, ci sono vari modi per creare un elenco a discesa: ValidationType.DropDownList, List e FreeList offrono tutti questa funzionalità. Il controllo supporta una coppia valore/testo negli elenchi a discesa, negli elenchi e nelle freelist. Utilizzare il metodo Validation.ValueList.Add per aggiungere una nuova coppia valore/testo nell'elenco.

 Nel codice seguente, "1" è il valore dell'elemento dell'elenco e "1:test" è il testo visualizzato dell'elemento dell'elenco.

**C#**

{{< highlight "csharp" >}}

 // Adds to a bindcolumn

GridWeb1.WebWorksheets[0].BindColumns["CategoryID"].Validation.ValueList.Add("1,1:test");

// Adds to a validation cell

GridWeb1.WebWorksheets[1].Cells["A1"].Validation.ValueList.Add("1,1:test");



{{< /highlight >}}

**V.B**

{{< highlight "csharp" >}}

 ' Adds to a bindcolumn

GridWeb1.WebWorksheets(0).BindColumns("CategoryID").Validation.ValueList.Add("1,1:test")

' Adds to a validation cell

GridWeb1.WebWorksheets(1).Cells("A1").Validation.ValueList.Add("1,1:test")



{{< /highlight >}}

Utilizzare il metodo LoadValueList per caricare gli elementi dell'elenco da un oggetto dataview:

**C#**

{{< highlight "csharp" >}}

 GridWeb1.WebWorksheets[0].BindColumns["CategoryID"].Validation.LoadValueList(dataSet31.Categories.DefaultView, "CategoryID", "CategoryName", true);



{{< /highlight >}}

**V.B**

{{< highlight "csharp" >}}

 GridWeb1.WebWorksheets(0).BindColumns("CategoryID").Validation.LoadValueList(dataSet31.Categories.DefaultView, "CategoryID", "CategoryName", True)



{{< /highlight >}}

{{% /alert %}}
