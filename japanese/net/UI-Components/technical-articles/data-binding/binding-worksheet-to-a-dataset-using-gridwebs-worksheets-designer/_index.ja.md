---
title: GridWebs Worksheets Designer を使用して Worksheet を DataSet にバインドする
type: docs
weight: 20
url: /ja/net/binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer/
---
{{% alert color="primary" %}} 

この記事では、ワークシート デザイナーである Aspose.Cells.GridWeb で提供される特別なツールを使用して、GUI モードでワークシートをデータベース テーブルにバインドする簡単な方法について説明します。

{{% /alert %}} 
## **Worksheets Designer を使用してワークシートをデータベースにバインドする**
	**ステップ 1: サンプル データベースの作成**
1. まず、この記事で使用するサンプル データベースを作成します。 Microsoft Access を使用して、Products というテーブルを含むデータベースを作成しています。そのスキーマを以下に示します。
   **Products テーブルの設計情報** 

![todo:画像_代替_文章](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_1.png)




1. Products テーブルにいくつかのダミー レコードが追加されます。
   **Products テーブルのレコード** 

![todo:画像_代替_文章](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_2.png)
### **ステップ 2: サンプル アプリケーションの設計**
ASP.NET Web アプリケーションは、以下に示すように Visual Studio.NET で作成および設計されています。
**設計されたサンプル アプリケーション** 

![todo:画像_代替_文章](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_3.png)
### **ステップ 3: サーバー エクスプローラーを使用してデータベースに接続する**
データベースに接続する時が来ました。 Visual Studio.NET のサーバー エクスプローラーを使用して簡単に実行できます。

1. 選択する**データの接続**の**サーバー エクスプローラー**右クリックします。
1. 選択する**接続を追加**メニューから。
   **接続の追加オプションの選択** 

![todo:画像_代替_文章](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_4.png)



[データ リンク プロパティ] ダイアログが表示されます。
**[データ リンク プロパティ] ダイアログ** 

![todo:画像_代替_文章](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_5.png)



このダイアログを使用して、任意のデータベースに接続できます。デフォルトでは、SQL Server データベースに接続できます。この例では、Microsoft Access データベースに接続する必要があります。

1. クリック**プロバイダー**タブ。
1. 選択する**Microsoft Jet 4.0 OLE DB プロバイダー**から**OLE DB プロバイダー**リスト。
1. クリック**次**.
   **OLE DB プロバイダーを選択した後に [次へ] をクリックする** 

![todo:画像_代替_文章](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_6.png)


の**繋がり**タブページが開きます。

1.  Microsoft Access データベース ファイル (この場合は db.mdb) を選択し、**わかった**.
   **データベースファイルを選択してOKボタンをクリック** 

![todo:画像_代替_文章](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_7.png)

{{% alert color="primary" %}} 

クリック後**わかった**、Microsoft Access データベースへのデータベース接続が**サーバー エクスプローラー**.接続をダブルクリックして、データベース内のすべてのテーブル、ビュー、およびストアド プロシージャを表示します。

{{% /alert %}} 
### **手順 4: データベース接続オブジェクトをグラフィカルに作成する**
1. を使用して、データベース内のテーブルを参照します。**サーバー エクスプローラー**.
 Products テーブルは 1 つだけです。
1. から Products テーブルをドラッグ アンド ドロップします。**サーバー エクスプローラー**に**ウェブフォーム**.
   **Products テーブルをサーバー エクスプローラーからドラッグし、Web フォームにドロップする** 

![todo:画像_代替_文章](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_8.png)



ダイアログが表示される場合があります。
**接続文字列にデータベース パスワードを含めることを確認するダイアログ** 

![todo:画像_代替_文章](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_9.png)



接続文字列にデータベース パスワードを含めるかどうかを決定します。この例では、**パスワードを含めないでください**. 
つのデータベース接続オブジェクト (oleDbConnection1 と oleDbDataAdapter1) が作成され、追加されました。
**データベース接続オブジェクト (oleDbConnection1 & oleDbDataAdapter1) の作成と表示** 

![todo:画像_代替_文章](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_10.png)



### **ステップ 5: DataSet の生成**
ここまでで、データベース接続オブジェクトを作成しましたが、データベースに接続した後にデータを保存する場所が必要です。 DataSet オブジェクトはデータを正確に格納でき、VS.NET IDE を使用して簡単に生成することもできます。

1. 選択する**oleDbDataAdaper1**右クリックします。
1. 選択する**DataSet の生成**メニューからのオプション。
   **[DataSet の生成] オプションの選択** 

![todo:画像_代替_文章](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_11.png)



[DataSet の生成] ダイアログが表示されます。
ここで、作成する新しい DataSet オブジェクトの名前と、それに追加するテーブルを選択できます。

1. を選択**このデータセットをデザイナーに追加します**オプション。
1. クリック**わかった**.
   **OKボタンをクリックしてDataSetを生成** 

![todo:画像_代替_文章](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_12.png)



dataSet11 オブジェクトがデザイナーに追加されます。
**生成され、デザイナーに追加された DataSet** 

![todo:画像_代替_文章](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_13.png)
### **ステップ 6: ワークシート デザイナーの使用**
さぁ、秘密を解き明かしましょう。

1. GridWeb コントロールを選択して右クリックします。
1. 選択する**ワークシート デザイナー**メニューからのオプション。

   **ワークシート デザイナ オプションの選択** 

![todo:画像_代替_文章](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_14.png)



ワークシート コレクション エディター (ワークシート デザイナーとも呼ばれます) が表示されます。
**ワークシート コレクション エディタ ダイアログ** 

![todo:画像_代替_文章](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_15.png)



このダイアログには、Sheet1 をデータベース内の任意のテーブルにバインドするように構成できるいくつかのプロパティが含まれています。

1. を選択**情報元**財産。
前の手順で生成された dataSet11 オブジェクトがメニューに表示されます。
1. dataSet11 を選択します。
1. クリック**データメンバー**財産。
 Worksheets Designer は、dataSet11 内のテーブルのリストを自動的に表示します。 Products テーブルは 1 つだけです。
1. Products テーブルを選択します。
   **DataSource および DataMember プロパティの設定** 

![todo:画像_代替_文章](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_16.png)




1. を確認してください**BindColumns**財産。
   **BindColumns プロパティのクリック** 

![todo:画像_代替_文章](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_17.png)



をクリックすると**BindColumns**プロパティは、BindColumn コレクション エディターを開きます。
**BindColumn コレクション エディター** 

![todo:画像_代替_文章](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_18.png)



BindColumn コレクション エディターでは、**製品**テーブルは BindColumns コレクションに自動的に追加されます。

1. 任意の列を選択し、そのプロパティをカスタマイズします。
たとえば、各列のキャプションを変更できます。
   **ProductID 列のキャプションの変更** 

![todo:画像_代替_文章](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_19.png)




1. 変更後、 をクリックします。**わかった**.
1. をクリックして、すべてのダイアログを閉じます。**わかった**.
最後に、WebForm1.aspx ページに戻ります。
   **ワークシート デザイナーの使用後に WebForm1.aspx ページに戻る** 

![todo:画像_代替_文章](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_20.png)


上記では、 Products テーブルの列名が表示されています。列の幅が狭いため、一部の列の完全な名前が完全には表示されません。
### **手順 7: Page_Load イベント ハンドラーへのコードの追加**
Worksheets Designer を使用した後は、(oleDbDataAdapter1 を使用して) データベースからのデータを dataSet11 オブジェクトに入力し、その DataBind メソッドを呼び出して GridWeb コントロールを dataSet11 にバインドするコードを Page_Load イベント ハンドラーに追加するだけです。

1. コードを追加します。

**C#**

{{< highlight "csharp" >}}

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

**VB.NET**

{{< highlight "csharp" >}}

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

1. Page_Load イベント ハンドラに追加されたコードを確認します。
   **Page_Load イベント ハンドラに追加されたコード** 

![todo:画像_代替_文章](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_21.png)
### **ステップ 8: アプリケーションの実行**
アプリケーションをコンパイルして実行します。**Ctrl+F5**またはクリック**始める**. 
**アプリケーションの実行** 

![todo:画像_代替_文章](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_22.png)



コンパイル後、WebForm1.aspx ページがブラウザー ウィンドウで開かれ、データベースからすべてのデータが読み込まれます。
**データベースから GridWeb コントロールに読み込まれたデータ** 

![todo:画像_代替_文章](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_23.png)
## **GridWeb コントロールの操作**
データが GridWeb コントロールに読み込まれると、ユーザーはデータを制御できます。 GridWeb では、さまざまな種類のデータ操作機能が提供されています。
### **データ検証**
Aspose.Cells.GridWeb は、データベースで定義されたデータ型に従って、バインドされたすべての列に対して適切な検証規則を自動的に作成します。セルの上にカーソルを置くと、セルの検証タイプが表示されます。
**セルの検証タイプの確認** 

![todo:画像_代替_文章](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_24.png)

ここで、選択したセルには**<INT>**つまり、ユーザーは整数値のみを入力できます。別の値を入力すると、検証エラーが発生します。さらに、**<必須>**は、製品 ID の値を送信する必要があることを示しています。
### **行の削除**
行を削除するには、行 (または行内の任意のセル) を選択し、右クリックして選択します。**行を削除**.
**メニューから [行の削除] オプションを選択する** 

![todo:画像_代替_文章](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_25.png)


行は即座に削除されます。
**グリッドデータ（行削除後）** 

![todo:画像_代替_文章](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_26.png)
### **行の編集**
セルまたは行のデータを編集し、**セーブ**また**送信**変更を保存します。
### **行の追加**
1. 行を追加するには、セルを右クリックして**行を追加する**.
   **メニューから [行の追加] オプションを選択する** 

![todo:画像_代替_文章](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_27.png)



シートの他の行の最後に新しい行が追加されます。
**グリッドに追加された新しい行** 

![todo:画像_代替_文章](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_28.png)



新しい行の左側にはアスタリスクがあります{{< emoticons/cross >}}、行が新しいことを示します。

1. 新しい行に値を追加します。
1. クリック**セーブ**また**送信**変更を確認します。
   ***Save をクリックしてデータへの変更を保存する**ボタン*

![todo:画像_代替_文章](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_29.png)
### **数値フォーマットの設定**
現時点での価格は、**商品価格**列は数値として表示されます。通貨のように見せることができます。

1. Visual Studio.NET に戻ります。
1. BindColumn コレクション エディターを開きます。
の**番号タイプ**のプロパティ**商品価格**列がに設定されています**全般的**.
   **General に設定された NumberType プロパティ** 

![todo:画像_代替_文章](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_30.png)




1. クリック**ドロップダウンリスト**そして選択**通貨4**リストから。
   **NumberType プロパティが Currency4 に変更されました** 

![todo:画像_代替_文章](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_31.png)




1. アプリケーションを再度実行します。
の値**商品価格**列が通貨になりました。
   **通貨での商品価格 数値形式** 

![todo:画像_代替_文章](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_32.png)
### **データの編集**
これまでのアプリケーションでは、ユーザーはテーブル データの表示のみを許可されていました。ユーザーは GridWeb コントロールでデータを編集できますが、ブラウザを閉じてデータベースを開いても何も変わりません。加えられた変更はデータベースに保存されません。

次の例では、アプリケーションにコードを追加して、GridWeb が変更をデータベースに保存できるようにします。

1. 開く**プロパティ**ペインを開き、リストから GridWeb コントロールの SaveCommand イベントを選択します。
   **GridWeb の SaveCommand イベントの選択** 

![todo:画像_代替_文章](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_33.png)




1. ダブルクリック**保存コマンド**イベントと VS.NET は、GridWeb1_SaveCommand イベント ハンドラーを作成します。
1.  oleDbDataAdapter1 を使用してワークシートにバインドされた DataSet 内の変更されたデータでデータベースを更新するコードをこのイベント ハンドラーに追加します。

**C#**

{{< highlight "csharp" >}}

 //Implementing the event handler for SaveCommand event

private void GridWeb1_SaveCommand(object sender, System.EventArgs e)

{

    try

    {

        //Getting the modified data of worksheet as a DataSet

        DataSet dataset = (DataSet)GridWeb1.WebWorksheets[0].DataSource;

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

**VB.NET**

{{< highlight "csharp" >}}

 'Implementing the event handler for SaveCommand event

Private Sub GridWeb1_SaveCommand(ByVal sender As Object, ByVal e As System.EventArgs) Handles GridWeb1.SaveCommand

    Try

        'Getting the modified data of worksheet as a DataSet

        Dim dataset As DataSet = CType(GridWeb1.WebWorksheets(0).DataSource, DataSet)

        'Updating database according to modified DataSet

        oleDbDataAdapter1.Update(dataset)

    Finally

        'Closing database connection

        oleDbConnection1.Close()

    End Try

End Sub



{{< /highlight >}}

GridWeb1_SaveCommand イベント ハンドラーに追加されたコードも確認できます。
**GridWeb1_SaveCommand イベント ハンドラーに追加されたコード** 

![todo:画像_代替_文章](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_34.png)

を使用して変更をデータベースに保存します。**セーブ**ボタンは確実にそれらを保存します。
## **結論**
{{% alert color="primary" %}} 

データバインディングは、Aspose.Cells.GridWeb の重要な機能です。 Aspose.Cells.GridWeb が提供する Worksheets Designer ユーティリティを使用して、ワークシートをデータベースにバインドするのは簡単です。 Aspose.Cells.GridWeb は、強力なグリッド ソリューションを作成する際の時間と労力を節約します。

{{% /alert %}}
