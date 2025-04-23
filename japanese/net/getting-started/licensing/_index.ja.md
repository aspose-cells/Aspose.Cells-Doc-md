---
title: ライセンス
type: docs
weight: 120
url: /ja/net/licensing/
description: Aspose.Cells for .NET では、購入用の異なるプランを提供したり、Free Trial や評価用の30日間の仮ライセンスを提供したりすることができます。
keywords: C# でディスクまたはストリームからライセンスを適用する。C# でディスクまたはストリームからライセンスを設定する。 Aspose.Cells for NET でライセンスを適用する。
---

## **Aspose.Cells コンポーネントでライセンスを適用する方法**

ライセンスは、製品名、ライセンスを受け取る開発者数、サブスクリプションの有効期限などの詳細を含むプレーンテキストの XML ファイルです。このファイルはデジタル署名されているため、ファイルを変更しないでください。ファイルに行を誤って追加すると、ファイルが無効になります。Aspose.Cells を利用する前にライセンスを設定する必要があります。アプリケーション（またはプロセス）ごとに一度だけライセンスを設定する必要があります。ライセンスはファイル、ストリーム、または埋め込みリソースから読み込むことができます。

Aspose.Cells は次の場所にライセンスを取得しようとします:

- 明示的なパス
- Aspose.Cells.dll を含むフォルダ
- Aspose.Cells.dll を呼び出したアセンブリを含むフォルダ
- エントリ アセンブリ（.exe ファイル）を含むフォルダ
- Aspose.Cells.dll を呼び出したアセンブリに埋め込まれたリソース

ライセンスを適用する一般的な方法には、ファイルまたはストリームから、または埋め込みリソースとしてロードする方法があります。

### **ディスクまたはストリームからライセンスを適用する方法**

ライセンスを設定する最も簡単な方法は、Aspose.Cells.dll と同じフォルダにライセンス ファイルを置き、そのパスを指定するだけです。

{{< highlight csharp >}}

 //Instantiate an instance of license and set the license file through its path

Aspose.Cells.License license = new Aspose.Cells.License();

license.SetLicense("Aspose.Cells.lic");

{{< /highlight >}}

{{% alert color="primary" %}}

SetLicense メソッドを呼び出すとき、ライセンス名はライセンス ファイル名と同じである必要があります。たとえば、ライセンス ファイル名を**Aspose.Cells.lic.xml**に変更できます。その後、コードで変更したライセンス名(**Aspose.Cells.lic.xml**)を SetLicense メソッドに使用する必要があります。

{{% /alert %}}

ストリームからライセンスをロードすることも可能です。

{{< highlight csharp >}}

 //Instantiate an instance of license and set the license through a stream

Aspose.Cells.License license = new Aspose.Cells.License();

license.SetLicense(myStream);

{{< /highlight >}}

### **メータード ライセンスの適用方法**

Aspose.Cellsでは、開発者がメータードキーを適用することができます。これは新しいライセンスメカニズムです。新しいライセンスメカニズムは、既存のライセンス方法と併用されます。API機能の使用に基づいて請求を受けたい顧客は、メータードライセンスを使用できます。詳細については、[メータードライセンスFAQ](https://purchase.aspose.com/faqs/licensing/metered)セクションを参照してください。  

新しいクラス[Metered](https://reference.aspose.com/cells/net/aspose.cells/metered)が導入され、メータードキーを適用する方法を示すサンプルコードが次に示されています。

{{< highlight csharp >}}

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

### **埋め込みリソースの使用方法**

ライセンスファイルをアプリケーションにパッケージ化し、失われないようにするもう一つの便利な方法は、Aspose.Cellsを呼び出すアセンブリの埋め込みリソースとして含めることです。ライセンスファイルを埋め込みリソースとして含めるには、次の手順を実行します。

1. Visual Studio .NETで、**ファイル**メニューから**既存のアイテムの追加**を選択して、プロジェクトにライセンス（.lic）ファイルを含めます。
1. ソリューションエクスプローラでファイルを選択し、プロパティウィンドウで**ビルドアクション**を**埋め込みリソース**に設定します。

アセンブリに埋め込まれているライセンス（埋め込みリソース）にアクセスするには、Microsoft .NET FrameworkのSystem.Reflection.AssemblyクラスのGetExecutingAssemblyおよびGetManifestResourceStreamメソッドを呼び出す必要はありません。必要なのは、プロジェクトにライセンスファイルを埋め込みリソースとして追加し、そのライセンスファイルの名前をSetLicenseメソッドに渡すだけです。**Aspose.Cells.License**クラスは、埋め込みリソースでライセンスファイルを自動的に見つけます。このライセンス（埋め込み）をアプリケーションに設定する方法を理解するために、以下に示されている例を確認してください。

{{< highlight csharp >}}

 //Instantiate the License class

Aspose.Cells.License license = new Aspose.Cells.License();

//Pass only the name of the license file embedded in the assembly

license.SetLicense("Aspose.Cells.lic");

{{< /highlight >}}

## **Aspose.Cells Gridコントロールでのライセンスの設定方法**

Aspose.Cells Grid Suiteでは、ライセンスをファイル、ストリーム、または埋め込みリソースからロードできます。Aspose.Cells.GridDesktop / Aspose.Cells.GridWebは、ライセンスを次の場所で検索しようとします。

1. 明示的なパス
1. コンポーネントのDLL（Aspose.Cells.GridDesktopまたはAspose.Cells.GridWebに含まれる）が含まれているフォルダ
1. コンポーネントのDLL（Aspose.Cells.GridDesktopまたはAspose.Cells.GridWebに含まれている）を呼び出したアセンブリが含まれているフォルダ
1. エントリアセンブリ（.exe）が含まれているフォルダ
1. コンポーネントのDLL（Aspose.Cells.GridDesktopまたはAspose.Cells.GridWebに含まれる）を呼び出したアセンブリに埋め込まれているリソース

{{% alert color="primary" %}}

Aspose.Cells.GridDesktopコントロールを使用している場合は、ライセンスクラスとしてAspose.Cells.GridDesktop.Licenseが使用されますが、Aspose.Cells.GridWebコントロールを使用している場合は、Aspose.Cells.GridWeb.Licenseクラスが使用されます。

{{% /alert %}}

### **ディスクまたはストリームからライセンスを適用する方法**

ライセンスを設定する最も簡単な方法は、ライセンスファイルをコンポーネントのDLLと同じフォルダに配置し、ファイル名のパスを指定するだけです（Aspose.Cells.GridWebに含まれています）。

{{< highlight csharp >}}

//Instantiate an instance of license and set the license file through its path

Aspose.Cells.GridWeb.License license = new Aspose.Cells.GridWeb.License();

license.SetLicense("MyLicense.lic");

{{< /highlight >}}

{{% alert color="primary" %}}

SetLicenseメソッドを呼び出す際、ライセンス名はライセンスファイル名と同じである必要があります。たとえば、ライセンスファイル名を"MyLicense.lic.xml"に変更することができます。次に、コードでは、修正済みのライセンス名（つまりMyLicense.lic.xml）をSetLicenseメソッドに使用する必要があります。

{{% /alert %}}

ストリームからライセンスをロードすることも可能です。

{{< highlight csharp >}}

//Instantiate an instance of license and set the license through a stream

Aspose.Cells.GridWeb.License license = new Aspose.Cells.GridWeb.License();

license.SetLicense(myStream);

{{< /highlight >}}

### **埋め込みリソースとしてライセンスを適用する方法**

ライセンスをアプリケーションにパッケージ化し、失われないようにするもう一つの便利な方法は、コンポーネントのDLL（Aspose.Cells.GridDesktopに含まれる）を呼び出すアセンブリの埋め込みリソースとして含めることです。ライセンスファイルを埋め込みリソースとして含めるには、次の手順を実行します。

1. Visual Studio .NETで、**ファイル**メニューで**既存のアイテムの追加**オプションを使用して、プロジェクトにライセンス（.lic）ファイルを含めます。
1. ソリューションエクスプローラでファイルを選択し、プロパティウィンドウでビルドアクションを埋め込みリソースに設定します。
アセンブリ（埋め込みリソースとして）に埋め込まれたライセンスにアクセスするには、Microsoft .NET FrameworkのSystem.Reflection.AssemblyクラスのGetExecutingAssemblyおよびGetManifestResourceStreamメソッドを呼び出す必要はありません。代わりに、プロジェクトにライセンスファイルを埋め込みリソースとして追加し、そのライセンスファイルの名前をSetLicenseメソッドに渡すだけです。ライセンスクラスは、埋め込みリソースでライセンスファイルを自動的に見つけます。

このアプリケーションに埋め込みリソースとしてライセンスを適用する方法について理解するために、以下に示されている例を確認してください。

{{< highlight csharp >}}

 //Instantiate the License class

Aspose.Cells.GridDesktop.License license = new Aspose.Cells.GridDesktop.License();

//Pass only the name of the license file embedded in the assembly

license.SetLicense("Aspose.Total.lic");

{{< /highlight >}}

## **WinFormアプリケーションでAspose.Cells.GridDesktopのライセンスを適用する方法**

アプリケーションが開始する前にライセンスコードを配置し、一度だけ適用することをお勧めします。たとえば、Windows C#アプリケーションの場合は、Mainメソッドにライセンスコードを配置します。

{{< highlight csharp >}}

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

## **Aspose.Cells.GridWebでのライセンスの適用に関する注意事項**

WebアプリケーションのGlobal.asax.csにライセンスコードを配置することをお勧めします（このライセンスファイルは"d:\"ドライブに配置されたと仮定されます）。

{{< highlight csharp >}}

 protected void Application_Start(Object sender, EventArgs e)

{

    Aspose.Cells.GridWeb.License lic = new Aspose.Cells.GridWeb.License();

    lic.SetLicense(@"d:\Aspose.Cells.GridWeb.lic.xml");

}

{{< /highlight >}}

ストリームからライセンスを読み込む

{{< highlight csharp >}}

 protected void Application_Start(Object sender, EventArgs e)

{

    Aspose.Cells.GridWeb.License lic = new Aspose.Cells.GridWeb.License();

    lic.SetLicense(myStream);

}

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
