---
title : "Installation" 
description : "" 
weight : 12035 
toc : false
type: docs
url: /net/gettingstarted/installationanddeployment/installation/
---

# Aspose.Cells for .NET : Installation


{{< panel title="Contents Summary" style="primary" >}}
*   1 [Install Aspose.Cells for .NET through NuGet](#install-aspose.cells-for-.net-through-nuget)
    *   1.1 [Install Aspose.Cells using Package Manager GUI](#install-aspose.cells-using-package-manager-gui)
    *   1.2 [Install Aspose.Cells using the Package Manager Console](#install-aspose.cells-using-the-package-manager-console)
*   2 [Referencing Aspose.Cells from a .NET Project](#referencing-aspose.cells-from-a-.net-project)
    *   2.1 [Referencing the component from a VS.NET 2010 Client Profile project](#referencing-the-component-from-a-vs.net-2010-client-profile-project)
*   3 [Referencing Aspose.Cells Grid Controls from a .NET project](#referencing-aspose.cells-grid-controls-from-a-.net-project)
*   4 [Uninstalling Aspose.Cells for .NET](#uninstalling-aspose.cells-for-.net)
{{< /panel >}}
 

 

## Install Aspose.Cells for .NET through NuGet

NuGet is the easiest way to download and install Aspose APIs for .NET. Open Microsoft Visual Studio and NuGet package manager. Search "aspose" to find the desired Aspose API. Click on "Install", the selected API will be downloaded and referenced in your project.

### Install Aspose.Cells using Package Manager GUI

Follow these steps to reference the Aspose.Cells component using package manager GUI:

*   Open your solution/project in Visual Studio.
*   Click **Tools** -> **Library Package Manager** -> **Manage NuGet Packages** from Solution. You can also easily access the same option by through the Solution Explorer. Right-click the solution or project and select **Manage NuGet Packages** from context menu.
*   Select **Online** from the left hand menu and type “Aspose.Cells” in the search text box to find the Aspose.Cells .NET package.
*   Click the **Install** button next to the Aspose.Cells for .NET entry to install the latest version into your project.

### Install Aspose.Cells using the Package Manager Console

You can follow the steps below to reference the Aspose.Cells component using the package manager console:

*   Open your solution/project in Visual Studio.
*   Select **Tools** -> **Library Package Manager** -> **Package Manager Console** from the menu to open package manager console.
    *   Type the command “Install-Package Aspose.Cells” and press enter to install latest full release into your application. Alternatively you can add the "-prerelease" suffix to the command in order to specify that the latest release including hot fixes is to be installed as well.
*   You will see that the "Downloading Aspose.Cells..." tip appears down the bottom left of the window indicating that the download is process.
*   Once downloaded you will see the following confirmation messages. If you are not farmilar with the Aspose EULA then it is a good idea to read the license referenced in the URL.
*   You should now find that Aspose.Cells has successfully been added and referenced in your application for you.

## Referencing Aspose.Cells from a .NET Project

In order to use Aspose.Cells in an application, add a reference to it. To add a reference using Visual Studio:

1.  In the **Solution Explorer**, expand the project node you want to add a reference to.
2.  Right-click the **References** node for the project and select **Add Reference** from the menu.
3.  In the **Add Reference** dialog box, select the .NET tab (selected by default). If you installed using the MSI installer, Aspose.Cells will appear in the top pane.
4.  Select it and click **Select**.

If you have downloaded or unpacked the DLL only:

1.  Locate the Aspose.Cells.dll file using the **Browse** button. Aspose.Cells should appear in the **Selected Components** pane of the dialog box.
2.  Click **OK**. The Aspose.Cells reference appear under the **References** node of the project.

### Referencing the component from a VS.NET 2010 Client Profile project

If your project's Target framework is .NET Framework 3.5/4 Client Profile, use the Aspose.Cells.dll component file located in the net\_ClientProfile folder of your installation directory. For example:

*   In **Solution Explorer** of VS.NET 2010 for your project, right-click **References** and select **Add Reference**.
*   Select the **Browse** tab in the dialog and click Look for dropdown.
*   Find and select the Aspose.Cells.dll component file in your installation directory, for example: .../Program Files/Aspose/Aspose.Cells for .NET/Bin/net\_ClientProfile/ **(Make sure that you installed the product using the MSI installer on your machine.)**
*   Click **OK** to close the dialog

If your VS.NET 2010 project's target framework is ".NET Framework 4" or other, then simply use the Aspose.Cells.dll component file located in net4.0/net2.0 folder.

## Referencing Aspose.Cells Grid Controls from a .NET project

To use a grid control in your application, add a reference to it. To reference a grid control in Visual studio do the following:

*   In **Solution Explorer**, expand the project node you want to add a reference to.
*   Right-click the **References** node for the project and select **Add Reference** from the menu.
*   In the **Add Reference** dialog box, select the **.NET tab** (selected by default). If you have used MSI installer to install Aspose.Cells for .NET, Aspose.Cells.GridDesktop and Aspose.Cells.GridWeb appear in the top pane.
*   Select them and click **Select**.
*   The Aspose.Cells.GridDesktop and Aspose.Cells.GridWeb references appears under the References node of the project.

If you downloaded and unpacked the DLL only:

*   Locate the Aspose.Cells.GridDesktop.dll and Aspose.Cells.GridWeb.dll files using the Browse button. Aspose.Cells Grid Suite has been referenced and should appear in the **Selected Components** pane of the dialog box.
*   Click **OK.**

## Uninstalling Aspose.Cells for .NET

If you have used MSI installer to deploy Aspose.Cells for .NET, follow these steps to completely remove the component and the controls, the associated demos and documentations:

*   From the **Start** menu, select **Settings**, followed by **Control Panel**.
*   Click **Add/Remove Programs**.
*   Select Aspose.Cells for .NET (version).
*   Click **Change/Remove** to remove Aspose.Cells.

## Attachments:

![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Referencing Aspose.Cells for .NET.png](https://docs2.aspose.com/cells/net/attachments/5024995/5115501.png) (image/png)  

