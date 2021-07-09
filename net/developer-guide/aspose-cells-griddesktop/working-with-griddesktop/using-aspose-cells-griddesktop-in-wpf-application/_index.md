---
title: Using Aspose.Cells.GridDesktop in WPF Application
type: docs
weight: 50
url: /net/using-aspose-cells-griddesktop-in-wpf-application/
---

{{% alert color="primary" %}} 

This article demonstrates how to use the Windows Presentation Foundation (WPF) Designer for Visual Studio to host a Windows Forms control such as Aspose.Cells.GridDesktop in a WPF application. 
We will be using Visual Studio 2015 to demonstrate the process, however, you can use any version including Visual Studio 2008 or later.

{{% /alert %}} 

This tutorial will walk you through the process of adding Aspose.Cells.GridDesktop control to a WPF application. You need any version of the Visual Studio IDE that supports WPF development in order to try this on your side.
## **Create a WPF application using Visual Studio**
First create a WPF application using Visual Studio IDE. Click on **File** >> **New** >> **Project** menu and select **WPF Application** from Templates, name the project and click **OK**. You can target your project to any .NET Framework higher than 2.0, however, you cannot use client profile .NET Frameworks.
## **Add references to required namespaces**
Add the references to the following assemblies by right clicking the References from Solution Explorer window and select Add Reference menu.

- WindowsFormsIntegration assembly (WindowsFormsIntegration.dll).
- Windows Forms assembly (System.Windows.Forms.dll).
- Aspose.Cells.GridDesktop assembly (Aspose.Cells.GridDesktop.dll).

This action adds the required assemblies to the application, that is; copies the assemblies to the the Bin folder of the application.
## **Add references to XAML**
Next, go to the XAML file and add the following namespaces and assembly references within the Windows tag.

{{< highlight java >}}

 xmlns:wf="clr-namespace:System.Windows.Forms;assembly=System.Windows.Forms"

xmlns:gridDesktop="clr-namespace:Aspose.Cells.GridDesktop;assembly=Aspose.Cells.GridDesktop">

{{< /highlight >}}

**The final Windows tag will look similar to as shown below.**

![todo:image_alt_text](using-aspose-cells-griddesktop-in-wpf-application_1.png)
## **Add Aspose.Cells.GridDesktop control to XAML**
Simply add the below code inside the Grid tag in XAML. The **WindowsFormsHost** tag is used to host Windows Forms control and **gridDesktop:GridDesktop** tag represents the Aspose.Cells.GridDesktop control. You can also name the control so that it can be referenced easily in the code.

{{< highlight java >}}

 <WindowsFormsHost Loaded="FrameworkElement_OnLoaded">

    <WindowsFormsHost.Child>

        <gridDesktop:GridDesktop x:Name="grid" />

    </WindowsFormsHost.Child>

</WindowsFormsHost>

{{< /highlight >}}

**The final XAML will look as follow.** 

![todo:image_alt_text](using-aspose-cells-griddesktop-in-wpf-application_2.png)
## **Use Aspose.Cells.GridDesktop**
We can now access & use Aspose.Cells.GridDesktop control in the .cs file as any other Windows Forms applications. In order to keep the demonstration simple, we are just loading a sample spreadsheet in the Aspose.Cells.GridDesktop control and saving it back. Moreover, we have used the FrameworkElement_OnLoaded event to trigger the following statements.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-UsingGridDesktopInWpf-MainWindow.xaml-UsingGridDesktopInWpf.cs" >}}
## **Build & Run**
Now, build and run the application using **F5** or **Start** button on the Visual Studio UI.
