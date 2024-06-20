---
title: Arbeitsblatt GridWeb neu binden
type: docs
weight: 50
url: /de/net/aspose-cells-gridweb/rebind-worksheet-gridweb/
keywords: GridWeb, neu binden
description: In diesem Artikel erfahren Sie, wie ein Arbeitsblatt in GridWeb neu gebunden wird.
---

{{% alert color="primary" %}} 

Wenn Sie ein Arbeitsblatt mit dem Worksheets Designer in der IDE an ein Dataset binden, wird ein Arbeitsblatt-Tag in der APSX-Datei erstellt. Dies kann folgendermaßen aussehen: 

**XML** 

Datei. Es könnte so aussehen: 

**XML**

{{< highlight csharp >}}

 <acw:Worksheet DataMember="Products" BindStartRow="2" Name="Products" 

EnableCreateBindColumnHeader="True" DataSource='<%# dataSet11 %>'>



{{< /highlight >}}

Wenn Sie GridWeb1.DataBind() oder WebWorksheet.DataBind() aufrufen, wird das Arbeitsblatt mit den Daten in dataSet11 gefüllt. 

Manchmal möchten Sie das Arbeitsblatt neu binden: 

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

Das Arbeitsblatt wird immer an dataSet11 gebunden, auch wenn Sie die Eigenschaft worksheet.DataSource zur Laufzeit ändern. Dies liegt daran, dass das Blatt immer die DataSource-Bindungsinformationen im Tag des Arbeitsblatts in der ASPX-Datei verwendet. Um das Blatt zur Laufzeit an eine andere Datenquelle zu binden, entfernen Sie die Datenquellenbindungsinformationen im Arbeitsblatt-Tag in der ASPC-Datei. Bearbeiten Sie das Tag wie folgt: 

**XML**

{{< highlight csharp >}}

 <acw:Worksheet BindStartRow="2" Name="Products" 

EnableCreateBindColumnHeader="True">



{{< /highlight >}}

Legen Sie vor dem Aufruf der DataBind-Methode die worksheet.DataSource- und worksheet.DataMember-Eigenschaften fest.

{{% /alert %}}
