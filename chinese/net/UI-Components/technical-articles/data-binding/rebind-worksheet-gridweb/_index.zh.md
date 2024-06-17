---
title: 重新绑定工作表 GridWeb
type: docs
weight: 50
url: /zh/net/aspose-cells-gridweb/rebind-worksheet-gridweb/
keywords: GridWeb，重新绑定
description: 本文介绍如何在 GridWeb 中重新绑定工作表。
---

{{% alert color="primary" %}} 

当您使用 IDE 中的 Worksheets Designer 将工作表绑定到数据集时，将在 APSX 中创建一个工作表标记。 

文件。它可能看起来像这样： 

**XML** 

**XML**

{{< highlight csharp >}}

 <acw:Worksheet DataMember="Products" BindStartRow="2" Name="Products" 

EnableCreateBindColumnHeader="True" DataSource='<%# dataSet11 %>'>



{{< /highlight >}}

当你调用 GridWeb1.DataBind() 或 WebWorksheet.DataBind() 时，工作表将被数据集 dataSet11 填充。 

有时您可能想重新绑定工作表： 

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

即使在运行时更改工作表.DataSource 属性，工作表始终会绑定到 dataSet11，这是因为工作表始终使用 ASPX 文件中工作表标记中的 DataSource 绑定信息。要在运行时将工作表绑定到另一个数据源，请移除 ASPC 文件中工作表标记中的数据源绑定信息。将标记编辑为如下内容： 

**XML**

{{< highlight csharp >}}

 <acw:Worksheet BindStartRow="2" Name="Products" 

EnableCreateBindColumnHeader="True">



{{< /highlight >}}

在调用 DataBind 方法之前，指定工作表的 DataSource 和 DataMember 属性。

{{% /alert %}}
