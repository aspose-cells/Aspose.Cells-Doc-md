---
title: Rebind Worksheet GridWeb
type: docs
weight: 50
url: /net/rebind-worksheet-gridweb/
---

{{% alert color="primary" %}} 

When you bind a worksheet to a dataset with the 

Worksheets Designer in the IDE, a worksheet tag will be created in the APSX 

file. It may look like this: 

**XML**

{{< highlight csharp >}}

 <acw:Worksheet DataMember="Products" BindStartRow="2" Name="Products" 

EnableCreateBindColumnHeader="True" DataSource='<%# dataSet11 %>'>



{{< /highlight >}}

When you call GridWeb1.DataBind() or WebWorksheet.DataBind(), the worksheet will be filled with the data in dataSet11. 

Sometimes you may want to rebind the worksheet: 

**C#]**

{{< highlight csharp >}}

 private void Button1_Click(object sender, System.EventArgs e)

{

    GridWeb1.WebWorksheets[0].Cells.Clear();

    // Load data to the dataSet11.

    LoadData(dataSet11);

    GridWeb1.WebWorksheets[0].DataBind();

}



{{< /highlight >}}

**VB**

{{< highlight csharp >}}

 Private Sub Button1_Click(ByVal sender As System.Object, ByVal e As 

System.EventArgs) Handles Button1.Click

    GridWeb1.WebWorksheets(0).Cells.Clear()

    ' Load data to the dataSet11.

    LoadData(dataSet11)

    GridWeb1.WebWorksheets(0).DataBind()

End Sub



{{< /highlight >}}

The worksheet will always bind to dataSet11 even if you change the worksheet.DataSource property at runtime. This is because the sheet alway uses the DataSource binding information in the worksheet's tag in the ASPX file. To bind the sheet to another datasource at runtime, remove the datasource binding information in the worksheet tag in the ASPC file. Edit the tag to this: 

**XML**

{{< highlight csharp >}}

 <acw:Worksheet BindStartRow="2" Name="Products" 

EnableCreateBindColumnHeader="True">



{{< /highlight >}}

Specify the worksheet.DataSource and worksheet.DataMember properties before calling the DataBind method.

{{% /alert %}}
