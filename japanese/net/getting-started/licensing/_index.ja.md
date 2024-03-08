---
title: Licensing
type: docs
weight: 120
url: /ja/net/licensing/
description: Aspose.Cells for .NET では、さまざまな購入プランが提供されるか、Licensing と C# のサブスクリプション ポリシーを使用した評価用の無料トライアルと 30 日間の一時ライセンスが提供されます。
keywords: C# Apply License from Disk or Stream. C# Set License from Disk or Stream. Apply License in Aspose.Cells for NET.
---
##  **Aspose.Cells コンポーネントにライセンスを適用する方法**

ライセンスは、製品名、ライセンスが付与されている開発者の数、サブスクリプションの有効期限などの詳細が含まれるプレーン テキストの XML ファイルです。ファイルはデジタル署名されているため、ファイルを変更しないでください。ファイルに誤って余分な改行を追加した場合でも、ファイルは無効になります。評価制限を回避したい場合は、Aspose.Cells を利用する前にライセンスを設定する必要があります。ライセンスを設定する必要があるのは、アプリケーション (またはプロセス) ごとに 1 回だけです。ライセンスは、ファイル、ストリーム、または埋め込みリソースからロードできます。

Aspose.Cells は、次の場所でライセンスを検索しようとします。

- 明示的なパス
- Aspose.Cells.dllが含まれるフォルダー
- Aspose.Cells.dll を呼び出したアセンブリを含むフォルダー
- エントリ アセンブリ (.exe) が含まれるフォルダー
- Aspose.Cells.dll を呼び出すアセンブリ内の埋め込みリソース

ライセンスを適用するには、ファイルまたはストリームから、または埋め込みリソースとして適用する 2 つの一般的な方法があります。

###  **ディスクまたはストリームからライセンスを適用する方法**

ライセンスを設定する最も簡単な方法は、ライセンス ファイルを Aspose.Cells.dll と同じフォルダーに置き、パスを指定せずにファイル名だけを指定することです。

{{< highlight "csharp" >}}

 //Instantiate an instance of license and set the license file through its path

Aspose.Cells.License license = new Aspose.Cells.License();

license.SetLicense("Aspose.Cells.lic");

{{< /highlight >}}

{{% alert color="primary" %}}

SetLicense メソッドを呼び出すときは、ライセンス名がライセンス ファイル名と同じである必要があります。たとえば、ライセンス ファイル名を *Aspose.Cells.lic.xml** に変更できます。次に、コード内で SetLicense メソッドに変更したライセンス名 (**Aspose.Cells.lic.xml**) を使用する必要があります。

{{% /alert %}}

ストリームからライセンスをロードすることもできます。

{{< highlight "csharp" >}}

 //Instantiate an instance of license and set the license through a stream

Aspose.Cells.License license = new Aspose.Cells.License();

license.SetLicense(myStream);

{{< /highlight >}}

###  **従量制課金ライセンスを適用する方法**

Aspose.Cells を使用すると、開発者は従量制キーを適用できます。これは新しいライセンスメカニズムです。新しいライセンス メカニズムは、既存のライセンス方式と併用されます。 API 機能の使用量に基づいて請求されることを希望する顧客は、従量制ライセンスを使用できます。詳細については、を参照してください。[従量制 Licensing よくある質問](https://purchase.aspose.com/faqs/licensing/metered)セクション。

新しいクラス[従量制](https://reference.aspose.com/cells/net/aspose.cells/metered)従量制キーを適用するために導入されました。以下は、従量制の公開キーと秘密キーを設定する方法を示すサンプル コードです。

{{< highlight "csharp" >}}

 //Set metered public and private keys

Metered metered = new Metered();

//Access the setMeteredKey property and pass public and private keys as parameters

metered.SetMeteredKey("*************", "*************");

//Instantiate a new Workbook

Workbook workbook = new Workbook();

//Check if the license is set

Console.WriteLine(workbook.IsLicensed);

//Get the Consumption quantity

decimal amountBefore = Metered.GetConsumptionQuantity();

Console.WriteLine(amountBefore);

Workbook workbook2 = new Workbook("e:\\test2\\Book1.xlsx");

workbook2.Save("e:\\test2\\out1.xlsx");

//Since uploading data is already running on another thread, so you might need to wait for some time (optional)

System.Threading.Thread.Sleep(10000);

//Get the Consumption quantity again which should be greater a bit

decimal amountAfter = Metered.GetConsumptionQuantity();

Console.WriteLine(amountAfter);

{{< /highlight >}}

###  **埋め込みリソースの使用方法**

ライセンスをアプリケーションにパッケージ化し、ライセンスが失われないようにするもう 1 つの優れた方法は、Aspose.Cells を呼び出すアセンブリの 1 つに埋め込みリソースとしてライセンスを含めることです。ライセンス ファイルを埋め込みリソースとして含めるには、次の手順を実行します。 :

1.  Visual Studio .NET で、ライセンス (.lic) ファイルを選択してプロジェクトに含めます。**既存のアイテムを追加**から**ファイル**メニュー。
1. ソリューション エクスプローラーでファイルを選択し、設定します。**ビルドアクション**に**埋め込みリソース**プロパティウィンドウで

アセンブリに埋め込まれたライセンス (埋め込みリソースとして) にアクセスするには、Microsoft .NET フレームワークの System.Reflection.Assembly クラスの GetExecutingAssembly メソッドと GetManifestResourceStream メソッドを呼び出す必要はありません。必要なのは、ライセンス ファイルを埋め込みリソースとしてプロジェクトに追加し、ライセンス ファイルの名前を SetLicense メソッドに渡すことだけです。の**Aspose.Cells.License**クラスは、埋め込みリソース内のライセンス ファイルを自動的に検索します。アプリケーションにライセンス (埋め込み) を設定するこの方法を理解するには、以下の例を参照してください。

{{< highlight "csharp" >}}

 //Instantiate the License class

Aspose.Cells.License license = new Aspose.Cells.License();

//Pass only the name of the license file embedded in the assembly

license.SetLicense("Aspose.Cells.lic");

{{< /highlight >}}

##  **Aspose.Cells グリッド コントロールでライセンスを設定する方法**

Aspose.Cells Grid Suite では、ファイル、ストリーム、または埋め込みリソースからライセンスをロードできます。 Aspose.Cells.GridDesktop / Aspose.Cells.GridWeb は、次の場所でライセンスを検索しようとします。

1. 明示的なパス
1. コンポーネントの DLL が含まれるフォルダー (Aspose.Cells.GridDesktop または Aspose.Cells.GridWeb に含まれます)
1. コンポーネントの dll を呼び出したアセンブリを含むフォルダー (Aspose.Cells.GridDesktop または Aspose.Cells.GridWeb に含まれる)
1. エントリ アセンブリ (.exe) が含まれるフォルダー
1. コンポーネントの dll を呼び出すアセンブリ内の埋め込みリソース (Aspose.Cells.GridDesktop または Aspose.Cells.GridWeb に含まれる)

{{% alert color="primary" %}}

Aspose.Cells.GridDesktop コントロールを使用している場合、ライセンス クラスは Aspose.Cells.GridDesktop.License として使用されますが、Aspose.Cells.GridWeb コントロールを使用している場合は、ライセンスの設定に Aspose.Cells.GridWeb.License クラスが使用されます。

{{% /alert %}}

###  **ディスクまたはストリームからライセンスを適用する方法**

ライセンスを設定する最も簡単な方法は、ライセンス ファイルをコンポーネントの DLL と同じフォルダー (Aspose.Cells.GridWeb に含まれる) に置き、パスを指定せずにファイル名だけを指定することです。

{{< highlight "csharp" >}}

//Instantiate an instance of license and set the license file through its path

Aspose.Cells.GridWeb.License license = new Aspose.Cells.GridWeb.License();

license.SetLicense("MyLicense.lic");

{{< /highlight >}}

{{% alert color="primary" %}}

SetLicense メソッドを呼び出すとき、ライセンス名はライセンス ファイル名と同じである必要があります。たとえば、ライセンス ファイル名を「MyLicense.lic.xml」に変更できます。次に、コード内で SetLicense メソッドに変更したライセンス名 (MyLicense.lic.xml) を使用する必要があります。

{{% /alert %}}

ストリームからライセンスをロードすることもできます。

{{< highlight "csharp" >}}

//Instantiate an instance of license and set the license through a stream

Aspose.Cells.GridWeb.License license = new Aspose.Cells.GridWeb.License();

license.SetLicense(myStream);

{{< /highlight >}}

###  **ライセンスを埋め込みリソースとして適用する方法**

ライセンスをアプリケーションにパッケージ化し、ライセンスが失われないようにするもう 1 つの優れた方法は、コンポーネントの DLL (Aspose.Cells.GridDesktop に含まれる) を呼び出すアセンブリの 1 つに埋め込みリソースとしてライセンスを含めることです。ライセンス ファイルを埋め込みリソースとして含めるには、次の手順を実行します。

1.  Visual Studio .NET で、ライセンス (.lic) ファイルをプロジェクトに含めます。**既存のアイテムを追加**のオプション**ファイル**メニュー。
1. ソリューション エクスプローラーでファイルを選択し、プロパティ ウィンドウでビルド アクションを埋め込みリソースに設定します。
1. アセンブリに埋め込まれたライセンス (埋め込みリソースとして) にアクセスするには、Microsoft .NET フレームワークの System.Reflection.Assembly クラスの GetExecutingAssembly メソッドと GetManifestResourceStream メソッドを呼び出す必要はありません。代わりに、ライセンス ファイルを埋め込みリソースとしてプロジェクトを作成し、ライセンス ファイルの名前を SetLicense メソッドに渡します。 License クラスは、埋め込みリソース内のライセンス ファイルを自動的に検索します。

ライセンスを埋め込みリソースとしてアプリケーションに適用するこの方法を理解するには、以下の例を参照してください。

{{< highlight "csharp" >}}

 //Instantiate the License class

Aspose.Cells.GridDesktop.License license = new Aspose.Cells.GridDesktop.License();

//Pass only the name of the license file embedded in the assembly

license.SetLicense("Aspose.Total.lic");

{{< /highlight >}}

##  **WinForm アプリケーションの Aspose.Cells.GridDesktop でライセンスを適用する方法**

アプリケーションを開始する前にライセンス コードを入力し、適用するのは 1 回だけにすることをお勧めします。たとえば、Windows C# アプリケーションの場合、ライセンス コードを Main メソッドに置きます。

{{< highlight "csharp" >}}

public class Form1 : System.Windows.Forms.Form

{

private Aspose.Cells.GridDesktop.GridDesktop gridDesktop1;

/// <summary>

/// Required designer variable.

/// </summary>

private System.ComponentModel.Container components = null;

public Form1()

{

//

// Required for Windows Form Designer support

//

InitializeComponent();

//

// TODO: Add any constructor code after InitializeComponent call

//

}

/// The main entry point for the application.

/// </summary>

.

.

.

.

[STAThread]

static void Main()

{

Aspose.Cells.GridDesktop.License lic = new Aspose.Cells.GridDesktop.License();

//Use this line if you are using an explicit path for the license file.

lic.SetLicense(@"C:\MyLicense.lic");

//Or use the line below if you are using the license file as an embedded resource.

//lic.SetLicense("MyLicense.lic");

Application.Run(new Form1());

}

private void Form1_Load(object sender, System.EventArgs e)

{

Aspose.Cells.GridDesktop.Worksheet sheet = this.gridDesktop1.Worksheets.Add("MySheet");

sheet.Cells["A1"].SetCellValue("Hello");

gridDesktop1.ActiveSheetIndex = 1;

}

}

{{< /highlight >}}

##  **Aspose.Cells.GridWebでライセンスを適用する場合の注意事項**

ライセンス コードを Web アプリケーションの Global.asax.cs に配置することをお勧めします (このライセンス ファイルは「 d:\ 」ドライブに配置されているものとします)。

{{< highlight "csharp" >}}

 protected void Application_Start(Object sender, EventArgs e)

{

    Aspose.Cells.GridWeb.License lic = new Aspose.Cells.GridWeb.License();

    lic.SetLicense(@"d:\Aspose.Cells.GridWeb.lic.xml");

}

{{< /highlight >}}

ストリームからのライセンスのロード

{{< highlight "csharp" >}}

 protected void Application_Start(Object sender, EventArgs e)

{

    Aspose.Cells.GridWeb.License lic = new Aspose.Cells.GridWeb.License();

    lic.SetLicense(myStream);

}

{{< /highlight >}}
