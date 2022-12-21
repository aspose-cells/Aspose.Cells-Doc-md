---
title: ワークシート GridWeb を再バインド
type: docs
weight: 50
url: /ja/net/rebind-worksheet-gridweb/
---
{{% alert color="primary" %}} 

ワークシートをデータセットにバインドすると、

 IDE のワークシート デザイナー。APSX でワークシート タグが作成されます。

ファイル。次のようになります。

**XML**

{{< highlight "csharp" >}}

 <acw:Worksheet DataMember="Products" BindStartRow="2" Name="Products" 

EnableCreateBindColumnHeader="True" DataSource='<%# dataSet11 %>'>



{{< /highlight >}}

 GridWeb1.DataBind() または WebWorksheet.DataBind() を呼び出すと、ワークシートに dataSet11 のデータが入力されます。

ワークシートを再バインドしたい場合があります。

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

実行時に worksheet.DataSource プロパティを変更しても、ワークシートは常に dataSet11 にバインドされます。これは、シートが ASPX ファイル内のワークシートのタグにある DataSource バインディング情報を常に使用するためです。実行時にシートを別のデータ ソースにバインドするには、ASPC ファイルのワークシート タグのデータ ソース バインド情報を削除します。タグを次のように編集します。

**XML**

{{< highlight "csharp" >}}

 <acw:Worksheet BindStartRow="2" Name="Products" 

EnableCreateBindColumnHeader="True">



{{< /highlight >}}

DataBind メソッドを呼び出す前に、worksheet.DataSource および worksheet.DataMember プロパティを指定します。

{{% /alert %}}
