---
title: ライセンス
type: docs
weight: 120
url: /ja/net/licensing/
---
{{% alert color="primary" %}}

から簡単に Aspose.Cells の評価版をダウンロードできます。[ダウンロードページ](https://www.nuget.org/packages/Aspose.Cells) @ NuGet リポジトリ。評価版は、コンポーネントのライセンス版とまったく同じ機能を提供します。さらに、評価版は、ライセンスを購入し、数行のコードを追加してライセンスを適用するだけで、ライセンスが付与されます。

{{% /alert %}}

## **評価版の制限事項**

Aspose.Cells 製品の評価版 (ライセンスが指定されていない) は、すべての製品機能を提供しますが、1 つのプログラムで 100 個のファイルを開くことができ、評価版の透かしが付いた追加のワークシートに制限されています。

制限事項を以下に示します。

- **開いているファイルの数** (Aspose.Cells)
プログラムを実行すると、Aspose.Cells ライブラリを使用して 100 個の Excel ファイルしか開くことができません。アプリケーションがこの数を超えると、例外がスローされます。
- **構成ファイルの設定**(Aspose.Cells.グリッドウェブ)
次のコード行を構成セクション (例: web.config ファイル) に追加して、スクリプト パスを再指定することはできません。 acw_client はファイルを含むフォルダーで、Aspose.Cells.GridWeb はこのフォルダーを使用して内部構成を管理します。スクリプト ファイル、画像ファイル、および GridWeb の動作を指定し、その他の操作を設定するその他のファイルがあります。構成ファイルは、コントロールが埋め込まれたクライアント リソース (画像、スクリプトなど) を使用しないようにするために使用されます。これは、場合によっては便利です。さらに、web.config ファイル内のこの構成設定は、コントロールの LICENSED バージョンでのみ有効になります。

**XML**

{{< highlight "csharp" >}}

 <appSettings>

<add key="aspose.cells.gridweb.acw_client_path" value="/acw_client/" />

<add key="aspose.cells.gridweb.force_script_path" value="true" />

</appSettings>

{{< /highlight >}}

{{% alert color="primary" %}}

これらの設定は、ファイル システム Web サイトまたは MS Ajax 拡張機能などで Aspose.Cells.GridWeb コントロールを使用している場合、場合によっては必須になることがあります。

{{% /alert %}}

さらに、評価透かしを含むワークシートは、Aspose.Cells ライブラリを使用して生成された Excel ファイルで常にアクティブなワークシートとして表示されます。ライセンス版のみ、アクティブなワークシートを他のワークシートに設定できます。 Aspose.Cells による出力 PDF または画像ファイルでは、ドキュメント/画像の上部に評価の透かしが貼り付けられます。GridWeb コントロールでも評価著作権警告 (余分なワークシート) を非表示にすることはできません。常に追加されます。 (ワークシート タブの最後) コントロール内。

{{% alert color="primary" %}}

評価版の制限なしで Aspose.Cells をテストしたい場合は、[30日間の一時ライセンス](https://purchase.aspose.com/temporary-license).

{{% /alert %}}

## **Aspose.Cells コンポーネントでのライセンスの適用**

ライセンスは、製品名、ライセンスが付与されている開発者の数、サブスクリプションの有効期限などの詳細を含むプレーン テキストの XML ファイルです。ファイルはデジタル署名されているため、ファイルを変更しないでください。誤ってファイルに改行を追加しても無効になります。評価制限を回避したい場合は、Aspose.Cells を使用する前にライセンスを設定する必要があります。アプリケーション (またはプロセス) ごとに 1 回だけライセンスを設定する必要があります。ライセンスは、ファイル、ストリーム、または埋め込みリソースからロードできます。

Aspose.Cells は、次の場所でライセンスを見つけようとします。

- 明示的なパス
- Aspose.Cells.dll を含むフォルダー
- Aspose.Cells.dll を呼び出したアセンブリを含むフォルダー
- エントリ アセンブリ (.exe) を含むフォルダー
- Aspose.Cells.dll を呼び出したアセンブリ内の埋め込みリソース

ライセンスを適用するには、ファイルまたはストリームから、または埋め込みリソースとして、2 つの一般的な方法があります。

### **ディスクまたはストリームからのライセンスの適用**

ライセンスを設定する最も簡単な方法は、ライセンス ファイルを Aspose.Cells.dll と同じフォルダーに置き、パスを省略してファイル名だけを指定することです。

{{< highlight "csharp" >}}

 //Instantiate an instance of license and set the license file through its path

Aspose.Cells.License license = new Aspose.Cells.License();

license.SetLicense("Aspose.Cells.lic");

{{< /highlight >}}

{{% alert color="primary" %}}

 SetLicense メソッドを呼び出すとき、ライセンス名はライセンス ファイル名と同じである必要があります。たとえば、ライセンス ファイル名を次のように変更できます。**Aspose.Cells.lic.xml**.次に、コードで、変更されたライセンス名 (**Aspose.Cells.lic.xml**) SetLicense メソッドの場合。

{{% /alert %}}

ストリームからライセンスをロードすることもできます。

{{< highlight "csharp" >}}

 //Instantiate an instance of license and set the license through a stream

Aspose.Cells.License license = new Aspose.Cells.License();

license.SetLicense(myStream);

{{< /highlight >}}

### **従量制ライセンスの適用**

Aspose.Cells を使用すると、開発者は従量制のキーを適用できます。これは、新しいライセンス メカニズムです。新しいライセンス メカニズムは、既存のライセンス方法と共に使用されます。 API 機能の使用量に基づいて課金されることを希望するお客様は、従量制ライセンスを使用できます。詳細については、を参照してください。[従量制ライセンスに関する FAQ](https://purchase.aspose.com/faqs/licensing/metered)セクション。

新しいクラス[従量制](https://reference.aspose.com/cells/net/aspose.cells/metered)従量制キーを適用するために導入されました。以下は、従量制の公開鍵と秘密鍵を設定する方法を示すサンプル コードです。

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

### **埋め込みリソースの使用**

ライセンスをアプリケーションにパッケージ化して紛失しないようにするもう 1 つの優れた方法は、Aspose.Cells を呼び出すアセンブリの 1 つにライセンスを埋め込みリソースとして含めることです。ライセンス ファイルを埋め込みリソースとして含めるには、次の手順を実行します。 :

1.  Visual Studio .NET で、ライセンス (.lic) ファイルを選択してプロジェクトに含めます。**既存のアイテムを追加**から**ファイル**メニュー。
1. ソリューション エクスプローラーでファイルを選択し、設定します。**ビルド アクション**に**埋め込みリソース**プロパティウィンドウで

アセンブリに (埋め込みリソースとして) 埋め込まれたライセンスにアクセスするには、Microsoft .NET フレームワークの System.Reflection.Assembly クラスの GetExecutingAssembly および GetManifestResourceStream メソッドを呼び出す必要はありません。ライセンス ファイルを埋め込みリソースとしてプロジェクトに追加し、ライセンス ファイルの名前を SetLicense メソッドに渡すだけです。の**Aspose.Cells.License**クラスは、埋め込まれたリソースでライセンス ファイルを自動的に見つけます。以下の例を参照して、アプリケーションにライセンス (組み込み) を設定するこの方法を理解してください。

{{< highlight "csharp" >}}

 //Instantiate the License class

Aspose.Cells.License license = new Aspose.Cells.License();

//Pass only the name of the license file embedded in the assembly

license.SetLicense("Aspose.Cells.lic");

{{< /highlight >}}

## **Aspose.Cells グリッド コントロールでのライセンスの設定**

Aspose.Cells Grid Suite では、ファイル、ストリーム、または埋め込みリソースからライセンスをロードできます。 Aspose.Cells.GridDesktop / Aspose.Cells.GridWeb は、次の場所でライセンスを見つけようとします。

1. 明示的なパス
1. コンポーネントの dll を含むフォルダー (Aspose.Cells.GridDesktop または Aspose.Cells.GridWeb に含まれる)
1. コンポーネントの dll を呼び出したアセンブリを含むフォルダー (Aspose.Cells.GridDesktop または Aspose.Cells.GridWeb に含まれる)
1. エントリ アセンブリ (.exe) を含むフォルダー
1. コンポーネントの dll を呼び出したアセンブリ内の埋め込みリソース (Aspose.Cells.GridDesktop または Aspose.Cells.GridWeb に含まれる)

{{% alert color="primary" %}}

Aspose.Cells.GridDesktop コントロールを使用している場合、ライセンス クラスは Aspose.Cells.GridDesktop.License として使用されますが、Aspose.Cells.GridWeb コントロールを使用している場合は、Aspose.Cells.GridWeb.License クラスを使用してライセンスを設定します。

{{% /alert %}}

### **ディスクまたはストリームからのライセンスの適用**

ライセンスを設定する最も簡単な方法は、コンポーネントの dll (Aspose.Cells.GridWeb に含まれる) と同じフォルダーにライセンス ファイルを置き、パスを除いてファイル名だけを指定することです。

{{< highlight "csharp" >}}

//Instantiate an instance of license and set the license file through its path

Aspose.Cells.GridWeb.License license = new Aspose.Cells.GridWeb.License();

license.SetLicense("MyLicense.lic");

{{< /highlight >}}

{{% alert color="primary" %}}

SetLicense メソッドを呼び出すとき、ライセンス名はライセンス ファイル名と同じである必要があります。たとえば、ライセンス ファイル名を「MyLicense.lic.xml」に変更できます。次に、コード内で、SetLicense メソッドに変更されたライセンス名 (つまり、MyLicense.lic.xml) を使用する必要があります。

{{% /alert %}}

ストリームからライセンスをロードすることもできます。

{{< highlight "csharp" >}}

//Instantiate an instance of license and set the license through a stream

Aspose.Cells.GridWeb.License license = new Aspose.Cells.GridWeb.License();

license.SetLicense(myStream);

{{< /highlight >}}

### **組み込みリソースとしてのライセンスの適用**

ライセンスをアプリケーションにパッケージ化して紛失しないようにするもう 1 つの優れた方法は、コンポーネントの dll (Aspose.Cells.GridDesktop に含まれる) を呼び出すアセンブリの 1 つに、ライセンスを埋め込みリソースとして含めることです。ライセンス ファイルを埋め込みリソースとして含めるには、次の手順を実行します。

1.  Visual Studio .NET で、ライセンス (.lic) ファイルをプロジェクトに含めます。**既存のアイテムを追加**上のオプション**ファイル**メニュー。
1. ソリューション エクスプローラーでファイルを選択し、[プロパティ] ウィンドウで [ビルド アクション] を [埋め込みリソース] に設定します。
1. アセンブリに (埋め込みリソースとして) 埋め込まれたライセンスにアクセスするには、Microsoft .NET Framework の System.Reflection.Assembly クラスの GetExecutingAssembly および GetManifestResourceStream メソッドを呼び出す必要はありません。代わりに、ライセンス ファイルを埋め込みリソースとしてプロジェクトを作成し、ライセンス ファイルの名前を SetLicense メソッドに渡します。 License クラスは、埋め込みリソース内のライセンス ファイルを自動的に見つけます。

以下の例を参照して、ライセンスを組み込みリソースとしてアプリケーションに適用するこの方法を理解してください。

{{< highlight "csharp" >}}

 //Instantiate the License class

Aspose.Cells.GridDesktop.License license = new Aspose.Cells.GridDesktop.License();

//Pass only the name of the license file embedded in the assembly

license.SetLicense("Aspose.Total.lic");

{{< /highlight >}}

## **WinForm アプリケーションの Aspose.Cells.GridDesktop でのライセンスの適用**

アプリケーションの開始前にライセンス コードを配置し、一度だけ適用することをお勧めします。たとえば、Windows C# アプリケーションの場合、ライセンス コードを Main メソッドに配置します。

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

## **Aspose.Cells.GridWebでのライセンス申請に関する注意事項**

Web アプリケーションの Global.asax.cs にライセンス コードを配置することをお勧めします (このライセンス ファイルは " d:\ " ドライブに配置されると想定されています)。

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
