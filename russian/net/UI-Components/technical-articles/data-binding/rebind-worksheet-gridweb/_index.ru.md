---
title: Перепривязать рабочий лист GridWeb
type: docs
weight: 50
url: /ru/net/rebind-worksheet-gridweb/
---
{{% alert color="primary" %}} 

 Когда вы привязываете рабочий лист к набору данных с

 Конструктор рабочих листов в среде IDE, тег рабочего листа будет создан в APSX.

 файл. Это может выглядеть так:

**XML**

{{< highlight "csharp" >}}

 <acw:Worksheet DataMember="Products" BindStartRow="2" Name="Products" 

EnableCreateBindColumnHeader="True" DataSource='<%# dataSet11 %>'>



{{< /highlight >}}

 При вызове GridWeb1.DataBind() или WebWorksheet.DataBind() рабочий лист будет заполнен данными из dataSet11.

 Иногда вам может понадобиться повторно связать рабочий лист:

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

**ВБ**

{{< highlight "csharp" >}}

 Private Sub Button1_Click(ByVal sender As System.Object, ByVal e As 

System.EventArgs) Handles Button1.Click

    GridWeb1.WebWorksheets(0).Cells.Clear()

    ' Load data to the dataSet11.

    LoadData(dataSet11)

    GridWeb1.WebWorksheets(0).DataBind()

End Sub



{{< /highlight >}}

Рабочий лист всегда будет привязан к dataSet11, даже если вы измените свойство worksheet.DataSource во время выполнения. Это связано с тем, что лист всегда использует информацию о привязке источника данных в теге рабочего листа в файле ASPX. Чтобы привязать лист к другому источнику данных во время выполнения, удалите информацию о привязке источника данных в теге рабочего листа в файле ASPC. Измените тег на это:

**XML**

{{< highlight "csharp" >}}

 <acw:Worksheet BindStartRow="2" Name="Products" 

EnableCreateBindColumnHeader="True">



{{< /highlight >}}

Укажите свойства worksheet.DataSource и worksheet.DataMember перед вызовом метода DataBind.

{{% /alert %}}
