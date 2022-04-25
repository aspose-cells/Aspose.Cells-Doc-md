---
title: How to use Aspose.Cells.GridWeb with .NET Core
type: docs
weight: 40
url: /net/how-to-use-aspose-cells-gridweb-with-net-core/
---

{{% alert color="primary" %}} 

This topic explains how to use Aspose.Cells.GridWeb with .NET Core applications using Visual Studio.NET 2019. This topic is useful for the beginner-level developers working with Aspose.Cells.GridWeb.

{{% /alert %}} 
## **Use Aspose.Cells.GridWeb with .NET Core**
This topic shows how to use Aspose.Cells.GridWeb by making a sample website in Visual Studio 2019. The process has been divided into steps.
### **Step 1: Creating a New Project**
1. Open Visual Studio 2019.
1. From the **File** menu, select **New**, then **Project**.
   Create a new project dialog is opened.
1. Select **ASP.NET Core Web Application** from Visual Studio installed project templates and click **Next**.

![todo:image_alt_text](how-to-use-aspose-cells-gridweb-with-net-core_1.jpg)

1. Specify a location where the location and the name of the project and click **Create**.

![todo:image_alt_text](how-to-use-aspose-cells-gridweb-with-net-core_2.jpg)

1. Select the **Web Application (Model-View-Controller)** template and make sure that **ASP .NET Core 2.1** is selected. 

![todo:image_alt_text](how-to-use-aspose-cells-gridweb-with-net-core_3.jpg)

1. Click **Create**.
### **Step 2: Checking the initial view**
Running the newly created project shows the default template in the browser as shown in the image below.



![todo:image_alt_text](how-to-use-aspose-cells-gridweb-with-net-core_4.jpg)
### **Step 3: Adding Aspose.Cells.GridWeb**
1. Add the following Nuget Packages to the project

<PackageReference Include="Microsoft.AspNetCore.App" />
<PackageReference Include="Microsoft.AspNetCore.Razor.Design" Version="2.1.2" PrivateAssets="All" />
<PackageReference Include="Newtonsoft.Json" Version="12.0.3" />
<PackageReference Include="System.Drawing.Common" Version="4.7.0" />
<PackageReference Include="System.Text.Encoding.CodePages" Version="4.7.0" />

1. Add Aspose.Cells.GridWeb Package

![todo:image_alt_text](how-to-use-aspose-cells-gridweb-with-net-core_5.jpg)

1. Add the following to the **_ViewImports.cshtml** file in the Views folder.
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "GridWebCore-ViewImports.cs" >}}

The file will look like this after the modifications

![todo:image_alt_text](how-to-use-aspose-cells-gridweb-with-net-core_6.jpg)

1. Put the following code in the HomeController's Index method.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "GridWebCore-HomeController.cs" >}}

{{% alert color="primary" %}} 

Remember to update the SessionStorePath and the ImportExcelFile path.

{{% /alert %}} 

![todo:image_alt_text](how-to-use-aspose-cells-gridweb-with-net-core_7.jpg)

1. Add the following code in the **Index.cshtml** file in the View > Home directory.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "GridWebCore-IndexView.cs" >}}

The file will look like this after the change.

![todo:image_alt_text](how-to-use-aspose-cells-gridweb-with-net-core_8.jpg)

1. Add Session support and GridScheduedService in the Startup.cs file
   1. Add the following code snippet in the ConfigureServices method.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "GridWebCore-Startup1.cs" >}}

![todo:image_alt_text](how-to-use-aspose-cells-gridweb-with-net-core_9.jpg)

1. Add the following code snippet in the Configure method.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "GridWebCore-Startup2.cs" >}}

![todo:image_alt_text](how-to-use-aspose-cells-gridweb-with-net-core_10.jpg)

1. Put the latest acw_client in directory: **wwwroot/js** {{% alert color="primary" %}}   {{% /alert %}}
1. Add **AcwController** in Controllers to deal with the acw route map that can provide all the default operations for general edit action.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "GridWebCore-AcwController.cs" >}}

![todo:image_alt_text](how-to-use-aspose-cells-gridweb-with-net-core_11.jpg)
### **Step 4: Test the App**
Running the app will the output similar to the one shown in the image below.

![todo:image_alt_text](how-to-use-aspose-cells-gridweb-with-net-core_12.jpg)
