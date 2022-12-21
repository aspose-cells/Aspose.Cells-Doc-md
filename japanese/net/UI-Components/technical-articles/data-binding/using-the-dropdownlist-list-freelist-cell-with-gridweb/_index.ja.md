---
title: DropDownList、List、FreeList Cell を GridWeb で使用する
type: docs
weight: 60
url: /ja/net/using-the-dropdownlist-list-freelist-cell-with-gridweb/
---
{{% alert color="primary" %}} 

Aspose.Cells では、ドロップダウン リストを作成するさまざまな方法があります。ValidationType.DropDownList、List、および FreeList はすべてこの機能を提供します。コントロールは、ドロップダウン リスト、リスト、およびフリーリストで値/テキストのペアをサポートします。 Validation.ValueList.Add メソッドを使用して、新しい値とテキストのペアをリストに追加します。

以下のコードでは、「1」がリスト項目の値で、「1:test」がリスト項目の表示テキストです。

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

LoadValueList メソッドを使用して、データビュー オブジェクトからリスト項目をロードします。

**C#**

{{< highlight "csharp" >}}

 GridWeb1.WebWorksheets[0].BindColumns["CategoryID"].Validation.LoadValueList(dataSet31.Categories.DefaultView, "CategoryID", "CategoryName", true);



{{< /highlight >}}

**VB**

{{< highlight "csharp" >}}

 GridWeb1.WebWorksheets(0).BindColumns("CategoryID").Validation.LoadValueList(dataSet31.Categories.DefaultView, "CategoryID", "CategoryName", True)



{{< /highlight >}}

{{% /alert %}}
