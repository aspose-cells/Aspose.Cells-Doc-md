---
title: 階層ビュー シートの作成
type: docs
weight: 30
url: /ja/net/aspose-cells-gridweb/create-hierarchical-view-sheet/
keywords: GridWeb, 階層的
description: この記事では、GridWeb で階層ビューを作成する方法について紹介します。
---

{{% alert color="primary" %}} 

データ バインディングは、強力で使いやすい GridWeb の機能です。データベーステーブルに保存されたデータを取得して DataSet に入れ、データを表すデータ テーブルを作成します。データ バインディング機能を使用すると、相互リンクされたデータの階層ビュー（マスター-チャイルド ビュー）を作成し、コントロールに表示することができます。 

そして、より洗練された表示になります。 

このために、以下のリレーションシップをデータ テーブル間に確立する必要があります。 

このトピックでは、階層ビュー シートの作成について説明します。シートの一部の行には子ビューがあります。ユーザーが行の **展開** をクリックすると、

button {{< emoticons/cross >}}, the child view table of that row is expanded down. This feature is very helpful for building a hierarchical view report. 

**階層ビューを持つテーブル** 

![todo:image_alt_text](creating-hierarchical-view-sheet_1.png)

{{% /alert %}} 
## **データテーブルにリレーションシップを作成する**
たとえば、ADO.Net API を使用してデータベーステーブルからデータを抽出する場合、階層ビュー シートを作成するには、まず、いくつかのテーブルに基づいて DataSet オブジェクトを設計し、それらの間に関係を作成する必要があります。

VS.NET の **DataSet Designer** を使用して、関係を作成します。この例では、Customers、Orders、Order Details の 3 つの DataTable があります。シートでは、デフォルトですべての顧客情報が表示されます。ユーザーが顧客を展開すると、 

グリッドがその顧客が行ったすべての注文を表示します。ユーザーが注文を展開すると、グリッドがその注文の詳細を表示します。データは階層的です。 

注文の詳細は注文の下にリストされ、注文は顧客の下にリストされます。 

このためには、データテーブル間に次のリレーションシップを確立する必要があります。

1. DataTable Orders に外部キーを作成し、キー フィールドは CustomerID です。

1. DataTable Order Details に外部キーを作成し、キー フィールドは OrderID です。 

![todo:image_alt_text](creating-hierarchical-view-sheet_2.png)




1. DataTableのOrder Detailsに外部キーを作成します。キーのフィールドはOrderIDです。 

![todo:image_alt_text](creating-hierarchical-view-sheet_3.png)



データセット デザイナーは次のようになります。 

![todo:image_alt_text](creating-hierarchical-view-sheet_4.png)
### **ワークシートにバインド**
**Worksheets Designer** を使用して、ワークシートの DataSource と DataMember を設定し、データフィールドのバインディング列を構成します。 

各行に自動的に + アイコンが追加されます。このアイコンは、バインドオブジェクト（通常は DataRowView オブジェクト）に対応するレコードごとに表示されます。+ アイコンをクリックすると、レコードが展開されて子ビューが表示されます。以下の例では、**Worksheets Designer** を使用してバインドします。 

子ビュー。+アイコンをクリックすると、レコードが展開して子ビューが表示されます。以下の例では、**Worksheets Designer**を使用して 

ルート親 DataTable Customers へのワークシート。 

![todo:image_alt_text](creating-hierarchical-view-sheet_5.png)
### **子テーブルのバインド列をカスタマイズする**
コントロールは、開発者が子テーブルのバインド列をカスタマイズするために使用する GridWeb.BindingChildView という名前のイベントを提供します。この例 

は、通貨形式で注文詳細の **UnitPrice** フィールドを表示する必要があります。バインド列の数値形式を変更するためのイベントハンドラを追加します。 

**C#**

{{< highlight csharp >}}

 // Handles the BindingChildView event to set the UnitPrice column.

private void GridWeb1_BindingChildView(Aspose.Cells.GridWeb.GridWeb childGrid, Aspose.Cells.GridWeb.Data.WebWorksheet childSheet)

{

    DataView view = (DataView)childSheet.DataSource;

    if (view.Table.TableName == "Order Details")

    {

        childSheet.BindColumns["UnitPrice"].NumberType = NumberType.Currency3;

    }

}



{{< /highlight >}}

ワークシートで GridDesktop データ バインディング機能を実装する

{{< highlight csharp >}}

 'Handles the BindingChildView event to set the UnitPrice column.

Private Sub GridWeb1_BindingChildView(ByVal childGrid As Aspose.Cells.GridWeb.GridWeb, ByVal childSheet As 

Aspose.Cells.GridWeb.Data.WebWorksheet) Handles GridWeb1.BindingChildView

    Dim view As DataView = CType(childSheet.DataSource, DataView)

    If view.Table.TableName = "Order Details" Then

        childSheet.BindColumns("UnitPrice").NumberType = NumberType.Currency3

    End If

End Sub



{{< /highlight >}}
### **データベースからデータを読み込み、バインドする**
Aspose.Cells.GridWeb のワークシートデザイナーを使用してデータセットにワークシートをバインドする の記載にあるように、
次の手順でデータをデータベースからデータセットにロードし、データセットをシートにバインドするには、Page_Load ブロックにコードを追加する必要があります。 

次のステップ。 

Asppose.Grid.Web.Data.WebWorksheet クラスには、いくつかの便利なプロパティがあります。

たとえば、プロパティ EnableCreateBindColumnHeader は、シート内のバインド列の見出しを作成するために使用されます。また、列

ヘッダーは、バインドされた列の名前を表示します。値には **true** または **false** を取ります。 

プロパティ BindStartRow および BindStartColumn は、ソースの GridWeb コントロールのシート内の位置を指定します。
プロパティ EnableExpandChildView は、ワークシートの拡張子を無効にするために使用されます。デフォルトでは true に設定されています。

このクラスには、いくつかの便利なメソッドもあります。 

- DataBind() メソッドは、ソースとシートをバインドします。
- CreateNewBindRow() は、新しい行を追加してそれをデータソースにバインドします。
- DeleteBindRow() は、バインドされた行を削除します。
- SetRowExpand() メソッドは、展開された行を設定し、データバインディングモードで子ビューコンテンツを表示します。
- GetRowExpand() メソッドは、行が展開されているかどうかを示すブール値を取得します。

以下のコードでは、DataSet オブジェクト "dataSet21" に、3 つのテーブルに基づくデータが入力されます。顧客テーブルはフィルタリングされ、階層的な表示の最初のテーブルとなります。"sheet" という名前の WebWorksheet オブジェクトが作成され、まずシートをクリアし、次に 

データ ソースにリンクされます。 

**VB.NET** 

**C#**

{{< highlight csharp >}}

 private void Page_Load(object sender, System.EventArgs e)

{

    // Put user code to initialize the page here

    if (!IsPostBack)

    {

        BindWithoutInSheetHeaders();

    }

}

private void BindWithoutInSheetHeaders()

{

    DemoDatabase2 db = new DemoDatabase2();

    string path = MapPath(".");

    path = path.Substring(0, path.LastIndexOf("\\"));

    path = path.Substring(0, path.LastIndexOf("\\"));

    db.oleDbConnection1.ConnectionString = "Provider=Microsoft.Jet.OLEDB.4.0;Data Source=" + path + "\\Database\\Northwind.mdb";

    try

    {

        // Connects to database and fetches data.

        // Customers Table.

        db.oleDbDataAdapter1.Fill(dataSet21);

        // Orders Table.

        db.oleDbDataAdapter2.Fill(dataSet21);

        // OrderDetailTable.

        db.oleDbDataAdapter3.Fill(dataSet21);

        // Filter data

        dataSet21.Customers.DefaultView.RowFilter = "CustomerID<'BSAAA'";

        WebWorksheet sheet = GridWeb1.WorkSheets[0];

        // Clears the sheet.

        sheet.Cells.Clear();

        // Disables creating in-sheet headers.

        sheet.EnableCreateBindColumnHeader = false;

        // Data cells begin from row 0.

        sheet.BindStartRow = 0;

        // Bind the sheet to the dataset.

        sheet.DataBind();

    }

    finally

    {

        db.oleDbConnection1.Close();

    }

}



{{< /highlight >}}

ワークシートで GridDesktop データ バインディング機能を実装する

{{< highlight csharp >}}

 Private Sub Page_Load(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles MyBase.Load

    'Put user code to initialize the page here

    If Not IsPostBack Then

        BindWithoutInSheetHeaders()

    End If

End Sub

Private Sub BindWithoutInSheetHeaders()

    Dim db As DemoDatabase2 = New DemoDatabase2()

    Dim path As String = MapPath(".")

    path = path.Substring(0, path.LastIndexOf("\"))

    path = path.Substring(0, path.LastIndexOf("\"))

    db.OleDbConnection1.ConnectionString = "Provider=Microsoft.Jet.OLEDB.4.0;Data Source=" + path + "\Database\Northwind.mdb"

    Try

        ' Connects to database and fetches data.

        ' Customers Table.

        db.OleDbDataAdapter1.Fill(DataSet21)

        ' Orders Table.

        db.OleDbDataAdapter2.Fill(DataSet21)

        ' OrderDetailTable.

        db.OleDbDataAdapter3.Fill(DataSet21)

        ' Filter data

        DataSet21.Customers.DefaultView.RowFilter = "CustomerID<'BSAAA'"

        Dim sheet As WebWorksheet = GridWeb1.WorkSheets(0)

        ' Clears the sheet.

        sheet.Cells.Clear()

        ' Disables creating in-sheet headers.

        sheet.EnableCreateBindColumnHeader = False

        ' Data cells begin from row 0.

        sheet.BindStartRow = 0

        ' Bind the sheet to the dataset.

        sheet.DataBind()

    Finally

        db.OleDbConnection1.Close()

    End Try

End Sub



{{< /highlight >}}
