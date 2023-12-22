---
title: Licensing
type: docs
weight: 120
url: /zh/net/licensing/
description: Aspose.Cells for .NET 提供不同的购买计划，或使用 Licensing 和 C# 中的订阅策略提供免费试用和 30 天临时许可证进行评估。
keywords: Apply License from Disk or Stream. Set License from Disk or Stream. Apply License in Aspose.Cells.
---
{{% alert color="primary" %}}

您可以轻松地从其下载 Aspose.Cells 的评估版本[下载页面](https://www.nuget.org/packages/Aspose.Cells) NuGet 仓库。评估版本提供与组件的许可版本完全相同的功能。此外，当您购买许可证并添加几行代码来应用许可证时，评估版就会获得许可。

{{% /alert %}}

##  **评估版限制**

Aspose.Cells 产品的评估版（未指定许可证）提供完整的产品功能，但仅限于在一个程序中打开 100 个文件以及带有评估水印的额外工作表。

限制如下所示：

- **打开文件的数量** (Aspose.Cells)
运行程序时，您只能使用 Aspose.Cells 库打开 100 个 Excel 文件。如果您的应用程序超过此数量，则会抛出异常。
- **配置文件设置**(Aspose.Cells.GridWeb)
您无法通过将以下代码行添加到配置部分（例如在 web.config 文件中）来重新指定脚本路径。 acw_client是一个包含文件和Aspose.Cells的文件夹。GridWeb使用这个文件夹来管理其内部配置，它有脚本文件、图像文件和其他文件来指定GridWeb的行为并设置其他操作。配置文件用于防止控件使用嵌入式客户端资源（图像、脚本等），这在某些情况/场景中很有用。此外，web.config 文件中的此配置设置仅对控件的许可版本有效。

**XML**

{{< highlight "csharp" >}}

 <appSettings>

<add key="aspose.cells.gridweb.acw_client_path" value="/acw_client/" />

<add key="aspose.cells.gridweb.force_script_path" value="true" />

</appSettings>

{{< /highlight >}}

{{% alert color="primary" %}}

如果您在文件系统网站或 MS Ajax 扩展等中使用 Aspose.Cells.GridWeb 控件，这些设置在某些情况/场景下可能是强制性的。

{{% /alert %}}

此外，带有评估水印的工作表将始终在使用 Aspose.Cells 库生成的 Excel 文件中显示为活动工作表。仅在许可版本中，您可以将活动工作表设置为其他工作表。在输出 PDF 或 Aspose.Cells 的图像文件中，评估水印将粘贴在文档/图像的顶部。您也无法在 GridWeb 控件中隐藏评估版权警告（额外的工作表），它始终会添加（在工作表选项卡的末尾）在控件中。

{{% alert color="primary" %}}

如果您想测试 Aspose.Cells 而没有评估版限制，您还可以请求[30 天临时许可证](https://purchase.aspose.com/temporary-license).

{{% /alert %}}

##  **如何在Aspose.Cells组件中申请License**

该许可证是一个纯文本 XML 文件，其中包含产品名称、许可的开发人员数量、订阅到期日期等详细信息。该文件经过数字签名，因此请勿修改该文件。即使无意中在文件中添加了额外的换行符也会使其失效。如果您想避免其评估限制，则需要在使用 Aspose.Cells 之前设置许可证。每个应用程序（或进程）只需设置一次许可证。许可证可以从文件、流或嵌入式资源加载。

Aspose.Cells 尝试在以下位置查找许可证：

- 显式路径
- 包含Aspose.Cells.dll的文件夹
- 包含名为 Aspose.Cells.dll 的程序集的文件夹
- 包含入口程序集的文件夹（您的 .exe）
- 程序集中名为 Aspose.Cells.dll 的嵌入资源

有两种常见的方法可以从文件或流中应用许可证，或者作为嵌入式资源应用许可证。

###  **如何从磁盘或流应用许可证**

设置许可证的最简单方法是将许可证文件放在与 Aspose.Cells.dll 相同的文件夹中，并仅指定文件名而不指定其路径。

{{< highlight "csharp" >}}

 //Instantiate an instance of license and set the license file through its path

Aspose.Cells.License license = new Aspose.Cells.License();

license.SetLicense("Aspose.Cells.lic");

{{< /highlight >}}

{{% alert color="primary" %}}

调用SetLicense方法时，许可证名称应与您的许可证文件名相同。例如，您可以将许可证文件名更改为*Aspose.Cells.lic.xml**。然后在您的代码中，您应该为 SetLicense 方法使用修改后的许可证名称 (**Aspose.Cells.lic.xml**)。

{{% /alert %}}

还可以从流加载许可证。

{{< highlight "csharp" >}}

 //Instantiate an instance of license and set the license through a stream

Aspose.Cells.License license = new Aspose.Cells.License();

license.SetLicense(myStream);

{{< /highlight >}}

###  **如何申请计量许可证**

Aspose.Cells 允许开发者应用计量密钥。这是一种新的许可机制。新的发牌机制将与现有的发牌方法同时使用。想要根据 API 功能的使用情况进行计费的客户可以使用计量许可。欲了解更多详情，请参阅[计量 Licensing 常见问题解答](https://purchase.aspose.com/faqs/licensing/metered)部分。

新班级[计量](https://reference.aspose.com/cells/net/aspose.cells/metered)已引入应用计量密钥。以下是演示如何设置计量公钥和私钥的示例代码。

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

###  **如何使用嵌入式资源**

将许可证与应用程序打包并确保其不会丢失的另一种巧妙方法是将其作为嵌入式资源包含到调用 Aspose.Cells 的程序集中。要将许可证文件作为嵌入式资源包含，请执行以下步骤:

1. 在 Visual Studio .NET 中，通过选择将许可证 (.lic) 文件包含到项目中**添加现有项目**来自**文件**菜单。
1. 在解决方案资源管理器中选择文件并设置**构建行动**到**嵌入式资源**在属性窗口中

要访问嵌入在程序集中的许可证（作为嵌入资源），不需要调用 Microsoft .NET Framework 的 System.Reflection.Assembly 类的 GetExecutingAssembly 和 GetManifestResourceStream 方法。所需要做的就是将许可证文件作为嵌入式资源添加到您的项目中，并将许可证文件的名称传递到 SetLicense 方法中。这**Aspose.Cells.License**class 会自动在嵌入资源中查找许可证文件。请查看下面给出的示例，以了解在应用程序中设置许可证（嵌入）的这种方法。

{{< highlight "csharp" >}}

 //Instantiate the License class

Aspose.Cells.License license = new Aspose.Cells.License();

//Pass only the name of the license file embedded in the assembly

license.SetLicense("Aspose.Cells.lic");

{{< /highlight >}}

##  **如何在Aspose.Cells网格控件中设置许可证**

在 Aspose.Cells Grid Suite 中，可以从文件、流或嵌入式资源加载许可证。 Aspose.Cells.GridDesktop / Aspose.Cells.GridWeb 尝试在以下位置查找许可证：

1. 显式路径
1. 包含组件 dll 的文件夹（包含在 Aspose.Cells.GridDesktop 或 Aspose.Cells.GridWeb 中）
1. 包含调用组件 dll 的程序集的文件夹（包含在 Aspose.Cells.GridDesktop 或 Aspose.Cells.GridWeb 中）
1. 包含入口程序集的文件夹（您的 .exe）
1. 程序集中调用组件 dll 的嵌入资源（包含在 Aspose.Cells.GridDesktop 或 Aspose.Cells.GridWeb 中）

{{% alert color="primary" %}}

如果您使用 Aspose.Cells.GridDesktop 控件，则许可证类将用作 Aspose.Cells.GridDesktop.License，但如果您使用 Aspose.Cells.GridWeb 控件，则将使用 Aspose.Cells.GridWeb.License 类来设置许可证。

{{% /alert %}}

###  **如何从磁盘或流应用许可证**

设置许可证的最简单方法是将许可证文件放在与组件的 dll（包含在 Aspose.Cells.GridWeb 中）相同的文件夹中，并仅指定文件名而不指定其路径。

{{< highlight "csharp" >}}

//Instantiate an instance of license and set the license file through its path

Aspose.Cells.GridWeb.License license = new Aspose.Cells.GridWeb.License();

license.SetLicense("MyLicense.lic");

{{< /highlight >}}

{{% alert color="primary" %}}

当您调用SetLicense方法时，许可证名称应与您的许可证文件名相同。例如，您可以将许可证文件名更改为“MyLicense.lic.xml”。然后在您的代码中，您应该为 SetLicense 方法使用修改后的许可证名称（即 MyLicense.lic.xml）。

{{% /alert %}}

还可以从流加载许可证。

{{< highlight "csharp" >}}

//Instantiate an instance of license and set the license through a stream

Aspose.Cells.GridWeb.License license = new Aspose.Cells.GridWeb.License();

license.SetLicense(myStream);

{{< /highlight >}}

###  **如何将许可证申请为嵌入式资源**

将许可证与应用程序打包并确保其不会丢失的另一种巧妙方法是将其作为嵌入式资源包含到调用组件 dll 的程序集中（包含在 Aspose.Cells.GridDesktop 中）。要将许可证文件包含为嵌入式资源，请执行以下步骤：

1. 在 Visual Studio .NET 中，使用以下命令将许可证 (.lic) 文件包含到项目中**添加现有项目**上的选项**文件**菜单。
1. 在“解决方案资源管理器”中选择该文件，然后在“属性”窗口中将“构建操作”设置为“嵌入资源”。
1. 要访问嵌入在程序集中的许可证（作为嵌入资源），不需要调用 Microsoft .NET Framework 的 System.Reflection.Assembly 类的 GetExecutingAssembly 和 GetManifestResourceStream 方法。而是将许可证文件作为嵌入资源添加到您的应用程序中。项目并将许可证文件的名称传递到 SetLicense 方法中。 License 类自动在嵌入资源中查找许可证文件。

请查看下面给出的示例，以了解将许可证作为嵌入式资源应用到您的应用程序的这种方法。

{{< highlight "csharp" >}}

 //Instantiate the License class

Aspose.Cells.GridDesktop.License license = new Aspose.Cells.GridDesktop.License();

//Pass only the name of the license file embedded in the assembly

license.SetLicense("Aspose.Total.lic");

{{< /highlight >}}

##  **如何在 Aspose.Cells.GridDesktop 中为 WinForm 应用程序申请许可证**

建议您在应用程序启动之前放置许可代码，并且仅应用一次。例如，对于 Windows C# 应用程序，请将许可代码放入 Main 方法中。

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

##  **Aspose.Cells.GridWeb申请License注意事项**

建议将许可代码放在 Web 应用程序的 Global.asax.cs 中（假设该许可文件放在“ d:\ ”驱动器上）：

{{< highlight "csharp" >}}

 protected void Application_Start(Object sender, EventArgs e)

{

    Aspose.Cells.GridWeb.License lic = new Aspose.Cells.GridWeb.License();

    lic.SetLicense(@"d:\Aspose.Cells.GridWeb.lic.xml");

}

{{< /highlight >}}

从流加载许可证

{{< highlight "csharp" >}}

 protected void Application_Start(Object sender, EventArgs e)

{

    Aspose.Cells.GridWeb.License lic = new Aspose.Cells.GridWeb.License();

    lic.SetLicense(myStream);

}

{{< /highlight >}}
