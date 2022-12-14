---
title: Återbind kalkylblad GridWeb
type: docs
weight: 50
url: /sv/net/rebind-worksheet-gridweb/
---
{{% alert color="primary" %}} 

 När du binder ett kalkylblad till en datauppsättning med

 Kalkylbladsdesigner i IDE, en kalkylbladstagg kommer att skapas i APSX

 fil. Det kan se ut så här:

**XML**

{{< highlight "csharp" >}}

 <acw:Worksheet DataMember="Products" BindStartRow="2" Name="Products" 

EnableCreateBindColumnHeader="True" DataSource='<%# dataSet11 %>'>



{{< /highlight >}}

 När du anropar GridWeb1.DataBind() eller WebWorksheet.DataBind(), kommer kalkylbladet att fyllas med data i dataSet11.

 Ibland kanske du vill binda om kalkylbladet:

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

Kalkylbladet kommer alltid att binda till dataSet11 även om du ändrar egenskapen workheet.DataSource vid körning. Detta beror på att arket alltid använder DataSource-bindningsinformationen i kalkylbladets tagg i ASPX-filen. Om du vill binda arket till en annan datakälla vid körning tar du bort datakällans bindningsinformation i kalkylbladstaggen i ASPC-filen. Redigera taggen till detta:

**XML**

{{< highlight "csharp" >}}

 <acw:Worksheet BindStartRow="2" Name="Products" 

EnableCreateBindColumnHeader="True">



{{< /highlight >}}

Ange egenskaperna för arbetsblad.Datakälla och arbetsblad.DataMember innan du anropar DataBind-metoden.

{{% /alert %}}
