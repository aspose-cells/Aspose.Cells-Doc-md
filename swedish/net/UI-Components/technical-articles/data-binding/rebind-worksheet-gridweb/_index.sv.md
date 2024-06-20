---
title: Återbind kalkylblad GridWeb
type: docs
weight: 50
url: /sv/net/aspose-cells-gridweb/rebind-worksheet-gridweb/
keywords: GridWeb,återbinda
description: Den här artikeln introducerar hur man återbinder kalkylbladet i GridWeb.
---

{{% alert color="primary" %}} 

När du binder ett kalkylblad till en dataset med 

Arbetsbladsdesignern i IDE:n skapas en arbetsbladsetikett i APSX 

fil. Det kan se ut så här: 

**XML**

{{< highlight csharp >}}

 <acw:Worksheet DataMember="Products" BindStartRow="2" Name="Products" 

EnableCreateBindColumnHeader="True" DataSource='<%# dataSet11 %>'>



{{< /highlight >}}

När du anropar GridWeb1.DataBind() eller WebWorksheet.DataBind() kommer kalkylarket att fyllas med data i dataSet11. 

Ibland kan du vilja ombinda kalkylarket: 

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

Kalkylarket kommer alltid att binda till dataSet11 även om du ändrar worksheet.DataSource-egenskapen vid körning. Detta beror på att arket alltid använder bindningsinformationen för DataSource i taggen för kalkylarket i ASPX-filen. För att binda arket till en annan datakälla vid körning, ta bort bindningsinformationen för datakällan i arket i ASPC-filen. Redigera taggen till detta: 

**XML**

{{< highlight csharp >}}

 <acw:Worksheet BindStartRow="2" Name="Products" 

EnableCreateBindColumnHeader="True">



{{< /highlight >}}

Ange worksheet.DataSource- och worksheet.DataMember-egenskaperna innan du anropar DataBind-metoden.

{{% /alert %}}
