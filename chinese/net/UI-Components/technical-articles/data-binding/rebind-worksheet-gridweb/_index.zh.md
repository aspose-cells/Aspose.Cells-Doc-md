---
title: 重新绑定工作表 GridWeb
type: docs
weight: 50
url: /zh/net/rebind-worksheet-gridweb/
---
{{% alert color="primary" %}} 

当您将工作表绑定到数据集时

IDE 中的工作表设计器，将在 APSX 中创建一个工作表标签

文件。它可能看起来像这样：

**XML**

{{< highlight "csharp" >}}

 <acw:Worksheet DataMember="Products" BindStartRow="2" Name="Products" 

EnableCreateBindColumnHeader="True" DataSource='<%# dataSet11 %>'>



{{< /highlight >}}

当您调用 GridWeb1.DataBind() 或 WebWorksheet.DataBind() 时，工作表将填充 dataSet11 中的数据。

有时您可能想重新绑定工作表：

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

**虚拟机**

{{< highlight "csharp" >}}

 Private Sub Button1_Click(ByVal sender As System.Object, ByVal e As 

System.EventArgs) Handles Button1.Click

    GridWeb1.WebWorksheets(0).Cells.Clear()

    ' Load data to the dataSet11.

    LoadData(dataSet11)

    GridWeb1.WebWorksheets(0).DataBind()

End Sub



{{< /highlight >}}

即使您在运行时更改了 worksheet.DataSource 属性，工作表也将始终绑定到 dataSet11。这是因为工作表始终使用 ASPX 文件中工作表标记中的 DataSource 绑定信息。要在运行时将工作表绑定到另一个数据源，请删除 ASPC 文件中工作表标记中的数据源绑定信息。将标签编辑为：

**XML**

{{< highlight "csharp" >}}

 <acw:Worksheet BindStartRow="2" Name="Products" 

EnableCreateBindColumnHeader="True">



{{< /highlight >}}

在调用 DataBind 方法之前指定 worksheet.DataSource 和 worksheet.DataMember 属性。

{{% /alert %}}
