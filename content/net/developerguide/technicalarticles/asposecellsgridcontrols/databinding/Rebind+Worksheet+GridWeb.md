+++
title = "Rebind Worksheet GridWeb" 
description = "" 
weight = 20351 
+++

Aspose.Cells for .NET : Rebind Worksheet GridWeb  

# Aspose.Cells for .NET : Rebind Worksheet GridWeb


When you bind a worksheet to a dataset with the

Worksheets Designer in the IDE, a worksheet tag will be created in the APSX

file. It may look like this:

**XML**

{{< code lang="xml" >}}
<acw:Worksheet DataMember="Products" BindStartRow="2" Name="Products" 

EnableCreateBindColumnHeader="True" DataSource='<%# dataSet11 %>'>
 
{{< /code >}}

When you call `GridWeb1.DataBind()` or `WebWorksheet.DataBind()`, the worksheet will be filled with the data in dataSet11.

Sometimes you may want to rebind the worksheet:

**C#\]**

{{< code lang="cs" >}}
private void Button1_Click(object sender, System.EventArgs e)
{
    GridWeb1.WebWorksheets[0].Cells.Clear();
    // Load data to the dataSet11.
    LoadData(dataSet11);
    GridWeb1.WebWorksheets[0].DataBind();
}
 
{{< /code >}}

**VB**

Private Sub Button1\_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button1.Click    GridWeb1.WebWorksheets(0).Cells.Clear()    ' Load data to the dataSet11.    LoadData(dataSet11)    GridWeb1.WebWorksheets(0).DataBind()End Sub 

The worksheet will always bind to dataSet11 even if you change the `worksheet.DataSource` property at runtime. This is because the sheet alway uses the `DataSource` binding information in the worksheet's tag in the ASPX file. To bind the sheet to another datasource at runtime, remove the datasource binding information in the worksheet tag in the ASPC file. Edit the tag to this:

**XML**

<acw:Worksheet BindStartRow="2" Name="Products" EnableCreateBindColumnHeader="True"> 

Specify the `worksheet.DataSource` and `worksheet.DataMember` properties before calling the `DataBind` method.

