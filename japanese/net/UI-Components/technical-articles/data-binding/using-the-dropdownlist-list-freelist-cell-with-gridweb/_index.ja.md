---
title: GridWebでのDropDownList、List、FreeList Cellの使用
type: docs
weight: 60
url: /ja/net/aspose-cells-gridweb/using-the-dropdownlist-list-freelist-gridweb/
keywords: GridWeb,dropdownlist,freelist,list
description: この記事では、GridWebでリストを使用する方法について紹介します。
---

{{% alert color="primary" %}} 

Aspose.Cellsを使用すると、ValidationType.DropDownList、List、FreeListを使用してドロップダウンリストを作成するさまざまな方法があります。このコントロールは、ドロップダウンリスト、リスト、フリーリストで値/テキストのペアをサポートします。新しい値/テキストのペアをリストに追加するには、Validation.ValueList.Addメソッドを使用します。

以下のコードでは、「1」はリスト項目の値で、「1:test」はリスト項目の表示テキストです。 

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

LoadValueListメソッドを使用して、データビューオブジェクトからリスト項目をロードします: 

**C#**

{{< highlight csharp >}}

 GridWeb1.WorkSheets[0].BindColumns["CategoryID"].Validation.LoadValueList(dataSet31.Categories.DefaultView, "CategoryID", "CategoryName", true);



{{< /highlight >}}

**VB**

{{< highlight csharp >}}

 GridWeb1.WorkSheets(0).BindColumns("CategoryID").Validation.LoadValueList(dataSet31.Categories.DefaultView, "CategoryID", "CategoryName", True)



{{< /highlight >}}

{{% /alert %}}
