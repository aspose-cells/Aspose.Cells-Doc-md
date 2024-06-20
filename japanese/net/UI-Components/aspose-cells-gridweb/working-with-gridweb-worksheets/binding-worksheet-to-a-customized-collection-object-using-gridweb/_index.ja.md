---
title: GridWebを使用してカスタマイズされたコレクションオブジェクトにワークシートをバインドする
type: docs
weight: 130
url: /ja/net/aspose-cells-gridweb/bind-worksheet-to-a-customized-collection-object-using-gridweb/
keywords: GridWeb,bind
description: この記事では、GridWebでコレクションにワークシートをバインドする方法について紹介します。 
---

{{% alert color="primary" %}} 

.NET Frameworkでは、多くのコレクションクラスが提供されていますが、開発要件を完全に満たさない場合があります。そのため、開発者は**カスタムコレクション**を作成し、GridWebでそのようなカスタムコレクションにワークシートをバインドできます。

{{% /alert %}} 
## **カスタムコレクションとワークシートのバインディング**
この機能を示すために、この記事では、手順を踏んでサンプルアプリケーションの作成方法について説明します。まず、カスタムコレクションを作成し、そのコレクションをワークシートとバインドする方法を説明します。
### **ステップ1: カスタムレコードの作成**
カスタムコレクションを作成する前に、コレクションに格納されるカスタムレコードを保持するクラスを作成します。この記事の目的は、独自のカスタムコレクションを作成し、それをGridWebにバインドする方法を示すことなので、独自のカスタムレコードの作成方法は自由です。

以下の例では、MyCustomRecordクラスを使用して、5つのプライベートフィールドと5つの公開プロパティを持つカスタムレコードを示しています。プロパティの構造は次のとおりです:

- **StringField1**（string）を読み書きするためのStringField1プロパティ。
- **StringField2**（string）を読む専用のReadonlyField2プロパティ。
- DateField1プロパティを使用して**datefield1** (DateTime) を読み書きします。
- IntField1プロパティを使用して**intfield1** (整数) を読み書きします。
- DoubleField1プロパティを使用して**doublefield1** (倍精度浮動小数点数) を読み書きします。

**C#**

{{< highlight csharp >}}

 //Creating a class that will act as record for the custom collection

public class MyCustomRecord

{

    //Private data members

    private string stringfield1;

    private string stringfield2 = "ABC";

    private DateTime datefield1;

    private int intfield1;

    private double doublefield1;

    //Creating a string property

    public string StringField1

    {

        get { return stringfield1; }

        set { stringfield1 = value; }

    }

    //Creating a readonly string property

    public string ReadonlyField2

    {

        get { return stringfield2; }

    }

    //Creating a DateTime property

    public DateTime DateField1

    {

        get { return datefield1; }

        set { datefield1 = value; }

    }

    //Creating an int property

    public int IntField1

    {

        get { return intfield1; }

        set { intfield1 = value; }

    }

    //Creating a double property

    public double DoubleField1

    {

        get { return doublefield1; }

        set { doublefield1 = value; }

    }

}

{{< /highlight >}}
### **ステップ2: カスタムコレクションの作成**
次に、顧客レコードを追加してアクセスするためのカスタムコレクションを作成します。 簡単にするために、この例では読み取り専用インデクサーを含むMyCollectionクラスを使用しています。 このインデクサーを使用すると、コレクションに格納されている任意のカスタムレコードを取得できます。

**C#**

{{< highlight csharp >}}

 //Creating a custom collection

public class MyCollection : CollectionBase

{

    //Leaving the collection constructor empty

    public MyCollection()

    {

    }

    //Creating a readonly property for custom collection. This Item property is used by GridWeb control to

    //determine the collection's type

    public MyCustomRecord this[int index]

    {

        get { return (MyCustomRecord)this.List[index]; }

    }

}

{{< /highlight >}}
### **ステップ3: ワークシートとカスタムコレクションのバインディング**
カスタムコレクションの作成プロセスは完了しました。 今度は、Aspose.Cells.GridWebのワークシートにバインドするためにカスタムコレクションを使用します。 まず、Webフォームを作成し、その中にGridWebコントロールを追加して、いくつかのコードを追加します。

バインディングにカスタムコレクションを使用するには、まずMyCollectionクラスのオブジェクト(上記の手順で作成)を作成します。
次に、MyCollectionオブジェクトにMyCustomRecordオブジェクトを作成して追加します。

{{% alert color="primary" %}} 

MyCollectionクラスにMyCustomRecordオブジェクトをコレクションに追加するためのメソッドがない理由が気になりますか？ 上記のコードをもう一度よく見てみると、MyCollectionクラスがCollectionBaseクラスから継承されています（コレクションにオブジェクトを追加するためのAddメソッドを提供するIListインタフェースを実装したクラスです）。 IListクラスのAddメソッドを使用するために、MyCollectionオブジェクトをIListにアップキャストします。

{{% /alert %}} 

最後に、MyCollectionオブジェクトをワークシートのデータソースとして設定し、ワークシートをコレクションとバインドします。 この時点では、ワークシートのバウンド列に対して検証ルールを作成することもできます。

**C#**

{{< highlight csharp >}}

 //Implementing Page_Load event handler

protected void Page_Load(object sender, EventArgs e)

{

    if (Page.IsPostBack == false && this.GridWeb1.IsPostBack == false)

    {

        //Creating an object of custom collection

        MyCollection list = new MyCollection();

        //Creating an instance of Random class

        System.Random rand = new System.Random();

        //Creating a loop that will run 5 times

        for (int i = 0; i < 5; i++)

        {

            //Creating an object of Custom Record

            MyCustomRecord rec = new MyCustomRecord();

            //Initializing all properties of Custom Record

            rec.DateField1 = DateTime.Now;

            rec.DoubleField1 = rand.NextDouble() * 10;

            rec.IntField1 = rand.Next(20);

            rec.StringField1 = "ABC_" + i;

            //Adding Custom Record to Collection

            ((IList)list).Add(rec);

        }

        //Accessing a desired worksheet

        GridWorksheet sheet = GridWeb1.WorkSheets[0];

        //Setting the Data Source of worksheet

        sheet.DataSource = list;

        //Creating columns automatically

        sheet.CreateAutoGenratedColumns();

        //Setting the validation type of value to DateTime

        sheet.BindColumns[2].Validation.ValidationType = ValidationType.DateTime;

        //Binding worksheet

        sheet.DataBind();

        //Assigning an event handler to InitializeNewBindRow event of the worksheet

        //sheet.InitializeNewBindRow += new InitializeNewBindRowHandler(GridWeb1_InitializeNewBindRow);

    }

}

{{< /highlight >}}
### **ステップ4: ワークシートのInitializeNewBindRowイベントの処理**
上記のコードでは、ワークシートのInitializeNewBindRowにGridWeb1_InitializeNewBindRowイベントハンドラーを割り当てるために使用される追加のコード行があるのに気づいたかもしれません。 このイベントは、ワークシートに新しいバウンド行が追加されるたびにトリガーされます。 このイベントのためにイベントハンドラーを作成したのは、MyCustomRecordオブジェクトのDateField1プロパティのためです。

Aspose.Cells.GridWebは、新しいバウンド行がGridWebコントロールに追加されるたびに**int**および**double**値を自動的に**ゼロ (0)**で初期化します。 日付の場合は、GridWebコントロールがシステムから現在の日付を自動的に追加するようにします。 そのために、InitializeNewBindRowイベントのGridWeb1_InitializeNewBindRowイベントハンドラーを作成しました。

GridWebを使用してバインドオブジェクト引数からMyCustomRecordクラスの特定のインスタンスにアクセスし、そのDateField1プロパティに現在のシステム日付を割り当てます。

**C#**

{{< highlight csharp >}}

 //Creating GridWeb1_InitializeNewBindRow event handler

private void GridWeb1_InitializeNewBindRow(GridWorksheet sender, object bindObject)

{

    //Accessing that custom record object that is newly bound

    MyCustomRecord rec = (MyCustomRecord)bindObject;

    //Initializing the DateTime of a property when a new row gets bound to the database

    rec.DateField1 = DateTime.Now;

}

{{< /highlight >}}
### **ステップ5: アプリケーションの実行**
アプリケーションを**Ctrl+F5**を押すか、VS.NETの**Start**ボタンをクリックして実行します。 Webフォームが新しいブラウザウィンドウで開きます。 

**カスタムコレクションにバインドしたワークシート** 

![todo:image_alt_text](binding-worksheet-to-a-customized-collection-object-using-gridweb_1.png)



GridWebコントロールを右クリックして、レコードを追加したり削除したりします。 例えば、**Add Row**オプションを選択してワークシートに新しいレコードを追加します。 

**メニューからAdd Rowオプションを選択** 

![todo:image_alt_text](binding-worksheet-to-a-customized-collection-object-using-gridweb_2.png)



ワークシートに新しい行が追加されると、セルには現在のシステム日付を含めたデフォルトデータが含まれます。 

**デフォルトデータがある新しい行がワークシートに追加されました** 

![todo:image_alt_text](binding-worksheet-to-a-customized-collection-object-using-gridweb_3.png)



データを変更した後、**保存**または**送信**をクリックして変更内容を保存します。 

**Saveボタンをクリックして変更を保存** 

![todo:image_alt_text](binding-worksheet-to-a-customized-collection-object-using-gridweb_4.png)
## **結論**
{{% alert color="primary" %}} 

この記事では、作成されたカスタムコレクションにワークシートをバインドする方法を示しました。 Aspose.Cells.GridWebを使用すると、開発者はGUIモードまたはコーディングを介してワークシートをデータベースまたはカスタムコレクションにバインドできます。 これにより、開発者はアプリケーションを作成するための幅広いオプションが提供されます。

{{% /alert %}}
