---
title: Rebinder Worksheet GridWeb
type: docs
weight: 50
url: /fr/net/aspose-cells-gridweb/rebind-worksheet-gridweb/
keywords: GridWeb,rebinder
description: Cet article présente comment relier une feuille de calcul dans GridWeb.
---

{{% alert color="primary" %}} 

Lorsque vous liez une feuille de calcul à un jeu de données avec le 

Concepteur de feuilles de calcul dans l'IDE, une balise de feuille de calcul sera créée dans le fichier APSX 

. Il peut ressembler à ceci : 

**XML**

{{< highlight csharp >}}

 <acw:Worksheet DataMember="Products" BindStartRow="2" Name="Products" 

EnableCreateBindColumnHeader="True" DataSource='<%# dataSet11 %>'>



{{< /highlight >}}

Lorsque vous appelez GridWeb1.DataBind() ou WebWorksheet.DataBind(), la feuille de calcul sera remplie avec les données de dataSet11. 

Parfois, vous voudrez peut-être relier la feuille de calcul : 

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

La feuille de calcul se lie toujours à dataSet11 même si vous modifiez la propriété worksheet.DataSource à l'exécution. Cela est dû au fait que la feuille utilise toujours les informations de liaison DataSource dans la balise de la feuille de calcul dans le fichier ASPX. Pour lier la feuille à une autre source de données à l'exécution, supprimez les informations de liaison de la source de données dans la balise de la feuille de calcul dans le fichier ASPC. Modifiez la balise en ceci : 

**XML**

{{< highlight csharp >}}

 <acw:Worksheet BindStartRow="2" Name="Products" 

EnableCreateBindColumnHeader="True">



{{< /highlight >}}

Spécifiez les propriétés worksheet.DataSource et worksheet.DataMember avant d'appeler la méthode DataBind.

{{% /alert %}}
