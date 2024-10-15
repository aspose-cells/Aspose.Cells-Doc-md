---
title: Using Aspose.Cells on 32-bit and 64-bit Platforms
type: docs
weight: 10
url: /net/using-aspose-cells-on-32-bit-and-64-bit-platforms/
---

{{% alert color="primary" %}} 

Aspose.Cells is a pure .NET component that can simplify your deployment process by using XCOPY deployment. To install Aspose.Cells, you can simply copy the component assembly (Aspose.Cells.dll) into a directory for your application: the application can start using it right away. This is possible because of the self-describing nature of .NET components. This type of deployment has also zero-impact on the installation process.

{{% /alert %}} 
## **Deployment**
Aspose.Cells supports both 32-bit and 64-bit environments. When you install Aspose.Cells for .NET component using Aspose.Cells MSI installer, different DLLs are added to different folders in the Aspose.Cells ${installation_Path} folder(s). See the description in the table what folder contains the assemblies you need to use with a particular version of the .NET Framework.

|**Folder**|**Description**|
| :- | :- |
|net2.0|Contains assemblies to use with .NET Framework 2.0, 3.0, 3.5, 4.0 and Mono. These are the assemblies that you should normally use for both 32-bit and 64-bit environments.|
|net2.0_AuthenticodeSigned|Same as above, but the assemblies are digitally signed with Authenticode. Signed assemblies may load slower than without Authenticode|
|net3.5_ClientProfile|Contains assemblies to use with .NET Framework 3.5 or 4.0 Client Profile.|
|net3.5_ClientProfile_AuthenticodeSigned|Same as above, but the assemblies are digitally signed with Authenticode. Signed assemblies may load slower than without Authenticode.|
|net3.5|Contains assemblies to use with .NET Framework 3.5 or 4.0.|
|net3.5_AuthenticodeSigned|Same as above, but the assemblies are digitally signed with Authenticode. Signed assemblies may load slower than without Authenticode.|
|net4.0|Contains assemblies to use with .NET Framework 4.0 and 4.5.|
|netStandard|Contains assemblies to use with .Net Standard 2.0|
|netcoreapp2.1|Contains assemblies to use with .Net core 2.1|
|Xamarin.iOS|Contains assemblies to use with Xamarin.iOS|
|Xamarin.Android|Contains assemblies to use with Xamarin.Android|
|net5.0|Contains assemblies to use with .net5.0.|
|net6.0|Contains assemblies to use with .net6.0.|
{{% alert color="primary" %}} 

In VS.NET (for example 2005, 2008, 2010, 2012 etc.) projects, when adding a reference to Aspose.Cells, the Add Reference dialog refers to Aspose.Cells.dll files in the net2.0 or  net3.5 folder(s) respectively. (For further reference, read Referencing Aspose.Cells from a .NET project.) You can change the reference to the library according to your environment. Please note if the project's target framework is .NET Framework 3.5/4 Client Profile, use the Aspose.Cells.dll component file located in net_ClientProfile folder.

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}