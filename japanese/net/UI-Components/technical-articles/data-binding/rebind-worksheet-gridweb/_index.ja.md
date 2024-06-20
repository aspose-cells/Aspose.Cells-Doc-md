---
title: Worksheet GridWebの再バインド
type: docs
weight: 50
url: /ja/net/aspose-cells-gridweb/rebind-worksheet-gridweb/
keywords: GridWeb,再バインド
description: この記事では、GridWebでワークシートを再バインドする方法について紹介します。
---

{{% alert color="primary" %}} 

データセットにワークシートをバインドすると、 

IDEのWorksheets Designerでワークシートをバインドすると、APSXファイルにワークシートタグが作成されます。 

次のようになります: 

**XML**

{{< highlight csharp >}}

 <acw:Worksheet DataMember="Products" BindStartRow="2" Name="Products" 

EnableCreateBindColumnHeader="True" DataSource='<%# dataSet11 %>'>



{{< /highlight >}}

GridWeb1.DataBind()またはWebWorksheet.DataBind()を呼び出すと、データセット11のデータがワークシートに表示されます。 

ワークシートを再バインドすることがあります: 

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

ワークシート.DataSourceプロパティを実行時に変更しても、シートは常にデータセット11にバインドされます。これは、シートが常にASPXファイル内のワークシートのタグにあるデータソースバインディング情報を使用しているためです。実行時にシートを別のデータソースにバインドするには、ASPXファイル内のワークシートタグからデータソースのバインディング情報を削除します。タグを次のように編集します: 

**XML**

{{< highlight csharp >}}

 <acw:Worksheet BindStartRow="2" Name="Products" 

EnableCreateBindColumnHeader="True">



{{< /highlight >}}

DataBindメソッドを呼び出す前に、worksheet.DataSourceおよびworksheet.DataMemberプロパティを指定します。

{{% /alert %}}
