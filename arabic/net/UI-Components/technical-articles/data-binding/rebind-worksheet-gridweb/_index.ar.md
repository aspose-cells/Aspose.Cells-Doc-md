---
title: Rebind ورقة عمل GridWeb
type: docs
weight: 50
url: /ar/net/rebind-worksheet-gridweb/
---
{{% alert color="primary" %}} 

 عند ربط ورقة عمل بمجموعة بيانات بامتداد

 مصمم أوراق العمل في IDE ، سيتم إنشاء علامة ورقة العمل في APSX

 ملف. قد يبدو كالتالي:

**XML**

{{< highlight "csharp" >}}

 <acw:Worksheet DataMember="Products" BindStartRow="2" Name="Products" 

EnableCreateBindColumnHeader="True" DataSource='<%# dataSet11 %>'>



{{< /highlight >}}

 عند استدعاء GridWeb1.DataBind () أو WebWorksheet.DataBind () ، سيتم ملء ورقة العمل بالبيانات الموجودة في dataSet11.

 قد ترغب أحيانًا في إعادة إنشاء ورقة العمل:

**C#]**

{{< highlight "csharp" >}}

 private void Button1_Click(object sender, System.EventArgs e)

{

    GridWeb1.WebWorksheets[0].Cells.Clear();

    // Load data to the dataSet11.

    LoadData(dataSet11);

    GridWeb1.WebWorksheets[0].DataBind();

}



{{< /highlight >}}

**VB**

{{< highlight "csharp" >}}

 Private Sub Button1_Click(ByVal sender As System.Object, ByVal e As 

System.EventArgs) Handles Button1.Click

    GridWeb1.WebWorksheets(0).Cells.Clear()

    ' Load data to the dataSet11.

    LoadData(dataSet11)

    GridWeb1.WebWorksheets(0).DataBind()

End Sub



{{< /highlight >}}

ستلتزم ورقة العمل دائمًا بـ dataSet11 حتى إذا قمت بتغيير الخاصية workheet.DataSource في وقت التشغيل. هذا لأن الورقة تستخدم دائمًا معلومات ربط DataSource في علامة ورقة العمل في ملف ASPX. لربط الورقة بمصدر بيانات آخر في وقت التشغيل ، قم بإزالة معلومات ربط مصدر البيانات في علامة ورقة العمل في ملف ASPC. قم بتحرير العلامة إلى هذا:

**XML**

{{< highlight "csharp" >}}

 <acw:Worksheet BindStartRow="2" Name="Products" 

EnableCreateBindColumnHeader="True">



{{< /highlight >}}

حدد خصائص Worksheet.DataSource و workheet.DataMember قبل استدعاء أسلوب DataBind.

{{% /alert %}}
