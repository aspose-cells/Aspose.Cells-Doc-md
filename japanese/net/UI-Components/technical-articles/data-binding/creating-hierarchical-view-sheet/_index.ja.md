---
title: 階層ビュー シートの作成
type: docs
weight: 30
url: /ja/net/creating-hierarchical-view-sheet/
---
{{% alert color="primary" %}} 

データ バインディングは、強力で使いやすい GridWeb 機能です。データベース テーブルに格納されたデータが DataSet にフェッチされ、データが入力されます。

データ テーブルを表します。データ バインディング機能を使用すると、相互にリンクされたデータの階層ビュー (マスターと子のビュー) を作成し、

コントロールに表示して、よりエレガントにします。

このトピックでは、階層ビュー シートの作成について説明します。シート内の一部の行には子ビューがあります。ユーザーが行の**拡大**

ボタン{{< emoticons/cross >}}、その行の子ビュー テーブルが下に展開されます。この機能は、階層ビュー レポートを作成するのに非常に役立ちます。

**階層ビューを持つテーブル** 

![todo:画像_代替_文章](creating-hierarchical-view-sheet_1.png)

{{% /alert %}} 
## **DataTable のリレーションを作成する**
たとえば、ADO.Net API を使用して、データベース テーブルからデータを抽出します。階層ビュー シートを作成するには、DataSet を設計する必要があります

いくつかのテーブルに基づいてオブジェクトを作成し、最初にそれらの間の関係を作成します。 VS.NET を使用する**データセット デザイナー**関係を作成します。の

この例では、Customers、Orders、Order Details の 3 つの DataTable があります。シートには、デフォルトですべての顧客情報が表示されます。いつ

ユーザーが顧客を展開すると、顧客が行ったすべての注文がグリッドに表示されます。ユーザーが注文を展開すると、グリッドに詳細が表示されます

その順序の。データは階層的です。注文の詳細は注文の下にリストされ、注文は顧客の下にリストされます。

これが機能するには、データ テーブル間で次の関係を確立する必要があります。

1.  DataTable Orders に外部キーを作成します。キー フィールドは CustomerID です。

![todo:画像_代替_文章](creating-hierarchical-view-sheet_2.png)




1. DataTable Order Details に外部キーを作成します。キー フィールドは OrderID です。

![todo:画像_代替_文章](creating-hierarchical-view-sheet_3.png)



 DataSet デザイナーは次のようになります。

![todo:画像_代替_文章](creating-hierarchical-view-sheet_4.png)
### **ワークシートをバインド**
今すぐ使用**ワークシート デザイナー**ワークシートの DataSource と DataMember を設定し、データ フィールド バインド列を構成します。

コントロールは、バインディング オブジェクト (通常は DataRowView オブジェクト) が持つレコードに対応する各行に + アイコンを自動的に追加します。

子ビュー。 + アイコンをクリックすると、レコードが展開されて子ビューが表示されます。以下の例では、**ワークシート デザイナー**をバインドする

ワークシートをルートの親 DataTable Customers に追加します。

![todo:画像_代替_文章](creating-hierarchical-view-sheet_5.png)
### **子テーブルのバインド列をカスタマイズする**
コントロールは、開発者が子テーブルのバインド列をカスタマイズするために使用する GridWeb.BindingChildView という名前のイベントを提供します。この例

注文の詳細を表示する必要があります」**単価**通貨形式のフィールド。イベント ハンドラーを追加して、バインド列の数値形式を変更します。

**C#**

{{< highlight "csharp" >}}

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

**VB.NET**

{{< highlight "csharp" >}}

 'Handles the BindingChildView event to set the UnitPrice column.

Private Sub GridWeb1_BindingChildView(ByVal childGrid As Aspose.Cells.GridWeb.GridWeb, ByVal childSheet As 

Aspose.Cells.GridWeb.Data.WebWorksheet) Handles GridWeb1.BindingChildView

    Dim view As DataView = CType(childSheet.DataSource, DataView)

    If view.Table.TableName = "Order Details" Then

        childSheet.BindColumns("UnitPrice").NumberType = NumberType.Currency3

    End If

End Sub



{{< /highlight >}}
### **データベースとバインドからデータをロードする**
で説明されているように[GridWeb の Worksheets Designer を使用して Worksheet を DataSet にバインドする](/cells/ja/net/binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer/),
Page_Load ブロックにコードを追加して、データベースから DataSet にデータをロードし、DataSet をシートにバインドする必要があります。

次の一歩。

Asppose.Grid.Web.Data.WebWorksheet クラスには、いくつかの便利なプロパティがあります。

- たとえば、プロパティ EnableCreateBindColumnHeader は、シート内のバインドされた列の見出しを作成するために使用されます。

 headers は、バインドされた列名を表示します。値を取ります**真実**また**間違い**. 

- プロパティ BindStartRow および BindStartColumn は、ソースがバインドされる GridWeb コントロールのシート内の位置を指定します。
- プロパティ EnableExpandChildView は、ワークシートの展開された子ビューを無効にするために使用されます。デフォルトでは、true に設定されています。

クラスにはいくつかの便利なメソッドもあります。

- DataBind() メソッドは、シートをソースにバインドします。
- CreateNewBindRow() は新しい行を追加し、それをデータ ソースにバインドします。
- DeleteBindRow() はバインドされた行を削除します。
- SetRowExpand() メソッドは、展開された行を設定し、子ビューのコンテンツをデータ バインディング モードで表示します。
- GetRowExpand() メソッドは、行が展開されているかどうかを示すブール値を取得します。

以下のコードでは、DataSet オブジェクト "dataSet21" に 3 つのテーブルに基づくデータが入力されます。 Customers テーブルがフィルター処理されて、

階層表示の最初のテーブル。 「シート」という名前の WebWorksheet オブジェクトが作成され、最初にシートがクリアされてから設定されます

データソースにリンクされています。

**C#**

{{< highlight "csharp" >}}

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

        WebWorksheet sheet = GridWeb1.WebWorksheets[0];

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

**VB.NET**

{{< highlight "csharp" >}}

 Private Sub Page_Load(System.Object としての ByVal 送信者、System.EventArgs としての ByVal e) MyBase.Load を処理します

'ここにページを初期化するためのユーザー コードを配置します

IsPostBack でない場合

BindWithoutInSheetHeaders()

終了条件

サブ終了

Private Sub BindWithoutInSheetHeaders()

 Dim db As DemoDatabase2 = New DemoDatabase2()

Dim path As String = MapPath(".")

 path = path.Substring(0, path.LastIndexOf("\"))

 path = path.Substring(0, path.LastIndexOf("\"))

 db.OleDbConnection1.ConnectionString = "Provider=Microsoft.Jet.OLEDB.4.0;Data Source=" + パス + "\Database\Northwind.mdb"

試す

' データベースに接続してデータを取得します。

 ' 顧客テーブル。

デシベル.OleDbDataAdapter1.Fill(DataSet21)

 ' 注文テーブル。

デシベル.OleDbDataAdapter2.Fill(DataSet21)

 'OrderDetailTable.

デシベル.OleDbDataAdapter3.Fill(DataSet21)

 ' データのフィルタリング

DataSet21.Customers.DefaultView.RowFilter = "CustomerID<'BSAAA'"

        Dim sheet As WebWorksheet = GridWeb1.WebWorksheets(0)

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
