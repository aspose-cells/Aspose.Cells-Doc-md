---
title: Utilizzando DropDownList, List, FreeList Cell con GridWeb
type: docs
weight: 60
url: /it/net/aspose-cells-gridweb/using-the-dropdownlist-list-freelist-gridweb/
keywords: GridWeb,dropdownlist,freelist,list
description: Questo articolo presenta come utilizzare elenchi in GridWeb.
---

{{% alert color="primary" %}} 

Con Aspose.Cells, ci sono vari modi per creare un elenco a discesa: ValidationType.DropDownList, List e FreeList offrono tutte questa funzionalità. Il controllo supporta una coppia valore/testo negli elenchi a discesa, negli elenchi e nei freedlist. Utilizzare il metodo Validation.ValueList.Add per aggiungere una nuova coppia valore/testo nell'elenco.

Nel codice sottostante, "1" è il valore dell'elemento della lista e "1:test" è il testo visualizzato dell'elemento della lista. 

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

Utilizza il metodo LoadValueList per caricare gli elementi della lista da un oggetto dataview: 

**C#**

{{< highlight csharp >}}

 GridWeb1.WorkSheets[0].BindColumns["CategoryID"].Validation.LoadValueList(dataSet31.Categories.DefaultView, "CategoryID", "CategoryName", true);



{{< /highlight >}}

**VB**

{{< highlight csharp >}}

 GridWeb1.WorkSheets(0).BindColumns("CategoryID").Validation.LoadValueList(dataSet31.Categories.DefaultView, "CategoryID", "CategoryName", True)



{{< /highlight >}}

{{% /alert %}}
