---
title: Getting Started
type: docs
weight: 10
url: /net/getting-started/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}} 

This page will show you how to install Aspose Cells and create a Hello World application.

{{% /alert %}}

## **Installation**

### **Install Aspose.Cells through NuGet**

NuGet is the easiest way to download and install Aspose.Cells for .NET. 

1. Open Microsoft Visual Studio and the NuGet package manager.  
2. Search "Aspose.Cells" to find the desired Aspose.Cells for .NET.  
3. Click "Install". Aspose.Cells for .NET will be downloaded and referenced in your project.  
**![Install Aspose Cells through NuGet](install-through-nuget.png)**

You can also download it from the NuGet web page for Aspose.Cells:  
[Aspose.Cells for .NET NuGet Package](https://www.nuget.org/packages/Aspose.Cells/)

[More steps for details](/cells/net/installation/)

### **Install Aspose.Cells on Windows**

1. Download Aspose.Cells.msi from the following page:  
[Download Aspose.Cells.msi](https://downloads.aspose.com/cells/net/)  
2. Double‑click the Aspose.Cells.msi and follow the instructions to install it:

**![Install Aspose Cells on windows](install-on-windows.png)**

[More steps for details](/cells/net/installing-aspose-cells-on-windows/)

### **Install Aspose.Cells on Linux**

In this example, I use Ubuntu to show how to start using Aspose.Cells on Linux.

1. Create a .NET Core application, named **AsposeCellsTest**.  
2. Open the file **AsposeCellsTest.csproj** and add the following lines to it for Aspose.Cells package references:
{{< highlight plain >}}
  <ItemGroup>
    <PackageReference Include="Aspose.Cells" Version="26.1" />
  </ItemGroup>
{{< /highlight >}}
3. Open the project with VS Code on Ubuntu:  
**![Install Aspose Cells on linux](install-on-linux.png)**
4. Run the test with the following code:
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-StartOnLinux.cs" >}}

Note: Aspose.Cells for .NET Standard can support your requirement on Linux.

Applies to: .NET Standard 2.0, .NET Core 2.1, .NET Core 3.1, .NET 5.0, .NET 6.0 and later versions.

### **Install Aspose.Cells on macOS**

In this example, I use macOS High Sierra to show how to start using Aspose.Cells on macOS.

1. Create a .NET Core application, named **AsposeCellsTest**.  
2. Open the application with Visual Studio for Mac, then install Aspose.Cells through NuGet:  
**![Install Aspose Cells on macOS](install-on-mac-os.png)**
3. Run the test with the following code:
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-StartOnMacOS.cs" >}}
4. If you need to use drawing‑related features, please install **libgdiplus** on macOS. See:  
[How to Install libgdiplus in macOS](/cells/net/how-to-install-libgdiplus-in-macos/)

Note: Aspose.Cells for .NET Standard can support your requirement on macOS.

Applies to: .NET Standard 2.0, .NET Core 2.1, .NET Core 3.1, .NET 5.0, .NET 6.0 and later versions.

### [**Run Aspose Cells in Docker**](/cells/net/how-to-run-aspose-cells-in-docker/)

### **How to use a graphics library on non‑Windows platforms with .NET 6**

Aspose.Cells for .NET 6 now uses SkiaSharp as the graphics library, as recommended in the official Microsoft statement. For more details about using Aspose.Cells with .NET 6, please see [How to Run Aspose.Cells for .NET 6](/cells/net/how-to-run-aspose-cells-for-net6/).

## **Creating the Hello World Application**

The steps below create the Hello World application using the Aspose.Cells API:

1. If you have a license, then [apply it](/cells/net/licensing/).  
   If you are using the evaluation version, skip the license‑related code lines.  
2. Create an instance of the [Workbook](https://reference.aspose.com/cells/net/aspose.cells/workbook) class to create a new Excel file or open an existing Excel file.  
3. Access any desired cell of a worksheet in the Excel file.  
4. Insert the words **Hello World!** into the accessed cell.  
5. Generate the modified Microsoft Excel file.

The implementation of the above steps is demonstrated in the examples below.

### **Code Sample: Creating a New Workbook**

The following example creates a new workbook from scratch, inserts **Hello World!** into cell **A1** in the first worksheet, and saves it as an Excel file.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Introduction-FirstApplication-1.cs" >}}

### **Code Sample: Opening an Existing File**

The following example opens an existing Microsoft Excel template file **Sample.xlsx**, inserts **Hello World!** into cell **A1** in the first worksheet, and saves it as an Excel file.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Introduction-OpenExistingFile-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
