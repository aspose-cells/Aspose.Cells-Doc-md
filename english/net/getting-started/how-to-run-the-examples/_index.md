---
title: How to Run the Examples
type: docs
weight: 140
url: /net/how-to-run-the-examples/
---

## **Software Requirements**
Please make sure you meet the following requirements before downloading and running the examples.

1. Visual Studio 2015 or higher
1. NuGet Package Manager installed in Visual Studio. It is mostly already installed in Visual Studio 2015. For details on how to install NuGet package manager please check: [Installing NuGet client tools](https://docs.microsoft.com/en-us/nuget/install-nuget-client-tools)
1. Go to Tools->Options->NuGet Package Manager->Package Sources and make sure that the option **nuget.org** is checked
1. Example project uses NuGet Automatic Package Restore feature therefore you should have an active internet connection. If you do not have an active internet connection on the machine where examples are to be executed please check [Installation](/cells/net/installation-and-deployment/) and manually add reference to Aspose.Cells.dll in the example project.
## **Download from GitHub**
All examples of Aspose.Cells for .NET are hosted on [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET).
## **Aspose.Cells Examples**
- You can either clone the repository using your favorite GitHub client or download the ZIP file from [here](https://github.com/aspose-cells/Aspose.Cells-for-.NET/archive/master.zip).
- Extract the contents of ZIP file to any folder on your computer. All the examples are located in the **Examples** folder.
- There is a Visual Studio solution file for C# Examples i.e. **Aspose.Cells.Examples.CSharp.sln**.
- The project is created and maintained in Visual Studio 2015.
- Open the solution file in Visual Studio and build the project.
- On first run, the dependencies will automatically be downloaded via NuGet. You may also download the DLLs separately from [here](https://downloads.aspose.com/cells/net).
- **Data** folder at the root folder of **Examples** contains input files which CSharp examples used. It is mandatory that you download the **Data** folder along with the examples project.
- Open **RunExamples.cs**, all the examples are called from here.
- Uncomment the examples you want to run from within the project.
## **Aspose.Cells.GridDesktop Examples**
- Aspose.Cells.GridDesktop examples are also included in [Aspose.Cells GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET) repository and will be available as part of the ZIP file downloadable from [here](https://github.com/aspose-cells/Aspose.Cells-for-.NET/archive/master.zip).
- All examples are located in **Examples_GridDesktop** folder.
- Similar to Aspose.Cells examples, GridWeb examples solution file name is **Aspose.Cells.GridDesktop.Examples.CSharp.sln**.
- Open the solution file in Visual Studio and build the project.
- All dependencies are included as part of the examples project. You may also download the DLLs separately from [here](https://downloads.aspose.com/cells/net).
- **Data** folder at the root folder of **Examples_GridDesktop** contains input files used by examples. It is mandatory that you download the **Data** folder along with the examples project.
- Open and run the project.
- Click on the example in the menu that you want to run from within the form.
## **Aspose.Cells.GridWeb Examples**
- Aspose.Cells.GridWeb examples are also included in [Aspose.Cells GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET) repository and will be available as part of the ZIP file downloadable from [here](https://github.com/aspose-cells/Aspose.Cells-for-.NET/archive/master.zip).
- All examples are located in **Examples_GridWeb** folder.
- Similar to Aspose.Cells examples, GridWeb examples solution file name is **Aspose.Cells.GridWeb.Examples.CSharp.sln**.
- Open the solution file in Visual Studio and build the project.
- All dependencies are included as part of the examples projects. You may also download the DLLs separately from [here](https://downloads.aspose.com/cells/net).
- **Data** folder at the root folder of **Examples_GridWeb** contains input files used by examples. It is mandatory that you download the **Data** folder along with the examples project.
- Open and run **Examples.aspx** in the examples project.
- Click on the example in the browser that you want to run from within the project.
{{< app/cells/assistant language="csharp" >}}