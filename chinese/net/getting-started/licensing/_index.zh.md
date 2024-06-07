---
title: 许可
type: docs
weight: 120
url: /zh/net/licensing/
description: Aspose.Cells for .NET提供不同的购买计划或提供免费试用和提供30天临时许可证，以便在C#中使用许可证和订阅政策进行评估。
keywords: C# 从磁盘或流应用许可证。C# 从磁盘或流设置许可证。在Aspose.Cells for .NET中应用许可证。
---

## **如何在Aspose.Cells组件中应用许可证**

许可证是一个包含产品名称、被许可开发人员数量、订阅到期日期等详细信息的纯文本XML文件。该文件经过数字签名，因此不要修改该文件。即使是无意中向文件中添加了额外的换行符也会使其无效。如果想要避免其评估限制，需要在使用Aspose.Cells之前设置许可证。只需要在应用程序（或进程）中设置一次许可证。许可证可以从文件、流或嵌入资源中加载。

Aspose.Cells试图在以下位置找到许可证:

- 明确路径
- 包含Aspose.Cells.dll的文件夹
- 包含调用Aspose.Cells.dll的程序集的文件夹
- 包含入口程序集（.exe文件）的文件夹
- 包含调用Aspose.Cells.dll的程序集中的嵌入资源

有两种常见的方法来应用许可证，从文件或流中，或作为嵌入资源。

### **如何从磁盘或流应用许可证**

设置许可证最简单的方法是将许可证文件放在与Aspose.Cells.dll相同的文件夹中，并仅指定文件名而不包括其路径。

{{< highlight csharp >}}

 //Instantiate an instance of license and set the license file through its path

Aspose.Cells.License license = new Aspose.Cells.License();

license.SetLicense("Aspose.Cells.lic");

{{< /highlight >}}

{{% alert color="primary" %}}

当调用SetLicense方法时，许可证名称应与许可证文件名相同。例如，您可以将许可证文件名更改为**Aspose.Cells.lic.xml**。然后在代码中，您应该使用修改后的许可证名称（**Aspose.Cells.lic.xml**）来调用SetLicense方法。

{{% /alert %}}

还可以从流加载许可证。

{{< highlight csharp >}}

 //Instantiate an instance of license and set the license through a stream

Aspose.Cells.License license = new Aspose.Cells.License();

license.SetLicense(myStream);

{{< /highlight >}}

### **如何申请按使用量计费的许可**

Aspose.Cells允许开发人员应用按使用量计费的密钥。这是一种新的许可机制。新的许可机制将与现有的许可方法一起使用。那些希望基于API功能的使用量计费的客户可以使用按使用量计费。有关更多详细信息，请参阅[Metered Licensing FAQ](https://purchase.aspose.com/faqs/licensing/metered)章节。  

引入了一个新的[Metered](https://reference.aspose.com/cells/net/aspose.cells/metered)类，用于应用计量密钥。以下是演示如何设置计量公钥和私钥的示例代码。

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

### **如何使用嵌入资源**

还有一个将许可证与您的应用程序捆绑在一起，确保不会丢失的聪明方法是将其作为嵌入资源包含在调用 Aspose.Cells 的一个组件中。要将许可证文件作为嵌入资源包含，请执行以下步骤：

1. 在 Visual Studio .NET 中，通过选择 **文件** 菜单中的 **添加现有项** 将许可证（.lic）文件包括到项目中。
1. 在“解决方案资源管理器”中选择文件，并在“属性”窗口中将 **生成操作** 设置为 **嵌入的资源**。

要访问嵌入在程序集中的许可证（作为嵌入资源），无需调用 Microsoft .NET Framework 的 System.Reflection.Assembly 类的 GetExecutingAssembly 和 GetManifestResourceStream 方法。只需将许可证文件作为嵌入资源添加到项目中，并将许可证文件的名称传递给 SetLicense 方法即可。**Aspose.Cells.License** 类会自动在嵌入资源中查找许可证文件。请查看下面提供的示例，以了解在应用程序中设置许可证（嵌入式）的方法。

{{< highlight csharp >}}

 //Instantiate the License class

Aspose.Cells.License license = new Aspose.Cells.License();

//Pass only the name of the license file embedded in the assembly

license.SetLicense("Aspose.Cells.lic");

{{< /highlight >}}

## **如何在 Aspose.Cells Grid 控件中设置许可证**

在 Aspose.Cells Grid 套件中，许可证可以从文件、流或嵌入资源加载。Aspose.Cells.GridDesktop / Aspose.Cells.GridWeb 会尝试在以下位置查找许可证：

1. 明确的路径
1. 包含组件的 dll（包括在 Aspose.Cells.GridDesktop 或 Aspose.Cells.GridWeb 中）的文件夹
1. 包含调用组件 dll（包括在 Aspose.Cells.GridDesktop 或 Aspose.Cells.GridWeb 中）的程序集的文件夹
1. 包含 entry 程序集的文件夹（你的 .exe）
1. 包含调用组件 dll（包括在 Aspose.Cells.GridDesktop 或 Aspose.Cells.GridWeb 中）的程序集中的嵌入资源

{{% alert color="primary" %}}

如果正在使用 Aspose.Cells.GridDesktop 控件，则许可证类将用作 Aspose.Cells.GridDesktop.License；如果使用的是 Aspose.Cells.GridWeb 控件，则将使用 Aspose.Cells.GridWeb.License 类来设置许可证。

{{% /alert %}}

### **如何从磁盘或流应用许可证**

设置许可证最简单的方法是将许可证文件放在与该组件的 dll 文件相同的文件夹中（包括在 Aspose.Cells.GridWeb 中），并且只指定文件名，不包含路径。

{{< highlight csharp >}}

//Instantiate an instance of license and set the license file through its path

Aspose.Cells.GridWeb.License license = new Aspose.Cells.GridWeb.License();

license.SetLicense("MyLicense.lic");

{{< /highlight >}}

{{% alert color="primary" %}}

调用 SetLicense 方法时，许可证文件名应与您的许可证文件名相同。例如，您可以将许可证文件名更改为"MyLicense.lic.xml"。然后在代码中，应使用修改后的许可证名（即 MyLicense.lic.xml）用于 SetLicense 方法。

{{% /alert %}}

还可以从流加载许可证。

{{< highlight csharp >}}

//Instantiate an instance of license and set the license through a stream

Aspose.Cells.GridWeb.License license = new Aspose.Cells.GridWeb.License();

license.SetLicense(myStream);

{{< /highlight >}}

### **如何将许可文件作为嵌入资源应用**

还有一个将许可证与您的应用程序捆绑在一起，确保不会丢失的聪明方法是将其作为嵌入资源包含在调用组件 dll（包括在 Aspose.Cells.GridDesktop）的一个程序集中。要将许可证文件作为嵌入资源包含，请执行以下步骤：

1. 在 Visual Studio .NET 中，使用 **文件** 菜单中的 **添加现有项** 选项将许可证（.lic）文件包括到项目中。
1. 在“解决方案资源管理器”中选择文件，并在“属性”窗口中将生成操作设置为嵌入的资源。
要访问嵌入在程序集中的许可证（作为嵌入资源），无需调用微软 .NET Framework 的 System.Reflection.Assembly 类的 GetExecutingAssembly 和 GetManifestResourceStream 方法。相反，在项目中添加许可证文件作为嵌入资源，并将许可证文件的名称传递给 SetLicense 方法即可。License 类会自动在嵌入资源中找到许可证文件。

请查看下面提供的示例，以了解将许可证作为嵌入资源应用到您的应用程序的方法。

{{< highlight csharp >}}

 //Instantiate the License class

Aspose.Cells.GridDesktop.License license = new Aspose.Cells.GridDesktop.License();

//Pass only the name of the license file embedded in the assembly

license.SetLicense("Aspose.Total.lic");

{{< /highlight >}}

## **如何在 Aspose.Cells.GridDesktop 中为 WinForm 应用程序应用许可证**

建议在应用程序启动之前放置您的许可代码，并且仅应用一次。例如对于 C# 窗体应用程序，将许可代码放置在 Main 方法中。

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

## **关于在 Aspose.Cells.GridWeb 中应用许可证的注意事项**

建议将许可证代码放在 Web 应用程序的 Global.asax.cs 文件中（假定此许可证文件放在 "d:\" 驱动器上）。

{{< highlight csharp >}}

 protected void Application_Start(Object sender, EventArgs e)

{

    Aspose.Cells.GridWeb.License lic = new Aspose.Cells.GridWeb.License();

    lic.SetLicense(@"d:\Aspose.Cells.GridWeb.lic.xml");

}

{{< /highlight >}}

从流加载许可证

{{< highlight csharp >}}

 protected void Application_Start(Object sender, EventArgs e)

{

    Aspose.Cells.GridWeb.License lic = new Aspose.Cells.GridWeb.License();

    lic.SetLicense(myStream);

}

{{< /highlight >}}
