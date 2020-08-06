---
title: Integrate Aspose.Cells Grid Controls with Visual Studio.NET
type: docs
weight: 10
url: /net/integrate-aspose-cells-grid-controls-with-visual-studio-net/
---

{{% alert color="primary" %}} 

Visual Studio.NET developers can easily drag controls from the **Toolbox** onto a Windows or Web form. Aspose.Cells Grid suite can be downloaded with an MSI installer, or as a set of DLLs package. This articles explains what to do to make sure that Aspose.Cells.Grid controls can be used in Visual Studio.NET when its installed using the DLLs instead of the installer.

{{% /alert %}} 
## **Integrate Aspose.Cells Grid Controls with Visual Studio.NET**
To integrate Aspose.Cells Grid controls with Visual Studio.NET:

1. Open the Toolbox.
1. Select the General tab (or any other tab you want to add controls to).
1. Right-click the General tab.
1. On Visual Studio.NET 2003: Select **Add/Remove Items** from the menu.
1. On Visual Studio.NET 2005, select **Choose Items** from the menu. The Customize Toolbox dialog will be appeared (This process is is more or less the same for newer VS.NET IDEs (e.g VS.NET 2013/2015 or later)).
1. Click **Browse** and locate the Aspose.Cells.GridDesktop.dll and Aspose.Cells.GridWeb.dll files.
1. Select the DLLs and then click **Open**. The Customize Toolbox dialog will now contain controls from Aspose.Cells Grid Suite. The newly added controls will be highlighted by the dialog.
1. Click **OK** to add the controls to your Visual Studio.NET Toolbox.

the Aspose.Cells Grid Controls will have been added to the Toolbox's **General** tab. Only the GridWeb control is not active. This is because we are working on a Windows Forms application. GridWeb is only available when you are working on Web Forms whereas GridDesktop can be used with Windows forms only.
