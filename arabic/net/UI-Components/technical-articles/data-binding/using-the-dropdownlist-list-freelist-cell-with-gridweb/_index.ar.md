---
title: استخدام DropDownList و List و FreeList Cell مع GridWeb
type: docs
weight: 60
url: /ar/net/aspose-cells-gridweb/using-the-dropdownlist-list-freelist-gridweb/
keywords: GridWeb,dropdownlist,freelist,list
description: يقدم هذا المقال كيفية استخدام القائمة في GridWeb.
---

{{% alert color="primary" %}} 

مع Aspose.Cells، هناك طرق مختلفة لإنشاء قائمة منسدلة: ValidationType.DropDownList و List و FreeList تقدم هذه الميزة جميعًا. يدعم التحكم زوج قيمة/نص في القوائم المنسدلة والقوائم والقوائم الحرة. استخدم طريقة Validation.ValueList.Add لإضافة زوج قيمة/نص جديد إلى القائمة.

في الكود أدناه، "1" هو قيمة عنصر القائمة، و"1:test" هو النص الذي يتم عرضه لعنصر القائمة. 

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

استخدم طريقة LoadValueList لتحميل عناصر القائمة من كائن dataview: 

**C#**

{{< highlight csharp >}}

 GridWeb1.WorkSheets[0].BindColumns["CategoryID"].Validation.LoadValueList(dataSet31.Categories.DefaultView, "CategoryID", "CategoryName", true);



{{< /highlight >}}

**VB**

{{< highlight csharp >}}

 GridWeb1.WorkSheets(0).BindColumns("CategoryID").Validation.LoadValueList(dataSet31.Categories.DefaultView, "CategoryID", "CategoryName", True)



{{< /highlight >}}

{{% /alert %}}
