---
title: DataBind yöntemini çağırmadan önce çalışsheet.DataSource ve çalışsheet.DataMember özelliklerini belirtin.
type: docs
weight: 60
url: /tr/net/aspose-cells-gridweb/using-the-dropdownlist-list-freelist-gridweb/
keywords: GridWeb,dropdownlist,freelist,list
description: GridWeb de Dropdown Listesi, Liste, FreeList Hücresini Kullanma
---

{{% alert color="primary" %}} 

Bu makale, GridWeb'de listeyi nasıl kullanacağını tanıtır.

Aspose.Cells ile bir dropdown listesi oluşturmanın çeşitli yolları vardır: ValidationType.DropDownList, List ve FreeList hepsi bu özelliği sunar. Kontrol, dropdown listelerinde, listelerde ve serbest listelerde bir değer/metin çiftini destekler. Yeni bir değer/metin çifti eklemek için Validation.ValueList.Add yöntemini kullanın. 

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

Aşağıdaki kodda, "1", listenin öğesinin değeri ve "1:test", listenin görüntülenen metnidir. 

**C#**

{{< highlight csharp >}}

 GridWeb1.WorkSheets[0].BindColumns["CategoryID"].Validation.LoadValueList(dataSet31.Categories.DefaultView, "CategoryID", "CategoryName", true);



{{< /highlight >}}

**VB**

{{< highlight csharp >}}

 GridWeb1.WorkSheets(0).BindColumns("CategoryID").Validation.LoadValueList(dataSet31.Categories.DefaultView, "CategoryID", "CategoryName", True)



{{< /highlight >}}

{{% /alert %}}
