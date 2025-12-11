---
title: Rebind Worksheet GridWeb
type: docs
weight: 50
url: /net/aspose-cells-gridweb/rebind-worksheet-gridweb/
keywords: GridWeb,rebind
description: This article introduces how to rebind a worksheet in GridWeb.
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}} 

When you bind a worksheet to a dataset with the **Worksheet Designer** in the IDE, a worksheet tag will be created in the **.aspx** file. It may look like this: 

**XML**

{{< highlight csharp >}}
<acw:Worksheet DataMember="Products" BindStartRow="2" Name="Products" 
EnableCreateBindColumnHeader="True" DataSource='<%# dataSet11 %>'>
{{< /highlight >}}

When you call `GridWeb1.DataBind()` or `WebWorksheet.DataBind()`, the worksheet will be filled with the data in `dataSet11`. 

Sometimes you may want to rebind the worksheet: 

**C#**

{{< highlight csharp >}}
private void Button1_Click(object sender, System.EventArgs e)
{
    GridWeb1.WorkSheets[0].Cells.Clear();
    // Load data into dataSet11.
    LoadData(dataSet11);
    GridWeb1.WorkSheets[0].DataBind();
}
{{< /highlight >}}

**VB**

{{< highlight csharp >}}
Private Sub Button1_Click(ByVal sender As System.Object, ByVal e As 
System.EventArgs) Handles Button1.Click
    GridWeb1.WorkSheets(0).Cells.Clear()
    ' Load data into dataSet11.
    LoadData(dataSet11)
    GridWeb1.WorkSheets(0).DataBind()
End Sub
{{< /highlight >}}

The worksheet will always bind to `dataSet11` even if you change the `worksheet.DataSource` property at runtime. This is because the sheet always uses the data‑source binding information in the worksheet's tag in the **.aspx** file. To bind the sheet to another data source at runtime, remove the data‑source binding information in the worksheet tag in the **.aspx** file. Edit the tag to this: 

**XML**

{{< highlight csharp >}}
<acw:Worksheet BindStartRow="2" Name="Products" 
EnableCreateBindColumnHeader="True">
{{< /highlight >}}

Specify the `worksheet.DataSource` and `worksheet.DataMember` properties before calling the `DataBind` method.

{{% /alert %}}
