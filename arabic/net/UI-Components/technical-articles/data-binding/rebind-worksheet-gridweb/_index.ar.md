---
title: إعادة ربط GridWeb Worksheet
type: docs
weight: 50
url: /ar/net/aspose-cells-gridweb/rebind-worksheet-gridweb/
keywords: GridWeb، إعادة الربط
description: يقدم هذا المقال كيفية إعادة ربط ورقة البيانات في GridWeb.
---

{{% alert color="primary" %}} 

عندما تقوم بربط ورقة البيانات بمجموعة البيانات باستخدام 

مصممي الأوراق في البيئة المتكاملة، سيتم إنشاء علامة لورقة البيانات في ملف ASPX 

 قد تبدو مثل هذا: 

**XML**

{{< highlight csharp >}}

 <acw:Worksheet DataMember="Products" BindStartRow="2" Name="Products" 

EnableCreateBindColumnHeader="True" DataSource='<%# dataSet11 %>'>



{{< /highlight >}}

عند استدعاء GridWeb1.DataBind() أو WebWorksheet.DataBind()، ستتم ملء ورقة البيانات بالبيانات في dataSet11. 

في بعض الأحيان قد ترغب في إعادة ربط ورقة البيانات: 

**C#]**

{{< highlight csharp >}}

 private void Button1_Click(object sender, System.EventArgs e)

{

    GridWeb1.WorkSheets[0].Cells.Clear();

    // Load data to the dataSet11.

    LoadData(dataSet11);

    GridWeb1.WorkSheets[0].DataBind();

}



{{< /highlight >}}

**VB**

{{< highlight csharp >}}

 Private Sub Button1_Click(ByVal sender As System.Object, ByVal e As 

System.EventArgs) Handles Button1.Click

    GridWeb1.WorkSheets(0).Cells.Clear()

    ' Load data to the dataSet11.

    LoadData(dataSet11)

    GridWeb1.WorkSheets(0).DataBind()

End Sub



{{< /highlight >}}

سوف ترتبط ورقة البيانات دائمًا بـ dataSet11 حتى إذا قمت بتغيير خاصية worksheet.DataSource في وقت التشغيل. يحدث هذا لأن الورقة تستخدم دائمًا معلومات ربط مصدر البيانات في العلامة الموجودة في ملف ASPX. لربط الورقة بمصدر بيانات آخر في وقت التشغيل، أزل معلومات ربط مصدر البيانات في العلامة الموجودة في ملف ASPC. حرر العلامة إلى هذا الشكل: 

**XML**

{{< highlight csharp >}}

 <acw:Worksheet BindStartRow="2" Name="Products" 

EnableCreateBindColumnHeader="True">



{{< /highlight >}}

حدد خصائص worksheet.DataSource و worksheet.DataMember قبل استدعاء طريقة DataBind.

{{% /alert %}}
