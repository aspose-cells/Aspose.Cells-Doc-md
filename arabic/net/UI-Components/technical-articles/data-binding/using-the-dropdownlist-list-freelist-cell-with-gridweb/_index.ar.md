---
title: استخدام القائمة المنسدلة ، القائمة ، القائمة الحرة Cell مع GridWeb
type: docs
weight: 60
url: /ar/net/using-the-dropdownlist-list-freelist-cell-with-gridweb/
---
{{% alert color="primary" %}} 

مع Aspose.Cells ، توجد طرق مختلفة لإنشاء قائمة منسدلة: ValidationType.DropDownList و List و FreeList تقدم جميعها هذه الميزة. يدعم عنصر التحكم زوج القيمة / النص في القوائم المنسدلة والقوائم والقوائم الحرة. استخدم طريقة Validation.ValueList.Add لإضافة زوج قيمة / نص جديد إلى القائمة.

 في الكود أدناه ، "1" هي قيمة عنصر القائمة ، و "1: اختبار" هو النص المعروض لعنصر القائمة.

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

استخدم الأسلوب LoadValueList لتحميل عناصر القائمة من كائن عرض البيانات:

**C#**

{{< highlight "csharp" >}}

 GridWeb1.WebWorksheets[0].BindColumns["CategoryID"].Validation.LoadValueList(dataSet31.Categories.DefaultView, "CategoryID", "CategoryName", true);



{{< /highlight >}}

**VB**

{{< highlight "csharp" >}}

 GridWeb1.WebWorksheets(0).BindColumns("CategoryID").Validation.LoadValueList(dataSet31.Categories.DefaultView, "CategoryID", "CategoryName", True)



{{< /highlight >}}

{{% /alert %}}
