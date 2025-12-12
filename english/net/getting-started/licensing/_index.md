---
title: Licensing
type: docs
weight: 120
url: /net/licensing/
description: Aspose.Cells for .NET provides different plans for purchase or offers a Free Trial and a 30-day Temporary License for evaluation using Licensing and Subscription policies in C#.
keywords: C# Apply License from Disk or Stream. C# Set License from Disk or Stream. Apply License in Aspose.Cells for NET.
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **How to Apply a License in Aspose.Cells Component**

The license is a plain text XML file that contains details such as the product name, number of developers it is licensed to, subscription expiry date and so on. The file is digitally signed, so don't modify the file. Even inadvertent addition of an extra line break into the file will invalidate it.You need to set a license before utilizing Aspose.Cells if you want to avoid its evaluation limitation. It is only required to set a license once per application (or process). The license can be loaded from a file, stream or an embedded resource.

Aspose.Cells tries to find the license in the following locations:

- Explicit path
- The folder that contains Aspose.Cells.dll
- The folder that contains the assembly that called Aspose.Cells.dll
- The folder that contains the entry assembly (your .exe)
- An embedded resource in the assembly that called Aspose.Cells.dll

There are two common methods to apply a license, from file or stream, or as an embedded resource.

### **How to Apply a License from Disk or Stream**

The easiest way to set a license is to put the license file in the same folder as Aspose.Cells.dll and specify just the file name without its path.

{{< highlight csharp >}}

 //Instantiate an instance of license and set the license file through its path

Aspose.Cells.License license = new Aspose.Cells.License();

license.SetLicense("Aspose.Cells.lic");

{{< /highlight >}}

{{% alert color="primary" %}}

When you call the SetLicense method, the license name should be same as that of your license file name. For example, you may change the license file name to **Aspose.Cells.lic.xml**. Then in your code, you should use the modified license name (**Aspose.Cells.lic.xml**) for the SetLicense method.

{{% /alert %}}

It is also possible to load a license from a stream.

{{< highlight csharp >}}

 //Instantiate an instance of license and set the license through a stream

Aspose.Cells.License license = new Aspose.Cells.License();

license.SetLicense(myStream);

{{< /highlight >}}

### **How to Apply Metered License**

Aspose.Cells allows developers to to apply a metered key. It is a new licensing mechanism. The new licensing mechanism will be used along with the existing licensing method. Those customers who want to be billed based on the usage of the API features can use the metered licensing. For more details, please refer to [Metered Licensing FAQ](https://purchase.aspose.com/faqs/licensing/metered) section.  

A new class [Metered](https://reference.aspose.com/cells/net/aspose.cells/metered) has been introduced to apply a metered key. Following is the sample code demonstrating how to set metered public and private key.

{{< highlight csharp >}}

 //Set metered public and private keys

Metered metered = new Metered();

//Access the setMeteredKey method and pass public and private keys as parameters

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

### **How to Use an Embedded Resource**

Another neat way of packaging the license with your application and making sure it will not be lost, is to include it as an embedded resource into one of the assemblies that calls Aspose.Cells. To include the license file as an embedded resource, perform the following steps:

1. In Visual Studio .NET, include the license (.lic) file into the project by selection **Add Existing Item** from the **File** menu.
1. Select the file in the Solution Explorer and set **Build Action** to **Embedded Resource** in the Properties window

To access the license embedded in the assembly (as embedded resource), it is not needed to call GetExecutingAssembly and GetManifestResourceStream methods of System.Reflection.Assembly class of Microsoft .NET Framework. All is needed to do, is to just add the license file as an embedded resource to your project and pass the name of the license file into SetLicense method. The **Aspose.Cells.License** class will automatically find the license file in the embedded resources. Please review the example given below to understand this method of setting license (embedded) in your applications.

{{< highlight csharp >}}

 //Instantiate the License class

Aspose.Cells.License license = new Aspose.Cells.License();

//Pass only the name of the license file embedded in the assembly

license.SetLicense("Aspose.Cells.lic");

{{< /highlight >}}

## **How to Set License in Aspose.Cells Grid Controls**

In Aspose.Cells Grid Suite, license can be loaded from a file, stream or an embedded resource. Aspose.Cells.GridDesktop / Aspose.Cells.GridWeb tries to find the license in the following locations:

1. Explicit path
1. The folder that contains the dll of the component (included in Aspose.Cells.GridDesktop or Aspose.Cells.GridWeb)
1. The folder that contains the assembly that called the dll of the component (included in Aspose.Cells.GridDesktop or Aspose.Cells.GridWeb)
1. The folder that contains the entry assembly (your .exe)
1. An embedded resource in the assembly that called the dll of the component (included in Aspose.Cells.GridDesktop or Aspose.Cells.GridWeb)

{{% alert color="primary" %}}

If you are using Aspose.Cells.GridDesktop control then the license class will be used as Aspose.Cells.GridDesktop.License but if you are using Aspose.Cells.GridWeb control then Aspose.Cells.GridWeb.License class will be used to set the license.

{{% /alert %}}

### **How to Apply a License from Disk or Stream**

The easiest way to set a license, is to put the license file in the same folder as that of the dll of the component (included in Aspose.Cells.GridWeb) and specify just the file name without its path.

{{< highlight csharp >}}

//Instantiate an instance of license and set the license file through its path

Aspose.Cells.GridWeb.License license = new Aspose.Cells.GridWeb.License();

license.SetLicense("MyLicense.lic");

{{< /highlight >}}

{{% alert color="primary" %}}

When you call SetLicense method, the license name should be same as that of your license file name. For example, you may change the license file name to "MyLicense.lic.xml". Then in your code, you should use the modified license name (that is MyLicense.lic.xml) for the SetLicense method.

{{% /alert %}}

It is also possible to load a license from a stream.

{{< highlight csharp >}}

//Instantiate an instance of license and set the license through a stream

Aspose.Cells.GridWeb.License license = new Aspose.Cells.GridWeb.License();

license.SetLicense(myStream);

{{< /highlight >}}

### **How to Apply a License as an Embedded Resource**

Another neat way of packaging the license with your application and making sure it will not be lost, is to include it as an embedded resource into one of the assemblies that calls the dll of the component (included in Aspose.Cells.GridDesktop). To include the license file as an embedded resource, perform the following steps:

1. In Visual Studio .NET, include the license (.lic) file into the project using the **Add Existing Item** option on the **File** menu.
1. Select the file in the Solution Explorer and set Build Action to Embedded Resource in the Properties window.
1. To access the license embedded in the assembly (as embedded resource), it is not needed to call the GetExecutingAssembly and GetManifestResourceStream methods of the System.Reflection.Assembly class of Microsoft .NET Framework.Instead, add the license file as an embedded resource in your project and pass the name of the license file into the SetLicense method. The License class automatically finds the license file in the embedded resources.

Please review the example given below to understand this method of applying a license as an embedded resource to your applications.

{{< highlight csharp >}}

 //Instantiate the License class

Aspose.Cells.GridDesktop.License license = new Aspose.Cells.GridDesktop.License();

//Pass only the name of the license file embedded in the assembly

license.SetLicense("Aspose.Total.lic");

{{< /highlight >}}

## **How to Apply a License in Aspose.Cells.GridDesktop for a WinForm Application**

It's recommended that you should put your licensing code before your application starts and apply it only once. For example, for a windows C# application, put the licensing code in the Main method.

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

## **Notes on Applying a License in Aspose.Cells.GridWeb**

It's recommended to put the licensing code in the Global.asax.cs of your web application (this license file is assumed to be put on the " d:\ " drive):

{{< highlight csharp >}}

 protected void Application_Start(Object sender, EventArgs e)

{

    Aspose.Cells.GridWeb.License lic = new Aspose.Cells.GridWeb.License();

    lic.SetLicense(@"d:\Aspose.Cells.GridWeb.lic.xml");

}

{{< /highlight >}}

Loading a License from a Stream

{{< highlight csharp >}}

 protected void Application_Start(Object sender, EventArgs e)

{

    Aspose.Cells.GridWeb.License lic = new Aspose.Cells.GridWeb.License();

    lic.SetLicense(myStream);

}

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
