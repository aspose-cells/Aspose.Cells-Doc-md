---
title: Reenlazar hoja de trabajo GridWeb
type: docs
weight: 50
url: /es/net/rebind-worksheet-gridweb/
---
{{% alert color="primary" %}} 

 Cuando vincula una hoja de trabajo a un conjunto de datos con el

 Worksheets Designer en el IDE, se creará una etiqueta de hoja de trabajo en el APSX

 expediente. Puede verse así:

**XML**

{{< highlight "csharp" >}}

 <acw:Worksheet DataMember="Products" BindStartRow="2" Name="Products" 

EnableCreateBindColumnHeader="True" DataSource='<%# dataSet11 %>'>



{{< /highlight >}}

 Cuando llame a GridWeb1.DataBind() o WebWorksheet.DataBind(), la hoja de trabajo se completará con los datos en dataSet11.

 A veces es posible que desee volver a encuadernar la hoja de trabajo:

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

La hoja de trabajo siempre se vinculará a dataSet11 incluso si cambia la propiedad worksheet.DataSource en tiempo de ejecución. Esto se debe a que la hoja siempre usa la información de enlace de DataSource en la etiqueta de la hoja de trabajo en el archivo ASPX. Para vincular la hoja a otra fuente de datos en tiempo de ejecución, elimine la información de vinculación de la fuente de datos en la etiqueta de la hoja de trabajo en el archivo ASPC. Edite la etiqueta a esto:

**XML**

{{< highlight "csharp" >}}

 <acw:Worksheet BindStartRow="2" Name="Products" 

EnableCreateBindColumnHeader="True">



{{< /highlight >}}

Especifique las propiedades worksheet.DataSource y worksheet.DataMember antes de llamar al método DataBind.

{{% /alert %}}
