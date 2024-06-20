---
title: Volver a vincular Worksheet GridWeb
type: docs
weight: 50
url: /es/net/aspose-cells-gridweb/rebind-worksheet-gridweb/
keywords: GridWeb, volver a vincular
description: Este artículo explica cómo volver a vincular una hoja de cálculo en GridWeb.
---

{{% alert color="primary" %}} 

Cuando vincula una hoja de cálculo a un conjunto de datos con el 

Diseñador de hojas de cálculo en el entorno de desarrollo integrado (IDE), se creará una etiqueta de hoja de cálculo en el archivo APSX 

. Puede parecerse a esto: 

**XML**

{{< highlight csharp >}}

 <acw:Worksheet DataMember="Products" BindStartRow="2" Name="Products" 

EnableCreateBindColumnHeader="True" DataSource='<%# dataSet11 %>'>



{{< /highlight >}}

Cuando llame a GridWeb1.DataBind() o WebWorksheet.DataBind(), la hoja de cálculo se llenará con los datos en dataSet11. 

A veces puede que desee volver a vincular la hoja de cálculo: 

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

La hoja de cálculo siempre se vinculará a dataSet11 incluso si cambias la propiedad worksheet.DataSource en tiempo de ejecución. Esto se debe a que la hoja siempre utiliza la información de vinculación DataSource en la etiqueta de la hoja en el archivo ASPX. Para vincular la hoja a otra fuente de datos en tiempo de ejecución, elimina la información de vinculación a la fuente de datos en la etiqueta de la hoja en el archivo ASPC. Edita la etiqueta de esta manera: 

**XML**

{{< highlight csharp >}}

 <acw:Worksheet BindStartRow="2" Name="Products" 

EnableCreateBindColumnHeader="True">



{{< /highlight >}}

Especifica las propiedades worksheet.DataSource y worksheet.DataMember antes de llamar al método DataBind.

{{% /alert %}}
