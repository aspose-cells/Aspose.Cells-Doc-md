---
title: DropDownList, List, FreeList Cell'i GridWeb ile Kullanma
type: docs
weight: 60
url: /tr/net/using-the-dropdownlist-list-freelist-cell-with-gridweb/
---
{{% alert color="primary" %}} 

Aspose.Cells ile açılır liste oluşturmanın çeşitli yolları vardır: ValidationType.DropDownList, List ve FreeList'in tümü bu özelliği sunar. Kumanda, açılır listelerde, listelerde ve serbest listelerde bir değer/metin çiftini destekler. Listeye yeni bir değer/metin çifti eklemek için Validation.ValueList.Add yöntemini kullanın.

 Aşağıdaki kodda, "1", liste öğesinin değeridir ve "1:test", liste öğesinin görüntülenen metnidir.

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

Liste öğelerini bir veri görünümü nesnesinden yüklemek için LoadValueList yöntemini kullanın:

**C#**

{{< highlight "csharp" >}}

 GridWeb1.WebWorksheets[0].BindColumns["CategoryID"].Validation.LoadValueList(dataSet31.Categories.DefaultView, "CategoryID", "CategoryName", true);



{{< /highlight >}}

**VB**

{{< highlight "csharp" >}}

 GridWeb1.WebWorksheets(0).BindColumns("CategoryID").Validation.LoadValueList(dataSet31.Categories.DefaultView, "CategoryID", "CategoryName", True)



{{< /highlight >}}

{{% /alert %}}
