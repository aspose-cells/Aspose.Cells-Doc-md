---
title: 许可证
type: docs
weight: 120
url: /zh/net/licensing/
description: Aspose.Cells for .NET 提供不同的购买计划或提供免费试用和为评估使用 C# 中的许可和订阅政策提供 30 天临时许可。
keywords: C# 从磁盘或流应用许可。C# 从磁盘或流设置许可。在 Aspose.Cells for NET 中应用许可。
---

## **如何在 Aspose.Cells 组件中应用许可证**

许可证是一个包含产品名称、许可给多少开发人员、订阅到期日期等详细信息的纯文本 XML 文件。该文件经过数字签名，因此不要修改该文件。即使无意中在文件中添加额外的换行符也会使其无效。如果要避免评估限制，你需要在使用 Aspose.Cells 之前设置许可证。每个应用程序（或进程）只需要设置一次许可证。许可证可以从文件、流或嵌入的资源中加载。

Aspose.Cells 尝试在以下位置找到许可证：

- 显式路径
- 包含 Aspose.Cells.dll 的文件夹
- 包含调用 Aspose.Cells.dll 的程序集的文件夹
- 包含入口程序集的文件夹（你的 .exe）
- 包含调用 Aspose.Cells.dll 的程序集中的嵌入资源

有两种常见方法可以应用许可证，从文件或流，或作为嵌入的资源。

### **如何从磁盘或流中应用许可证**

设置许可证的最简单方法是将许可证文件放在与Aspose.Cells.dll相同的文件夹中，并且只指定文件名而不带路径。

{{< highlight csharp >}}

 //Instantiate an instance of license and set the license file through its path

Aspose.Cells.License license = new Aspose.Cells.License();

license.SetLicense("Aspose.Cells.lic");

{{< /highlight >}}

{{% alert color="primary" %}}

当调用SetLicense方法时，许可证名称应与许可证文件名称相同。例如，您可以将许可证文件名更改为**Aspose.Cells.lic.xml**。然后在您的代码中，您应该将已修改的许可证名称（**Aspose.Cells.lic.xml**）用于SetLicense方法。

{{% /alert %}}

还可以从流中加载许可证。

{{< highlight csharp >}}

 //Instantiate an instance of license and set the license through a stream

Aspose.Cells.License license = new Aspose.Cells.License();

license.SetLicense(myStream);

{{< /highlight >}}

### **如何应用计量许可证**

Aspose.Cells允许开发人员应用计量密钥。这是一种新的许可证机制。新的许可证机制将与现有的许可证方法一起使用。那些希望按照API功能的使用情况计费的客户可以使用计量许可证。有关更多详细信息，请参阅 [计量许可证常见问题解答](https://purchase.aspose.com/faqs/licensing/metered) 部分。  

已引入一个新类 [Metered](https://reference.aspose.com/cells/net/aspose.cells/metered) 来应用计量密钥。以下是演示如何设置计量公钥和私钥的示例代码。

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

### **如何使用嵌入式资源**

另一种巧妙的方式是将许可证与您的应用程序打包在一起，以确保不会丢失，即将其作为嵌入式资源包含到调用Aspose.Cells的其中一个程序集中。要将许可证文件包含为嵌入式资源，请执行以下步骤:

1. 在Visual Studio .NET中，通过从**文件**菜单中选择**添加现有项**，将许可证 (.lic) 文件包含到项目中。
1. 在**解决方案资源管理器**中选择文件，然后在**属性**窗口中将**生成操作**设置为**嵌入的资源**

要访问程序集中的嵌入式许可证（作为嵌入的资源），不需要调用Microsoft .NET Framework的System.Reflection.Assembly类的GetExecutingAssembly和GetManifestResourceStream方法。只需将许可证文件添加为嵌入的资源到您的项目中，并将许可证文件的名称传递给SetLicense方法即可。**Aspose.Cells.License** 类将自动在嵌入的资源中查找许可证文件。请查看以下示例以了解在应用程序中设置许可证（嵌入式）的方法。

{{< highlight csharp >}}

 //Instantiate the License class

Aspose.Cells.License license = new Aspose.Cells.License();

//Pass only the name of the license file embedded in the assembly

license.SetLicense("Aspose.Cells.lic");

{{< /highlight >}}

## **如何在Aspose.Cells网格控件中设置许可证**

在Aspose.Cells网格套件中，许可证可以从文件、流或嵌入的资源加载。Aspose.Cells.GridDesktop / Aspose.Cells.GridWeb 尝试在以下位置查找许可证:

1. 明确路径
1. 包含组件dll的文件夹（包括在Aspose.Cells.GridDesktop或Aspose.Cells.GridWeb中）
1. 包含调用组件dll的程序集的文件夹（包括在Aspose.Cells.GridDesktop或Aspose.Cells.GridWeb中）
1. 包含入口程序集的文件夹（您的 .exe）
1. 包含调用组件dll的程序集中的嵌入式资源（包括在Aspose.Cells.GridDesktop或Aspose.Cells.GridWeb中）

{{% alert color="primary" %}}

如果您使用Aspose.Cells.GridDesktop控件，那么将使用Aspose.Cells.GridDesktop.License类来设置许可证，但如果您使用Aspose.Cells.GridWeb控件，则将使用Aspose.Cells.GridWeb.License类来设置许可证。

{{% /alert %}}

### **如何从磁盘或流中应用许可证**

设置许可证的最简单方法是将许可证文件放置在与组件的dll文件（包含在Aspose.Cells.GridWeb中）相同的文件夹中，并只指定文件名而不包括路径。

{{< highlight csharp >}}

//Instantiate an instance of license and set the license file through its path

Aspose.Cells.GridWeb.License license = new Aspose.Cells.GridWeb.License();

license.SetLicense("MyLicense.lic");

{{< /highlight >}}

{{% alert color="primary" %}}

当您调用SetLicense方法时，许可证名称应与许可证文件名称相同。例如，您可以将许可证文件名更改为"MyLicense.lic.xml"。然后在代码中，您应该使用修改后的许可证名称（即MyLicense.lic.xml）作为SetLicense方法的参数。

{{% /alert %}}

还可以从流中加载许可证。

{{< highlight csharp >}}

//Instantiate an instance of license and set the license through a stream

Aspose.Cells.GridWeb.License license = new Aspose.Cells.GridWeb.License();

license.SetLicense(myStream);

{{< /highlight >}}

### **如何将许可证作为嵌入资源应用**

另一种将许可证与应用程序捆绑在一起并确保不会丢失的方法是将其作为嵌入资源包含到调用组件dll的程序集之一中（包含在Aspose.Cells.GridDesktop中）. 要将许可证文件作为嵌入资源包含，执行以下步骤：

1. 在Visual Studio .NET中，使用**文件**菜单中的**添加现有项**选项将许可证（.lic）文件包含到项目中。
1. 在“解决方案资源管理器”中选择文件，然后在“属性”窗口中将**生成操作**设置为嵌入资源。
1. 要访问嵌入在程序集中的许可证（作为嵌入资源），不需要调用Microsoft .NET Framework的System.Reflection.Assembly类的GetExecutingAssembly和GetManifestResourceStream方法。相反，将许可证文件作为嵌入资源添加到项目，并将许可证文件的名称传递给SetLicense方法。License类会自动在嵌入资源中找到许可证文件。

请查看下面的示例，以了解如何将许可证作为嵌入资源应用到您的应用程序中。

{{< highlight csharp >}}

 //Instantiate the License class

Aspose.Cells.GridDesktop.License license = new Aspose.Cells.GridDesktop.License();

//Pass only the name of the license file embedded in the assembly

license.SetLicense("Aspose.Total.lic");

{{< /highlight >}}

## **如何在WinForm应用程序的Aspose.Cells.GridDesktop中应用许可证**

建议您在应用程序启动之前放置许可代码，并且仅应用一次。例如，对于Windows C#应用程序，在主方法中放置许可代码。

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

## **在Aspose.Cells.GridWeb中应用许可证的注意事项**

建议您将许可证代码放置在您的Web应用程序的Global.asax.cs文件中（假设此许可证文件放置在" d：\ "驱动器上）。

{{< highlight csharp >}}

 protected void Application_Start(Object sender, EventArgs e)

{

    Aspose.Cells.GridWeb.License lic = new Aspose.Cells.GridWeb.License();

    lic.SetLicense(@"d:\Aspose.Cells.GridWeb.lic.xml");

}

{{< /highlight >}}

从流中加载许可证

{{< highlight csharp >}}

 protected void Application_Start(Object sender, EventArgs e)

{

    Aspose.Cells.GridWeb.License lic = new Aspose.Cells.GridWeb.License();

    lic.SetLicense(myStream);

}

{{< /highlight >}}
