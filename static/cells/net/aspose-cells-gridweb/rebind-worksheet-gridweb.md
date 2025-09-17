##Rebind Worksheet GridWeb
This article introduce how to rebind worksheet in GridWeb.
When you bind a worksheet to a dataset with the
Worksheets Designer in the IDE, a worksheet tag will be created in the APSX
file. It may look like this:
**XML**
EnableCreateBindColumnHeader="True" DataSource='<%# dataSet11 %>'>
When you call GridWeb1.DataBind() or WebWorksheet.DataBind(), the worksheet will be filled with the data in dataSet11.
Sometimes you may want to rebind the worksheet:
**C#]**
private void Button1_Click(object sender, System.EventArgs e)
{
GridWeb1.WorkSheets[0].Cells.Clear();
// Load data to the dataSet11.
LoadData(dataSet11);
GridWeb1.WorkSheets[0].DataBind();
}
**VB**
Private Sub Button1_Click(ByVal sender As System.Object, ByVal e As
System.EventArgs) Handles Button1.Click
GridWeb1.WorkSheets(0).Cells.Clear()
' Load data to the dataSet11.
LoadData(dataSet11)
GridWeb1.WorkSheets(0).DataBind()
End Sub
The worksheet will always bind to dataSet11 even if you change the worksheet.DataSource property at runtime. This is because the sheet always uses the DataSource binding information in the worksheet's tag in the ASPX file. To bind the sheet to another datasource at runtime, remove the datasource binding information in the worksheet tag in the ASPC file. Edit the tag to this:
**XML**
EnableCreateBindColumnHeader="True">
Specify the worksheet.DataSource and worksheet.DataMember properties before calling the DataBind method.
