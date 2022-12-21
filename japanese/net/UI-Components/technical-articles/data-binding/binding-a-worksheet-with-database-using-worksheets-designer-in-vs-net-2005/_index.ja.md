---
title: VS.Net 2005 でワークシート デザイナーを使用してワークシートをデータベースにバインドする
type: docs
weight: 40
url: /ja/net/binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005/
---
{{% alert color="primary" %}}

この記事では、ワークシートをデータベース テーブルにバインドする最も簡単な方法について説明します。**Visual Studio.Net 2005**という名前の Aspose.Cells.GridWeb に付属の特別なツールを使用して**ワークシート デザイナー**.この記事を読めば、Aspose.Cells.GridWeb のデータ バインディング機能を使用すると、**ワークシート デザイナー** .

{{% /alert %}}

## **VS.Net 2005 でワークシート デザイナーを使用してワークシートをデータベースにバインドする**

この記事の目的は、すべての開発者がデータ バインディング アプリケーションを作成する方法を学習できるようにすることです。**VS.ネット 2005**の使用と役割を理解する**ワークシート デザイナー**編集者。何かを学び、理解するための最良の方法は、例を通してです。したがって、この記事では、**ワークシート デザイナー**ワークシートをデータベースにバインドします。アプリケーションを段階的に作成しましょう。

### **ステップ 1: サンプル データベースの作成**

まず、この記事で使用するサンプル データベースを作成します。 MS Access を使用して、以下を含むサンプル データベースを作成しました。**製品**スキーマが以下に示されているテーブル:

![todo:画像_代替_文章](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_1.png)

**形：**の設計情報**製品**テーブル

いくつかのダミー レコードが**製品**図の下に示すようにテーブル:

![todo:画像_代替_文章](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_2.png)

**形：**のレコード**製品**テーブル

### **ステップ 2: サンプル アプリケーションの設計**

アン**ASP.NET Web アプリケーション**以下の図に示すように、Visual Studio.NET 2005 で作成および設計されています。これらのスクリーン ショットは、Visual Studio.Net 2005 で Aspose.Cells.GridWeb を使用することにあまり慣れていない開発者にとって役立ちます。

最初に VS.Net 2005 を起動します。

![todo:画像_代替_文章](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_3.png)

**形：** VS.Net 2005 の開始

File|New|Web Site... メニューから新しい Web サイトを作成します。

![todo:画像_代替_文章](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_4.png)

**形：**新しい Web サイトの作成

[ファイル|新規|Web サイト...] メニュー オプションをクリックした後、**新しい Web サイト**ダイアログが表示されます。クリック**ブラウズ**その中のボタン。

![todo:画像_代替_文章](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_5.png)

**形：**新しい Web サイト ダイアログ

をクリックした後、**ブラウズ**ボタンをクリックして、ローカル IIS の場所フォルダーを選択します。図に示すように、新しいフォルダーを作成して仮想フォルダーにすることができます。

![todo:画像_代替_文章](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_6.png)

**形：**新しいフォルダを作成する


をクリックした後、**開ける**ボタン**場所を選択**ダイアログ、**新しい Web サイト**ダイアログは次のようになります。

![todo:画像_代替_文章](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_7.png)

**形：**プロジェクトの場所の設定

これでプロジェクトが作成されました

![todo:画像_代替_文章](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_8.png)

**形：**作成したプロジェクト

### **XHTML および HTML モード**

**Aspose.Cells.GridWeb**VS.Net 2005 でデフォルトで実装されている XHTML モードを完全にサポートします。**XhtmlMode**のプロパティ**グリッドウェブ**コントロールはに設定されています**真実**Web ページにコントロールを配置すると、既定で。しかし、VS.Net 2005 でコントロールに HTML モードを実装する場合は、非常に簡単に実行できます。を変更する必要があります**<!DOCTYPE>**Web ページのソース コードに少しタグを付けて、**XhtmlMode**のプロパティ**グリッドウェブ**制御する**間違い** .

#### **このトピックでは、コントロールに HTML モードを使用します。したがって、以下の手順に従ってください**

##### **1. Web ページのソース ビューに切り替え、ソース コードで次の <!DOCTYPE> タグを見つけます。**

**XML**

{{< highlight "csharp" >}}

 <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

{{< /highlight >}}

そのタグを見つけたら、以下に示すように、ソース コードでその完全なタグを選択します。

![todo:画像_代替_文章](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_9.png)

**形：**選択中**<!DOCTYPE> タグ**

を交換してください**<!DOCTYPE>**ソースコードから次のタグを付けてください。

**XML**

{{< highlight "csharp" >}}

  <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN"> 

{{< /highlight >}}

![todo:画像_代替_文章](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_10.png)

**形：**変更中**<!DOCTYPE> タグ**

##### **2. GridWeb コントロールを Web フォームに追加した後。コントロールを選択し、[プロパティ] ウィンドウから XhtmlMode プロパティを選択して False に設定する必要があります。**

**GridWeb を Web フォームに追加する** 

を右クリック**ツールボックス**そして選択**アイテムを選択...**メニューから。

![todo:画像_代替_文章](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_11.png)

**形：**アイテムの選択

今すぐ選択**グリッドウェブ**コンポーネントとクリック**わかった**

{{% alert color="primary" %}}

![todo:画像_代替_文章](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_12.png)

**形：**選択中**グリッドウェブ**コンポーネントダイアログのコンポーネント

今、**グリッドウェブ**下図のように追加されます。

![todo:画像_代替_文章](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_13.png)

**形：** **グリッドウェブ**ツールボックスに追加されます

を置きます**グリッドウェブ**以下に示すように、Webフォームで。

![todo:画像_代替_文章](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_14.png)

**形：**配置する**グリッドウェブ**ウェブページで

{{% /alert %}} {{% alert color="primary" %}}

**手順** コントロールを選択します。**XhtmlMode**からのプロパティ**プロパティ**ウィンドウを開き、それを**間違い**価値。

{{% /alert %}}

##### **手順 3: サーバー エクスプローラーを使用してデータベースに接続し、接続オブジェクトを設定する**

最初に、以前に作成したプロジェクトに MS Access データベースを追加します。**ステップ1** .あなたはそれを見るかもしれません**デシベル.mdb**ファイルがプロジェクトに追加されます。

![todo:画像_代替_文章](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_15.png)

**形：**プロジェクトフォルダにデータベースを追加

今、私たちはに行きます**コンポーネント デザイナー**Web ページの右クリック メニュー オプションを使用して Web フォームのウィンドウを開きます。

![todo:画像_代替_文章](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_16.png)

**形：**選択中**コンポーネント デザイナーを表示**オプション

コンポーネント デザイナー ウィンドウは次のように表示されます。

![todo:画像_代替_文章](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_17.png)

**形：**コンポーネント デザイナー ウィンドウ

ダブルクリック**OleDbConnection**コンポーネントを [データ] パネルから選択して、oleDbConnection1 オブジェクトをウィンドウに配置します。

![todo:画像_代替_文章](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_18.png)

**形：** oleDbConnection1 オブジェクト

では、データベースに接続します。を使用して簡単に行うことができます**サーバー エクスプローラー**Visual Studio.NET 2005で。選択するだけです**データの接続**の**サーバー エクスプローラー**そして右クリック。目の前にコンテキスト メニューが表示されます。選択する**接続を追加...**次の図に示すように、メニューからオプションを選択します。

![todo:画像_代替_文章](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_19.png)

**形：**選択中**接続を追加...**メニューからのオプション


選択後**接続を追加...**メニューからのオプション、**接続を追加**ダイアログが開き、**ブラウズ**以下に示すように、データベースファイルを選択します。

![todo:画像_代替_文章](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_20.png)

**形：**データベースファイルの選択

接続をテストできます。

![todo:画像_代替_文章](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_21.png)

**形：**接続のテスト

接続を参照して、テーブルとそのフィールドを確認できます。

![todo:画像_代替_文章](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_22.png)

**形：**接続のテーブルとそのフィールドを確認する

今、あなたが選択した場合**oleDbConnection1**のオブジェクト**コンポーネント デザイナー**ウィンドウで、作成したばかりの既存の接続に関連する接続文字列を選択できます。これは、**oleDbConnection1**プロパティウィンドウのオブジェクト。

![todo:画像_代替_文章](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_23.png)

**形：**オブジェクトの接続文字列の選択

最後に、オブジェクトの修飾子が次のように変更されます**保護された**アクセシビリティを向上させるために。

![todo:画像_代替_文章](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_24.png)

**形：**オブジェクトの修飾子の設定

##### **手順 4: データ アダプター オブジェクトの構成**

今、追加します**OleDbDataAdapter**コンポーネントをツールボックスの [データ] パネルから選択して構成します。ダブルクリック**OleDbDataAdapter**ツールボックスの [データ] パネルで、構成ウィザードが開始され、図に示すように既存の接続が選択されます。

![todo:画像_代替_文章](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_25.png)

**形：**データ アダプタ構成ウィザード

クリック後**次**ボタンをクリックします。**クエリビルダー**追加するには**製品**テーブルで、[すべての列] を選択し、**わかった**ボタン。

![todo:画像_代替_文章](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_26.png)

**形：**製品テーブルの追加

![todo:画像_代替_文章](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_27.png)

**形：**クエリビルダー

今すぐクリック**終了**ボタンをクリックしてウィザードを終了します。

![todo:画像_代替_文章](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_28.png)

**形：**ウィザードの終了

ウィザードを構成すると、以下に示すように、oleDbDataAdapter1 が自動的にウィンドウに追加されます。また、その修飾子をに設定することもできます**保護された**.

![todo:画像_代替_文章](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_29.png)

**形：**デザイナー ウィンドウで OleDbDataAdapter オブジェクトを取得する

##### **ステップ 5: DataSet の生成**

データベース接続とデータ アダプター オブジェクトを作成しましたが、データベースに接続した後にデータを保存できるものが必要です。あ**データセット**オブジェクトはデータを正確に保存でき、VS.NET 2005 IDE を使用して簡単に生成することもできます。そのためには、**oleDbDataAdaper1**そして右クリック。いくつかのオプションを含むコンテキスト メニューがポップアップ表示されます。選択する**生む** **データセット...**下の図に示すように、メニューからオプションを選択します。

![todo:画像_代替_文章](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_30.png)

**形：**選択中**生む** **データセット...**メニューからのオプション

選択後**生む** **データセット...**メニューからのオプション、**DataSet の生成**ダイアログが開きます。このダイアログを使用して、新しい名前を選択できます**データセット**作成するオブジェクトと追加するテーブル**データセット**.小切手**このデータセットをデザイナーに追加します**オプションをクリックして**わかった**下図のようにボタンを押します。

![todo:画像_代替_文章](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_31.png)

**形：**クリックする**わかった**生成するボタン**データセット**

今、あなたは見ることができます**データセット11**以下の図に示すように、デザイナにオブジェクトが追加されました。オブジェクト修飾子を**保護された**.

![todo:画像_代替_文章](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_32.png)

**形：** **データセット**生成され、デザイナー ウィンドウに追加されます

.cs ファイル関連の接続、データ アダプター、データセット オブジェクトで、特定のコードが自動的に生成されます。

![todo:画像_代替_文章](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_33.png)

**形：**生成コード

##### **ステップ 6: ワークシート デザイナーの使用**

さぁ、秘密を解き明かしましょう。コントロールを選択して右クリックします。コンテキスト メニューが開きます。下の図に示すように、メニューからワークシート デザイナ... オプションを選択します。

![todo:画像_代替_文章](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_34.png)

**形：**選択中**ワークシート デザイナー...**メニューからのオプション

その後**ワークシート コレクション エディター**ダイアログ（とも呼ばれます**ワークシート デザイナー** が開かれると、バインドするように構成できるいくつかのプロパティが表示されます。**シート1**データベース内の任意のテーブルで。選びましょう**情報元**財産。書く**データセット11**その中に (前の手順で生成してデザイナー ウィンドウに追加したもの)。次に、をクリックします**データメンバー**財産。書く**製品**以下の図に示すように、ここでテーブル名として：

![todo:画像_代替_文章](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_35.png)

**形：**設定**情報元**と**データメンバー**プロパティ

これで、構成できます**BindColumns**財産。それをクリックした後、バインディング列を追加して、**キャプション** , **データフィールド**(それは**製品**テーブル フィールド)、およびその他のプロパティ。を設定できます。**自動作成**に**真実**適用する**検証**を設定します。**番号タイプ**あなたの条件のための異なった分野の。

![todo:画像_代替_文章](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_36.png)

**形：**クリックする**BindColumns**財産

![todo:画像_代替_文章](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_37.png)

**形：** **BindColumn コレクション エディター**ダイアログ

##### **ステップ 7: Web ページのコード行を追加する**

私たちは使用しました**ワークシート デザイナー**簡単で、あとは数行のコードを追加するだけです

まず、追加します**OnInit**初期化するイベント関連コード**InitializeComponent**接続、コマンド、dataadapter、およびデータセット オブジェクトを初期化および作成するメソッド。これらのコード行は、自動生成されたコードでは追加されないため、手動で追加する必要があります。

![todo:画像_代替_文章](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_38.png)

**形：**いくつかのコードを追加する1

![todo:画像_代替_文章](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_39.png)

**形：**いくつかのコードを追加する2

次に、いくつかのコードを**Page_Load**塗りつぶしのイベントハンドラ**データセット11**データベースからのデータを持つオブジェクト (使用**oleDbDataAdapter1** ) およびバインディング**グリッドウェブ**で制御**データセット11**それを呼び出すことによって**データバインド**方法。

{{% alert color="primary" %}}   {{% /alert %}}

##### **例：**

**C#**

{{< highlight "csharp" >}}

 //Implementing Page_Load event handler

protected void Page_Load(object sender, EventArgs e)

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

Protected Sub Page_Load(ByVal sender As Object, ByVal e As System.EventArgs) Handles Me.Load

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

追加されたコードを確認することもできます**Page_Load**以下の図に示すイベント ハンドラ:

![todo:画像_代替_文章](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_40.png)

**形：**に追加されたコード**Page_Load**イベントハンドラ

ここまでで、非常に便利なデータベース アプリケーションを構築できました。ただし、このアプリケーションでは、テーブルのデータを表示することしかできません。でデータを編集できますが、**グリッドウェブ**制御しますが、ブラウザ ウィンドウを閉じてデータベースを開くとき。何も変わっていないことがわかります。つまり、行った変更はデータベースに保存されません。だから、あなたがしなければならないことがあります。

次に、アプリケーションにコードを追加して、**グリッドウェブ**その変更を実際のデータベースに保存することがあります。開けましょう**プロパティ**ペインと選択**保存コマンド**のイベント**グリッドウェブ**そのイベントのリストから制御します。をダブルクリックすると**保存コマンド**イベント VS.NET 2005 IDE が作成します**GridWeb1_SaveCommand**あなたのためのイベントハンドラー。に含まれる変更されたデータでデータベースを更新するために、このイベント ハンドラーにいくつかのコードを追加します。**データセット** （ワークシートにバインド）使用**oleDbDataAdapter1**.

##### **例：**

**C#**

{{< highlight "csharp" >}}

 //Implementing the event handler for SaveCommand event

protected void GridWeb1_SaveCommand(object sender, EventArgs e)

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

Protected Sub GridWeb1_SaveCommand(ByVal sender As Object, ByVal e As System.EventArgs)

  Handles GridWeb1.SaveCommand

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

追加されたコードを確認することもできます**GridWeb1_SaveCommand**以下の図に示すイベント ハンドラ:

![todo:画像_代替_文章](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_41.png)

**形：**に追加されたコード**GridWeb1_SaveCommand**イベントハンドラ

ここで、変更をデータベースに保存する場合は、**セーブ**のボタン**グリッドウェブ**、彼らは間違いなく救われるでしょう。

##### **ステップ 8: アプリケーションを実行する**

最後に、次のいずれかを押すことで、アプリケーションをコンパイルして実行できます**Ctrl+F5**またはクリック**始める**ボタン。デバッグ ダイアログで、適切なデバッグ オプションを指定し、**わかった**下図のようにボタンを押します。

![todo:画像_代替_文章](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_42.png)

**形：**実行中のアプリケーション

コンパイル後、**デフォルト.aspx**以下に示すように、Web アプリケーションのページが新しいブラウザ ウィンドウで開かれ、データベースからロードされたすべてのデータを確認できます。

![todo:画像_代替_文章](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_43.png)

**形：**ロードされたデータ**グリッドウェブ**データベースからの制御

データが読み込まれるとき**グリッドウェブ**コントロールを使用すると、Aspose.Cells.GridWeb がデータの暗黙的なコントロールをユーザーに提供するように感じるでしょう。どのようなデータ操作機能が提供されているかを確認しましょう**グリッドウェブ**そのユーザーに。

##### **データ検証**

Aspose.Cells.GridWeb は、データベースで定義されたデータ型に従って、バインドされたすべての列に対して適切な検証規則を自動的に作成します。下の図に示すように、セルの上にマウス ポインターを置くと、セルの検証タイプを確認できます。

![todo:画像_代替_文章](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_44.png)

**形：**セルの検証タイプの確認

上の図では、選択したセルに含まれていることがわかります**\<INT>**つまり、ユーザーは整数値のみを入力できます。そうしないと、検証エラーが発生します。さらに、**\<必須>**の値が**製品番号**ユーザーが提出する必要があります。

##### **行の削除**

行を削除するには、まず行 (または行の任意のセル) を選択し、**行を削除**以下に示すように、右クリックメニューからのオプション：

![todo:画像_代替_文章](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_45.png)

**形：**選択中**行を削除**メニューからのオプション

選択後**行を削除**メニューから、行が**グリッドウェブ**.今すぐクリック**セーブ**のボタン**グリッドウェブ**元のデータベース テーブルのそのレコードを削除します。

![todo:画像_代替_文章](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_46.png)

**形：**グリッドデータ（行削除後）

##### **行の編集**

セルまたは行のデータを編集してから、**セーブ**ボタンをクリックして変更を保存します。

![todo:画像_代替_文章](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_47.png)

**形：**グリッドデータ (レコード 1 の編集)

![todo:画像_代替_文章](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_48.png)

**形：**グリッドデータ (編集レコード 2)

##### **行の追加**

行を追加するには、**行を追加する**以下に示すように、右クリックメニューからのオプション：

![todo:画像_代替_文章](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_49.png)

**形：**選択中**行を追加する**メニューからのオプション

選択後、行の最後に新しい行がシートに追加されます**行を追加する**メニューからのオプション。新しく追加された行の左側に、**アスタリスク**行が新しく追加されたことを示します。

![todo:画像_代替_文章](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_50.png)

**形：**グリッドに追加された新しい行

新しい行に値を入力したら、**セーブ**以下に示すように、元のデータベース テーブルの変更を確認するボタン

![todo:画像_代替_文章](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_51.png)

**形：**をクリックして変更をデータベース テーブルに保存する**セーブ**ボタン

{{% alert color="primary" %}}   {{% /alert %}}

##### **結論**

{{% alert color="primary" %}}

**データバインディング**Aspose.Cells.GridWeb の重要な機能です。開発者がワークシートをデータベースにバインドするのは本当に簡単です**ワークシート デザイナー**Aspose.Cells.GridWeb が提供するユーティリティ。 Aspose.Cells.GridWeb は、開発者が強力なグリッド ソリューションを作成する時間と労力を節約するのに非常に役立ちます。

{{% /alert %}}
