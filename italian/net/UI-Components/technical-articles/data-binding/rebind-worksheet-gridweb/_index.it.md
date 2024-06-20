---
title: Rilega Worksheet GridWeb
type: docs
weight: 50
url: /it/net/aspose-cells-gridweb/rebind-worksheet-gridweb/
keywords: GridWeb, rilegare
description: Questo articolo presenta come rilegare il foglio di lavoro in GridWeb.
---

{{% alert color="primary" %}} 

Quando si lega un foglio di lavoro a un set di dati con il 

Fogli di lavoro Designer nell'IDE, verrà creato un tag del foglio di lavoro nel file APSX 

documento. Potrebbe assomigliare a questo: 

**XML**

{{< highlight csharp >}}

 <acw:Worksheet DataMember="Products" BindStartRow="2" Name="Products" 

EnableCreateBindColumnHeader="True" DataSource='<%# dataSet11 %>'>



{{< /highlight >}}

Quando si chiama GridWeb1.DataBind() o WebWorksheet.DataBind(), il foglio di lavoro verrà riempito con i dati in dataSet11. 

A volte potresti voler rilegare il foglio di lavoro: 

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

Il foglio di lavoro sarà sempre legato a dataSet11 anche se si modifica la proprietà worksheet.DataSource a runtime. Questo perché il foglio utilizza sempre le informazioni di collegamento del DataSource nel tag del foglio di lavoro nel file ASPX. Per legare il foglio a un'altra origine dati a runtime, rimuovere le informazioni di collegamento dell'origine dati nel tag del foglio di lavoro nel file ASPX. Modifica il tag in questo modo: 

**XML**

{{< highlight csharp >}}

 <acw:Worksheet BindStartRow="2" Name="Products" 

EnableCreateBindColumnHeader="True">



{{< /highlight >}}

Specificare le proprietà worksheet.DataSource e worksheet.DataMember prima di chiamare il metodo DataBind.

{{% /alert %}}
