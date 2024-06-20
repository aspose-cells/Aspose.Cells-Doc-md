---
title: GridWebのワークシートデザイナーを使用したデータセットへのバインディング
type: docs
weight: 20
url: /ja/net/aspose-cells-gridweb/bind-worksheet-to-a-dataset-use-designer/
keywords: GridWeb,bind,DataSet,Designer,designer
description: この記事では、Worksheets Designerを使用してデータセットをワークシートにバインドする方法について紹介します。
---

{{% alert color="primary" %}} 

この記事では、Aspose.Cells.GridWebに供給される特別なツールを使用してGUIモードでデータベーステーブルをワークシートにバインドする簡単なアプローチについて説明します。 

{{% /alert %}} 
## **Worksheets Designerを使用してデータベースとワークシートをバインド**
	**ステップ1: サンプルデータベースの作成**
1. ますますは、この記事で使用されるサンプルデータベースを作成します。データベースは、Productsというテーブルを含むデータベースをMicrosoft Accessを使用して作成しています。スキーマは以下の通りです。
   **Productsテーブルの設計情報** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_1.png)




1. 商品テーブルにいくつかのダミーレコードを追加します。
   **Productsテーブル内のレコード** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_2.png)
### **ステップ2：サンプルアプリケーションの設計**
ASP.NETウェブアプリケーションを作成し、Visual Studio.NETで設計します。以下に示すように。 
**設計されたサンプルアプリケーション** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_3.png)
### **ステップ3：サーバーエクスプローラを使用してデータベースに接続**
今度はデータベースに接続する時間です。Visual Studio.NETのサーバーエクスプローラを使用して簡単に行うことができます。 

1. **サーバーエクスプローラ** で **データ接続** を選択し、右クリックします。
1. メニューから **接続の追加** を選択します。
   **接続の追加** オプションを選択する 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_4.png)



データリンクプロパティダイアログが表示されます。 
**データリンクプロパティダイアログ** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_5.png)



このダイアログを使用して、任意のデータベースに接続できます。デフォルトでは、SQL Serverデータベースに接続することができます。この例では、Microsoft Accessデータベースに接続する必要があります。 

1. **プロバイダ** タブをクリックします。
1. **OLE DBプロバイダ**のリストから **Microsoft Jet 4.0 OLE DBプロバイダ** を選択します。
1. **次へ** をクリックします。
   **OLE DBプロバイダを選択してから次へをクリック** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_6.png)


**接続** タブページが開きます。 

1. Microsoft Accessデータベースファイル（この例ではdb.mdb）を選択し、**OK** をクリックします。
   **データベースファイルを選択してOKボタンをクリック** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_7.png)

{{% alert color="primary" %}} 

**OK** をクリックすると、**Server Explorer** にMicrosoft Accessデータベースへのデータベース接続が作成されます。接続をダブルクリックすると、データベース内のすべてのテーブル、ビュー、およびストアドプロシージャが表示されます。

{{% /alert %}} 
### **ステップ4：データベース接続オブジェクトのグラフィカル作成**
1. **Server Explorer** を使用してデータベース内のテーブルを参照します。
   テーブルはProductsだけです。 
1. **Server Explorer** から **Web Form** にProductsテーブルをドラッグアンドドロップします。
   **Server ExplorerからProductsテーブルをWeb Formにドラッグしてドロップする** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_8.png)



ダイアログが表示される場合があります。
**接続文字列にデータベースのパスワードを含めるかどうかを確認するためのダイアログ** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_9.png)



データベースの接続文字列にパスワードを含めるかどうかを決定します。この例では、「パスワードを含めない」を選択しました。 
2つのデータベース接続オブジェクト(oleDbConnection1とoleDbDataAdapter1)が作成および追加されました。
データベース接続オブジェクト(oleDbConnection1およびoleDbDataAdapter1)が作成され、表示されました。 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_10.png)



### **ステップ5: DataSetの生成**
これまでにデータベース接続オブジェクトを作成しましたが、データベースに接続した後にデータを保存する場所がまだ必要です。DataSetオブジェクトはデータを正確に保存でき、VS.NET IDEを使用して簡単に生成することもできます。 

1. **oleDbDataAdaper1** を選択し、右クリックします。
1. メニューから**Generate DataSet**オプションを選択します。
   **Generate DataSetオプションの選択** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_11.png)



Generate DataSetダイアログが表示されます。 
ここで、新しいDataSetオブジェクトの名前を選択し、それに追加するテーブルを選択できます。 

1. **このデータセットをデザイナーに追加**オプションを選択します。
1. **OK** をクリックします。
   **DataSetを生成するためのOKボタンをクリック** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_12.png)



dataSet11オブジェクトがデザイナーに追加されます。
**DataSetが生成され、デザイナーに追加されました** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_13.png)
### **ステップ6: ワークシートデザイナーの使用**
これで、秘密を公開する時間です。 

1. グリッドWebコントロールを選択し、右クリックします。
1. メニューから**Worksheets Designer**オプションを選択します。 

   **Worksheets Designerオプションの選択** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_14.png)



ワークシートのコレクションエディタ(ワークシートデザイナーとも呼ばれます)が表示されます。 
**ワークシートコレクションエディタダイアログ** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_15.png)



ダイアログには、Sheet1をデータベース内の任意のテーブルにバインドするために構成できるいくつかのプロパティが含まれています。

1. **DataSource** プロパティを選択します。
   前のステップで生成されたdataSet11オブジェクトがメニューにリストされます。 
1. dataSet11を選択します。
1. **DataMember** プロパティをクリックします。
   ワークシートデザイナーは、dataSet11内のテーブルのリストを自動的に表示します。ここには1つのテーブル、Productsがあります。
1. Products テーブルを選択します。
   **DataSourceおよびDataMemberプロパティの設定** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_16.png)




1. **BindColumns** プロパティをチェックします。
   **BindColumns** プロパティをクリックします。 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_17.png)



**BindColumns** プロパティをクリックすると、BindColumn コレクション エディタが開きます。
**BindColumns コレクション エディタ** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_18.png)



BindColumn コレクション エディタでは、Products テーブルのすべての列が自動的に BindColumns コレクションに追加されます。 

1. 任意の列を選択し、そのプロパティをカスタマイズします。
   例えば、各列の見出しを変更することができます。
   ProductID 列の見出しを変更する 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_19.png)




1. 変更を行った後、**OK** をクリックします。
1. **OK** をクリックしてすべてのダイアログを閉じます。
   最後に、Worksheets Designer を使用した後、WebForm1.aspx ページに戻ります。 
   Worksheets Designer を使用した後、WebForm1.aspx ページに戻る 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_20.png)


上記に、Products テーブルの列名が表示されています。一部の列名が完全に表示されていないため、列の幅が小さいです。 
### **ステップ 7: Page_Load イベントハンドラにコードを追加**
Worksheets Designer を使用したので、今は、データベースのデータを dataSet11 オブジェクトに充填し（oleDbDataAdapter1 を使用）、GridWeb コントロールを dataSet11 にバインドするために、Page_Load イベントハンドラにコードを追加するだけです。 

1. コードを追加します: 

**C#**

{{< highlight csharp >}}

 //Implementing Page_Load event handler

private void Page_Load(object sender, System.EventArgs e)

{

    //Checking if there is not any PostBack

    if (!IsPostBack)

    {

        try

        {

            //Filling DataSet with data 

            oleDbDataAdapter1.Fill(dataSet11);

            //Binding GridWeb with DataSet

            GridWeb1.DataBind();

        }

        finally

        {

            //Finally, closing database connection

            oleDbConnection1.Close();

        }

    }

}



{{< /highlight >}}

ワークシートで GridDesktop データ バインディング機能を実装する

{{< highlight csharp >}}

 'Implementing Page_Load event handler

Private Sub Page_Load(ByVal sender As Object, ByVal e As System.EventArgs) Handles MyBase.Load

    'Checking if there is not any PostBack

    If Not IsPostBack Then

        Try

            'Filling DataSet with data 

            oleDbDataAdapter1.Fill(dataSet11)

            'Binding GridWeb with DataSet

            GridWeb1.DataBind()

        Finally

            'Finally, closing database connection

            oleDbConnection1.Close()

        End Try

    End If

End Sub



{{< /highlight >}}

Page_Load イベントハンドラに追加されたコードを確認します。
   Page_Load イベントハンドラに追加されたコード 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_21.png)
### **ステップ 8: アプリケーションの実行**
アプリケーションをコンパイルして実行します: **Ctrl+F5** を押すか、**Start** をクリックします。 
アプリケーションの実行 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_22.png)



コンパイル後、WebForm1.aspx ページがブラウザウィンドウで開き、すべてのデータがデータベースから読み込まれます。
データベースから GridWeb コントロールにデータが読み込まれる 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_23.png)
## **GridWeb コントロールの操作**
GridWeb コントロールにデータが読み込まれると、ユーザーはデータを操作できます。GridWeb にはさまざまな種類のデータ操作機能が提供されています。 
### **データの検証**
Aspose.Cells.GridWeb は、データベースで定義されたデータ型に従って、すべてのバインドされた列に適切な検証ルールを自動的に作成します。 カーソルを上に置くことで、セルの検証タイプを確認できます。
セルの検証タイプをチェックする 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_24.png)

Here, the selected cell contains the **<INT>** validation, which means that users can only enter integer values into it. If they enter another value, a validation error occurs. Moreover, **<REQUIRED>** shows that the value Product ID must be submitted. 
### **行の削除**
行を削除するには、行（または行内の任意のセル）を選択し、右クリックして **行の削除** を選択します。
**メニューから行の削除オプションを選択** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_25.png)


行が即座に削除されます。
**行が削除された後のグリッドデータ** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_26.png)
### **行の編集**
セルや行のデータを編集してから **保存** または **送信** をクリックして変更を保存します。 
### **行の追加**
1. 行を追加するには、セルを右クリックして **行の追加** を選択します。
   **メニューから行の追加オプションを選択** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_27.png)



新しい行が他の行の末尾にシートに追加されます。
**グリッドに追加された新しい行** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_28.png)



At the left of the new row is an asterisk {{< emoticons/cross >}}, indicating that the row is new. 

1. 新しい行に値を追加します。
1. 変更を確認するには **保存** または **送信** をクリックします。
   **Save** ボタンをクリックしてデータの変更を保存する 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_29.png)
### **数値形式の設定**
現在、**製品価格** 列の価格は数値として表示されています。それらを通貨のように表示することができます。

1. Visual Studio.NET に戻ります。
1. BindColumn Collection Editor を開きます。
   **製品価格** 列の **NumberType** プロパティが **一般** に設定されています。
   **NumberType プロパティが一般に設定されています** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_30.png)




1. **DropDownList** をクリックし、リストから **Currency4** を選択します。
   **NumberType プロパティが通貨4に変更されました** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_31.png)




1. アプリケーションをもう一度実行します。
   **製品価格** 列の値は今や通貨です。
   **通貨の数値形式の製品価格** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_32.png)
### **データの編集**
これまでのアプリケーションはテーブルデータを表示するだけでした。ユーザーは GridWeb コントロールでデータを編集できますが、ブラウザを閉じてデータベースを開くと、何も変わっていません。行った変更はデータベースに保存されません。 

次の例では、アプリケーションにコードを追加して、GridWeb がデータベースに対して変更を保存できるようにします。 

1. **プロパティ** ペインを開き、リストから GridWeb コントロールの SaveCommand イベントを選択します。
   **GridWebのSaveCommandイベントを選択** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_33.png)




1. **SaveCommand** イベントをダブルクリックすると、VS.NET は GridWeb1_SaveCommand イベント ハンドラを作成します。
1. このイベント ハンドラにコードを追加し、oleDbDataAdapter1 を使用してワークシートにバインドされた DataSet 内の変更されたデータをデータベースに更新します。 

**C#**

{{< highlight csharp >}}

 //Implementing the event handler for SaveCommand event

private void GridWeb1_SaveCommand(object sender, System.EventArgs e)

{

    try

    {

        //Getting the modified data of worksheet as a DataSet

        DataSet dataset = (DataSet)GridWeb1.WorkSheets[0].DataSource;

        //Updating database according to modified DataSet

        oleDbDataAdapter1.Update(dataset);

    }

    finally

    {

        //Closing database connection

        oleDbConnection1.Close();

    }

}



{{< /highlight >}}

ワークシートで GridDesktop データ バインディング機能を実装する

{{< highlight csharp >}}

 'Implementing the event handler for SaveCommand event

Private Sub GridWeb1_SaveCommand(ByVal sender As Object, ByVal e As System.EventArgs) Handles GridWeb1.SaveCommand

    Try

        'Getting the modified data of worksheet as a DataSet

        Dim dataset As DataSet = CType(GridWeb1.WorkSheets(0).DataSource, DataSet)

        'Updating database according to modified DataSet

        oleDbDataAdapter1.Update(dataset)

    Finally

        'Closing database connection

        oleDbConnection1.Close()

    End Try

End Sub



{{< /highlight >}}

GridWeb1_SaveCommand イベント ハンドラに追加されたコードも確認できます
**GridWeb1_SaveCommand イベント ハンドラに追加されたコード** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_34.png)

変更をデータベースに保存する **Save** ボタンをクリックすると、確実に保存されます。
## **結論**
{{% alert color="primary" %}} 

データ バインディングは Aspose.Cells.GridWeb の重要な機能です。Aspose.Cells.GridWeb が提供する Worksheets Designer ユーティリティを使用して、データベースにワークシートをバインドすることは簡単です。Aspose.Cells.GridWeb を使用すると、強力なグリッド ソリューションの作成に時間と労力を節約できます。 

{{% /alert %}}
