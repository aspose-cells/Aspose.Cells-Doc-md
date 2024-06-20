---
title: Перезагрузите Рабочий лист GridWeb
type: docs
weight: 50
url: /ru/net/aspose-cells-gridweb/rebind-worksheet-gridweb/
keywords: GridWeb,перезагрузка
description: В этой статье рассматривается, как перезагружать рабочий лист в GridWeb.
---

{{% alert color="primary" %}} 

Когда вы связываете рабочий лист с набором данных в IDE, будет создан тег таблицы в файле APSX, который может выглядеть так: 

Worksheets Designer в IDE: тег рабочего листа в APSX 

файле. Это может выглядеть так: 

**XML**

{{< highlight csharp >}}

 <acw:Worksheet DataMember="Products" BindStartRow="2" Name="Products" 

EnableCreateBindColumnHeader="True" DataSource='<%# dataSet11 %>'>



{{< /highlight >}}

Когда вы вызываете GridWeb1.DataBind() или WebWorksheet.DataBind(), рабочий лист будет заполнен данными в dataSet11. 

Иногда вам может понадобиться перезагрузить рабочий лист: 

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

Рабочий лист всегда будет связан с dataSet11, даже если вы измените свойство worksheet.DataSource во время выполнения. Это потому, что лист всегда использует информацию о привязке источника данных в теге рабочего листа в файле ASPX. Чтобы привязать лист к другому источнику данных во время выполнения, удалите информацию о привязке источника данных в теге рабочего листа в файле ASPC. Измените тег на это: 

**XML**

{{< highlight csharp >}}

 <acw:Worksheet BindStartRow="2" Name="Products" 

EnableCreateBindColumnHeader="True">



{{< /highlight >}}

Укажите свойства worksheet.DataSource и worksheet.DataMember перед вызовом метода DataBind.

{{% /alert %}}
