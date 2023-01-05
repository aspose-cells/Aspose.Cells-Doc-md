---
title: Rebind foglio di lavoro GridWeb
type: docs
weight: 50
url: /it/net/rebind-worksheet-gridweb/
---
{{% alert color="primary" %}} 

 Quando si associa un foglio di lavoro a un set di dati con l'estensione

 Worksheets Designer nell'IDE, verrà creato un tag del foglio di lavoro in APSX

 file. Potrebbe assomigliare a questo:

**XML**

{{< highlight "csharp" >}}

 <acw:Worksheet DataMember="Products" BindStartRow="2" Name="Products" 

EnableCreateBindColumnHeader="True" DataSource='<%# dataSet11 %>'>



{{< /highlight >}}

 Quando si chiama GridWeb1.DataBind() o WebWorksheet.DataBind(), il foglio di lavoro verrà riempito con i dati in dataSet11.

 A volte potresti voler ricollegare il foglio di lavoro:

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

**V.B**

{{< highlight "csharp" >}}

 Private Sub Button1_Click(ByVal sender As System.Object, ByVal e As 

System.EventArgs) Handles Button1.Click

    GridWeb1.WebWorksheets(0).Cells.Clear()

    ' Load data to the dataSet11.

    LoadData(dataSet11)

    GridWeb1.WebWorksheets(0).DataBind()

End Sub



{{< /highlight >}}

Il foglio di lavoro verrà sempre associato a dataSet11 anche se si modifica la proprietà worksheet.DataSource in fase di esecuzione. Ciò è dovuto al fatto che il foglio utilizza sempre le informazioni sull'associazione DataSource nel tag del foglio di lavoro nel file ASPX. Per associare il foglio a un'altra origine dati in fase di esecuzione, rimuovi le informazioni sull'associazione dell'origine dati nel tag del foglio di lavoro nel file ASPC. Modifica il tag in questo modo:

**XML**

{{< highlight "csharp" >}}

 <acw:Worksheet BindStartRow="2" Name="Products" 

EnableCreateBindColumnHeader="True">



{{< /highlight >}}

Specificare le proprietà worksheet.DataSource e worksheet.DataMember prima di chiamare il metodo DataBind.

{{% /alert %}}
